"""PRD stage readiness — thin composer over SoT + EPIC scores.

Answers "can we advance v0.X → v0.Y?" by combining:
  - mandatory artifact counts from GATE_REQUIREMENTS (mirrors gate-criteria.md)
  - mean readiness of relevant SoT files (read from existing readiness.json)
  - cross-reference integrity across the repo
  - mean EPIC score (v0.7+ gates only)
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
    SEVERITY_PENALTY,
    MAX_PENALTY,
    build_summary,
    find_repo_root,
)


STAGE_WEIGHTS = {
    "required_ids_present":      0.30,
    "relevant_sot_readiness":    0.30,
    "cross_ref_integrity":       0.20,
    "downstream_epic_readiness": 0.20,
}

# Gate transition requirements — mirrors .claude/skills/ghm-gate-check/references/gate-criteria.md.
# `required_prefixes`: min counts per prefix. `prefix_aliases`: accept any from the list
# (so DBT can alternately be ENT, etc.). `relevant_sots`: files whose readiness rolls into
# this gate's score. `enables_downstream_epic_readiness`: true for v0.7+ gates where EPICs exist.
GATE_REQUIREMENTS: dict[str, dict] = {
    "v0.2": {
        "name": "v0.1 → v0.2 (Spark → Market Definition)",
        "required_prefixes": {"CFD": 3},
        "relevant_sots": ["SoT/SoT.customer_feedback.md"],
    },
    "v0.3": {
        "name": "v0.2 → v0.3 (Market Definition → Commercial Model)",
        "required_prefixes": {"CFD": 3, "BR": 1},
        "relevant_sots": ["SoT/SoT.customer_feedback.md", "SoT/SoT.BUSINESS_RULES.md"],
    },
    "v0.4": {
        "name": "v0.3 → v0.4 (Commercial Model → User Journeys)",
        "required_prefixes": {"BR": 3, "KPI": 1, "CFD": 5, "FEA": 1},
        "relevant_sots": ["SoT/SoT.BUSINESS_RULES.md", "SoT/SoT.customer_feedback.md"],
    },
    "v0.5": {
        "name": "v0.4 → v0.5 (User Journeys → Red Team)",
        "required_prefixes": {"PER": 1, "UJ": 3},
        "relevant_sots": ["SoT/SoT.USER_JOURNEYS.md", "SoT/SoT.BUSINESS_RULES.md"],
    },
    "v0.6": {
        "name": "v0.5 → v0.6 (Red Team → Architecture)",
        "required_prefixes": {"RISK": 5, "TECH": 3},
        "relevant_sots": ["SoT/SoT.RISKS.md", "SoT/SoT.TECHNICAL_DECISIONS.md"],
    },
    "v0.7": {
        "name": "v0.6 → v0.7 (Architecture → Build)",
        "required_prefixes": {"ARC": 1, "API": 1, "DBT": 1},
        "prefix_aliases": {"DBT": ["DBT", "ENT"]},
        "relevant_sots": [
            "SoT/SoT.TECHNICAL_DECISIONS.md",
            "SoT/SoT.API_CONTRACTS.md",
            "SoT/SoT.DATA_MODEL.md",
        ],
    },
    "v0.8": {
        "name": "v0.7 → v0.8 (Build → Deployment)",
        "required_prefixes": {"EPIC": 1, "TEST": 1},
        "relevant_sots": [
            "SoT/SoT.TESTING.md",
            "SoT/SoT.API_CONTRACTS.md",
            "SoT/SoT.DATA_MODEL.md",
            "SoT/SoT.BUSINESS_RULES.md",
        ],
        "enables_downstream_epic_readiness": True,
    },
    "v0.9": {
        "name": "v0.8 → v0.9 (Deployment → GTM)",
        "required_prefixes": {"DEP": 1, "RUN": 1, "MON": 1},
        "relevant_sots": ["SoT/SoT.DEPLOYMENT.md"],
        "enables_downstream_epic_readiness": True,
    },
    "v1.0": {
        "name": "v0.9 → v1.0 (GTM → Launch)",
        "required_prefixes": {"GTM": 1, "KPI": 3},
        "relevant_sots": ["SoT/SoT.customer_feedback.md"],
        "enables_downstream_epic_readiness": True,
    },
}


# ---------- Autodetect ---------- #

def autodetect_gate(repo: Path) -> Optional[str]:
    """Read PRD.md's 'Next Target Gate' field; prefer the destination in arrow form."""
    prd = repo / "PRD.md"
    if not prd.is_file():
        return None
    text = prd.read_text(errors="replace")
    arrow_m = re.search(r"Next Target Gate.*?v0?\.\d+.*?(?:\u2192|->|to)\s*(v\d\.\d+|v1\.0)", text)
    if arrow_m:
        return arrow_m.group(1)
    m = re.search(r"Next Target Gate.*?(v0?\.\d|v1\.0)", text)
    if m:
        return m.group(1)
    m = re.search(r"Current Lifecycle Gate.*?(v0?\.\d|v1\.0)", text)
    if m:
        current = m.group(1)
        if current == "v1.0":
            return None
        major, minor = current.split(".")
        return f"{major}.{int(minor) + 1}"
    return None


