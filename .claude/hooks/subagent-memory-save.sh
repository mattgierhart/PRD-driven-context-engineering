#!/usr/bin/env bash
# GHM Subagent Memory Save Hook (SubagentStop)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: POSIX shell, grep, sed, awk (standard utilities)
# No external packages required
set -euo pipefail

# --- Helpers ---

json_output() {
  local context="$1"
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"systemMessage": "%s"}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin JSON (contains agent_id, agent_type, agent_transcript_path, stop_hook_active)
  local input
  input=$(cat)

  # Extract agent_type from stdin JSON
  local agent_type
  agent_type=$(printf '%s' "$input" | sed -n 's/.*"agent_type"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$agent_type" ]; then
    exit 0
  fi

  local agent_dir=".claude/agents/${agent_type}"
  local memory_file="${agent_dir}/MEMORY.md"
  local hook_dir
  hook_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

  local reminder=""

  # --- Memory checkpoint ---
  if [ -f "$memory_file" ]; then
    reminder="## Memory Update Checkpoint

Agent: ${agent_type}
Memory file: ${memory_file}

Before concluding, ensure the following were captured:
  - New patterns discovered -> Patterns Learned table
  - Decisions made -> Key Decisions table
  - Collaboration friction -> Relevant section
  - Open questions -> Open Questions list"
  fi

  # --- Post-delegation drift check ---
  if [ -f "status/metrics.json" ] && [ -f "README.md" ]; then
    local drift_check="${hook_dir}/metrics_drift_check.py"
    if [ -f "$drift_check" ]; then
      local drift_output
      local drift_exit=0
      drift_output=$(python3 "$drift_check" 2>&1) || drift_exit=$?
      if [ "$drift_exit" -ne 0 ] && [ -n "$drift_output" ]; then
        local drift_msg="

## Post-Delegation Drift Check

${drift_output}

The subagent's work may have changed metrics without cascading.
Review and update README Truth Table before continuing."
        reminder="${reminder}${drift_msg}"
      fi
    fi
  fi

  # Only output if there's something to say
  if [ -n "$reminder" ]; then
    json_output "$reminder"
  fi

  exit 0
}

main
