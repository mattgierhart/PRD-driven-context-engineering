---
version: 2.0
purpose: Progressive Product Requirements Document aligned to the PRD Led Context Engineering lifecycle.
last_updated: 2025-12-22
---

# [Product Name] · Product Requirements Document (PRD)

**Authority & Workflow**

- `README.md` — repository orientation (always read first).
- `PRD.md` — this file. Owns the strategic narrative from v0.1 → v1.0.
- `CLAUDE.md` — agent behavior. Confirms how to implement what this PRD asks for.
- `epics/EPIC-{XX}-<slug>.md` — execution window. Updates IDs created/modified when advancing v0.7+.
- See `README.md` for gate criteria and rituals.

**Template Usage**

1. Replace placeholders (`{}`) with product-specific data.
2. Maintain strict version headers (v0.1 → v1.0). Never delete prior versions; append revisions.
3. Use SoT IDs (BR-XXX, CFD-XXX, etc.) whenever referencing research, rules, or technical decisions.
4. Log lifecycle transitions in the change log table below. Reference EPIC IDs for execution notes.

---

## PRD Metadata

| Field                      | Value                              |
| -------------------------- | ---------------------------------- |
| **Current Lifecycle Gate** | v0.x                               |
| **Last Updated**           | 2025-12-22                         |
| **Last Editor**            | {Name / Agent}                     |
| **Status**                 | Discovery / Build / Live           |
| **Next Target Gate**       | v0.{x+1}                           |
| **Related EPIC**           | EPIC-{XX}                          |
| **SoT Snapshot**           | {List key IDs touched this update} |

## Lifecycle Change Log

| Version                | Date       | Editor  | Summary                              | Linked IDs / EPIC   |
| ---------------------- | ---------- | ------- | ------------------------------------ | ------------------- |
| v0.1 Spark             | YYYY-MM-DD | {Owner} | Problem + outcomes framed            | CFD-###             |
| v0.2 Market Definition | YYYY-MM-DD | {Owner} | ICP + segmentation                   | BR-###              |
| v0.3 Commercial Model  | YYYY-MM-DD | {Owner} | Pricing & positioning hypotheses     | BR-###, CFD-###     |
| v0.4 User Journeys     | YYYY-MM-DD | {Owner} | Journeys mapped to pains             | UJ-###              |
| v0.5 Red Team Review   | YYYY-MM-DD | {Owner} | Risks + mitigations                  | BR-###, TEST-###    |
| v0.6 Architecture      | YYYY-MM-DD | {Owner} | Stack, schema, contracts baseline    | API-###, DBT-###    |
| v0.7 Build Execution   | YYYY-MM-DD | {Owner} | EPIC backlog & QA strategy           | EPIC-{XX}, TEST-### |
| v0.8 Release & Deployment | YYYY-MM-DD | {Owner} | Release criteria + ops playbook   | DEP-###             |
| v0.9 Go-to-Market      | YYYY-MM-DD | {Owner} | GTM, analytics, feedback loop        | GTM-### / CFD-###   |
| v1.0 Market Adoption   | YYYY-MM-DD | {Owner} | Paying customers + optimization plan | BR-###, KPI-###     |

> **Revision Pattern**: When looping back, add a new row (e.g., `v0.3r1`) and reference the EPIC that triggered the revision.

---

## v0.1 Spark — Problem & Outcomes

**Spark Summary**  
{Short paragraph describing the spark, audience, and outcomes. Elevator pitch style.}

**Problem Statement**

- **Who is hurting?** {Segment / persona}
- **What pain exists today?** {Short description}
- **Why now?** {Trigger or catalyst}

**Desired Outcomes**

- {Outcome 1 — measurable}
- {Outcome 2 — measurable}

**Initial Success Signals**

