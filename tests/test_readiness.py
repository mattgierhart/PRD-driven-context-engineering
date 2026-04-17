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
