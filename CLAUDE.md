---
title: "CLAUDE Agent Operating Guide"
updated: "2026-01-12"
authority: "PRD Led Context Engineering"
---

# CLAUDE.md — Agent Operating Guide

> **Mission**: Build software in lockstep with the PRD Version Lifecycle.
> **Authority**: Load `README.md` → `PRD.md` → `CLAUDE.md` → Active EPIC.
> **Core Rule**: If it's not in the ID Graph (SoT), it doesn't exist.

---

## 1. Session Protocols (MANDATORY)

### Start of Session

1. **Load Context**: `README.md`, `PRD.md`, and the Active EPIC.
2. **Read Session State**: Check Section 0 of the Active EPIC for "Where we left off".
3. **Check Git Status**: Confirm you are on the right branch/commit.

### End of Session

1. **Update EPIC Section 0**:
   - **Progress**: What specifically was done? (Link IDs)
   - **Stop Point**: File/Line where work ceased.
   - **Next**: Exact instructions for the next agent.
2. **Commit**: `session: [EPIC-XX] summary of work`.

---

## 2. Execution Rules

### Document Ecosystem

The methodology uses a layered document structure:

| Layer | Files | Purpose |
|-------|-------|---------|
| **Navigation** | README.md | Entry point, dashboard, current status |
| **Strategy** | PRD.md | Requirements evolving v0.1→v1.0 |
| **Execution** | epics/EPIC-XX.md | Active work, session handoffs |
| **Knowledge** | SoT/*.md | Durable specs with unique IDs |
| **Scratchpad** | temp/*.md | Ephemeral notes, harvested to SoT |

**ID Ownership**:
- SoT files own: BR, UJ, PER, SCR, API, DBT, TEST, DEP, RUN, MON, CFD, DES, TECH, ARC, INT
- PRD.md owns: FEA (v0.3), RISK (v0.5), GTM (v0.9)
- README.md owns: KPI metrics

**Cross-Reference Rule**: Every ID should link to related IDs. This creates a knowledge graph that agents can traverse.

### Documentation Discipline

- **IDs**: Reference `BR-`, `UJ-`, `API-` IDs in code comments and commits.
- **SoT Updates**: Update `SoT/` files _before_ or _during_ code changes, never "later".
- **Temp Files**: Use `temp/` for scratchpad, but harvest to SoT before closing the EPIC.

### Progressive Documentation Protocol

> **Rule**: One Document, Many Versions > Many Documents.

- **No Fragmentation**: Never create `PRD-v2.md`. Update `PRD.md` and increment the version header.
- **Change Tracking**: Use inline diffs for minor changes and append logs for major ones.
- **Handoffs**: If hitting context limits, leave a `<!-- HANDOFF -->` marker with summary of state.

### Context Efficiency

- **Batching**: Ask for comprehensive plans (Opus-style) before executing piecemeal (Sonnet-style).
- **Consolidation**: Validation and Verification steps should happen in bulk to save tokens.
- **Pruning**: if context is full, suggest a `session_handoff` where you summarize state and clear history.

### Coding Standards

#### Traceability Protocol (MANDATORY)

Every major code unit must declare which ID it implements.

```typescript
// @implements BR-101 (Free Limit)
// @see API-045
export class RateLimiter { ... }
```

- **Tests First**: Create/Update tests (`TEST-`) for every feature.
- **No Secrets**: Never commit credentials.
- **Small Commits**: Group changes by ID/Feature.

### Lifecycle Gates

- **Do Not Skip**: Verify the Gate Checklist in `PRD.md` or `README.md` (PRD Lifecycle) before advancing.
- **Blockers**: If a gate cannot be passed, update the EPIC and STOP.

---

## 3. Quick Reference

- **Lifecycle Guide**: [`README.md`](README.md)
- **ID System**: [`SoT/SoT.UNIQUE_ID_SYSTEM.md`](SoT/SoT.UNIQUE_ID_SYSTEM.md)
- **SoT Index**: [`SoT/SoT.README.md`](SoT/SoT.README.md)
- **EPIC Template**: [`epics/EPIC_TEMPLATE.md`](epics/EPIC_TEMPLATE.md)
- **Active Work**: [`epics/`](epics/)

**When in doubt, follow the Source of Truth.**
