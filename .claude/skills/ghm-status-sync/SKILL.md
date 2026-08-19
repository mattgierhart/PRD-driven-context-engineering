---
name: ghm-status-sync
description: >
  Synchronizes README.md Command Center with current project state.
  Triggers on gate changes, EPIC status changes, or explicit `/ghm-status-sync` invocation.
  Outputs updated README.md dashboard with current lifecycle stage, blockers, and metrics.
context: inline
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# Status Sync

Synchronize the README.md Command Center with the current project state after a gate-state change
or, from v0.7 onward, an EPIC status change.

## Workflow Overview

1. **Load Context** → Read README.md and PRD.md; at v0.7+ also read the approved active EPIC
2. **Extract State** → Pull lifecycle stage, blockers, metrics
3. **Update Dashboard** → Sync README sections with current truth

## Core Output Template

| Element | Definition | Evidence |
|---------|------------|----------|
| **Lifecycle Stage** | Current PRD version from PRD.md | `Current Lifecycle Gate: v0.X` |
| **Gate Status** | Visual progress indicators | 🟢 Complete / 🟡 In Progress / ⚪ Pending |
| **Active EPIC** | Current work from EPIC header, v0.7+ only | `EPIC-XX: Title` or none before v0.7 |
| **Blockers** | PRD gate blockers before v0.7; EPIC Session State blockers from v0.7 onward | List with severity |

## Step 1: Load Context

Read these files in order:
1. `CLAUDE.md` (operating and read-order contract)
2. `README.md` (current state)
3. `PRD.md` (metadata block for lifecycle stage)
4. At v0.7+, the approved Active EPIC Session State section (blockers, progress)

### Checklist
- [ ] README.md loaded
- [ ] PRD.md metadata extracted
- [ ] If PRD is v0.7+, Active EPIC identified and Session State section read

## Step 2: Extract Current State

Pull authoritative values:

| Field | Source |
|-------|--------|
| Lifecycle Stage | PRD.md `Current Lifecycle Gate` |
| Gate Progress | PRD.md gate table |
| Active EPIC | Approved numeric EPIC with exact `State: In Progress`, v0.7+ only |
| Blockers | PRD gate state before v0.7; EPIC Session State from v0.7 onward |
| Metrics | Accepted KPI/feedback/adoption records and their cited evidence; omit when unavailable |

## Step 3: Update README Dashboard

Apply synchronization rules:

1. **Lifecycle Stage**: Update header to match PRD.md
2. **Gate Table**:
   - 🟢 = Passed gates (all criteria met)
   - 🟡 = Current gate (in progress)
   - ⚪ = Future gates (not started)
3. **Active EPIC**: Before v0.7 show none; from v0.7 onward update metadata in Active Work
4. **Blockers**: Sync from the lifecycle-appropriate PRD gate or EPIC state
5. **Squad Status** (Section: `squad-status`, if the README has one — skip this step when the marker is absent): Update agent and EPIC tables:
   - For each agent in `.claude/agents/`: derive "Last Active" only from an explicit dated
     memory/session/change-log entry attributable to that agent; a blank starter or filesystem
     copy mtime is not activity. Use `—` when no explicit evidence exists.
   - Resolve "Current EPIC" only from an approved In Progress EPIC that names the agent.
   - For each EPIC in `epics/`: read State field, Epic Lead, and Change Log last date
   - Status values: `active` (explicit session evidence <2h old), `idle` (no recent explicit
     activity), `blocked` (explicit blocker in lifecycle-appropriate state)

## Quality Gates

### Pass Checklist
- [ ] README lifecycle stage matches PRD.md
- [ ] Gate indicators are accurate (no 🟢 on incomplete gates)
- [ ] Active EPIC is absent before v0.7 or current from v0.7 onward
- [ ] Blockers reflect actual state

### Testability Check
- [ ] Can be validated by comparing README to PRD.md
- [ ] Gate status is traceable to gate criteria

## Anti-Patterns

| Pattern | Example | Fix |
|---------|---------|-----|
| Stale gate status | 🟢 on gate with missing criteria | → Verify all criteria before marking complete |
| Missing blockers | Lifecycle record has blockers, README shows none | → Sync from the current PRD gate or approved EPIC |
| Premature EPIC reference | README points to an EPIC before v0.7 | → Show no active EPIC until the build gate is owner-approved |
| Wrong EPIC reference | README points to a closed EPIC at v0.7+ | → Check EPIC status before updating |
| Copy time treated as activity | Fresh memory seed makes every agent active | → Require an explicit dated activity record; otherwise use `—` / `idle` |

## Boundaries

**DO**:
- Status synchronization
- Link updates
- Gate progression indicators

**DON'T**:
- Content changes to descriptions
- Create new sections
- Modify PRD.md (read-only source)

## Handoff

After status sync completes:
- README.md is current and accurate
- Ready for next work session
- Gate-check skill can validate if advancing
