---
template: "product-readme"
ghm_stack: "Command Center"
last_updated: 2025-02-14
---

# {Product Name}

> **Command Center & Navigation Hub** — always load this file first.
> Tracks status, PRD lifecycle, and the active ID surface for AI + human collaborators.

---

## 📊 Operating Snapshot (Auto-Sync)

| Metric | Current Value | Target | Last Updated | Trend |
|--------|---------------|--------|--------------|-------|
| **Lifecycle Gate** | v0.x | v1.0 | YYYY-MM-DD | → |
| **Active EPIC** | EPIC-{XX} | — | YYYY-MM-DD | → |
| **Product Status** | 🟡 Discovery / 🚧 Build / 🚀 Live | 🚀 Live | YYYY-MM-DD | → |
| **Risk Index** | {0-100,000} | <10,000 | YYYY-MM-DD | ↓/→/↑ |
| **Test Coverage (Lines)** | XX.XX% | ≥80% | YYYY-MM-DD | ↑ |
| **Build Status** | ✅ Passing / 🔴 Failing | Passing | YYYY-MM-DD | → |
| **Open Blockers** | {Count} | 0 | YYYY-MM-DD | ↓ |
| **Deploy Target** | {Environment} | Production | YYYY-MM-DD | → |

**Data Source**: `status/metrics.json` (generated workflow). Do not edit manually.

**Freshness Rules**
- ⚠️ If "Last Updated" > 7 days → rerun validation before taking action.
- 🔴 If "Last Updated" > 14 days → treat all metrics as stale.

---

## 🎯 Mandatory Onboarding Checklist

**Context**: {Product Name} – {One-line product description}

**Tech Stack**: {Framework / Language / Infrastructure}

**Active EPIC**: [EPIC-{XX}](epics/EPIC-{XX}-{slug}.md) – {Brief description}

**Load Order (3+1 stack)**
1. ✅ `README.md` — operational picture & navigation (you are here).
2. 📘 [`PRD.md`](PRD.md) — strategic requirements by lifecycle stage.
3. 🤖 [`CLAUDE.md`](CLAUDE.md) — behavior rules for build agents.
4. 🧭 Active EPIC (`epics/EPIC-{XX}-{slug}.md`) — execution window.

**Before you code**
- [ ] Confirm Risk Index <10,000.
- [ ] Confirm coverage ≥ target for your scope.
- [ ] Review blocker list and owners.
- [ ] Skim lifecycle summary below to know current gate.
- [ ] Note IDs flagged for change in "Active IDs".

---

## 🚧 Current Work Surface

### EPIC-{XX}: {Feature / Outcome}
- **Lifecycle Focus**: Advances PRD → v0.{x+1}
- **Status**: 🚧 In Progress (Phase {Plan / Build / Verify / Hand-off})
- **Start Date**: YYYY-MM-DD
- **Target Ship**: YYYY-MM-DD
- **GitHub Issues**: #{issue-1}, #{issue-2}

#### Next 3 Actions
1. {Action tied to issue}
2. {Action tied to issue}
3. {Action tied to issue}

#### Known Blockers
- {Blocker description} (Owner: {Name}, Due: YYYY-MM-DD)
- *None*

### 🔎 Active IDs in Scope

