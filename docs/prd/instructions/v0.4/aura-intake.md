# PRD v0.4 AURA Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Convert validated personas + journeys into the PRD v0.4 User Journeys section, ensuring SoT references (`UJ-`, `CFD-`, `BR-`, `API-`) are registered and dependencies are ready for Red Team review.
**Inputs:** Journey Cards and Persona Sheets produced via the [PRD v0.4 Research Agent Instructions](./research-agents.md), including candidate UJ- IDs and evidence artifacts.
**Deliverable:** Updated PRD sections (`Personas`, `User Journeys`, `Pain & Value Mapping`, `Dependency Summary`) plus SoT ledger updates.

## ID Interlock Map
- **Inputs:** Journey Cards with `UJ-*` placeholders, supporting `CFD-*` artifacts, and dependency notes pointing to `BR-`, `API-`, `DBT-`, or `TEST-` IDs.
- **Processing:** Confirm whether existing IDs (e.g., `CFD-PRC-*`, `BR-PRC-*`) remain valid once user evidence is mapped. If contradictions emerge, document required loopbacks.
- **Outputs:**
  - Registered `UJ-*` entries with lineage to specific `CFD-*` artifacts and monetization IDs.
  - Dependency ledger enumerating new `BR-`/`API-`/`DBT-`/`TEST-` IDs plus owners and due dates.
  - Lifecycle memo for v0.5 summarizing which journeys or personas pose the biggest risk to Gate 1.

## Business Rule Criteria & Key Questions
1. **Persona Traceability:** Can reviewers follow each persona from PRD summary → Journey narrative → SoT ID without ambiguity?
2. **Pain ↔ Value Mapping:** Does every major pain tie to a monetization/value promise and specify which ID enforces or measures it?
3. **Dependency Readiness:** Are all integrations/compliance steps captured as actionable IDs with owners, ensuring architecture/risk teams have zero blind spots?
4. **Evidence Integrity:** Are quotes/statistics properly cited with `CFD-*` IDs, and do they resolve the open questions from v0.3?
5. **Real-User Activation:** Have you confirmed live user reviewers, device coverage, and a feedback cadence so the build team doesn’t defer validation (see [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build))?
6. **Lifecycle Continuity:** Have you flagged for the Red Team which personas/journeys still contain unproven assumptions or require mitigation experiments?

## Intake Checklist
Verify the bundle contains:
- Coverage Matrix summarizing journeys vs. personas
- 3–7 Journey Cards with artifacts + candidate UJ- IDs
- Persona sheets with KPIs, workflows, tooling
- Dependency notes (BR-/API-/DBT-/TEST- suggestions)
- Lifecycle notes targeting v0.5 Red Team focus areas

## Processing Workflow
1. **Context Refresh:** Re-read PRD v0.3 to ensure personas align with target segments. Note any monetization assumptions that need validation.
2. **Journey Selection:** Choose the most critical 3–5 journeys for the core PRD narrative; place others in Appendix/Backlog.
3. **Persona Section:** Write persona summaries (role, KPIs, constraints). Reference CFD- and UJ- IDs to prove evidence lineage.
4. **Journey Narrative:** For each selected journey, craft a paragraph describing trigger → steps → pain → desired value. Include inline citations referencing Journey Card artifacts.
5. **Pain & Value Mapping:** Build a table linking pains to value propositions and monetization hooks from v0.3. Highlight where future build/tests focus.
6. **Real-User Loop Plan:** Document who will review prototypes (names/roles/device) and establish a feedback cadence (e.g., weekly check-in) to avoid late usability surprises per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build).
7. **Dependency Register:** Translate research dependency notes into tangible ID hooks: new BR- policies, API-/DBT- contracts, TEST- validations. Document owners and next actions.
8. **Evidence Index:** Summarize which CFD- IDs back each persona/journey so reviewers can trace interviews quickly.
9. **Lifecycle Hook:** Outline what the Red Team (v0.5) should challenge (biggest risks, assumptions). Note open interviews if coverage gaps exist.

## Output Template Snippet
```
## Personas
### [Persona Name]
- KPI / definition of success
- Tooling today (Artifact CFD-UJ-###)
- Pains tied to monetization assumptions

## Core Journeys
1. **Journey ID – Trigger**
   - Summary
   - Evidence refs: `CFD-UJ-###`, `Artifact` files

## Pain ↔ Value Table
| Pain | Evidence | Value Promise | ID Hooks |

## Dependencies & Next IDs
- `UJ-###`: Journey summary + owner for SoT entry
- `BR-OPS-###`: Policy requirement
- `API-LAB-001`: Data contract placeholder

## Lifecycle Notes
What the Red Team must pressure-test.
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Persona Integrity** | Data matches research; any gaps flagged. |
| **Journey Clarity** | Steps paraphrased accurately with citations. |
| **ID Registration** | Every UJ-/CFD-/BR-/API- hook logged in SoT tracker. |
| **Dependency Visibility** | Downstream requirements summarized with owners. |
| **Lifecycle Prep** | Risks + assumptions articulated for v0.5 review. |
| **Feedback Loop Ready** | Named users + device coverage logged with cadence per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build). |

