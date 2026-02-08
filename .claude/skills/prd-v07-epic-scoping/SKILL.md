---
name: prd-v07-epic-scoping
description: Transform v0.6 specifications into context-window-sized work packages (EPICs) during PRD v0.7 Build Execution. Triggers on requests to create epics, scope work, break down implementation, or when user asks "create epics", "scope work", "break down work", "context window sizing", "what to build first?", "implementation planning", "epic breakdown". Consumes API-, DBT-, FEA-, ARC-. Outputs EPIC- entries with objectives, ID references, dependencies, and context windows. Feeds v0.7 Test Planning.
---

# Epic Scoping

Position in workflow: v0.6 Technical Specification → **v0.7 Epic Scoping** → v0.7 Test Planning

## Core Concept: Epic = Context Window

> An EPIC is not a "big user story." It is a **cognitive boundary**—a scope of work that fits in working memory (human or AI). The goal is to load exactly what's needed to complete a focused task without distraction.

**The question is not** "How long will this take?" but **"Can an agent complete this without needing more context than fits in a session?"**

## Sizing Rules

| Size | Characteristics | Action |
|------|-----------------|--------|
| **Right-sized** | 3-5 API endpoints, 2-4 DBT tables, 1-2 UJ flows | Good fit ✓ |
| **Too big** | >10 APIs, >5 tables, multiple unrelated features | Split by domain |
| **Too small** | Single endpoint, no meaningful deliverable | Merge with related |

**Rule of thumb**: If you can't describe the EPIC's goal in one sentence, it's too big.

## Scoping Process

1. **Inventory implementation items** from API-, DBT-, FEA-, ARC-
   - What must be built?

2. **Identify natural boundaries**
   - Feature clusters (features that work together)
   - Data domains (tables that belong together)
   - Architectural seams (module boundaries from ARC-)

3. **Size each potential EPIC** against context window capacity
   - Can an agent hold all relevant IDs in one session?

4. **Sequence EPICs by dependencies**
   - What must be built first?
   - What enables other EPICs?

5. **Create EPIC- entries** with full ID references

6. **Validate**: Can an agent complete this EPIC without needing more context than fits in a session?

## Sequencing Framework

| Order | Priority | Rationale | Examples |
|-------|----------|-----------|----------|
| 1 | Infrastructure EPICs | Everything depends on these | Auth, DB setup, project scaffold |
| 2 | Core data model EPICs | Foundation for features | User, Workspace, base entities |
| 3 | Critical path EPICs | Journeys that drive KPIs | UJ- that affects KPI-001 |
| 4 | Supporting feature EPICs | Secondary features | Settings, admin, nice-to-haves |

## EPIC- Output Template

```
EPIC-XXX: [Epic Name]
State: [Planned | In Progress | Testing | Complete]
Lifecycle: v0.7 Build Execution

## 0. Session State (The "Brain Dump")
- **Last Action**: [What was just completed]
- **Stopping Point**: [File/line or test failure]
- **Next Steps**: [Exact instructions for next session]
- **Context**: [Key decisions, blockers, questions]

## 1. Objective & Scope
Goal: [One sentence describing what this EPIC achieves]

Deliverables:
  - [ ] [Specific deliverable A]
  - [ ] [Specific deliverable B]
  - [ ] [Specific deliverable C]

Out of Scope: [What we are NOT doing in this EPIC]

## 2. Context & IDs
Business Rules: [BR-XXX, BR-YYY]
User Journeys: [UJ-XXX, UJ-YYY]
APIs: [API-XXX to API-ZZZ]
Data Models: [DBT-XXX, DBT-YYY]
Architecture: [ARC-XXX]
Features: [FEA-XXX, FEA-YYY]
Tests: [TEST-XXX to TEST-ZZZ] — Added during Test Planning

## 3. Dependencies
Requires: [EPIC-YYY must complete first]
Enables: [EPIC-ZZZ depends on this]
External: [Any external dependencies]

## 4. Context Windows (Build Phases)
Window 1: [Focus Area] — e.g., "Database Schema"
  - [ ] Task A
  - [ ] Task B

Window 2: [Focus Area] — e.g., "API Endpoints"
  - [ ] Task C
  - [ ] Task D

Window 3: [Focus Area] — e.g., "UI Integration"
  - [ ] Task E
  - [ ] Task F

## 5. Validation Criteria
- [ ] All TEST- entries pass
- [ ] Manual verification of UJ-
- [ ] Code has @implements tags
- [ ] SoT/ updated to match implementation
```

