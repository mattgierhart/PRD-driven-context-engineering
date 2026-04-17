"""SoT file readiness scorer — the primitive layer.

Answers "is SoT/<file>.md in good shape?" via six dimensions:
entry_count, entry_depth, cross_ref_density, orphan_rate, status_coverage,
confidence_coverage. status/confidence auto-disable when the repo hasn't
adopted those conventions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from . import SCHEMA_VERSION, VERSION
from .common import (
    HEADING_DEF_RE,
    ID_RE,
    PLACEHOLDER_MARKERS,
    SEVERITY_PENALTY,
    MAX_PENALTY,
    SoTEntry,
    build_summary,
    collect_all_references,
    find_repo_root,
    index_all_entries,
    load_domain_profile,
)


SOT_WEIGHTS = {
    "entry_count":         0.15,
    "entry_depth":         0.25,
    "cross_ref_density":   0.20,
    "orphan_rate":         0.15,
    "status_coverage":     0.10,
    "confidence_coverage": 0.15,
}

CRITICAL_CAPS = {
    "placeholder_file": 10,   # no entries + placeholder marker
    "nearly_empty":     40,   # <3 entries but referenced externally
}


# ---------- Dimension computations ---------- #

def is_placeholder_file(text: str, entries: list[SoTEntry]) -> bool:
    if entries:
        return False
    lower = text.lower()
    return any(m in lower for m in PLACEHOLDER_MARKERS) or len(text.strip()) < 100


def compute_entry_count(entries: list[SoTEntry], text: str) -> tuple[float, list[dict], bool]:
    """Populated-enough score + placeholder-file flag."""
    is_placeholder = is_placeholder_file(text, entries)
    if is_placeholder:
        return 0.0, [{
            "dimension": "entry_count",
            "reason": "File is a placeholder stub with no ID entries.",
            "severity": "high",
            "fix": "Populate with real entries or remove references that need this file.",
        }], True
    n = len(entries)
    if n == 0:
        return 0.0, [{
            "dimension": "entry_count",
            "reason": "File has no ID entries.",
            "severity": "high",
            "fix": "Add at least one ID entry to establish the file.",
        }], False
    if n < 3:
        return 50.0, [{
            "dimension": "entry_count",
            "reason": f"Only {n} entries — file is sparse.",
            "severity": "medium",
            "fix": "Add entries to reach meaningful coverage for the domain.",
        }], False
    return 100.0, [], False


def compute_entry_depth(entries: list[SoTEntry]) -> tuple[Optional[float], list[dict]]:
    if not entries:
        return None, []
    stubs = [e for e in entries if not e.is_non_stub()]
    score = ((len(entries) - len(stubs)) / len(entries)) * 100.0
    unmet = [
        {"dimension": "entry_depth", "ref": e.id,
         "reason": f"{e.id} is only {e.word_count()} words — likely a stub.",
         "severity": "medium",
         "fix": f"Expand {e.id} with rationale, schema, or required sub-sections."}
        for e in stubs
    ]
    return score, unmet


def compute_cross_ref_density(entries: list[SoTEntry]) -> tuple[Optional[float], list[dict]]:
    if not entries:
        return None, []
    with_refs = [e for e in entries if e.outbound_refs()]
    score = (len(with_refs) / len(entries)) * 100.0
    isolated = [e for e in entries if not e.outbound_refs()]
    unmet = [
        {"dimension": "cross_ref_density", "ref": e.id,
         "reason": f"{e.id} references no other IDs — isolated in the knowledge graph.",
         "severity": "low",
         "fix": f"Link {e.id} to related BR-/API-/UJ- entries."}
        for e in isolated[:5]
    ]
    return score, unmet


def compute_orphan_rate(entries: list[SoTEntry], own_file: str,
                        all_refs: dict[str, set[str]]) -> tuple[Optional[float], list[dict]]:
    if not entries:
        return None, []
    orphans = [e for e in entries if not (all_refs.get(e.id, set()) - {own_file})]
    cited = len(entries) - len(orphans)
    score = (cited / len(entries)) * 100.0
    unmet = [
        {"dimension": "orphan_rate", "ref": e.id,
         "reason": f"{e.id} is never referenced outside {own_file} — orphaned.",
         "severity": "low",
         "fix": f"Ensure {e.id} is cited from EPICs, PRD, or related SoT entries — "
                f"or remove if unused."}
        for e in orphans[:5]
    ]
    return score, unmet


def compute_status_coverage(entries: list[SoTEntry]) -> tuple[Optional[float], list[dict]]:
    if not entries:
        return None, []
    with_status = [e for e in entries if e.has_status()]
    if not with_status:
        return None, []  # repo doesn't use Status convention
    score = (len(with_status) / len(entries)) * 100.0
    missing = [e for e in entries if not e.has_status()]
    unmet = [
        {"dimension": "status_coverage", "ref": e.id,
         "reason": f"{e.id} has no Status: field.",
         "severity": "low",
         "fix": f"Add 'Status: Active|Draft|Deprecated' to {e.id}."}
        for e in missing[:5]
    ]
    return score, unmet


def compute_confidence_coverage(entries: list[SoTEntry]) -> tuple[Optional[float], list[dict]]:
    if not entries:
        return None, []
    with_conf = [e for e in entries if e.has_confidence()]
    if not with_conf:
        return None, []
    score = (len(with_conf) / len(entries)) * 100.0
    missing = [e for e in entries if not e.has_confidence()]
    unmet = [
        {"dimension": "confidence_coverage", "ref": e.id,
         "reason": f"{e.id} has no Confidence: N/5 field.",
         "severity": "low",
         "fix": f"Add 'Confidence: N/5 (source: ...)' to {e.id} per ghm-id-register."}
        for e in missing[:5]
    ]
    return score, unmet


# ---------- Consumer map (SoT → EPICs that reference it) ---------- #

def build_epic_consumer_map(repo: Path, domain: dict) -> dict[str, list[str]]:
    """Return `{sot_file_rel_path: [epic_id, ...]}` — which EPICs consume each file.

    An EPIC consumes a SoT file if its Section 3 references any ID whose owning
    prefix maps to that file via the domain profile.
    """
    epics_dir = repo / "epics"
    if not epics_dir.is_dir():
        return {}
    consumers: dict[str, set[str]] = {}
    for epic in epics_dir.glob("EPIC-*.md"):
        if epic.name == "EPIC_TEMPLATE.md":
            continue
        text = epic.read_text(errors="replace")
        matches = list(re.finditer(r"^##\s+.*Context.*IDs.*$", text, re.MULTILINE))
        if not matches:
            continue
        start = matches[0].end()
        next_heading = re.search(r"^#{1,2}\s+", text[start:], re.MULTILINE)
        section_3 = text[start:start + next_heading.start()] if next_heading else text[start:]
        epic_id_m = re.search(r"EPIC-\d{2,3}", epic.name)
        if not epic_id_m:
            continue
        epic_id = epic_id_m.group(0)
        prefixes_used = {m.group(1) for m in ID_RE.finditer(section_3)}
        for prefix in prefixes_used:
            info = domain.get(prefix)
            if info and info.get("file"):
                consumers.setdefault(info["file"], set()).add(epic_id)
    return {f: sorted(ids) for f, ids in consumers.items()}


# ---------- Aggregation ---------- #

def renormalize(scores: dict[str, Optional[float]]) -> dict[str, float]:
    active = {d: SOT_WEIGHTS[d] for d in SOT_WEIGHTS if scores.get(d) is not None}
    total = sum(active.values())
    return {d: w / total for d, w in active.items()} if total else {}


def compute_file(sot_file: Path, repo: Path, index: dict[str, SoTEntry],
                 all_refs: dict[str, set[str]],
                 consumer_map: dict[str, list[str]]) -> dict:
    rel = str(sot_file.relative_to(repo))
    text = sot_file.read_text(errors="replace")
    entries = [e for e in index.values() if e.file == rel]

    dims: dict[str, dict] = {}
    unmet: list[dict] = []

    s, u, is_placeholder = compute_entry_count(entries, text)
    dims["entry_count"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_entry_depth(entries)
    dims["entry_depth"] = {"score": round(s, 1) if s is not None else None}
    unmet.extend(u)

    s, u = compute_cross_ref_density(entries)
    dims["cross_ref_density"] = {"score": round(s, 1) if s is not None else None}
    unmet.extend(u)

    s, u = compute_orphan_rate(entries, rel, all_refs)
    dims["orphan_rate"] = {"score": round(s, 1) if s is not None else None}
    unmet.extend(u)

    s, u = compute_status_coverage(entries)
    dims["status_coverage"] = {"score": s if s is not None else None}
    unmet.extend(u)

    s, u = compute_confidence_coverage(entries)
    dims["confidence_coverage"] = {"score": s if s is not None else None}
    unmet.extend(u)

    score_map = {d: dims[d].get("score") for d in dims}
    weights = renormalize(score_map)

    weighted = 0.0
    for d, w in weights.items():
        dims[d]["weight"] = round(w, 3)
        weighted += (score_map[d] or 0) * w

    for d in dims:
        if d not in weights:
            dims[d]["status"] = "not_applicable"
            dims[d].pop("score", None)

    raw_penalty = sum(SEVERITY_PENALTY.get(c.get("severity", "medium"), 3) for c in unmet)
    penalty = min(raw_penalty, MAX_PENALTY)

    cap = 100
    caps_applied: list[dict] = []
    if is_placeholder:
        cap = min(cap, CRITICAL_CAPS["placeholder_file"])
        caps_applied.append({"rule": "placeholder_file", "cap": CRITICAL_CAPS["placeholder_file"],
                             "reason": "File is placeholder with no real entries."})
    elif 0 < len(entries) < 3 and any(all_refs.get(e.id, set()) - {rel} for e in entries):
        cap = min(cap, CRITICAL_CAPS["nearly_empty"])
        caps_applied.append({"rule": "nearly_empty", "cap": CRITICAL_CAPS["nearly_empty"],
                             "reason": f"Only {len(entries)} entries but file is referenced externally."})

    final = min(cap, max(0.0, weighted - penalty))

    return {
        "target": rel,
        "work_type": "sot",
        "score": round(final, 1),
        "weighted_score": round(weighted, 1),
        "penalty": penalty,
        "cap_applied": cap if caps_applied else None,
        "caps": caps_applied,
        "entry_count": len(entries),
        "consumed_by_epics": consumer_map.get(rel, []),
        "dimensions": dims,
        "unmet_criteria": unmet,
    }


# ---------- CLI ---------- #

def discover_sot_files(repo: Path) -> list[Path]:
    sot_dir = repo / "SoT"
    if not sot_dir.is_dir():
        return []
    return sorted(p for p in sot_dir.glob("*.md")
                  if p.name not in {"SoT.README.md", "SoT.UNIQUE_ID_SYSTEM.md"})


def main_cli() -> int:
    p = argparse.ArgumentParser(description="Compute SoT file readiness scores.")
    p.add_argument("target", type=str, help='SoT file path, or "all".')
    p.add_argument("--repo", type=Path, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    if args.target == "all":
        repo = args.repo.resolve() if args.repo else find_repo_root(Path.cwd())
        targets = discover_sot_files(repo)
        if not targets:
            print(f"error: no SoT files found under {repo}/SoT/", file=sys.stderr)
            return 2
    else:
        target = Path(args.target).resolve()
        if not target.is_file():
            print(f"error: SoT file not found: {target}", file=sys.stderr)
            return 2
        repo = args.repo.resolve() if args.repo else find_repo_root(target)
        targets = [target]

    domain = load_domain_profile(repo)
    index = index_all_entries(repo)
    all_refs = collect_all_references(repo)
    consumer_map = build_epic_consumer_map(repo, domain)

    sot_blocks: dict[str, dict] = {}
    for sot in targets:
        block = compute_file(sot, repo, index, all_refs, consumer_map)
        sot_blocks[block["target"]] = block

    out_path = (Path(args.output) if args.output and args.output != "-"
                else (repo / "status" / "readiness.json"))
    existing: dict = {}
    if args.output != "-" and out_path.is_file():
        try:
            existing = json.loads(out_path.read_text())
        except json.JSONDecodeError:
            existing = {}

    output = {
        "last_computed": datetime.now(timezone.utc).isoformat(),
        "computed_by": f"compute-sot-readiness@{VERSION}",
        "schema_version": SCHEMA_VERSION,
        "sot_files": sot_blocks,
        "epics": existing.get("epics", {}),
        "stages": existing.get("stages", {}),
    }
    output["summary"] = build_summary(output)

    out_json = json.dumps(output, indent=2, ensure_ascii=False)
    if args.output == "-":
        print(out_json)
    else:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_json + "\n")
        if args.verbose:
            print(f"wrote {out_path}")

    if args.verbose:
        print()
        print(f"{'File':<40} {'score':>6}  {'weighted':>8}  {'entries':>7}  {'unmet':>5}")
        print("-" * 80)
        for path, block in sorted(sot_blocks.items()):
            name = path.split("/", 1)[-1] if "/" in path else path
            print(f"{name:<40} {block['score']:>6}  {block['weighted_score']:>8}  "
                  f"{block['entry_count']:>7}  {len(block['unmet_criteria']):>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main_cli())
