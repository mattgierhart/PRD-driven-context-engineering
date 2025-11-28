# PRD v0.7 Build Execution Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). At v0.7, ownership shifts from AURA (Strategy) to **APOLLO (Build Lead)**. This file uses `apollo-intake.md` to reflect that transition.

## Mission Alignment
**Objective:** Transform the architecture baseline (v0.6) into an executable build plan with EPICs, issues, test strategies, and deployment playbooks—ready for implementation.
**Inputs:** PRD v0.6 (architecture decision, ARC-/API-/DBT- IDs), Gate 2 approval, risk mitigations from v0.5, and any prototype learnings.
**Deliverable:** PRD v0.7 sections (`Build Plan`, `EPIC Registry`, `Test Strategy`, `Integration Playbook`), instantiated EPIC files, and updated SoT entries for TEST-/DEP-/BR- IDs.

## ID Interlock Map
- **Inputs:**
  - Architecture IDs (`ARC-*`, `API-*`, `DBT-*`) from v0.6
  - Risk mitigations (`BR-RISK-*`, `TEST-RISK-*`) from v0.5
  - User journeys (`UJ-*`) and business rules (`BR-*`) from v0.4/v0.3
- **Processing:**
  - Decompose architecture into buildable EPICs, each referencing the IDs they implement
  - Create TEST- IDs for acceptance criteria derived from UJ- and BR- entries
  - Establish DEP- IDs for deployment dependencies and environment requirements
- **Outputs:**
  - `EPIC-###` files with Section 3A ID tracking populated
  - `TEST-*` entries in the testing playbook (unit, integration, E2E mapped to journeys)
  - `DEP-*` entries for infrastructure, secrets, and environment configuration
  - Updated BR- entries for any build-time constraints discovered

## Business Rule Criteria & Key Questions
1. **EPIC Coverage:** Does every architectural component have a corresponding EPIC or issue? Can you trace from ARC- → EPIC → TEST-?
2. **Test Strategy Completeness:** Are TEST- IDs defined for all critical paths (UJ-*), business rules (BR-*), and API contracts (API-*)?
3. **Dependency Clarity:** Are all external dependencies (services, secrets, environments) captured as DEP- IDs with owners and provisioning status?
4. **Acceptance Precision:** Are acceptance criteria specific enough for AI agents to implement without ambiguity (per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build))?
5. **Device Validation:** Does the test strategy include real-device testing for primary user devices, not just emulators?
6. **Lifecycle Continuity:** Does the build plan specify what evidence triggers Gate 3 (Buildability) and what IDs must be updated before v0.8?

## Intake Checklist
Confirm inputs include:
- [ ] PRD v0.6 with Gate 2 PASS decision
- [ ] Architecture diagrams and ARC- IDs finalized
- [ ] API contracts (API-*) and data schemas (DBT-*) documented
- [ ] Risk register with mitigation status from v0.5
- [ ] UJ- entries for critical user journeys
- [ ] Cost guardrails (BR-PRC-*) confirmed

## Processing Workflow
1. **Context Load:** Review PRD v0.6, README, active EPIC (if any), and SoT entries. Note any blockers from Gate 2 conditions.
2. **EPIC Decomposition:** Break architecture into 3-7 EPICs covering distinct build phases (foundation, core features, integrations, polish). Each EPIC references the ARC-/API-/DBT- IDs it implements.
3. **Issue Breakdown:** Within each EPIC, define issues sized for 1 context window (~2-4 hours of agent work). Include acceptance criteria tied to TEST- IDs.
4. **Test Strategy Design:** Map TEST- IDs to coverage types:
   - Unit tests for business logic (BR-*)
   - Integration tests for API contracts (API-*)
   - E2E tests for user journeys (UJ-*)
   - Performance tests for SLO targets
5. **Dependency Registration:** Create DEP- IDs for all infrastructure, secrets, and third-party services. Document provisioning steps and owners.
6. **Prompt Scaffold Creation:** For each EPIC, draft AI prompt scaffolds with explicit acceptance criteria, file paths, and test commands (per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)).
7. **Device Test Plan:** Specify which devices/browsers require manual or automated testing, prioritizing primary user devices.
8. **Gate 3 Criteria:** Define what constitutes "buildable" — typically all EPICs scoped, TEST- IDs registered, DEP- dependencies provisioned.
9. **Documentation Update:** Update PRD v0.7 sections, create EPIC files from templates, and populate SoT entries.
10. **Stakeholder Sync:** Share build plan with engineering, confirm resource availability, and align on sprint/iteration cadence.