**Example EPIC- entry:**
```
EPIC-01: User Authentication
State: Planned
Lifecycle: v0.7 Build Execution

## 0. Session State
- **Last Action**: N/A (not started)
- **Stopping Point**: N/A
- **Next Steps**: Begin with Window 1 (Database Schema)
- **Context**: Using Supabase Auth per TECH-003

## 1. Objective & Scope
Goal: Enable users to sign up, log in, and manage their sessions.

Deliverables:
  - [ ] User registration with email/password
  - [ ] Login/logout functionality
  - [ ] Session management with refresh tokens
  - [ ] Password reset flow

Out of Scope: Social auth (EPIC-02), team invites (EPIC-05)

## 2. Context & IDs
Business Rules: BR-001 (email uniqueness), BR-002 (password requirements)
User Journeys: UJ-000 (onboarding), UJ-010 (password reset)
APIs: API-001, API-002, API-003, API-004, API-005
Data Models: DBT-010 (users), DBT-011 (sessions)
Architecture: ARC-003 (Supabase Auth)
Features: FEA-010, FEA-011
Tests: TEST-001 to TEST-015 (to be defined in Test Planning)

## 3. Dependencies
Requires: None (first EPIC)
Enables: EPIC-02, EPIC-03, EPIC-04, EPIC-05
External: Supabase project setup

## 4. Context Windows
Window 1: Database Schema
  - [ ] Create users table with RLS
  - [ ] Create sessions table
  - [ ] Set up Supabase Auth triggers

Window 2: API Endpoints
  - [ ] Implement POST /auth/signup (API-001)
  - [ ] Implement POST /auth/login (API-002)
  - [ ] Implement POST /auth/logout (API-003)
  - [ ] Implement POST /auth/refresh (API-004)
  - [ ] Implement POST /auth/reset-password (API-005)

Window 3: UI Integration
  - [ ] Build signup form (SCR-001)
  - [ ] Build login form (SCR-002)
  - [ ] Build password reset flow (SCR-003)
  - [ ] Implement auth state management

## 5. Validation Criteria
- [ ] TEST-001 to TEST-015 pass
- [ ] Can complete UJ-000 (signup → dashboard)
- [ ] Can complete UJ-010 (password reset)
- [ ] All API endpoints return correct errors
- [ ] Sessions expire correctly after timeout
```

## EPIC Phase Structure

Each EPIC follows 5 phases:

| Phase | Purpose | Activities |
|-------|---------|------------|
| **A: Plan** | Load context | Read EPIC, load referenced IDs, verify Session State |
| **B: Design** | Update SoT | Draft/refine ID entries in SoT/ before coding |
| **C: Build** | Implement | Work through Context Windows, test-first |
| **D: Validate** | Verify | Run tests, manual checks, traceability audit |
| **E: Finish** | Clean up | Update SoT, archive temp/, mark complete |

## Anti-Patterns to Avoid

| Anti-Pattern | Signal | Fix |
|--------------|--------|-----|
| **Epic explosion** | 20+ EPICs for MVP | Consolidate; most MVPs need 3-7 |
| **One mega-EPIC** | Everything in one EPIC | Split by architectural boundary |
| **No ID references** | EPIC without BR-, API-, DBT- links | Every EPIC must reference SoT/ |
| **Circular dependencies** | EPIC-01 needs EPIC-02 needs EPIC-01 | Identify shared foundation, extract to EPIC-00 |
| **Context overload** | Agent can't hold full EPIC context | Split into smaller Context Windows |
| **Missing sequencing** | No build order defined | Establish explicit dependency chain |
| **Vague objectives** | "Build the backend" | Specific, measurable: "Implement API-001–005" |

## Quality Gates

Before proceeding to Test Planning:

- [ ] All API- and DBT- entries assigned to EPICs
- [ ] No orphaned specifications (everything has an EPIC home)
- [ ] Dependencies form a DAG (no circular dependencies)
- [ ] Each EPIC has clear, measurable deliverables
- [ ] Context Windows defined for each EPIC
- [ ] Sequencing makes sense (foundations first)

## Downstream Connections

EPIC- entries feed into:

| Consumer | What It Uses | Example |
|----------|--------------|---------|
| **Test Planning** | EPIC scope defines test boundaries | TEST- entries for EPIC-01 scope |
| **Implementation Loop** | EPIC is execution unit | Work happens inside EPIC context |
| **Session Management** | Section 0 tracks progress | Resume from where we left off |
| **Progress Tracking** | EPIC state shows overall progress | 3/7 EPICs complete |

## Detailed References

- **Epic scoping examples**: See `references/examples.md`
- **EPIC- entry template**: See `assets/epic.md`
- **Dependency mapping guide**: See `references/dependency-mapping.md`
