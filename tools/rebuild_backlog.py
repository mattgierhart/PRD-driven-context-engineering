#!/usr/bin/env python3
"""Rebuild .ghm/task-backlog.yaml from existing TASK-### folders."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
GHM_DIR = REPO_ROOT / ".ghm"
TASKS_DIR = GHM_DIR / "tasks"
BACKLOG_PATH = GHM_DIR / "task-backlog.yaml"


def parse_simple_yaml(path: Path) -> Dict[str, str]:
    """Minimal YAML parser for the task metadata fields we care about."""
    data: Dict[str, str] = {}
    current_list: str | None = None
    for raw in path.read_text().splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_list:
            value = stripped[2:].strip().strip('"')
            data.setdefault(current_list, []).append(value)
            continue
        if ":" not in stripped:
            current_list = None
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {"|", ">"}:
            data[key] = ""
            current_list = None
        elif not value:
            data[key] = []
            current_list = key
        else:
            data[key] = value.strip('"')
            current_list = None
    return data


def rebuild() -> None:
    if not TASKS_DIR.exists():
        raise SystemExit("No tasks directory found at .ghm/tasks. Nothing to rebuild.")

    entries: List[Dict[str, str]] = []
    for folder in sorted(TASKS_DIR.glob("TASK-*")):
        if not folder.is_dir():
            continue
        yaml_path = folder / f"{folder.name}.yaml"
        if not yaml_path.exists():
            print(f"[warn] Missing {yaml_path}")
            continue
        data = parse_simple_yaml(yaml_path)
        entry = {
            "id": folder.name,
            "title": data.get("summary", folder.name).strip('"'),
            "epic": data.get("epic", "TBD"),
            "gate": data.get("gate", "v0.x"),
            "prd_version": data.get("prd_version_impact", "v0.x → v0.y"),
            "github_issue": data.get("github_issue", "TBD"),
            "status": data.get("status", "todo"),
            "path": str(folder.relative_to(REPO_ROOT)),
        }
        entries.append(entry)

    backlog = {"tasks": entries, "updated_at": datetime.now(timezone.utc).isoformat()}
    BACKLOG_PATH.write_text(json.dumps(backlog, indent=2) + "\n")
    print(f"Rebuilt backlog with {len(entries)} tasks → {BACKLOG_PATH}")


if __name__ == "__main__":
    rebuild()
