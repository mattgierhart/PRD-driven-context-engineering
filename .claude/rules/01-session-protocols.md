---
alwaysApply: true
---

# Session Protocols (MANDATORY)

## Start of Session

1. **Load Context**: `README.md`, `PRD.md`, and the Active EPIC.
2. **Read Session State**: Check the **Session State** section of the Active EPIC for "Where we left off".
3. **Check Git Status**: Confirm you are on the right branch/commit.

> **Why this order matters**: Claude Code's prompt cache works by prefix matching. Content that changes rarely (README, PRD) loads first to maximize cache hits. The EPIC session state changes every session and loads last to minimize cache invalidation. This is the same stable→volatile pattern Anthropic uses in Claude Code's system prompt assembly.
>
> **Eviction priority** (what gets compressed first when context is full):
> 1. `temp/` scratchpad notes (ephemeral by design)
> 2. Old tool results and conversation history (auto-compacted)
> 3. EPIC session state (summarized, then refreshed)
> 4. SoT entries (never evicted — these are the knowledge graph)

## End of Session

1. **Update the EPIC Session State section**:
   - **Progress**: What specifically was done? (Link IDs)
   - **Stop Point**: File/Line where work ceased.
   - **Next**: Exact instructions for the next agent.
2. **Commit**: `session: [EPIC-XX] summary of work`.
