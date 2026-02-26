#!/usr/bin/env bash
# GHM SoT Update Trigger Hook (Stop)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: POSIX shell, grep, sed (standard utilities)
# No external packages required
# No local module imports
set -euo pipefail

# Implementation file patterns
IMPL_EXTENSIONS="py|ts|js|tsx|jsx|go|rs|java|rb"

# Generate ID prefix pattern from domain-profile.yaml (Issue #59)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PREFIX_GROUP="$(bash "${SCRIPT_DIR}/../../scripts/generate-id-pattern.sh" 2>/dev/null || echo '(BR|UJ|PER|SCR|API|DBT|TEST|DEP|RUN|MON|CFD|DES|TECH|ARC|INT|FEA|RISK|GTM|KPI|EPIC)')"
SOT_PATTERN="\\b${PREFIX_GROUP}-[0-9]{3}\\b"

# --- Helpers ---

json_output() {
  local context="$1"
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"systemMessage": "%s"}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin (may contain transcript info)
  local input
  input=$(cat)

  # Extract file paths from the input (Edit/Write/Create patterns)
  local modified_files
  modified_files=$(printf '%s' "$input" | grep -oE '[A-Za-z0-9_./-]+\.(py|ts|js|tsx|jsx|go|rs|java|rb|md)' | sort -u || true)

  if [ -z "$modified_files" ]; then
    exit 0
  fi

  # Check for implementation files
  local impl_files=""
  local impl_count=0
  while IFS= read -r f; do
    if echo "$f" | grep -qE "\.(${IMPL_EXTENSIONS})$"; then
      impl_files="${impl_files}${impl_files:+ }$f"
      impl_count=$((impl_count + 1))
    fi
  done <<< "$modified_files"

  # Check for SoT references in existing modified files
  local sot_refs=""
  while IFS= read -r f; do
    if [ -f "$f" ]; then
      local refs
      refs=$(grep -oE "$SOT_PATTERN" "$f" 2>/dev/null | sort -u | tr '\n' ', ' | sed 's/,$//' || true)
      if [ -n "$refs" ]; then
        sot_refs="${sot_refs}${sot_refs:+, }${refs}"
      fi
    fi
  done <<< "$modified_files"

  # Determine if reminder needed
  if [ "$impl_count" -eq 0 ] && [ -z "$sot_refs" ]; then
    exit 0
  fi

  # Build reminder
  local reminder="## SoT Update Check"

  if [ "$impl_count" -gt 0 ]; then
    reminder="${reminder}

**Implementation files modified:** ${impl_count} file(s)"
  fi

  if [ -n "$sot_refs" ]; then
    reminder="${reminder}

**SoT references found:** ${sot_refs}"
  fi

  reminder="${reminder}

**Action:** If this work affects documented specifications:
1. Check \`README.md\` -> SoT Directory for affected spec files
2. Update relevant Source of Truth files (SoT/)
3. Ensure Unique IDs remain consistent

*This is a reminder, not a blocker. Skip if changes are implementation-only.*"

  json_output "$reminder"
  exit 0
}

main
