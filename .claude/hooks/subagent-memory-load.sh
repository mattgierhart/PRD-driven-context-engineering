#!/bin/bash
# Hook: SubagentStart - Load agent memory if it exists
# Prints memory content to STDOUT for injection into subagent context

AGENT_NAME="$1"
AGENT_DIR=".claude/agents/${AGENT_NAME}"
MEMORY_FILE="${AGENT_DIR}/MEMORY.md"

# Check if this agent has a memory file
if [ -f "$MEMORY_FILE" ]; then
    echo "--- LOADING PROJECT MEMORY ---"
    cat "$MEMORY_FILE"
    echo "--- END PROJECT MEMORY ---"
    echo ""
    echo "Remember: Update this memory before returning results."
else
    # No memory file - agent operates without memory (this is fine)
    echo "Note: No memory file for ${AGENT_NAME}. Proceeding without project memory."
fi
