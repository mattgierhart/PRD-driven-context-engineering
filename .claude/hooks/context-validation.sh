#!/usr/bin/env bash
# GHM Context Validation Hook (SessionStart)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: POSIX shell, grep, sed (standard utilities)
# No external packages required
# No local module imports
set -euo pipefail

# --- Helpers ---

get_prd_version() {
  local prd="PRD.md"
  if [ ! -f "$prd" ]; then
    echo ""
    return
  fi
  # Extract first version pattern like "v0.5" from top of file
  head -50 "$prd" | grep -oE 'v[0-9]+\.[0-9]+' | head -1 | sed 's/^v//' || true
}

find_active_epic() {
  local readme="README.md"

  # Try explicit path in README
  if [ -f "$readme" ]; then
    local epic_path
    epic_path=$(grep -oE 'epics/EPIC-[0-9]{2}(-[A-Za-z0-9-]+)?\.md' "$readme" | head -1 || true)
    if [ -n "$epic_path" ] && [ -f "$epic_path" ]; then
      echo "$epic_path"
      return
    fi
  fi

  # Fallback: highest-numbered epic file
  if [ -d "epics" ]; then
    local latest
    latest=$(ls epics/EPIC-*.md 2>/dev/null | sort -r | head -1 || true)
    if [ -n "$latest" ]; then
      echo "$latest"
      return
    fi
  fi

  echo ""
}

# --- Main ---

main() {
  local missing=""
  for f in CLAUDE.md README.md PRD.md; do
    if [ ! -f "$f" ]; then
      missing="${missing}${missing:+, }$f"
    fi
  done

  local warning=""
  if [ -n "$missing" ]; then
    warning="Missing core files: $missing"
  fi

  # Determine reading order
  local version
  version=$(get_prd_version)

  local epic_path=""
  if [ -n "$version" ]; then
    local major minor
    major=$(echo "$version" | cut -d. -f1)
    minor=$(echo "$version" | cut -d. -f2)
    if [ "$major" -gt 0 ] || [ "$minor" -ge 7 ]; then
      epic_path=$(find_active_epic)
    fi
  fi

  # Build reading order
  local reading_order="1. \`CLAUDE.md\`
2. \`README.md\`
3. \`PRD.md\`"

  local epic_line="- EPICs not yet created (pre-v0.7)"
  if [ -n "$epic_path" ]; then
    reading_order="${reading_order}
4. \`${epic_path}\`"
    epic_line="- Active work unit and acceptance criteria (${epic_path})"
  fi

  local directive="## Context Loading Required

Before responding to any task, read these files in order:
${reading_order}

This establishes:
- Structural rules and documentation discipline (CLAUDE.md)
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
${epic_line}"

  if [ -n "$warning" ]; then
    directive="${warning}

${directive}"
  fi

  # Output JSON — escape for JSON string (POSIX-portable)
  local json_context
  json_context=$(printf '%s' "$directive" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"additionalContext": "%s"}\n' "$json_context"
  exit 0
}

main