**Modified This EPIC**
- [UJ-101](USER_JOURNEYS.md#uj-101) – {Journey name}
- [API-045](API_CONTRACTS.md#api-045) – {Endpoint}

**Created This EPIC**
- [CFD-204](customer_feedback.md#cfd-204) – {Insight}
- [TEST-303](testing_playbook.md#test-303) – {Test case}

**Referenced (No Change)**
- [BR-112](BUSINESS_RULES.md#br-112) – {Rule}
- [DBT-018](ACTUAL_SCHEMA.md#dbt-018) – {Table}

> **Summary**: {X} modified · {Y} created · {Z} referenced IDs.
> For full traceability see [EPIC-{XX} → Section 3A](epics/EPIC-{XX}-{slug}.md#3a-id-tracking).

---

## 🌀 PRD Version Lifecycle Progress

| Stage | Status | Summary | Next Trigger |
|-------|--------|---------|--------------|
| **v0.1 Spark** | ✅ / 🚧 | Problem, outcomes, constraints | Market clarity sign-off |
| **v0.2 Market Definition** | ✅ / 🚧 | Segments & ICP defined | Commercial hypotheses ready |
| **v0.3 Commercial Model** | ✅ / 🚧 | Pricing & positioning | Competitive sanity review |
| **v0.4 User Journeys** | ✅ / 🚧 | Core journeys w/ pains | Risk review completed |
| **v0.5 Red Team Review** | ✅ / 🚧 | Risks + mitigations | Architecture drafted |
| **v0.6 Architecture** | ✅ / 🚧 | Stack, schema, contracts | Build plan staffed |
| **v0.7 Build Execution** | ✅ / 🚧 | EPIC backlog + QA plan | Release checklists |
| **v0.8 Deployment & Ops** | ✅ / 🚧 | Release criteria met | GTM activation |
| **v0.9 Go-to-Market** | ✅ / 🚧 | Launch + analytics | Adoption milestones |
| **v1.0 Market Adoption** | ✅ / 🚧 | Paying customers & optimization | Post-v1 roadmap |

**Latest Change Notes**: {Short bullet summary referencing IDs}

---

## 📚 Navigation Cheatsheet (3 + 1 + SoT + Temp)

### Navigation Layer
- **`README.md`** — this Command Center.
- **`PRD.md`** — lifecycle narrative (reference IDs).
- **`CLAUDE.md`** — operating rules for agents.

### +1 Active EPIC
- `epics/EPIC-{XX}-{slug}.md` — window of work, includes Section 3A for ID deltas.

### Source of Truth Library
- `USER_JOURNEYS.md` (UJ-XXX)
- `BUSINESS_RULES.md` (BR-XXX)
- `customer_feedback.md` (CFD-XXX)
- `API_CONTRACTS.md` (API-XXX)
- `ACTUAL_SCHEMA.md` (DBT-XXX)
- `testing_playbook.md` (TEST-XXX)
- `deployment_playbook.md` (DEP-XXX)
- Additional SoT files as needed, all ID-scoped.

### Temp & Archive Protocol
- Drop scratchpads into `temp/` with owner + expiry.
- Harvest into SoT before completing Phase E.
- Move finalized artifacts to `archive/YYYY-MM/` with PRD references updated.

---

## 🧭 Repo Map (Customize for your product)

```
/                     # Product root
├── README.md         # Command Center (this file)
├── PRD.md            # Versioned strategy
├── CLAUDE.md         # Agent behavior
├── epics/            # Active + archived EPICs
├── source_of_truth/  # Optional folder for split SoT files
├── src/              # Application code
├── tests/            # Automated coverage
├── temp/             # Short-lived scratchpads (purge or harvest)
└── archive/          # Frozen history (by YYYY-MM)
```

Adjust to reflect actual layout. Ensure README links remain accurate after edits.

---

## 🧪 Quick Commands (Adapt per stack)

```bash
# Install & bootstrap
yarn install

# Run local dev
yarn dev

# Run test suites
yarn test

yarn test:coverage

# Lint & format
yarn lint
yarn format

# Update metrics & registry
yarn workflow:verify   # refresh metrics.json & ID registry
```

---

## 🚨 Critical Alerts
- {Alert + owner + due date}
- *None currently*

---

## 🧮 Risk Breakdown (If using Risk Index)

| Category | Points | Notes |
|----------|--------|-------|
| Coverage Gaps | {points} | {context} |
| Documentation | {points} | {context} |
| Tech Debt | {points} | {context} |
| Security | {points} | {context} |
| Operations | {points} | {context} |

Mitigation plan documented in [EPIC-{XX}](epics/EPIC-{XX}-{slug}.md).

---

## 🗓 Version History Summary

| PRD Version | Date | Milestone | Notes |
|-------------|------|-----------|-------|
| v0.1 Spark | YYYY-MM-DD | Problem + outcomes agreed | Spark snapshot linked |
| v0.2 Market Definition | YYYY-MM-DD | Segments locked | ID refs: CFD-### |
| v0.3 Commercial Model | YYYY-MM-DD | Pricing hypotheses | ID refs: BR-### |
| v0.4 User Journeys | YYYY-MM-DD | Journeys authored | ID refs: UJ-### |
| v0.5 Red Team Review | YYYY-MM-DD | Risks cataloged | ID refs: BR-/TEST-### |
| v0.6 Architecture | YYYY-MM-DD | Architecture baseline | ID refs: API-/DBT-### |
| v0.7 Build Execution | YYYY-MM-DD | Backlog + QA strategy | EPIC hand-off |
| v0.8 Deployment & Ops | YYYY-MM-DD | Release readiness | DEP-### |
| v0.9 Go-to-Market | YYYY-MM-DD | Launch plan active | GTM docs |
| v1.0 Market Adoption | YYYY-MM-DD | Paying customers | Growth roadmap |

---

*Last updated*: YYYY-MM-DD HH:MM TZ  
*Maintainer*: {Name / Team}

