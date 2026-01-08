---
title: "Unique ID System"
updated: "2026-01-08"
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
| **FEA**  | Feature           | `FEATURES.md`                            |
| **PER**  | Persona           | `PERSONAS.md`                            |
| **SCR**  | Screen            | `SCREENS.md`                             |
| **DES**  | Design Element    | `DESIGN_SYSTEM.md`                       |
| **RISK** | Risk              | `RISK_REGISTER.md`                       |
| **TECH** | Technology Choice | `TECH_STACK.md`                          |
| **ARC**  | Architecture Decision | `ARCHITECTURE_DECISIONS.md`          |
| **EPIC** | Work Package      | `epics/EPIC-XXX.md`                      |

---

## 2.1 Compound IDs

Some concepts require **compound IDs** that combine two prefixes to express a relationship or governance rule.

**Format**: `[PREFIX1]-[PREFIX2]-[NUMBER]`

| Compound ID | Meaning | Use Case |
|-------------|---------|----------|
| **BR-FEA-XXX** | Feature Governance Rule | Business rules that constrain feature decisions |

**Example Compound IDs:**
```
BR-FEA-001: "P0 features must have KPI link"
BR-FEA-002: "Fast Follow products prioritize parity before delta"
BR-FEA-003: "No P3 features until P0-P1 complete"
```

**When to Use Compound IDs:**
- The concept governs or constrains another ID type
- A simple prefix doesn't capture the relationship
- The rule applies to a specific domain (features, journeys, etc.)

**When NOT to Use:**
- If a simple prefix suffices (most cases)
- For simple references (use "Links to: FEA-001" instead)

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

### D. Feature Governance

> "Business Rules constrain Feature Decisions"

```text
BR-FEA-001 (P0 requires KPI link)
  └─→ FEA-001 (Core Feature) ✓ Has KPI-001 link
  └─→ FEA-015 (Nice-to-have) ✗ No KPI link → demoted to P3

BR-FEA-002 (Parity before Delta for Fast Follow)
  └─→ FEA-002 (Parity) → P0
  └─→ FEA-010 (Delta) → P2 (after parity complete)
```

### E. Epic as Context Window

> "EPICs scope work to cognitive capacity"

```text
EPIC-001 (User Authentication)
  ├─→ API-001, API-002, API-003 (Auth endpoints)
  ├─→ DBT-001 (Users table)
  ├─→ BR-001, BR-002 (Auth rules)
  ├─→ UJ-001 (Login flow)
  └─→ TEST-001 to TEST-010 (Validation)
      └─→ Code with // @implements tags
```

### F. Implementation Traceability

> "Code declares which IDs it implements"

```text
Code: src/auth/createUser.ts
  └─→ // @implements API-001 (Create User)
      └─→ // @see BR-001 (Email uniqueness)
      └─→ // @see DBT-001 (Users table)
          └─→ TEST-001 (validates API-001)
```
