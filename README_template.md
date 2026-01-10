# Gear Heart Methodology (GHM) — Command Center

> **Status**: Active
> **Current PRD Version**: v0.1 (See `PRD.md`)
> **Active EPIC**: None (See `epics/`)

---

## 1. Quick Navigation

| File                         | Purpose                                                                    |
| ---------------------------- | -------------------------------------------------------------------------- |
| **[`PRD.md`](PRD.md)**       | **Product Definition**. The single narrative of "What we are building".    |
| **[`CLAUDE.md`](CLAUDE.md)** | **AI Instructions**. How agents must behave in this repo.                  |
| **[`epics/`](epics/)**       | **Execution**. Where work happens. Check here for the current sprint/task. |

---

## 2. Core Principles (The 3+1 System)

1. **Navigation Files**: `README` + `PRD` + `CLAUDE` = The map.
2. **Active Work**: Happens in **EPICs**.
3. **Specs**: All specs (rules, flows, APIs) live in `SoT/` with unique IDs.
   - `BR-XXX`: Business Rules
   - `UJ-XXX`: User Journeys
   - `API-XXX`: Contracts
   - `CFD-XXX`: Customer Feedback
4. **Gates**: We do not advance the PRD version without meeting the **Definition of Done** (see [`README.md`](README.md)).

---

## 3. Product Status Dashboard

**Lifecycle Stage**: `v0.1 Spark` (Target)

| Gate                  | Status         | Owner    | Blocker? |
| --------------------- | -------------- | -------- | -------- |
| **v0.1 Spark**        | 🟡 In Progress | Strategy | -        |
| **v0.2 Market**       | ⚪ Pending     | -        | -        |
| **v0.3 Commercial**   | ⚪ Pending     | -        | -        |
| **v0.4 Journeys**     | ⚪ Pending     | -        | -        |
| **v0.5 Risks**        | ⚪ Pending     | -        | -        |
| **v0.6 Architecture** | ⚪ Pending     | -        | -        |
| **v0.7 Build**        | ⚪ Pending     | -        | -        |
| **v0.8 Release**      | ⚪ Pending     | -        | -        |
| **v0.9 Launch**       | ⚪ Pending     | -        | -        |
| **v1.0 Growth**       | ⚪ Pending     | -        | -        |

> _Update this table as you pass gates._

---

## 4. Product Roadmap

> **Focus**: Align development phases to clear outcomes.

### Deployment 1: Beta (Concept Validation)

- **Associated Epics**: `[Link to Epics]`
- **Key Specs**: `[UJ-xxx, BR-xxx]`

- [ ] **Core Functionality**: The essential value loop is working.
- [ ] **Context**: Uses scripted data or pre-provisioned accounts (not full self-serve).
- [ ] **Objective**: Validate the concept.

### Deployment 2: MVP (Pilot Readiness)

- **Associated Epics**: `[Link to Epics]`
- **Key Specs**: `[UJ-xxx, BR-xxx]`

- [ ] **Production Quality**: Stable, secure, and usable by real customers.
- [ ] **Marketing**: Direct sales/onboarding of pilots.
- [ ] **Objective**: Generate feedback ("What is broken?").

### Deployment 3: Releases (Feature Expansion)

- **Associated Epics**: `[Link to Epics]`
- **Key Specs**: `[UJ-xxx, BR-xxx]`

- [ ] **Feature Expansion**: Addressing gaps found in MVP pilot.
- [ ] **Marketing**: Active promotion.
- [ ] **Objective**: Grow user base.

### Deployment 4: V1.0 (Market Fit)

- **Associated Epics**: `[Link to Epics]`
- **Key Specs**: `[UJ-xxx, BR-xxx]`

- [ ] **Signal**: Customer adoption rate meets expectations.
- [ ] **Objective**: Optimization and Scale.

---

## 5. Quick Commands

```bash
# Generate Visual Reports (if tools installed)
python agents/tools/generate-visuals.py --all

# Run Tests
npm test # or equivalent
```

---

## 5. Repository Guide

- **`epics/`**: The living state of work (Issues/Tickets).
- **`SoT/`**: The Source of Truth (Requirements).
- **`agents/`**: AI Workforce & Tools.
- **`templates/`**: (Deprecated). Use `SoT/templates/` or copy `epics/EPIC_TEMPLATE.md`.
- **`archive/`**: where finished EPICs go to rest.

---

> **Note**: This repository is an implementation of the [Gear Heart Methodology](README.md).
