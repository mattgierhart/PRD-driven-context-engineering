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

from _readiness.common import (
    HEADING_DEF_RE,
    ID_RE,
    collect_all_references,
    epic_id_from_filename,
    expand_ranges,
    index_all_entries,
    iter_epic_files,
    load_domain_profile,
)
from _readiness.epic import EpicContext, compute_dependency_readiness
from _readiness.stage import compute_cross_ref_integrity, index_all_ids

REPO_ROOT = Path(__file__).resolve().parent.parent
READINESS_CLI = REPO_ROOT / "scripts" / "readiness.py"

PASS_THRESHOLD = 70
BLOCK_THRESHOLD = 50


def test_id_regexes_support_compounds_and_epic_compatibility() -> None:
    accepted = {"BR-001", "ADO-STAGE-001", "BR-FEA-001", "EPIC-01", "EPIC-001"}
    rejected = {
        "BR-01", "ADO-STAGE-01", "ADO-STAGE-EXTRA-001", "API-EPIC-01",
        "EPIC-SUB-001", "xBR-001", "BR-001st", "BR-001-extra",
    }
    for value in accepted:
        match = ID_RE.search(value)
        assert match and match.group(0) == value
        heading = HEADING_DEF_RE.search(f"# {value} Example")
        assert heading and heading.group(1) == value
    for value in rejected:
        assert ID_RE.fullmatch(value) is None
        assert HEADING_DEF_RE.search(f"## {value} Example") is None


def test_id_range_expansion_requires_matching_prefixes_and_valid_shape() -> None:
    assert expand_ranges("ADO-STAGE-001 → ADO-STAGE-003") == {
        "ADO-STAGE-001", "ADO-STAGE-002", "ADO-STAGE-003",
    }
    assert expand_ranges("EPIC-01 -> EPIC-03") == {"EPIC-01", "EPIC-02", "EPIC-03"}
    assert expand_ranges("ADO-STAGE-001 → API-003") == set()
    assert expand_ranges("ADO-STAGE-EXTRA-001 → 003") == set()
    assert expand_ranges("EPIC-SUB-001 → 003") == set()


def test_epic_file_discovery_accepts_only_exact_execution_filenames(tmp_path: Path) -> None:
    epics = tmp_path / "epics"
    epics.mkdir()
    accepted = {"EPIC-01.md", "EPIC-001-foundation.md", "EPIC-100-release_1.md"}
    rejected = {
        "EPIC-0junk.md", "EPIC-01x.md", "EPIC-001-.md", "EPIC-SUB-001.md",
        "EPIC_TEMPLATE.md",
    }
    for name in accepted | rejected:
        (epics / name).write_text(f"# {name}\n")

    discovered = iter_epic_files(epics)
    assert {path.name for path in discovered} == accepted
    assert {epic_id_from_filename(path) for path in discovered} == {
        "EPIC-01", "EPIC-001", "EPIC-100",
    }
    for name in rejected:
        assert epic_id_from_filename(epics / name) is None


def test_explicit_domain_profile_is_a_closed_registry(tmp_path: Path) -> None:
    profile = tmp_path / ".claude" / "domain-profile.yaml"
    profile.parent.mkdir()
    profile.write_text(
        "id_prefixes:\n"
        "  ZZZ:\n"
        "    file: SoT/SoT.CUSTOM.md\n"
    )
    sot = tmp_path / "SoT"
    sot.mkdir()
    (sot / "SoT.CUSTOM.md").write_text(
        "## ZZZ-001: Registered\n\n"
        "## BR-001: Must remain invisible\n"
    )

    assert set(load_domain_profile(tmp_path)) == {"ZZZ"}
    assert index_all_ids(tmp_path) == {"ZZZ": {"ZZZ-001"}}


def test_guides_and_malformed_epics_do_not_enter_the_readiness_graph(tmp_path: Path) -> None:
    profile = tmp_path / ".claude" / "domain-profile.yaml"
    profile.parent.mkdir()
    profile.write_text(
        "id_prefixes:\n"
        "  BR: { file: SoT/SoT.BUSINESS_RULES.md }\n"
        "  EPIC: { file: epics/ }\n"
    )
    sot = tmp_path / "SoT"
    sot.mkdir()
    (sot / "SoT.BUSINESS_RULES.md").write_text(
        "## BR-001: Accepted\n\nA durable rule with rationale and enforcement.\n"
    )
    (sot / "SoT.README.md").write_text("Guide examples: BR-001 BR-999\n")
    (sot / "SoT.UNIQUE_ID_SYSTEM.md").write_text(
        "## BR-999: Instructional example\n\nReferences BR-001.\n"
    )
    epics = tmp_path / "epics"
    epics.mkdir()
    (epics / "EPIC-01x-malformed.md").write_text(
        "# EPIC-01x\n\n## BR-999: Lookalike definition\n\nReferences BR-001.\n"
    )

    entries = index_all_entries(tmp_path)
    references = collect_all_references(tmp_path)
    id_index = index_all_ids(tmp_path)
    score, unmet = compute_cross_ref_integrity(tmp_path, id_index, {"BR", "EPIC"})

    assert set(entries) == {"BR-001"}
    assert "BR-999" not in references
    assert references["BR-001"] == {"SoT/SoT.BUSINESS_RULES.md"}
    assert id_index == {"BR": {"BR-001"}}
    assert score == 100
    assert unmet == []


def test_dependency_lookup_does_not_accept_prefix_collisions(tmp_path: Path) -> None:
    epics = tmp_path / "epics"
    epics.mkdir()
    (epics / "EPIC-010-lookalike.md").write_text(
        "# EPIC-010\n\n> **State**: Complete\n"
    )
    ctx = EpicContext(
        id="EPIC-002",
        file=epics / "EPIC-002-consumer.md",
        inputs={"depends_on_epics": ["EPIC-01"]},
    )

    score, unmet = compute_dependency_readiness(ctx, tmp_path)
    assert score == 0
    assert unmet and unmet[0]["ref"] == "EPIC-01"

    (epics / "EPIC-01-dependency.md").write_text(
        "# EPIC-01\n\n> **State**: Complete\n"
    )
    score, unmet = compute_dependency_readiness(ctx, tmp_path)
    assert score == 100
    assert unmet == []


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


def test_run_rebuilds_output_without_stale_epics(healthy_repo: Path) -> None:
    """Each run starts fresh, so removed EPICs cannot survive from an older JSON report."""
    _, first = run_readiness(healthy_repo)
    assert first["epics"]
    for epic in (healthy_repo / "epics").glob("EPIC-*.md"):
        if epic.name != "EPIC_TEMPLATE.md":
            epic.unlink()
    _, second = run_readiness(healthy_repo)
    assert second["epics"] == {}


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
