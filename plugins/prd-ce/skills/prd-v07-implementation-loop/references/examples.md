# Implementation Loop Examples

## Complete Implementation Session

### Starting State
```markdown
## 0. Session State
- **Last Action**: Completed Window 1 (Database Schema)
- **Stopping Point**: Ready to start API-001
- **Next Steps**: Implement API-001 (signup endpoint)
- **Context**: Schema approved, RLS working
```

### Session Execution

**Step 1: Load Context**
```
Read EPIC-01
Review API-001 specification:
  - POST /api/auth/signup
  - Body: { email, password }
  - Returns: { user, session }
  - Enforces: BR-001, BR-002
```

**Step 2: Write Test (Red)**
```typescript
// tests/api/auth/signup.test.ts
// @tests TEST-001

import { describe, it, expect, beforeEach } from 'vitest';
import { createTestClient, resetDatabase } from '../helpers';

describe('POST /api/auth/signup', () => {
  beforeEach(async () => {
    await resetDatabase();
  });

  // @tests TEST-001
  it('creates user with valid credentials', async () => {
    const client = createTestClient();

    const response = await client.post('/api/auth/signup').send({
      email: 'new@example.com',
      password: 'ValidPass123!',
    });

    expect(response.status).toBe(201);
    expect(response.body.data.user.email).toBe('new@example.com');
    expect(response.body.data.session.token).toBeDefined();
  });

  // @tests TEST-002
  it('rejects duplicate email', async () => {
    const client = createTestClient();

    // Create first user
    await client.post('/api/auth/signup').send({
      email: 'existing@example.com',
      password: 'ValidPass123!',
    });

    // Attempt duplicate
    const response = await client.post('/api/auth/signup').send({
      email: 'existing@example.com',
      password: 'DifferentPass456!',
    });

    expect(response.status).toBe(409);
    expect(response.body.error.code).toBe('EMAIL_EXISTS');
  });

  // @tests TEST-003
  it('rejects weak password', async () => {
    const client = createTestClient();

    const response = await client.post('/api/auth/signup').send({
      email: 'new@example.com',
      password: 'weak',
    });

    expect(response.status).toBe(400);
    expect(response.body.error.code).toBe('WEAK_PASSWORD');
  });
});
```

**Step 3: Run Test (Verify Red)**
```bash
npm test -- signup.test.ts

# Output:
# ✗ creates user with valid credentials (404 Not Found)
# ✗ rejects duplicate email (404 Not Found)
# ✗ rejects weak password (404 Not Found)
```

**Step 4: Implement (Green)**
```typescript
// src/api/auth/signup.ts
// @implements API-001 (POST /api/auth/signup)
// @see BR-001 (email uniqueness)
// @see BR-002 (password requirements)
// @see DBT-001 (users table)

import { NextRequest, NextResponse } from 'next/server';
import { db } from '@/lib/db';
import { hashPassword } from '@/lib/auth';
import { validatePassword } from '@/lib/validation';

export async function POST(request: NextRequest) {
  const body = await request.json();
  const { email, password } = body;

  // @implements BR-002 (password requirements)
  const passwordValidation = validatePassword(password);
  if (!passwordValidation.valid) {
    return NextResponse.json(
      { error: { code: 'WEAK_PASSWORD', details: passwordValidation.errors } },
      { status: 400 }
    );
  }

  // @implements BR-001 (email uniqueness)
  const existingUser = await db.users.findByEmail(email);
  if (existingUser) {
    return NextResponse.json(
      { error: { code: 'EMAIL_EXISTS' } },
      { status: 409 }
    );
  }

  // @implements DBT-001 (create user record)
  const user = await db.users.create({
    email,
    passwordHash: await hashPassword(password),
  });

  // Create session
  const session = await db.sessions.create({ userId: user.id });

  return NextResponse.json(
    {
      data: {
        user: { id: user.id, email: user.email },
        session: { token: session.token },
      },
    },
    { status: 201 }
  );
}
```

**Step 5: Run Test (Verify Green)**
```bash
npm test -- signup.test.ts

# Output:
# ✓ creates user with valid credentials
# ✓ rejects duplicate email
# ✓ rejects weak password
```

**Step 6: Update Session State**
```markdown
## 0. Session State
- **Last Action**: Completed API-001 (signup endpoint), tests passing
- **Stopping Point**: src/api/auth/signup.ts complete
- **Next Steps**:
  1. Implement API-002 (login endpoint)
  2. Add TEST-004, TEST-005 for login
- **Context**: Used NextResponse for consistency with app router
```

---

## Traceability in Practice

### Before (No Traceability)
```typescript
// Bad: No one knows what this implements or why
export async function handler(req, res) {
  if (req.body.password.length < 8) {
    return res.status(400).json({ error: 'Bad password' });
  }
  // ... rest of code
}
```

### After (Full Traceability)
```typescript
// @implements API-001 (POST /users)
// @see BR-002 (password requirements)
export async function handler(req, res) {
  // @implements BR-002 (minimum 8 characters)
  if (req.body.password.length < 8) {
    return res.status(400).json({
      error: { code: 'WEAK_PASSWORD', details: ['MIN_LENGTH'] }
    });
  }
  // ... rest of code
}
```

**Benefits:**
- Code reviewer knows to check BR-002 spec
- Future maintainer understands why 8 chars
- Test knows to verify this case
- Spec update reminds to update code

---

## SoT Update During Implementation

### Scenario: Discovered Edge Case

During implementation of API-001, you realize:
- Spec didn't mention email normalization
- Some emails have trailing spaces

**Don't**: Ignore it and hope it works
**Don't**: Fix in code without updating spec

**Do**: Update spec AND code together

```markdown
# Update to SoT/SoT.API_CONTRACTS.md

API-001: POST /users
...
Request:
  Body:
    email: string — User email (normalized: lowercase, trimmed)
...
```

```typescript
// @implements API-001 (email normalization)
const normalizedEmail = email.toLowerCase().trim();
```

Add TEST- entry:
```markdown
TEST-007: Email is normalized before storage
Given: Signup with email " User@Example.COM "
When: POST /api/users
Then: Email stored as "user@example.com"
```

---

## Handling Blockers

### Scenario: Test Can't Be Written

```
Trying to write TEST-015 for API-005 (export report)
Problem: Unclear what file format should be exported
```

**Action:**
1. **Don't guess** — This creates spec drift
2. **Update Session State** with blocker:
   ```markdown
   - **Context**: BLOCKED on TEST-015 — need clarity on export format
     Options: PDF, CSV, or both?
     Awaiting decision from [stakeholder]
   ```
3. **Move to different task** in same Context Window if possible
4. **Escalate** if it blocks the entire Window

### Scenario: Implementation Reveals Wrong Spec

```
API-003 spec says: PUT /users/:id (full replace)
Implementation reality: Should be PATCH (partial update)
```

**Action:**
1. Stop implementation
2. Update spec:
   ```markdown
   API-003: Update User (REVISED)
   Method: PATCH (changed from PUT)
   Rationale: Partial updates more common, safer
   ```
3. Update TEST- entries to reflect PATCH
4. Continue implementation
5. Note in Session State:
   ```markdown
   - **Context**: Changed API-003 from PUT to PATCH per [reasoning]
   ```
