"""EPIC readiness scorer — composes SoT scores with EPIC-level dimensions.

Answers "can we build this EPIC?" via nine dimensions. Emits `caused_by`
pointers on caps and unmet criteria so consumers can traverse the graph
from EPIC → blocking SoT file without re-querying.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

from . import SCHEMA_VERSION, VERSION
from .common import (
    HEADING_DEF_RE,
    ID_RE,
    SEVERITY_PENALTY,
    MAX_PENALTY,
    SoTEntry,
    build_summary,
    expand_ranges,
    extract_section,
    find_repo_root,
    index_all_entries,
    load_domain_profile,
    load_readiness_config,
    parse_frontmatter,
)


EPIC_WEIGHTS = {
    "spec_resolution":        0.20,
    "spec_depth":             0.15,
    "test_coverage_declared": 0.15,
    "upstream_gate":          0.10,
    "dependency_readiness":   0.10,
    "ambiguity_load":         0.05,
    "confidence_avg":         0.15,
    "status_maturity":        0.05,
    "file_readiness":         0.05,
}

# Critical caps: (rule_name, cap_value, reason). Evaluated top-to-bottom; lowest cap wins.
CRITICAL_CAPS = [
    ("test_coverage_zero", 55,
     "test_coverage_declared is 0 — v0.7 requires TEST- entries before build."),
    ("spec_resolution_low", 60,
     "spec_resolution below 80% — too many referenced IDs don't resolve."),
    ("stub_sot_file", 60,
     "A SoT file referenced by this EPIC is a placeholder stub."),
]


@dataclass
class EpicContext:
    """Parsed inputs for a single EPIC's readiness computation."""
    id: str
    file: Path
    inputs: dict
    referenced_ids: list[str] = field(default_factory=list)
    unresolved_assumptions: int = 0
    state: str = "Unknown"


# ---------- Parse ---------- #

def parse_epic(epic_file: Path, inputs_override: Optional[dict]) -> EpicContext:
    text = epic_file.read_text(errors="replace")
    frontmatter, body = parse_frontmatter(text)
    inputs = inputs_override or frontmatter.get("readiness_inputs") or {}

    epic_id_match = re.search(r"EPIC-\d{2,3}", epic_file.name)
    epic_id = inputs.get("target") or (epic_id_match.group(0) if epic_id_match else epic_file.stem)

    ctx = EpicContext(id=epic_id, file=epic_file, inputs=inputs)

    # State line: "> **State**: `Planned`" etc.
    state_m = re.search(r"\*\*State\*\*[:\s]+`?([A-Za-z ]+?)`?[\s`]*$", body, re.MULTILINE)
    if state_m:
        ctx.state = state_m.group(1).strip()

    # Section 3: Context & IDs — extract all referenced IDs (incl. ranges)
    section_3 = extract_section(body, r"^##\s+.*Context.*IDs.*$")
    if section_3 is None:
        section_3 = extract_section(body, r"^##\s+3\.\s+Context")
    ids_set: set[str] = set()
    if section_3:
        for m in ID_RE.finditer(section_3):
            ids_set.add(f"{m.group(1)}-{m.group(2)}")
        ids_set |= expand_ranges(section_3)
    ctx.referenced_ids = sorted(ids_set)

    # Section 1: Assumptions & Ambiguities — count unresolved rows
    session = extract_section(body, r"^##\s+.*Session State.*$")
    if session:
        unresolved = 0
        for line in session.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 6:
                continue
            type_cell = cells[2].upper() if len(cells) > 2 else ""
            resolution_cell = cells[5].lower() if len(cells) > 5 else ""
            if type_cell in {"ASSUMPTION", "AMBIGUITY"}:
                if resolution_cell in {"", "-", "—", "pending"}:
                    unresolved += 1
        ctx.unresolved_assumptions = unresolved

    return ctx


# ---------- Dimension computations ---------- #

