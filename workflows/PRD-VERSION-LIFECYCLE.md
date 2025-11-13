---
title: "PRD Version Lifecycle Workflow"
version: 1.0
updated: "2025-02-14"
---

# PRD Version Lifecycle · v0.1 → v1.0

> **Purpose**: Define the non-skippable lifecycle gates for a PRD within the Gear Heart Methodology.
> **Audience**: Product strategists (AURA), build agents (CLAUDE/APOLLO), and reviewers running gate checks.
> **Companion Docs**: `README.md`, `PRD.md`, `CLAUDE.md`, `templates/epics/EPIC-template.md`, `workflows/UNIQUE-ID-SYSTEM.md`.

---

## How to Use This Workflow
1. Start each working session by confirming the current gate in `README.md`.
2. Read the corresponding section in `PRD.md` to understand intent, evidence, and SoT references.
3. Use the gate checklists below to validate readiness before advancing.
4. Record gate approvals in `PRD.md` (Lifecycle Change Log) and surface summary in `README.md`.
5. When looping back, document the reason (e.g., “v0.3r1 – new pricing data CFD-214”).

---

## Gate Overview

| Gate | Owner | Definition of Ready | Definition of Done | Primary IDs |
|------|-------|---------------------|--------------------|-------------|
| **v0.1 Spark** | AURA | Problem hypothesis captured, stakeholders aligned on outcomes. | Problem statement, desired outcomes, constraints, success signals recorded. | CFD- / BR- |
| **v0.2 Market Definition** | AURA | Spark validated; initial research available. | ICPs + segments defined, “not for” list, market sizing, supporting research logged. | CFD- / BR- |
| **v0.3 Commercial Model** | AURA | Market slices accepted; competitors identified. | Monetization model, pricing hypotheses, fast-follow anchors, moat thesis. | CFD- / BR- |
| **v0.4 User Journeys** | AURA | Commercial assumptions plausible; target user flows identified. | 3–7 user journeys tied to pains, SoT IDs drafted, dependencies noted. | UJ- / BR- / API- |
| **v0.5 Red Team Review** | AURA | Journeys + business model complete. | Risks cataloged with mitigations, early warning signals, dev challenges flagged. | BR- / TEST- |
| **v0.6 Architecture** | Build Lead | Risks understood; requirements stable. | Architecture baseline documented (API, DBT, integration notes), tooling decisions recorded. | API- / DBT- / ARC- |
| **v0.7 Build Execution** | Build Lead | Architecture signed off; EPIC backlog sized. | Active EPIC(s) planned, QA strategy in place, Definition of Done agreed. | EPIC / TEST- |
| **v0.8 Deployment & Ops** | Build Lead | Build nearing completion; deployment pathways identified. | Release criteria met, runbooks + monitoring defined, DEP- IDs updated. | DEP- / TEST- |
| **v0.9 Go-to-Market** | GTM Lead | Deployment path locked; success metrics defined. | Launch plan, messaging, analytics instrumentation, feedback loops active. | CFD- / GTM- |
| **v1.0 Market Adoption** | Product Lead | Launch complete; usage + revenue data flowing. | Paying customers, retention metrics, optimization roadmap, loopback triggers documented. | KPI- / CFD- |

---

## Gate Checklists

### v0.1 Spark
- [ ] Problem statement references at least one CFD- ID.
- [ ] Desired outcomes measurable (baseline + target).
- [ ] Constraints & non-goals documented.
- [ ] Open questions list created for v0.2.

### v0.2 Market Definition
- [ ] Segmentation table complete (size, urgency, source ID).
- [ ] “Not for” segment defined.
- [ ] Business rules (BR- IDs) capture any go/no-go constraints.
- [ ] Open questions for v0.3 identified.

### v0.3 Commercial Model
- [ ] Anchor competitor table filled with pricing estimates.
- [ ] Monetization model chosen with rationale.
- [ ] Fast-follow delta (1–10%) articulated.
- [ ] Pricing hypotheses mapped to BR-/CFD- IDs.

### v0.4 User Journeys
- [ ] Minimum three journeys with persona, trigger, steps, pain, value.
- [ ] Proposed UJ- IDs listed with titles and cross-links.
- [ ] Dependencies (BR-/API-/DBT- IDs) noted.
- [ ] Outstanding validation items flagged for v0.5.

### v0.5 Red Team Review
- [ ] Risks table complete across market/product/technical/operational.
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
- [ ] Runbooks drafted (link to SoT).
- [ ] Rollback / contingency considered.

### v0.9 Go-to-Market
- [ ] Launch calendar, messaging pillars, channel owners set.
- [ ] Analytics dashboards or metrics instrumentation ready.
- [ ] Feedback loop defined (CFD-/GTM- IDs).
- [ ] Success metrics + reporting cadence assigned.

### v1.0 Market Adoption
- [ ] Paying customer data recorded with KPI- IDs.
- [ ] Retention / engagement metrics tracked.
- [ ] Optimization backlog documented (EPIC references).
- [ ] Loopbacks identified (which gate to revisit and why).

---

## Gate Review Ritual
1. Prepare: Owner assembles evidence (links to PRD sections, SoT IDs, EPIC references).
2. Review: Cross-functional group (strategy, build, GTM) walks through checklist.
3. Decide: Approve, approve-with-actions, or block.
4. Record: Update `PRD.md` change log + `README.md` lifecycle table. Note decision in EPIC or project tracker.
5. Follow-up: Capture any actions as new EPICs/issues or SoT updates.

---

## Loopbacks & Exceptions
- Loopbacks must create a new row in the PRD change log (e.g., v0.3r2) with reason + triggering evidence.
- Emergency changes still require ID updates; if time-constrained, log TODOs with owners and due dates.
- If a gate is skipped due to external pressure, record the rationale and mitigation plan explicitly in `PRD.md` and the EPIC retrospective.

---

## Companion Resources
- `workflows/UNIQUE-ID-SYSTEM.md` — ID formats & registry guidance.
- `templates/product/product-PRD-template.md` — structured PRD template implementing this lifecycle.
- `templates/epics/EPIC-template.md` — execution container referencing lifecycle gates.
- `templates/agents/AURA-primary-agent-template.md` — strategy lead instructions for v0.1–v0.5.

Keep this workflow file updated as the methodology evolves.

