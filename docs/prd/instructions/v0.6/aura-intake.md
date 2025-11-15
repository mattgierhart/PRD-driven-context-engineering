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
4. **Risk Closure:** Have you explicitly stated which v0.5 risks are closed, deferred, or escalated, referencing their IDs?
5. **Lifecycle Continuity:** Does the Gate 2 note inform v0.7 build planning about which IDs they must extend (e.g., tests, dep IDs) to protect the architecture decision?

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
8. **Gate 2 Decision:** Record PASS/PIVOT/KILL along with required follow-ups (e.g., tests to run before build). Update README "Latest Change Notes" with the decision summary.
9. **SoT + Backlog Updates:** Create/update ARC-/API-/DBT-/BR-/TECH- IDs, assign owners, and link to temp artifacts. Close out architecture research temp files per methodology.
10. **Communication:** Share final selection, diagrams, guardrails, and outstanding risks with engineering + product stakeholders.

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

## Collaboration & Packaging
- Draft updates in `[architecture-option]__prd-v0.6.md` before merging to PRD.
- Update SoT directories (`source-of-truth/architecture/`, etc.) with new ID files and link them from README/PRD.
- Coordinate with security/compliance owners for any BR- enforcement tasks surfaced.

## Reporting Checklist
- [ ] Architecture option selected + documented
- [ ] PRD technical sections refreshed with diagrams + citations
- [ ] Cost guardrails + enforcement IDs logged
- [ ] Integration inventory + SoT IDs updated
- [ ] Gate 2 decision recorded + broadcast
