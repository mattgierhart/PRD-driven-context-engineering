#!/usr/bin/env bash
# scripts/validate-ids.sh
# Validates ID integrity across all .md files in the repository.
#
# Checks:
#   1. Orphaned definitions — ID defined in a SoT file but never referenced elsewhere
#   2. Dangling references — ID referenced but never defined in any SoT file
#   3. Duplicate definitions — same ID defined in multiple SoT files
#
# Usage:
#   bash scripts/validate-ids.sh           # Run from repo root
#   bash scripts/validate-ids.sh --quiet   # Exit code only (for CI)
#
# Exit codes: 0 = clean, 1 = issues found
#
# See: Issue #58
# Dependencies: POSIX shell, grep, sed, sort, comm (standard utilities)
set -uo pipefail

# --- Configuration ---

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Source ID prefix pattern from generator (Issue #59)
PREFIX_GROUP="$(bash "${SCRIPT_DIR}/generate-id-pattern.sh" 2>/dev/null || echo '(BR|UJ|PER|SCR|API|DBT|TEST|DEP|RUN|MON|CFD|DES|TECH|ARC|INT|FEA|RISK|GTM|KPI|EPIC)')"
ID_PATTERN="${PREFIX_GROUP}-[0-9]{2,3}"

QUIET=false
if [ "${1:-}" = "--quiet" ]; then
  QUIET=true
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

# --- Temp files ---

DEFINITIONS_FILE=$(mktemp)
REFERENCES_FILE=$(mktemp)
DEFINITIONS_WITH_FILES=$(mktemp)
REFERENCES_WITH_FILES=$(mktemp)
trap 'rm -f "$DEFINITIONS_FILE" "$REFERENCES_FILE" "$DEFINITIONS_WITH_FILES" "$REFERENCES_WITH_FILES"' EXIT

# --- Collect definitions ---
# Definitions are heading lines in SoT/ files matching: ## PREFIX-NNN or ### PREFIX-NNN

log_header "Scanning for ID definitions..."

cd "$PROJECT_ROOT"

# Collect SoT files to scan
sot_files=$(find SoT/ -name '*.md' -not -name 'SoT.README.md' -not -name 'SoT.UNIQUE_ID_SYSTEM.md' 2>/dev/null | sort || true)

# Also include PRD.md and epics for FEA-, RISK-, GTM-, EPIC- definitions
extra_files=""
if [ -f PRD.md ]; then extra_files="PRD.md"; fi
for ef in epics/*.md; do
  [ -f "$ef" ] && extra_files="${extra_files} ${ef}"
done

all_def_files="${sot_files} ${extra_files}"

for sot_file in $all_def_files; do
  [ -z "$sot_file" ] && continue
  [ ! -f "$sot_file" ] && continue

  matches=$(grep -nE "^#{2,3} ${ID_PATTERN}" "$sot_file" 2>/dev/null || true)
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

# Find duplicates BEFORE deduplicating (so we can detect them)
DUPES=$(sort "$DEFINITIONS_FILE" | uniq -d 2>/dev/null || true)

# Deduplicate definitions list
sort -u "$DEFINITIONS_FILE" -o "$DEFINITIONS_FILE" 2>/dev/null || true
DEF_COUNT=$(wc -l < "$DEFINITIONS_FILE" 2>/dev/null | tr -d ' ')
log "  Found ${DEF_COUNT} ID definition(s)"

# --- Collect references ---
# References are inline mentions of IDs in any .md file

log_header "Scanning for ID references..."

# Collect all .md files (excluding system docs)
ref_files=$(find . -name '*.md' \
  -not -path './.claude/*' \
  -not -path './archive/*' \
  -not -path './node_modules/*' \
  -not -name 'SoT.UNIQUE_ID_SYSTEM.md' \
  -not -name 'HOOK_CONTRACT.md' \
  -not -name 'MIGRATION.md' \
  2>/dev/null | sort || true)

for md_file in $ref_files; do
  [ -z "$md_file" ] && continue
  [ ! -f "$md_file" ] && continue

  matches=$(grep -noE "\\b${ID_PATTERN}\\b" "$md_file" 2>/dev/null || true)
  [ -z "$matches" ] && continue

  echo "$matches" | while IFS= read -r line; do
    line_num=$(echo "$line" | cut -d: -f1)
    id=$(echo "$line" | cut -d: -f2-)
    if [ -n "$id" ]; then
      echo "${id}|${md_file}:${line_num}" >> "$REFERENCES_WITH_FILES"
      echo "$id" >> "$REFERENCES_FILE"
    fi
  done
done

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
# .claude/domain-profile.yaml. No rules declared → no-op, exit 0. python3
# absent → skipped (the POSIX-only guarantee holds for checks 1-3). Only
# `block`-severity violations (exit 1) count toward ISSUES; `warn`s are advisory.
log_header "Checking required cross-reference edges..."
if command -v python3 >/dev/null 2>&1; then
  # Plain string (not array) so empty expansion is safe under `set -u` on
  # bash 3.2 (macOS default). Single flag, no spaces — word-splitting is fine.
  edge_flag=""
  [ "$QUIET" = true ] && edge_flag="--quiet"
  if python3 "${SCRIPT_DIR}/validate-edges.py" --repo "$PROJECT_ROOT" $edge_flag; then
    : # clean, warn-only, or no rules declared
  else
    ISSUES=$((ISSUES + 1))
  fi
else
  log "  (skipped — python3 not available)"
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
