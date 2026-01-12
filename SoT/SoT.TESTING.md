---
version: 1.0
purpose: Source of Truth for test specifications and coverage requirements.
id_prefix: TEST-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.BUSINESS_RULES.md, EPICs
---

# Testing (SoT File)

> **Purpose**: Test case specifications, coverage targets, and validation strategies.
> **ID Prefix**: TEST-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.BUSINESS_RULES.md, SoT.USER_JOURNEYS.md, EPICs

## Navigation by Category

**Unit Tests** (TEST-001 to TEST-099):

- [TEST-001](#test-001-test-name) - {Test name}

**Integration Tests** (TEST-101 to TEST-199):

- [TEST-101](#test-101-test-name) - {Test name}

**End-to-End Tests** (TEST-201 to TEST-299):

- [TEST-201](#test-201-test-name) - {Test name}

**Performance Tests** (TEST-301 to TEST-399):

- [TEST-301](#test-301-test-name) - {Test name}

---

## Coverage Targets

| Category | Statement | Branch | Function | Line |
|----------|-----------|--------|----------|------|
| Core Logic | ≥80% | ≥75% | ≥85% | ≥80% |
| API Layer | ≥80% | ≥75% | ≥85% | ≥80% |
| UI Layer | ≥70% | ≥65% | ≥75% | ≥70% |

---

## TEST-001: {Test Name}

**ID**: TEST-001
**Category**: Unit | Integration | E2E | Performance
**Status**: Active | Deprecated | Planned
**Priority**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD

### Description

{What this test validates and why it matters.}

### Test Case (Given-When-Then)

**Given**: {Initial state or preconditions}
**When**: {Action or trigger}
**Then**: {Expected outcome}

### Validates

- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule tested}
- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {Endpoint tested}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey validated}
- [DBT-XXX](SoT.DATA_MODEL.md#dbt-xxx) - {Schema tested}

### Implementation

**File**: `tests/{category}/{name}.test.ts`
**Traceability**: `// @implements TEST-001`

---

## Deprecated Tests

### TEST-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [TEST-YYY](#test-yyy-name) | None
**Reason**: {Why deprecated}

---

## Cross-Reference Index

**Tests by Business Rule**:

- BR-001 validated by: TEST-001, TEST-101

**Tests by API**:

- API-001 validated by: TEST-101, TEST-201

---

## Update Protocol

### When to Add New TEST-XXX IDs

1. **Unit Test**: Testing isolated function/component
2. **Integration Test**: Testing API or service interaction
3. **E2E Test**: Testing complete user journey
4. **Performance Test**: Testing response times or load

### Bidirectional Reference Checklist

When adding a new TEST-XXX:

- [ ] Update SoT.BUSINESS_RULES.md "Validated By" section
- [ ] Update SoT.API_CONTRACTS.md "Related IDs" section
- [ ] Update SoT.USER_JOURNEYS.md if testing a journey
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Add `// @implements TEST-XXX` in test file

---

*End of SoT.TESTING.md - Authoritative source for all TEST-XXX IDs*
