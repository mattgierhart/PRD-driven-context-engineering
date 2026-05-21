#!/usr/bin/env bash
# Protect sensitive files from accidental edits. Exit 2 = block, 0 = allow.
set -euo pipefail

OTEL_LIB="${HOME}/.claude/hooks/otel-lib.sh"
source "$OTEL_LIB" 2>/dev/null || true

START_NS="$(now_unix_nano 2>/dev/null || echo 0)"
INPUT="$(cat)"
FILE_PATH="$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')"

PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/" "SoT/" "PRD.md" "*.pem" "*.key")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "Protected: $FILE_PATH matches pattern '$pattern'" >&2
    END_NS="$(now_unix_nano 2>/dev/null || echo 0)"
    emit_policy_block "PreToolUse" "protect-files.sh" "$pattern" "$FILE_PATH" "$INPUT" "$START_NS" "$END_NS" || true
    emit_policy_eval_duration "protect-files.sh" "$INPUT" "$START_NS" "$END_NS" || true
    exit 2
  fi
done

exit 0
