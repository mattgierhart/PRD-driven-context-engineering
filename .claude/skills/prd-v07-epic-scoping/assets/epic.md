# EPIC- Template

Copy this template to `epics/EPIC-XXX.md`:

```markdown
# EPIC-XXX: [Epic Name]

State: [Planned | In Progress | Testing | Complete]
Lifecycle: v0.7 Build Execution
Created: [Date]
Updated: [Date]

---

## 0. Session State (The "Brain Dump")

> Update this section at the END of every session.

- **Last Action**: [What was just completed]
- **Stopping Point**: [Exact file:line or test failure]
- **Next Steps**: [Exact instructions for next session]
- **Context**: [Key decisions made, blockers hit, questions open]

---

## 1. Objective & Scope

**Goal**: [One sentence describing what this EPIC achieves]

### Deliverables
- [ ] [Specific deliverable A]
- [ ] [Specific deliverable B]
- [ ] [Specific deliverable C]

### Out of Scope
- [What we are explicitly NOT doing]
- [Deferred to EPIC-YYY]

---

## 2. Context & IDs

| Type | IDs |
|------|-----|
| Business Rules | BR-XXX, BR-YYY |
| User Journeys | UJ-XXX |
| APIs | API-XXX to API-ZZZ |
| Data Models | DBT-XXX, DBT-YYY |
| Architecture | ARC-XXX |
| Features | FEA-XXX, FEA-YYY |
| Tests | TEST-XXX to TEST-ZZZ |
| Screens | SCR-XXX, SCR-YYY |

---

## 3. Dependencies

### Requires (must complete before this)
- [ ] EPIC-YYY: [Reason]
- [ ] External: [Setup/config needed]

### Enables (blocked until this completes)
- EPIC-ZZZ: [What they need from us]

---

## 4. Context Windows (Build Phases)

### Window 1: [Focus Area, e.g., "Database Schema"]
- [ ] Task A
- [ ] Task B
- [ ] Task C

### Window 2: [Focus Area, e.g., "API Endpoints"]
- [ ] Task D
- [ ] Task E
- [ ] Task F

### Window 3: [Focus Area, e.g., "UI Integration"]
- [ ] Task G
- [ ] Task H

---

## 5. Validation Criteria

- [ ] All TEST- entries for this EPIC pass
- [ ] Manual verification of UJ- journeys
- [ ] Code has `// @implements` tags for all IDs
- [ ] specs/ files updated to match implementation
- [ ] No orphaned code (everything traces to an ID)

---

## 6. Change Log

| Date | Change | By |
|------|--------|-----|
| [Date] | Created EPIC | [Author] |
| | | |

```

## Session State Protocol

**MANDATORY**: Update the Session State section before ending ANY session.

This is the "brain dump" that allows the next session (human or AI) to resume exactly where you left off.

Good example:
```
- **Last Action**: Completed API-002 (login endpoint), tests passing
- **Stopping Point**: src/auth/login.ts:45 — need to add rate limiting
- **Next Steps**:
  1. Add rate limiter to login endpoint per BR-005
  2. Update TEST-003 to verify rate limiting
  3. Move to Window 3 (UI)
- **Context**: Decided to use Supabase's built-in rate limiting rather than custom
```

Bad example:
```
- **Last Action**: Working on auth
- **Stopping Point**: Somewhere in the code
- **Next Steps**: Continue
- **Context**: N/A
```