def compute_spec_resolution(ctx: EpicContext, index: dict[str, SoTEntry],
                            domain: dict, sot_scores: dict) -> tuple[float, list[dict]]:
    if not ctx.referenced_ids:
        return 100.0, []
    resolved = [i for i in ctx.referenced_ids if i in index]
    unresolved = [i for i in ctx.referenced_ids if i not in index]
    score = (len(resolved) / len(ctx.referenced_ids)) * 100.0
    unmet: list[dict] = []
    for i in unresolved:
        prefix = i.split("-")[0]
        owning_file = (domain.get(prefix) or {}).get("file")
        entry = {"dimension": "spec_resolution", "ref": i,
                 "reason": f"{i} referenced in EPIC Section 3 but not defined in any SoT/PRD file.",
                 "severity": "high",
                 "fix": f"Define {i} in its SoT file, or remove the reference from Section 3."}
        if owning_file:
            entry["caused_by"] = owning_file
            entry["caused_by_score"] = sot_scores.get(owning_file, {}).get("score")
        unmet.append(entry)
    return score, unmet


def compute_spec_depth(ctx: EpicContext, index: dict[str, SoTEntry]) -> tuple[float, list[dict]]:
    resolved = [index[i] for i in ctx.referenced_ids if i in index]
    if not resolved:
        return 100.0, []
    stubs = [e for e in resolved if not e.is_non_stub()]
    non_stub = len(resolved) - len(stubs)
    score = (non_stub / len(resolved)) * 100.0
    unmet = [
        {"dimension": "spec_depth", "ref": e.id,
         "reason": f"{e.id} in {e.file} has only {e.word_count()} words — likely a stub.",
         "severity": "medium",
         "fix": f"Expand {e.id} with rationale, schema, or required sub-sections."}
        for e in stubs
    ]
    return score, unmet


def compute_test_coverage(ctx: EpicContext, index: dict[str, SoTEntry],
                          repo: Path, sot_scores: dict) -> tuple[float, list[dict]]:
    needs_tests = [i for i in ctx.referenced_ids if i.split("-")[0] in {"API", "BR"}]
    if not needs_tests:
        return 100.0, []

    testing_path = "SoT/SoT.TESTING.md"
    testing_score = sot_scores.get(testing_path, {}).get("score")
    test_files = list((repo / "SoT").glob("SoT.TESTING.md")) if (repo / "SoT").is_dir() else []
    if not test_files:
        return 0.0, [{"dimension": "test_coverage_declared",
                      "reason": "SoT.TESTING.md not found; no test coverage possible.",
                      "severity": "high",
                      "caused_by": testing_path,
                      "caused_by_score": testing_score,
                      "fix": "Create SoT.TESTING.md and populate TEST- entries."}]

    test_entries = [e for e in index.values() if e.prefix == "TEST"]
    if not test_entries:
        return 0.0, [{"dimension": "test_coverage_declared",
                      "reason": f"SoT.TESTING.md contains no TEST- entries; {len(needs_tests)} API-/BR- in scope need coverage.",
                      "severity": "high",
                      "caused_by": testing_path,
                      "caused_by_score": testing_score,
                      "fix": "Populate TEST- entries (Given-When-Then) for each API-/BR- in Section 3."}]

    covered = set()
    for test_entry in test_entries:
        for m in ID_RE.finditer(test_entry.body):
            ref = f"{m.group(1)}-{m.group(2)}"
            if ref in needs_tests:
                covered.add(ref)
    score = (len(covered) / len(needs_tests)) * 100.0
    missing = [i for i in needs_tests if i not in covered]
    unmet = [
        {"dimension": "test_coverage_declared", "ref": i,
         "reason": f"{i} has no TEST- entry referencing it.",
         "severity": "high",
         "fix": f"Add a TEST- entry in SoT.TESTING.md that implements/verifies {i}."}
        for i in missing
    ] if missing else []
    return score, unmet


