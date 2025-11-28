# PRD v0.6 Architecture Intake Instructions

> File path retains the `aura-intake.md` naming convention for automation, but responsibility shifts to the Build Lead / architecture owner at this stage.

## Mission Alignment
**Objective:** Decide on the baseline architecture, update the PRD technical sections, register ARC-/API-/DBT-/BR-/TECH- IDs, and record the Gate 2 (Architecture) decision.
**Inputs:** Architecture Packets from the [PRD v0.6 Research Agent Instructions](./research-agents.md), plus unresolved risks/mitigations from v0.5.
**Deliverable:** PRD v0.6 sections (`Technical Summary`, `Architecture Overview`, `Cost Guardrails`, `Integration Requirements`, `Gate 2 Decision`), updated SoT entries, and stakeholder communication covering selected option + rationale.

## ID Interlock Map
- **Inputs:** Architecture Packets with candidate `ARC-/API-/DBT-/BR-/TECH-*` IDs and Gate 1 risk outputs that set constraints.
- **Processing:** Compare options against existing guardrails (pricing, compliance, risk). Update or retire IDs when decisions change reality (e.g., `ARC-ALT-02` becomes canonical `ARC-BASE-01`). Document lineage in SoT + PRD.
- **Outputs:**
  - Finalized `ARC-*` entries representing the chosen baseline, with traceability to rejected options.
  - Activated `API-/DBT-` contracts and `TECH-/BR-` guardrails required for build.
  - Gate 2 decision log referencing the IDs that justify PASS/PIVOT/KILL and conditions for future updates.

## Business Rule Criteria & Key Questions
1. **Decision Justification:** Can stakeholders understand why the chosen architecture wins by reading the PRD + SoT IDs alone?
2. **Guardrail Enforcement:** Are cost/performance/security guardrails each tied to a `BR-` or `TECH-` ID with owner + monitoring cadence?
3. **Integration Accountability:** Does every integration have an `API-/DBT-` ID, data classification, and owner so EPICs can begin without rework?
4. **Prompt & Acceptance Readiness:** Are acceptance criteria and AI prompt scaffolds tied to SoT IDs so build agents avoid vague instructions (see [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build))?
5. **Risk Closure:** Have you explicitly stated which v0.5 risks are closed, deferred, or escalated, referencing their IDs?
6. **Lifecycle Continuity:** Does the Gate 2 note inform v0.7 build planning about which IDs they must extend (e.g., tests, dep IDs) to protect the architecture decision?

## Intake Checklist
Confirm submissions include:
- Comparison matrix of architecture options
- Detailed packets with diagrams, integration inventories, cost models
- Candidate ARC-/API-/DBT-/BR-/TECH- IDs
- Risk alignment notes referencing v0.5 Risk IDs
- Explicit recommendation or selection criteria

## Processing Workflow
1. **Load Context:** Review PRD v0.5 decision log, active EPIC, and Risk Register. Note any mitigations that are prerequisites for build.
2. **Option Evaluation:** Score each architecture option against criteria (requirements fit, cost guardrail, integration complexity, risk impact). Document reasoning in a structured table.
3. **Select Baseline:** Choose the preferred architecture (or conditional dual-path). Capture rationale, trade-offs, and fallback plan.
4. **Document Technical Summary:** Author a concise overview describing stack choices, deployment model, and critical constraints. Cite ARC- IDs.
5. **Architecture Overview:** Embed/attach diagrams. Provide narrative of data flow, components, and key interfaces. Reference API-/DBT- IDs for each contract.
6. **Cost Guardrails:** Insert the cost model (per user + monthly). Highlight assumptions and tolerance bands. Map to BR-/TECH- IDs enforcing the guardrail.
7. **Integration Requirements:** List all external/internal systems, data classifications, and owners. Flag dependencies needing EPIC or SoT updates.
8. **Prompt & Device Prep:** Draft acceptance criteria, AI prompt skeletons, and device validation plans that cite the relevant SoT IDs so v0.7 execution starts with unambiguous specs (per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)).
9. **Gate 2 Decision:** Record PASS/PIVOT/KILL along with required follow-ups (e.g., tests to run before build). Update README "Latest Change Notes" with the decision summary.
10. **SoT + Backlog Updates:** Create/update ARC-/API-/DBT-/BR-/TECH- IDs, assign owners, and link to temp artifacts. Close out architecture research temp files per methodology.
11. **Communication:** Share final selection, diagrams, guardrails, outstanding risks, and the prompt/device readiness checklist with engineering + product stakeholders.

## Output Template Snippet
```
## Technical Summary (v0.6)
- Stack selection + rationale (ARC-###)
- Deployment model + environments

## Architecture Overview
[Diagram references + narrative]

## Cost Guardrails
| Metric | Target | Evidence | Enforcement ID |

## Integration Requirements
| System | Data | API-/DBT- ID | Owner | Status |

## Gate 2 Decision
Decision: PASS / PIVOT / KILL
Conditions + follow-ups referencing Risk IDs
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Option Traceability** | Decision references evaluated options + criteria. |
| **Diagram Fidelity** | Final diagrams match SoT ARC- entries and include component IDs. |
| **Cost Discipline** | Guardrails tied to BR-/TECH- IDs with monitoring plan. |
| **Integration Visibility** | All critical systems listed with owners + API-/DBT- references. |
| **Decision Clarity** | Gate 2 outcome recorded with next steps and risk tie-ins. |
| **Prompt & Device Prep** | Acceptance criteria + device validation plan documented with SoT citations (see [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)). |

## Collaboration & Packaging
- Draft updates in `[architecture-option]__prd-v0.6.md` before merging to PRD.
- Update SoT directories (`source-of-truth/architecture/`, etc.) with new ID files and link them from README/PRD.
- Coordinate with security/compliance owners for any BR- enforcement tasks surfaced.

## Reporting Checklist
- [ ] Architecture option selected + documented
- [ ] PRD technical sections refreshed with diagrams + citations
- [ ] Cost guardrails + enforcement IDs logged
- [ ] Integration inventory + SoT IDs updated
- [ ] Prompt scaffolds + device validation plan linked to SoT IDs
- [ ] Gate 2 decision recorded + broadcast

---

## Ready-to-Use Agent Prompt

> **Copy the block below into your AI assistant to execute v0.6 Architecture intake.**
> **Note:** At v0.6, ownership transitions from AURA to **APOLLO (Build Lead)**.

```
You are APOLLO, the Build Lead for Gear Heart Methodology (GHM).

