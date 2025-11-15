#!/usr/bin/env python3
"""Block ExitPlanMode until TASK-### + GitHub issue scaffolding exists."""
import json
import os
import sys

input_data = json.load(sys.stdin)
tool_name = input_data.get("tool_name", "")
project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "<project>")

if tool_name != "ExitPlanMode":
    sys.exit(0)

instructions = (
    "[SYSTEM]: Plan mode cannot be exited until you mirror the approved scope as both a GitHub issue and "
    "a Gear Heart task. Do the following before sending your next reply:\n\n"
    "1. Create or confirm the GitHub issue that matches this scope.\n"
    f"2. Run `python3 {project_dir}/tools/create_task.py --title \"<same summary>\" --epic EPIC-XX --gate v0.x --github-issue <URL>`\n"
    "   - Supply all referenced SoT IDs with `--sot-id BR-###` flags.\n"
    "3. Update the GitHub issue description with the generated TASK-### folder path.\n"
    f"4. Verify the new entry appears in `{project_dir}/.ghm/task-backlog.yaml`.\n"
    "5. Mention the TASK-### id and GitHub issue URL in your next response.\n\n"
    "If this work is a true one-line fix (no SoT impact), state that explicitly and why a task is unnecessary." )

output = {
    "decision": "block",
    "reason": instructions,
    "systemMessage": "[GHM] Plan approved — Claude must create the GitHub issue + TASK-### scaffold before coding."
}

print(json.dumps(output))