def compute_upstream_gate(ctx: EpicContext, readiness_json: Optional[dict]) -> tuple[float, list[dict]]:
    if not readiness_json or "stage" not in readiness_json:
        return 100.0, []
    stage_score = readiness_json["stage"].get("score", 0)
    threshold = ctx.inputs.get("threshold_warn", 70)
    if stage_score >= threshold:
        return 100.0, []
    return (stage_score / threshold) * 100.0, [{
        "dimension": "upstream_gate",
        "reason": f"Owning stage readiness score ({stage_score}) below EPIC threshold ({threshold}).",
        "severity": "medium",
        "fix": "Raise stage readiness before building this EPIC, or lower threshold.",
    }]


def compute_dependency_readiness(ctx: EpicContext, repo: Path) -> tuple[float, list[dict]]:
    deps = ctx.inputs.get("depends_on_epics") or []
    if not deps:
        return 100.0, []
    complete = 0
    unmet_items: list[dict] = []
    for dep in deps:
        dep_files = list((repo / "epics").glob(f"{dep}*.md"))
        if not dep_files:
            unmet_items.append({"dimension": "dependency_readiness", "ref": dep,
                                "reason": f"Dependency {dep} not found in epics/.",
                                "severity": "high", "fix": f"Create {dep} or remove the dependency."})
            continue
        text = dep_files[0].read_text(errors="replace")
        state_m = re.search(r"\*\*State\*\*[:\s]+`?([A-Za-z ]+?)`?[\s`]*$", text, re.MULTILINE)
        state = state_m.group(1).strip() if state_m else "Unknown"
        if state == "Complete":
            complete += 1
        else:
            unmet_items.append({"dimension": "dependency_readiness", "ref": dep,
                                "reason": f"Dependency {dep} state is '{state}', needs 'Complete'.",
                                "severity": "high",
                                "fix": f"Complete {dep} before starting this EPIC."})
    score = (complete / len(deps)) * 100.0
    return score, unmet_items


def compute_ambiguity_load(ctx: EpicContext) -> tuple[float, list[dict]]:
    score = max(0.0, 100.0 - ctx.unresolved_assumptions * 20.0)
    unmet = []
    if ctx.unresolved_assumptions > 0:
        unmet.append({
            "dimension": "ambiguity_load",
            "reason": f"{ctx.unresolved_assumptions} unresolved row(s) in Assumptions & Ambiguities log.",
            "severity": "medium",
            "fix": "Resolve or defer the items in Session State → Assumptions & Ambiguities.",
        })
    return score, unmet


def compute_confidence_avg(ctx: EpicContext, index: dict[str, SoTEntry]) -> tuple[Optional[float], list[dict]]:
    resolved = [index[i] for i in ctx.referenced_ids if i in index]
    vals = [e.confidence() for e in resolved if e.confidence() is not None]
    if not vals:
        return None, []
    avg = sum(vals) / len(vals)
    score = (avg / 5.0) * 100.0
    floor = ctx.inputs.get("confidence_floor", 3)
    low = [e for e in resolved if e.confidence() is not None and e.confidence() < floor]
    unmet = [
        {"dimension": "confidence_avg", "ref": e.id,
         "reason": f"{e.id} confidence {e.confidence()}/5 below floor {floor}/5.",
         "severity": "low",
         "fix": f"Gather stronger evidence for {e.id} or adjust confidence_floor."}
        for e in low
    ]
    return score, unmet


def compute_status_maturity(ctx: EpicContext, index: dict[str, SoTEntry]) -> tuple[Optional[float], list[dict]]:
    resolved = [index[i] for i in ctx.referenced_ids if i in index]
    with_status = [(e, e.status()) for e in resolved if e.status() is not None]
    if not with_status:
        return None, []
    non_draft = [e for e, s in with_status if s.lower() != "draft"]
    score = (len(non_draft) / len(with_status)) * 100.0
    drafts = [e for e, s in with_status if s.lower() == "draft"]
    unmet = [
        {"dimension": "status_maturity", "ref": e.id,
         "reason": f"{e.id} Status is still 'Draft'.",
         "severity": "low",
         "fix": f"Promote {e.id} to Active once validated."}
        for e in drafts
    ]
    return score, unmet


