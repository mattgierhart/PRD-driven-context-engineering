---
version: 1.0
purpose: Source of Truth file for test cases and validation scenarios. Each test has a unique ID for cross-referencing.
id_prefix: TEST-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by EPICs, APIs, user journeys, and business rules
---

# Testing Playbook (SoT File)

> **Purpose**: Complete specifications for all test cases and validation scenarios.
> **ID Prefix**: TEST-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by API_CONTRACTS.md, USER_JOURNEYS.md, BUSINESS_RULES.md, EPICs

## Navigation by Category

**Unit Tests** (TEST-001 to TEST-099):
- [TEST-001](#test-001-test-name) - {Test name}
- [TEST-002](#test-002-test-name) - {Test name}

**Integration Tests** (TEST-101 to TEST-199):
- [TEST-101](#test-101-test-name) - {Test name}
- [TEST-102](#test-102-test-name) - {Test name}

**E2E Tests** (TEST-201 to TEST-299):
- [TEST-201](#test-201-test-name) - {Test name}

**Performance Tests** (TEST-301 to TEST-399):
- [TEST-301](#test-301-test-name) - {Test name}

**Security Tests** (TEST-401 to TEST-499):
- [TEST-401](#test-401-test-name) - {Test name}

---

## TEST-001: {Test Name}

**ID**: TEST-001
**Category**: Unit | Integration | E2E | Performance | Security
**Status**: Active | Deprecated | Planned
**Priority**: Critical | High | Medium | Low
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Owner**: QA Team | Engineering

### Test Specification

**Given**: {Initial state and preconditions}
**When**: {Action or trigger}
**Then**: {Expected outcome}

**Test Type**: {Unit/Integration/E2E/Performance/Security}
**Test Framework**: {Jest/Playwright/Cypress/k6/etc.}

### Test Implementation

**File Location**: `tests/{category}/{test-file}.test.ts`

**Test Code**:
```typescript
describe('TEST-001: {Test Name}', () => {
  it('should {expected behavior}', async () => {
    // Arrange
    const {setup} = await setupTestContext();

    // Act
    const result = await performAction(setup);

    // Assert
    expect(result).toBe(expectedValue);
  });

  it('should handle error case', async () => {
    // Test error scenarios
  });
});
```

### Related IDs

**Validates APIs**:
- [API-XXX](API_CONTRACTS.md#api-xxx) - {API endpoint being tested}
- [API-YYY](API_CONTRACTS.md#api-yyy) - {Another API}

**Validates Business Rules**:
- [BR-XXX](BUSINESS_RULES.md#br-xxx) - {Business rule being validated}
- [BR-YYY](BUSINESS_RULES.md#br-yyy) - {Another rule}

**Validates User Journeys**:
- [UJ-XXX](USER_JOURNEYS.md#uj-xxx) - {User journey being tested}
- [UJ-YYY](USER_JOURNEYS.md#uj-yyy) - {Another journey}

**Tests Database Operations**:
- [DBT-XXX](ACTUAL_SCHEMA.md#dbt-xxx) - {Table being tested}

**Part of Test Suite**:
- [TEST-XXX](#test-xxx-related-test) - {Related test}

**Referenced by EPICs**:
- [EPIC-XX](epics/EPIC-XX-{name}.md) - {EPIC that requires this test}

### Test Data

**Required Test Data**:
- Test User: `test-user-001@example.com`
- Test Product: `prod_test_abc123`
- Test Subscription: `sub_test_xyz789`

**Golden Dataset**: `tests/fixtures/golden-dataset.json`

**Mock Data**:
```json
{
  "userId": "test_user_123",
  "productId": "test_prod_456",
  "quantity": 1
}
```

### Success Criteria

- [ ] All assertions pass
- [ ] No console errors or warnings
- [ ] Test runs in <{X}ms
- [ ] Code coverage maintained at >{Y}%
- [ ] No flaky test behavior (100% pass rate over 10 runs)

### Failure Scenarios

**Scenario 1**: {Error condition}
- Expected Behavior: {What should happen}
- Error Message: `{Expected error message}`
- Recovery: {How to handle}

**Scenario 2**: {Edge case}
- Expected Behavior: {What should happen}
- Validation: {How to verify}

### Performance Expectations

**Execution Time**: <{X} seconds
**Resource Usage**: <{Y} MB memory
**Timeout**: {Z} seconds

### Maintenance Notes

**Dependencies**: {External services or mocks required}
**Environment Variables**: `TEST_API_KEY`, `TEST_DATABASE_URL`
**Known Issues**: {Any known flaky behavior or limitations}

### Test Manifest Integration

This test is tracked in `TEST_MANIFEST.md`:

```markdown
| TEST-001 | {Test Name} | Unit | ✅ Passing | 2025-11-09 |
```

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | YYYY-MM-DD | Initial test | {Name} |
| 1.1 | YYYY-MM-DD | Added edge case coverage | {Name} |

---

## TEST-002: {Next Test Name}

{Repeat the above structure for each test}

---

## Test Coverage Gates

### Coverage Targets

| Category | Target | Current | Status |
|----------|--------|---------|--------|
| Unit Tests | >80% | {X}% | ✅/⚠️/❌ |
| Integration Tests | >70% | {Y}% | ✅/⚠️/❌ |
| E2E Tests | Critical paths | {Z}% | ✅/⚠️/❌ |
| Business Rules | 100% | {W}% | ✅/⚠️/❌ |

### Gate Requirements

**Phase D: Testing Gate**:
- [ ] All critical tests passing (TEST-XXX priority: Critical)
- [ ] Unit test coverage ≥80%
- [ ] Integration test coverage ≥70%
- [ ] All business rules validated (BR-XXX)
- [ ] All user journeys tested (UJ-XXX)
- [ ] No P0/P1 test failures

---

## Test Execution Protocol

### Running Tests

**All Tests**:
```bash
npm test
```

**By Category**:
```bash
npm run test:unit        # Unit tests only
npm run test:integration # Integration tests only
npm run test:e2e         # E2E tests only
npm run test:security    # Security tests only
npm run test:performance # Performance tests only
```

**By Priority**:
```bash
npm run test:critical    # Critical priority tests
npm run test:smoke       # Smoke test suite
```

**With Coverage**:
```bash
npm run test:coverage    # Generate coverage report
```

### Continuous Integration

**On Every PR**:
- Run all unit tests
- Run integration tests for changed modules
- Generate coverage report
- Block merge if coverage drops

**On Merge to Main**:
- Run full test suite
- Run E2E tests
- Run security scan
- Deploy to staging if all pass

---

## Cross-Reference Index

> **Auto-Generated Section**: Run `npm run codex:sync-registry` to rebuild

**Tests by API**:
- API-001 validated by: TEST-001, TEST-045, TEST-102
- API-002 validated by: TEST-002, TEST-046

**Tests by User Journey**:
- UJ-101 validated by: TEST-201, TEST-202, TEST-203
- UJ-102 validated by: TEST-204

**Tests by Business Rule**:
- BR-001 validated by: TEST-001, TEST-005
- BR-112 validated by: TEST-046

**Tests by Priority**:
- Critical: TEST-001, TEST-045, TEST-201
- High: TEST-002, TEST-046, TEST-202
- Medium: TEST-003, TEST-047

---

## Update Protocol

### When to Add New TEST-XXX IDs

1. **New API Endpoint**: Create test for each new API
2. **New Business Rule**: Create validation test for each rule
3. **New User Journey**: Create E2E test for each journey
4. **Bug Fix**: Create regression test for each bug
5. **Performance SLA**: Create performance test for each target

### Bidirectional Reference Checklist

When adding a new TEST-XXX:
- [ ] Update API_CONTRACTS.md "Validated By Tests" section for APIs tested
- [ ] Update USER_JOURNEYS.md "Validated By" section for journeys tested
- [ ] Update BUSINESS_RULES.md "Validated By Tests" section for rules tested
- [ ] Update TEST_MANIFEST.md with new test entry
- [ ] Update EPIC Section 3A "IDs Created This EPIC" table
- [ ] Update README.md "Active IDs" section if part of current work
- [ ] Add test file to appropriate directory (`tests/{category}/`)
- [ ] Run `npm run codex:sync-registry` to update ID_REGISTRY.md

---

*End of testing_playbook.md - This SoT file is the authoritative source for all TEST-XXX IDs*
