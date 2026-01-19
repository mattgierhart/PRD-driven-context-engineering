# EPIC- Template

Copy this template to `epics/EPIC-{NUMBER}-{slug}.md`:

```markdown
# EPIC-{NUMBER}: {Epic Name}

> **State**: `Planned` | `In Progress` | `Testing` | `Complete`
> **Lifecycle**: v0.7 Build Execution
> **Epic Lead**: {Agent or Team Member}
> **Branch**: `epic/EPIC-{NUMBER}-{slug}`

---

## 0. Context Capsule

### Resource Envelope

| Dimension | Target | Notes |
|-----------|--------|-------|
| **Pre-load Context** | ~{N}k tokens | SoT files + EPIC + referenced code |
| **Working Room** | ~{200-N}k tokens | Space for tool outputs |
| **Session Goal** | {Checkpoint target} | What "done" looks like |

**Guideline**: If pre-load exceeds 100k tokens, split EPIC or reduce session scope.

### Dependencies

| Type | Items | Status |
|------|-------|--------|
| **Requires** | EPIC-{XX} | `Complete` / `Pending` |
| **External** | {Setup needed} | `Ready` / `Blocked` |
| **Enables** | EPIC-{YY} | Blocked until this completes |

### Pre-load Checklist

- [ ] `SoT/SoT.{X}.md` — IDs: {key IDs}
- [ ] `SoT/SoT.{Y}.md` — IDs: {key IDs}

---

## 1. Session State (The "Brain Dump")

> Update this section at the END of every session.

### Current State

- **Last Action**: {What was just completed — reference IDs}
- **Stopping Point**: {Exact file:line or test failure}
- **Next Steps**:
  1. {First action}
  2. {Second action}
  3. {Third action}
- **Blockers**: {Any blockers — or "None"}
- **Decisions Made**: {Key decisions with rationale}

### Resume Instructions

> {Exactly what the next session should do — or "N/A - EPIC Complete"}

---

## 2. Objective & Scope

**Goal**: {One sentence describing what this EPIC achieves}

### Deliverables
- [ ] {Specific deliverable A}
- [ ] {Specific deliverable B}
- [ ] {Specific deliverable C}

### Out of Scope
- {What we are explicitly NOT doing}
- {Deferred to EPIC-YYY}

---

## 3. Context & IDs

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

## 4. Execution Plan (The 5 Phases)

### Phase A: Plan
- [ ] Context loaded (PRD, SoT, README)
- [ ] Dependencies verified
- [ ] Strategy defined
- [ ] Branch created: `epic/EPIC-{NUMBER}-{slug}`

**Checkpoint A**: Planning complete, branch exists.

### Phase B: Design
- [ ] Specs updated in SoT/
- [ ] Architecture documented
- [ ] TEST- entries created

**Checkpoint B**: Specs drafted, tests defined.

### Phase C: Build (Context Windows)

**Window 1: {Focus Area}**
- [ ] Task A
- [ ] Task B
- [ ] Verification: {completion criteria}

**Checkpoint C1**: {What exists when done}

---

**Window 2: {Focus Area}**
- [ ] Task C
- [ ] Task D
- [ ] Verification: {completion criteria}

**Checkpoint C2**: {What exists when done}

---

**Window 3: {Focus Area}**
- [ ] Task E
- [ ] Task F
- [ ] Verification: {completion criteria}

**Checkpoint C3**: {What exists when done}

### Phase D: Validate
- [ ] All TEST- entries pass
- [ ] Manual verification of UJ-
- [ ] Code has `// @implements` tags
- [ ] SoT matches implementation

**Checkpoint D**: Tests green, verification complete.

### Phase E: Finish (Harvest)
- [ ] Temp files cleaned up
- [ ] SoT entries finalized
- [ ] Learning capture complete
- [ ] Resume Instructions = "N/A - EPIC Complete"
- [ ] PR ready

**Checkpoint E**: EPIC complete, PR ready.

---

## 5. Acceptance Criteria

- [ ] All deliverables marked done
- [ ] All TEST- entries pass
- [ ] Resume Instructions = "N/A - EPIC Complete"
- [ ] No orphan ID references
- [ ] Branch merged or PR approved

---

## 6. Change Log

| Date | Change | By |
|------|--------|-----|
| {Date} | Created EPIC | {Author} |
| | | |
```

## Session State Protocol

**MANDATORY**: Update Section 1 before ending ANY session.

Good example:
```
### Current State
- **Last Action**: Completed API-002 (login endpoint), tests passing
- **Stopping Point**: src/auth/login.ts:45 — need to add rate limiting
- **Next Steps**:
  1. Add rate limiter to login endpoint per BR-005
  2. Update TEST-003 to verify rate limiting
  3. Move to Window 3 (UI)
- **Blockers**: None
- **Decisions Made**: Using Supabase's built-in rate limiting rather than custom

### Resume Instructions
> Continue with rate limiting implementation. File: src/auth/login.ts:45. Reference BR-005 for limits.
```

Bad example:
```
### Current State
- **Last Action**: Working on auth
- **Stopping Point**: Somewhere in the code
- **Next Steps**: Continue
- **Blockers**: None
- **Decisions Made**: None

### Resume Instructions
> Keep working
```

## Branch Convention

**Naming**: `epic/EPIC-{NUMBER}-{slug}`

**Workflow**:
1. EPIC created → `git checkout -b epic/EPIC-{NUMBER}-{slug}`
2. Work happens → Commits reference IDs
3. Checkpoints → Commit with checkpoint state
4. EPIC complete → PR opened
5. PR merged → Branch deleted

**Force Gate**: Use `--force-gate` to bypass checks. Document reason in Change Log. Should be exceptional.
