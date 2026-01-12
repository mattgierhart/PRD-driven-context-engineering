# SoT Builder Examples

Real-world examples of creating new Source of Truth files.

---

## Example 1: Partner Integration Contracts

### Scenario

A B2B SaaS product needs to track third-party integrations (Stripe, Twilio, SendGrid) with their own contracts, SLAs, and API dependencies. Existing SoT files don't fit:

- `SoT.API_CONTRACTS.md` — Tracks OUR APIs, not partner APIs
- `SoT.BUSINESS_RULES.md` — Tracks rules, not integration specs

### Decision Process

**Q: What artifact type does this track?**
A: Partner Integration Contracts — specs for each third-party service

**Q: Why can't existing SoT files handle this?**
A: Partner integrations need fields like "SLA", "Billing Contact", "Fallback Provider" that don't fit API or BR schemas

**Q: What ID prefix will you use?**
A: `PIC-` (Partner Integration Contract)

### Schema Design

```markdown
ID Prefix: PIC-###

Categories:
- PIC-001 to PIC-099: Payment providers
- PIC-101 to PIC-199: Communication services
- PIC-201 to PIC-299: Infrastructure services

Required Fields:
- Partner Name
- Contract Status (Active/Expired/Pending)
- SLA Guarantee
- Billing Contact
- Fallback Provider (if any)
- Integration APIs (links to API-XXX)
```

### Resulting SoT File Structure

```markdown
---
version: 1.0
purpose: Source of Truth for third-party partner integrations and their contracts
id_prefix: PIC-###
last_updated: 2025-01-10
authority: This SoT defines all external service dependencies
---

# Partner Integration Contracts (SoT File)

> **Purpose**: Specifications for all third-party service integrations
> **ID Prefix**: PIC-XXX
> **Status**: Active SoT file
> **Cross-References**: SoT.API_CONTRACTS.md, SoT.BUSINESS_RULES.md

## Navigation by Category

**Payment Providers** (PIC-001 to PIC-099):
- [PIC-001](#pic-001-stripe) - Stripe Payment Processing

**Communication Services** (PIC-101 to PIC-199):
- [PIC-101](#pic-101-twilio) - Twilio SMS/Voice

---

## PIC-001: Stripe Payment Processing

**ID**: PIC-001
**Partner**: Stripe, Inc.
**Status**: Active
**Contract Signed**: 2024-06-15
**Renewal Date**: 2025-06-15
**Billing Contact**: payments@ourcompany.com

### SLA Guarantee

- Uptime: 99.99%
- Transaction Processing: <2 seconds
- Support Response: 4 hours (business critical)

### Integration Points

**Our APIs that use this partner**:
- [API-045](SoT.API_CONTRACTS.md#api-045) - POST /payments/charge
- [API-046](SoT.API_CONTRACTS.md#api-046) - POST /subscriptions/create

**Business Rules affected**:
- [BR-101](SoT.BUSINESS_RULES.md#br-101) - Payment retry policy

### Fallback Provider

Primary: Stripe
Fallback: None (evaluate adding Adyen)

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | 2025-01-10 | Initial creation | Product Team |

---

## Update Protocol

### When to Add New PIC-XXX IDs

1. **New Partner**: Signing contract with new service provider
2. **Service Migration**: Moving from one provider to another
3. **New Integration Type**: Adding partner for new capability

### Bidirectional Reference Checklist

When adding a new PIC-XXX:
- [ ] Update SoT.API_CONTRACTS.md "Uses Partner" section for affected APIs
- [ ] Update SoT.BUSINESS_RULES.md if partner affects rule enforcement
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry tables
```

---

## Example 2: Migration Procedures

### Scenario

An enterprise product needs to track database migration procedures with rollback plans and dependencies. This doesn't fit existing SoT files:

- `SoT.ACTUAL_SCHEMA.md` — Tracks schema state, not migration procedures
- `SoT.deployment_playbook.md` — General deployment, not schema-specific

### Decision Process

**Q: What artifact type does this track?**
A: Database migration procedures with rollback plans

**Q: Why can't existing SoT files handle this?**
A: Migrations need sequencing, dependencies, and rollback scripts that don't fit DEP- entries

