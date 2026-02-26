#!/usr/bin/env bash
# scripts/generate-id-pattern.sh
# Reads id_prefixes from .claude/domain-profile.yaml and outputs a regex group.
#
# Usage:
#   bash scripts/generate-id-pattern.sh
#   # Output: (BR|UJ|PER|SCR|API|DBT|TEST|DEP|RUN|MON|CFD|DES|TECH|ARC|INT|FEA|RISK|GTM|KPI|EPIC)
#
# Hooks source this to stay in sync with domain-profile.yaml automatically.
# See: Issue #59, PR #51
#
# Dependencies: POSIX shell, grep, sed, tr (standard utilities)
set -euo pipefail

# Resolve project root (works from any subdirectory)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PROFILE="${PROJECT_ROOT}/.claude/domain-profile.yaml"

# Hardcoded fallback if domain-profile.yaml is missing or unparseable
FALLBACK="(BR|UJ|PER|SCR|API|DBT|TEST|DEP|RUN|MON|CFD|DES|TECH|ARC|INT|FEA|RISK|GTM|KPI|EPIC)"

if [ ! -f "$PROFILE" ]; then
  echo "$FALLBACK"
  exit 0
fi

# Extract prefix keys from id_prefixes section:
# - Find lines between "id_prefixes:" and the next top-level key (no indent)
# - Match lines with 2-space indent followed by uppercase key and colon
# - Extract just the key name
PREFIXES=$(sed -n '/^id_prefixes:/,/^[a-z]/p' "$PROFILE" \
  | grep -E '^  [A-Z]+:' \
  | sed 's/^ *//' \
  | sed 's/:.*//' \
  | tr '\n' '|' \
  | sed 's/|$//' || true)

if [ -z "$PREFIXES" ]; then
  echo "$FALLBACK"
  exit 0
fi

echo "(${PREFIXES})"