def compute_file_readiness(ctx: EpicContext, index: dict[str, SoTEntry],
                           repo: Path, domain: dict, sot_scores: dict) -> tuple[float, list[dict]]:
    """Are the SoT files referenced by Section 3 populated (not placeholder stubs)?

    Includes files that *would* own dangling refs via domain profile prefix
    mapping — otherwise a repo where UJ-001..006 reference a placeholder
    USER_JOURNEYS.md would escape detection because the IDs never resolved.
    """
    files_used: set[str] = set()
    for i in ctx.referenced_ids:
        if i in index:
            files_used.add(index[i].file)
        else:
            prefix = i.split("-")[0]
            info = domain.get(prefix) if domain else None
            if info and info.get("file"):
                owning = info["file"]
                if (repo / owning).is_file():
                    files_used.add(owning)
    if not files_used:
        return 100.0, []

    stubs: list[str] = []
    for rel in files_used:
        p = repo / rel
        if not p.is_file():
            stubs.append(rel)
            continue
        text = p.read_text(errors="replace")
        headings = [l for l in text.splitlines() if HEADING_DEF_RE.match(l)]
        body_lower = text.lower()
        placeholder_markers = ("pending prd development", "todo", "placeholder", "to be filled")
        has_placeholder = any(m in body_lower for m in placeholder_markers)
        if not headings and (has_placeholder or len(text.strip()) < 100):
            stubs.append(rel)

    if not stubs:
        return 100.0, []
    score = ((len(files_used) - len(stubs)) / len(files_used)) * 100.0
    unmet = [
        {"dimension": "file_readiness", "ref": s,
         "reason": f"{s} is a stub/placeholder file with no real entries.",
         "severity": "high",
         "caused_by": s,
         "caused_by_score": sot_scores.get(s, {}).get("score"),
         "fix": f"Populate {s} with real SoT entries before this EPIC begins."}
        for s in stubs
    ]
    return score, unmet


# ---------- Aggregation ---------- #

def apply_overrides(ctx: EpicContext, readiness_config: dict) -> dict:
    state = {d: "enabled" for d in EPIC_WEIGHTS}
    repo_defaults = readiness_config.get("dimension_defaults") or {}
    for k, v in repo_defaults.items():
        if k in state:
            state[k] = v
    epic_overrides = ctx.inputs.get("dimension_overrides") or {}
    for k, v in epic_overrides.items():
        if k in state:
            state[k] = v
    return state


def renormalize_weights(override_state: dict[str, str],
                        scores: dict[str, Optional[float]]) -> dict[str, float]:
    active = {
        d: EPIC_WEIGHTS[d] for d in EPIC_WEIGHTS
        if override_state.get(d) != "disabled" and scores.get(d) is not None
    }
    total = sum(active.values())
    return {d: w / total for d, w in active.items()} if total else {}


