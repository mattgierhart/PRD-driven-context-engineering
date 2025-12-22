---
title: "Lifecycle & Operations Guide"
version: 2.0
updated: "2025-12-22"
authority: "Gear Heart Methodology"
---

# Lifecycle & Operations Guide

> **Purpose**: The single source of truth for the PRD Version Lifecycle (v0.1 → v1.0), Repository Structure, and Operational Workflows.

---

## 1. The 3+1+SoT+Temp Framework

This methodology organizes documentation into four distinct layers to maintain context for both Humans and AI.

| Layer     | Component          | Purpose                                                                                                                                 |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **3**     | **Navigation**     | `README.md` (Status/Ops), `PRD.md` (Product Definition), `CLAUDE.md` (AI Instructions).                                                 |
| **+1**    | **Active Context** | The **Active EPIC** file (e.g., `epics/EPIC-01-setup.md`). Tracks current execution state.                                              |
| **Specs** | **Specification**  | Durable, ID-based specs in `specs/` (e.g., `BUSINESS_RULES.md`). <br>**Rule**: Never duplicate specs. PRD and EPICs must reference IDs. |
| **Temp**  | **Scratchpad**     | Temporary files in `temp/` for analysis. Must be harvested into SoT and archived/deleted before closing an EPIC.                        |

---

## 2. Repository Layout

```text
/
├── README.md              # Command Center — status & navigation
├── ROADMAP.md             # Release Phasing (MVP -> Beta -> V1)
├── PRD.md                 # Product Definitions (Phased v0.1 → v1.0)
├── CLAUDE.md              # AI Agent Instructions
├── epics/                 # Active Work (The "Sprint")
├── specs/                 # Source of Truth (The "Rules")
├── agents/                # AI Workforce (Tools & Configs)
├── archive/               # Completed EPICs and captured temp files
├── temp/                  # Working scratchpads (transient)
├── templates/             # Canonical templates for cloning
└── methodology/           # This guide and other reference docs
```

---

## 3. PRD Version Lifecycle (v0.1 → v1.0)

Work progresses through strict gates. You cannot advance to the next version until the **Definition of Done (DoD)** is met.

### **v0.1 Spark** (Problem & Outcomes)

**Focus**: framing the problem, desired outcomes, and basic constraints.

- **DoD Checklist**:
  - [ ] Problem statement references at least one `CFD-` (Customer/Market) insight.
  - [ ] Desired outcomes include measurable success signals.
  - [ ] Open question list prepared for v0.2.

### **v0.2 Market Definition** (Segments & ICP)

**Focus**: Validating who this is for (and who it is NOT for).

- **DoD Checklist**:
  - [ ] Segment table complete (size, urgency, source `CFD-` ID).
  - [ ] "Not for" segment defined with rationale.
  - [ ] `BR-` IDs created for gating business rules (e.g., "Must be US-based").

### **v0.3 Commercial Model** (Value & Pricing)

**Focus**: How it makes money and fits in the market.

- **DoD Checklist**:
  - [ ] Anchor competitors profiled (with pricing `CFD-` references).
  - [ ] Monetization model documented.
  - [ ] Pricing hypotheses mapped to `BR-` rules.

### **v0.4 User Journeys** (Personas & Flows)

**Focus**: Mapping commercial value to user actions.

- **DoD Checklist**:
  - [ ] 3–7 core journeys mapped (Persona + Trigger + Steps + Value).
  - [ ] `UJ-` IDs created for each journey.
  - [ ] Dependencies (`BR-`/`API-`) noted for v0.6.

### **v0.5 Red Team Review** (Risks & Feasibility)

**Focus**: "Murder Board" — why will this fail?

- **DoD Checklist**:
  - [ ] Risk table covers Market, Product, Tech, and Ops risks.
  - [ ] Mitigation strategies tied to `TEST-` or `BR-` IDs.
  - [ ] **Gate Decision**: Go / Pivot / Kill recorded in PRD.

### **v0.6 Architecture** (Technical Strategy)

**Focus**: Stack selection, data model, and API contracts.

- **DoD Checklist**:
  - [ ] Architecture Diagram/Summary completed.
  - [ ] `API-` contracts and `DBT-` schemas drafted for core flows.
  - [ ] Cost guardrails established.

### **v0.7 Build Execution** (EPIC Loop)

**Focus**: Iterative implementation via EPICs. This phase repeats until feature complete.

- **DoD Checklist (Per EPIC)**:
  - [ ] Phases A–E of EPIC workflow complete.
  - [ ] All code tested (`TEST-` coverage requirements met).
  - [ ] SoT files updated (`API-`, `DBT-`, `UJ-`, `BR-` are current).
  - [ ] README metrics refreshed.

### **v0.8 Deployment & Ops** (Release Readiness)

**Focus**: Production safety, runbooks, and monitoring.

- **DoD Checklist**:
  - [ ] Deployment playbooks (`DEP-`) and Runbooks (`RUN-`) created.
  - [ ] Monitoring (`MON-`) and Alerting configured.
  - [ ] Rollback plan validated.

### **v0.9 Go-to-Market** (Launch)

**Focus**: Marketing, analytics, and feedback loops.

- **DoD Checklist**:
  - [ ] Launch metrics instrumented (`KPI-` / `ANL-`).
  - [ ] Feedback channels (`CFD-`) defined and active.
  - [ ] Launch plan executing.

### **v1.0 Market Adoption** (Optimization)

**Focus**: Real usage, retention, and enhancements.

- **DoD Checklist**:
  - [ ] Paying customer data flowing.
  - [ ] Retention analysis showing fit.
  - [ ] PRD marked v1.0; future work moves to Optimization/Scale EPICs.

---

## 4. EPIC Execution Workflow (The "How")

All work in **v0.7+** (and often earlier) happens inside **EPICs**.

| Phase           | Description                                          | Key Artifacts                                   |
| --------------- | ---------------------------------------------------- | ----------------------------------------------- |
| **A. Plan**     | Load Context, Scope Work, List IDs.                  | `EPIC-XX.md` created, Section 2 & 3A populated. |
| **B. Design**   | Solution Design, Interface Definitions.              | Design docs, `API-`/`DBT-` updates draft.       |
| **C. Build**    | Code & Test Implementation.                          | Code commits, `TEST-` IDs active.               |
| **D. Validate** | QA, Verification, Bug Fixes.                         | Test results, Green build.                      |
| **E. Finish**   | **Documentation Harvest**. Update SoT, Archive Temp. | SoT files updated, Temp files archived.         |

**Session Protocols**:

- **Start**: Read `README` (Status) → `EPIC` (Section 0: Session State) → `PRD` (Requirements).
- **End**: Update `EPIC` Section 0 (Session State) with concise "Where I left off" and "Next Steps".

---

## 5. Governance Rules

1. **ID First**: If it's important, it needs an ID (Rule -> `BR-001`, Journey -> `UJ-010`).
2. **No Orphaned Docs**: Every file must be linked from README, PRD, or an Active EPIC.
3. **Temp is Temporary**: Never leave files in `temp/` after an EPIC closes.
4. **Gates are Hard**: Do not proceed to the next PRD version without satisfying the DoD.
