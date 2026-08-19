"""Repository-wide hygiene guards.

The distribution suite scans only *distributable* surfaces for machine-local paths. This test
extends the same patterns to every tracked text file so scratch notes, audits, and docs can never
re-introduce an absolute home path into the public repository (polish plan item 1.1n).
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FORBIDDEN_PATTERNS = {
    "macOS absolute home path": re.compile(r"/Users/[A-Za-z0-9._-]+(?:/|$)"),
    "Linux absolute home path": re.compile(r"(?i)/home/[a-z0-9._-]+(?:/|$)"),
    "Windows absolute home path": re.compile(r"(?i)\b[a-z]:\\users\\[^\\\s]+\\"),
    "scratchpad clone path": re.compile(r"/private/tmp/claude-[0-9]+/"),
}
TEXT_SUFFIXES = {".md", ".html", ".py", ".sh", ".yaml", ".yml", ".json", ".txt", ".css", ".tape", ".toml", ".cfg"}
# The pattern definitions themselves live here and in the distribution suite.
ALLOWLIST = {"tests/test_repo_hygiene.py", "tests/test_distribution.py"}


def _tracked_text_files() -> list[Path]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=REPO_ROOT, capture_output=True, text=True, check=True).stdout
    files = []
    for rel in out.split("\0"):
        if not rel or rel in ALLOWLIST:
            continue
        path = REPO_ROOT / rel
        if path.suffix.lower() in TEXT_SUFFIXES and path.is_file():
            files.append(path)
    return files


def test_no_machine_local_paths_anywhere_tracked() -> None:
    hits: list[str] = []
    for path in _tracked_text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                hits.append(f"{path.relative_to(REPO_ROOT)}: {label}")
    assert not hits, "machine-local paths in tracked files:\n" + "\n".join(hits)
