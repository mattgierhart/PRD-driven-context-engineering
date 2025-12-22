# EPIC-{NUMBER} {EPIC NAME}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete` > **Lifecycle**: v0.7 Build Execution (See `README.md`)
> **Epic Lead**: {Agent Name}

---

## 0. Session State (The "Brain Dump")

> **Crucial**: Update this section before ending every session.

- **Last Action**: {What was just completed}
- **Stopping Point**: {Exact file/line or test failure}
- **Next Steps**: {Exact instructions for the next agent}
- **Context**: {Key decisions or blockers}

---

## 1. Objective & Scope

> **Goal**: What specific outcome does this Epic achieve?

- **Deliverables**:
  - [ ] {Feature A}
  - [ ] {Feature B}
- **Out of Scope**: {What we are NOT doing}

---

## 2. Context & IDs

> **Rule**: List all referenced IDs from `specs/`.

- **Business Rules**: `BR-{XXX}`
- **User Journeys**: `UJ-{XXX}`
- **APIs**: `API-{XXX}`

---

## 3. Execution Plan (The 5 Phases)

### Phase A: Plan

- [ ] **Context Loaded**: Read `PRD.md`, `specs/`, and `README.md`.
- [ ] **Strategy**: How will we approach this? (e.g., "Build Backend first, then UI").

### Phase B: Design

- [ ] **Specs Updated**: Create/Update IDs in `specs/` (e.g., `API-XXX`) _drafts_.
- [ ] **Architecture**: Document schema changes or component structure.

### Phase C: Build (The "Context Window")

> **Concept**: Break work into "Context Windows" (sprints)to maintain focus.

**Context Window 1: {Focus Area}** (e.g., "Core Logic")

- [ ] **Step 1**: {Task}
- [ ] **Step 2**: {Task}
- [ ] **Test**: {Verification Step}

**Context Window 2: {Focus Area}** (e.g., "UI Implementation")

- [ ] **Step 1**: {Task}
- [ ] **Step 2**: {Task}
- [ ] **Test**: {Verification Step}

> _Add Context Windows as needed to manage focus and epic size._

### Phase D: Validate

- [ ] **Automated Tests**: Run `npm test` or specific suites.
- [ ] **Manual Check**: Verify UI/Flows against `UJ-{XXX}`.
- [ ] **Code Traceability**: Verify `// @implements ID` tags are present.

### Phase E: Finish (Harvest)

- [ ] **Temp Cleanup**: Move any useful notes from `temp/` to `specs/` or `archive/`.
- [ ] **Spec Finalization**: Ensure all specs in `specs/` match the code.
- [ ] **Session Audit**: Ensure Section 0 is clean.

---

## 4. Change Log

| Date       | Agent  | Action       |
| ---------- | ------ | ------------ |
| YYYY-MM-DD | {Name} | Created EPIC |
