#!/usr/bin/env bash
# scripts/validate-ids.sh
# Validates ID integrity across the canonical product-memory surfaces.
#
# Checks:
#   1. Orphaned definitions — ID defined in a SoT file but never referenced elsewhere
#   2. Dangling references — ID referenced but never defined in any SoT file
#   3. Duplicate definitions — same ID defined in multiple SoT files
#
# Usage:
#   bash scripts/validate-ids.sh           # Run from repo root
#   bash scripts/validate-ids.sh --quiet   # Exit code only (for CI)
#   bash scripts/validate-ids.sh --scope PRD.md SoT/SoT.BUSINESS_RULES.md  # closed-set validation
#
# Exit codes: 0 = clean, 1 = issues found, 2 = invalid arguments or registry configuration
#
# See: Issue #58
# Dependencies: Bash, grep, sed, sort, comm (standard utilities)
set -uo pipefail

# --- Configuration ---

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PRD_CE_PROJECT_ROOT:-${CLAUDE_PROJECT_DIR:-}}"
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null || true)"
fi
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
fi

# Source the closed ID registry from the generator (Issue #59). The generator falls back only
# when no profile exists; a present but invalid profile is a configuration error.
if ! PREFIX_GROUP="$(bash "${SCRIPT_DIR}/generate-id-pattern.sh")"; then
  echo "ERROR: unable to load registered ID prefixes" >&2
  exit 2
fi
PREFIXES="${PREFIX_GROUP#(}"
PREFIXES="${PREFIXES%)}"
NON_EPIC_PREFIXES=$(printf '%s' "$PREFIXES" \
  | sed -E 's/(^|\|)EPIC(\||$)/\1/; s/^\|//; s/\|$//')
HAS_EPIC=false
case "|${PREFIXES}|" in *'|EPIC|'*) HAS_EPIC=true ;; esac

# Build only the grammar arms explicitly registered by the consumer. EPIC keeps its historical
# two/three-digit execution-ID form, but it is not implicitly enabled in a custom closed registry.
ID_PATTERN=""
if [ -n "$NON_EPIC_PREFIXES" ]; then
  ID_PATTERN="((${NON_EPIC_PREFIXES})(-[A-Z][A-Z0-9]*)?-[0-9]{3})"
fi
if [ "$HAS_EPIC" = true ]; then
  if [ -n "$ID_PATTERN" ]; then
    ID_PATTERN="(${ID_PATTERN}|EPIC-[0-9]{2,3})"
  else
    ID_PATTERN="(EPIC-[0-9]{2,3})"
  fi
fi
if [ -z "$ID_PATTERN" ]; then
  echo "ERROR: registered ID prefix set produced no supported grammar" >&2
  exit 2
fi

QUIET=false
SCOPE_MODE=false
SCOPE_FILES=()
while [ $# -gt 0 ]; do
  case "$1" in
    --quiet) QUIET=true; shift ;;
    --scope)
      SCOPE_MODE=true; shift
      while [ $# -gt 0 ] && [ "${1#--}" = "$1" ]; do
        SCOPE_FILES+=("$1"); shift
      done
      ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done
if [ "$SCOPE_MODE" = true ] && [ "${#SCOPE_FILES[@]}" -eq 0 ]; then
  echo "--scope requires one or more repository-relative Markdown files" >&2
  exit 2
fi

validate_scope_file() {
  local relative="$1"
  case "$relative" in
    ""|/*|./*|../*|*/../*|*/..|*/./*|*/.|*//*|*.md/) return 1 ;;
    *.md) ;;
    *) return 1 ;;
  esac

  local current="$PROJECT_ROOT"
  local component
  local components=()
  IFS='/' read -r -a components <<< "$relative"
  for component in "${components[@]}"; do
    current="$current/$component"
    if [ -L "$current" ]; then
      return 1
    fi
  done
  [ -f "$PROJECT_ROOT/$relative" ]
}

if [ "$SCOPE_MODE" = true ]; then
  for scope_file in "${SCOPE_FILES[@]}"; do
    if ! validate_scope_file "$scope_file"; then
      echo "invalid --scope path (expected a normalized, repository-relative Markdown file with no symlinks): $scope_file" >&2
      exit 2
    fi
  done
fi

# --- Helpers ---

log() {
  if [ "$QUIET" = false ]; then
    echo "$@"
  fi
}

