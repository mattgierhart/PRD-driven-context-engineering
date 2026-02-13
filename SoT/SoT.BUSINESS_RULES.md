---
version: 1.0
purpose: Source of Truth for business rules and operational constraints.
id_prefix: BR-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, SoT.API_CONTRACTS.md, EPICs, and code
---
<!-- SECTION: template-structure -->

# Business Rules (SoT File)

> **Purpose**: Complete specifications for business constraints, pricing rules, and enforcement policies.
> **ID Prefix**: BR-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, SoT.TESTING.md, EPICs

## Navigation by Category

**Pricing & Entitlements** (BR-001 to BR-099):

- [BR-001](#br-001-rule-name) - {Rule name}

**Data & Security** (BR-101 to BR-199):

- [BR-101](#br-101-rule-name) - {Rule name}

**User Permissions** (BR-201 to BR-299):

- [BR-201](#br-201-rule-name) - {Rule name}

**Compliance & Legal** (BR-301 to BR-399):

- [BR-301](#br-301-rule-name) - {Rule name}

**Performance & Limits** (BR-401 to BR-499):

- [BR-401](#br-401-rule-name) - {Rule name}

---

## BR-001: {Rule Name}

**ID**: BR-001
**Category**: Pricing | Data | Permissions | Compliance | Performance
**Status**: Active | Deprecated | Planned
**Severity**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Rule Statement

{Clear, enforceable statement of the business rule. Use imperative language.}

**Example**: "Free tier users MUST be limited to 3 products. Attempts to exceed MUST show upgrade prompt."

### Rationale

- **Business Driver**: {Why this rule exists}
- **User Impact**: {How it affects UX}

### Enforcement

**Location**: {Where enforced - server/client/both}
**Timing**: {When checked - on action, background, real-time}

### Related IDs

- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {Endpoint enforcing this}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey where rule applies}
- [DBT-XXX](SoT.DATA_MODEL.md#dbt-xxx) - {Table with constraint}
- [TEST-XXX](SoT.TESTING.md#test-xxx) - {Test validating compliance}

### Error Handling

- **Error Code**: `BR_001_VIOLATION`
- **User Message**: "{User-friendly error}"
- **Recovery**: {What user can do}

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Rules

### BR-XXX: {Rule Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [BR-YYY](#br-yyy-rule-name) | None
**Reason**: {Why deprecated}

<!-- /CUSTOMIZABLE: entries -->

---

## Cross-Reference Index

**Rules by API**:

- API-045 enforces: BR-001, BR-102

**Rules by Severity**:

- Critical: BR-001, BR-305
- High: BR-002, BR-103

---

## Update Protocol

### When to Add New BR-XXX IDs

1. **New Business Constraint**: Rule affecting user behavior or system limits
2. **Pricing Change**: New tier, limit, or entitlement rule
3. **Compliance Requirement**: Legal/regulatory mandate

### Bidirectional Reference Checklist

When adding a new BR-XXX:

- [ ] Update SoT.API_CONTRACTS.md "Enforces Business Rules" section
- [ ] Update SoT.USER_JOURNEYS.md "Business Rules Enforced" section
- [ ] Update SoT.TESTING.md with validation test
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.BUSINESS_RULES.md - Authoritative source for all BR-XXX IDs*
