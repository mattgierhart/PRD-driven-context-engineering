# EPIC-{NUMBER} {EPIC NAME}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete`
> **Lifecycle**: v0.7 Build Execution (See `README.md`)
> **Epic Lead**: {Agent or Team Member}

---

## 0. Session State (The "Brain Dump")

> **CRITICAL**: Update this section before ending every session. This is what enables continuity across sessions and agents.

### Current State

- **Last Action**: {What was just completed — reference IDs}
- **Stopping Point**: {Exact file:line or test failure}
- **Next Steps**:
  1. {First specific action for next session}
  2. {Second specific action}
  3. {Third specific action if needed}
- **Context**: {Key decisions made, blockers hit, questions open}

### Session State Guidelines

**Last Action** — Be specific, reference IDs:
- Good: "Completed API-002 (login endpoint), all tests passing"
- Bad: "Working on auth"

**Stopping Point** — Provide enough detail to resume immediately:
- Good: "src/api/auth/login.ts:47 — need to add rate limiting per BR-005"
- Bad: "Somewhere in the code"

**Next Steps** — Numbered, actionable. Another agent should be able to resume:
- Good: "1. Add rate limiter middleware per BR-005 / 2. Update TEST-008 / 3. Move to API-003"
- Bad: "Continue working"

**Context** — Capture decisions, blockers, and open questions:
- Include: Architecture decisions, blockers encountered, deviations from spec
- Exclude: Obvious facts, routine steps, already-resolved issues

---

## 1. Objective & Scope

> **Goal**: What specific outcome does this EPIC achieve?

### Deliverables

- [ ] {Feature A}
- [ ] {Feature B}
- [ ] {Feature C}

### Out of Scope

- {What we are NOT doing}
- {Deferred to EPIC-YYY}

---

## 2. Context & IDs

> **Rule**: List all referenced IDs from `SoT/`. Every ID used in this EPIC should be tracked here.

| Type | IDs |
| ---- | --- |
| Business Rules | BR-XXX, BR-YYY |
| User Journeys | UJ-XXX |
| APIs | API-XXX to API-ZZZ |
| Data Models | DBT-XXX |
| Tests | TEST-XXX to TEST-ZZZ |
| Screens | SCR-XXX |

---

## 3. Execution Plan (The 5 Phases)

### Phase A: Plan

- [ ] **Context Loaded**: Read `PRD.md`, `SoT/`, and `README.md`
- [ ] **Dependencies Verified**: Check required EPICs are complete
- [ ] **Strategy Defined**: Document approach (e.g., "Backend first, then UI")

### Phase B: Design

- [ ] **Specs Updated**: Create/update IDs in `SoT/` (e.g., `API-XXX` drafts)
- [ ] **Architecture Documented**: Schema changes, component structure
- [ ] **TEST- Entries Created**: Define test coverage before implementation

### Phase C: Build (Context Windows)

> **Concept**: Break work into "Context Windows" to maintain focus and enable clean handoffs.

**Context Window 1: {Focus Area}** (e.g., "Database Schema")

- [ ] Task A
- [ ] Task B
- [ ] Verification: {How to confirm this window is complete}

**Context Window 2: {Focus Area}** (e.g., "API Endpoints")

- [ ] Task C
- [ ] Task D
- [ ] Verification: {How to confirm this window is complete}

**Context Window 3: {Focus Area}** (e.g., "UI Integration")

- [ ] Task E
- [ ] Task F
- [ ] Verification: {How to confirm this window is complete}

> _Add Context Windows as needed. Each should be completable in a focused session._

### Phase D: Validate

- [ ] **Automated Tests**: All TEST-XXX entries pass
- [ ] **Manual Check**: Verify flows against UJ-XXX
- [ ] **Code Traceability**: Verify `// @implements ID` tags present in all major code units
- [ ] **SoT Sync**: Specs match implementation

### Phase E: Finish (Harvest)

- [ ] **Temp Cleanup**: Move useful notes from `temp/` to `SoT/`, archive or delete temp files
- [ ] **Spec Finalization**: All `SoT/` entries match final implementation
- [ ] **Session State Clean**: Section 0 has no open next steps
- [ ] **Change Log Updated**: Document completion in Section 4

---

## 4. Change Log

| Date | Author | Action |
| ---- | ------ | ------ |
| YYYY-MM-DD | {Name} | Created EPIC |
| | | |
