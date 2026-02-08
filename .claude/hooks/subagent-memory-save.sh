#!/bin/bash
# Hook: SubagentStop - Prompt for memory update + post-delegation drift check
# This hook reminds the orchestrator to capture memory updates and validates
# that the subagent's work didn't introduce metrics drift.

AGENT_NAME="$1"
AGENT_DIR=".claude/agents/${AGENT_NAME}"
MEMORY_FILE="${AGENT_DIR}/MEMORY.md"
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Memory checkpoint (existing behavior) ---
if [ -f "$MEMORY_FILE" ]; then
    echo ""
    echo "--- MEMORY UPDATE CHECKPOINT ---"
    echo "Agent: ${AGENT_NAME}"
    echo "Memory file: ${MEMORY_FILE}"
    echo ""
    echo "Before concluding, ensure the following were captured:"
    echo "  - New patterns discovered -> Patterns Learned table"
    echo "  - Decisions made -> Key Decisions table"
    echo "  - Collaboration friction -> Relevant section"
    echo "  - Open questions -> Open Questions list"
    echo "--- END CHECKPOINT ---"
fi

# --- Post-delegation drift check ---
# After subagent completes, check if metrics.json and README.md still agree.
# This catches the "subagent handoff gap" where a subagent changes values
# (e.g., removes tests) without cascading to README.
if [ -f "status/metrics.json" ] && [ -f "README.md" ]; then
    DRIFT_CHECK="${HOOK_DIR}/metrics_drift_check.py"
    if [ -f "$DRIFT_CHECK" ]; then
        DRIFT_OUTPUT=$(python3 "$DRIFT_CHECK" 2>&1)
        DRIFT_EXIT=$?
        if [ $DRIFT_EXIT -ne 0 ] && [ -n "$DRIFT_OUTPUT" ]; then
            echo ""
            echo "--- POST-DELEGATION DRIFT CHECK ---"
            echo "$DRIFT_OUTPUT"
            echo ""
            echo "The subagent's work may have changed metrics without cascading."
            echo "Review and update README Truth Table before continuing."
            echo "--- END DRIFT CHECK ---"
        fi
    fi
fi

# Exit cleanly regardless - don't block agents
exit 0
