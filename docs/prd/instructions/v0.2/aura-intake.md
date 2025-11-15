# PRD v0.2 AURA Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Promote v0.1 sparks into a defensible Market Definition package covering segments, TAM sizing, and "Not for" rules while maintaining Gear Heart Methodology discipline.
**Inputs:** Research bundles created with the [PRD v0.2 Research Agent Instructions](./research-agents.md). Assume each bundle contains validated Segment Cards, Summary Sheet, artifact links, and candidate CFD-/BR- IDs.
**Deliverable:** Updated PRD sections (`Market Thesis`, `Segment Overview`, `Not For / Guardrails`, `Evidence Summary`) plus an ID Register diff capturing all CFD-/BR- actions and lifecycle notes for v0.3 Commercial Model.

## ID Interlock Map
- **Inputs:** `CFD-SGM-*` and `BR-NF-*` proposals from research, plus unresolved `CFD-SPARK-*` signals tracked in PRD v0.1.
- **Transformation:** Decide if inherited IDs are extended, merged, or deprecated. Annotate the PRD + SoT ledger to show lineage (e.g., "CFD-SPARK-002 → CFD-SGM-104 (segment focus refined)").
- **Outputs:**
  - Confirmed `CFD-SGM-*` entries embedded in PRD tables and SoT files.
  - Operational `BR-NF-*` rules with owners + enforcement cadence.
  - Lifecycle block noting which IDs will seed pricing (CFD-PRC-*), discount policies (BR-PRC-*), or KPI experiments in v0.3.

## Business Rule Criteria & Key Questions
1. **Segment Prioritization:** Which segments answer "Where do we win first?" and how do their IDs reflect that ordering inside the PRD change log?
2. **Guardrail Coverage:** Do the `BR-NF-*` rules close the top scope-creep risks noted in README/EPIC, and are the rules testable?
3. **Evidence Sufficiency:** Are TAM/TAM adjustments traceable to CFD artifacts with formulas so finance/execs can re-run assumptions?
4. **Downstream Readiness:** Does the lifecycle hook articulate the monetization questions (ASP, metric, discounting) the v0.3 team must solve, referencing the exact IDs that need updating?
5. **ID Hygiene:** Have you recorded every ID delta (new, extended, retired) in the SoT diff so automation can propagate context into future stages?

## Intake Checklist
Confirm every bundle includes:
- Summary Sheet table with TAM, urgency, and Not-For columns
- Segment Cards with transparent TAM math and evidence references
- Artifact files named `[segment-id]__[artifact].*` stored with shareable links
- Proposed CFD-/BR- IDs and lifecycle hooks in each card
- Cover note specifying priority order across segments

Escalate missing artifacts to the research lead before editing the PRD.

## Processing Workflow
1. **Load Context:** Read latest PRD v0.1 draft, open questions list, and README command surface. Note inherited IDs that will be extended.
2. **Bundle Prioritization:** Evaluate Summary Sheet priority cues. Select the top 2 segments for primary narrative, keeping others in appendix/backlog.
3. **Market Thesis Drafting:** Synthesize triggers + TAM into a 2–3 paragraph thesis referencing CFD- IDs inline. Highlight urgency (why now) and macro constraints.
4. **Segment Table Build:** Create/refresh the PRD table with columns for Size, Urgency, Tech Stack, Buying Committee, and Proposed "Next Gate". Cite artifact filenames for each row.
5. **Not-For & Guardrails:** Translate exclusion notes into BR- proposals. Document each as `Rule`, `Evidence`, `Owner`, `Lifecycle Impact`. Ensure a dedicated subsection exists in PRD v0.2.
6. **Evidence Summary:** Add a brief ledger referencing supporting CFD- IDs. Call out where data is missing and what v0.3 must validate (pricing, monetization, etc.).
7. **ID Register Updates:** Update the SoT backlog/ledger with the candidate IDs, status (`new`, `extend`, `blocked`), and owner. Note any dependencies on EPICs or SoT files.
8. **Lifecycle Alignment:** Close with a "Ready for v0.3" note enumerating what research/decisions remain.

## Output Template Snippet
```
# PRD v0.2 Market Definition Update

## Market Thesis
[Paragraphs referencing CFD-SGM-### artifacts]

## Segment Overview
| Segment | TAM | Urgency Signal | Buying Committee | Next Gate |
|---------|-----|----------------|------------------|-----------|
| ... | ... | ... | ... | ... |

## Not For & Guardrails
- **BR-SEG-201:** Rule description → Evidence (Artifact) → Owner → Lifecycle impact
- ...

## Evidence Summary
Bulleted list linking CFD- IDs to statements.

## Lifecycle Hook
- v0.3 Needs: [pricing research, competitive signals]
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Traceability** | Every claim ties back to a CFD- artifact or explicit TODO if evidence missing. |
| **Sizing Integrity** | TAM math reproduced verbatim from research; adjustments documented if scope changed. |
| **Guardrail Rigor** | Each BR- entry lists enforcement owner + measurement approach. |
| **Lifecycle Clarity** | Next milestone + required research plainly stated. |
| **ID Hygiene** | New IDs recorded in SoT ledger with status + source bundle. |

## Collaboration & Packaging
- Save drafts as `[segment-id-or-bundle]__prd-v0.2.md` alongside research artifacts before merging into canonical `PRD.md`.
- Notify stakeholders via README/EPIC notes summarizing: segments promoted, BR- adds, unresolved data.
- When splitting scope, tag backlog items with the corresponding Segment ID to maintain context for v0.3.

## Reporting Checklist
- [ ] PRD sections updated (Market Thesis, Segment Table, Not-For)
- [ ] Evidence citations reference correct artifact filenames
- [ ] SoT ID ledger updated with CFD-/BR- entries
- [ ] Lifecycle hook + v0.3 TODOs captured
- [ ] Summary posted to stakeholders with decision-ready signal
