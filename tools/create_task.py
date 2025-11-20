#!/usr/bin/env python3
"""Generate a TASK-### scaffold and update the backlog.

Usage:
  python tools/create_task.py --title "Clarify onboarding" \
      --epic EPIC-01-onboarding --gate v0.7 --prd-version-impact "v0.6 → v0.7" \
      --github-issue https://github.com/org/repo/issues/123 --sot-id BR-021 --sot-id API-007
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
GHM_DIR = REPO_ROOT / ".ghm"
TASKS_DIR = GHM_DIR / "tasks"
BACKLOG_PATH = GHM_DIR / "task-backlog.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a Gear Heart TASK-### scaffold")
    parser.add_argument("--title", required=True, help="Concise statement of the work scope")
    parser.add_argument("--epic", required=True, help="EPIC identifier (e.g., EPIC-01-onboarding)")
    parser.add_argument("--gate", required=True, help="Lifecycle gate (e.g., v0.7)")
    parser.add_argument("--prd-version-impact", dest="prd_version", default="v0.x → v0.y",
                        help="Text describing the PRD version delta")
    parser.add_argument("--github-issue", dest="github_issue", default="",
                        help="GitHub issue URL (can be filled after creation)")
    parser.add_argument("--sot-id", dest="sot_ids", action="append", default=[],
                        help="Add a SoT ID reference (repeatable)")
    parser.add_argument("--owner", default="TBD", help="Default assignee or owner")
    parser.add_argument("--status", default="todo", choices=["todo", "in_progress", "blocked", "done"],
                        help="Initial backlog status")
    return parser.parse_args()


def load_backlog() -> Dict[str, List[Dict[str, str]]]:
    if BACKLOG_PATH.exists():
        raw = BACKLOG_PATH.read_text().strip()
        if raw:
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                raise SystemExit(f"Backlog file {BACKLOG_PATH} is not valid JSON/YAML")
    return {"tasks": []}


def next_task_id(existing: List[Dict[str, str]]) -> str:
    max_n = 0
    for entry in existing:
        task_id = entry.get("id", "")
        if task_id.startswith("TASK-"):
            try:
                max_n = max(max_n, int(task_id.split("-", 1)[1]))
            except ValueError:
                continue
    return f"TASK-{max_n + 1:03d}"


def write_yaml_file(path: Path, lines: List[str]) -> None:
    path.write_text("\n".join(lines) + "\n")


def ensure_dirs() -> None:
    if not GHM_DIR.exists():
        raise SystemExit("Missing .ghm/ directory. Run this script from the repo root after bootstrapping.")
    TASKS_DIR.mkdir(parents=True, exist_ok=True)


def build_task_yaml(args: argparse.Namespace, task_id: str) -> List[str]:
    sot_ids = args.sot_ids or ["TBD"]
    lines = [
        f"id: {task_id}",
        f"summary: \"{args.title}\"",
        f"github_issue: {args.github_issue or 'TBD'}",
        f"epic: {args.epic}",
        f"gate: {args.gate}",
        f"prd_version_impact: \"{args.prd_version}\"",
        f"status: {args.status}",
        f"owner: {args.owner}",
        "sot_ids:",
    ]
    for sid in sot_ids:
        lines.append(f"  - {sid}")
    lines.extend([
        "acceptance_criteria:",
        "  - \"Behavior verified via referenced TEST-IDs\"",
        "  - \"README + PRD updates merged\"",
        "required_tests:",
        "  - command: npm run test",
        "    evidence: TBD",
        "notes: |",
        "  Update after each session with references to commits, PRs, and SoT IDs.",
    ])
    return lines


def build_plan_md(task_id: str, args: argparse.Namespace) -> str:
    return f"""# {task_id} Plan\n\n- Mirrors GitHub Issue ({args.github_issue or 'TBD'}) 1:1.\n- References {args.epic} and gate {args.gate}.\n\n## Steps\n1. Confirm SoT IDs listed in the task YAML and Section 3A.\n2. Implement scoped work, naming commits with relevant IDs.\n3. Run required tests (`npm run test` by default) and capture evidence.\n4. Update README/PRD + append memory entries if decisions are durable.\n\n## Risks / Unknowns\n- [ ] Document blockers or follow-ups here.\n\n"""


def build_context_md(task_id: str) -> str:
    return f"""# {task_id} Context\n\n## Session Log\n- {datetime.utcnow().date()} — _Start log here. Include commands/tests/IDs each time you pause._\n\n## ID Deltas\n- Track BR-/API-/TEST- IDs touched during this session.\n\n## Decisions Worth Remembering\n- [ ] Use `tools/add_memory_entry.py` with `--task {task_id}` when the decision affects future work.\n\n## Next Steps\n- [ ] List remaining work before closing the GitHub issue.\n\n"""


def update_backlog(backlog: Dict[str, List[Dict[str, str]]], entry: Dict[str, str]) -> None:
    backlog.setdefault("tasks", []).append(entry)
    backlog["updated_at"] = datetime.now(timezone.utc).isoformat()
    BACKLOG_PATH.write_text(json.dumps(backlog, indent=2) + "\n")


def main() -> None:
    args = parse_args()
    ensure_dirs()
    backlog = load_backlog()
    task_id = next_task_id(backlog.get("tasks", []))

    task_folder = TASKS_DIR / task_id
    task_folder.mkdir(parents=True, exist_ok=False)

    write_yaml_file(task_folder / f"{task_id}.yaml", build_task_yaml(args, task_id))
    (task_folder / f"{task_id}-plan.md").write_text(build_plan_md(task_id, args))
    (task_folder / f"{task_id}-context.md").write_text(build_context_md(task_id))

    backlog_entry = {
        "id": task_id,
        "title": args.title,
        "epic": args.epic,
        "gate": args.gate,
        "prd_version": args.prd_version,
        "github_issue": args.github_issue or "TBD",
        "status": args.status,
        "path": str(task_folder.relative_to(REPO_ROOT)),
    }
    update_backlog(backlog, backlog_entry)

    print(f"Created {task_id} at {task_folder}")
    print(f"Backlog updated → {BACKLOG_PATH}")


if __name__ == "__main__":
    main()
