---
title: "CLAUDE Agent Operating Guide"
updated: "2026-01-18"
authority: "PRD Led Context Engineering"
---

# CLAUDE.md — Agent Operating Guide

> **Mission**: Build software in lockstep with the PRD Version Lifecycle.
> **Authority**: Load `README.md` → `PRD.md` → `CLAUDE.md` → Active EPIC.
> **Core Rule**: If it's not in the ID Graph (Specs), it doesn't exist.

---

## 1. Session Protocols (MANDATORY)

### Start of Session

1. **Load Context**: `README.md`, `PRD.md`, and the Active EPIC.
2. **Read Session State**: Check Section 1 of the Active EPIC for Resume Instructions.
3. **Check Git Status**: Confirm you are on the right branch (`epic/EPIC-{NUMBER}-{slug}`).
4. **Verify Pre-load**: Load files listed in EPIC Section 0 (Context Capsule).

### During Session (Checkpoint Discipline)

**At every checkpoint**, before proceeding to the next phase:

1. **Update EPIC Section 1** (Session State):
   - Last Action: What was just completed (reference IDs)
   - Stopping Point: Current file/line
   - Next Steps: What comes next
   - Decisions Made: Any choices made with rationale
2. **Commit progress**: `checkpoint: [EPIC-XX] {phase} complete`
3. **Verify checkpoint criteria**: Confirm the checkpoint's "done" state is actually true

This creates natural save points. If context fills or session ends unexpectedly, work is recoverable.

### End of Session

1. **Update EPIC Section 1**:
   - **Progress**: What specifically was done? (Link IDs)
   - **Stop Point**: File/Line where work ceased.
   - **Next**: Exact instructions for the next agent.
   - **Resume Instructions**: What the next session should do first.
2. **Run Learning Capture Protocol**: Answer the agent-specific questions in `.claude/agents/{AGENT}.md` and update Project Memory.
3. **Commit**: `session: [EPIC-XX] summary of work`.

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
- **Validation Script**: Run `./scripts/check-stage-gate.sh <target_stage>` to verify gate criteria.

### Branch Convention

Each EPIC gets its own branch following this convention:

**Naming**: `epic/EPIC-{NUMBER}-{slug}`

Examples:
- `epic/EPIC-01-auth-endpoints`
- `epic/EPIC-02-user-dashboard`
- `epic/EPIC-03-payment-integration`

**Workflow**:
1. EPIC created → `git checkout -b epic/EPIC-{NUMBER}-{slug}`
2. Work happens → Commits reference IDs in messages
3. Checkpoints → Commit with state saved in EPIC Section 1
4. EPIC complete → PR opened
5. PR merged → Branch deleted, EPIC marked Complete

**One EPIC = One Branch = One PR** — This creates clear ownership and easy rollback.

### Context Management

EPICs are **context capsules** — work units sized for AI agent handoffs.

| Dimension | Target | Rationale |
|-----------|--------|-----------|
| **Pre-load context** | <100k tokens | SoT files + EPIC + code references |
| **Working room** | >100k tokens | Space for tool outputs, debugging |
| **Session goal** | 1 checkpoint | Clear "done" state per session |

**Context Monitoring**: Don't estimate upfront — monitor during work. If context exceeds 100k tokens mid-session, **pause and checkpoint immediately**:
1. Update EPIC Section 1 (Session State)
2. Commit current progress
3. Consider splitting remaining work

### Force Gate Override

In exceptional cases, you can bypass gate validation:

1. **Document the reason** in PRD.md Change Log or EPIC Change Log
2. **Use `--force-gate`** flag when relevant (mechanism varies by context)
3. **Create follow-up task** to address missing artifacts

**This should be rare.** Log format:
```
| YYYY-MM-DD | Agent | Force-gate: v0.X→v0.Y, reason: {why} | {follow-up task} |
```

If forcing gates frequently, escalate to human — the methodology may need adjustment.

---

## 3. Quick Reference

- **Lifecycle Guide**: [`README.md`](README.md)
- **ID System**: [`SoT/SoT.UNIQUE_ID_SYSTEM.md`](SoT/SoT.UNIQUE_ID_SYSTEM.md)
- **SoT Index**: [`SoT/SoT.README.md`](SoT/SoT.README.md)
- **EPIC Template**: [`epics/EPIC_TEMPLATE.md`](epics/EPIC_TEMPLATE.md)
- **Active Work**: [`epics/`](epics/)
- **Stage Gate Validation**: [`scripts/check-stage-gate.sh`](scripts/check-stage-gate.sh)
- **Hook Documentation**: [`.claude/hooks/`](.claude/hooks/)

**When in doubt, follow the Source of Truth.**
