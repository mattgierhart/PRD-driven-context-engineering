---
template_version: "3.2.0"
---

# EPIC-{NUMBER} {EPIC NAME}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete` > **Lifecycle**: v0.7 Build Execution (See `README.md`)
> **Epic Lead**: {Agent Name}
> **Agents**: {Primary: devlab | Supporting: studio, horizon}
> **Coordination Mode**: `single` | `multi-agent`

---

<!-- SECTION: session-state -->
## Session State (The "Brain Dump")

> **Crucial**: Update this section before ending every session.

- **Active Session**: none
- **Last Action**: {What was just completed}
- **Stopping Point**: {Exact file/line or test failure}
- **Next Steps**: {Exact instructions for the next agent}
- **Context**: {Key decisions or blockers}

### Assumptions & Ambiguities Log

> Track assumptions made and ambiguities encountered during execution. **Type**: `ASSUMPTION` = agent chose an interpretation; `AMBIGUITY` = agent cannot proceed without clarification. Review this table at session start to catch incorrect assumptions early.

| # | Related ID | Type | Description | Evidence / Reasoning | Resolution |
|---|-----------|------|-------------|---------------------|------------|
| — | — | — | _(none yet)_ | — | — |
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
- [ ] **Agent Assignment** _(multi-agent only)_: Map agents to phases/windows below.

#### Agent Routing (multi-agent only)

> Skip this table for single-agent EPICs.

| Phase/Window | Agent | Mode | Context Required |
|---|---|---|---|
| {Phase or Window} | {agent} | {research / implement / verify} | {IDs to preload} |

### Synthesis Checkpoint (before implementation)

> **Rule**: The coordinator must synthesize findings before directing implementation. Good spec: specific file paths, line numbers, exact changes. Bad spec: "based on your findings, fix it."

After research/design phases complete, the coordinator MUST produce:

- [ ] **Implementation Spec**: Specific files to create/modify, with line-level guidance
- [ ] **ID Traceability Map**: Every change traced to BR-/UJ-/API- IDs
- [ ] **Agent Prompts** _(multi-agent only)_: Self-contained prompts for each implementation worker (worker cannot see conversation history or this EPIC)
- [ ] **Merge Strategy** _(multi-agent only)_: How worker branches/worktrees merge back

### Phase B: Design

- [ ] **Specs Updated**: Create/Update IDs in `SoT/` (e.g., `API-XXX`) _drafts_.
- [ ] **Architecture**: Document schema changes or component structure.

### Phase C: Build (The "Context Window")

> **Concept**: Break work into "Context Windows" (sprints) to maintain focus.
> **Multi-agent**: Each window can be assigned to a different worker agent.

**Context Window 1: {Focus Area}** (e.g., "Core Logic")
- **Agent**: {devlab} _(multi-agent only)_

- [ ] **Step 1**: {Task}
- [ ] **Step 2**: {Task}
- [ ] **Test**: {Verification Step}

**Context Window 2: {Focus Area}** (e.g., "UI Implementation")
- **Agent**: {devlab} _(multi-agent only)_

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
- [ ] **Memory Harvest**: For each participating agent:
  1. Read `.claude/agents/{agent}/MEMORY.md`
  2. Promote entries with 3+ occurrences or cross-EPIC relevance → `SoT/SoT.LESSONS_LEARNED.md` as LL-XXX
  3. Archive promoted entries → agent's `MEMORY_ARCHIVE.md` (preserve provenance)
  4. Update `Verified` dates on SoT entries this EPIC touched
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
