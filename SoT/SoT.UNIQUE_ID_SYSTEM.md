---
title: "Unique ID System"
updated: "2025-12-22"
authority: "Gear Heart Methodology"
---

# Unique ID System

> **Rule**: Every durable concept gets an ID. IDs are stable. Names are not.

This file serves as both the **governance guide** for the ID system and the **central registry** of all IDs in the knowledge graph.

---

## Part 1: ID System Governance

### 1.1 ID Format

**Format**: `[PREFIX]-[NUMBER]-[SLUG]`

- **Prefix**: 3-4 letters (e.g., `BR`, `API`).
- **Number**: 3 digits, strictly incrementing (e.g., `001`, `002`).
- **Slug** (Optional): Short description (e.g., `api-001-user-login`).

**Example**: `BR-104`, `UJ-012`, `API-800`

### 1.2 Standard Prefixes

| Prefix   | Meaning           | Spec File (SoT/)             |
| -------- | ----------------- | ---------------------------- |
| **BR**   | Business Rule     | `SoT.BUSINESS_RULES.md`      |
| **UJ**   | User Journey      | `SoT.USER_JOURNEYS.md`       |
| **API**  | API Contract      | `SoT.API_CONTRACTS.md`       |
| **DBT**  | Data Schema       | `SoT.ACTUAL_SCHEMA.md`       |
| **CFD**  | Customer Feedback | `SoT.customer_feedback.md`   |
| **DES**  | Design Component  | `SoT.DESIGN_BRIEF.md`        |
| **TEST** | Test Case         | `SoT.testing_playbook.md`    |
| **DEP**  | Deployment Step   | `SoT.deployment_playbook.md` |
| **GTM**  | Go-to-Market      | `SoT.deployment_playbook.md` |
| **RUN**  | Runbook           | `SoT.deployment_playbook.md` |
| **MON**  | Monitoring        | `SoT.deployment_playbook.md` |
| **KPI**  | Key Metric        | `README.md`                  |

### 1.3 How to Assign IDs

1. **Check the Ledger**: Look at the `SoT/` file for the highest used number.
2. **Increment**: Add 1.
3. **Log it**: Write the new entry in the SoT (`SoT/`) file.
4. **Use it**: Reference it in code, PRDs, and EPICs as `[PREFIX-XXX]`.

> **Note**: Never re-use an ID even if the feature is deleted. Deprecate it instead.

### 1.4 Common Patterns (The Graph)

#### A. API Implements Rule

> "Code enforces Business Logic"

```text
BR-001 (User Limit)
  └─→ API-045 (POST /users validation)
      └─→ TEST-301 (Unit test for API-045)
```

#### B. User Journey Dependencies

> "UX Flow requires Backend + Design"

```text
UJ-101 (Onboarding Flow)
  ├─→ API-045 (Create User)
  ├─→ DES-042 (Sign Up Mockup)
  └─→ BR-001 (Limit Check)
```

#### C. Feedback Drives Features

> "User Request becomes Feature"

```text
CFD-089 (Request: Dark Mode)
  └─→ UJ-105 (Theme Switcher Flow)
      ├─→ DBT-025 (User Preferences Table)
      └─→ TEST-310 (Visual Regression)
```

---

## Part 2: ID Registry

> **Update Method**: Maintain manually unless you add tooling in a fork.
> **Note**: Tables below are templates. Populate when forking for your product.

### 2.1 Quick Stats

| ID Type  | Count   | SoT File                   | Status     |
| -------- | ------- | -------------------------- | ---------- |
| UJ-XXX   | {count} | SoT.USER_JOURNEYS.md       | ✅ Active  |
| BR-XXX   | {count} | SoT.BUSINESS_RULES.md      | ✅ Active  |
| API-XXX  | {count} | SoT.API_CONTRACTS.md       | ✅ Active  |
| DBT-XXX  | {count} | SoT.ACTUAL_SCHEMA.md       | ✅ Active  |
| CFD-XXX  | {count} | SoT.customer_feedback.md   | ✅ Active  |
| DES-XXX  | {count} | SoT.DESIGN_BRIEF.md        | ✅ Active  |
| TEST-XXX | {count} | SoT.testing_playbook.md    | ✅ Active  |
| DEP-XXX  | {count} | SoT.deployment_playbook.md | ✅ Active  |

**Last Sync**: {timestamp}
**Total IDs**: {total_count}

### 2.2 ID Index Tables

#### User Journeys (UJ-XXX)

| ID     | Title           | Status | Used By         |
| ------ | --------------- | ------ | --------------- |
| UJ-001 | {Journey Title} | Active | API-XXX, BR-XXX |

#### Business Rules (BR-XXX)

| ID     | Rule Name    | Severity | Enforced By |
| ------ | ------------ | -------- | ----------- |
| BR-001 | {Rule Name}  | Critical | API-XXX     |

#### API Contracts (API-XXX)

| ID      | Endpoint        | Method | Validates |
| ------- | --------------- | ------ | --------- |
| API-001 | {Endpoint Path} | POST   | BR-XXX    |

#### Database Tables (DBT-XXX)

| ID      | Table Name   | Accessed By |
| ------- | ------------ | ----------- |
| DBT-001 | {table_name} | API-XXX     |

#### Customer Feedback (CFD-XXX)

| ID      | Category | Status  | Affects |
| ------- | -------- | ------- | ------- |
| CFD-001 | Research | Planned | UJ-XXX  |

#### Design Components (DES-XXX)

| ID      | Component Name   | Platform | Used In |
| ------- | ---------------- | -------- | ------- |
| DES-001 | {Component Name} | Web      | UJ-XXX  |

#### Tests (TEST-XXX)

| ID       | Test Name   | Category | Validates |
| -------- | ----------- | -------- | --------- |
| TEST-001 | {Test Name} | Unit     | API-XXX   |

#### Deployments (DEP-XXX)

| ID      | Configuration | Environment | Used By |
| ------- | ------------- | ----------- | ------- |
| DEP-001 | {Config Name} | Production  | API-XXX |

---

## Part 3: Validation

### 3.1 Cross-Reference Checks

When forking this repo, validate:

- **Orphaned IDs**: IDs defined but never referenced
- **Dangling References**: IDs referenced but not defined
- **Broken Links**: Cross-references pointing to non-existent IDs

## Change Log

| Date       | Change                                              |
| ---------- | --------------------------------------------------- |
| 2025-12-22 | Combined UNIQUE_ID_SYSTEM and ID_REGISTRY into one  |
