"""Tests for the graph-contract tools: validate-edges.py (U2) and asof.py (U1).

U2 — required cross-reference edges: run the real CLI against small built repos
and assert on exit code + JSON, mirroring test_readiness.py's subprocess style.
U1 — valid-time reconstruction: import `as_of` and assert it reconstructs the
decision set as of a past version against the committed temporal_repo fixture.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES = REPO_ROOT / "tests" / "fixtures"
VALIDATE_EDGES = REPO_ROOT / "scripts" / "validate-edges.py"

# conftest.py puts scripts/ on sys.path, so asof imports cleanly.
from asof import as_of  # noqa: E402


# ---------- helpers ---------- #

def _write(repo: Path, rel: str, content: str) -> None:
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def _edge_repo(tmp_path: Path, rules_yaml: str, sot: dict[str, str]) -> Path:
    repo = tmp_path / "edge_repo"
    _write(repo, ".claude/domain-profile.yaml", rules_yaml)
    for rel, content in sot.items():
        _write(repo, rel, content)
    return repo


def _run_edges(repo: Path) -> tuple[int, dict]:
    result = subprocess.run(
        [sys.executable, str(VALIDATE_EDGES), "--repo", str(repo), "--json"],
        capture_output=True, text=True,
    )
    return result.returncode, json.loads(result.stdout)


# ---------- U2: required cross-reference edges ---------- #

def test_no_rules_validates_clean(tmp_path: Path) -> None:
    """An empty `required_edges` list is a no-op — exit 0, zero violations."""
    repo = _edge_repo(
        tmp_path,
        "required_edges: []\n",
        {"SoT/SoT.BUSINESS_RULES.md": "## BR-001 | A rule\n- something.\n"},
    )
    code, data = _run_edges(repo)
    assert code == 0
    assert data["violations"] == []


def test_outbound_block_flags_missing_edge(tmp_path: Path) -> None:
    """from: UJ requires: SCR (block) — a UJ with no SCR reference fails the gate."""
    rules = (
        "required_edges:\n"
        "  - { from: UJ, requires: SCR, direction: outbound, severity: block }\n"
    )
    journeys = (
        "## UJ-001 | Onboarding\n- references API-001 only.\n\n"
        "## UJ-002 | Checkout\n- uses SCR-010.\n\n"
        "## SCR-010 | Cart\n- a screen.\n"
    )
    repo = _edge_repo(tmp_path, rules, {"SoT/SoT.USER_JOURNEYS.md": journeys})
    code, data = _run_edges(repo)

    assert code == 1, "block-severity violation must fail (exit 1)"
    flagged = {v["id"] for v in data["violations"]}
    assert "UJ-001" in flagged       # no SCR edge
    assert "UJ-002" not in flagged    # references SCR-010 → satisfied
    assert data["blocking"] == 1


def test_inbound_warn_is_nonfatal(tmp_path: Path) -> None:
    """from: API requires: TEST inbound (warn) — missing test reported, but exit 0."""
    rules = (
        "required_edges:\n"
        "  - { from: API, requires: TEST, direction: inbound, severity: warn }\n"
    )
    repo = _edge_repo(tmp_path, rules, {
        "SoT/SoT.API_CONTRACTS.md": "## API-001 | Login\n- endpoint.\n\n## API-002 | Logout\n- endpoint.\n",
        "SoT/SoT.TESTING.md": "## TEST-001 | login test\n- verifies API-001.\n",
    })
    code, data = _run_edges(repo)

    assert code == 0, "warn-severity violations must not fail the gate"
    flagged = {v["id"] for v in data["violations"]}
    assert "API-002" in flagged       # no TEST points back at it
    assert "API-001" not in flagged    # TEST-001 references it → satisfied
    assert data["blocking"] == 0


# ---------- U1: valid-time reconstruction ---------- #

def test_asof_before_supersession() -> None:
    """As of v0.6, ARC-001 is authoritative and its replacement is still future."""
    result = as_of(FIXTURES / "temporal_repo", "v0.6", ["ARC", "TECH"])
    current = {d["id"] for d in result["current"]}
    future = {d["id"] for d in result["future"]}

    assert current == {"ARC-001", "TECH-001"}
    assert "ARC-002" in future          # Valid From v0.8 > v0.6


def test_asof_after_supersession() -> None:
    """As of v0.8, ARC-002 takes over and ARC-001 moves to the superseded set."""
    result = as_of(FIXTURES / "temporal_repo", "v0.8", ["ARC", "TECH"])
    current = {d["id"] for d in result["current"]}
    superseded = {d["id"]: d for d in result["superseded"]}

    assert current == {"ARC-002", "TECH-001"}
    assert "ARC-001" in superseded
    assert superseded["ARC-001"]["invalidated_by"] == "ARC-002"


def test_asof_cli_smoke() -> None:
    """The CLI runs end-to-end and emits valid JSON."""
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "asof.py"),
         "v0.6", "--repo", str(FIXTURES / "temporal_repo"), "--json"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["target"] == "v0.6"
