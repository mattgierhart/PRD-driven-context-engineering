---
version: 1.0
purpose: Source of Truth file for all user journey specifications. Each journey has a unique ID for cross-referencing.
id_prefix: UJ-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by PRD.md, EPICs, and other SoT files
---

# User Journeys (SoT File)

> **Purpose**: Complete specifications for all user flows and journeys.
> **ID Prefix**: UJ-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, API_CONTRACTS.md, testing-playbook.md, EPICs

## Navigation by Category

**Core Journeys** (UJ-001 to UJ-099):
- [UJ-001](#uj-001-journey-name) - {Journey name}
- [UJ-002](#uj-002-journey-name) - {Journey name}

**Feature-Specific Journeys** (UJ-101 to UJ-199):
- [UJ-101](#uj-101-journey-name) - {Journey name}
- [UJ-102](#uj-102-journey-name) - {Journey name}

**Admin/Internal Journeys** (UJ-201 to UJ-299):
- [UJ-201](#uj-201-journey-name) - {Journey name}

**Error/Edge Case Journeys** (UJ-301 to UJ-399):
- [UJ-301](#uj-301-journey-name) - {Journey name}

---

## UJ-001: {Journey Name}

**ID**: UJ-001
**Category**: Core User Journey
**Status**: Active | Deprecated | Planned
**Owner**: Product Team
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Overview

**User Goal**: {What the user wants to accomplish}
**Trigger**: {What initiates this journey}
**Success Criteria**: {How we know the journey succeeded}
**Performance Target**: <{X} seconds
**Expected Frequency**: {Daily/Weekly/Monthly per user}

### Journey Steps

1. **{Step Name}**
   - User Action: {What user does}
   - System Response: {What happens}
   - UI Element: [DES-XXX] (if applicable)

2. **{Step Name}**
   - User Action: {What user does}
   - System Response: {What happens}
   - API Call: [API-XXX] (if applicable)

3. **{Step Name}**
   - User Action: {What user does}
   - System Response: {What happens}
   - Validation: [BR-XXX] (business rule enforced)

### Related IDs

**APIs Used**:
- [API-XXX](API_CONTRACTS.md#api-xxx) - {Endpoint description}
- [API-YYY](API_CONTRACTS.md#api-yyy) - {Endpoint description}

**Business Rules Enforced**:
- [BR-XXX](BUSINESS_RULES.md#br-xxx) - {Rule description}
- [BR-YYY](BUSINESS_RULES.md#br-yyy) - {Rule description}

**Database Tables Accessed**:
- [DBT-XXX](ACTUAL-SCHEMA.md#dbt-xxx) - {Table description}
- [DBT-YYY](ACTUAL-SCHEMA.md#dbt-yyy) - {Table description}

**Design Components**:
- [DES-XXX]({product}-DesignBrief.md#des-xxx) - {Component description}

**Validated By**:
- [TEST-XXX](testing-playbook.md#test-xxx) - {Test description}
- [TEST-YYY](testing-playbook.md#test-yyy) - {Test description}

**Related Feedback**:
- [CFD-XXX](customer-feedback.md#cfd-xxx) - {Feedback about this journey}

### Error Flows

**Error Scenario 1** (Error code: {XXX}):
- Trigger: {What causes this error}
- User sees: {Error message}
- Recovery: {How user recovers}
- Related Journey: [UJ-XXX-E01] (if dedicated error journey)

**Error Scenario 2** (Error code: {YYY}):
- Trigger: {What causes this error}
- User sees: {Error message}
- Recovery: {How user recovers}

### Metrics & Analytics

**Success Metrics**:
- Completion rate: {X}% (target: {Y}%)
- Average time: {X} seconds (target: <{Y} seconds)
- Error rate: {X}% (target: <{Y}%)

**Drop-off Points**:
- Step 2: {X}% abandon (reason: {why})
- Step 4: {Y}% abandon (reason: {why})

**Analytics Events**:
```typescript
// Journey start
trackEvent('uj_001_start', { user_id, source });

// Journey complete
trackEvent('uj_001_complete', { user_id, duration_ms });

// Journey abandon
trackEvent('uj_001_abandon', { user_id, step, reason });
```

### Detailed Specification

For detailed wireframes, mockups, and step-by-step specifications, see:
- [user-journeys/{filename}.md](user-journeys/{filename}.md)
- Figma: {Link to Figma file/frame}

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | YYYY-MM-DD | Initial creation | {Name} |
| 1.1 | YYYY-MM-DD | {Change description} | {Name} |

---

## UJ-002: {Next Journey Name}

{Repeat the above structure for each journey}

---

## Deprecated Journeys

### UJ-XXX: {Deprecated Journey Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [UJ-YYY](#uj-yyy-journey-name)
**Reason**: {Why deprecated}
**Migration Guide**: {How to transition to new journey}
**Removal Date**: {When this ID will be fully removed}

---

## Cross-Reference Index

> **Auto-Generated Section**: Run `npm run codex:sync-journeys` to rebuild

**Journeys by API**:
- API-045 used by: UJ-101, UJ-102, UJ-201
- API-046 used by: UJ-101

**Journeys by Business Rule**:
- BR-112 enforced in: UJ-101, UJ-102
- BR-089 enforced in: UJ-101

**Journeys by Test Coverage**:
- TEST-301 validates: UJ-101 (steps 1-3)
- TEST-302 validates: UJ-101 (error flows)

---

## Update Protocol

### When to Add New UJ-XXX IDs

1. **New User Journey**: Complete flow from trigger to goal completion
2. **Journey Variant**: Alternative path for existing journey (e.g., mobile vs. web)
3. **Error Flow**: Distinct error handling or recovery journey
4. **Feature Journey**: New feature introducing new user interactions

### Bidirectional Reference Checklist

When adding a new UJ-XXX:
- [ ] Update API_CONTRACTS.md "Used By" section for each API called in this journey
- [ ] Update BUSINESS_RULES.md "Affects User Journeys" section for each rule enforced
- [ ] Update ACTUAL-SCHEMA.md "Used in User Journeys" section for each table accessed
- [ ] Update design-brief.md with DES-XXX references for UI components used
- [ ] Update testing-playbook.md with TEST-XXX references for validation tests
- [ ] Update EPIC Section 3A "IDs Created This EPIC" table
- [ ] Update README.md "Active IDs" section if part of current work
- [ ] Run `npm run codex:sync-registry` to update ID-REGISTRY.md

---

*End of USER-JOURNEYS.md - This SoT file is the authoritative source for all UJ-XXX IDs*
