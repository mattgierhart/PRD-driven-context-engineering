#!/usr/bin/env python3
"""Validate Gear Heart runtime state (tasks, backlog, memory)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
GHM_DIR = REPO_ROOT / ".ghm"
TASKS_DIR = GHM_DIR / "tasks"
BACKLOG_PATH = GHM_DIR / "task-backlog.yaml"
MEMORY_PATH = GHM_DIR / "memory.jsonl"
CONFIG_PATH = GHM_DIR / "config.yaml"


def _strip_comment(value: str) -> str:
    return value.split("#", 1)[0].strip()

def parse_simple_yaml(path: Path) -> Dict[str, str]:
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


def load_config() -> Dict[str, str]:
    config = {"profile": "standard", "enforcement_level": "standard"}
    if not CONFIG_PATH.exists():
        return config
    for raw in CONFIG_PATH.read_text().splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        cleaned = _strip_comment(value)
        if cleaned:
            config[key.strip()] = cleaned
    return config


def load_backlog() -> Dict[str, List[Dict[str, str]]]:
    if not BACKLOG_PATH.exists():
        return {"tasks": []}
    try:
        return json.loads(BACKLOG_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Backlog file is not valid JSON: {exc}")


def collect_tasks() -> Dict[str, Dict[str, str]]:
    tasks: Dict[str, Dict[str, str]] = {}
    if not TASKS_DIR.exists():
        return tasks
    for folder in sorted(TASKS_DIR.glob("TASK-*")):
        if not folder.is_dir():
            continue
        yaml_path = folder / f"{folder.name}.yaml"
        if not yaml_path.exists():
            raise SystemExit(f"Task folder missing YAML file: {yaml_path}")
        data = parse_simple_yaml(yaml_path)
        data["path"] = str(folder.relative_to(REPO_ROOT))
        tasks[folder.name] = data
    return tasks


def validate_memory(tasks: Dict[str, Dict[str, str]], strict: bool) -> Tuple[List[str], List[str]]:
    warnings: List[str] = []
    errors: List[str] = []
    if not MEMORY_PATH.exists():
        warnings.append("memory.jsonl missing (append-only log not started)")
        return warnings, errors
    for lineno, raw in enumerate(MEMORY_PATH.read_text().splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        try:
            entry = json.loads(stripped)
        except json.JSONDecodeError:
            errors.append(f"memory.jsonl line {lineno} is not valid JSON")
            continue
        task_id = entry.get("task", "")
        if not task_id:
            warnings.append(f"memory.jsonl line {lineno} missing task reference")
        elif task_id not in tasks:
            msg = f"memory.jsonl line {lineno} references missing task {task_id}"
            (errors if strict else warnings).append(msg)
    return warnings, errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate .ghm runtime state")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    config = load_config()
    strict_mode = args.strict or config.get("enforcement_level") == "strict"

    tasks = collect_tasks()
    backlog = load_backlog()
    backlog_entries = backlog.get("tasks", [])
    warnings: List[str] = []
    errors: List[str] = []

    backlog_ids = set()
    for entry in backlog_entries:
        task_id = entry.get("id")
        if not task_id:
            errors.append("Backlog entry missing id")
            continue
        backlog_ids.add(task_id)
        if task_id not in tasks:
            errors.append(f"Backlog references {task_id} but folder is missing")
            continue
        task_data = tasks[task_id]
        rel_path = entry.get("path")
        if rel_path != task_data.get("path"):
            warnings.append(f"{task_id}: backlog path {rel_path} != actual {task_data.get('path')}")
        issue = entry.get("github_issue", "")
        if not issue or issue.upper() == "TBD":
            msg = f"{task_id}: GitHub issue not recorded"
            (errors if strict_mode else warnings).append(msg)

    for task_id, data in tasks.items():
        if task_id not in backlog_ids:
            warnings.append(f"{task_id}: present on disk but missing from backlog (run rebuild_backlog.py)")
        required = ["summary", "epic", "gate", "prd_version_impact"]
        for field in required:
            if not data.get(field):
                errors.append(f"{task_id}: missing {field} in {task_id}.yaml")

    mem_warnings, mem_errors = validate_memory(tasks, strict_mode)
    warnings.extend(mem_warnings)
    errors.extend(mem_errors)

    if errors or (strict_mode and warnings):
        for msg in errors:
            print(f"[ERROR] {msg}")
        if strict_mode:
            for msg in warnings:
                print(f"[WARN] {msg}")
        sys.exit(1)

    for msg in warnings:
        print(f"[WARN] {msg}")
    print(f"Validation complete — profile={config.get('profile')} enforcement={config.get('enforcement_level')} tasks={len(tasks)}")


if __name__ == "__main__":
    main()
