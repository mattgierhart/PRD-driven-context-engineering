---
title: "Unique ID System"
updated: "2026-08-08"
authority: "PRD Led Context Engineering"
---
<!-- SECTION: template-structure -->

# Unique ID System

> **Rule**: Every durable concept gets an ID. IDs are stable. Names are not.

This file serves as the **governance guide** for the ID system and the **central registry** of all ID prefixes. The canonical machine-readable prefix registry is in [`.claude/domain-profile.yaml`](../.claude/domain-profile.yaml).

---

## Part 1: ID System Governance

### 1.1 ID Format

**Format**: `[PREFIX]-[NUMBER]` or `[PREFIX]-[SUBTYPE]-[NUMBER]`

- **Prefix**: registered base type (e.g., `BR`, `API`, `ADO`)
- **Subtype** (optional): documented uppercase category within a base type (e.g., `STAGE`, `FEA`);
  only the base prefix is machine-registered
- **Number**: 3 digits, strictly incrementing (e.g., `001`, `002`)
- **EPIC compatibility exception**: execution IDs may retain the established 2-digit form
  (`EPIC-NN`); validators accept 2 or 3 digits for EPIC only.

**Examples**: `BR-104`, `UJ-012`, `API-045`, `ADO-STAGE-001`, `BR-FEA-001`, `EPIC-01`

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
| **ENV** | Environment Profile | `SoT.TECHNICAL_DECISIONS.md` | v0.6 Architecture |
| **INT** | Integration | `SoT.INTEGRATIONS.md` | v0.6 Architecture |
| **API** | API Contract | `SoT.API_CONTRACTS.md` | v0.6 Architecture |
| **DBT** | Data Schema | `SoT.DATA_MODEL.md` | v0.6 Architecture |
| **BR** | Business Rule | `SoT.BUSINESS_RULES.md` | v0.2 Market Definition |
| **TEST** | Test Case | `SoT.TESTING.md` | v0.7 Build |
| **DEP** | Deployment | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **MON** | Monitoring | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **RUN** | Runbook | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **SEC** | Secret & Credential | `SoT.DEPLOYMENT.md` | v0.8 Release |
| **LL** | Lesson Learned | `SoT.LESSONS_LEARNED.md` | Cross-EPIC |
| **ADO** | Adoption Stage & Evidence | `SoT.ADOPTION.md` | v1.0 Market Adoption |

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
| **BR-FEA** | Documented feature-governance subtype | `BR-FEA-001` |
| **BR-API** | Documented API-validation subtype | `BR-API-045` |

### 1.3 How to Assign IDs

1. **Check**: Look at the SoT file for the highest used number
2. **Increment**: Add 1
3. **Log**: Write the new entry in the SoT file
4. **Use**: Reference as `[PREFIX-XXX]` in code, PRDs, EPICs

> **Note**: Never re-use an ID. Deprecate instead.

### 1.4 Common Patterns (The Graph)

#### A. API Enforces Rule

```text
API-045 (POST /users validation)
  └─ enforces → BR-001
BR-001
  └─ validated-by → TEST-301 (Unit test)
```

#### B. User Journey Dependencies

```text
UJ-101 (Onboarding Flow)
  ├─ uses → API-045 (Create User)
  └─ uses → DES-042 (Sign Up Component)
```

#### C. Feedback Drives Features

```text
FEA-015 in PRD (Theme Feature)
  └─ informed-by → CFD-089 (Request: Dark Mode)
UJ-105 (Theme Switcher Flow)
  └─ uses → FEA-015
```

> **Relationship types**: `informed-by`, `implements`, `enforces`, `validated-by`, `uses`, `depends-on`, `driven-by`, `supersedes`, `conflicts-with`, `designed-for`. See `ghm-id-register` skill for full vocabulary.

### 1.5 Staleness Protocol

Every SoT entry SHOULD include a `Verified: YYYY-MM-DD` field. Interpretation:

