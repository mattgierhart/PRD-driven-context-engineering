# {Product Name}

> **Single Source of Truth Dashboard** - AI Agent Onboarding & Operational Command Center
>
> **⚠️ MANDATORY**: All AI agents MUST read this file FIRST before any work

---

## 📊 Today's Truth Table

> **Purpose**: Absolute authority for all metrics. Updated automatically from test runs and validation scripts.

| Metric | Current Value | Target | Last Updated | Trend |
|--------|--------------|--------|--------------|-------|
| **Product Status** | {🟡 Development / 🚀 Production} | Production | YYYY-MM-DD HH:MM TZ | - |
| **PRD Version** | v0.x | v1.0 | YYYY-MM-DD | → |
| **Risk Score** | {0-100,000} | <10,000 | YYYY-MM-DD | ↓/→/↑ |
| **Test Coverage (Overall)** | XX.XX% | ≥80% | YYYY-MM-DD HH:MM | ↑ |
| **Test Coverage (Statements)** | XX.XX% | ≥80% | YYYY-MM-DD HH:MM | ↑ |
| **Test Coverage (Branches)** | XX.XX% | ≥75% | YYYY-MM-DD HH:MM | ↑ |
| **Test Coverage (Functions)** | XX.XX% | ≥85% | YYYY-MM-DD HH:MM | ↑ |
| **Test Coverage (Lines)** | XX.XX% | ≥80% | YYYY-MM-DD HH:MM | ↑ |
| **Tests Passing** | XXX / XXX | 100% | YYYY-MM-DD HH:MM | ✅ |
| **Test Suites Active** | XX of XX | All | YYYY-MM-DD HH:MM | → |
| **Build Status** | ✅ Passing / 🔴 Failing | Passing | YYYY-MM-DD HH:MM | ✅ |
| **Deployment Status** | {Environment} | Production | YYYY-MM-DD HH:MM | - |
| **Active Blockers** | {Count} | 0 | YYYY-MM-DD | - |

**Data Source**: `status/metrics.json` (auto-generated, never manually edit Truth Table)

**Metrics Freshness Warning**:
- ⚠️ If "Last Updated" >7 days: Re-run verification before relying on these numbers
- 🔴 If "Last Updated" >14 days: Metrics considered stale, mandatory refresh required

---

## 🎯 AI Agent Onboarding (MUST READ FIRST)

**You are working on**: {Product Name} - {One-line product description}

**Tech Stack**: {Framework} + {Language} + {Database} + {Hosting}

**Current EPIC**: [EPIC-{XX}](epics/EPIC-{XX}-{name}.md) - {Brief description}

**Loading Order** (MANDATORY):
1. ✅ This file (README.md) → Operational dashboard
2. → [PRD.md](PRD.md) → Business requirements
3. → [Current EPIC](epics/EPIC-{XX}-{name}.md) → Today's execution
4. → SoT files (as needed per phase)

**Before You Code**:
- [ ] Verify Risk Score <10,000 (see Truth Table above)
- [ ] Verify Test Coverage ≥80% (see Truth Table above)
- [ ] Verify Build Status ✅ Passing (see Truth Table above)
- [ ] Check Active Blockers (see Truth Table above)
- [ ] Identify which EPIC phase you're in (see Current Work below)

---

## 🚧 Current Work

### Active EPIC: EPIC-{XX} - {Feature Name}

**Status**: 🚧 In Progress (Phase {A-E})
**Started**: YYYY-MM-DD
**PRD Version**: v0.x
**GitHub Issues**: #{issue1}, #{issue2}, #{issue3}

**Current Phase**: {A - Planning / B - Design / C - Implementation / D - Testing / E - Documentation}

**Next Actions**:
1. {Specific next task from EPIC}
2. {Specific next task from EPIC}
3. {Specific next task from EPIC}

**Known Blockers**:
- {Blocker description} (Owner: {Name}, Due: YYYY-MM-DD)
- *None currently*

### 📍 Active IDs in Scope

> **Quick Navigation**: Jump directly to specifications by clicking ID links

