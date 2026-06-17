#!/usr/bin/env bash
# GHM Subagent Memory Load Hook (SubagentStart)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: POSIX shell, sed, awk (standard utilities)
# No external packages required
set -euo pipefail

# --- Helpers ---

json_output() {
  local context="$1"
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": "%s"}}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin JSON (contains agent_id, agent_type)
  local input
  input=$(cat)

  # Extract agent_type from stdin JSON (maps to agent directory name)
  local agent_type
  agent_type=$(printf '%s' "$input" | sed -n 's/.*"agent_type"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$agent_type" ]; then
    exit 0
  fi

  local agent_dir=".claude/agents/${agent_type}"
  local memory_file="${agent_dir}/MEMORY.md"

  # If no memory file exists, nothing to inject
  if [ ! -f "$memory_file" ]; then
    exit 0
  fi

  local memory_content
  memory_content=$(cat "$memory_file")

  local directive="## Agent Memory Loaded

The following project memory was loaded from \`${memory_file}\`:

${memory_content}

**Reminder**: Update this memory before returning results."

  json_output "$directive"
  exit 0
}

main
