---
title: "PRD Development Workflow"
version: 2.0
updated: "2025-02-14"
authority: "Gear Heart Methodology · Tier 1"
purpose: "Define milestone-based PRD progression (v0.1 → v1.0) and documentation discipline for 3+1+SoT+Temp."
---

# PRD Development Workflow · v0.1 → v1.0

> **Purpose**: Operational playbook for progressing a PRD from Spark to Market Adoption without skipping lifecycle gates.
> **Audience**: Primary strategy agent (AURA), build leads (APOLLO or equivalents), and reviewers running gate checks.
> **Companion Docs**: [`PRD-VERSION-LIFECYCLE.md`](PRD-VERSION-LIFECYCLE.md), [`PROGRESSIVE-DOCUMENTATION-GUIDE.md`](PROGRESSIVE-DOCUMENTATION-GUIDE.md), [`UNIQUE-ID-SYSTEM.md`](UNIQUE-ID-SYSTEM.md), [`templates/product/product-PRD-template.md`](../templates/product/product-PRD-template.md).

---

## 3 + 1 + SoT + Temp Framework

### Core Navigation Files ("The 3")
```
Claude.md  → HOW we work
README.md  → WHERE we are
PRD.md     → WHAT we are building
```
- Always load in that order at the start of every session.
- `README.md` owns the Command Center surface and points to the active EPIC.
- `PRD.md` changes at lifecycle gates only; do not use it for daily status updates.

### Active Execution File ("+1")
```
Active EPIC → EPIC file named in README.md (Section “Current Work Surface”)
```
- Tracks tasks, ID deltas, and temp files for the current build window.
- Frozen at EPIC completion and archived under `archive/`.

### Source of Truth (SoT) References
- Long-form references keyed by IDs (BR-/API-/DBT-/CFD-/UJ-/DEP-/KPI-… ).
- Updated during EPIC Phase E and lifecycle gate transitions.
- Never duplicated in PRD; PRD cites SoT IDs instead.

### Temp Artefacts
- Ephemeral scratchpads stored in `temp/` during active work.
- Naming: `{type}-{YYYY-MM-DD}-{topic}.md` (e.g., `analysis-2025-02-14-pricing.md`).
- Extract insights into SoT during Phase E → archive to `archive/YYYY-MM/` → delete from `temp/`.

---

## Lifecycle Ladder

| Version | Gate | Primary Owner | Typical Duration | Focus | Core Outputs | Gate Criteria |
|---------|------|---------------|------------------|-------|--------------|---------------|
| **v0.1** | Spark | AURA | 1–2 days | Problem + outcomes framing | PRD spark narrative, CFD- seeds | Clear problem statement, desired outcomes, open questions |
| **v0.2** | Market Definition | AURA | 3–5 days | Segments, ICP, “not for” clarity | PRD market section, CFD-/BR- IDs | Validated segments, TAM sizing evidence |
| **v0.3** | Commercial Model | AURA | 3–5 days | Monetization, pricing anchors | PRD commercial section, BR-/CFD- IDs | Fast-follow positioning, pricing hypotheses |
| **v0.4** | User Journeys | AURA | 5–7 days | Personas, journeys, pains | PRD journey section, UJ- IDs | 3–7 mapped journeys tied to pains |
| **v0.5** | Red Team Review | AURA | 1–2 days | Risks, mitigations, go/no-go | PRD risks section, BR-/TEST- IDs | Risk table with mitigations, Gate 1 decision |
| **v0.6** | Architecture | Build Lead | 3–5 days | Stack, contracts, feasibility | PRD tech summary, API-/DBT-/ARC- IDs | Architecture baseline, cost guardrails |
| **v0.7.x** | Build Execution | Build Lead | 2–3 weeks / EPIC | Implementation in EPIC cycles | EPIC files, TEST- IDs, PRD v0.7.x log | EPIC DoD met, tests pass, SoT updated |
| **v0.8** | Deployment & Ops | Build Lead | 3–5 days | Release readiness | DEP- IDs, runbooks, PRD deploy section | Deployment + rollback plans validated |
| **v0.9** | Go-to-Market | GTM Lead | 1–2 weeks | Launch plan, analytics, feedback | PRD GTM section, GTM-/CFD- IDs | Launch calendar, instrumentation active |
| **v1.0** | Market Adoption | Product Lead | 2–4 weeks | Adoption, optimization | PRD adoption section, KPI-/CFD- IDs | Paying customers, retention + optimization plan |

> **Loopbacks**: Add `rN` suffix in PRD change log (e.g., `v0.3r1`) with reason and triggering ID.

---

## Stage Playbooks

Each stage below specifies the **work being done**, **required documentation**, and **completion criteria** before advancing to the next gate.

### v0.1 Spark — Problem & Outcomes
- **Work**: Capture spark narrative, define pains, align on outcomes.
- **PRD Updates**: Executive summary, problem statement, desired outcomes, initial success signals, constraints, open questions.
- **SoT / IDs**: Seed CFD- IDs for founding insights or market signals.
- **Temp Files**: `spark-research-{date}.md`, `stakeholder-notes-{date}.md`.
- **Complete When**:
  - [ ] Problem statement references at least one CFD- insight.
  - [ ] Outcomes include measurable success signals.
  - [ ] Constraints/non-goals documented.
  - [ ] Open question list for v0.2 maintained.

