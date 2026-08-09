#!/usr/bin/env bash
# GHM Subagent Memory Load Hook (SubagentStart)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: Bash, sed, awk, od (standard utilities)
# No external packages required
set -euo pipefail

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_json.sh
. "$HOOK_DIR/_json.sh"

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null || true)"
fi
[ -n "$PROJECT_ROOT" ] && [ -d "$PROJECT_ROOT" ] && cd "$PROJECT_ROOT"

# --- Helpers ---

json_output() {
  local context="$1"
  local json_context
  json_context=$(json_escape "$context")
  printf '{"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": "%s"}}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin JSON (contains agent_id, agent_type)
  local input
  input=$(cat)

  # Extract agent_type from stdin JSON. Plugin-hosted agents are scoped as
  # "plugin-name:agent-name"; consumer memory remains under the unscoped name.
  local agent_type
  agent_type=$(printf '%s' "$input" | sed -n 's/.*"agent_type"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$agent_type" ]; then
    exit 0
  fi

  local agent_name=""
  case "$agent_type" in
    prd-ce:*) agent_name="${agent_type#prd-ce:}" ;;
    *:*) exit 0 ;; # Never disclose consumer memory to another plugin's scoped agent.
    *) agent_name="$agent_type" ;;
  esac
  case "$agent_name" in
    ""|*[!A-Za-z0-9_-]*) exit 0 ;;
  esac

  local agent_dir=".claude/agents/${agent_name}"
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
