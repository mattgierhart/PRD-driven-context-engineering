#!/bin/bash
# Hook: SubagentStop - Prompt for memory update
# This hook reminds the orchestrator to capture memory updates

AGENT_NAME="$1"
AGENT_DIR=".claude/agents/${AGENT_NAME}"
MEMORY_FILE="${AGENT_DIR}/MEMORY.md"

# Only prompt if this agent has a memory file
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

# Exit cleanly regardless - don't block agents without memory
exit 0
