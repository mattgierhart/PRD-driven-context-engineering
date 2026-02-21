---
template_version: "3.0.0"
---

# EPIC-{NUMBER} {EPIC NAME}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete` > **Lifecycle**: v0.7 Build Execution (See `README.md`)
> **Epic Lead**: {Agent Name}

---

<!-- SECTION: session-state -->
## Session State (The "Brain Dump")

> **Crucial**: Update this section before ending every session.

- **Last Action**: {What was just completed}
- **Stopping Point**: {Exact file/line or test failure}
- **Next Steps**: {Exact instructions for the next agent}
- **Context**: {Key decisions or blockers}
<!-- /SECTION: session-state -->

---

<!-- CUSTOMIZABLE: objective-scope -->
## Objective & Scope

> **Goal**: What specific outcome does this Epic achieve?

- **Deliverables**:
  - [ ] {Feature A}
  - [ ] {Feature B}
- **Out of Scope**: {What we are NOT doing}
<!-- /CUSTOMIZABLE: objective-scope -->

---

<!-- CUSTOMIZABLE: context-ids -->
## Context & IDs

> **Rule**: List all referenced IDs from `SoT/`.

- **Business Rules**: `BR-{XXX}`
- **User Journeys**: `UJ-{XXX}`
- **APIs**: `API-{XXX}`
<!-- /CUSTOMIZABLE: context-ids -->

---

<!-- SECTION: execution-plan -->
## Execution Plan (The 5 Phases)

### Phase A: Plan

- [ ] **Context Loaded**: Read `PRD.md`, `SoT/`, and `README.md`.
- [ ] **Strategy**: How will we approach this? (e.g., "Build Backend first, then UI").

### Phase B: Design

- [ ] **Specs Updated**: Create/Update IDs in `SoT/` (e.g., `API-XXX`) _drafts_.
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

- [ ] **Temp Cleanup**: Move any useful notes from `temp/` to `SoT/`, then remove the temp file.
- [ ] **Spec Finalization**: Ensure all specs in `SoT/` match the code.
- [ ] **Session Audit**: Ensure **Session State** section is clean.
- [ ] **Agent Observations**: Review and triage observations below.

#### Agent Observations

> Agents log proposed SoT entries, pattern discoveries, and improvement suggestions here during execution. During Phase E harvest, the EPIC lead triages each observation into: (a) create SoT entry, (b) update existing entry, or (c) discard.

| # | Observation | Proposed Action | Triage |
|---|-------------|-----------------|--------|
| 1 | {Pattern or insight discovered during execution} | {Create BR-XXX / Update API-YYY / None} | {Pending / Accepted / Discarded} |

<!-- /SECTION: execution-plan -->

---

<!-- SECTION: change-log -->
## Change Log

| Date       | Agent  | Action       |
| ---------- | ------ | ------------ |
| YYYY-MM-DD | {Name} | Created EPIC |
<!-- /SECTION: change-log -->