### v0.2 Market Definition — Segments & ICP
- **Work**: Validate segments, quantify opportunity, state exclusions.
- **PRD Updates**: Market thesis, segment table (size, urgency, sources), "Not for" list, enabling BR- rules, research evidence summary.
- **SoT / IDs**: Create/extend CFD- IDs for research, BR- IDs for gating rules (e.g., geography constraints).
- **Temp Files**: `market-research-{date}.md`, `segment-analysis-{date}.md`.
- **Complete When**:
  - [ ] At least two segments validated with evidence.
  - [ ] TAM / sizing documented with methodology.
  - [ ] "Not for" criteria explicit.
  - [ ] BR- IDs capture go/no-go rules.
  - [ ] Open items for v0.3 captured.

### v0.3 Commercial Model — Monetization & Positioning
- **Work**: Analyze competitors, define monetization, state moat thesis.
- **PRD Updates**: Anchor competitor table, monetization model, pricing guardrails, fast-follow delta, moat statement.
- **SoT / IDs**: CFD- IDs for pricing research, BR- IDs for pricing/discount rules, optional KPI- seeds.
- **Temp Files**: `pricing-research-{date}.md`, `competitive-analysis-{date}.md`.
- **Complete When**:
  - [ ] Anchor competitors profiled with price signals.
  - [ ] Monetization model documented with rationale.
  - [ ] Pricing hypotheses include measurable deltas.
  - [ ] Moat thesis tied to evidence (IDs cited).
  - [ ] Pending questions for v0.4 enumerated.

### v0.4 User Journeys — Personas & Pains
- **Work**: Convert commercial hypotheses into validated user journeys.
- **PRD Updates**: Persona summaries, pain points with quotes, journey overview table, value realization narrative.
- **SoT / IDs**: Draft UJ- IDs for each journey; extend CFD- IDs with interview data; create BR-/API- dependency notes.
- **Temp Files**: `user-interview-{date}-{persona}.md`, `journey-sketch-{date}.md`.
- **Complete When**:
  - [ ] 3–7 core journeys mapped with persona, trigger, steps, pains, value.
  - [ ] Each journey linked to proposed UJ- ID.
  - [ ] Quotes / evidence stored under CFD- IDs.
  - [ ] Dependencies to BR-/API-/DBT- IDs noted for v0.5 and beyond.

### v0.5 Red Team Review — Risks & Gate 1 Decision
- **Work**: Challenge assumptions, categorize risks, decide go/no-go.
- **PRD Updates**: Risk table (market/product/technical/operational), mitigation strategies, early warning signals, Gate 1 decision rationale.
- **SoT / IDs**: BR- IDs for mitigation rules, TEST- IDs for validation tasks, risk log references.
- **Temp Files**: `red-team-{date}.md`, `gate1-decision-{date}.md`.
- **Complete When**:
  - [ ] Risks categorized with severity & owners.
  - [ ] Mitigations tied to BR-/TEST- IDs.
  - [ ] Decision recorded (PASS / PIVOT / KILL) in PRD change log.
  - [ ] All temp insights extracted or assigned.

### v0.6 Architecture — Technical Feasibility (Gate 2)
- **Work**: Choose stack, design architecture, validate cost & integration.
- **PRD Updates**: Technical summary, architecture overview, cost guardrails (<$0.10/user), key integrations.
- **SoT / IDs**: API- contracts, DBT- schema, ARC- architecture, BR- enforcement rules, TECH- or DEP- as needed.
- **Temp Files**: `architecture-evaluation-{date}.md`, `tech-stack-tradeoffs-{date}.md`.
- **Complete When**:
  - [ ] Architecture diagram and rationale captured (ARC- ID).
  - [ ] API- and DBT- IDs cover core surfaces.
  - [ ] Cost model validated and documented.
  - [ ] Integration/compliance requirements enumerated.
  - [ ] Gate 2 decision recorded.

### v0.7.x Build Execution — EPIC Cycles
- **Work**: Implement features via EPIC phases A–E.
- **PRD Updates**: v0.7.x change log entries summarizing EPIC outcomes, validated assumptions, learning repository references.
- **SoT / IDs**: Update TEST-, DEP-, API-, DBT-, BR-, and UJ- IDs per feature; log new IDs in EPIC Section 3A.
- **Temp Files**: `EPIC-XX-analysis-{date}.md`, `decision-{date}-{topic}.md`, `test-plan-{date}.md` (cleared during Phase E).
- **Completion Requirements Per EPIC**:
  - [ ] Phases A–E complete with checklist sign-off.
  - [ ] Tests at target coverage with results logged.
  - [ ] SoT files updated and referenced in PRD/README.
  - [ ] Temp files archived under `archive/YYYY-MM/`.
  - [ ] README metrics refreshed.

