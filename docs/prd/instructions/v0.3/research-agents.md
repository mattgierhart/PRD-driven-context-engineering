# PRD v0.3 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Deliver monetization intelligence (pricing ladders, competitor benchmarks, willingness-to-pay signals) that lets AURA write the PRD v0.3 Commercial Model section with confidence.
**Downstream Consumer:** AURA (or pricing-strategy delegate) will convert your research into Monetization Model, Pricing Guardrails, Anchor Competitor Table, and Moat statements.
**Deliverable Count:** Produce one Monetization Brief per prioritized segment (2 briefs minimum). Each brief must include at least three anchor competitors and two monetization experiments.
**Methodology Alignment:** Findings must map to CFD- IDs for pricing/market data, BR- IDs for pricing or discount rules, and optional KPI- IDs for measuring monetization experiments. Call out how each brief prepares v0.4 journey work (e.g., which personas care about pricing levers).

## ID Interlock Map
- **Inputs:** `CFD-SGM-*` segment data, `BR-NF-*` guardrails, and open monetization questions logged in PRD v0.2.
- **Processing:** Extend CFD entries when pricing research refines the segment thesis (e.g., `CFD-SGM-102 → CFD-PRC-210`). Track cross-links so readers know which pricing data unlocks which segment.
- **Outputs:**
  - `CFD-PRC-*` IDs capturing competitor pricing, WTP quotes, and package comparisons.
  - `BR-PRC-*` guardrails defining pricing floors, ceilings, discount constraints, and triggers.
  - Optional `KPI-*` seeds for ARPU, conversion, or payback targets.
  - Persona hints referencing upcoming `UJ-*` targets so v0.4 knows which journeys to validate.

## Business Rule Criteria & Key Questions
1. **Revenue Model Fit:** Does every monetization hypothesis answer "How do we charge?" and "What drives margin?" for the prioritized segments?
2. **Guardrail Enforceability:** Are proposed `BR-PRC-*` rules measurable (owner, metric, cadence) so finance/build teams can enforce them in PRD + SoT?
3. **Competitive Anchoring:** Do `CFD-PRC-*` entries show the rationale for being above/below each anchor competitor? Capture delta and mitigation.
4. **Experiment Path:** Are the KPI/test suggestions concrete enough for the future EPIC backlog, with IDs referencing where results will live?
5. **Lifecycle Continuity:** Do briefs specify exactly what v0.4 needs to verify with users (e.g., price sensitivity per persona) so the journey work can build on this research without rework?

## Research Workflow
1. **Preparation:** Review PRD v0.2 Market Definition outputs (segment priorities, BR- guardrails) and the open questions flagged for v0.3. Note which IDs you are extending in `pricing-research-{date}.md`.
2. **Anchor Competitor Sweep:** For each segment, gather three competitors representing premium, parity, and budget tiers. Capture: pricing metric (per seat, per workflow), add-on costs, packaging rules, discount triggers.
3. **Buyer Willingness Evidence:** Collect quotes/interviews showing budget ceilings or ROI expectations. Prefer sources within the last 6 months.
4. **Commercial Hypothesis Drafting:** Frame at least two monetization paths (e.g., usage-based vs. tiered) referencing the evidence. Include assumptions, sensitivities, and gating questions.
5. **Moat Investigation:** Identify where differentiation can exist (compliance coverage, integration lock-in, workflow speed). Tie each to evidence / competitor gaps.
6. **ID Mapping:** For every discrete data set, propose CFD-IDs (e.g., `CFD-PRC-201`). For every rule (discount floors, bundling constraints), propose BR- IDs (e.g., `BR-PRC-105`). Flag candidate KPI- IDs for measuring ARPU, conversion, or payback.
7. **Handoff Prep:** Assemble Monetization Briefs, artifact bundle, and summary scoreboard (pricing ranges, moats, risk). Highlight open issues needed for v0.4.

## Output Package
### Monetization Scoreboard (top of submission)
| Segment | Anchor Competitors | Price Band (USD) | Proposed Model | KPI Seeds |
|---------|--------------------|------------------|----------------|-----------|
| ... | ... | ... | ... | ... |

### Monetization Brief Template (per segment)
```
# [Segment ID] Monetization Brief – PRD v0.3
🧾 **Brief ID:** [slug reused in filenames and candidate CFD-/BR- entries]

## Anchor Competitors
| Vendor | Packaging | Price | Evidence (Artifact) | Notes |
|-------|-----------|-------|----------------------|-------|

## Pricing Signals & WTP
- Quote: "..." – Source (Artifact: ...)
- Budget Context: [Ops metric describing spend / seat]

## Proposed Monetization Paths
1. **Model A:** [Description, metric, target ASP, supporting CFD- ID]
   - Risks / assumptions
   - Candidate BR- entries (discount rules, usage caps)
2. **Model B:** [...]

## Moat Thesis
- Differentiator 1 (e.g., compliance, workflow speed) → Evidence (CFD-PRC-###)
- Differentiator 2 → ...

## KPI & Experiment Hooks
- `KPI-ARPU-###`: [Metric definition + measurement plan]
- Test Ideas: [2 short experiment descriptions]

## Lifecycle Notes
- What v0.4 needs validated (personas sensitive to price, journey updates)
- Dependencies (tech, partnerships)
```

## Research Constraints
- **Pricing Proof:** Screenshots/PDFs for every price reference captured within 30 days.
- **Multiple Models:** Provide at least two monetization hypotheses per segment even if one is preferred.
- **Moat Evidence:** Differentiation must cite competitor gaps, not internal aspiration.
- **Data Fidelity:** Record currency and billing units explicitly; avoid rounding beyond two significant digits without justification.
- **ID Continuity:** If extending an existing CFD-, note it (e.g., `CFD-PRC-101 → extended with 2025 data`).

## Quality Gates
| Criterion | Pass | Fail |
|-----------|------|------|
| **Competitor Coverage** | ≥3 distinct competitors with artifacts | Duplicated vendors or secondary sources only |
| **Model Clarity** | Hypotheses include metric, ASP, constraints | Vague "subscription" statements |
| **Moat Articulation** | Evidence-backed differentiators mapped to IDs | Aspirational language without proof |
| **Experiment Utility** | KPI/test ideas actionable within next EPIC | Research-only suggestions |
| **Lifecycle Readiness** | Calls out what v0.4 must interview/test | No downstream guidance |

## Packaging for AURA
- Zip artifacts per segment (`[segment-id]__pricing-artifacts.zip`) or provide folder links mirroring ID names.
- Provide an `Evidence Ledger` appendix linking file name → CFD-/BR- proposals → PRD statement.
- Add a cover memo summarizing recommended monetization path plus top two risks.

## Reporting Checklist
- [ ] Scoreboard table complete
- [ ] ≥2 Monetization Briefs with artifacts
- [ ] Candidate CFD-/BR-/KPI- IDs enumerated
- [ ] Moat statements grounded in evidence
- [ ] Lifecycle notes for v0.4 recorded
