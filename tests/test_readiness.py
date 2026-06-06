"""Smoke tests for the readiness scoring pipeline.

These run the same entry points a user would (`readiness.py run`) against
deterministic fixture repos, then assert on the produced `status/readiness.json`.
Keeps the test surface small — we're validating that the scoring machinery
holds together, not that every formula is pinned to an exact number.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
READINESS_CLI = REPO_ROOT / "scripts" / "readiness.py"

PASS_THRESHOLD = 70
BLOCK_THRESHOLD = 50


def run_readiness(repo: Path, extra_args: list[str] | None = None) -> tuple[int, dict]:
    """Run `readiness.py run --quiet` in the fixture; return (exit_code, readiness_json)."""
    cmd = [sys.executable, str(READINESS_CLI), "run", "--quiet"]
    if extra_args:
        cmd.extend(extra_args)
    result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True)
    readiness_path = repo / "status" / "readiness.json"
    data = json.loads(readiness_path.read_text()) if readiness_path.is_file() else {}
    return result.returncode, data


# ---------- Baseline scoring ---------- #

def test_empty_repo_scores_low(empty_repo: Path) -> None:
    """Placeholder SoTs + dangling refs → stage BLOCK, every SoT at 0."""
    exit_code, data = run_readiness(empty_repo)
    assert exit_code == 2, f"expected BLOCK exit 2, got {exit_code}"

    stage = data["summary"]["current_stage"]
    assert stage["score"] < BLOCK_THRESHOLD, f"empty repo stage scored {stage['score']}"
    assert not stage["passing"]

    # Every SoT file should be a placeholder (score 0)
    for path, block in data["sot_files"].items():
        assert block["score"] == 0, f"{path} unexpectedly scored {block['score']}"


def test_healthy_repo_scores_above_warn(healthy_repo: Path) -> None:
    """Well-populated repo with resolved refs + tests → stage PASS."""
    exit_code, data = run_readiness(healthy_repo)
    assert exit_code == 0, f"expected PASS exit 0, got {exit_code}"

    stage = data["summary"]["current_stage"]
    assert stage["score"] >= PASS_THRESHOLD, f"healthy repo stage scored {stage['score']}"
    assert stage["passing"]

    # Every EPIC should pass the warn threshold
    for eid, block in data["epics"].items():
        assert block["score"] >= PASS_THRESHOLD, f"{eid} scored {block['score']}"


# ---------- Specific defect detection ---------- #

def test_dangling_ref_surfaces_as_spec_resolution_unmet(healthy_repo: Path) -> None:
    """Deleting a referenced SoT entry should produce a spec_resolution unmet criterion
    with `caused_by` pointing at the owning file."""
    api_file = healthy_repo / "SoT" / "SoT.API_CONTRACTS.md"
    text = api_file.read_text()
    # Remove API-002 entirely
    patched = text.split("## API-002")[0] + "## API-003" + text.split("## API-003", 1)[1]
    api_file.write_text(patched)

    _, data = run_readiness(healthy_repo)
    epic_block = next(iter(data["epics"].values()))
    spec_res_unmet = [c for c in epic_block["unmet_criteria"]
                      if c["dimension"] == "spec_resolution"]
    assert any(c.get("ref") == "API-002" for c in spec_res_unmet), \
        f"expected API-002 dangling; got {[c.get('ref') for c in spec_res_unmet]}"
    # The unmet should cite the owning SoT file
    api_002_unmet = next(c for c in spec_res_unmet if c.get("ref") == "API-002")
    assert api_002_unmet.get("caused_by") == "SoT/SoT.API_CONTRACTS.md"


def test_stub_testing_file_triggers_cap(healthy_repo: Path) -> None:
    """Replacing SoT.TESTING.md with a placeholder triggers the test_coverage_zero cap."""
    testing_file = healthy_repo / "SoT" / "SoT.TESTING.md"
    testing_file.write_text("# Testing\n\n*Pending PRD development*\n")

    _, data = run_readiness(healthy_repo)
    epic_block = next(iter(data["epics"].values()))
    cap_rules = [c["rule"] for c in epic_block["caps"]]
    assert "test_coverage_zero" in cap_rules, f"expected cap; got {cap_rules}"

    # The cap should cite SoT.TESTING.md specifically
    test_cap = next(c for c in epic_block["caps"] if c["rule"] == "test_coverage_zero")
    assert test_cap["caused_by"] == "SoT/SoT.TESTING.md"
    assert test_cap["caused_by_score"] == 0


def test_cross_layer_causal_links(healthy_repo: Path) -> None:
    """Every EPIC caused_by pointer must match a real sot_files key; every SoT
    file's consumed_by_epics must reference real EPIC keys. This is what makes
    the graph traversable."""
    _, data = run_readiness(healthy_repo)
    sot_paths = set(data["sot_files"].keys())
    epic_ids = set(data["epics"].keys())

    for eid, epic in data["epics"].items():
        for cap in epic.get("caps", []):
            if cap.get("caused_by"):
                assert cap["caused_by"] in sot_paths, \
                    f"{eid} cap cites unknown SoT: {cap['caused_by']}"
        for c in epic.get("unmet_criteria", []):
            if c.get("caused_by"):
                assert c["caused_by"] in sot_paths, \
                    f"{eid} unmet cites unknown SoT: {c['caused_by']}"

    for path, block in data["sot_files"].items():
        for consumer in block.get("consumed_by_epics", []):
            assert consumer in epic_ids, \
                f"{path} lists unknown consumer: {consumer}"


def test_dimension_override_disabled(healthy_repo: Path) -> None:
    """A dimension listed in dimension_overrides should be marked disabled in output,
    and the remaining weights should renormalize to sum ≈ 1.0."""
    _, data = run_readiness(healthy_repo)
    epic_block = next(iter(data["epics"].values()))
    dims = epic_block["dimensions"]

    # confidence_avg and status_maturity are disabled in the fixture EPIC
    assert dims["confidence_avg"].get("status") == "disabled", dims["confidence_avg"]
    assert dims["status_maturity"].get("status") == "disabled", dims["status_maturity"]

    # Active weights should sum to approximately 1.0
    active_weights = sum(d.get("weight", 0) for d in dims.values() if "weight" in d)
    assert abs(active_weights - 1.0) < 0.01, \
        f"weights sum to {active_weights}, expected ~1.0 after renormalization"


# ---------- Development Graph dimensions (v0.6→v0.7) ---------- #

# Implementable specs referenced by the healthy_repo EPIC-01 Section 3.
HEALTHY_IMPLEMENTABLE = [
    "BR-001", "BR-002", "BR-003",
    "API-001", "API-002", "API-003",
    "DBT-001", "DBT-002", "UJ-001",
]


def write_devgraph(repo: Path, spec_status: dict[str, str],
                   conformance: list[dict] | None = None) -> None:
    """Write a contract-shaped status/devgraph.json (see docs/DEVELOPMENT_GRAPH.md)."""
    nodes = [
        {"id": sid, "label": sid, "layer": "spec", "node_kind": sid.split("-")[0],
         "file_type": "concept", "source_file": "SoT/x.md", "status": status}
        for sid, status in spec_status.items()
    ]
    devgraph = {
        "directed": True, "multigraph": False, "schema_version": "0.1",
        "graph": {"scope": "EPIC-01", "scope_ids": list(spec_status),
                  "generated_by": "test", "readiness_ref": "status/readiness.json"},
        "nodes": nodes,
        "links": [],
        "conformance": conformance or [],
    }
    out = repo / "status" / "devgraph.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(devgraph))


def test_devgraph_absent_dimensions_dormant(healthy_repo: Path) -> None:
    """With no status/devgraph.json, both dev-graph dimensions auto-disable —
    they must NOT distort the score (the whole point of the dormant design)."""
    _, data = run_readiness(healthy_repo)
    dims = next(iter(data["epics"].values()))["dimensions"]
    assert dims["implementation_coverage"].get("status") == "not_applicable"
    assert dims["architecture_conformance"].get("status") == "not_applicable"
    # Dormant dimensions carry no weight.
    assert "weight" not in dims["implementation_coverage"]
    assert "weight" not in dims["architecture_conformance"]


def test_implementation_coverage_activates_when_built(healthy_repo: Path) -> None:
    """A dev graph marking every scoped spec implemented → coverage 100, active."""
    write_devgraph(healthy_repo, {sid: "implemented" for sid in HEALTHY_IMPLEMENTABLE})
    _, data = run_readiness(healthy_repo)
    dim = next(iter(data["epics"].values()))["dimensions"]["implementation_coverage"]
    assert dim.get("score") == 100.0, dim
    assert dim.get("weight", 0) > 0, "active dimension should carry renormalized weight"


def test_unbuilt_specs_triggers_cap(healthy_repo: Path) -> None:
    """Most scoped specs unbuilt → implementation_coverage < 50 → unbuilt_specs cap,
    with each unbuilt spec surfaced as an unmet criterion citing its owning file."""
    status = {sid: "unimplemented" for sid in HEALTHY_IMPLEMENTABLE}
    status["BR-001"] = "implemented"
    status["API-001"] = "implemented"  # 2 / 9 built ≈ 22% < 50
    write_devgraph(healthy_repo, status)

    _, data = run_readiness(healthy_repo)
    epic_block = next(iter(data["epics"].values()))

    cap_rules = [c["rule"] for c in epic_block["caps"]]
    assert "unbuilt_specs" in cap_rules, f"expected unbuilt_specs cap; got {cap_rules}"
    cap = next(c for c in epic_block["caps"] if c["rule"] == "unbuilt_specs")
    assert cap["cap"] == 60
    assert cap["caused_by"], "cap should cite the SoT file owning the most unbuilt specs"
    assert epic_block["score"] <= 60, "cap must bound the final score"

    unmet = [c for c in epic_block["unmet_criteria"]
             if c["dimension"] == "implementation_coverage"]
    refs = {c.get("ref") for c in unmet}
    assert "DBT-001" in refs and "BR-002" in refs, f"unbuilt specs not surfaced: {refs}"
    # Each unmet cites the owning SoT file (graph traversability).
    br_unmet = next(c for c in unmet if c.get("ref") == "BR-002")
    assert br_unmet.get("caused_by") == "SoT/SoT.BUSINESS_RULES.md"


def test_architecture_conformance_violation(healthy_repo: Path) -> None:
    """An ARC-001 conformance violation → architecture_conformance scores 0 and
    surfaces a drift unmet criterion citing the technical-decisions SoT file."""
    conformance = [{
        "arc_id": "ARC-001", "rule": "three-tier boundary must hold",
        "verdict": "violate",
        "violations": [{"source": "ui_widget_render", "target": "db_pool",
                        "source_location": "ui/widget.ts:9"}],
    }]
    write_devgraph(healthy_repo,
                   {sid: "implemented" for sid in HEALTHY_IMPLEMENTABLE},
                   conformance=conformance)

    _, data = run_readiness(healthy_repo)
    epic_block = next(iter(data["epics"].values()))
    dim = epic_block["dimensions"]["architecture_conformance"]
    assert dim.get("score") == 0.0, dim

    drift = [c for c in epic_block["unmet_criteria"]
             if c["dimension"] == "architecture_conformance"]
    assert any(c.get("ref") == "ARC-001" for c in drift), drift
    assert drift[0].get("caused_by") == "SoT/SoT.TECHNICAL_DECISIONS.md"


# ---------- Summary block ---------- #

def test_summary_top_blockers_ranking(empty_repo: Path) -> None:
    """When multiple SoT files are at 0, top_blockers should rank by (100-score) × #blocked."""
    _, data = run_readiness(empty_repo)
    blockers = data["summary"]["top_blockers"]
    # Should list SoT.TESTING.md or other 0-scored files with EPIC consumers
    assert len(blockers) > 0, "expected at least one top blocker in empty repo"
    # Ranking: impact descending
    impacts = [b["impact"] for b in blockers]
    assert impacts == sorted(impacts, reverse=True), f"not sorted by impact: {impacts}"
    # Impact formula holds
    for b in blockers:
        expected = (100 - b["score"]) * b["blocks"]
        assert abs(b["impact"] - expected) < 0.5, f"impact mismatch on {b['file']}"