**Q: What ID prefix will you use?**
A: `MIG-` (Migration)

### Schema Design

```markdown
ID Prefix: MIG-###

Categories:
- MIG-001 to MIG-099: Schema migrations
- MIG-101 to MIG-199: Data migrations
- MIG-201 to MIG-299: Index migrations

Required Fields:
- Migration Name
- Status (Pending/Applied/Rolled Back)
- Dependencies (previous MIG-XXX)
- Affected Tables (DBT-XXX)
- Rollback Script
- Applied Date
```

### Key Differences from Example 1

This example shows a **procedural SoT** (ordered steps) vs. a **entity SoT** (static definitions):

- Entry order matters (dependencies)
- Status changes over time (Applied/Rolled Back)
- Links to both past and future entries

---

## Example 3: What NOT to Create

### Anti-Pattern: "Notes" SoT

**Request**: "I want a SoT for random notes and ideas"

**Why it fails**:
- Not durable (notes are transient)
- No clear ID structure
- Doesn't need cross-referencing
- Better served by `temp/` folder

**Better approach**: Use `temp/scratch.md` for session notes, then harvest insights to `SoT.customer_feedback.md` (CFD- entries) if they become durable.

### Anti-Pattern: Duplicate Coverage

**Request**: "I want a SoT for authentication rules"

**Why it fails**:
- Already covered by `SoT.BUSINESS_RULES.md` (BR- entries)
- Would fragment related information
- Creates maintenance burden

**Better approach**: Add BR-XXX entries in the "Security" category range (BR-101 to BR-199) within the existing BUSINESS_RULES file.

### Anti-Pattern: Methodology in Template

**Request**: "I want a SoT that includes best practices for each entry"

**Why it fails**:
- Methodology teaching belongs in skill references
- Violates template purity standard
- Bloats context when file is loaded

**Better approach**: Keep template pure, create a skill (like `prd-vXX-{domain}`) that loads methodology when creating entries.

---

## Before/After: Template Contamination

### BEFORE (Contaminated Template)

```markdown
## MIG-001: Add user_preferences table

**ID**: MIG-001
**Status**: Pending

### Best Practices for This Migration

When creating new tables:
1. Always add created_at and updated_at columns
2. Consider indexing foreign keys
3. Use UUID for primary keys in distributed systems
4. Think about partitioning for large tables...

### Migration Script

```sql
CREATE TABLE user_preferences...
```
```

**Problem**: "Best Practices" section is methodology teaching that should be in a skill reference.

### AFTER (Pure Template)

```markdown
## MIG-001: Add user_preferences table

**ID**: MIG-001
**Status**: Pending
**Created**: 2025-01-10
**Dependencies**: None (first migration)
**Affects Tables**: [DBT-015](SoT.ACTUAL_SCHEMA.md#dbt-015)

### Migration Script

```sql
CREATE TABLE user_preferences (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  preferences JSONB NOT NULL DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Rollback Script

```sql
DROP TABLE IF EXISTS user_preferences;
```

### Version History

| Version | Date | Changes | Applied By |
|---------|------|---------|------------|
| 1.0 | 2025-01-10 | Initial creation | Platform Team |
```

**Fixed**: Methodology moved to skill references. Template contains only structural information.

---

## Registration Checklist

After creating any new SoT file, complete:

### SoT.README.md Update

```markdown
| `SoT.{YOUR_FILE}.md` | {PREFIX}-### | {Purpose} |
```

### SoT.UNIQUE_ID_SYSTEM.md Updates

**Section 1.2 - Add prefix**:
```markdown
| **{PREFIX}** | {Meaning} | `SoT.{YOUR_FILE}.md` |
```

**Section 2.2 - Add index table**:
```markdown
#### {Your Type} ({PREFIX}-XXX)

| ID | Title | Status | Used By |
|----|-------|--------|---------|
```

### Verification

- [ ] File exists at `SoT/SoT.{NAME}.md`
- [ ] SoT.README.md lists the file
- [ ] SoT.UNIQUE_ID_SYSTEM.md has the prefix
- [ ] Can create a test entry using template
- [ ] Cross-references work in both directions