# ---------- ID indexing for stage scope ---------- #

def index_all_ids(repo: Path) -> dict[str, set[str]]:
    """{prefix: {id, ...}} across SoT/, PRD.md, epics/, README.md.

    Handles EPIC- via filename (`epics/EPIC-NN-*.md`) since EPICs use `#` not `##`.
    """
    out: dict[str, set[str]] = {}
    files: list[Path] = []
    sot = repo / "SoT"
    if sot.is_dir():
        files.extend(sot.glob("*.md"))
    for extra in ("PRD.md", "README.md"):
        p = repo / extra
        if p.is_file():
            files.append(p)
    epics = repo / "epics"
    if epics.is_dir():
        for p in epics.glob("EPIC-*.md"):
            m = re.match(r"(EPIC-\d{2,3})", p.name)
            if m:
                out.setdefault("EPIC", set()).add(m.group(1))
            if p.name != "EPIC_TEMPLATE.md":
                files.append(p)

    for f in files:
        for line in f.read_text(errors="replace").splitlines():
            m = HEADING_DEF_RE.match(line)
            if m:
                prefix, num = m.group(1).split("-")
                out.setdefault(prefix, set()).add(f"{prefix}-{num}")
    return out


# ---------- Dimension computations ---------- #

def compute_required_ids_present(gate_cfg: dict, id_index: dict[str, set[str]]) -> tuple[float, list[dict]]:
    required = gate_cfg.get("required_prefixes", {})
    aliases = gate_cfg.get("prefix_aliases", {})
    if not required:
        return 100.0, []
    met = 0
    unmet: list[dict] = []
    for prefix, min_count in required.items():
        count = sum(len(id_index.get(alias, set())) for alias in aliases.get(prefix, [prefix]))
        if count >= min_count:
            met += 1
        else:
            unmet.append({
                "dimension": "required_ids_present",
                "ref": prefix,
                "reason": f"Found {count} {prefix}- entries; gate requires \u2265{min_count}.",
                "severity": "high",
                "fix": f"Author {min_count - count} more {prefix}- entries before advancing.",
            })
    score = (met / len(required)) * 100.0
    return score, unmet


def compute_relevant_sot_readiness(gate_cfg: dict, sot_scores: dict) -> tuple[float, list[dict]]:
    relevant = gate_cfg.get("relevant_sots", [])
    if not relevant:
        return 100.0, []
    usable = [(p, sot_scores[p]["score"]) for p in relevant if p in sot_scores]
    if not usable:
        return 0.0, [{
            "dimension": "relevant_sot_readiness",
            "reason": "No SoT file scores available — run compute-sot-readiness first.",
            "severity": "high",
            "fix": "Run compute-sot-readiness.py all before computing stage readiness.",
        }]
    mean = sum(s for _, s in usable) / len(usable)
    unmet = [
        {"dimension": "relevant_sot_readiness", "ref": p,
         "reason": f"{p} scores {s} — drags down stage readiness.",
         "severity": "medium" if s > 30 else "high",
         "caused_by": p,
         "caused_by_score": s,
         "fix": f"Raise {p} to \u226570 to clear this dimension."}
        for p, s in usable if s < 70
    ]
    return mean, unmet