## Output Template Snippet
```markdown
## Build Plan (v0.7)

### EPIC Registry
| EPIC ID | Name | Scope | Key IDs | Status |
|---------|------|-------|---------|--------|
| EPIC-01 | Foundation & Auth | Core infra, auth flow | ARC-001, API-AUTH-001 | Planned |
| EPIC-02 | Core Features | Primary user journeys | UJ-001, UJ-002, BR-101 | Planned |
| ... | ... | ... | ... | ... |

### Test Strategy
| Coverage Type | TEST- IDs | Automation | Target |
|--------------|-----------|------------|--------|
| Unit | TEST-UNIT-001..010 | Jest/Vitest | 80% branch coverage |
| Integration | TEST-INT-001..005 | Playwright | All API-* contracts |
| E2E | TEST-E2E-001..003 | Cypress | Critical UJ-* paths |
| Performance | TEST-PERF-001 | k6/Lighthouse | SLO targets |

### Dependency Registry
| DEP ID | Type | Service/Resource | Owner | Status |
|--------|------|------------------|-------|--------|
| DEP-001 | Infrastructure | Supabase project | @backend | Provisioned |
| DEP-002 | Secret | Stripe API keys | @payments | Pending |
| ... | ... | ... | ... | ... |

### Gate 3 Criteria
- [ ] All EPICs defined with acceptance criteria
- [ ] TEST- IDs registered for critical paths
- [ ] DEP- dependencies provisioned or scheduled
- [ ] AI prompt scaffolds drafted for EPIC-01
- [ ] Device test plan confirmed
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **EPIC Traceability** | Every EPIC references the ARC-/API-/DBT- IDs it implements |
| **Test Coverage Plan** | TEST- IDs exist for all UJ-* critical paths and BR-* constraints |
| **Dependency Visibility** | All external dependencies have DEP- IDs with owners |
| **Acceptance Precision** | Criteria are specific enough for implementation without clarification |
| **Device Coverage** | Test plan includes real devices for primary user personas |
| **Gate 3 Readiness** | Criteria defined and achievable within planned timeline |

## Collaboration & Handoff
- Store EPIC files in `epics/EPIC-##-[name].md` using the EPIC template with Section 0 (Session State) and Section 3A (ID Tracking).
- Update `source-of-truth/testing-playbook.md` with new TEST- IDs.
- Create `source-of-truth/deployment-playbook.md` entries for DEP- IDs.
- Coordinate with JANUS (Ops Lead) on infrastructure provisioning timeline.
- Notify AURA if build discoveries require strategy loopback (e.g., journey infeasibility).

## Reporting Checklist
- [ ] PRD v0.7 Build Plan section completed
- [ ] EPIC files created with ID tracking populated
- [ ] Test strategy documented with TEST- IDs
- [ ] Dependency registry with DEP- IDs and owners
- [ ] AI prompt scaffolds drafted for first EPIC
- [ ] Gate 3 criteria defined and communicated
- [ ] Stakeholder sync completed

---

## Ready-to-Use Agent Prompt

> **Copy the block below into your AI assistant to execute v0.7 Build Execution intake.**

```
You are APOLLO, the Build Lead for Gear Heart Methodology (GHM).

## Your Mission
Transform the v0.6 architecture decision into an executable build plan with EPICs, test strategies, and deployment dependencies.

## Context to Load
Before responding, ensure you have access to:
1. PRD.md (especially v0.6 Architecture sections)
2. README.md (current status and blockers)
3. source-of-truth/ files for: ARC-*, API-*, DBT-*, UJ-*, BR-* IDs
4. templates/epics/EPIC-template.md

## Your Deliverables
Produce the following artifacts:

### 1. EPIC Registry (3-7 EPICs)
For each EPIC:
- EPIC ID and descriptive name
- Scope summary (1-2 sentences)
- IDs implemented (ARC-*, API-*, UJ-*, BR-*)
- Estimated complexity (S/M/L)
- Dependencies on other EPICs

### 2. Test Strategy
Map TEST- IDs to:
- Unit tests → BR-* business rules
- Integration tests → API-* contracts
- E2E tests → UJ-* user journeys
- Performance tests → SLO targets

### 3. Dependency Registry
For each external dependency, create DEP- ID with:
- Type (infrastructure, secret, service, data)
- Resource name and provider
- Owner (role or team)
- Provisioning status and timeline

### 4. First EPIC Detail
For EPIC-01 (Foundation), provide:
- Full issue breakdown (sized for 1 context window each)
- Acceptance criteria tied to TEST- IDs
- AI prompt scaffold for implementation
- File paths and test commands

## Output Format
Structure your response as:
1. Executive Summary (5 bullets max)
2. EPIC Registry Table
3. Test Strategy Table
4. Dependency Registry Table
5. EPIC-01 Detailed Breakdown
6. Gate 3 Criteria Checklist
7. Risks and Blockers (if any)

## Constraints
- Every EPIC must trace to at least one ARC-/API-/UJ- ID
- Acceptance criteria must be specific enough to implement without clarification
- Include real-device testing in the test strategy (not just emulators)
- Flag any architecture gaps that block EPIC definition
- Reference CFD-401 for prompt precision guidance

## Gate 3 Success Criteria
Your output should enable a PASS on Gate 3 (Buildability) when:
- All EPICs are defined with clear scope and ID references
- TEST- IDs are registered for critical paths
- DEP- dependencies are identified with owners
- First EPIC has implementation-ready prompt scaffolds
```
