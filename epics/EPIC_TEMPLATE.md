# EPIC-{NUMBER} {EPIC NAME}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete`
> **Lifecycle**: v0.7 Build Execution (See `README.md`)
> **Epic Lead**: {Agent or Team Member}
> **Branch**: `epic/EPIC-{NUMBER}-{slug}`

---

## 0. Context Capsule

> **Purpose**: Define the boundaries of this work unit for context management and handoffs.

### Resource Envelope

| Dimension | Target | Notes |
|-----------|--------|-------|
| **Pre-load Context** | ~{N}k tokens | SoT files + EPIC + referenced code |
| **Working Room** | ~{200-N}k tokens | Space for tool outputs and problem-solving |
| **Session Goal** | {Checkpoint target} | What "done" looks like for this session |

**Context Guideline**: If pre-loaded context exceeds 100k tokens, consider splitting the EPIC or reducing scope per session.

### Dependencies

| Type | Items | Status |
|------|-------|--------|
| **Requires** | EPIC-{XX} | `Complete` / `Pending` |
| **External** | {Setup/config needed} | `Ready` / `Blocked` |
| **Enables** | EPIC-{YY}, EPIC-{ZZ} | Blocked until this completes |

### Pre-load Checklist

Files to read at session start (agent should `@`-mention or read these):
- [ ] `SoT/SoT.{RELEVANT}.md` — IDs: {list key IDs}
- [ ] `SoT/SoT.{RELEVANT}.md` — IDs: {list key IDs}
- [ ] {Any other critical context files}

---

## 1. Session State (The "Brain Dump")

> **CRITICAL**: Update this section before ending every session. This is what enables continuity across sessions and agents.

### Current State

- **Last Action**: {What was just completed — reference IDs}
- **Stopping Point**: {Exact file:line or test failure}
- **Next Steps**:
  1. {First specific action for next session}
  2. {Second specific action}
  3. {Third specific action if needed}
- **Blockers**: {Any blockers encountered — or "None"}
- **Decisions Made**: {Key decisions this session with rationale}

### Resume Instructions

> For the next agent/session: {Exactly what to do to continue — if EPIC is complete, write "N/A - EPIC Complete"}

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

---

## 2. Objective & Scope

> **Goal**: {One sentence describing what this EPIC achieves}

### Deliverables

- [ ] {Feature A}
- [ ] {Feature B}
- [ ] {Feature C}

### Out of Scope

- {What we are NOT doing}
- {Deferred to EPIC-YYY}

---

## 3. Context & IDs

> **Rule**: List all referenced IDs from `SoT/`. Every ID used in this EPIC should be tracked here.

| Type | IDs |
| ---- | --- |
| Business Rules | BR-XXX, BR-YYY |
| User Journeys | UJ-XXX |
| APIs | API-XXX to API-ZZZ |
| Data Models | DBT-XXX |
| Tests | TEST-XXX to TEST-ZZZ |
| Screens | SCR-XXX |
| Architecture | ARC-XXX |

---

## 4. Execution Plan (The 5 Phases)

### Phase A: Plan

- [ ] **Context Loaded**: Read `PRD.md`, `SoT/`, and `README.md`
- [ ] **Dependencies Verified**: Check required EPICs are complete
- [ ] **Strategy Defined**: Document approach (e.g., "Backend first, then UI")
- [ ] **Branch Created**: `git checkout -b epic/EPIC-{NUMBER}-{slug}`

**Checkpoint A**: Planning complete, branch exists, ready to design.

### Phase B: Design

- [ ] **Specs Updated**: Create/update IDs in `SoT/` (e.g., `API-XXX` drafts)
- [ ] **Architecture Documented**: Schema changes, component structure
- [ ] **TEST- Entries Created**: Define test coverage before implementation

**Checkpoint B**: All specs drafted, tests defined, ready to build.

### Phase C: Build (Context Windows)

> **Concept**: Break work into "Context Windows" — focused work units with clear checkpoints.

**Context Window 1: {Focus Area}** (e.g., "Database Schema")

- [ ] Task A
- [ ] Task B
- [ ] Verification: {How to confirm this window is complete}

**Checkpoint C1**: {What exists when Window 1 is done — specific files, passing tests}

---

**Context Window 2: {Focus Area}** (e.g., "API Endpoints")

- [ ] Task C
- [ ] Task D
- [ ] Verification: {How to confirm this window is complete}

**Checkpoint C2**: {What exists when Window 2 is done}

---

**Context Window 3: {Focus Area}** (e.g., "UI Integration")

- [ ] Task E
- [ ] Task F
- [ ] Verification: {How to confirm this window is complete}

**Checkpoint C3**: {What exists when Window 3 is done}

> _Add Context Windows as needed. Each should be completable in a focused session._

### Phase D: Validate

- [ ] **Automated Tests**: All TEST-XXX entries pass
- [ ] **Manual Check**: Verify flows against UJ-XXX
- [ ] **Code Traceability**: Verify `// @implements ID` tags present in all major code units
- [ ] **SoT Sync**: Specs match implementation

**Checkpoint D**: All tests green, manual verification complete.

### Phase E: Finish (Harvest)

- [ ] **Temp Cleanup**: Move useful notes from `temp/` to `SoT/`, archive or delete temp files
- [ ] **Spec Finalization**: All `SoT/` entries match final implementation
- [ ] **Learning Capture**: Run agent's Learning Capture Protocol and update Project Memory
- [ ] **Pattern Harvest**: Check Harvest Queue — extract any 3+ occurrence patterns to their targets
- [ ] **Session State Clean**: Section 1 Resume Instructions = "N/A - EPIC Complete"
- [ ] **PR Ready**: All commits pushed, PR created or ready to create

**Checkpoint E**: EPIC complete, PR merged or ready for review.

---

## 5. Acceptance Criteria

> **Hook validation**: These criteria are checked before EPIC can be marked Complete.

- [ ] All deliverables (Section 2) marked done
- [ ] All TEST- entries for this EPIC pass
- [ ] Resume Instructions indicate completion ("N/A - EPIC Complete")
- [ ] No orphan ID references (all IDs exist in SoT)
- [ ] Branch merged or PR approved

---

## 6. Change Log

| Date | Author | Action |
| ---- | ------ | ------ |
| YYYY-MM-DD | {Name} | Created EPIC |
| | | |

---

## Branch Convention

**Naming**: `epic/EPIC-{NUMBER}-{slug}`

Examples:
- `epic/EPIC-01-auth-endpoints`
- `epic/EPIC-02-user-dashboard`
- `epic/EPIC-03-payment-integration`

**Workflow**:
1. EPIC created → Branch created from `main`
2. Work happens → Commits on branch (reference IDs in commit messages)
3. Checkpoints → Commits with checkpoint state
4. EPIC complete → PR opened
5. PR merged → Branch deleted, EPIC archived

**Force Gate**: If you must bypass completion criteria, use `--force-gate` flag and document the reason in the Change Log. This should be exceptional.
