---
version: 1.0
purpose: Template for auto-generated central registry of all IDs across Source of Truth files
generation: Hybrid (script-generated + human validation)
status: TEMPLATE - Copy to your project and customize
authority: When populated, this becomes the central ID index for your project
---

# ID Registry

> **Purpose**: Central index of all unique IDs across the knowledge graph
> **Status**: 📋 **TEMPLATE** - This file shows the intended structure for ID tracking
> **Usage**: When you start a project, the validation scripts in `tools/` will help populate this file

## About This File

This is a **template** showing how GHM tracks IDs across Source of Truth files. When you adopt GHM for your project:

1. Copy this template to your project's `.codex/` directory
2. As you create SoT entries (BR-XXX, API-XXX, etc.), they'll be tracked here
3. Use `python tools/generate_visuals.py` to generate ID graphs and reports

## ID Type Reference

| ID Type | SoT File | Purpose |
|---------|----------|---------|
| UJ-XXX | USER_JOURNEYS.md | User journey flows |
| BR-XXX | BUSINESS_RULES.md | Business rules and constraints |
| API-XXX | API_CONTRACTS.md | API endpoint specifications |
| DBT-XXX | ACTUAL_SCHEMA.md | Database table definitions |
| CFD-XXX | customer_feedback.md | Customer feedback items |
| TEST-XXX | testing_playbook.md | Test specifications |
| DEP-XXX | deployment_playbook.md | Deployment configurations |
| DES-XXX | design_brief.md | Design components |
| SEC-XXX | security_playbook.md | Security controls (optional) |
| PERF-XXX | performance_playbook.md | Performance metrics (optional) |

> **Note**: Counts and sync timestamps will appear here once you start creating SoT entries in your project.

---

## Example Structure

The sections below show the table format for each ID type. When you create SoT entries, they'll be indexed here.

### User Journeys (UJ-XXX)

| ID | Title | Status | Used By |
|----|-------|--------|---------|
| *UJ-001* | *Example: User Login Flow* | *Active* | *API-001, TEST-001* |

### Business Rules (BR-XXX)

| ID | Rule Name | Severity | Enforced By |
|----|-----------|----------|-------------|
| *BR-001* | *Example: Password Minimum Length* | *Critical* | *API-001* |

### API Contracts (API-XXX)

| ID | Endpoint | Method | Used By |
|----|----------|--------|---------|
| *API-001* | */api/auth/login* | *POST* | *UJ-001* |

### Database Tables (DBT-XXX)

| ID | Table Name | Accessed By |
|----|------------|-------------|
| *DBT-001* | *users* | *API-001* |

### Customer Feedback (CFD-XXX)

| ID | Category | Status | Affects |
|----|----------|--------|---------|
| *CFD-001* | *Feature Request* | *Planned* | *UJ-001* |

### Tests (TEST-XXX)

| ID | Test Name | Category | Validates |
|----|-----------|----------|-----------|
| *TEST-001* | *Login Success Test* | *Integration* | *API-001* |

### Other ID Types

Similar tables exist for:
- **DEP-XXX** — Deployment configurations
- **DES-XXX** — Design components
- **SEC-XXX** — Security controls (optional)
- **PERF-XXX** — Performance metrics (optional)

---

## Validation Reports

When populated, this section will show:
- **Orphaned IDs** — Referenced but not defined
- **Dangling References** — Defined but never referenced
- **Broken Links** — Cross-references to non-existent IDs

Use `python tools/generate_visuals.py --all` to generate validation reports.

---

## Available Tooling

GHM provides Python-based tools for ID management and validation:

```bash
# Generate ID knowledge graph and validation reports
python tools/generate_visuals.py --all

# Validate session state in EPICs
python tools/validate_sessions.py --all
```

See `tools/README.md` for full documentation.

---

*This template shows the structure for ID tracking in GHM projects. See [UNIQUE_ID_SYSTEM.md](../methodology/workflows/UNIQUE_ID_SYSTEM.md) for the full ID specification.*
