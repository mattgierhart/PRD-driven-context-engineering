---
title: "Unique ID System"
updated: "2025-12-22"
authority: "Gear Heart Methodology"
---

# Unique ID System

> **Rule**: Every durable concept gets an ID. IDs are stable. Names are not.

---

## 1. ID Format

**Format**: `[PREFIX]-[NUMBER]-[SLUG]`

- **Prefix**: 3-4 letters (e.g., `BR`, `API`).
- **Number**: 3 digits, strictly incrementing (e.g., `001`, `002`).
- **Slug** (Optional): Short description (e.g., `api-001-user-login`).

**Example**: `BR-104`, `UJ-012`, `API-800`

---

## 2. Standard Prefixes

| Prefix   | Meaning           | Spec File (specs/)                       |
| -------- | ----------------- | ---------------------------------------- |
| **BR**   | Business Rule     | `BUSINESS_RULES.md`                      |
| **UJ**   | User Journey      | `USER_JOURNEYS.md`                       |
| **API**  | API Contract      | `API_CONTRACTS.md`                       |
| **DBT**  | Data Schema       | `ACTUAL_SCHEMA.md`                       |
| **CFD**  | Customer Feedback | `customer_feedback.md`                   |
| **TEST** | Test Case         | `testing_playbook.md`                    |
| **DEP**  | Deployment Step   | `deployment_playbook.md`                 |
| **KPI**  | Key Metric        | `README.md` (or dedicated Metrics table) |

---

## 3. How to Assign IDs

1. **Check the Ledger**: Look at the `specs/` file for the highest used number.
2. **Increment**: Add 1.
3. **Log it**: Write the new entry in the Spec (`specs/`) file.
4. **Use it**: Reference it in code, PRDs, and EPICs as `[PREFIX-XXX]`.

> **Note**: Never re-use an ID even if the feature is deleted. Deprecate it instead.

---

## 4. Common Patterns (The Graph)

### A. API Implements Rule

> "Code enforces Business Logic"

```text
BR-001 (User Limit)
  └─→ API-045 (POST /users validation)
      └─→ TEST-301 (Unit test for API-045)
```

### B. User Journey Dependencies

> "UX Flow requires Backend + Design"

```text
UJ-101 (Onboarding Flow)
  ├─→ API-045 (Create User)
  ├─→ DES-042 (Sign Up Mockup)
  └─→ BR-001 (Limit Check)
```

### C. Feedback Drives Features

> "User Request becomes Feature"

```text
CFD-089 (Request: Dark Mode)
  └─→ UJ-105 (Theme Switcher Flow)
      ├─→ DBT-025 (User Preferences Table)
      └─→ TEST-310 (Visual Regression)
```
