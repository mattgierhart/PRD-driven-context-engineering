---
version: 1.0
purpose: Source of Truth for database schema and data model specifications.
id_prefix: DBT-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, EPICs
---
<!-- SECTION: template-structure -->

# Data Model (SoT File)

> **Purpose**: Database tables, views, and relationships for the product.
> **ID Prefix**: DBT-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md, SoT.TESTING.md

## Navigation by Category

**Core Tables** (DBT-001 to DBT-099):

- [DBT-001](#dbt-001-table-name) - {Table name}

**Feature Tables** (DBT-101 to DBT-199):

- [DBT-101](#dbt-101-table-name) - {Table name}

**Junction Tables** (DBT-201 to DBT-299):

- [DBT-201](#dbt-201-table-name) - {Table name}

**Views** (DBT-301 to DBT-399):

- [DBT-301](#dbt-301-view-name) - {View name}

---

## DBT-001: {Table Name}

**ID**: DBT-001
**Category**: Core | Feature | Junction | View
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Purpose

{What this table stores and why it exists.}

### Columns

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `id` | UUID | Yes | Primary key |
| `user_id` | UUID | Yes | Owner reference |
| `name` | TEXT | Yes | Display name |
| `status` | TEXT | Yes | Record status |
| `created_at` | TIMESTAMPTZ | Yes | Creation timestamp |
| `updated_at` | TIMESTAMPTZ | Yes | Last update |

### Key Indexes

- Primary key on `id`
- Index on `user_id` for ownership lookups
- Partial index on `status` where not deleted

### Related IDs

- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {Endpoint accessing this table}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey using this data}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Rule enforced by constraint}
- [TEST-XXX](SoT.TESTING.md#test-xxx) - {Schema validation test}

### Foreign Keys

- **References**: `auth.users` (user_id → id)
- **Referenced By**: [DBT-XXX](#dbt-xxx-child-table) (parent_id → id)

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Tables

### DBT-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [DBT-YYY](#dbt-yyy-name) | None
**Reason**: {Why deprecated}

<!-- /CUSTOMIZABLE: entries -->

---

## Cross-Reference Index

**Tables by API**:

- API-001 accesses: DBT-001, DBT-101

**Tables by Journey**:

- UJ-001 uses: DBT-001, DBT-101

---

## Update Protocol

### When to Add New DBT-XXX IDs

1. **New Table**: Core data entity for the product
2. **New View**: Denormalized read model
3. **Junction Table**: Many-to-many relationship

### Bidirectional Reference Checklist

When adding a new DBT-XXX:

- [ ] Update SoT.API_CONTRACTS.md "Related IDs" section
- [ ] Update SoT.USER_JOURNEYS.md if journey uses this data
- [ ] Update SoT.BUSINESS_RULES.md if constraint enforces rule
- [ ] Update SoT.TESTING.md with schema tests
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.DATA_MODEL.md - Authoritative source for all DBT-XXX IDs*
