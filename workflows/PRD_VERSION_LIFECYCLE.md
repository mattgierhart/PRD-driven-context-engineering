---
title: "PRD Version Lifecycle Workflow"
version: 1.1
updated: "2025-02-14"
authority: "Gear Heart Methodology · Tier 1"
scope: "Lifecycle gate checks for advancing PRD v0.1 → v1.0"
---

# PRD Version Lifecycle · v0.1 → v1.0

> **Purpose**: Define the non-skippable lifecycle gates for a PRD within the Gear Heart Methodology.
> **Audience**: Strategy leads (AURA), build agents, reviewers, and PMs validating readiness at each gate.
> **Companion Docs**: [`WORKFLOW-PRD-DEVELOPMENT.md`](WORKFLOW-PRD-DEVELOPMENT.md) for deep stage guidance, `README.md`, `PRD.md`, `CLAUDE.md`, [`UNIQUE-ID-SYSTEM.md`](UNIQUE-ID-SYSTEM.md).

---

## Quick Reference Ladder

| Gate | Owner | Focus | Primary Outputs | Key IDs |
|------|-------|-------|-----------------|---------|
| **v0.1 Spark** | AURA | Problem + outcomes | PRD spark narrative, open questions | CFD- |
| **v0.2 Market Definition** | AURA | Segments + TAM | PRD market thesis, segment table | CFD- / BR- |
| **v0.3 Commercial Model** | AURA | Monetization & positioning | PRD commercial model, moat thesis | CFD- / BR- |
| **v0.4 User Journeys** | AURA | Personas & journeys | PRD journey section, proposed UJ- IDs | UJ- / CFD- / BR- |
| **v0.5 Red Team Review** | AURA | Risks & Gate 1 decision | PRD risk analysis, mitigation plan | BR- / TEST- |
| **v0.6 Architecture** | Build Lead | Technical feasibility | PRD tech summary, stack decisions | API- / DBT- / ARC- |
| **v0.7 Build Execution** | Build Lead | EPIC cycles | EPIC backlog, QA plan, PRD v0.7.x log | EPIC / TEST- |
| **v0.8 Deployment & Ops** | Build Lead | Release readiness | Runbooks, deployment strategy | DEP- / RUN- / TEST- |
| **v0.9 Go-to-Market** | GTM Lead | Launch & analytics | Launch plan, instrumentation, feedback loop | GTM- / CFD- / KPI- |
| **v1.0 Market Adoption** | Product Lead | Adoption & optimization | Adoption metrics, optimization backlog | KPI- / CFD- |

