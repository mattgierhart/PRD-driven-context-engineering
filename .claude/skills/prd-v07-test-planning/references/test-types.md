# Test Type Decision Guide

## Overview

| Type | Scope | Speed | Confidence | When to Use |
|------|-------|-------|------------|-------------|
| **Unit** | Single function | Fast (ms) | Low (isolated) | Business logic, utilities |
| **Integration** | Module + deps | Medium (s) | Medium | API endpoints, DB operations |
| **E2E** | Full system | Slow (min) | High | Critical user journeys |
| **Contract** | Interface | Fast | Medium | External API integration |
| **Performance** | Speed/load | Varies | N/A | Critical paths |

## When to Use Each Type

### Unit Tests

**Use for:**
- Pure functions (validators, formatters, calculators)
- Business rule logic (BR-)
- Utility functions

**Don't use for:**
- Database operations
- API endpoints
- UI interactions

**Example:**
```typescript
// Good unit test candidate
function validatePassword(password: string): ValidationResult {
  // Pure logic, no external dependencies
}

// TEST-001: validatePassword rejects short passwords
// TEST-002: validatePassword requires uppercase
```

### Integration Tests

**Use for:**
- API endpoints (API-)
- Database operations (DBT-)
- Service interactions

**Don't use for:**
- Pure logic (use unit tests)
- Full user flows (use E2E)

**Example:**
```typescript
// Good integration test candidate
POST /api/users → creates user in database

// TEST-010: POST /users creates record
// TEST-011: POST /users returns 409 for duplicate email
```

### E2E Tests

**Use for:**
- Critical user journeys (UJ-)
- Onboarding flows
- Purchase flows
- Key feature validation

**Don't use for:**
- Every possible path (too slow)
- Edge cases (use unit/integration)
- Internal implementation details

**Example:**
```
// Good E2E test candidate
UJ-000: Signup → Verify → Dashboard

// TEST-020: New user can complete signup and see dashboard
```

### Contract Tests

**Use for:**
- Third-party API integrations
- Service-to-service boundaries
- Schema validation

**Don't use for:**
- Internal APIs (use integration tests)
- Logic testing (use unit tests)

**Example:**
```
// Good contract test candidate
Stripe webhook payload structure

// TEST-030: Stripe webhook matches expected schema
```

### Performance Tests

**Use for:**
- Critical path latency (API response time)
- Database query performance
- Load testing before launch

**Don't use for:**
- MVP (usually premature)
- Non-critical paths

**Example:**
```
// Good performance test candidate
API-010: GET /reports list

// TEST-040: /reports returns in <200ms for 1000 records
```

## Test Pyramid

```
                    ┌─────────┐
                    │   E2E   │  Few, slow, high confidence
                    │  Tests  │
                    └────┬────┘
                         │
               ┌─────────┴─────────┐
               │    Integration    │  Some, medium speed
               │       Tests       │
               └─────────┬─────────┘
                         │
          ┌──────────────┴──────────────┐
          │         Unit Tests          │  Many, fast, focused
          └─────────────────────────────┘
```

**Rule of thumb for MVP:**
- 60% Unit tests
- 30% Integration tests
- 10% E2E tests

## Decision Tree

```
Is it a pure function with no external dependencies?
├── Yes → Unit Test
└── No ↓

Does it involve database or external service?
├── Yes → Integration Test
└── No ↓

Is it a complete user journey?
├── Yes → E2E Test
└── No ↓

Is it about API shape/contract?
├── Yes → Contract Test
└── No ↓

Is it about speed/load?
├── Yes → Performance Test
└── No → Probably don't need a test for this
```

## Practical Examples

### Scenario: User Signup Feature

```
┌────────────────────────────────────────────────────┐
│                    E2E (1 test)                    │
│  TEST-020: Complete signup journey                 │
│    User can sign up → verify email → see dashboard │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│              Integration (5 tests)                 │
│  TEST-001: POST /signup succeeds                   │
│  TEST-002: POST /signup fails duplicate email      │
│  TEST-003: POST /signup fails weak password        │
│  TEST-004: User record created in DB               │
│  TEST-005: Welcome email sent                      │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│                  Unit (8 tests)                    │
│  TEST-010: validateEmail accepts valid email       │
│  TEST-011: validateEmail rejects invalid email     │
│  TEST-012: validatePassword min length             │
│  TEST-013: validatePassword requires uppercase     │
│  TEST-014: validatePassword requires number        │
│  TEST-015: hashPassword returns hash               │
│  TEST-016: hashPassword is not reversible          │
│  TEST-017: generateVerificationToken unique        │
└────────────────────────────────────────────────────┘
```

Total: 14 tests for one feature
- 8 unit (fast, focused)
- 5 integration (thorough)
- 1 E2E (confidence)