- Metric: {Signal / Source} (Target: {value})
- Insight IDs: {CFD-###, note or link}

**Constraints & Non-goals**

- {Constraint 1}
- {Non-goal 1}

**Open Questions** (must be answered before v0.2)

- {Question}
- {Question}

---

## v0.2 Market Definition — ICP & Segments

**Market Thesis**  
{Short narrative referencing Spark outcomes.}

**Primary Segments (max 3)**
| Segment | Description | Size / TAM | Urgency | Source (ID) |
|---------|-------------|------------|---------|-------------|
| Segment A | {Persona / firmographics} | {Value} | {High/Med/Low} | CFD-### |

**Not For**

- {Who we explicitly exclude and why}

**Enabling Business Rules (BR-XXX)**

- BR-### — {Rule description}
- BR-### — {Rule description}

**Research & Evidence**

- CFD-### — {Interview / survey insight}
- CFD-### — {Desk research}

**Outstanding Work → v0.3**

- {Hypothesis or question}

---

## v0.3 Commercial Model — Pricing & Positioning

**Anchor Competitors**
| Competitor | Positioning | Pricing Signals | Reference |
|------------|-------------|-----------------|-----------|
| {Name} | {Value prop} | ${price}/unit | CFD-### |

**Monetization Strategy**

- Model: {Usage / Seat / Tiered}
- Primary KPI: {MRR / ACV / etc}
- Pricing Guardrails: {Range or constraints}

**Moat Thesis**

- {What makes us 1–10% better/cheaper}
- Supporting IDs: BR-###, CFD-###

**Experiments & Fast-Follow Plans**

- {Experiment summary} → ID: BR-### / TEST-###

**Outstanding Work → v0.4**

- {Hypothesis requiring user validation}

---

## v0.4 User Journeys — From Pain to Value

**Journey Overview**
| ID | Persona | Trigger | Key Steps | Pain Points | Moments of Value |
|----|---------|---------|-----------|-------------|------------------|
| UJ-### | {Persona} | {Trigger} | {Steps summary} | {Pain} | {Value}

**Journey Narratives**

- **UJ-### – {Title}**
  - Step Flow: {1 → 2 → 3}
  - Dependencies: BR-###, API-###
  - Opportunity Notes: {Design or build implications}

**UX / Research Assets**

- Link: `SoT/SoT.USER_JOURNEYS.md#uj-###`
- Additional references: {Figma / research IDs}

**Outstanding Work → v0.5**

- {Risk or open question to stress-test}

---

## v0.5 Red Team Review — Risks & Mitigations

**Risk Register**
| Category | Risk | Impact | Likelihood | Early Signal | Mitigation | Linked IDs |
|----------|------|--------|------------|--------------|------------|------------|
| Market | {Risk description} | {H/M/L} | {H/M/L} | {Signal} | {Mitigation action} | BR-### |

**Development Challenges (Flag for EPIC Planning)**

- {Challenge} → Impacted IDs: API-###, TEST-###

**Security / Compliance Notes**

- {Requirement} → BR-### / DEP-###

**Outstanding Work → v0.6**

- {Architecture question to resolve}

---

## v0.6 Architecture — Technical Blueprint

**System Overview**

- Architecture summary referencing TECHNICAL_ARCHITECTURE.md (ID: ARC-### if used).

**API Contracts (API-XXX)**

- API-### — {Endpoint purpose} (Method, Auth, Success / Error states)

**Data Model (DBT-XXX)**

- DBT-### — {Table / model} (Primary keys, relationships)

**Integration Notes**

- External dependencies, rate limits, compliance.

**Outstanding Work → v0.7**

- {Implementation open question}

---

## v0.7 Build Execution — Plan for Delivery

**EPIC Backlog Overview**
| EPIC | Objective | Lifecycle Impact | Status | Notes |
|------|-----------|------------------|--------|-------|
| EPIC-{XX} | {Outcome} | Advances to v0.{x+1} | 🚧 | {Summary}

**Testing Strategy Snapshot (TEST-XXX)**

- TEST-### — {Scope}
- TEST-### — {Scope}

**Definition of Done**

- [ ] All IDs created/modified logged in EPIC Section 2.
- [ ] README metrics updated via workflow.
- [ ] Coverage thresholds defined.

**Outstanding Work → v0.8**

- {Deployment or operational prep item}

---

## v0.8 Release & Deployment — Operational Readiness

**Release Checklist**

- [ ] Deployment environments configured (DEP-###).
- [ ] Monitoring & alerting baselined.
- [ ] Runbooks documented.

**Operational Policies**

- {Policy} → DEP-###

**Outstanding Work → v0.9**

- {GTM requirement}

---

## v0.9 Go-to-Market — Launch & Feedback

**Launch Plan Summary**

- Channels: {Email / Sales / Community}
- Messaging Pillars: {1-3 bullets}
- Launch Owner: {Name / Team}

**Analytics & Feedback Loop**

- Key Metrics: {Metric + target}
- Feedback Sources: {CFD-###, analytics dashboards}

**Outstanding Work → v1.0**

- {Adoption / revenue milestone}

---

## v1.0 Market Adoption — Optimize & Expand

**Adoption Status**

- Paying Customers: {# / MRR}
- Usage Health: {Metric + target}

**Optimization Backlog**

- {Idea / hypothesis} → EPIC-{YY}

**Future Bets & Loopbacks**

- {Potential revisits to earlier lifecycle stages}

---

## Appendices & References

- **Glossary**: {Terms and definitions}
- **ID Index**: Link to `SoT/SoT.UNIQUE_ID_SYSTEM.md` (Part 2: ID Registry).
- **Supporting Docs**: {Links to research, design, architecture}

> Maintain appendices as lightweight navigation helpers. All authoritative data must live in SoT files referenced above.
