#!/usr/bin/env bash
# GHM Context Validation Hook (SessionStart)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Dependencies: Bash, grep, sed, awk, od (standard utilities)
# Optional: python3 for session lock timestamp math (graceful fallback if unavailable)
set -euo pipefail

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_json.sh
. "$HOOK_DIR/_json.sh"

PROJECT_ROOT="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$PROJECT_ROOT" ] || [ ! -d "$PROJECT_ROOT" ]; then
  PROJECT_ROOT="$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null || true)"
fi
[ -n "$PROJECT_ROOT" ] && [ -d "$PROJECT_ROOT" ] && cd "$PROJECT_ROOT"

# --- Helpers ---

get_prd_version() {
  local prd="PRD.md"
  if [ ! -f "$prd" ]; then
    echo ""
    return
  fi
  # Frontmatter is authoritative. Static lifecycle prose may mention v0.1 first even when the
  # current gate is later, so use only a narrowly named metadata fallback.
  local version
  version=$(head -30 "$prd" | sed -n 's/^version:[[:space:]]*//p' | head -1 \
    | tr -d "\"'" | sed 's/^v//' || true)
  if printf '%s' "$version" | grep -qE '^[0-9]+\.[0-9]+$'; then
    echo "$version"
    return
  fi
  grep -m1 -E '(Current Lifecycle Gate|Current PRD Version).*v[0-9]+\.[0-9]+' "$prd" \
    | grep -oE 'v[0-9]+\.[0-9]+' | head -1 | sed 's/^v//' || true
}

find_active_epics() {
  if [ -d "epics" ]; then
    local epic state
    for epic in \
      epics/EPIC-[0-9][0-9].md epics/EPIC-[0-9][0-9]-*.md \
      epics/EPIC-[0-9][0-9][0-9].md epics/EPIC-[0-9][0-9][0-9]-*.md; do
      [ -f "$epic" ] || continue
      state=$(sed -n 's/^>[[:space:]]*\*\*State\*\*:[[:space:]]*`\{0,1\}\([^`|]*\).*/\1/p' "$epic" \
        | head -1 | sed 's/[[:space:]]*$//' || true)
      [ "$state" = "In Progress" ] && printf '%s\n' "$epic"
    done
  fi
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
  local epics_apply=0
  if [ -n "$version" ]; then
    local major minor
    major=$(echo "$version" | cut -d. -f1)
    minor=$(echo "$version" | cut -d. -f2)
    if [ "$major" -gt 0 ] || [ "$minor" -ge 7 ]; then
      epics_apply=1
      local active_epics epic_count
      active_epics=$(find_active_epics)
      epic_count=$(printf '%s\n' "$active_epics" | grep -c . || true)
      if [ "$epic_count" -eq 1 ]; then
        epic_path="$active_epics"
      elif [ "$epic_count" -gt 1 ]; then
        warning="${warning:+${warning}
}Lifecycle v${version} has multiple EPICs marked In Progress; resolve to exactly one before implementation."
      fi
    fi
  fi

  # Build reading order
  local reading_order="1. \`CLAUDE.md\`
2. \`README.md\`
3. \`PRD.md\`
4. Accepted \`SoT/\` records referenced by \`PRD.md\`"

  local epic_line="- EPICs not yet created (pre-v0.7)"
  if [ -n "$epic_path" ]; then
    reading_order="${reading_order}
5. \`${epic_path}\`"
    epic_line="- Active work unit and acceptance criteria (${epic_path})"
  elif [ "$epics_apply" -eq 1 ]; then
    epic_line="- Missing active EPIC at lifecycle v${version}; implementation remains blocked"
    warning="${warning:+${warning}
}Lifecycle v${version} requires an approved active EPIC, but no numeric EPIC file was found."
  fi

  local directive="## Context Loading Required

Before responding to any task, read these files in order:
${reading_order}

This establishes:
- Structural rules and documentation discipline (CLAUDE.md)
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
- Accepted durable product detail (SoT records referenced by PRD.md)
${epic_line}

## Operating Discipline (PRD-CE)

- **Read order**: CLAUDE.md -> README.md -> PRD.md -> accepted SoT -> Active EPIC (v0.7+ only).
- **Truth precedence**: PRD.md -> accepted SoT -> approved EPIC; CLAUDE.md governs behavior, not product facts.
- **Core rule**: If it is not in the ID Graph (SoT specs), it does not exist. Reference BR-/UJ-/API-/FEA- IDs in code and commits.
- **SoT before code**: Update SoT/ during the change, never later. Tag major code units with @implements <ID>; untagged code is an orphan (context leak).
- **Gate before advance**: Run 'python3 "${CLAUDE_PLUGIN_ROOT:-.}/scripts/readiness.py" run --repo "$PWD"' before advancing a lifecycle stage. If score < threshold_warn, update the current PRD gate record (or the EPIC at v0.7+) and STOP.
- **Progressive docs**: One document, many versions. Never fork PRD-v2.md; increment the version header."

  # --- EPIC session lock check ---
  if [ -n "$epic_path" ] && [ -f "$epic_path" ]; then
    local active_session
    active_session=$(grep "Active Session" "$epic_path" | head -1 | sed 's/.*: //' || true)
    # Check if session is set (not "none" or empty)
    if [ -n "$active_session" ] && [ "$active_session" != "none" ]; then
      # Try to extract ISO timestamp and check staleness via Python (macOS-compatible)
      local lock_ts
      lock_ts=$(echo "$active_session" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}' || true)
      if [ -n "$lock_ts" ] && command -v python3 >/dev/null 2>&1; then
        local hours_ago
        hours_ago=$(python3 -c "
from datetime import datetime
try:
    ts = datetime.fromisoformat('${lock_ts}')
    diff = (datetime.now() - ts).total_seconds() / 3600
    print(int(diff))
except:
    print(-1)
" 2>/dev/null || echo "-1")
        if [ "$hours_ago" -ge 0 ] && [ "$hours_ago" -lt 2 ]; then
          local lock_user
          lock_user=$(echo "$active_session" | sed 's/ \/.*//')
          warning="${warning:+${warning}
}EPIC Lock: ${epic_path##*/} has an active session by ${lock_user} (${hours_ago}h ago). Coordinate before making changes."
        fi
      fi
    fi
  fi

  if [ -n "$warning" ]; then
    directive="${warning}

${directive}"
  fi

  # Output JSON with the shared Bash-only control-byte encoder.
  local json_context
  json_context=$(json_escape "$directive")
  printf '{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "%s"}}\n' "$json_context"
  exit 0
}

main
