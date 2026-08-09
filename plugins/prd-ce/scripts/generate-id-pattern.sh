#!/usr/bin/env bash
# scripts/generate-id-pattern.sh
# Reads id_prefixes from .claude/domain-profile.yaml and outputs a regex group.
#
# Usage:
#   bash scripts/generate-id-pattern.sh
#   # Output: registered base prefixes such as (BR|UJ|API|ARC|ADO|EPIC)
#
# Hooks source this to stay in sync with domain-profile.yaml automatically.
# See: Issue #59, PR #51
#
# Dependencies: Bash, grep, sed, tr (standard utilities)
set -euo pipefail

# Resolve the consumer project root. Plugin scripts live outside the consumer repository, so prefer
# explicit/runtime roots and the current Git checkout before falling back to the source layout.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PRD_CE_PROJECT_ROOT:-${CLAUDE_PROJECT_DIR:-}}"
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null || true)"
fi
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
fi
PROFILE="${PROJECT_ROOT}/.claude/domain-profile.yaml"

# The fallback is only for repositories that do not have an explicit profile. Once a profile
# exists, it is the closed registry: an empty or malformed registry must not silently broaden.
FALLBACK="(BR|UJ|PER|SCR|API|DBT|TEST|DEP|RUN|MON|SEC|CFD|DES|TECH|ARC|ENV|INT|LL|ADO|FEA|RISK|GTM|KPI|EPIC)"

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
  echo "ERROR: ${PROFILE} exists but declares no readable id_prefixes" >&2
  exit 2
fi

echo "(${PREFIXES})"
