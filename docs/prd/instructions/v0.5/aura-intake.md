# PRD v0.5 AURA Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Facilitate Red Team review, capture risks/mitigations inside the PRD, and document the Gate 1 (Go / Pivot / Kill) decision.
**Inputs:** Risk Register + Risk Cards produced via the [PRD v0.5 Research Agent Instructions](./research-agents.md), including candidate BR-/TEST- IDs and evidence artifacts.
**Deliverable:** Updated PRD sections (`Risk Overview`, `Risk Table`, `Mitigation Plan`, `Gate 1 Decision`), SoT ledger updates, and README signal summarizing the outcome.

## ID Interlock Map
- **Inputs:** Risk Cards referencing existing IDs and proposed mitigation IDs (BR-/TEST-/CFD- extensions).
- **Processing:** For every risk, document how it affects the PRD narrative and SoT: mark IDs as `validated`, `needs-mitigation`, or `blocked`. If a mitigation introduces new IDs, cross-link them to the risk row.
- **Outputs:**
  - Updated PRD risk tables citing `RISK-*` IDs and mapping them to the impacted `CFD-/BR-/UJ-/API-` entries.
  - Formalized `BR-RISK-*` and `TEST-RISK-*` entries with owners/dates.
  - Gate 1 decision note referencing the IDs that justify the choice and listing lifecycle impacts (e.g., "loop back to v0.3 if TEST-RISK-302 fails").

## Business Rule Criteria & Key Questions
1. **Decision Traceability:** Can stakeholders trace the Gate 1 outcome directly to the Risk IDs and supporting evidence without extra context?
2. **Mitigation Coverage:** Does every critical risk have at least one enforceable BR-/TEST- mitigation with a responsible owner and timeline?
3. **Documentation Continuity:** Are updates reflected in PRD, README, and SoT so the progressive narrative remains cohesive?
4. **Distribution Visibility:** Does the Gate note specify go-to-market experiments, channel tests, or audience-building tasks needed before launch, per [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)?
5. **Loopback Governance:** Have you clearly stated what triggers a regression to earlier PRD stages if certain mitigations fail?
6. **Stakeholder Readiness:** Do communications explain which IDs now control go/no-go decisions for architecture (v0.6) so the build team knows the constraints?

## Intake Checklist
Ensure bundle includes:
- Risk Register table (≥6 entries across categories)
- Detailed Risk Cards with severity × likelihood ratings
- Evidence artifacts linked to candidate CFD- IDs
- Proposed BR-/TEST- mitigations and owners
- Gate recommendation summary (Pass, Pivot, Kill)

## Processing Workflow
1. **Context Review:** Revisit PRD v0.4 to understand assumptions. Confirm SoT references for the IDs targeted by risks.
2. **Risk Categorization:** Validate coverage across market/product/technical/operational categories. Flag gaps for additional research if needed.
3. **Risk Table Construction:** Insert/refresh table capturing Risk ID, category, severity, likelihood, impact metric, mitigation, and ID references.
4. **Mitigation Detailing:** Translate research proposals into actionable BR-/TEST- entries with owners, due dates, and success criteria. Update SoT/backlog accordingly.
5. **Distribution Threading:** Convert any monetization or adoption risks into explicit GTM hypotheses (e.g., `BR-GTM-###`, `TEST-GTM-###`) so later stages prioritize audience-building work in line with [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build).
6. **Gate Recommendation Draft:** Summarize top risks, mitigation readiness, and decision logic. Use evidence citations and explicitly reference the Risk IDs.
7. **Decision Recording:** Convene stakeholders (virtually/asynchronously). Capture final Gate 1 decision, conditions, and follow-up tasks in PRD + README change log. If Pivot/Kill, state which PRD version to revert to and why.
8. **Lifecycle Hook:** Document what v0.6 (Architecture) needs based on the decision (e.g., risks that must be mitigated before build).
9. **Communication:** Publish a short update (README + Slack/email) listing Gate outcome, new IDs created, outstanding risks, and the distribution plan checkpoint.

## Output Template Snippet
```
## Risk Overview (v0.5)
### Top Risks
1. [Risk ID] – summary (Severity × Likelihood)

### Risk Table
| Risk | Category | Sev | Likelihood | Impact | Mitigation (ID) | Status |

### Mitigation Plan
- `BR-RISK-###`: [rule description, owner, due date]
- `TEST-RISK-###`: [experiment summary]

### Gate 1 Decision
Decision: PASS / PIVOT / KILL
Conditions: [...]
Evidence: [Risk IDs referenced]

### Lifecycle Notes
- Requirements for v0.6 Architecture
- Loopback instructions (if pivot/kill)
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Risk Coverage** | All risk categories present or rationale given. |
| **Mitigation Specificity** | Each mitigation includes owner, due date, and BR-/TEST- ID. |
| **Decision Clarity** | Gate outcome captured with rationale tied to Risk IDs. |
| **SoT Sync** | ID ledger updated for new BR-/TEST- entries and linked to PRD sections. |
| **Lifecycle Continuity** | Clear instructions for v0.6 on which risks remain open. |
| **Distribution Ready** | GTM hypotheses and supporting IDs documented so launch work begins early (see [CFD-401](../../../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)). |

## Collaboration & Packaging
- Draft updates in `[risk-bundle]__prd-v0.5.md` before merging to canonical PRD.
- Record Gate 1 decision in README "Latest Change Notes" with timestamp and link to PRD section.
- Notify stakeholders (engineering, finance, GTM) of new BR-/TEST- IDs requiring action.

## Reporting Checklist
- [ ] Risk Overview + Table updated in PRD
- [ ] Mitigations logged with ID references
- [ ] Gate 1 decision documented + broadcast
- [ ] SoT ledger updated for BR-/TEST-/CFD- deltas
- [ ] Distribution hypotheses + GTM IDs recorded
- [ ] Lifecycle instructions for v0.6 shared