### v0.8 Deployment & Ops — Gate 3
- **Work**: Prepare production deployment, monitoring, and runbooks.
- **PRD Updates**: Deployment strategy, launch readiness checklist, rollback approach.
- **SoT / IDs**: DEP- deployment procedures, RUN- runbooks, MON- monitoring configs, TEST- performance validations.
- **Temp Files**: `deployment-dryrun-{date}.md`, `security-review-{date}.md`.
- **Complete When**:
  - [ ] Environments configured and validated.
  - [ ] Monitoring/alerting operational.
  - [ ] Rollback plan tested.
  - [ ] Security review complete with actions tracked.
  - [ ] Gate 3 decision logged.

### v0.9 Go-to-Market — Launch & Feedback
- **Work**: Execute launch plan, instrumentation, and feedback loops.
- **PRD Updates**: Launch calendar, messaging pillars, analytics plan, feedback capture process.
- **SoT / IDs**: GTM- IDs for campaigns, CFD- IDs for feedback channels, KPI- seeds for tracking.
- **Temp Files**: `launch-brief-{date}.md`, `feedback-log-{date}.md`.
- **Complete When**:
  - [ ] Launch plan approved with owners and dates.
  - [ ] Instrumentation dashboards ready (KPI-/ANL- IDs).
  - [ ] Feedback loop defined (CFD-/GTM- IDs).
  - [ ] Launch execution window scheduled.

### v1.0 Market Adoption — Optimization & Loopbacks
- **Work**: Validate adoption, track retention, define optimization roadmap.
- **PRD Updates**: Adoption metrics, retention analysis, optimization backlog, loopback triggers.
- **SoT / IDs**: KPI- IDs for usage metrics, CFD- IDs for feedback, EPIC references for upcoming optimization work.
- **Temp Files**: `adoption-review-{date}.md`, `optimization-plan-{date}.md`.
- **Complete When**:
  - [ ] Paying customers & retention targets met.
  - [ ] Optimization roadmap captured with EPIC IDs.
  - [ ] Loopbacks recorded (which gate to revisit and why).
  - [ ] PRD flagged as v1.0 in change log.

---

## EPIC Workflow (Phase A–E)

| Phase | Focus | Key Actions | Outputs |
|-------|-------|-------------|---------|
| **A. Planning & Analysis** | Load context (3+1+SoT), scope EPIC, list IDs to touch. | EPIC brief updated, temp analysis notes created. | Section 2 of EPIC template complete. |
| **B. Design** | Draft UX/tech designs, confirm dependencies. | Design artifacts, updated UJ-/API- references. | Section 3B documented. |
| **C. Implementation** | Build features, write tests alongside code. | Commits/PRs referencing EPIC. | Section 3C progress notes. |
| **D. Testing & Validation** | Run tests, address QA, capture learnings. | Test results, issues resolved. | Section 3D checklist complete. |
| **E. Documentation & Handoff** | Update SoT, archive temp, refresh README metrics. | SoT diffs, archived files, PRD/README updates. | Section 3E sign-off, lifecycle increment (v0.7.x+1). |

> See [`templates/epics/EPIC-template.md`](../templates/epics/EPIC-template.md) for the detailed EPIC structure and ID ledger.

---

## SoT Creation Timeline
```
v0.2 → CFD- (research evidence), BR- (market rules)
v0.3 → CFD-/BR- (pricing), KPI- seeds
v0.4 → UJ- (journeys), CFD- (interviews)
v0.5 → BR-/TEST- (mitigations)
v0.6 → API-, DBT-, ARC-, BR-
v0.7.x → TEST-, DEP-, UJ-, DBT- updates
v0.8 → DEP-, RUN-, MON-
v0.9 → GTM-, CFD-, KPI-
v1.0 → KPI-, CFD-, EPIC references for optimization
```

Maintain an ID ledger in each EPIC (Section 3A) and aggregate into README “Active IDs” table.

---

## Temp File Lifecycle Enforcement
1. **Create** during Phases A–D for fast capture (store under `temp/`).
2. **Extract** insights into PRD/SoT during Phase E.
3. **Archive** to `archive/YYYY-MM/` with same filename.
4. **Delete** temp originals post-archive to keep repo tidy.
5. **Never reference** temp files directly from PRD — always cite SoT IDs.

> Automation idea: scheduled check to ensure no temp file older than 7 days remains.

---

## Post-v1.0 Evolution
- Continue using the same `PRD.md` (no new PRD files) for v1.1, v1.2…
- Use README “Active Work” to point to enhancement EPICs (v1.1.x).
- Only create a new PRD when undertaking a fundamental pivot or re-architecture (new market, new product).
- Keep SoT directories evergreen; append new IDs rather than replacing.

---

## Related References
- [`CLAUDE.md`](../CLAUDE.md) — Behavior expectations & documentation discipline.
- [`docs/REPO-ORGANIZATION.md`](../docs/REPO-ORGANIZATION.md) — Folder scaffolding for copy-ready repos.
- [`templates/agents/AURA-primary-agent-template.md`](../templates/agents/AURA-primary-agent-template.md) — Strategy lead playbook for v0.1–v0.5.

Keep this workflow aligned with field usage; update the version header and change log in README when revisions occur.
