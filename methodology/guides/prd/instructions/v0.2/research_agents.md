# PRD v0.2 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Validate market segments, quantify TAM/SAM/SOM, and flag "Not for" guardrails that will power the PRD v0.2 Market Definition gate.
**Downstream Consumer:** AURA (or delegated strategy drafter) uses your output to populate the Market Thesis, Segment Table, and Not-For sections of the PRD plus seed CFD-/BR- IDs in the Source-of-Truth (SoT) graph.
**Deliverable Count:** Provide 2–3 fully validated segments per assignment. Each must include demand urgency evidence and at least one exclusion criteria.
**Methodology Alignment:** Every segment must map to (a) new or extended CFD- IDs that hold market data, (b) proposed BR- IDs for go/no-go rules, and (c) lifecycle hooks pointing to v0.3 Commercial Model preparation.

## ID Interlock Map
- **Inputs:** `CFD-SPARK-*` signals + open questions logged in PRD v0.1; any provisional BR- guardrails already noted in README.
- **Processing:** Extend or retire inherited IDs as evidence matures. Record changes in your temp notes so the SoT ledger reflects lineage (e.g., `CFD-SPARK-003 → superseded by CFD-SGM-101`).
- **Outputs:**
  - New `CFD-SGM-*` entries capturing TAM math, urgency triggers, and quantitative references.
  - New `BR-NF-*` rules defining exclusions tied to evidence.
  - Lifecycle hook table noting which IDs will evolve into pricing (CFD-PRC-*) or KPI seeds in v0.3.

## Business Rule Criteria & Key Questions
1. **Segment Viability:** Does each proposed `CFD-SGM-*` answer *who we serve*, *why now*, and *how big the upside is*? If not, loop back until the question is resolved.
2. **Exclusion Discipline:** Can every `BR-NF-*` rule be enforced (owner + metric) and does it prevent scope creep in the PRD narrative?
3. **Evidence Provenance:** Are TAM calculations reproducible from the cited data? Document formulas inline so downstream reviewers can audit quickly.
4. **Lifecycle Continuity:** Do you state what monetization/pricing unknowns remain so v0.3 can pick them up without re-reading raw research?
5. **ID Readiness:** Before submission, confirm each artifact is tagged with the ID it justifies so AURA can drop it straight into the SoT diff.

## Research Workflow
1. **Context Load:** Open the 3 + 1 (Claude.md → README.md → PRD.md → active EPIC) plus SoT records touched in v0.1. Log any inherited IDs you plan to extend in your temp notes (`market-research-{date}.md`).
2. **Segment Shortlist:** Derive 4–5 hypotheses from the v0.1 open questions. Rank by data availability and ability to articulate "Not for" boundaries quickly. Only advance the top 2–3.
3. **Data Sweep:** For each segment, capture:
   - Market size (TAM with citation, SOM proxy if possible)
   - Buying trigger and urgency signals (news, funding, regulatory changes within 12 months)
   - Channel/concentration data (top vendors, # of businesses, tool usage)
4. **Exclusion Rules:** Document what makes a customer out-of-scope (org size, compliance tier, geography, tech stack). These will become BR- IDs inside the PRD.
5. **Evidence Logging:** Attach screenshots/PDFs for every metric or quote. Name files `[segment-id]__[artifact-type].*` and map them to candidate CFD- IDs such as `CFD-SGM-###`.
6. **Handoff Prep:** Build the Summary Sheet + Segment Cards noted below. Close with lifecycle notes describing what v0.3 research is already unlocked per segment.

## Output Package
### 1. Summary Sheet (table)
| Segment ID | Segment Name | TAM (USD) | Primary Urgency Signal | Not-For Boundary | Lifecycle Hook |
|------------|--------------|-----------|------------------------|------------------|----------------|
| `sgm-dental-labs` | Independent Dental Labs | $1.2B | FDA 2024 traceability rule (CFD-SGM-101) | Labs <5 seats | Ready for v0.3 pricing benchmark |

### 2. Segment Card Template (repeat per segment)
```
## [Segment Name]
🪪 **Segment ID:** [slug — reuse in filenames and candidate CFD-/BR- IDs]
📏 **Size & Economics:** TAM $X.XB, SOM $Y.YM ARR (Sources: [link1], [link2])
⏱️ **Urgency / Trigger:** [One-liner with timestamped citation]
💼 **Buying Committee:** [Roles involved, seat counts, budget owner]
🧠 **Job-To-Be-Done:** [≤40 words]
🚫 **NOT FOR:** [Clear exclusion statement → propose BR- ID `BR-NF-[slug]`]
📊 **Evidence Ledger:**
   - `CFD-SGM-###`: [artifact description, file name, capture date]
   - `CFD-SGM-###`: [...]
🔍 **Channel & Stack Notes:** [Existing tools, integration blockers]
📈 **Lifecycle Hook:** [What needs to happen in v0.3 and beyond]
```

## Research Constraints
- **Recency:** Market data must be <12 months old. If older, include the inflation/adjustment logic inline.
- **TAM Discipline:** Derive TAM using transparent formulas (e.g., #accounts × ASP). Link each assumption to a CFD- artifact.
- **Segment Precision:** Avoid umbrella categories. Include NAICS/SIC or other objective identifiers when possible.
- **Not-For Evidence:** Every exclusion must be grounded in evidence (compliance requirements, cost structure, tool mismatch). No speculative exclusions.
- **ID Traceability:** Reference candidate CFD-/BR- IDs inside the Summary Sheet and Segment Cards so AURA can instantiate them without re-tracing.

## Quality Gates
| Criterion | Pass Condition | Reject Condition |
|-----------|----------------|------------------|
| **Evidence Depth** | ≥2 primary sources per segment (one quant, one qualitative) | Reliance on single analyst blog |
| **Exclusion Clarity** | Explicit rule + rationale + supporting artifact | "Not for small teams" without data |
| **Urgency Signal** | Triggered within 12 months and tied to segment economics | Generic tailwind with no timestamp |
| **TAM Math** | Transparent formula + numbers add up | Hand-wavy multiples without sourcing |
| **Lifecycle Hook** | States the next research/drafting need for v0.3 | Missing downstream guidance |

## Packaging for AURA
- Store the submission as `[date]-market-definition-v0.2.md` alongside artifacts in `/temp/` before handoff; archive after sign-off per methodology.
- Provide a Source List appendix mapping each citation to the candidate CFD- ID so SoT updates are one-click.
- Flag `BR-` proposals explicitly, e.g., ``BR-REG-201 – Exclude LATAM due to PSD2 variance (Artifact: sgm-finops__regulation.pdf)``.
- Include a cover note summarizing where segments differ most and which should enter the PRD first.

## Reporting Checklist
- [ ] 2–3 Segment Cards completed with fresh data
- [ ] Summary Sheet table populated
- [ ] Not-For statements + candidate BR- IDs documented
- [ ] Evidence files named per convention and linked to CFD- IDs
- [ ] Lifecycle hooks for v0.3 recorded
- [ ] Temp notes updated + archived reference noted in README if required
