#!/usr/bin/env bash
# GHM Traceability Gate (PreToolUse: Write|Edit)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Purpose: Verify an active EPIC exists before allowing source code writes.
# Methodology paths (SoT/, epics/, temp/, .claude/) and Markdown documentation are allowed.
# Product JSON/YAML remains governed like source code.
#
# Dependencies: Bash, grep, awk, od (standard utilities)
set -euo pipefail

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_json.sh
. "$HOOK_DIR/_json.sh"

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null || true)"
fi
[ -n "$PROJECT_ROOT" ] && [ -d "$PROJECT_ROOT" ] && cd "$PROJECT_ROOT"

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
    SoT/*|*/SoT/*|epics/*|*/epics/*|temp/*|*/temp/*|.claude/*|*/.claude/*|*.md)
      exit 0
      ;;
  esac

  # Require exactly one numeric EPIC whose State field is exactly `In Progress`.
  local active_count=0 epic state
  if [ -d "epics" ]; then
    for epic in \
      epics/EPIC-[0-9][0-9].md epics/EPIC-[0-9][0-9]-*.md \
      epics/EPIC-[0-9][0-9][0-9].md epics/EPIC-[0-9][0-9][0-9]-*.md; do
      [ -f "$epic" ] || continue
      state=$(sed -n 's/^>[[:space:]]*\*\*State\*\*:[[:space:]]*`\{0,1\}\([^`|]*\).*/\1/p' "$epic" \
        | head -1 | sed 's/[[:space:]]*$//' || true)
      [ "$state" = "In Progress" ] && active_count=$((active_count + 1))
    done
  fi
  if [ "$active_count" -ne 1 ]; then
    local json_reason="Expected exactly one EPIC with State 'In Progress'; found ${active_count}. Source-code changes require an owner-approved v0.7+ execution context."
    json_reason=$(json_escape "$json_reason")
    printf '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "%s"}}\n' "$json_reason"
  fi

  exit 0
}

main
