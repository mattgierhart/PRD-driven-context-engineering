---
alwaysApply: true
---

# Session Protocols (MANDATORY)

## Start of Session

1. **Load Context**: `CLAUDE.md` → `README.md` → `PRD.md` → accepted SoT records.
2. **Read Lifecycle State**: Before v0.7, read the current PRD gate log and open questions. From
   v0.7 onward, also read the approved Active EPIC's **Session State** for "Where we left off".
3. **Check Git Status**: Confirm you are on the right branch/commit.

> **Why this order matters**: Claude Code's prompt cache works by prefix matching. Stable operating
> and product authority loads before volatile gate or EPIC state, minimizing cache invalidation.
>
> **Eviction priority** (what gets compressed first when context is full):
> 1. `temp/` scratchpad notes (ephemeral by design)
> 2. Old tool results and conversation history (auto-compacted)
> 3. Current PRD gate state, or EPIC session state from v0.7 onward (summarized, then refreshed)
> 4. SoT entries (never evicted — these are the knowledge graph)

## End of Session

1. **Update the lifecycle-appropriate state**:
   - Before v0.7: current PRD gate change log, open questions, and accepted SoT snapshot.
   - From v0.7 onward: approved EPIC **Session State** with progress, stop point, and next action.
2. **Commit**: use `session: [v0.X] summary` before v0.7, or `session: [EPIC-NN] summary` at v0.7+.
