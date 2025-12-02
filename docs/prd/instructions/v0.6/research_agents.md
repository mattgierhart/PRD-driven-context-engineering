# PRD v0.6 Research Agent Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). Keep filenames and structure consistent when cloning for future PRD stages.

## Mission Alignment
**Objective:** Provide the Build Lead (APOLLO/AURA technical delegate) with architecture-ready research: stack options, integration contracts, compliance considerations, and cost guardrails needed for the PRD v0.6 Architecture gate.
**Downstream Consumer:** Build Lead uses your analysis to document Technical Summary, Architecture Overview, Cost Model, and Integration requirements inside the PRD + SoT.
**Deliverable Count:** Deliver 2–3 Architecture Packets covering alternative stack configurations or deployment patterns. Each packet must include diagrams, integration inventories, cost calculations, and risk considerations.
**Methodology Alignment:** Findings must translate into ARC- IDs (architecture baselines), API-/DBT- IDs (contracts), BR- enforcement rules (e.g., data residency), and TECH-/DEP- IDs if infrastructure tooling is selected. Highlight dependencies on unresolved risks/tests from v0.5.

## ID Interlock Map
- **Inputs:** Gate 1 outputs (Risk IDs, `BR-RISK-*`, `TEST-*`), journey dependencies (`UJ-*`), and monetization guardrails (`BR-PRC-*` / `CFD-PRC-*`).
- **Processing:** Evaluate how each architecture option satisfies or conflicts with these IDs. Note if new architecture evidence supersedes prior assumptions (e.g., a cost guardrail updates `BR-PRC-120` or requires a new `TECH-*`).
- **Outputs:**
  - Candidate `ARC-*` IDs describing each architecture baseline.
  - `API-*` and `DBT-*` IDs for integration contracts, referencing journeys/risks they satisfy.
  - `BR-*`/`TECH-*` guardrails covering deployment, data residency, or observability requirements.
  - Dependency references to any `TEST-*` items required before Gate 2.

## Business Rule Criteria & Key Questions
1. **Risk Alignment:** Does each option show how it resolves the specific Risk IDs flagged in v0.5, or state residual risk + mitigation plan?
2. **Cost Assurance:** Are cost guardrails (<$0.10/user) backed by calculations linked to artifacts, and do they specify which BR-/TECH- IDs enforce them?
3. **Integration Clarity:** For every required system, do you define the API/DBT contract, owner, and security rules so architecture decisions are actionable?
4. **Progressive Documentation:** Can someone trace from persona/journey pain → monetization guardrail → architecture choice without gaps?
5. **Lifecycle Continuity:** Do packets define what evidence or approvals are needed to declare Gate 2 PASS and what IDs must be updated afterward?
6. **Experience Fidelity:** Have you specified how each architecture option supports priority devices (mobile vs. desktop) and surfaced responsive/UI considerations per [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)?

## Research Workflow
1. **Context Sync:** Read PRD v0.5 (risks + mitigations), README, active EPIC, and SoT entries referencing architecture (if any). Log unresolved risks impacting stack choices.
2. **Requirement Extraction:** From previous stages, list functional requirements, performance targets, compliance constraints, and integration touchpoints.
3. **Option Exploration:** For each architecture option (e.g., serverless vs. containerized, managed vs. custom integration), gather vendor capabilities, SLAs, pricing, and compliance certifications.
4. **Integration Mapping:** Identify required APIs, data pipelines, and event flows. Document the systems touched, data sensitivity, and ownership.
5. **Device Experience Planning:** Evaluate how the frontend/mobile experience will be delivered (responsive web, native wrappers, etc.) and capture any framework or testing implications, referencing [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build).
6. **Cost Modeling:** Build a simple cost model (<$0.10/user target) including infrastructure, 3rd-party services, and support. Provide best/worst case plus assumptions.
7. **Feasibility Assessment:** Evaluate risks (scalability, latency, vendor lock-in). Track dependencies on BR-/TEST- mitigations still open from v0.5.
8. **ID Proposal:** For each architecture option, propose ARC- ID(s) describing the blueprint, API-/DBT- IDs for contracts, and BR-/TECH- IDs for guardrails or tooling decisions.
9. **Handoff Prep:** Assemble Architecture Packets + Evidence ledger + comparison matrix to accelerate Build Lead decisions.

## Output Package
### Architecture Comparison Matrix
| Option | Summary | Core Tech | Est. Cost / User | Key APIs/DBTs | Risk Alignment |

### Architecture Packet Template
```
# Architecture Option – [Name]
🆔 **Packet ID:** [slug reused for ARC- and artifact naming]

## Context & Requirements
- Functional scope supported
- Constraints (compliance, latency, integrations)

## Reference Architecture
- Diagram (link or embed) referencing ARC- placeholder ID
- Component descriptions + data flow narrative

## Integration Inventory
| System | Direction | Data | API-/DBT- ID | Owner |

## Cost Model
- Assumptions (usage, data volume)
- Cost per user + monthly baseline (table)

## Risk Alignment
- Which v0.5 risks mitigated or exacerbated
- Dependencies (still-open BR-/TEST- IDs)

## Decision Signals
- Pros / Cons
- Ready-to-build prerequisites
```

## Research Constraints
- **Vendor Neutrality:** Present at least two viable architecture paths; avoid vendor lock-in recommendations without comparison.
- **Diagram Fidelity:** Provide diagrams (Mermaid, Excalidraw, etc.) that the Build Lead can import; include component labels.
- **Cost Transparency:** Show formulas + data sources for cost per user; cite pricing pages (artifact capture within 30 days).
- **Security & Compliance:** Include notes on data residency, encryption, access control. Reference BR- guardrails where needed.
- **Evidence Hygiene:** Archive vendor docs, benchmarks, or calculators used; map each to a CFD-/ARC- artifact ID.
- **Device Support:** Document which runtime/UI layer handles mobile-first requirements so downstream testing plans start with real devices (align with [CFD-401](../../../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)).

## Quality Gates
| Criterion | Pass | Fail |
|-----------|------|------|
| **Option Depth** | ≥2 architecture options with diagrams + cost | Single option or hand-wavy description |
| **Integration Clarity** | API-/DBT- touchpoints listed with owners | Missing integration detail |
| **Cost Accuracy** | Shows assumptions + remains within guardrail or states variance cause | Cost claim with no math |
| **Risk Connection** | References v0.5 risks + mitigations | Ignores prior risk register |
| **ID Mapping** | Candidate ARC-/API-/DBT-/BR-/TECH- IDs enumerated | No SoT linkage |

## Packaging for Build Lead
- Save packets as `[option-id]__architecture-packet.md` with diagrams/artifacts inside the same folder.
- Provide a README snippet summarizing recommendation + gating risks for quick stakeholder consumption.
- Deliver a SoT delta list showing proposed IDs and whether they are `new`, `extend`, or `blocked` pending decisions.

## Reporting Checklist
- [ ] Comparison matrix filled
- [ ] 2–3 Architecture Packets authored with diagrams
- [ ] Cost models validated + cited
- [ ] Integration inventory + candidate IDs documented
- [ ] Risk alignment + lifecycle notes for Gate 2 recorded
