#!/usr/bin/env bash
# pvc-je quality gate — runs on Stop. Validates SoT file integrity.
# SoT files for pvc-je: content/layoutMap.ts, lib/types.ts, docs/LAYOUTS.md
set -euo pipefail

INPUT="$(cat)"
CWD="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
WARNINGS=()

# Check that SoT files exist and are not empty
SOT_FILES=(
  "content/layoutMap.ts"
  "lib/types.ts"
  "docs/LAYOUTS.md"
)

for file in "${SOT_FILES[@]}"; do
  full_path="${CWD}/${file}"
  if [ ! -f "$full_path" ]; then
    WARNINGS+=("Missing SoT file: ${file}")
  elif [ ! -s "$full_path" ]; then
    WARNINGS+=("Empty SoT file: ${file} (may indicate accidental truncation)")
  fi
done

# Check for uncommitted changes to SoT files specifically
STAGED_SOT=$(git -C "$CWD" diff --cached --name-only -- "${SOT_FILES[@]}" 2>/dev/null || true)
if [ -n "$STAGED_SOT" ]; then
  WARNINGS+=("Staged SoT changes — confirm these are intentional: ${STAGED_SOT}")
fi

# Report warnings as system message
if [ "${#WARNINGS[@]}" -gt 0 ]; then
  WARNING_MSG=$(printf '%s\n' "${WARNINGS[@]}" | sed 's/^/  • /')
  jq -n --arg msg "pvc-je quality gate: ${#WARNINGS[@]} warning(s):\n${WARNING_MSG}" \
    '{"systemMessage": $msg}'
fi

exit 0
