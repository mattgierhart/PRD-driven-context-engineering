#!/usr/bin/env python3
"""
readiness.py — orchestrator for PRD-CE readiness scoring

Composes three scoring layers into a single report:

  SoT files    — per-file quality (entries, depth, cross-refs, orphans)
  EPICs        — build-readiness per work package, cites SoT root causes
  PRD stage    — can we advance v0.X → v0.Y? Composes SoT + EPIC scores

All layers write to <repo>/status/readiness.json. Causal links connect
the layers: an EPIC's score points at the SoT file blocking it; the SoT
file's block lists which EPICs depend on it; the stage score composes
both.

Usage:
  readiness.py run                # compute all layers, print report
  readiness.py status             # print report from existing readiness.json
  readiness.py run --json         # emit raw readiness.json to stdout

Options:
  --repo <path>    Repo root (default: cwd or autodetect)
  --json           Emit JSON instead of the text report
  --quiet          Suppress output; use exit code only
  --gate <vX.Y>    Override target gate for stage scoring
  --threshold <N>  Pass/warn threshold (default 70)

Exit codes:
  0  stage + all EPICs passing (score ≥ threshold)
  1  at least one item in WARN band (score ≥ block, < warn)
  2  at least one item in BLOCK band (score < block)
  3  runtime error
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SOT_SCRIPT = SCRIPT_DIR / "compute-sot-readiness.py"
EPIC_SCRIPT = SCRIPT_DIR / "compute-readiness.py"
STAGE_SCRIPT = SCRIPT_DIR / "compute-prd-readiness.py"

BLOCK_THRESHOLD = 50
DEFAULT_WARN_THRESHOLD = 70


# ---------- Execution pipeline ---------- #

def find_repo_root(start: Path) -> Path:
    p = start.resolve()
    if p.is_file():
        p = p.parent
    while p != p.parent:
        if (p / "PRD.md").is_file() or (p / "SoT").is_dir() or (p / "epics").is_dir():
            return p
        p = p.parent
    raise SystemExit("error: could not find repo root (no PRD.md, SoT/, or epics/ found)")


def run_script(script: Path, args: list[str], cwd: Path, quiet: bool) -> int:
    """Invoke a child script. Silence stdout unless --verbose is passed down."""
    cmd = [sys.executable, str(script), *args]
    if quiet:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    else:
        result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.DEVNULL, text=True)
    if result.returncode != 0 and not quiet:
        print(f"warning: {script.name} exited {result.returncode}", file=sys.stderr)
        if result.stderr:
            sys.stderr.write(result.stderr)
    return result.returncode


def compute_all(repo: Path, gate_override: str | None, quiet: bool) -> None:
    """Run the three scorers in dependency order: SoT → EPIC → Stage."""
    # 1. SoT (primitive — others read its output)
    run_script(SOT_SCRIPT, ["all"], repo, quiet)

    # 2. EPICs (one per file, each merged into readiness.json)
    epics_dir = repo / "epics"
    pilot_inputs = repo / "temp" / "epic-01-readiness-inputs.yaml"
    if epics_dir.is_dir():
        for epic in sorted(epics_dir.glob("EPIC-*.md")):
            if epic.name == "EPIC_TEMPLATE.md":
                continue
            args = [str(epic), "--merge"]
            # Temporary pilot hook: if the EPIC has no readiness_inputs and
            # a sibling temp file exists, load it. Drops away once frontmatter
            # adoption lands.
            if epic.name.startswith("EPIC-01") and pilot_inputs.is_file():
                args.extend(["--inputs", str(pilot_inputs)])
            run_script(EPIC_SCRIPT, args, repo, quiet)

    # 3. Stage (reads SoT + EPIC scores to compose)
    stage_args: list[str] = []
    if gate_override:
        stage_args.extend(["--gate", gate_override])
    run_script(STAGE_SCRIPT, stage_args, repo, quiet)


# ---------- Report formatting ---------- #

def band(score: float, warn: int, block: int = BLOCK_THRESHOLD) -> str:
    if score >= warn:
        return "PASS"
    if score >= block:
        return "WARN"
    return "BLOCK"


def band_marker(score: float, warn: int) -> str:
    b = band(score, warn)
    return {"PASS": "✓", "WARN": "~", "BLOCK": "✗"}[b]


def hr(char: str = "─", width: int = 72) -> str:
    return char * width


def format_report(readiness: dict, repo_name: str, warn: int) -> str:
    lines: list[str] = []
    lines.append(hr("━"))
    lines.append(f"  PRD Readiness — {repo_name}")
    lines.append(f"  {readiness.get('last_computed', 'n/a')}")
    lines.append(hr("━"))
    lines.append("")

    summary = readiness.get("summary", {})

    # STAGE section
    stages = readiness.get("stages", {})
    if stages:
        lines.append("STAGE")
        for gate, stage in sorted(stages.items()):
            b = band(stage["score"], warn)
            lines.append(f"  {gate}  score={stage['score']:<5}  [{b}]   {stage['gate_description']}")
            unmet = stage.get("unmet_criteria", [])
            if unmet:
                high = [u for u in unmet if u.get("severity") == "high"]
                for u in high[:3]:
                    reason = u["reason"][:80] + ("..." if len(u["reason"]) > 80 else "")
                    lines.append(f"    • [high] {reason}")
                if len(high) > 3:
                    lines.append(f"    • ... and {len(high) - 3} more high-severity")
        lines.append("")

    # EPIC section
    epics = readiness.get("epics", {})
    if epics:
        passing = sum(1 for e in epics.values() if e["score"] >= warn)
        lines.append(f"EPICs  ({passing}/{len(epics)} passing)")
        # Sort by score ascending — worst first
        sorted_epics = sorted(epics.items(), key=lambda kv: kv[1]["score"])
        shown = 0
        for eid, e in sorted_epics:
            marker = band_marker(e["score"], warn)
            cap_rules = ",".join(c.get("rule", "") for c in e.get("caps", []))
            suffix = f"  [{cap_rules}]" if cap_rules else ""
            if e["score"] < warn or shown < 3:
                lines.append(f"  {marker} {eid}  score={e['score']:<5}  [{band(e['score'], warn)}]{suffix}")
                shown += 1
        if shown < len(epics):
            lines.append(f"    (+ {len(epics) - shown} more passing)")
        lines.append("")

    # SoT LEVERAGE section
    sot_files = readiness.get("sot_files", {})
    blockers = summary.get("top_blockers", [])
    if sot_files:
        lines.append(f"SoT FILES  ({summary.get('sot_files_passing', 0)}/{summary.get('sot_files_total', len(sot_files))} passing)")
        if blockers:
            lines.append("  Top blockers (impact = (100-score) × #blocked EPICs):")
            for b in blockers[:5]:
                file_short = b["file"].replace("SoT/", "")
                lines.append(f"    [{b['score']:>4}] {file_short:<34} blocks {b['blocks']:>2} EPIC(s)  impact={b['impact']:>5.0f}")
        else:
            lines.append("  No blockers — all SoT files passing.")
        lines.append("")

    # NEXT ACTIONS — the leverage view translated into a punch list
    if blockers:
        lines.append("NEXT ACTIONS  (highest leverage first)")
        for i, b in enumerate(blockers[:3], 1):
            file_short = b["file"].replace("SoT/", "")
            consumers = b.get("blocking_epics", [])
            consumer_str = f"{consumers[0]} and {len(consumers) - 1} others" if len(consumers) > 1 else consumers[0]
            action = f"Populate {file_short}" if b["score"] == 0 else f"Raise {file_short} above {warn}"
            lines.append(f"  {i}. {action} — unblocks {consumer_str}")
        lines.append("")

    # Overall verdict
    current = summary.get("current_stage", {})
    if current:
        verdict_band = band(current["score"], warn)
        lines.append(hr())
        lines.append(f"  Current gate ({current['target']}): {current['score']}  [{verdict_band}]")
        lines.append(hr())

    return "\n".join(lines)


def overall_exit_code(readiness: dict, warn: int) -> int:
    """0=pass, 1=warn, 2=block, based on the worst-scored item across layers."""
    worst = 100.0
    for block in readiness.get("sot_files", {}).values():
        worst = min(worst, block.get("score", 100))
    for block in readiness.get("epics", {}).values():
        worst = min(worst, block.get("score", 100))
    for block in readiness.get("stages", {}).values():
        worst = min(worst, block.get("score", 100))
    if worst >= warn:
        return 0
    if worst >= BLOCK_THRESHOLD:
        return 1
    return 2


# ---------- Main ---------- #

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="PRD-CE readiness scoring — orchestrates SoT, EPIC, and stage scorers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exit codes: 0=pass, 1=warn, 2=block, 3=error.",
    )
    p.add_argument("action", choices=["run", "status"], nargs="?", default="run",
                   help="'run' computes all layers; 'status' prints latest from readiness.json.")
    p.add_argument("--repo", type=Path, default=None)
    p.add_argument("--gate", type=str, default=None,
                   help="Override target gate (e.g. v0.8).")
    p.add_argument("--threshold", type=int, default=DEFAULT_WARN_THRESHOLD,
                   help=f"Warn threshold (default {DEFAULT_WARN_THRESHOLD}).")
    p.add_argument("--json", dest="as_json", action="store_true",
                   help="Emit readiness.json to stdout instead of the text report.")
    p.add_argument("--quiet", action="store_true",
                   help="Suppress all output; use exit code only.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    repo = (args.repo.resolve() if args.repo else find_repo_root(Path.cwd()))
    readiness_file = repo / "status" / "readiness.json"

    if args.action == "run":
        if not SOT_SCRIPT.is_file() or not EPIC_SCRIPT.is_file() or not STAGE_SCRIPT.is_file():
            print(f"error: one or more scorer scripts missing next to {__file__}", file=sys.stderr)
            return 3
        compute_all(repo, args.gate, args.quiet)

    if not readiness_file.is_file():
        if not args.quiet:
            print(f"error: {readiness_file} not found — run `readiness.py run` first.", file=sys.stderr)
        return 3

    readiness = json.loads(readiness_file.read_text())

    if args.as_json:
        print(json.dumps(readiness, indent=2, ensure_ascii=False))
    elif not args.quiet:
        print(format_report(readiness, repo.name, args.threshold))

    return overall_exit_code(readiness, args.threshold)


if __name__ == "__main__":
    sys.exit(main())