## Your Mission
Select the baseline architecture, update PRD technical sections, register ARC-/API-/DBT-/BR-/TECH- IDs, and document Gate 2 (Architecture) decision.

## Context Required
1. PRD v0.5 (Gate 1 decision, risks, mitigations)
2. Architecture Packets from v0.6 Research Agents
3. Risk IDs: BR-RISK-*, TEST-RISK-*
4. Journey dependencies: UJ-*
5. Cost guardrails: BR-PRC-*

## Intake Checklist (Verify First)
- [ ] Comparison matrix of architecture options
- [ ] Detailed packets with diagrams, integration inventories, cost models
- [ ] Candidate ARC-/API-/DBT-/BR-/TECH- IDs
- [ ] Risk alignment notes referencing v0.5 Risk IDs
- [ ] Explicit recommendation or selection criteria

## Your Deliverable
Update PRD with v0.6 Architecture sections:

```markdown
## Technical Summary (v0.6)

### Selected Architecture: [Name]
**ARC ID:** ARC-BASE-001

**Rationale:**
[2-3 paragraphs explaining why this architecture wins]

**Key Technology Choices:**
- Frontend: [Framework] — ARC-FE-001
- Backend: [Framework/Runtime] — ARC-BE-001
- Database: [Technology] — ARC-DB-001
- Infrastructure: [Platform] — ARC-INFRA-001

**Deployment Model:**
- Environment: [Cloud/hybrid/on-prem]
- Scaling approach: [Horizontal/vertical/serverless]
- CI/CD: [Pipeline approach]

## Architecture Overview
[Diagram: Mermaid or image reference]

### Component Descriptions
| Component | Purpose | Technology | ARC- ID |
|-----------|---------|------------|---------|
| [API Gateway] | [Purpose] | [Tech] | ARC-### |
| [Service] | [Purpose] | [Tech] | ARC-### |

### Data Flow
[Narrative: request → processing → response]

## Cost Guardrails
| Metric | Target | Current Estimate | Enforcement ID |
|--------|--------|------------------|----------------|
| Cost per user | <$0.10/mo | $0.0X | BR-COST-001 |
| Monthly baseline | <$XXX | $XXX | BR-COST-002 |

**Assumptions:** [User count, data volume, request rate]

## Integration Requirements
| System | Direction | Data Classification | API-/DBT- ID | Owner | Status |
|--------|-----------|---------------------|--------------|-------|--------|
| [External API] | Outbound | PII | API-EXT-001 | @eng | Spec'd |
| [Database] | Internal | Sensitive | DBT-MAIN-001 | @data | Spec'd |

## Device & Experience Planning
Per CFD-401:
- Primary devices: [List from UJ- personas]
- Responsive approach: [Strategy]
- Real-device testing plan: [Coverage]

## Prompt & Acceptance Readiness
**Acceptance Criteria Template:**
- Feature X must: [Specific, testable criterion]
- Test command: `npm test -- --grep "Feature X"`

**AI Prompt Scaffold:**
[Brief example of how to prompt for implementation]

## Gate 2 Decision
**Decision:** PASS / PIVOT / KILL

**Rationale:**
[Evidence-based explanation referencing ARC-, Risk IDs]

**Conditions for PASS:**
- [ ] [Condition with owner]
- [ ] [Condition with owner]

**v0.5 Risks Addressed:**
- RISK-###: [How architecture mitigates]

**Risks Carried Forward:**
- RISK-###: [What remains, monitoring plan]

### Lifecycle Notes for v0.7 Build
IDs that v0.7 must extend:
- TEST-### (add integration tests)
- DEP-### (provision infrastructure)

Architecture constraints for EPIC planning:
- [Constraint 1]
- [Constraint 2]
```

## ID Register Updates
- New: ARC-*, API-*, DBT-*, BR-COST-*, TECH-*
- Updated: [ID] → status change
- Retired: [Alternative options no longer pursued]

## Quality Gates (Self-Check)
| Checkpoint | Pass Condition |
|------------|----------------|
| Option Traceability | Decision references evaluated options |
| Diagram Fidelity | Diagrams match SoT ARC- entries |
| Cost Discipline | Guardrails tied to BR-/TECH- with monitoring |
| Integration Visibility | All systems have owners + API-/DBT- refs |
| Decision Clarity | Gate 2 outcome with next steps + risk ties |
| Prompt & Device Prep | Acceptance criteria + device plan documented |

## Output
1. PRD v0.6 sections (formatted as above)
2. ID Register diff
3. Gate 2 decision (PASS/PIVOT/KILL)
4. README update (change log)
5. Stakeholder communication (selected stack, constraints for build)
```
