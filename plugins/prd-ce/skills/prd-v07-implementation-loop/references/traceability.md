# Traceability Patterns Guide

## Why Traceability Matters

Traceability connects code to requirements. It answers:
- "Why does this code exist?" → Links to FEA-, BR-
- "What spec does this implement?" → @implements API-, DBT-
- "What tests verify this?" → @tests TEST-
- "What else is affected if I change this?" → @see references

## Tag Syntax

### Primary Tags

```typescript
// @implements [ID] ([description])
// @implements API-001 (Create user endpoint)
// @implements BR-002 (Password minimum length)
// @implements DBT-001 (Users table schema)
```

### Reference Tags

```typescript
// @see [ID]
// @see BR-001, BR-002
// @see API-001
```

### Test Tags

```typescript
// @tests [ID]
// @tests TEST-001, TEST-002
```

## Where to Place Tags

### API Handlers

```typescript
// @implements API-001 (POST /users)
// @see BR-001 (email uniqueness)
// @see BR-002 (password requirements)
// @see DBT-001 (users table)
export async function createUser(req: Request): Promise<Response> {
```

### Business Logic Functions

```typescript
// @implements BR-002 (password requirements)
export function validatePassword(password: string): ValidationResult {
```

### Database Models/Migrations

```sql
-- @implements DBT-001 (users table)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  -- @implements BR-001 (email uniqueness via UNIQUE constraint)
```

### UI Components

```typescript
// @implements SCR-001 (Dashboard screen)
// @see UJ-001 (first value journey)
export function Dashboard() {
```

### Test Files

```typescript
// @tests TEST-001 (user creation succeeds)
// @tests TEST-002 (duplicate email rejected)
describe('POST /api/users', () => {
```

## Granularity Guidelines

### File Level
Place at the top of file for the primary ID:

```typescript
// @implements API-001 (Create user endpoint)

import { ... }

export async function handler() { ... }
```

### Function Level
Place above function for major logic:

```typescript
// @implements BR-005 (rate limiting)
export function rateLimiter(req: Request): boolean {
```

### Block Level
Place inline for specific rule enforcement:

```typescript
export async function createUser(req: Request) {
  // @implements BR-002 (password validation)
  if (!isValidPassword(password)) {
    return error;
  }

  // @implements BR-001 (email uniqueness check)
  if (await emailExists(email)) {
    return error;
  }
}
```

## Multi-ID Traceability

When code implements multiple IDs:

```typescript
// @implements API-001 (Create user)
// @implements BR-001 (email uniqueness)
// @implements BR-002 (password requirements)
// @see DBT-001, DBT-002
export async function createUser(req: Request) {
```

When code is shared by multiple APIs:

```typescript
// @see API-001, API-002, API-003 (shared auth middleware)
// @implements BR-010 (authentication required)
export function authMiddleware(req: Request) {
```

## Traceability Matrix

Maintain this in your head (or a doc) while implementing:

| Code | Implements | Tested By |
|------|------------|-----------|
| `createUser()` | API-001, BR-001, BR-002 | TEST-001–003 |
| `validatePassword()` | BR-002 | TEST-010–015 |
| `users` table | DBT-001 | TEST-030 |
| `Dashboard` | SCR-001 | TEST-050 |

## Tooling Suggestions

### Search for Implementation
```bash
# Find all code implementing a specific ID
grep -r "@implements API-001" src/
```

### Find Untested Code
```bash
# Find @implements without corresponding @tests
grep -r "@implements" src/ | cut -d: -f1 | sort -u > implemented.txt
grep -r "@tests" tests/ | grep -oP "TEST-\d+" | sort -u > tested.txt
# Compare to find gaps
```

### Generate Coverage Report
```bash
# Find all IDs mentioned in code
grep -rhoP "(API|BR|DBT|TEST|SCR)-\d+" src/ tests/ | sort | uniq -c | sort -rn
```

## Anti-Patterns

### No Tags
```typescript
// Bad: No one knows what this does or why
export function validate(input) {
  return input.length >= 8;
}
```

### Wrong Tags
```typescript
// Bad: Tag doesn't match actual implementation
// @implements API-001 (Create user)
export function deleteUser() { ... }
```

### Over-Tagging
```typescript
// Bad: Every line tagged (noise)
// @implements BR-001
const a = 1;
// @implements BR-001
const b = 2;
// @implements BR-001
return a + b;
```

### Stale Tags
```typescript
// Bad: Tag references deleted ID
// @implements API-099 (This API was removed in v2)
export function handler() { ... }
```

## Keeping Tags Updated

When you change code:
1. Check existing tags — still accurate?
2. If functionality changed — update tag
3. If ID was deprecated — remove tag, add note
4. If new functionality — add new tag

When you change specs:
1. Search for tags referencing changed ID
2. Update code to match new spec
3. Update tests if behavior changed
