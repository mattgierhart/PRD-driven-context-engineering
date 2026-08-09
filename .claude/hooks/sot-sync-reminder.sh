#!/usr/bin/env bash
# GHM SoT Sync Reminder (PostToolUse: Write|Edit)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Purpose: After source code writes, remind agent to update SoT files.
# Methodology files are excluded (they ARE the SoT).
#
# Dependencies: Bash, grep, awk, od (standard utilities)
set -euo pipefail

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_json.sh
. "$HOOK_DIR/_json.sh"

main() {
  local input
  input=$(cat)

  # Extract file_path from tool_input
  local file_path
  file_path=$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$file_path" ]; then
    exit 0
  fi

  # Skip methodology files — they don't need SoT reminders
  case "$file_path" in
    SoT/*|*/SoT/*|epics/*|*/epics/*|temp/*|*/temp/*|.claude/*|*/.claude/*|*.md)
      exit 0
      ;;
  esac

  local context="Reminder: You just modified source code (\`${file_path##*/}\`). Per documentation discipline rules, SoT/ files should be updated *during* code changes, not after. If this change affects any BR-, API-, DBT-, or TEST- entries, update them now before continuing."
  local json_context
  json_context=$(json_escape "$context")
  printf '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "%s"}}\n' "$json_context"

  exit 0
}

main
