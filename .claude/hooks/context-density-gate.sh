#!/usr/bin/env bash
# GHM Context Density Gate Hook (UserPromptSubmit)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: POSIX shell, grep, wc, sed (standard utilities)
# No external packages required
# No local module imports
set -euo pipefail

# --- Thresholds ---
MIN_EPIC_TOKENS=500
MAX_EPIC_TOKENS=4000
MAX_SOT_REFERENCES=10

# --- Helpers ---

estimate_tokens() {
  local file="$1"
  local chars
  chars=$(wc -c < "$file" 2>/dev/null || echo "0")
  echo $(( chars / 4 ))
}

count_sot_references() {
  local file="$1"
  grep -oE '\b(BR|UJ|API|CFD|KPI|COMP|UI|ERR|SEC|PERF|TEST)-[0-9]{3}\b' "$file" 2>/dev/null | sort -u | wc -l | tr -d ' '
}

resolve_epic_path() {
  local epic_num="$1"
  local slug="${2:-}"

  if [ -n "$slug" ] && [ -f "epics/EPIC-${epic_num}-${slug}.md" ]; then
    echo "epics/EPIC-${epic_num}-${slug}.md"
    return
  fi

  local match
  match=$(ls epics/EPIC-"${epic_num}"-*.md 2>/dev/null | head -1)
  if [ -n "$match" ]; then
    echo "$match"
    return
  fi

  echo "epics/EPIC-${epic_num}-<slug>.md"
}

json_output() {
  local context="$1"
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "%s"}}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin JSON and extract prompt
  local input
  input=$(cat)
  local prompt
  prompt=$(printf '%s' "$input" | sed -n 's/.*"prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$prompt" ]; then
    exit 0
  fi

  # Check for epic work initiation
  local epic_num=""
  local slug=""
  epic_num=$(printf '%s' "$prompt" | grep -oiE '(start|begin|work on|continue)\s+(work\s+on\s+)?epic[- ]?([0-9]{1,2})' | grep -oE '[0-9]+' | head -1 || true)

  # Check for gate approval request
  local gate_version=""
  gate_version=$(printf '%s' "$prompt" | grep -oiE '(approve|check|assess)\s+(the\s+)?gate\s+(for\s+)?v?[0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+' | head -1 || true)

  if [ -z "$epic_num" ] && [ -z "$gate_version" ]; then
    exit 0
  fi

  if [ -n "$epic_num" ]; then
    # Pad to 2 digits
    epic_num=$(printf '%02d' "$epic_num")
    local epic_path
    epic_path=$(resolve_epic_path "$epic_num" "$slug")

    if [ ! -f "$epic_path" ]; then
      json_output "## Context Check: EPIC-${epic_num}

Epic file not found: ${epic_path}
-> Create the epic file before starting work."
      exit 0
    fi

    local tokens
    tokens=$(estimate_tokens "$epic_path")
    local sot_refs
    sot_refs=$(count_sot_references "$epic_path")

    local issues=""

    if [ "$tokens" -lt "$MIN_EPIC_TOKENS" ] && [ "$sot_refs" -eq 0 ]; then
      issues="- **SPARSE**: Epic has ~${tokens} tokens and no SoT references.
  -> Add acceptance criteria, link relevant specs (BR-, UJ-), or decompose from PRD requirements before starting."
    fi

    if [ "$tokens" -gt "$MAX_EPIC_TOKENS" ]; then
      issues="${issues}${issues:+
}- **DENSE**: Epic has ~${tokens} tokens (exceeds ${MAX_EPIC_TOKENS} threshold).
  -> Consider splitting into multiple epics. Large epics cause context drift."
    fi

    if [ "$sot_refs" -gt "$MAX_SOT_REFERENCES" ]; then
      issues="${issues}${issues:+
}- **BROAD**: Epic references ${sot_refs} SoT items.
  -> Scope may be too broad. Consider splitting by spec type or domain."
    fi

    if [ -z "$issues" ]; then
      json_output "## Context Check: EPIC-${epic_num}

Context check passed: ~${tokens} tokens, ${sot_refs} SoT references.

Proceeding with work."
    else
      json_output "## Context Check: EPIC-${epic_num}

Issues detected:
${issues}

**Recommendation:** Address these before starting to reduce drift risk."
    fi
  elif [ -n "$gate_version" ]; then
    json_output "## Context Check: Gate v${gate_version}

Gate v${gate_version} requirements — verify these items are complete in PRD.md before approving gate."
  fi

  exit 0
}

main
