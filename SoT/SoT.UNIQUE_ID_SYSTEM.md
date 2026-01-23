---
title: "Unique ID System"
updated: "2026-01-12"
authority: "PRD Led Context Engineering"
---

# Unique ID System

> **Rule**: Every durable concept gets an ID. IDs are stable. Names are not.

This file serves as the **governance guide** for the ID system and the **central registry** of all ID prefixes.

---

## Part 1: ID System Governance

### 1.1 ID Format

**Format**: `[PREFIX]-[NUMBER]` or `[PREFIX]-[NUMBER]-[SLUG]`

- **Prefix**: 2-4 letters (e.g., `BR`, `API`)
- **Number**: 3 digits, strictly incrementing (e.g., `001`, `002`)
- **Slug** (Optional): Short description (e.g., `api-001-user-login`)

**Example**: `BR-104`, `UJ-012`, `API-045`

### 1.2 Standard Prefixes

#### IDs in SoT Files

| Prefix | Meaning | SoT File | PRD Stage |
|--------|---------|----------|-----------|
| **CFD** | Customer Feedback | `SoT.customer_feedback.md` | v0.1 Spark |
| **PER** | Persona | `SoT.USER_JOURNEYS.md` | v0.4 User Journeys |
| **UJ** | User Journey | `SoT.USER_JOURNEYS.md` | v0.4 User Journeys |
| **SCR** | Screen Flow | `SoT.USER_JOURNEYS.md` | v0.4 User Journeys |
| **DES** | Design Component | `SoT.DESIGN_COMPONENTS.md` | v0.4 User Journeys |
| **TECH** | Tech Stack | `SoT.TECHNICAL_DECISIONS.md` | v0.5 Red Team |
| **ARC** | Architecture | `SoT.TECHNICAL_DECISIONS.md` | v0.6 Architecture |
| **ENV** | Environment Setup | `SoT.TECHNICAL_DECISIONS.md` | v0.6 Architecture |
| **INT** | Integration | `SoT.INTEGRATIONS.md` | v0.6 Architecture |
| **API** | API Contract | `SoT.API_CONTRACTS.md` | v0.6 Architecture |
| **DBT** | Data Schema | `SoT.DATA_MODEL.md` | v0.6 Architecture |
| **BR** | Business Rule | `SoT.BUSINESS_RULES.md` | v0.6 Architecture |
| **TEST** | Test Case | `SoT.TESTING.md` | v0.7 Build |
| **DEP** | Deployment | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **MON** | Monitoring | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **RUN** | Runbook | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **SEC** | Secret/Credential | `SoT.DEPLOYMENT.md` | v0.7 Build |

#### IDs in PRD/README (Not SoT Files)

| Prefix | Meaning | Location | PRD Stage |
|--------|---------|----------|-----------|
| **KPI** | Key Metric | `README.md` | v0.3 Commercial |
| **FEA** | Feature | `PRD.md` Section 3 | v0.3 Commercial |
| **RISK** | Risk | `PRD.md` v0.5 Section | v0.5 Red Team |
| **GTM** | Go-to-Market | `PRD.md` v0.9 Section | v0.9 Launch |
| **EPIC** | Work Package | `epics/` folder | v0.7 Build |

#### Compound IDs

| Pattern | Meaning | Example |
|---------|---------|---------|
| **BR-FEA** | Feature governance | `BR-FEA-001` |
| **BR-API** | API validation | `BR-API-045` |

### 1.3 How to Assign IDs

1. **Check**: Look at the SoT file for the highest used number
2. **Increment**: Add 1
3. **Log**: Write the new entry in the SoT file
4. **Use**: Reference as `[PREFIX-XXX]` in code, PRDs, EPICs

> **Note**: Never re-use an ID. Deprecate instead.

### 1.4 Common Patterns (The Graph)

#### A. API Implements Rule

```text
BR-001 (User Limit)
  └─→ API-045 (POST /users validation)
      └─→ TEST-301 (Unit test)
```

#### B. User Journey Dependencies

```text
UJ-101 (Onboarding Flow)
  ├─→ API-045 (Create User)
  ├─→ DES-042 (Sign Up Component)
  └─→ BR-001 (Limit Check)
```

#### C. Feedback Drives Features

```text
CFD-089 (Request: Dark Mode)
  └─→ FEA-015 in PRD (Theme Feature)
      └─→ UJ-105 (Theme Switcher Flow)
```

---

## Part 2: SoT File Registry

| SoT File | ID Prefixes | Lines | Purpose |
|----------|-------------|-------|---------|
| `SoT.BUSINESS_RULES.md` | BR-XXX | ~120 | Business constraints |
| `SoT.USER_JOURNEYS.md` | UJ, PER, SCR | ~150 | User flows, personas, screens |
| `SoT.API_CONTRACTS.md` | API-XXX | ~120 | Endpoint specifications |
| `SoT.DATA_MODEL.md` | DBT-XXX | ~120 | Database schema |
| `SoT.TESTING.md` | TEST-XXX | ~120 | Test specifications |
| `SoT.DEPLOYMENT.md` | DEP, RUN, MON, SEC | ~320 | Operations, deployment & secrets |
| `SoT.customer_feedback.md` | CFD-XXX | ~120 | Customer insights |
| `SoT.DESIGN_COMPONENTS.md` | DES-XXX | ~100 | UI components |
| `SoT.TECHNICAL_DECISIONS.md` | TECH, ARC, ENV | ~130 | Tech, architecture & environment |
| `SoT.INTEGRATIONS.md` | INT-XXX | ~105 | Third-party services |

---

## Part 3: Validation

When forking, validate:

- **Orphaned IDs**: IDs defined but never referenced
- **Dangling References**: IDs referenced but not defined
- **Broken Links**: Cross-references pointing to non-existent IDs

---

## Change Log

| Date | Change |
|------|--------|
| 2026-01-23 | Added SEC-XXX prefix for secrets/credentials inventory |
| 2026-01-18 | Added ENV-XXX prefix for development environment specifications |
| 2026-01-12 | Standardized: Updated file references, added INT-XXX, clarified PRD vs SoT homes |
| 2026-01-12 | Added 8 missing ID prefixes. Organized by PRD stage |
| 2025-12-22 | Combined UNIQUE_ID_SYSTEM and ID_REGISTRY into one |
