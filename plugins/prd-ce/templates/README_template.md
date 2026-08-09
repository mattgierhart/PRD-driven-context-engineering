---
template_version: "3.3.0"
---

# {Product Name} — Product README

> **Status**: Discovery
> **Current PRD Version**: v0.1 (See `PRD.md`)
> **Active EPIC**: None (See `epics/`)

> **Read order:** `CLAUDE.md` → `README.md` → `PRD.md` → accepted `SoT/` → active EPIC (v0.7+ only).

---

<!-- SECTION: quick-navigation -->
## 1. Quick Navigation

| File                         | Purpose                                                                    |
| ---------------------------- | -------------------------------------------------------------------------- |
| **[`PRD.md`](PRD.md)**       | **Product Definition**. The product definition (Progressive PRD).          |
| **[`CLAUDE.md`](CLAUDE.md)** | **Agent Instructions**. The agent's operating instructions.                |
| **[`epics/`](epics/)**       | **Execution (v0.7+)**. Approved implementation context; none exists during v0.1–v0.6. |
<!-- /SECTION: quick-navigation -->

---

<!-- SECTION: core-principles -->
## 2. Core Principles (The 3+1 System)

1. **Navigation Files**: `README` + `PRD` + `CLAUDE` = The map.
2. **Progressive Work**: v0.1–v0.6 product-definition work lives in `PRD.md` + `SoT/`;
   implementation work moves into **EPICs** only at v0.7+.
3. **Specs**: All specs (rules, flows, APIs) live in `SoT/` with unique IDs.
   - `BR-XXX`: Business Rules
   - `UJ-XXX`: User Journeys
   - `API-XXX`: Contracts
   - `CFD-XXX`: Customer Feedback
4. **Gates**: We do not advance the PRD version without meeting the **Definition of Done** in [`PRD.md`](PRD.md).
<!-- /SECTION: core-principles -->

---

<!-- CUSTOMIZABLE: product-dashboard -->
## 3. Product Status Dashboard

**Lifecycle Stage**: `v0.1 Spark` (Target)

| Gate                          | Status         | Owner    | Blocker? |
| ----------------------------- | -------------- | -------- | -------- |
| **v0.1 Spark**                | 🟡 In Progress | Strategy | -        |
| **v0.2 Market Definition**    | ⚪ Pending     | -        | -        |
| **v0.3 Commercial Model**     | ⚪ Pending     | -        | -        |
| **v0.4 User Journeys**        | ⚪ Pending     | -        | -        |
| **v0.5 Red Team Review**      | ⚪ Pending     | -        | -        |
| **v0.6 Architecture**         | ⚪ Pending     | -        | -        |
| **v0.7 Build Execution**      | ⚪ Pending     | -        | -        |
| **v0.8 Release & Deployment** | ⚪ Pending     | -        | -        |
| **v0.9 Launch**               | ⚪ Pending     | -        | -        |
| **v1.0 Market Adoption**      | ⚪ Pending     | -        | -        |

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
<!-- /CUSTOMIZABLE: product-dashboard -->

---

## 5. Quick Commands

```bash
# Run Tests
npm test # or equivalent
```

---

## 6. Repository Guide

- **`epics/`**: The living implementation state from v0.7 onward; before then work is tracked in the current PRD gate and accepted SoT.
- **`SoT/`**: The Source of Truth (Requirements).
- **`temp/`**: Scratchpad work tied to the current PRD gate before v0.7, then to the active EPIC.
- **`.claude/`**: Consumer configuration and, for direct installs, the local agent runtime. In
  plugin-native mode, skills, hooks, agents, and scripts are supplied live by the plugin.

---

> **Agent Note**: `.claude/` can be replaced with `.gemini/`, `.codex/`, or any other agent structure, but the skills, hooks, custom commands, and agent model here were built with Anthropic's documentation model in mind.

> **Note**: This repository follows [PRD Led Context Engineering](https://github.com/mattgierhart/PRD-driven-context-engineering).
