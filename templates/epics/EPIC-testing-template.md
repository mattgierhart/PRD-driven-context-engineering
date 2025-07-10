---
version: 1.3
purpose: To define a comprehensive testing strategy for a project, covering unit, integration, end-to-end, and performance testing.
summary: Added progressive documentation features, model-specific guidance, and testing-first approach.
last_updated: 2025-07-06
epic_id: EPIC-04
epic_name: "{Project Name} Testing Strategy"
epic_type: "testing"
status: "planning"
model_restrictions: "none"
---

# EPIC-04: Testing - [Project Name] v{0.1}

## Epic Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Planning Version** | v0.1-0.3 (Opus) |
| **Execution Version** | v0.4+ (Sonnet) |
| **Last Updated** | [Date and Time] |
| **Last Editor** | [Model/User] |
| **Status** | Planning Phase |
| **Completion** | 0% |

## Version History
| Version | Date | Editor | Changes |
|---------|------|--------|---------|
| v0.1 | [Date] | [Editor] | Initial testing strategy |

## Quick Navigation
- [Overview](#overview)
- [Testing Philosophy](#testing-philosophy)
- [Test Framework Setup](#test-framework-setup)
- [Testing Standards](#testing-standards)
- [Test Categories](#test-categories)
- [Implementation Plan](#implementation-plan)
- [CI/CD Integration](#cicd-integration)
- [Progress Log](#progress-log)
- [Handoff History](#handoff-history)

**Authority**: See [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

## Overview
**Purpose**: Comprehensive testing strategy and implementation
**Test Coverage Target**: [80%+]
**Test Types**: Unit, Integration, E2E, Performance
**Created**: [Date]
**Last Updated**: [Date]

## Testing Philosophy

### Testing Pyramid
```
         /\
        /E2E\         <- 10% (Critical user flows)
       /------\
      /  Integ \      <- 20% (API & service tests)
     /----------\
    /    Unit    \    <- 70% (Component & function tests)
   /--------------\
```

### Core Principles
- **Fast Feedback**: Tests run in < 2 minutes
- **Reliable**: No flaky tests allowed
- **Maintainable**: Clear, simple test code
- **Valuable**: Test behavior, not implementation

## Test Framework Setup

### Technology Stack
```json
{
  "unit": {
    "framework": "Jest",
    "coverage": "Jest Coverage",
    "mocking": "Jest Mocks"
  },
  "integration": {
    "framework": "Jest + Supertest",
    "database": "Test containers"
  },
  "e2e": {
    "framework": "Playwright",
    "browsers": ["chromium", "firefox", "webkit"]
  },
  "performance": {
    "framework": "k6",
    "monitoring": "Lighthouse CI"
  }
}
```

### Configuration Files

#### Jest Configuration
```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  coveragePathIgnorePatterns: [
    '/node_modules/',
    '/tests/',
    '.d.ts$'
  ],
  setupFilesAfterEnv: ['<rootDir>/tests/setup.ts']
};
```

#### Playwright Configuration
```javascript
// playwright.config.ts
export default {
  testDir: './tests/e2e',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: process.env.TEST_URL || 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'mobile', use: { ...devices['iPhone 12'] } },
  ],
};
```

## Testing Standards {#testing-standards}
<!-- Model: opus for standards definition, sonnet for implementation -->

### Test Writing Guidelines
- **Arrange-Act-Assert** pattern for all tests
- **One assertion** per test when possible
- **Descriptive test names** that explain the behavior
- **No hardcoded values** - use fixtures and factories
- **Mock external dependencies** consistently

### Coverage Requirements
- **New features**: 90%+ coverage required
- **Bug fixes**: Must include regression tests
- **Refactoring**: Maintain or improve coverage
- **Critical paths**: 100% coverage mandatory

### Test Data Management
```typescript
// Use factories for consistent test data
const createTestUser = (overrides = {}) => ({
  id: 1,
  name: 'Test User',
  email: 'test@example.com',
  ...overrides
});
```

## Test Categories {#test-categories}

### 1. Unit Tests

#### Component Tests
```typescript
// __tests__/components/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from '@/components/Button';

describe('Button Component', () => {
  it('renders with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByText('Click me'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('applies disabled state', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByText('Click me')).toBeDisabled();
  });
});
```

#### Utility Function Tests
```typescript
// __tests__/utils/formatters.test.ts
import { formatCurrency, formatDate } from '@/utils/formatters';

describe('formatCurrency', () => {
  it('formats USD correctly', () => {
    expect(formatCurrency(1234.56)).toBe('$1,234.56');
    expect(formatCurrency(0)).toBe('$0.00');
    expect(formatCurrency(-100)).toBe('-$100.00');
  });

  it('handles different locales', () => {
    expect(formatCurrency(1234.56, 'EUR')).toBe('€1,234.56');
  });
});
```

### 2. Integration Tests

#### API Route Tests
```typescript
// __tests__/api/users.test.ts
import { createMocks } from 'node-mocks-http';
import handler from '@/pages/api/users';
import { prismaMock } from '@/tests/mocks/prisma';

describe('/api/users', () => {
  it('GET returns users list', async () => {
    const { req, res } = createMocks({
      method: 'GET',
    });

    prismaMock.user.findMany.mockResolvedValue([
      { id: 1, name: 'Test User', email: 'test@example.com' }
    ]);

    await handler(req, res);

    expect(res._getStatusCode()).toBe(200);
    expect(JSON.parse(res._getData())).toEqual({
      users: [{ id: 1, name: 'Test User', email: 'test@example.com' }]
    });
  });

  it('POST creates new user', async () => {
    const { req, res } = createMocks({
      method: 'POST',
      body: {
        name: 'New User',
        email: 'new@example.com'
      },
    });

    prismaMock.user.create.mockResolvedValue({
      id: 2,
      name: 'New User',
      email: 'new@example.com'
    });

    await handler(req, res);

    expect(res._getStatusCode()).toBe(201);
    expect(prismaMock.user.create).toHaveBeenCalledWith({
      data: {
        name: 'New User',
        email: 'new@example.com'
      }
    });
  });
});
```

#### Service Integration Tests
```typescript
// __tests__/services/stripe.test.ts
import { StripeService } from '@/services/stripe';
import Stripe from 'stripe';

jest.mock('stripe');

describe('StripeService', () => {
  let service: StripeService;
  let stripeMock: jest.Mocked<Stripe>;

  beforeEach(() => {
    stripeMock = new Stripe('') as jest.Mocked<Stripe>;
    service = new StripeService(stripeMock);
  });

  it('creates customer successfully', async () => {
    stripeMock.customers.create.mockResolvedValue({
      id: 'cus_123',
      email: 'test@example.com'
    } as Stripe.Customer);

    const customer = await service.createCustomer({
      email: 'test@example.com',
      name: 'Test User'
    });

    expect(customer.id).toBe('cus_123');
    expect(stripeMock.customers.create).toHaveBeenCalledWith({
      email: 'test@example.com',
      name: 'Test User'
    });
  });
});
```

### 3. End-to-End Tests

#### User Flow Tests
```typescript
// tests/e2e/auth-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication Flow', () => {
  test('user can sign up, log in, and log out', async ({ page }) => {
    // Sign up
    await page.goto('/signup');
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'SecurePass123!');
    await page.click('button[type="submit"]');
    
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('h1')).toContainText('Welcome');

    // Log out
    await page.click('button:has-text("Log out")');
    await expect(page).toHaveURL('/login');

    // Log in
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'SecurePass123!');
    await page.click('button[type="submit"]');
    
    await expect(page).toHaveURL('/dashboard');
  });
});
```

#### Critical Path Tests
```typescript
// tests/e2e/purchase-flow.spec.ts
test('complete purchase flow', async ({ page }) => {
  // Login
  await page.goto('/login');
  await loginUser(page, 'customer@example.com', 'password');

  // Browse products
  await page.goto('/products');
  await page.click('text=Premium Plan');
  
  // Add to cart
  await page.click('button:has-text("Add to Cart")');
  await expect(page.locator('.cart-count')).toHaveText('1');

  // Checkout
  await page.goto('/checkout');
  await page.fill('[name="cardNumber"]', '4242424242424242');
  await page.fill('[name="expiry"]', '12/25');
  await page.fill('[name="cvc"]', '123');
  
  await page.click('button:has-text("Complete Purchase")');
  
  // Verify success
  await expect(page).toHaveURL('/order-confirmation');
  await expect(page.locator('h1')).toContainText('Order Confirmed');
});
```

### 4. Performance Tests

#### Load Testing
```javascript
// tests/performance/load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 }, // Ramp up
    { duration: '5m', target: 100 }, // Stay at 100 users
    { duration: '2m', target: 0 },   // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests under 500ms
    http_req_failed: ['rate<0.1'],    // Error rate under 10%
  },
};

export default function () {
  const res = http.get('https://api.example.com/products');
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  
  sleep(1);
}
```

## Test Data Management

### Fixtures
```typescript
// tests/fixtures/users.ts
export const testUsers = {
  admin: {
    id: '1',
    email: 'admin@example.com',
    name: 'Admin User',
    role: 'ADMIN'
  },
  customer: {
    id: '2',
    email: 'customer@example.com',
    name: 'Test Customer',
    role: 'USER'
  }
};
```

### Database Seeding
```typescript
// tests/helpers/seed.ts
export async function seedTestDatabase() {
  await prisma.user.createMany({
    data: [testUsers.admin, testUsers.customer]
  });
  
  await prisma.product.createMany({
    data: testProducts
  });
}

export async function cleanupDatabase() {
  await prisma.$transaction([
    prisma.order.deleteMany(),
    prisma.product.deleteMany(),
    prisma.user.deleteMany(),
  ]);
}
```

## Continuous Integration

### GitHub Actions Workflow
```yaml
# .github/workflows/test.yml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - run: npm ci
      - run: npm run test:unit
      - run: npm run test:integration
      - run: npx playwright install
      - run: npm run test:e2e
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info
```

## Test Debugging

### Debug Commands
```bash
# Run specific test file
npm test -- Button.test.tsx

# Run tests in watch mode
npm test -- --watch

# Debug with breakpoints
node --inspect-brk ./node_modules/.bin/jest --runInBand

# Run E2E tests with UI
npx playwright test --ui

# Generate E2E test report
npx playwright show-report
```

### Common Issues

#### Flaky Tests
- Add explicit waits for async operations
- Mock external dependencies
- Use stable test data
- Increase timeouts for CI

#### Slow Tests
- Mock heavy operations
- Use test databases
- Parallelize test runs
- Skip expensive setup

## Test Metrics

### Coverage Goals
- **Statements**: 80%+
- **Branches**: 80%+
- **Functions**: 80%+
- **Lines**: 80%+

### Key Metrics
- Test execution time
- Flakiness rate
- Coverage trends
- Test maintenance cost

## Sub-Agent Commands

### Test Generation
```bash
@test-gen src/ --coverage 80
@test-gen src/api/ --integration-tests
@test-gen src/components/ --snapshot-tests
```

### Test Analysis
```bash
@tech-debt-finder-fixer tests/ --find-duplicates
@refactor tests/ --extract-helpers
@arch-review tests/ --check-patterns
```

## Best Practices

### Do's
- Write tests first (TDD)
- Test behavior, not implementation
- Keep tests simple and focused
- Use descriptive test names
- Mock external dependencies

### Don'ts
- Don't test framework code
- Don't write brittle selectors
- Don't share state between tests
- Don't ignore flaky tests
- Don't skip error cases

## Success Criteria
- [ ] 80%+ code coverage
- [ ] All tests pass in CI
- [ ] < 2 minute test suite
- [ ] Zero flaky tests
- [ ] Comprehensive E2E coverage

## Implementation Plan {#implementation-plan}
<!-- Model: opus for test strategy, sonnet for test implementation -->

### Test Implementation Tasks
<!-- Tasks will be added here during planning phase -->

### Task Template
```markdown
#### Task [ID] - [Task Title]
*   **Status:** `To Do` | `In Progress` | `Done` | `Blocked` | `blocked-for-opus` | `blocked-for-user`
*   **Model Suitability:** `opus-only` | `sonnet-ready` | `either`
*   **User Action Required:** [If blocked-for-user, specify what's needed: test data, access to services, decisions on test scope, etc.]
*   **Context:** [Why this task is necessary]
*   **Action Plan:** [What needs to be done]
*   **Validation:** [How to verify completion]
```

## CI/CD Integration {#cicd-integration}
<!-- CI/CD workflow documented in code samples above -->

## Progress Log {#progress-log}
<!-- APPEND new entries, don't replace -->
- [Date]: Testing strategy defined
- [Date]: Unit test framework configured
- [Date]: Integration test setup complete
- [Date]: E2E test suite operational
- [Date]: CI/CD pipeline integrated

## Handoff History {#handoff-history}
<!-- Track model transitions and blockers -->

<!-- HANDOFF: From [Model] to [Model] - [Date] -->
<!-- Summary of what was completed and what needs attention -->
<!-- END HANDOFF -->

## Gemini's Development Considerations
<!-- This section will be added by Gemini during review -->
<!-- Do not edit this section unless you are Gemini -->

---
*Template Version: 1.3*