def compute_cross_ref_integrity(repo: Path, id_index: dict[str, set[str]],
                                known_prefixes: set[str]) -> tuple[float, list[dict]]:
    """Percentage of known-prefix references that resolve to a definition."""
    defined: set[str] = set()
    for ids in id_index.values():
        defined |= ids

    references: set[str] = set()
    scan_files: list[Path] = []
    for sub in ("SoT", "epics"):
        p = repo / sub
        if p.is_dir():
            scan_files.extend(p.glob("*.md"))
    for extra in ("PRD.md", "README.md"):
        p = repo / extra
        if p.is_file():
            scan_files.append(p)

    for f in scan_files:
        for m in ID_RE.finditer(f.read_text(errors="replace")):
            prefix = m.group(1)
            if prefix not in known_prefixes:
                continue
            references.add(f"{prefix}-{m.group(2)}")

    if not references:
        return 100.0, []
    dangling = references - defined
    resolved = len(references) - len(dangling)
    score = (resolved / len(references)) * 100.0

    unmet = []
    if dangling:
        sample = sorted(dangling)[:5]
        unmet.append({
            "dimension": "cross_ref_integrity",
            "reason": f"{len(dangling)} dangling ID reference(s) across repo: "
                      f"{', '.join(sample)}" + ("..." if len(dangling) > 5 else ""),
            "severity": "high" if len(dangling) > 5 else "medium",
            "fix": "Define the referenced IDs, or remove the references.",
        })
    return score, unmet


def compute_downstream_epic_readiness(gate_cfg: dict, epic_scores: dict) -> tuple[Optional[float], list[dict]]:
    if not gate_cfg.get("enables_downstream_epic_readiness"):
        return None, []
    if not epic_scores:
        return 0.0, [{
            "dimension": "downstream_epic_readiness",
            "reason": "No EPIC scores available for v0.7+ gate — EPICs must be scored before advancing.",
            "severity": "high",
            "fix": "Run compute-readiness.py on each EPIC before computing stage readiness.",
        }]
    scores = [e["score"] for e in epic_scores.values()]
    mean = sum(scores) / len(scores)
    below = [(eid, e["score"]) for eid, e in epic_scores.items() if e["score"] < 70]
    unmet = [
        {"dimension": "downstream_epic_readiness", "ref": eid,
         "reason": f"{eid} scores {s} — below warn threshold (70).",
         "severity": "high" if s < 50 else "medium",
         "fix": f"Address unmet_criteria in {eid} before advancing stage."}
        for eid, s in below
    ]
    return mean, unmet


def renormalize(scores: dict[str, Optional[float]]) -> dict[str, float]:
    active = {d: STAGE_WEIGHTS[d] for d in STAGE_WEIGHTS if scores.get(d) is not None}
    total = sum(active.values())
    return {d: w / total for d, w in active.items()} if total else {}