log_header() {
  if [ "$QUIET" = false ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  fi
}

is_uninitialized_template() {
  grep -qE '^template_state:[[:space:]]*uninitialized[[:space:]]*$' "$1" 2>/dev/null
}

# --- Temp files ---

DEFINITIONS_FILE=$(mktemp)
REFERENCES_FILE=$(mktemp)
DEFINITIONS_WITH_FILES=$(mktemp)
REFERENCES_WITH_FILES=$(mktemp)
trap 'rm -f "$DEFINITIONS_FILE" "$REFERENCES_FILE" "$DEFINITIONS_WITH_FILES" "$REFERENCES_WITH_FILES"' EXIT

# --- Collect definitions ---
# Definitions are H1-H3 heading lines matching PREFIX-NNN. SoT entries normally use H2/H3;
# EPIC documents use an H1 title and remain the established two-digit execution-ID exception.

log_header "Scanning for ID definitions..."

cd "$PROJECT_ROOT"

if [ "$SCOPE_MODE" = true ]; then
  graph_files=("${SCOPE_FILES[@]}")
else
  # Default validation follows product-truth precedence. Instructional docs, generic templates,
  # generated packages, and scratch trees may contain example IDs, so they are not graph inputs.
  graph_files=()
  while IFS= read -r -d '' graph_file; do
    graph_files+=("$graph_file")
  done < <(
    find SoT/ -maxdepth 1 -type f -name 'SoT.*.md' \
      -not -name 'SoT.README.md' \
      -not -name 'SoT.UNIQUE_ID_SYSTEM.md' \
      -print0 2>/dev/null
  )
  [ -f PRD.md ] && graph_files+=("PRD.md")
  # README is the registered owner for KPI definitions and is therefore a graph surface.
  [ -f README.md ] && graph_files+=("README.md")
  while IFS= read -r -d '' graph_file; do
    graph_files+=("$graph_file")
  done < <(
    find epics/ -maxdepth 1 -type f \
      \( -name 'EPIC-[0-9][0-9].md' -o -name 'EPIC-[0-9][0-9]-*.md' \
         -o -name 'EPIC-[0-9][0-9][0-9].md' -o -name 'EPIC-[0-9][0-9][0-9]-*.md' \) \
      -print0 2>/dev/null
  )
fi

if [ "${#graph_files[@]}" -gt 0 ]; then
  for sot_file in "${graph_files[@]}"; do
    [ -z "$sot_file" ] && continue
    [ ! -f "$sot_file" ] && continue
    is_uninitialized_template "$sot_file" && continue

    matches=$(grep -nE "^#{1,3} ${ID_PATTERN}([[:space:]:]|$)" "$sot_file" 2>/dev/null || true)
    [ -z "$matches" ] && continue

    echo "$matches" | while IFS= read -r line; do
      line_num=$(echo "$line" | cut -d: -f1)
      content=$(echo "$line" | cut -d: -f2-)
      id=$(echo "$content" | grep -oE "${ID_PATTERN}" | head -1 || true)
      if [ -n "$id" ]; then
        echo "${id}|${sot_file}:${line_num}" >> "$DEFINITIONS_WITH_FILES"
        echo "$id" >> "$DEFINITIONS_FILE"
      fi
    done
  done
fi

# Find duplicates BEFORE deduplicating (so we can detect them)
DUPES=$(sort "$DEFINITIONS_FILE" | uniq -d 2>/dev/null || true)

# Deduplicate definitions list
sort -u "$DEFINITIONS_FILE" -o "$DEFINITIONS_FILE" 2>/dev/null || true
DEF_COUNT=$(wc -l < "$DEFINITIONS_FILE" 2>/dev/null | tr -d ' ')
log "  Found ${DEF_COUNT} ID definition(s)"

# --- Collect references ---
# References are inline mentions of IDs in the same authoritative graph corpus. In --scope mode,
# callers must provide a closed set containing both the definitions and references under review.

log_header "Scanning for ID references..."

ref_files=()
if [ "$SCOPE_MODE" = true ] && [ "${#SCOPE_FILES[@]}" -gt 0 ]; then
  ref_files=("${SCOPE_FILES[@]}")
elif [ "$SCOPE_MODE" = false ] && [ "${#graph_files[@]}" -gt 0 ]; then
  ref_files=("${graph_files[@]}")
fi

if [ "${#ref_files[@]}" -gt 0 ]; then
  for md_file in "${ref_files[@]}"; do
    [ -z "$md_file" ] && continue
    [ ! -f "$md_file" ] && continue
    is_uninitialized_template "$md_file" && continue

    # Extract whole hyphenated tokens first, including malformed lowercase/extra segments,
    # then accept only tokens whose complete shape matches the canonical grammar. This keeps
    # `BR-001-extra` from being truncated and misread as `BR-001` while preserving multiple IDs
    # on the same line without non-portable lookbehind.
    matches=$(grep -noE '[A-Za-z][A-Za-z0-9]*(-[A-Za-z0-9]+)+' "$md_file" 2>/dev/null || true)
    [ -z "$matches" ] && continue

    echo "$matches" | while IFS= read -r line; do
      line_num=$(echo "$line" | cut -d: -f1)
      candidate=$(echo "$line" | cut -d: -f2-)
      if printf '%s\n' "$candidate" | grep -qE "^${ID_PATTERN}$"; then
        id="$candidate"
        echo "${id}|${md_file}:${line_num}" >> "$REFERENCES_WITH_FILES"
        echo "$id" >> "$REFERENCES_FILE"
      fi
    done
  done
fi

sort -u "$REFERENCES_FILE" -o "$REFERENCES_FILE" 2>/dev/null || true
REF_COUNT=$(wc -l < "$REFERENCES_FILE" 2>/dev/null | tr -d ' ')
log "  Found ${REF_COUNT} unique ID reference(s)"

# --- Analysis ---

ISSUES=0

# 1. Duplicate definitions (DUPES computed above, before deduplication)
log_header "Checking for duplicate definitions..."
if [ -n "$DUPES" ]; then
  echo "$DUPES" | while IFS= read -r dup_id; do
    [ -z "$dup_id" ] && continue
    locations=$(grep "^${dup_id}|" "$DEFINITIONS_WITH_FILES" | sed 's/^[^|]*|/  - /' || true)
    log "  DUPLICATE: ${dup_id} defined in multiple locations:"
    log "$locations"
  done
  DUP_COUNT=$(echo "$DUPES" | grep -c . || true)
  ISSUES=$((ISSUES + DUP_COUNT))
else
  log "  No duplicates found."
fi

# 2. Dangling references (referenced but never defined)
log_header "Checking for dangling references..."

DANGLING=$(comm -23 <(sort -u "$REFERENCES_FILE") <(sort -u "$DEFINITIONS_FILE") 2>/dev/null || true)
if [ -n "$DANGLING" ]; then
  echo "$DANGLING" | while IFS= read -r dang_id; do
    [ -z "$dang_id" ] && continue
    first_ref=$(grep "^${dang_id}|" "$REFERENCES_WITH_FILES" | head -1 | sed 's/^[^|]*|//' || true)
    log "  DANGLING: ${dang_id} referenced but never defined (first seen: ${first_ref})"
  done
  DANG_COUNT=$(echo "$DANGLING" | grep -c . || true)
  ISSUES=$((ISSUES + DANG_COUNT))
else
  log "  No dangling references found."
fi

# 3. Orphaned definitions (defined but never referenced outside own SoT file)
log_header "Checking for orphaned definitions..."

ORPHANED=0
if [ -s "$DEFINITIONS_FILE" ]; then
  while IFS= read -r def_id; do
    [ -z "$def_id" ] && continue

    # Get the SoT file where this ID is defined
    def_file=$(grep "^${def_id}|" "$DEFINITIONS_WITH_FILES" | head -1 | sed 's/^[^|]*|//' | sed 's/:.*//' || true)

    # Check if referenced anywhere OTHER than its own file
    ext_refs=$(grep "^${def_id}|" "$REFERENCES_WITH_FILES" 2>/dev/null | grep -v "|${def_file}:" || true)

    if [ -z "$ext_refs" ]; then
      log "  ORPHANED: ${def_id} defined in ${def_file} but never referenced elsewhere"
      ORPHANED=$((ORPHANED + 1))
    fi
  done < "$DEFINITIONS_FILE"
fi

ISSUES=$((ISSUES + ORPHANED))
if [ "$ORPHANED" -eq 0 ]; then
  log "  No orphaned definitions found."
fi

# 4. Required cross-reference edges (semantic check — needs python3)
# Delegates to validate-edges.py, which reads `required_edges` from
# .claude/domain-profile.yaml. No rules declared → no-op, exit 0. Default validation
# fails with exit 2 when python3 is unavailable rather than silently skipping a configured
# semantic contract. Only `block`-severity violations (exit 1) count toward ISSUES;
# `warn`s are advisory.
log_header "Checking required cross-reference edges..."
if [ "$SCOPE_MODE" = true ]; then
  log "  (skipped — --scope performs closed-set structural validation only)"
elif [ "${#graph_files[@]}" -eq 0 ]; then
  log "  (skipped — no canonical graph files found)"
elif command -v python3 >/dev/null 2>&1; then
  # Plain string (not array) so empty expansion is safe under `set -u` on
  # bash 3.2 (macOS default). Single flag, no spaces — word-splitting is fine.
  edge_flag=""
  [ "$QUIET" = true ] && edge_flag="--quiet"
  edge_rc=0
  python3 "${SCRIPT_DIR}/validate-edges.py" --repo "$PROJECT_ROOT" $edge_flag || edge_rc=$?
  case "$edge_rc" in
    0) : ;; # clean, warn-only, or no rules declared
    1) ISSUES=$((ISSUES + 1)) ;;
    2)
      echo "ERROR: invalid required_edges configuration" >&2
      exit 2
      ;;
    *)
      echo "ERROR: semantic edge validator failed with exit ${edge_rc}" >&2
      exit 2
      ;;
  esac
else
  echo "ERROR: python3 is required for semantic edge validation" >&2
  exit 2
fi

# --- Summary ---

log_header "Summary"
log "  Definitions: ${DEF_COUNT}"
log "  References:  ${REF_COUNT}"
log "  Issues:      ${ISSUES}"

if [ "$ISSUES" -gt 0 ]; then
  log ""
  log "  Result: ISSUES FOUND"
  exit 1
else
  log ""
  log "  Result: CLEAN"
  exit 0
fi
