#!/usr/bin/env python3
"""Block StopSession until docs/tests updated and validator run."""
import json
import os
import sys

input_data = json.load(sys.stdin)
if input_data.get("stop_hook_active"):
    sys.exit(0)

project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "<project>")
validator_cmd = f"python3 {project_dir}/tools/validate_ghm.py"

reason = (
    "[SYSTEM]: Before stopping you must align repo state with the Gear Heart scaffolding. Complete these checks, then "
    "resend your previous message if nothing else changes:\n\n"
    "1. Update the active `TASK-###.yaml`, plan, and context log with today’s progress plus the GitHub issue link.\n"
    f"2. Ensure `.ghm/task-backlog.yaml` reflects the new status (use `{project_dir}/tools/rebuild_backlog.py` if needed).\n"
    "3. Update Section 3A in the active EPIC with every ID touched.\n"
    "4. Note README/PRD changes or gate movement, and summarize blockers in README alerts if needed.\n"
    "5. Run required tests/linters referenced in the task plan and record results.\n"
    f"6. Log durable decisions via `python3 {project_dir}/tools/add_memory_entry.py` when applicable.\n"
    f"7. Run `{validator_cmd}` (or `--strict` if the repo profile/enforcement requires it) and confirm it passes.\n\n"
    "Only after every step is complete may you resend the message that triggered this hook. If no changes were needed, "
    "respond with the exact same text as before." )

output = {
    "decision": "block",
    "reason": reason,
    "systemMessage": "[GHM] Claude is updating docs/tests/backlog and running validate_ghm.py before ending the session."
}

print(json.dumps(output))
