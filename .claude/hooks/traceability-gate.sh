#!/usr/bin/env bash
# GHM Traceability Gate (PreToolUse: Write|Edit)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Purpose: Verify an active EPIC exists before allowing source code writes.
# Methodology files (SoT/, epics/, .claude/, *.md, *.json, *.yaml) are always allowed.
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

  # Allow methodology files freely — never gate these
  case "$file_path" in
    */SoT/*|*/epics/*|*/temp/*|*/.claude/*|*.md|*.json|*.yaml|*.yml)
      exit 0
      ;;
  esac

  # Check if any EPIC is In Progress
  if [ -d "epics" ]; then
    local active
    active=$(grep -rl "In Progress" epics/EPIC-*.md 2>/dev/null | head -1 || true)
    if [ -z "$active" ]; then
      local json_reason="No EPIC is currently 'In Progress'. Code changes should be traceable to an active EPIC. Create or activate an EPIC first, or confirm this is exploratory work."
      json_reason=$(printf '%s' "$json_reason" | sed 's/"/\\"/g')
      printf '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "%s"}}\n' "$json_reason"
      exit 0
    fi
  fi

  # Active EPIC found or no epics/ directory (template repo) — allow
  exit 0
}

main
