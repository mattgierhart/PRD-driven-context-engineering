#!/usr/bin/env bash
# GHM Subagent Memory Save Hook (SubagentStop)
# Shell variant — see HOOK_CONTRACT.md for interface spec.
#
# Upgraded: Uses hookSpecificOutput/additionalContext (not systemMessage)
# to inject memory extraction as an agent instruction, not a passive reminder.
#
# Dependencies: POSIX shell, grep, sed, awk (standard utilities)
# No external packages required
set -euo pipefail

# --- Helpers ---

json_output() {
  local context="$1"
  local json_context
  json_context=$(printf '%s' "$context" | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{if(NR>1) printf "\\n"; printf "%s", $0}')
  printf '{"hookSpecificOutput": {"hookEventName": "SubagentStop", "additionalContext": "%s"}}\n' "$json_context"
}

# --- Main ---

main() {
  # Read stdin JSON (contains agent_id, agent_type, agent_transcript_path, stop_hook_active)
  local input
  input=$(cat)

  # Extract agent_type from stdin JSON
  local agent_type
  agent_type=$(printf '%s' "$input" | sed -n 's/.*"agent_type"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

  if [ -z "$agent_type" ]; then
    exit 0
  fi

  local agent_dir=".claude/agents/${agent_type}"
  local memory_file="${agent_dir}/MEMORY.md"
  local hook_dir
  hook_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

  local directive=""

  # --- Memory extraction directive ---
  if [ -f "$memory_file" ]; then
    local current_memory
    current_memory=$(cat "$memory_file")

    directive="## MANDATORY: Memory Extraction Before Return

Before returning your result, you MUST review your work this session and append entries to \`${memory_file}\` for:

1. **Feedback**: Any correction you received or approach that was validated. Format: Rule. **Why:** reason. **How to apply:** when/where.
2. **Patterns**: Anything you saw 2+ times that future agents should know. Format: Pattern. **Context:** where observed. **Action:** what to do.
3. **Decisions**: Choices you made with non-obvious rationale. Format: Decision. **Why:** rationale. **Alternatives rejected:** what and why.
4. **Handoff Notes**: Anything the next agent in the lifecycle will hit. Format: From→To. **Issue:** what broke. **Fix:** what works.

Current memory (append to the appropriate section, don't overwrite):

\`\`\`
${current_memory}
\`\`\`

If nothing worth remembering happened, explicitly state 'No new memories to extract' rather than silently skipping."
  fi

  # --- Post-delegation drift check ---
  if [ -f "status/metrics.json" ] && [ -f "README.md" ]; then
    local drift_check="${hook_dir}/metrics_drift_check.py"
    if [ -f "$drift_check" ]; then
      local drift_output
      local drift_exit=0
      drift_output=$(python3 "$drift_check" 2>&1) || drift_exit=$?
      if [ "$drift_exit" -ne 0 ] && [ -n "$drift_output" ]; then
        local drift_msg="

## Post-Delegation Drift Check

${drift_output}

The subagent's work may have changed metrics without cascading.
Review and update README Truth Table before continuing."
        directive="${directive}${drift_msg}"
      fi
    fi
  fi

  # Only output if there's something to say
  if [ -n "$directive" ]; then
    json_output "$directive"
  fi

  # --- Git-based memory sync: auto-stage memory changes ---
  # Runs AFTER stdout JSON output so it doesn't contaminate the hook response.
  # Best-effort — never blocks the hook.
  # Commit convention: memory({agent_type}): {summary}
  if [ -f "$memory_file" ] && command -v git >/dev/null 2>&1; then
    if git rev-parse --git-dir >/dev/null 2>&1; then
      git add "$memory_file" 2>/dev/null || true
    fi
  fi

  exit 0
}

main
