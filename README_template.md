# {Product Name} — Product README

<!-- SECTION: status-header -->
> **Status**: Active
> **Current PRD Version**: v0.1 (See `PRD.md`)
> **Active EPIC**: None (See `epics/`)
<!-- /SECTION: status-header -->

<!-- Metric Separation Principle:
  README is the human-authored view. status/metrics.json is the machine-writable source.
  Validation ensures agreement. Never auto-generate README content from JSON.

  Metric Deduplication Rule:
  Each metric value MUST appear in at most 2 locations: the Truth Table (authoritative)
  and the status header (quick reference). All other sections MUST reference the Truth
  Table rather than restating values. This prevents cascade drift where updating one
  location but missing another creates contradictions.
-->

---

## 1. Quick Navigation

| File                         | Purpose                                                                    |
| ---------------------------- | -------------------------------------------------------------------------- |
| **[`PRD.md`](PRD.md)**       | **Product Definition**. The product definition (Progressive PRD).          |
| **[`CLAUDE.md`](CLAUDE.md)** | **Agent Instructions**. The agent's operating instructions.                |
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

<!-- SECTION: status-dashboard -->
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
| **v1.0 Growth**               | ⚪ Pending     | -        | -        |

> _Update this table as you pass gates._
<!-- /SECTION: status-dashboard -->

---

<!-- SECTION: guardrails -->
## 4. Risk Scorecard

> Baseline established in v0.5 Red Team Review. Updated continuously as risks evolve.
> Details: `PRD.md` v0.5 | Template: `.claude/skills/prd-v05-risk-discovery-interview/assets/risk.md`

**Risk Level**: ⚪ Not Yet Assessed — Score: 0 | Updated: —

| Category | Risks | Open | Addressed | Score |
|----------|-------|------|-----------|-------|
| Market | — | — | — | — |
| User | — | — | — | — |
| Technical | — | — | — | — |
| **Total** | **—** | **—** | **—** | **—** |

<!-- Risk Scoring Reference:
  Categories:
    Market    = Market + Timing risks (will anyone buy this?)
    User      = Adoption + Dependency risks (will users succeed?)
    Technical = Technical + Resource risks (can we build & run this?)

  Severity:
    Impact:     High=3, Medium=2, Low=1
    Likelihood: High=3, Medium=2, Low=1
    Raw Score = Impact × Likelihood (1-9 per risk)

  Status Weights:
    open=1.0 | accepted=1.0 | mitigating=0.5 | mitigated=0.25 | resolved=0.0
    Effective Score = Raw × Status Weight

  Aggregation:
    Category Score = Σ effective scores for that category
    Total Score = Σ all category scores

  Risk Levels:
    🟢 Low (0-12) | 🟡 Moderate (13-25) | 🟠 Elevated (26-40) | 🔴 High (41+)

  Columns:
    Risks     = total RISK- entries in category
    Open      = status is 'open' or 'accepted'
    Addressed = status is 'mitigating', 'mitigated', or 'resolved'
    Score     = category score (sum of effective scores)

  Lifecycle:
    v0.5 establishes baseline. Any stage (v0.6-v1.0) can add new RISK- entries.
    Score updates whenever RISK- status changes.
-->
<!-- /SECTION: guardrails -->

---

<!-- SECTION: truth-table -->
<!-- Truth Table: Add project-specific metrics here at v0.7+ when metrics.json exists.
  This section is the AUTHORITATIVE location for metric values in README.
  The status-header may duplicate values for quick reference. No other section should.

  Example (uncomment and customize when entering Build phase):
  ## 4a. Truth Table
  | Metric | Value | Source |
  |--------|-------|--------|
  | Test Count | 0/0 | status/metrics.json |
  | Coverage (stmts) | 0% | status/metrics.json |
  | Risk Score | 0 | PRD.md v0.5 |
-->
<!-- /SECTION: truth-table -->

## 5. Product Roadmap

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

## 6. Quick Commands

```bash
# Run Tests
npm test # or equivalent
```

---

## 7. Repository Guide

- **`epics/`**: The living state of work (Issues/Tickets).
- **`SoT/`**: The Source of Truth (Requirements).
- **`temp/`**: Scratchpad work tied to active epics.
- **`.claude/`**: Agents, tools, skills, and hooks.

---

> **Agent Note**: `.claude/` can be replaced with `.gemini/`, `.codex/`, or any other agent structure, but the skills, hooks, custom commands, and agent model here were built with Anthropic's documentation model in mind.

> **Note**: This repository follows [PRD Led Context Engineering](https://github.com/mattgierhart/PRD-driven-context-engineering).