> For durations, SoT timing, and temp file patterns see [`WORKFLOW-PRD-DEVELOPMENT.md`](WORKFLOW-PRD-DEVELOPMENT.md#lifecycle-ladder).

---

## Gate Deliverables & Documentation Discipline

### v0.1 Spark
- **PRD**: Executive summary, problem statement, desired outcomes, constraints, initial success signals.
- **SoT**: Seed CFD- IDs (founder notes, market signals).
- **Temp**: Spark research notes archived at gate exit.

### v0.2 Market Definition
- **PRD**: Market thesis, segment/TAM table, "not for" statements, enabling BR- rules.
- **SoT**: CFD- IDs for research evidence; BR- IDs capturing go/no-go constraints.
- **Temp**: Market research scratchpads (moved to archive after extraction).

### v0.3 Commercial Model
- **PRD**: Anchor competitor table, monetization model, pricing guardrails, moat thesis.
- **SoT**: CFD- IDs for pricing intelligence; BR- IDs for pricing rules; optional KPI- seeds.
- **Temp**: Competitive/pricing analysis notes.

### v0.4 User Journeys
- **PRD**: Persona summaries, journey overview, pain/value alignment.
- **SoT**: Draft UJ- IDs, linked CFD- interview IDs, dependency BR-/API-/DBT- IDs.
- **Temp**: Interview transcripts, journey sketches (cleared once SoT updated).

### v0.5 Red Team Review
- **PRD**: Risk table with mitigations, early warning signals, Gate 1 decision.
- **SoT**: BR- IDs for mitigation rules, TEST- IDs for validation tasks.
- **Temp**: Red-team session logs archived; any TODOs captured with owners and due dates.

### v0.6 Architecture
- **PRD**: Technical summary, architecture overview, infrastructure cost guardrails.
- **SoT**: API- contracts, DBT- schemas, ARC- architecture baselines, BR- enforcement notes.
- **Temp**: Architecture trade-off logs archived post decision.

### v0.7 Build Execution
- **PRD**: v0.7.x change log entries summarizing EPIC outcomes, validated assumptions.
- **SoT**: TEST-, DEP-, API-, DBT-, BR-, UJ- updates per EPIC; recorded in EPIC Section 3A ledger.
- **Temp**: EPIC phase notes cleared in Phase E and archived by month.

### v0.8 Deployment & Ops
- **PRD**: Deployment readiness checklist, rollback approach, monitoring summary.
- **SoT**: DEP- deployment playbook, RUN- runbooks, MON- monitoring configs, TEST- perf validations.
- **Temp**: Dry-run logs, security reviews → archived once actions complete.

### v0.9 Go-to-Market
- **PRD**: Launch plan, messaging pillars, analytics plan, feedback loop description.
- **SoT**: GTM- campaign IDs, CFD- feedback capture, KPI- instrumentation specs.
- **Temp**: Launch checklists, feedback trackers (archived weekly).

### v1.0 Market Adoption
- **PRD**: Adoption metrics, retention analysis, optimization roadmap, loopback triggers.
- **SoT**: KPI- adoption metrics, CFD- post-launch insights, EPIC references for optimization work.
- **Temp**: Adoption review notes archived after reporting cycle.

---

## Gate Checklists

Use these before marking a gate complete. Every checkbox should tie to evidence in `PRD.md`, SoT IDs, or EPIC notes.

### v0.1 Spark
- [ ] Problem statement references at least one CFD- ID.
- [ ] Desired outcomes include baseline and target metrics.
- [ ] Constraints and non-goals captured.
- [ ] Open question list prepared for v0.2.

### v0.2 Market Definition
- [ ] Segment table complete (size, urgency, source ID).
- [ ] "Not for" segment defined with rationale.
- [ ] BR- IDs record gating business rules.
- [ ] Open questions for v0.3 documented with owners.

### v0.3 Commercial Model
- [ ] Anchor competitors table completed with pricing signals.
- [ ] Monetization model documented with rationale.
- [ ] Fast-follow delta (1–10%) articulated.
- [ ] Pricing hypotheses mapped to BR-/CFD- IDs.

### v0.4 User Journeys
- [ ] Minimum three journeys mapped with persona, trigger, steps, pains, value.
- [ ] Proposed UJ- IDs listed with titles and cross-links.
- [ ] Dependencies (BR-/API-/DBT- IDs) noted.
- [ ] Outstanding validation items flagged for v0.5.

### v0.5 Red Team Review
- [ ] Risks table covers market/product/technical/operational categories.
- [ ] Early warning signals + mitigation strategies captured.
- [ ] Development challenges noted for EPIC planning.
- [ ] Candidate TEST- IDs proposed for mitigation.

### v0.6 Architecture
- [ ] Architecture summary aligns with PRD scope and risk plan.
- [ ] API- IDs created/updated for critical endpoints.
- [ ] DBT- IDs outline key schema changes.
- [ ] Integration or compliance requirements documented.

### v0.7 Build Execution
- [ ] EPIC backlog prioritized with clear lifecycle impact.
- [ ] QA/test approach codified (TEST- IDs).
- [ ] Definition of Done confirmed.
- [ ] README + CLAUDE instructions synchronized.

### v0.8 Deployment & Ops
- [ ] Deployment environments + automation mapped (DEP- IDs).
- [ ] Monitoring/alerting configured or planned.
- [ ] Runbooks drafted and linked (RUN-/MON- IDs).
- [ ] Rollback / contingency scenario documented and rehearsed.

### v0.9 Go-to-Market
- [ ] Launch calendar, messaging pillars, channel owners set.
- [ ] Analytics dashboards or metrics instrumentation ready (KPI-/ANL- IDs).
- [ ] Feedback loop defined (CFD-/GTM- IDs) with capture cadence.
- [ ] Success metrics + reporting cadence assigned.

### v1.0 Market Adoption
- [ ] Paying customer data recorded with KPI- IDs.
- [ ] Retention / engagement metrics tracked.
- [ ] Optimization backlog documented (EPIC references).
- [ ] Loopbacks identified (which gate to revisit and why).

---

## Gate Review Ritual
1. **Prepare** — Owner assembles evidence (PRD sections, SoT IDs, EPIC references) and updates README lifecycle widget.
2. **Review** — Cross-functional group (strategy, build, GTM) walks through checklist together.
3. **Decide** — Approve, approve-with-actions, or block. Document action items with owners & due dates.
4. **Record** — Update `PRD.md` change log and `README.md` lifecycle summary. Note decisions in EPIC or project tracker.
5. **Follow-up** — Capture actions as new EPICs/issues or SoT updates. Confirm completion before closing the gate.

---

## Loopbacks & Exceptions
- Loopbacks must create a new row in the PRD change log (e.g., `v0.3r2`) with reason and triggering evidence (ID or metric).
- Emergency skips require explicit rationale + mitigation plan in PRD and EPIC retrospective; schedule follow-up gate review.
- Maintain README “Active IDs” table so agents know which SoT artifacts changed during loopbacks.

---

## Companion Resources
- [`WORKFLOW-PRD-DEVELOPMENT.md`](WORKFLOW-PRD-DEVELOPMENT.md) — Detailed stage-by-stage workflow, durations, SoT timing.
- [`templates/epics/EPIC-template.md`](../templates/epics/EPIC-template.md) — Execution container with ID ledger.
- [`templates/product/product-PRD_template.md`](../templates/product/product-PRD_template.md) — PRD scaffold aligned to this lifecycle.
- [`templates/agents/AURA-primary-agent-template.md`](../templates/agents/AURA-primary-agent-template.md) — Strategy lead guidance for v0.1–v0.5.

Keep this workflow updated with field learnings. Increment the version header and surface changes in `README.md` when revisions ship.