## Collaboration & Packaging
- Draft updates as `[journey-bundle]__prd-v0.4.md` before editing the canonical PRD.
- Notify stakeholders in README/EPIC about newly added UJ- IDs and dependencies needing technical review.
- Provide SoT update diff or checklist showing which IDs were created vs. extended.

## Reporting Checklist
- [ ] Persona + Journey sections updated with citations
- [ ] Pain ↔ Value ↔ Monetization table inserted
- [ ] Dependencies + ID hooks documented and logged
- [ ] Evidence index referencing CFD- IDs complete
- [ ] Real-user feedback roster + cadence published
- [ ] Lifecycle memo for v0.5 shared with product + risk leads

---

## Ready-to-Use Agent Prompt

> **Copy the block below into your AI assistant to execute v0.4 User Journeys intake as AURA.**

```
You are AURA, the Market & Product Strategy Lead for Gear Heart Methodology (GHM).

## Your Mission
Convert validated personas + journeys into PRD v0.4 User Journeys section with SoT-registered UJ- IDs and dependency hooks.

## Context Required
1. PRD v0.3 (Commercial Model, pricing, monetization assumptions)
2. Journey Cards and Persona Sheets from v0.4 Research Agents
3. CFD-PRC-*, BR-PRC-* IDs from v0.3

## Intake Checklist (Verify First)
- [ ] Coverage Matrix (journeys vs. personas)
- [ ] 3-7 Journey Cards with artifacts + candidate UJ- IDs
- [ ] Persona sheets with KPIs, workflows, tooling
- [ ] Dependency notes (BR-/API-/DBT-/TEST- suggestions)
- [ ] Lifecycle notes targeting v0.5 Red Team focus areas

## Your Deliverable
Update PRD with v0.4 User Journeys sections:

```markdown
## Personas

### [Primary Persona Name]
**Role:** [Title, org size, reporting structure]
**KPI / Success Definition:** [What they measure]
**Tools Today:** [Current stack] — Evidence: CFD-UJ-###
**Primary Device:** [Phone/tablet/desktop]
**Pains Tied to Monetization:**
- [Pain] → validates [BR-PRC-###] assumption

### [Secondary Persona Name]
[Same structure]

## Core User Journeys

### UJ-001: [Journey Title]
**Persona:** [Who]
**Trigger:** [What initiates this journey]

**Journey Flow:**
1. [Step] → Pain: [specific] → Evidence: CFD-UJ-###
2. [Step] → Pain: [specific]
3. [Continue 3-7 steps]

**Desired Value:** [Outcome tied to monetization]
**Dependencies:** API-###, BR-###

### UJ-002: [Journey Title]
[Same structure]

## Pain ↔ Value Mapping
| Pain | Evidence (CFD-) | Value Promise | Monetization Hook | Build Priority |
|------|-----------------|---------------|-------------------|----------------|
| [Pain 1] | CFD-UJ-### | [Value] | BR-PRC-### | High |

## Real-User Feedback Loop
| User/Role | Device | Feedback Cadence | Contact |
|-----------|--------|------------------|---------|
| [Name/Role] | [Device] | Weekly check-in | [method] |

Per CFD-401: Validate on real devices before build phase.

## Dependencies & New IDs
| ID | Type | Description | Owner | Status |
|----|------|-------------|-------|--------|
| UJ-001 | Journey | [Summary] | @product | New |
| BR-OPS-### | Policy | [Requirement] | @ops | New |
| API-LAB-### | Contract | [Data need] | @eng | Placeholder |

## Lifecycle Notes for v0.5 Red Team
Challenge these assumptions:
- [ ] [Unproven assumption about persona]
- [ ] [Risk in journey step]
- [ ] [Monetization assumption needing validation]

Open interviews needed: [list any coverage gaps]
```

## ID Register Updates
- New: UJ-*, CFD-UJ-*, BR-OPS-*, API-*
- Extended: [existing ID] → [updates]
- Dependencies: [IDs blocking architecture work]

## Quality Gates (Self-Check)
| Checkpoint | Pass Condition |
|------------|----------------|
| Persona Integrity | Data matches research, gaps flagged |
| Journey Clarity | Steps paraphrased accurately with citations |
| ID Registration | Every UJ-/CFD-/BR-/API- logged in SoT |
| Dependency Visibility | Downstream requirements have owners |
| Lifecycle Prep | Risks + assumptions clear for v0.5 |
| Feedback Loop Ready | Named users + device coverage logged |

## Output
1. PRD v0.4 sections (formatted as above)
2. ID Register diff
3. Gate recommendation (Ready for v0.5 / Blocked by [issue])
4. Stakeholder summary (personas added, key journeys, risks for Red Team)
```
