# PRD v0.3 AURA Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Translate monetization research into a PRD v0.3 Commercial Model narrative covering anchor competitors, pricing model, guardrails, fast-follow, and moat statements.
**Inputs:** Monetization Briefs produced under the [PRD v0.3 Research Agent Instructions](./research-agents.md), including artifacts, candidate CFD-/BR-/KPI- IDs, and lifecycle notes.
**Deliverable:** Updated PRD sections (`Commercial Model`, `Pricing Guardrails`, `Competitive Anchors`, `Moat Thesis`) plus a refreshed ID register and README callouts for downstream EPICs.

## ID Interlock Map
- **Inputs:** `CFD-PRC-*` data, `BR-PRC-*` guardrails, and KPI/test hooks from research, along with segment IDs inherited from v0.2.
- **Processing:** Translate each monetization hypothesis into PRD narrative + SoT entries. If a prior ID is superseded (e.g., `CFD-SGM-104` replaced by `CFD-PRC-220` for monetization context), log it in the SoT diff.
- **Outputs:**
  - PRD entries citing `CFD-PRC-*` artifacts and linking to segment IDs they refine.
  - Finalized `BR-PRC-*` guardrails with measurement owners.
  - Activated `KPI-*` seeds for tracking monetization experiments.
  - Lifecycle notes assigning which journeys (`UJ-*`) must validate price sensitivity next.

## Business Rule Criteria & Key Questions
1. **Model Completeness:** Can a reviewer answer "How do we make money and why will buyers accept it?" purely from the PRD v0.3 sections with supporting IDs?
2. **Guardrail Readiness:** Are `BR-PRC-*` rules testable (clear owner, metric, threshold) and tied to risk mitigations logged in README/SoT?
3. **Moat Validation:** Does every differentiation claim cite a `CFD-PRC-*` artifact and state how it informs the fast-follow plan or future EPIC scope?
4. **Experiment Planning:** Have you tagged `KPI-*`/test IDs with the question they answer (e.g., conversion, ARPU) so engineering/ops can prep instrumentation?
5. **Lifecycle Continuity:** Does the lifecycle hook tell v0.4 exactly which personas/journeys must validate monetization assumptions and which IDs they should extend?

## Intake Checklist
Ensure each brief includes:
- Scoreboard summary with segment/pricing ranges
- ≥3 competitor profiles with evidence artifacts
- Monetization hypotheses (≥2) with assumptions and risks
- Candidate BR- rules, KPI- seeds, and lifecycle hooks
- Experiment/test ideas that inform v0.4 interviews

Request rework if any brief lacks pricing artifacts or explicit ID proposals.

## Processing Workflow
1. **Context Refresh:** Load PRD v0.2 Market section + Not-For guardrails. Note the segments being promoted and open market questions.
2. **Brief Selection:** Prioritize segments flagged as "Ready". If more than two, choose the ones with clearest monetization signals for PRD focus and list others under Future Work.
3. **Anchor Competitor Table:** Build a PRD table summarizing competitor packaging, price, differentiators, and references. Cite CFD- IDs inline.
4. **Monetization Narrative:** For each promoted segment, write a 2–3 paragraph summary explaining the recommended model, rationale, and risks. Reference KPI- seeds where measurement is needed.
5. **Pricing Guardrails:** Convert BR- proposals into enforceable rules (floor, ceiling, discount logic, triggers). Document owner + enforcement hook.
6. **Fast-Follow Delta:** Add a short subsection listing where we will trail or copy competitor moves (tie to lifecycle plan and possible EPIC IDs).
7. **Moat Thesis:** Summarize differentiation pillars referencing competitor gaps. Include any dependencies requiring validation in v0.4.
8. **ID Register Updates:** Log each new/updated CFD-, BR-, KPI- ID in the SoT ledger with state and owner. Flag tests to be built in v0.5+.
9. **Lifecycle Hook:** Close with an explicit statement of what v0.4 user research must uncover regarding pricing sensitivity and adoption journeys.

## Output Template Snippet
```
## Commercial Model (v0.3)
### Anchor Competitors
| Vendor | Package | Price | Evidence |

### Recommended Monetization Model
[Summary paragraphs citing CFD-PRC-###]
- KPI Hooks: `KPI-ARPU-###`
- Assumptions

### Pricing Guardrails
- `BR-PRC-105`: Floor/ceiling + enforcement

### Moat Thesis & Fast-Follow
Bullets describing differentiation + copycat strategy.

### Lifecycle Next Step
What v0.4 interviews must test.
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Evidence Traceability** | Every figure references an artifact file + CFD- ID. |
| **Model Cohesion** | Pricing model ties directly to validated segment needs and Moat statements. |
| **Guardrail Practicality** | Each BR- entry names measurement owner + frequency. |
| **Lifecycle Planning** | Future work ties to specific personas/interview goals. |
| **ID Ledger Sync** | SoT updated with status + cross-links to PRD statements. |

## Collaboration & Packaging
- Draft updates in `[segment-id]__prd-v0.3.md` before merging to `PRD.md`.
- Share a summary update in README/EPIC call-outs with: chosen model, guardrails, key risks.
- Coordinate with finance/build leads for KPI instrumentation plans referenced in KPI- IDs.

## Reporting Checklist
- [ ] Commercial Model section updated with evidence citations
- [ ] Anchor Competitor table inserted/refreshed
- [ ] BR- pricing guardrails logged and linked
- [ ] KPI-/CFD- IDs recorded in SoT ledger
- [ ] Lifecycle plan + interview agenda for v0.4 documented
