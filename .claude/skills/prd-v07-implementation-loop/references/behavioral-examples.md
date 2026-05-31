# Behavioral Examples: Good vs. Bad AI Coding Patterns

> Derived from common AI coding failure modes, adapted to the PRD-driven SoT/ID system.
> Each example shows how the ID system makes behavioral discipline auditable.

## 1. Think Before Coding — Assumption Drift

**Scenario**: API-001 spec says "returns user object." Agent needs to implement the endpoint.

**BAD**: Agent invents response fields
```typescript
// @implements API-001
export async function getUser(req, res) {
  const user = await db.users.findById(req.params.id);
  return res.json({
    id: user.id,
    email: user.email,
    name: user.name,
    avatar: user.avatar,       // Not in any spec
    preferences: user.prefs,   // Not in any spec
    lastLogin: user.lastLogin, // Not in any spec
  });
}
```
The agent silently assumed which fields "user object" includes. These fields may not exist in DBT-010.

**GOOD**: Agent checks spec, finds gap, logs it
```typescript
// @implements API-001
// Fields: id, email confirmed in DBT-010. "name" not in schema — see Assumptions table #3.
export async function getUser(req, res) {
  const user = await db.users.findById(req.params.id);
  return res.json({ id: user.id, email: user.email });
}
```
Assumptions & Ambiguities table entry:
```
| 3 | API-001 | AMBIGUITY | "user object" fields not enumerated | DBT-010 has id, email only | Implementing confirmed fields; spec needs update |
```

## 2. Simplicity First — Overbuilding

**Scenario**: TEST-001 requires "user creation succeeds with valid data."

**BAD**: Agent builds well beyond what any TEST- requires
```typescript
// @implements API-001
export async function createUser(req, res) {
  const sanitized = sanitizeInput(req.body);      // No TEST- for sanitization
  const rateLimited = await checkRateLimit(req);   // No TEST- for rate limiting
  if (!rateLimited) return res.status(429).json({});

  const user = await db.users.create(sanitized);
  await auditLog.record('USER_CREATED', user.id); // No TEST- for audit logging
  await analytics.track('signup', user.id);        // No TEST- for analytics

  return res.status(201).json({ data: user });
}
```
Four features built that no TEST- requires. Each is untested and unspecified.

**GOOD**: Agent writes minimum code to pass TEST-001
```typescript
// @implements API-001
export async function createUser(req, res) {
  const user = await db.users.create({
    email: req.body.email,
    passwordHash: await hashPassword(req.body.password),
  });
  return res.status(201).json({ data: { id: user.id, email: user.email } });
}
```
Rate limiting gets added later when TEST-012 (which tests BR-005) becomes the focus.

## 3. Surgical Changes — Drive-By Refactoring

**Scenario**: Implementing API-003 (logout). Agent notices issues in API-001 (signup).

**BAD**: Agent "improves" unrelated code
```diff
  // Changes to src/api/auth/signup.ts (NOT in current focus)
- var user = await db.users.create(req.body);
+ const user = await db.users.create(req.body);
+ /** Creates a new user account with the provided credentials. */

  // Changes to src/utils/helpers.ts (NOT in current focus)
+ /**
+  * Formats a date string for display.
+  * @param date - The date to format
+  */

  // Changes to src/api/auth/logout.ts (actual focus)
  // @implements API-003
  export async function logout(req, res) { ... }
```
Three files touched. Only one traces to API-003. The diff is noisy and breaks traceability.

**GOOD**: Agent notes improvements, only touches focus area
```typescript
// src/api/auth/logout.ts — the ONLY file changed
// @implements API-003
export async function logout(req, res) {
  await db.sessions.delete({ userId: req.user.id });
  return res.status(200).json({ success: true });
}
```
Session State Context: "Noticed API-001 signup.ts uses `var` — consider updating in future session."

## 4. Goal-Driven Execution — Vague vs. Verifiable

**Scenario**: Ending a session. Agent updates Session State.

**BAD**: Vague completion claim
```markdown
- **Last Action**: Working on auth features
- **Stopping Point**: Somewhere in the auth code
- **Next Steps**: Continue with auth
- **Context**: Auth is mostly working, need to finish up some edge cases
```

**GOOD**: Specific, ID-referenced state
```markdown
- **Last Action**: Completed API-001 (signup) and API-002 (login). TEST-001 through TEST-005 PASS.
- **Stopping Point**: src/api/auth/reset.ts:85 — TEST-006 FAILS at line 42: expected 429 but got 200
- **Next Steps**:
  1. Implement rate limiter middleware per BR-005
  2. Make TEST-006 pass (rate limiting on password reset)
  3. Move to API-005 (verify email)
- **Context**: Using express-rate-limit with Redis per TECH-003. Decided 429 with Retry-After header per API-001 error spec.
```

## 5. Combined — Full Context Window Walkthrough

A complete Context Window session demonstrating all four principles together.

**Context**: EPIC-01, Window 2 (API Endpoints), focusing on API-002 (login).

**Step 1 — Load & Clarify** (Think Before Coding):
"This session implements API-002 (POST /auth/login). TEST-003 and TEST-004 define acceptance. BR-001 (email uniqueness) and BR-002 (password requirements) constrain behavior."

**Step 2 — Red** (write failing test from TEST-003 spec):
```typescript
// @tests TEST-003
it('logs in with valid credentials', async () => {
  // Assertions derived from API-002 spec: status 200, returns token and user
  const res = await request(app).post('/auth/login').send({ email, password });
  expect(res.status).toBe(200);
  expect(res.body.data.token).toBeDefined();
});
```

**Step 3 — Green** (minimum code to pass — Simplicity First):
```typescript
// @implements API-002
export async function login(req, res) {
  const user = await db.users.findByEmail(req.body.email);
  if (!user || !await verifyPassword(req.body.password, user.passwordHash)) {
    return res.status(401).json({ error: { code: 'INVALID_CREDENTIALS' } });
  }
  const token = generateToken(user.id);
  return res.json({ data: { token, user: { id: user.id, email: user.email } } });
}
```

**Step 4 — Tag & Update** (Surgical Changes — only touch what API-002 requires):
- `@implements API-002` tag added
- `@see BR-002` cross-reference added
- SoT not updated (spec matches implementation)
- No changes to API-001, API-003, or any other file

**Step 5 — Validate** (Goal-Driven — cite specific IDs):
"TEST-003 PASS. TEST-004 PASS. API-002 implementation complete. Moving to API-003."
