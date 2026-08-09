---
alwaysApply: true
---

# Documentation Discipline

- **IDs**: Reference `BR-`, `UJ-`, `API-` IDs in code comments and commits.
- **SoT Updates**: Update `SoT/` files _before_ or _during_ code changes, never "later".
- **Temp Files**: Use `temp/` for scratchpad, but harvest to SoT before closing the EPIC.

## Progressive Documentation Protocol

> **Rule**: One Document, Many Versions > Many Documents.

- **No Fragmentation**: Never create `PRD-v2.md`. Update `PRD.md` and increment the version header.
- **Change Tracking**: Use inline diffs for minor changes and append logs for major ones.
- **Handoffs**: If hitting context limits, leave a `<!-- HANDOFF -->` marker with summary of state.

## Context Efficiency

- **Batching**: Ask for comprehensive plans (Opus-style) before executing piecemeal (Sonnet-style).
- **Consolidation**: Validation and Verification steps should happen in bulk to save tokens.
- **Pruning**: If context is full, suggest a `session_handoff` where you summarize state and clear history.
