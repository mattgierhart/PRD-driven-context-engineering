#!/usr/bin/env bash
set -euo pipefail

# Governance check hook for Phase 6
# Emits event if template context is available
# Safe to fail silently if telemetry is unavailable

if [ -f ".claude/settings.json" ] && { [ -f "CLAUDE.md" ] || [ -f ".claude/CLAUDE.md" ]; }; then
  # Template context is present, emit governance event
  payload=$(jq -n \
    --arg session_id "${CLAUDE_SESSION_ID:-unknown}" \
    --arg cwd "$PWD" \
    --arg repo_name "$(basename "$PWD")" \
    --arg template_present "true" \
    '{session_id:$session_id,cwd:$cwd,repo_name:$repo_name,template_present:$template_present}')

  printf '%s' "$payload" | "$HOME/.claude/hooks/otel-lib.sh" \
    emit_otel "governance.template.context.available" "SessionStart" true 2>/dev/null || true
fi
