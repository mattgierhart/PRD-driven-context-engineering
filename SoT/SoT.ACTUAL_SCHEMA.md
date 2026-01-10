---
version: 1.0
purpose: Source of Truth file for actual database schema. Each table/view has a unique ID for cross-referencing.
id_prefix: DBT-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md, SoT.testing_playbook.md
generation: Hybrid (auto-generated from migrations + human context)
---

# Database Schema (SoT File)

> **Purpose**: Complete specifications for all database tables, views, and constraints.
> **ID Prefix**: DBT-XXX
> **Status**: Active SoT file
> **Generation**: Auto-generated schema + human-added context
> **Cross-References**: Referenced by SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md, SoT.testing_playbook.md

## Navigation by Category

**Core Tables** (DBT-001 to DBT-099):
- [DBT-001](#dbt-001-table-name) - {Table name}
- [DBT-002](#dbt-002-table-name) - {Table name}

**Feature Tables** (DBT-101 to DBT-199):
- [DBT-101](#dbt-101-table-name) - {Table name}
- [DBT-102](#dbt-102-table-name) - {Table name}

**Junction/Relationship Tables** (DBT-201 to DBT-299):
- [DBT-201](#dbt-201-table-name) - {Table name}

**Views & Materialized Views** (DBT-301 to DBT-399):
- [DBT-301](#dbt-301-view-name) - {View name}

**Audit/System Tables** (DBT-401 to DBT-499):
- [DBT-401](#dbt-401-table-name) - {Table name}

---

## DBT-001: {Table Name}

**ID**: DBT-001
**Category**: Core Table | Feature Table | Junction Table | View | Audit Table
**Status**: Active | Deprecated | Planned
**Owner**: Backend Team | Data Team
**Created**: YYYY-MM-DD (Migration: `YYYYMMDDHHMMSS_{name}.sql`)
**Last Updated**: YYYY-MM-DD (Migration: `YYYYMMDDHHMMSS_{name}.sql`)
**Schema**: `public` | `private` | `auth` | `storage`

### Purpose & Context

**What It Stores**: {Description of data stored in this table}
**Why It Exists**: {Business rationale for this table}
**Primary Use Cases**: {How this table is used}

### Schema Definition

> **Auto-Generated from Migration**: `migrations/YYYYMMDDHHMMSS_create_{table_name}.sql`

```sql
CREATE TABLE {schema}.{table_name} (
  -- Primary Key
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Required Fields
  name TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),

  -- Optional Fields
  description TEXT,
  metadata JSONB DEFAULT '{}',

  -- Foreign Keys
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  parent_id UUID REFERENCES {schema}.{parent_table}(id) ON DELETE SET NULL,

  -- Timestamps
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at TIMESTAMPTZ
);

-- Indexes
CREATE INDEX idx_{table_name}_user_id ON {schema}.{table_name}(user_id);
CREATE INDEX idx_{table_name}_status ON {schema}.{table_name}(status) WHERE deleted_at IS NULL;
CREATE INDEX idx_{table_name}_created_at ON {schema}.{table_name}(created_at DESC);

-- Full-text search (if applicable)
CREATE INDEX idx_{table_name}_search ON {schema}.{table_name}
USING gin(to_tsvector('english', name || ' ' || COALESCE(description, '')));

-- Unique constraints
ALTER TABLE {schema}.{table_name}
ADD CONSTRAINT unique_{table_name}_user_name UNIQUE (user_id, name);

-- Check constraints
ALTER TABLE {schema}.{table_name}
ADD CONSTRAINT check_{table_name}_status CHECK (status IN ('active', 'inactive', 'archived'));

-- Comments
COMMENT ON TABLE {schema}.{table_name} IS 'Stores {description}';
COMMENT ON COLUMN {schema}.{table_name}.metadata IS 'JSONB field for extensible properties';
```

### Field Specifications

| Column | Type | Nullable | Default | Description | Example |
|--------|------|----------|---------|-------------|---------|
| `id` | UUID | No | `gen_random_uuid()` | Primary identifier | `550e8400-e29b-41d4-a716-446655440000` |
| `name` | TEXT | No | - | Display name | `"Widget Pro"` |
| `status` | TEXT | No | `'active'` | Record status | `'active'` |
| `metadata` | JSONB | Yes | `'{}'` | Flexible extension field | `{"key": "value"}` |
| `created_at` | TIMESTAMPTZ | No | `now()` | Creation timestamp | `2025-11-09T10:30:00Z` |
| `updated_at` | TIMESTAMPTZ | No | `now()` | Last update timestamp | `2025-11-09T10:30:00Z` |
| `deleted_at` | TIMESTAMPTZ | Yes | NULL | Soft delete timestamp | `2025-11-09T10:30:00Z` |

### Indexes & Performance

**Indexes**:

| Index Name | Columns | Type | Purpose | Notes |
|------------|---------|------|---------|-------|
| `{table_name}_pkey` | `id` | B-tree | Primary key | Auto-created |
| `idx_{table_name}_user_id` | `user_id` | B-tree | Foreign key lookups | Covers most queries |
| `idx_{table_name}_status` | `status` WHERE `deleted_at IS NULL` | Partial B-tree | Active records only | Reduces index size |
| `idx_{table_name}_search` | `to_tsvector(...)` | GIN | Full-text search | For search features |

**Performance Characteristics**:
- Estimated row count: ~{X} rows (at scale)
- Average row size: ~{Y} bytes
- Estimated table size: ~{Z} MB (at scale)
- Query patterns: Mostly indexed lookups, some full-text search

**Query Optimization Notes**:
- Use `user_id` filter for best performance (indexed)
- Avoid `SELECT *` - specify needed columns
- Consider pagination for large result sets
- Use `deleted_at IS NULL` filter for active records

### Row-Level Security (RLS)

**RLS Enabled**: Yes | No

**Policies**:

```sql
-- Enable RLS
ALTER TABLE {schema}.{table_name} ENABLE ROW LEVEL SECURITY;

-- Policy 1: Users can view their own records
CREATE POLICY "Users can view own {table_name}"
  ON {schema}.{table_name}
  FOR SELECT
  USING (auth.uid() = user_id);

-- Policy 2: Users can insert their own records
CREATE POLICY "Users can insert own {table_name}"
  ON {schema}.{table_name}
  FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Policy 3: Users can update their own records
CREATE POLICY "Users can update own {table_name}"
  ON {schema}.{table_name}
  FOR UPDATE
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Policy 4: Users can soft-delete their own records
CREATE POLICY "Users can delete own {table_name}"
  ON {schema}.{table_name}
  FOR DELETE
  USING (auth.uid() = user_id);

-- Policy 5: Admins can view all records
CREATE POLICY "Admins can view all {table_name}"
  ON {schema}.{table_name}
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1 FROM auth.users
      WHERE auth.users.id = auth.uid()
      AND auth.users.role = 'admin'
    )
  );
```

**RLS Testing**:
- [TEST-XXX](SoT.testing_playbook.md#test-xxx) - Validates user isolation
- [TEST-YYY](SoT.testing_playbook.md#test-yyy) - Validates admin access

### Related IDs

**Accessed By APIs**:
- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {Endpoint name} (Read/Write/Update/Delete)
- [API-YYY](SoT.API_CONTRACTS.md#api-yyy) - {Another endpoint} (Read only)

**Used in User Journeys**:
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey that interacts with this table}
- [UJ-YYY](SoT.USER_JOURNEYS.md#uj-yyy) - {Another journey}

**Enforces Business Rules**:
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule via constraint}
- [BR-YYY](SoT.BUSINESS_RULES.md#br-yyy) - {Another rule}

**Validated By Tests**:
- [TEST-XXX](SoT.testing_playbook.md#test-xxx) - {Schema validation test}
- [TEST-YYY](SoT.testing_playbook.md#test-yyy) - {RLS policy test}
- [TEST-ZZZ](SoT.testing_playbook.md#test-zzz) - {Data integrity test}

**Foreign Key Relationships**:
- **References**:
  - [DBT-XXX](#dbt-xxx-parent-table) (`parent_id` → `id`) - Parent relationship
  - `auth.users` (`user_id` → `id`) - User ownership
- **Referenced By**:
  - [DBT-YYY](#dbt-yyy-child-table) (`{table_name}_id` → `id`) - Child relationship

### Triggers & Functions

**Triggers**:

```sql
-- Trigger 1: Auto-update timestamp
CREATE TRIGGER set_updated_at
  BEFORE UPDATE ON {schema}.{table_name}
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();

-- Trigger 2: Validate business rules
CREATE TRIGGER validate_{table_name}
  BEFORE INSERT OR UPDATE ON {schema}.{table_name}
  FOR EACH ROW
  EXECUTE FUNCTION validate_{table_name}_rules();

-- Trigger 3: Audit trail
CREATE TRIGGER audit_{table_name}_changes
  AFTER INSERT OR UPDATE OR DELETE ON {schema}.{table_name}
  FOR EACH ROW
  EXECUTE FUNCTION log_audit_trail();
```

**Function Implementations**:

```sql
-- Function: Update timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Function: Validate business rules
CREATE OR REPLACE FUNCTION validate_{table_name}_rules()
RETURNS TRIGGER AS $$
BEGIN
  -- Example: Enforce BR-001 at database level
  IF NEW.status = 'active' AND ... THEN
    RAISE EXCEPTION 'Business rule BR-001 violation: %', 'description';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Data Integrity & Constraints

**Referential Integrity**:
- All foreign keys use `ON DELETE CASCADE` or `ON DELETE SET NULL` appropriately
- No orphaned records allowed
- Cascading deletes properly configured

**Data Validation**:
- Status field constrained to valid enum values
- Dates validated for logical consistency
- JSONB metadata follows schema (documented in code)

**Audit Trail**:
- All changes logged to `audit_log` table
- Includes: user_id, action, old_value, new_value, timestamp
- Retention: {X} days

### Example Queries

**Common Query Patterns**:

```sql
-- Pattern 1: Get active records for user
SELECT id, name, status, created_at
FROM {schema}.{table_name}
WHERE user_id = $1
  AND deleted_at IS NULL
  AND status = 'active'
ORDER BY created_at DESC
LIMIT 20;

-- Pattern 2: Full-text search
SELECT id, name,
       ts_rank(to_tsvector('english', name || ' ' || COALESCE(description, '')),
               plainto_tsquery('english', $1)) as rank
FROM {schema}.{table_name}
WHERE to_tsvector('english', name || ' ' || COALESCE(description, ''))
      @@ plainto_tsquery('english', $1)
  AND user_id = $2
  AND deleted_at IS NULL
ORDER BY rank DESC
LIMIT 10;

-- Pattern 3: Aggregate statistics
SELECT status, COUNT(*) as count
FROM {schema}.{table_name}
WHERE user_id = $1
  AND deleted_at IS NULL
GROUP BY status;
```

### Migration History

**Migration Files** (chronological order):

| Migration | Date | Description | Breaking Change? |
|-----------|------|-------------|------------------|
| `20251109120000_create_{table_name}.sql` | 2025-11-09 | Initial table creation | N/A |
| `20251110100000_add_{column}_to_{table_name}.sql` | 2025-11-10 | Added optional field | No |
| `20251115143000_alter_{table_name}_constraints.sql` | 2025-11-15 | Updated check constraint | No |

### Backup & Recovery

**Backup Strategy**:
- Full backup: Daily at 2 AM UTC
- Incremental backup: Every 6 hours
- Point-in-time recovery: Available for last 30 days
- Retention: 90 days for full backups

**Recovery Testing**:
- Last tested: YYYY-MM-DD
- Recovery time objective (RTO): {X} hours
- Recovery point objective (RPO): {Y} minutes

### Compliance & Security

**Data Classification**:
- Contains PII: Yes | No
- Contains PHI: Yes | No (HIPAA)
- Contains PCI data: Yes | No
- Encryption at rest: Enabled

**Compliance Requirements**:
- GDPR: Right to erasure (soft delete via `deleted_at`)
- HIPAA: Audit trail enabled
- SOC2: Access logging enabled

### Detailed Specification

For migration files, seed data, and additional context, see:
- `supabase/migrations/YYYYMMDDHHMMSS_*.sql`
- `supabase/seed.sql` (development seed data)
- [database-schema/{table_name}.md](database-schema/{table_name}.md) (if extensive documentation needed)

### Version History

| Version | Date | Migration | Changes | Updated By |
|---------|------|-----------|---------|------------|
| 1.0 | YYYY-MM-DD | `20251109120000_create_{table_name}.sql` | Initial creation | {Name} |
| 1.1 | YYYY-MM-DD | `20251110100000_add_{column}_to_{table_name}.sql` | Added field | {Name} |

---

## DBT-002: {Next Table Name}

{Repeat the above structure for each table/view}

---

## Deprecated Tables

### DBT-XXX: {Deprecated Table Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [DBT-YYY](#dbt-yyy-table-name) | None (data archived)
**Reason**: {Why table was deprecated}
**Data Migration**: Completed YYYY-MM-DD (Migration: `YYYYMMDDHHMMSS_migrate_{old}_to_{new}.sql`)
**Drop Date**: {When table will be dropped} | Retained for audit (read-only)

---

## Cross-Reference Index

> **Auto-Generated Section**: Maintain manually unless you add tooling in a fork.

**Tables by API Access**:
- API-045 accesses: DBT-001 (RW), DBT-018 (R), DBT-019 (R)
- API-046 accesses: DBT-001 (R), DBT-018 (RW)

**Tables by User Journey**:
- UJ-101 uses: DBT-001, DBT-018, DBT-102
- UJ-102 uses: DBT-001

**Tables by Business Rule Enforcement**:
- BR-001 enforced by: DBT-001 (check constraint), DBT-102 (trigger)
- BR-112 enforced by: DBT-001 (RLS policy)

**Tables by Test Coverage**:
- TEST-301 validates: DBT-001 (schema)
- TEST-302 validates: DBT-001 (RLS policies)
- TEST-303 validates: DBT-018, DBT-019 (relationships)

**Foreign Key Graph**:

```
auth.users
  └─→ DBT-001 (user_id)
       ├─→ DBT-018 (parent_id)
       └─→ DBT-019 (parent_id)
           └─→ DBT-102 (relationship_id)
```

---

*End of SoT.ACTUAL_SCHEMA.md - This SoT file is the authoritative source for all DBT-XXX IDs*

## Maintenance Protocol

**Schema Updates**:
1. Create migration file: `supabase migration new {description}`
2. Write SQL in migration file
3. Test locally: `supabase db reset`
4. Update this file (auto-generate + add context)
5. Commit migration + updated SoT.ACTUAL_SCHEMA.md together

**Optional Tooling**:
If you add a schema doc generator in your product fork, document it here.