def compute_stage(gate: str, repo: Path, readiness_json: dict) -> dict:
    if gate not in GATE_REQUIREMENTS:
        raise SystemExit(f"Unknown gate: {gate}. Supported: {', '.join(GATE_REQUIREMENTS)}")

    gate_cfg = GATE_REQUIREMENTS[gate]
    id_index = index_all_ids(repo)
    sot_scores = readiness_json.get("sot_files", {})
    epic_scores = readiness_json.get("epics", {})

    dims: dict[str, dict] = {}
    unmet: list[dict] = []

    s, u = compute_required_ids_present(gate_cfg, id_index)
    dims["required_ids_present"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_relevant_sot_readiness(gate_cfg, sot_scores)
    dims["relevant_sot_readiness"] = {"score": round(s, 1)}
    unmet.extend(u)

    # Known prefixes: union of what gate requires + what's defined + standard methodology prefixes
    known_prefixes: set[str] = set(id_index.keys())
    known_prefixes |= set(gate_cfg.get("required_prefixes", {}).keys())
    for aliases in gate_cfg.get("prefix_aliases", {}).values():
        known_prefixes |= set(aliases)
    known_prefixes |= {"BR", "UJ", "PER", "SCR", "API", "DBT", "ENT", "TEST",
                       "DEP", "RUN", "MON", "CFD", "DES", "TECH", "ARC", "INT",
                       "RISK", "FEA", "GTM", "KPI", "EPIC", "LL"}

    s, u = compute_cross_ref_integrity(repo, id_index, known_prefixes)
    dims["cross_ref_integrity"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_downstream_epic_readiness(gate_cfg, epic_scores)
    dims["downstream_epic_readiness"] = {"score": round(s, 1) if s is not None else None}
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
    if score_map.get("required_ids_present", 100) < 50:
        cap = 45
        caps_applied.append({"rule": "missing_mandatory_artifacts", "cap": 45,
                             "reason": "Too many required artifact types missing — gate cannot pass."})
    if score_map.get("cross_ref_integrity", 100) < 60:
        cap = min(cap, 60)
        caps_applied.append({"rule": "cross_ref_broken", "cap": 60,
                             "reason": "Many dangling references — repo integrity compromised."})

    final = min(cap, max(0.0, weighted - penalty))

    return {
        "target": gate,
        "work_type": "stage",
        "gate_description": gate_cfg["name"],
        "score": round(final, 1),
        "weighted_score": round(weighted, 1),
        "penalty": penalty,
        "cap_applied": cap if caps_applied else None,
        "caps": caps_applied,
        "threshold_warn": 70,
        "threshold_block": 50,
        "dimensions": dims,
        "unmet_criteria": unmet,
    }


# ---------- CLI ---------- #

def main_cli() -> int:
    p = argparse.ArgumentParser(description="Compute PRD stage readiness score.")
    p.add_argument("--gate", type=str, default=None)
    p.add_argument("--repo", type=Path, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    repo = args.repo.resolve() if args.repo else find_repo_root(Path.cwd())
    gate = args.gate or autodetect_gate(repo)
    if not gate:
        print("error: could not detect target gate — use --gate <vX.Y>.", file=sys.stderr)
        return 2

    readiness_file = repo / "status" / "readiness.json"
    existing: dict = {}
    if readiness_file.is_file():
        try:
            existing = json.loads(readiness_file.read_text())
        except json.JSONDecodeError:
            existing = {}

    stage_block = compute_stage(gate, repo, existing)

    output = dict(existing)
    output["last_computed"] = datetime.now(timezone.utc).isoformat()
    output["computed_by"] = f"compute-prd-readiness@{VERSION}"
    output["schema_version"] = SCHEMA_VERSION
    output.setdefault("stages", {})[gate] = stage_block

    output["summary"] = build_summary(output)

    out_json = json.dumps(output, indent=2, ensure_ascii=False)
    if args.output == "-":
        print(out_json)
    else:
        out_path = Path(args.output) if args.output else readiness_file
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_json + "\n")
        if args.verbose:
            print(f"wrote {out_path}")

    if args.verbose:
        print(f"\nStage {gate}: {stage_block['gate_description']}")
        print(f"  score: {stage_block['score']}  (weighted {stage_block['weighted_score']}, "
              f"penalty -{stage_block['penalty']}, cap {stage_block['cap_applied'] or 'none'})")
        for d, info in stage_block["dimensions"].items():
            if "status" in info:
                print(f"  {d:<30} [{info['status']}]")
            else:
                print(f"  {d:<30} score={info['score']:>5}  weight={info.get('weight', 0):.3f}")
        if stage_block["unmet_criteria"]:
            print(f"\n  {len(stage_block['unmet_criteria'])} unmet:")
            for c in stage_block["unmet_criteria"][:6]:
                print(f"    - [{c['severity']}] {c.get('ref', c['dimension'])}: {c['reason'][:100]}")
    return 0


if __name__ == "__main__":
    sys.exit(main_cli())
