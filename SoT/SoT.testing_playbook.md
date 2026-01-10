---
version: 1.0
purpose: Source of Truth file for test specifications and coverage expectations. Each test has a unique ID for cross-referencing.
id_prefix: TEST-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by PRD.md, SoT.BUSINESS_RULES.md, SoT.API_CONTRACTS.md, EPICs, and code
---

# Testing Playbook (SoT File)

> **Purpose**: Complete specifications for test cases, coverage expectations, and validation strategies.
> **ID Prefix**: TEST-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.BUSINESS_RULES.md, SoT.API_CONTRACTS.md, SoT.USER_JOURNEYS.md, EPICs

## Navigation by Category

**Unit Tests** (TEST-001 to TEST-099):

- [TEST-001](#test-001-test-name) - {Test name}

**Integration Tests** (TEST-101 to TEST-199):

- [TEST-101](#test-101-test-name) - {Test name}

**End-to-End Tests** (TEST-201 to TEST-299):

- [TEST-201](#test-201-test-name) - {Test name}

**Performance Tests** (TEST-301 to TEST-399):

- [TEST-301](#test-301-test-name) - {Test name}

**Security Tests** (TEST-401 to TEST-499):

- [TEST-401](#test-401-test-name) - {Test name}

---

## Coverage Targets

| Category    | Statement | Branch | Function | Line |
| ----------- | --------- | ------ | -------- | ---- |
| Core Logic  | ≥80%      | ≥75%   | ≥85%     | ≥80% |
| API Layer   | ≥80%      | ≥75%   | ≥85%     | ≥80% |
| UI Layer    | ≥70%      | ≥65%   | ≥75%     | ≥70% |
| Utilities   | ≥90%      | ≥85%   | ≥95%     | ≥90% |

---

## TEST-001: {Test Name}

**ID**: TEST-001
**Category**: Unit | Integration | E2E | Performance | Security
**Status**: Active | Deprecated | Planned
**Priority**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Test Description

{Clear description of what this test validates.}

### Prerequisites

- {Prerequisite 1}
- {Prerequisite 2}

### Test Steps (Given-When-Then)

**Given**: {Initial state or preconditions}

**When**: {Action or trigger}

**Then**: {Expected outcome}

### Validates

- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule being tested}
- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {API contract being tested}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {User journey being tested}

### Implementation

**File**: `{path/to/test/file.test.ts}`
**Test Suite**: {Suite name}

```typescript
// @implements TEST-001
describe('{Test Suite}', () => {
  it('{Test description}', () => {
    // Test implementation
  });
});
```

### Edge Cases

| Case              | Input       | Expected Output | Status  |
| ----------------- | ----------- | --------------- | ------- |
| {Edge case name}  | {Input}     | {Output}        | Covered |

---

## Test Execution Commands

```bash
# Run all tests
npm test

# Run specific category
npm test -- --grep "TEST-0"    # Unit tests
npm test -- --grep "TEST-1"    # Integration tests
npm test -- --grep "TEST-2"    # E2E tests

# Run with coverage
npm test -- --coverage
```

---

## Change Log

| Date       | ID       | Change        | Author  |
| ---------- | -------- | ------------- | ------- |
| YYYY-MM-DD | TEST-XXX | Created entry | {Agent} |
