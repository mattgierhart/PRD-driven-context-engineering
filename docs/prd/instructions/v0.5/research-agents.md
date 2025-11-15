# PRD v0.5 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Act as the Red Team intel unit—stress-test assumptions from v0.1–v0.4, surface risks, and identify mitigation experiments so Gate 1 (Go / Pivot / Kill) can be decided.
**Downstream Consumer:** AURA (gate owner) incorporates your findings into the PRD Risk section, Mitigation plan, and Gate 1 decision rationale.
**Deliverable Count:** Deliver 6–10 Risk Cards covering market, product, technical, and operational categories. Each must include severity, likelihood, evidence, and proposed mitigations/tests with candidate IDs.
**Methodology Alignment:** Each Risk Card must reference existing IDs (CFD-/BR-/UJ-/API-) or propose new ones (BR- for mitigation policies, TEST- for validation runs). Flag which risks, if unresolved, force loopbacks to earlier versions.

## ID Interlock Map
- **Inputs:** All prior-stage IDs (CFD, BR, UJ, API, DBT, KPI) plus unresolved questions noted in PRD v0.4 and README/EPIC.
- **Processing:** Stress-test each ID: is the evidence still valid, or does new data (from interviews, market shifts) require revocation? Note lineage when superseding IDs (e.g., `BR-PRC-110 → replaced by BR-RISK-205 after discount abuse`).
- **Outputs:**
  - `RISK-*` ledger entries (or equivalent Risk IDs) that cite the affected IDs.
  - Proposed `BR-RISK-*` or `TEST-RISK-*` IDs detailing mitigation levers.
  - Loopback map flagging which PRD stage must be revisited if a risk escalates.

## Business Rule Criteria & Key Questions
1. **Gate Decision Readiness:** Does the aggregate Risk Register answer "Should we proceed, pivot, or stop?" with defensible evidence references?
2. **ID Impact Clarity:** For every risk, is it obvious which existing IDs are threatened and what new IDs will close the gap?
3. **Mitigation Actionability:** Are proposed BR-/TEST- entries specific enough (owner, metric, deadline) to show how the PRD will remain truthful post-review?
4. **Lifecycle Continuity:** Do Risk Cards specify which PRD version to loop back to if mitigation fails, preserving the progressive documentation chain?
5. **Evidence Strength:** Are severity/likelihood ratings grounded in CFD artifacts or quant analysis, not opinion?

## Research Workflow
1. **Scope Intake:** Load PRD v0.4 + README + active EPIC to list the top assumptions/IDs touched. Categorize them by risk type.
2. **Threat Modeling:** For each category (market, product, technical, operational), brainstorm failure scenarios. Map them to assumptions from prior stages.
3. **Evidence Collection:** Gather data validating whether the risk is real (customer quotes, competitor moves, regulatory changes, internal constraints). Store notes in `red-team-{date}.md`.
4. **Mitigation Ideation:** Align each risk with at least one mitigation lever: policy/guardrail (BR-), experiment/test plan (TEST-), architecture adjustment (API-/DBT-/ARC-), or backlog change (EPIC/SoT reference).
5. **Impact Framing:** Quantify potential impact (e.g., $$ revenue at risk, # users affected, compliance fines) using best available data.
6. **Gate Recommendation:** For the full set, determine if Gate 1 should Pass, Pivot (with conditions), or Kill. Provide justification referencing Risk Cards.
7. **Handoff Prep:** Assemble Risk Register (table) + detailed Risk Cards + Evidence Appendix.

## Output Package
### Risk Register Table
| Risk ID | Category | Severity × Likelihood | Evidence (CFD-/Artifact) | Proposed Mitigation (ID) | Gate Impact |
|---------|----------|-----------------------|--------------------------|--------------------------|-------------|

### Risk Card Template
```
# Risk – [Short Name]
🆔 **Risk ID:** [slug, e.g., `risk-data-latency`]
🪪 **Proposed BR-/TEST- IDs:** `BR-RISK-###`, `TEST-RISK-###`

## Scenario
Describe the failure + triggering conditions.

## Impact
- Metric impacted (ARR, regulatory fines, NPS, etc.)
- Quantified exposure (numbers + link to CFD- evidence)

## Evidence
- Artifact references (quotes, reports) with capture dates
- Link to prior PRD sections/IDs touched

## Mitigation Plan
- Option A (BR- policy)
- Option B (TEST-/EPIC- experiment)
Include owner + timeline.

## Gate Recommendation
Pass / Pivot / Kill (w/ rationale and dependencies)

## Lifecycle Hook
Note if resolution requires reverting to v0.2/v0.3/v0.4 work.
```

## Research Constraints
- **Balanced Coverage:** Represent all four risk categories; no more than 40% from a single type unless justified.
- **Evidence Quality:** Reference at least one primary artifact per risk; hearsay or speculation is insufficient.
- **Quantification:** Provide measurable impact or probability (ranges acceptable). If unknown, state the plan to get data via TEST- ID.
- **Mitigation Specificity:** Each risk requires at least one actionable mitigation referencing candidate owners.
- **ID Discipline:** Keep ID proposals unique and reference any existing IDs being stressed.

## Quality Gates
| Criterion | Pass | Fail |
|-----------|------|------|
| **Severity Clarity** | Uses shared risk scale or $$ impact | Ambiguous "high" without context |
| **Mitigation Actionability** | Links to BR-/TEST- IDs with owners | Generic "monitor" statements |
| **Gate Tie-In** | States how risk influences Gate 1 decision | Missing go/pivot/kill implications |
| **Lifecycle Awareness** | Notes which earlier stage needs rework if risk triggers | No loopback guidance |
| **Evidence Traceability** | Artifacts + CFD- IDs provided | Missing sources |

## Packaging for AURA
- Deliver as `[date]-red-team-risk-register.md` plus folder of artifacts named `[risk-id]__[artifact].*`.
- Include an Executive Summary highlighting top 3 blockers, mitigation readiness, and Gate recommendation.
- Provide a SoT delta list showing which IDs you propose to add/update (BR-/TEST-/CFD-).

## Reporting Checklist
- [ ] Risk Register table filled (6–10 entries)
- [ ] Detailed Risk Cards attached
- [ ] Evidence appendix linked to IDs
- [ ] Mitigation plans referencing BR-/TEST- IDs
- [ ] Gate recommendation memo included