**Modified This EPIC**:
- [UJ-101](USER-JOURNEYS.md#uj-101) - {Journey name} (improving)
- [API-045](API_CONTRACTS.md#api-045) - {Endpoint name} (modified ✅)
- [TEST-301](testing-playbook.md#test-301) - {Test name} (updated)

**Created This EPIC**:
- [API-046](API_CONTRACTS.md#api-046) - {Endpoint name} (created 🆕)
- [TEST-303](testing-playbook.md#test-303) - {Test name} (created 🆕)

**Referenced (No Change)**:
- [BR-112](BUSINESS_RULES.md#br-112) - {Rule name}
- [DBT-018](ACTUAL-SCHEMA.md#dbt-018) - {Table name}

**Summary**: Modified {X} IDs | Created {Y} IDs | Total scope: {Z} IDs

For complete impact map and dependency chain, see [EPIC-{XX}](epics/EPIC-{XX}-{name}.md#id-tracking)

### Phase-Specific SoT Files

**Phase A (Planning)**: PRD.md, BUSINESS_RULES.md, USER-JOURNEYS.md
**Phase B (Design)**: user-journeys/*.md, design-brief.md, USER-JOURNEYS.md
**Phase C (Implementation)**: TECHNICAL-ARCHITECTURE.md, API_CONTRACTS.md, ACTUAL-SCHEMA.md
**Phase D (Testing)**: testing-playbook.md, coverage reports
**Phase E (Documentation)**: deployment-playbook.md, all SoT updates

---

## 📂 Project Navigation

### Core Documentation (The "3" - Navigation Layer)
- **[Claude.md](Claude.md)** - Process rules and workflow (points to SoT files)
- **[PRD.md](PRD.md)** - Product requirements (v0.x) (provides context, references IDs)
- **This file (README.md)** - Operational dashboard (shows active IDs, navigation hub)

### Source of Truth (SoT) Files - ID Reference Library

**User & Business Layer**:
- **[USER-JOURNEYS.md](USER-JOURNEYS.md)** - Complete user flows (UJ-XXX)
- **[BUSINESS_RULES.md](BUSINESS_RULES.md)** - Business constraints (BR-XXX)
- **[customer-feedback.md](customer-feedback.md)** - User feedback items (CFD-XXX)

**Technical Layer**:
- **[API_CONTRACTS.md](API_CONTRACTS.md)** - API endpoint specifications (API-XXX)
- **[ACTUAL-SCHEMA.md](ACTUAL-SCHEMA.md)** - Database schema (DBT-XXX)
- **[TECHNICAL-ARCHITECTURE.md](TECHNICAL-ARCHITECTURE.md)** - System design and decisions

**Quality & Operations Layer**:
- **[testing-playbook.md](testing-playbook.md)** - Test cases and strategy (TEST-XXX)
- **[deployment-playbook.md](deployment-playbook.md)** - Infrastructure (DEP-XXX)
- **[{product}-DesignBrief.md]({product}-DesignBrief.md)** - Design components (DES-XXX)

**ID Registry** (Auto-Generated):
- **[.codex/ID-REGISTRY.md](.codex/ID-REGISTRY.md)** - Complete ID index (regenerate with `npm run codex:sync-registry`)

### Active Work
- **[epics/](epics/)** - All EPIC files (current + archived)
- **[Current EPIC](epics/EPIC-{XX}-{name}.md)** - Today's work focus

### Research & Design
- **[research/](research/)** - Market research and competitive analysis
- **[user-journeys/](user-journeys/)** - User personas and journey maps
- **[design-brief.md](design-brief.md)** - Design specifications

### Code & Tests
- **[src/](src/)** - Source code
- **[tests/](tests/)** - Test suites
- **[coverage/](coverage/)** - Test coverage reports

### Temporary & Archive
- **[temp/](temp/)** - Temporary working files (extract to SoT, then archive)
- **[archive/](archive/)** - Historical files organized by YYYY-MM/

---

## 🎓 EPIC Learning Repository

> **Purpose**: Accumulated wisdom from completed EPICs. Consult before starting similar work.

### EPIC-00: Foundation Setup (✅ Completed YYYY-MM-DD)
**Key Learnings**:
- {Learning 1}
- {Learning 2}
- {Learning 3}

**What Worked Well**:
- {Success pattern}

**What to Avoid**:
- {Anti-pattern}

**Archive**: [archive/YYYY-MM/EPIC-00.md](archive/YYYY-MM/)

### EPIC-01: {Feature Name} (✅ Completed YYYY-MM-DD)
**Key Learnings**:
- {Learning 1}
- {Learning 2}

**Archive**: [archive/YYYY-MM/EPIC-01.md](archive/YYYY-MM/)

---

## 🔧 Quick Commands

```bash
# Development
npm install          # Install dependencies
npm run dev          # Start dev server
npm run build        # Build for production
npm run lint         # Run linter
npm run format       # Format code

# Testing
npm test             # Run all tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Generate coverage report

# Deployment
npm run deploy:test  # Deploy to staging
npm run deploy:prod  # Deploy to production

# Validation
npm run verify       # Run full validation suite
npm run metrics      # Update metrics.json
```

---

## ⚠️ Critical Alerts

> **Purpose**: Time-sensitive issues requiring immediate attention

- {Current critical alert if any}
- *None currently*

---

## 📊 Risk Score Breakdown

**Current Risk Score**: {0-100,000} (Last Calculated: YYYY-MM-DD)

| Risk Category | Points | Notes |
|--------------|--------|-------|
| Test Coverage Gap | {points} | {calculation details} |
| Missing Documentation | {points} | {what's missing} |
| Tech Debt | {points} | {debt items} |
| Security Concerns | {points} | {concerns} |
| Performance Issues | {points} | {issues} |

**Mitigation Plan**: See [Current EPIC](epics/EPIC-{XX}-{name}.md) Phase D

---

## 🔗 External Resources

- **Production URL**: {https://...}
- **Staging URL**: {https://...}
- **Design System**: {https://...}
- **API Docs**: {https://...}
- **Monitoring Dashboard**: {https://...}
- **CI/CD Pipeline**: {https://...}

---

## 📜 Version History

| PRD Version | Date Achieved | Key Milestone | EPIC Completed |
|-------------|--------------|---------------|----------------|
| v0.1 | YYYY-MM-DD | Research Spark | - |
| v0.2 | YYYY-MM-DD | Market Research | - |
| v0.3 | YYYY-MM-DD | Competitive Analysis | - |
| v0.4 | YYYY-MM-DD | User Journeys | - |
| v0.5 | YYYY-MM-DD | Gate 1 (Market Validation) | - |
| v0.6 | YYYY-MM-DD | Gate 2 (Technical Feasibility) | EPIC-00 |
| v0.7 | - | Feature Development | EPIC-01+ |

---

*Last README Update*: YYYY-MM-DD HH:MM TZ
*README Maintained By*: {Team/Person}
*README Target Size*: 250-300 lines (current: {count})
