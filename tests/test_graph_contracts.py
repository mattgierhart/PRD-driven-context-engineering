"""Tests for the graph-contract tools: validate-edges.py (U2) and asof.py (U1).

U2 — required cross-reference edges: run the real CLI against small built repos
and assert on exit code + JSON, mirroring test_readiness.py's subprocess style.
U1 — valid-time reconstruction: import `as_of` and assert it reconstructs the
decision set as of a past version against the committed temporal_repo fixture.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES = REPO_ROOT / "tests" / "fixtures"
VALIDATE_EDGES = REPO_ROOT / "scripts" / "validate-edges.py"
VALIDATE_IDS = REPO_ROOT / "scripts" / "validate-ids.sh"

# conftest.py puts scripts/ on sys.path, so asof imports cleanly.
from asof import as_of  # noqa: E402


# ---------- helpers ---------- #

def _write(repo: Path, rel: str, content: str) -> None:
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def _edge_repo(tmp_path: Path, rules_yaml: str, sot: dict[str, str]) -> Path:
    repo = tmp_path / "edge_repo"
    registry = (
        "id_prefixes:\n"
        "  BR: { file: SoT/SoT.BUSINESS_RULES.md }\n"
        "  UJ: { file: SoT/SoT.USER_JOURNEYS.md }\n"
        "  SCR: { file: SoT/SoT.USER_JOURNEYS.md }\n"
        "  API: { file: SoT/SoT.API_CONTRACTS.md }\n"
        "  TEST: { file: SoT/SoT.TESTING.md }\n"
    )
    _write(repo, ".claude/domain-profile.yaml", registry + rules_yaml)
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


@pytest.mark.parametrize(
    "rules",
    [
        "required_edges:\n  - { from: UNKNOWN, requires: SCR }\n",
        "required_edges:\n  - { from: UJ, requires: UNKNOWN }\n",
        "required_edges:\n  - { from: UJ, requires: SCR, direction: sideways }\n",
        "required_edges:\n  - { from: UJ, requires: SCR, severity: blok }\n",
        "required_edges:\n  - { from: UJ, requires: SCR, severty: block }\n",
        "required_edges:\n  - { from: UJ, requires: SCR, directon: inbound }\n",
        "required_edges:\n  - { from: UJ, requires: 123 }\n",
        "required_edges: {}\n",
    ],
)
def test_invalid_edge_rule_configuration_fails_closed(tmp_path: Path, rules: str) -> None:
    repo = _edge_repo(
        tmp_path,
        rules,
        {"SoT/SoT.USER_JOURNEYS.md": "## UJ-001 | Journey\n- durable entry.\n"},
    )
    code, data = _run_edges(repo)
    assert code == 2
    assert data.get("configuration_error")


def test_validate_ids_preserves_edge_configuration_exit_two(tmp_path: Path) -> None:
    repo = _edge_repo(
        tmp_path,
        "required_edges:\n  - { from: UJ, requires: SCR, severity: blok }\n",
        {"SoT/SoT.USER_JOURNEYS.md": "## UJ-001 | Journey\n- durable entry.\n"},
    )
    result = subprocess.run(
        ["bash", str(VALIDATE_IDS), "--quiet"],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "invalid required_edges configuration" in result.stderr


def test_validate_ids_fails_closed_without_semantic_runtime(tmp_path: Path) -> None:
    repo = _edge_repo(
        tmp_path,
        "required_edges:\n  - { from: UJ, requires: SCR, severity: block }\n",
        {"SoT/SoT.USER_JOURNEYS.md": "## UJ-001 | Journey\n- durable entry.\n"},
    )
    bin_dir = tmp_path / "shell-tools"
    bin_dir.mkdir()
    for name in (
        "bash", "comm", "cut", "dirname", "find", "grep", "head", "mktemp",
        "rm", "sed", "sort", "tr", "uniq", "wc",
    ):
        source = shutil.which(name)
        assert source, name
        (bin_dir / name).symlink_to(source)

    result = subprocess.run(
        ["/bin/bash", str(VALIDATE_IDS), "--quiet"],
        cwd=repo,
        env={**os.environ, "PATH": str(bin_dir), "PRD_CE_PROJECT_ROOT": str(repo)},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "python3 is required for semantic edge validation" in result.stderr


@pytest.mark.parametrize("kind", ["missing", "absolute", "traversal", "symlink"])
def test_validate_ids_scope_rejects_unsafe_or_missing_paths(
    tmp_path: Path, kind: str,
) -> None:
    repo = tmp_path / "scope-repo"
    repo.mkdir()
    actual = repo / "actual.md"
    actual.write_text("# Guide\n")
    outside = tmp_path / "outside.md"
    outside.write_text("# Outside\n")
    if kind == "missing":
        scope = "missing.md"
    elif kind == "absolute":
        scope = str(actual)
    elif kind == "traversal":
        scope = "../outside.md"
    else:
        (repo / "linked.md").symlink_to(actual)
        scope = "linked.md"

    result = subprocess.run(
        ["bash", str(VALIDATE_IDS), "--scope", scope],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert "invalid --scope path" in result.stderr


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


def test_asof_compound_id_label_excludes_the_id(tmp_path: Path) -> None:
    repo = tmp_path / "compound_asof"
    _write(
        repo,
        "SoT/SoT.ADOPTION.md",
        "## ADO-STAGE-001: Early adopters\n\n"
        "**Valid From**: v0.1\n**Valid To**: —\n\nA durable adoption decision.\n",
    )
    result = as_of(repo, "v0.1", ["ADO"])
    assert result["current"] == [{
        "id": "ADO-STAGE-001",
        "label": "Early adopters",
        "valid_from": "v0.1",
        "valid_to": "—",
        "invalidated_by": None,
    }]


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
