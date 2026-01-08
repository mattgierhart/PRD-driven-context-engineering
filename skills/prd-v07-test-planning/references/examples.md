# Test Planning Examples

## Complete Test Suite for Auth EPIC

### API Tests

```
TEST-001: Signup succeeds with valid data
Type: Integration
Tests: API-001 (POST /auth/signup)
EPIC: EPIC-01

Given: No user with email "new@example.com" exists
When: POST /auth/signup with { email: "new@example.com", password: "SecurePass123!" }
Then:
  - Status: 201 Created
  - Body: { user: { id, email }, session: { token } }
  - User record created in DBT-010
  - Password stored as hash, not plaintext

Validation Method: Automated
Automation: tests/api/auth/signup.test.ts
Priority: Critical
```

```
TEST-002: Signup fails with existing email
Type: Integration
Tests: API-001, BR-001 (email uniqueness)
EPIC: EPIC-01

Given: User with email "existing@example.com" exists
When: POST /auth/signup with { email: "existing@example.com", password: "Pass123!" }
Then:
  - Status: 409 Conflict
  - Body: { error: { code: "EMAIL_EXISTS" } }
  - No new user record created

Validation Method: Automated
Automation: tests/api/auth/signup.test.ts
Priority: Critical
```

```
TEST-003: Signup fails with weak password
Type: Integration
Tests: API-001, BR-002 (password requirements)
EPIC: EPIC-01

Given: No preconditions
When: POST /auth/signup with { email: "new@example.com", password: "weak" }
Then:
  - Status: 400 Bad Request
  - Body: { error: { code: "WEAK_PASSWORD", details: [...] } }
  - No user record created

Validation Method: Automated
Automation: tests/api/auth/signup.test.ts
Priority: High
```

```
TEST-004: Login succeeds with valid credentials
Type: Integration
Tests: API-002 (POST /auth/login)
EPIC: EPIC-01

Given: User exists with email "user@example.com" and password "Pass123!"
When: POST /auth/login with { email: "user@example.com", password: "Pass123!" }
Then:
  - Status: 200 OK
  - Body: { session: { token, expiresAt } }
  - Session record created in DBT-011

Validation Method: Automated
Automation: tests/api/auth/login.test.ts
Priority: Critical
```

```
TEST-005: Login fails with wrong password
Type: Integration
Tests: API-002
EPIC: EPIC-01

Given: User exists with email "user@example.com"
When: POST /auth/login with { email: "user@example.com", password: "WrongPass!" }
Then:
  - Status: 401 Unauthorized
  - Body: { error: { code: "INVALID_CREDENTIALS" } }
  - No session created

Validation Method: Automated
Automation: tests/api/auth/login.test.ts
Priority: Critical
```

### Business Rule Tests

```
TEST-010: Password requires minimum 8 characters
Type: Unit
Tests: BR-002 (password requirements)
EPIC: EPIC-01

Given: Password validation function
When: Validate "short"
Then: Returns { valid: false, errors: ["MIN_LENGTH"] }

Validation Method: Automated
Automation: tests/unit/password-validation.test.ts
Priority: High
```

```
TEST-011: Password requires uppercase letter
Type: Unit
Tests: BR-002
EPIC: EPIC-01

Given: Password validation function
When: Validate "alllowercase123"
Then: Returns { valid: false, errors: ["UPPERCASE_REQUIRED"] }

Validation Method: Automated
Automation: tests/unit/password-validation.test.ts
Priority: High
```

### E2E Journey Tests

```
TEST-020: Complete signup journey
Type: E2E
Tests: UJ-000 (onboarding)
EPIC: EPIC-01

Given: User is on the signup page
When:
  1. User enters email and password
  2. User clicks "Sign Up"
  3. User clicks verification link in email
  4. User completes profile setup
Then:
  - User is redirected to dashboard
  - Welcome message is displayed
  - User can access authenticated features
  - Analytics: signup_completed event tracked

Validation Method: Both
Automation: tests/e2e/onboarding.spec.ts
Priority: Critical
```

```
TEST-021: Password reset journey
Type: E2E
Tests: UJ-010 (password reset)
EPIC: EPIC-01

Given: User exists but forgot password
When:
  1. User clicks "Forgot Password"
  2. User enters email
  3. User clicks reset link in email
  4. User enters new password
Then:
  - User can login with new password
  - Old password no longer works
  - User receives confirmation email

Validation Method: Both
Automation: tests/e2e/password-reset.spec.ts
Priority: High
```

### Database Constraint Tests

```
TEST-030: Users table enforces email uniqueness
Type: Integration
Tests: DBT-010 (users)
EPIC: EPIC-01

Given: User with email "test@example.com" exists
When: Attempt to INSERT another user with same email
Then: Database throws unique constraint violation

Validation Method: Automated
Automation: tests/db/users.test.ts
Priority: Critical
```

```
TEST-031: Sessions table requires user_id
Type: Integration
Tests: DBT-011 (sessions)
EPIC: EPIC-01

Given: Sessions table exists
When: Attempt to INSERT session without user_id
Then: Database throws not null violation

Validation Method: Automated
Automation: tests/db/sessions.test.ts
Priority: High
```

---

## Anti-Pattern Examples

### Bad: Vague Test

```
TEST-001: Auth works
Type: Integration
Tests: API-001

Given: System is running
When: User signs up
Then: It works

Priority: High
```

**Problem**: "It works" is not testable. What does success look like?

### Bad: Test Without ID Link

```
TEST-001: Password must be strong
Type: Unit

Given: Password input
When: User enters password
Then: Password is validated

Priority: Medium
```

**Problem**: No link to BR-, API-, or UJ-. Orphaned test.

### Bad: Implementation Test

```
TEST-001: bcrypt.hash is called with correct salt rounds
Type: Unit
Tests: API-001

Given: Signup request
When: Password is hashed
Then: bcrypt.hash called with 12 rounds

Priority: High
```

**Problem**: Tests implementation details (bcrypt), not behavior. If we change hashing library, test breaks even if behavior is correct.

**Better:**
```
TEST-001: Password is stored securely
Type: Integration
Tests: API-001

Given: User signs up with password "Pass123!"
When: Query user record from database
Then: Stored password does NOT equal "Pass123!" (is hashed)
```
