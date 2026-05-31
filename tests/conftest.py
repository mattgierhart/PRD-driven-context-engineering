"""Pytest configuration and shared fixtures for readiness scoring tests."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest

# Make the scripts/ directory importable so tests can reach `_readiness.*`.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def empty_repo(tmp_path: Path) -> Path:
    """A minimal repo with placeholder SoT files — should score near 0."""
    dst = tmp_path / "empty_repo"
    shutil.copytree(FIXTURES_DIR / "empty_repo", dst)
    return dst


@pytest.fixture
def healthy_repo(tmp_path: Path) -> Path:
    """A well-populated repo — should score ≥ 70 on its current stage."""
    dst = tmp_path / "healthy_repo"
    shutil.copytree(FIXTURES_DIR / "healthy_repo", dst)
    return dst
