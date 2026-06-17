#!/usr/bin/env bash
# GHM SoT Sync Reminder (PostToolUse: Write|Edit)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Purpose: After source code writes, remind agent to update SoT files.
# Methodology files are excluded (they ARE the SoT).
#
# Dependencies: POSIX shell, grep (standard utilities)
set -euo pipefail

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
    */SoT/*|*/epics/*|*/temp/*|*/.claude/*|*.md|*.json|*.yaml|*.yml)
      exit 0
      ;;
  esac

  local context="Reminder: You just modified source code (\`${file_path##*/}\`). Per documentation discipline rules, SoT/ files should be updated *during* code changes, not after. If this change affects any BR-, API-, DBT-, or TEST- entries, update them now before continuing."
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "%s"}}\n' "$json_context"

  exit 0
}

main
