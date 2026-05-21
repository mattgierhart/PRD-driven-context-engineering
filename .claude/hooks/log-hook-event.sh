#!/usr/bin/env bash
# Log hook events to JSONL for audit trail.
set -euo pipefail

source "${HOME}/.claude/hooks/otel-lib.sh" 2>/dev/null || true

START_NS="$(now_unix_nano 2>/dev/null || echo 0)"
INPUT="$(cat)"
mkdir -p .claude/logs

echo "$INPUT" | jq -c '{
  ts: (now|todate),
  session_id,
  hook_event_name,
  tool_name,
  tool_input
}' >> .claude/logs/hook-events.jsonl

END_NS="$(now_unix_nano 2>/dev/null || echo 0)"
HOOK_EVENT="$(echo "$INPUT" | jq -r '.hook_event_name // "unknown"')"
emit_hook_execution "$HOOK_EVENT" "pass" "log-hook-event.sh" "" "$INPUT" "$START_NS" "$END_NS" || true

exit 0