- **< 30 days**: Current. Use with confidence.
- **30-90 days**: Review before depending on it. Mark `⚠️ STALE` if unverified.
- **> 90 days**: Treat as historical. Verify against current code/state before using.

Agents encountering entries older than 90 days without recent verification SHOULD flag them in the
current PRD gate log before v0.7, or in the active EPIC's Agent Observations table from v0.7 onward.

### 1.6 Temporal Validity (valid-time)

Staleness (§1.5) tracks *transaction time* — when an entry was last touched. **Valid-time** tracks something different: the window during which a decision was actually authoritative. Git tells you when a file changed; it does not tell you *which architecture rule was in force while we were building v0.6*. Three optional fields on durable decision IDs (`ARC-`, `TECH-`; extensible to any prefix) make that queryable:

- **Valid From**: the PRD lifecycle version (e.g. `v0.6`) at which the decision took effect.
- **Valid To**: the version at which it stopped being authoritative. `—` while current.
- **Invalidated By**: the ID of the decision that superseded it. `—` while current.

**Supersede protocol** (extends "never re-use an ID — deprecate instead", §1.3): when a decision changes, do **not** overwrite it — close it and open a new one in place:

1. On the **old** entry: set `Valid To` to the superseding version, `Invalidated By` to the new ID, and `Status: Superseded`. Leave the entry where it is.
2. Create the **new** entry with its own ID, `Valid From` set to that version, and optionally `Supersedes: <old ID>`.

This keeps a single current reality *and* an auditable history — you can reconstruct the decision set as of any past version instead of doing git archaeology. The active methodology runtime's `asof.py <version>` reads these fields and does exactly that:

```text
$ python3 "${CLAUDE_PLUGIN_ROOT:-.}/scripts/asof.py" v0.6 --prefix ARC,TECH --repo .
ARC, TECH decisions authoritative as of v0.6
  ARC-001   Synchronous in-process request handling   valid v0.6 → v0.8
  TECH-001  Runtime: Node.js 20 LTS                   valid v0.5 → current
```

The fields are **optional and lenient**: an entry with no valid-time stamp is treated as always-valid, so adoption is incremental — stamp the decisions whose history matters (contested or superseded ones) first.

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Part 2: SoT File Registry

| SoT File | ID Prefixes | Lines | Purpose |
|----------|-------------|-------|---------|
| `SoT.BUSINESS_RULES.md` | BR-XXX | ~120 | Business constraints |
| `SoT.USER_JOURNEYS.md` | UJ, PER, SCR | ~150 | User flows, personas, screens |
| `SoT.API_CONTRACTS.md` | API-XXX | ~120 | Endpoint specifications |
| `SoT.DATA_MODEL.md` | DBT-XXX | ~120 | Database schema |
| `SoT.TESTING.md` | TEST-XXX | ~120 | Test specifications |
| `SoT.DEPLOYMENT.md` | DEP, RUN, MON, SEC | ~130 | Operations & deployment |
| `SoT.customer_feedback.md` | CFD-XXX | ~120 | Customer insights |
| `SoT.DESIGN_COMPONENTS.md` | DES-XXX | ~100 | UI components |
| `SoT.TECHNICAL_DECISIONS.md` | TECH, ARC, ENV | ~115 | Tech & architecture |
| `SoT.INTEGRATIONS.md` | INT-XXX | ~105 | Third-party services |
| `SoT.LESSONS_LEARNED.md` | LL-XXX | ~80 | Cross-session feedback |
| `SoT.ADOPTION.md` | ADO-XXX | ~120 | Adoption stage, beachhead, whole-product, and reference evidence |

<!-- /CUSTOMIZABLE: entries -->

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
| 2026-08-08 | Registered ADO, ENV, and SEC; clarified pre-v0.7 staleness routing and EPIC compatibility |
| 2026-01-12 | Standardized: Updated file references, added INT-XXX, clarified PRD vs SoT homes |
| 2026-01-12 | Added 8 missing ID prefixes. Organized by PRD stage |
| 2025-12-22 | Combined UNIQUE_ID_SYSTEM and ID_REGISTRY into one |