def compute(epic_file: Path, repo: Path, inputs_override: Optional[dict]) -> dict:
    domain = load_domain_profile(repo)
    config = load_readiness_config(repo)
    index = index_all_entries(repo)
    ctx = parse_epic(epic_file, inputs_override)

    existing: Optional[dict] = None
    readiness_path = repo / "status" / "readiness.json"
    if readiness_path.is_file():
        try:
            existing = json.loads(readiness_path.read_text())
        except json.JSONDecodeError:
            existing = None
    sot_scores = (existing or {}).get("sot_files", {}) if existing else {}

    dims: dict[str, dict] = {}
    unmet: list[dict] = []

    s, u = compute_spec_resolution(ctx, index, domain, sot_scores)
    dims["spec_resolution"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_spec_depth(ctx, index)
    dims["spec_depth"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_test_coverage(ctx, index, repo, sot_scores)
    dims["test_coverage_declared"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_upstream_gate(ctx, existing)
    dims["upstream_gate"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_dependency_readiness(ctx, repo)
    dims["dependency_readiness"] = {"score": round(s, 1)}
    unmet.extend(u)

    s, u = compute_ambiguity_load(ctx)
    dims["ambiguity_load"] = {"score": round(s, 1)}
    unmet.extend(u)

    conf_score, u = compute_confidence_avg(ctx, index)
    dims["confidence_avg"] = {"score": conf_score if conf_score is not None else None}
    unmet.extend(u)

    stat_score, u = compute_status_maturity(ctx, index)
    dims["status_maturity"] = {"score": stat_score if stat_score is not None else None}
    unmet.extend(u)

    s, u = compute_file_readiness(ctx, index, repo, domain, sot_scores)
    dims["file_readiness"] = {"score": round(s, 1)}
    unmet.extend(u)

    override_state = apply_overrides(ctx, config)
    score_map = {d: dims[d].get("score") for d in dims}
    weights = renormalize_weights(override_state, score_map)

    weighted_score = 0.0
    for d, w in weights.items():
        dims[d]["weight"] = round(w, 3)
        weighted_score += (score_map[d] or 0) * w

    for d in dims:
        if d not in weights:
            if override_state.get(d) == "disabled":
                dims[d]["status"] = "disabled"
            elif score_map[d] is None:
                dims[d]["status"] = "not_applicable"
            dims[d].pop("score", None)

    raw_penalty = sum(SEVERITY_PENALTY.get(c.get("severity", "medium"), 3) for c in unmet)
    penalty = min(raw_penalty, MAX_PENALTY)

    # Critical caps with caused_by enrichment
    caps_applied: list[dict] = []
    cap_score = 100
    if score_map.get("test_coverage_declared") == 0 and ctx.referenced_ids:
        needs_tests = any(i.split("-")[0] in {"API", "BR"} for i in ctx.referenced_ids)
        if needs_tests:
            cap_score = min(cap_score, CRITICAL_CAPS[0][1])
            caps_applied.append({"rule": "test_coverage_zero", "cap": CRITICAL_CAPS[0][1],
                                 "reason": CRITICAL_CAPS[0][2],
                                 "caused_by": "SoT/SoT.TESTING.md",
                                 "caused_by_score": sot_scores.get("SoT/SoT.TESTING.md", {}).get("score")})
    if score_map.get("spec_resolution", 100) < 80:
        cap_score = min(cap_score, CRITICAL_CAPS[1][1])
        dangling_files: dict[str, int] = {}
        for c in unmet:
            if c.get("dimension") == "spec_resolution" and c.get("caused_by"):
                dangling_files[c["caused_by"]] = dangling_files.get(c["caused_by"], 0) + 1
        worst = max(dangling_files.items(), key=lambda x: x[1]) if dangling_files else (None, 0)
        caps_applied.append({"rule": "spec_resolution_low", "cap": CRITICAL_CAPS[1][1],
                             "reason": CRITICAL_CAPS[1][2],
                             "caused_by": worst[0],
                             "caused_by_score": sot_scores.get(worst[0], {}).get("score") if worst[0] else None})
    if score_map.get("file_readiness", 100) < 100:
        cap_score = min(cap_score, CRITICAL_CAPS[2][1])
        stub_files = [c.get("caused_by") for c in unmet
                      if c.get("dimension") == "file_readiness" and c.get("caused_by")]
        caps_applied.append({"rule": "stub_sot_file", "cap": CRITICAL_CAPS[2][1],
                             "reason": CRITICAL_CAPS[2][2],
                             "caused_by": stub_files[0] if stub_files else None,
                             "caused_by_score": sot_scores.get(stub_files[0], {}).get("score") if stub_files else None})

    penalized = max(0.0, weighted_score - penalty)
    final_score = min(cap_score, penalized)

    thresholds = {
        "warn": ctx.inputs.get("threshold_warn", 70),
        "block": ctx.inputs.get("threshold_block", 50),
    }

    return {
        "target": ctx.id,
        "work_type": "epic",
        "state": ctx.state,
        "score": round(final_score, 1),
        "weighted_score": round(weighted_score, 1),
        "penalty": penalty,
        "cap_applied": cap_score if caps_applied else None,
        "caps": caps_applied,
        "threshold_warn": thresholds["warn"],
        "threshold_block": thresholds["block"],
        "dimensions": dims,
        "unmet_criteria": unmet,
        "referenced_ids_count": len(ctx.referenced_ids),
        "file": str(epic_file.relative_to(repo)),
    }


# ---------- CLI ---------- #

def main_cli() -> int:
    p = argparse.ArgumentParser(description="Compute PRD-CE EPIC readiness score.")
    p.add_argument("epic_file", type=Path)
    p.add_argument("--repo", type=Path, default=None)
    p.add_argument("--inputs", type=Path, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--merge", action="store_true")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    if not args.epic_file.is_file():
        print(f"error: epic file not found: {args.epic_file}", file=sys.stderr)
        return 2

    args.epic_file = args.epic_file.resolve()
    repo = args.repo.resolve() if args.repo else find_repo_root(args.epic_file)
    inputs_override = None
    if args.inputs:
        if not args.inputs.is_file():
            print(f"error: inputs file not found: {args.inputs}", file=sys.stderr)
            return 2
        with args.inputs.open() as f:
            loaded = yaml.safe_load(f) or {}
        inputs_override = loaded.get("readiness_inputs", loaded)

    epic_block = compute(args.epic_file, repo, inputs_override)

    existing_full: dict = {}
    readiness_file = repo / "status" / "readiness.json"
    if readiness_file.is_file():
        try:
            existing_full = json.loads(readiness_file.read_text())
        except json.JSONDecodeError:
            existing_full = {}

    output = {
        "last_computed": datetime.now(timezone.utc).isoformat(),
        "computed_by": f"compute-readiness@{VERSION}",
        "schema_version": SCHEMA_VERSION,
        "sot_files": existing_full.get("sot_files", {}),
        "epics": {epic_block["target"]: epic_block},
        "stages": existing_full.get("stages", {}),
    }

    if args.merge and existing_full.get("epics"):
        output["epics"] = {**existing_full["epics"], epic_block["target"]: epic_block}

    # Back-propagate implicit consumers: SoT files cited as caused_by here
    # are consumers even if not referenced explicitly in Section 3.
    implicit_consumers: set[str] = set()
    for cap in epic_block.get("caps", []):
        if cap.get("caused_by"):
            implicit_consumers.add(cap["caused_by"])
    for c in epic_block.get("unmet_criteria", []):
        if c.get("caused_by"):
            implicit_consumers.add(c["caused_by"])
    for sot_path in implicit_consumers:
        if sot_path in output["sot_files"]:
            current = output["sot_files"][sot_path].get("consumed_by_epics", [])
            if epic_block["target"] not in current:
                current.append(epic_block["target"])
                current.sort()
                output["sot_files"][sot_path]["consumed_by_epics"] = current

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
        print(f"\n{epic_block['target']} score: {epic_block['score']} "
              f"(warn<{epic_block['threshold_warn']}, block<{epic_block['threshold_block']})")
        for d, info in epic_block["dimensions"].items():
            marker = f"  {d:<24}"
            if "status" in info:
                print(f"{marker} [{info['status']}]")
            else:
                w = info.get("weight", 0)
                print(f"{marker} score={info['score']:>5}  weight={w:.3f}")
        if epic_block["unmet_criteria"]:
            print(f"\n{len(epic_block['unmet_criteria'])} unmet criteria:")
            for c in epic_block["unmet_criteria"][:10]:
                print(f"  - [{c['severity']}] {c.get('ref', c['dimension'])}: {c['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main_cli())
