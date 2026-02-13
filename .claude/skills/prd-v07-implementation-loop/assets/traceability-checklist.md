# Traceability Checklist

Use this checklist before marking a Context Window or EPIC as complete.

---

## Per-Function Checklist

For each major code unit (function, class, component, route handler):

- [ ] Has `// @implements [ID]` tag declaring what spec it fulfills
- [ ] Has `// @see [ID]` tags for related specs it references
- [ ] The ID exists in SoT/ and is current
- [ ] Test coverage exists for the ID (`// @tests TEST-XXX`)

---

## Tag Reference

| Code Element | Tag Pattern | Example |
|--------------|-------------|---------|
| API handler | `@implements API-XXX` | Route function |
| Business logic | `@implements BR-XXX` | Validation, rules |
| Database model | `@implements DBT-XXX` | Schema, model |
| UI component | `@implements SCR-XXX` | Screen/page |
| Test file | `@tests TEST-XXX` | Test implementation |
| Cross-reference | `@see [ID]` | Related spec |

---

## Placement Examples

### API Endpoint

```typescript
// @implements API-001 (POST /users)
// @see BR-001 (email uniqueness)
// @see BR-002 (password requirements)
// @see DBT-001 (users table)
export async function createUser(req: Request, res: Response) {
  // @implements BR-002
  const passwordResult = validatePassword(req.body.password);

  // @implements BR-001
  const existingUser = await db.users.findByEmail(req.body.email);

  // ...
}
```

### React Component

```tsx
// @implements SCR-003 (Dashboard Screen)
// @see UJ-002 (View Dashboard journey)
// @see BR-010 (data refresh rules)
export function Dashboard() {
  // ...
}
```

### Database Migration

```sql
-- @implements DBT-001 (Users table)
-- @see BR-001 (email uniqueness constraint)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,  -- BR-001
  -- ...
);
```

### Test File

```typescript
// @tests TEST-001, TEST-002, TEST-003
// @see API-001
describe('POST /api/users', () => {
  // @tests TEST-001
  it('creates user with valid data', async () => {
    // ...
  });
});
```

---

## Context Window Completion Checklist

Before marking a Context Window complete:

- [ ] All tasks in the window are done
- [ ] Every new function has `@implements` tags
- [ ] Related SoT entries are updated if spec changed
- [ ] Tests exist and pass for all TEST- entries in scope
- [ ] No orphaned code (code without ID linkage)
- [ ] Session State section updated

---

## EPIC Completion Checklist

Before marking EPIC complete:

- [ ] All Context Windows complete
- [ ] All TEST- entries for this EPIC pass
- [ ] Manual verification of relevant UJ- journeys done
- [ ] `@implements` tags present in all major code units
- [ ] No orphaned code in this EPIC's scope
- [ ] SoT files match final implementation
- [ ] Session State is clean (no open next steps)
- [ ] Change Log in Section 6 updated

---

## Finding Orphaned Code

Orphaned code is code that:
- Has no `@implements` tag
- Doesn't serve any documented ID
- Exists "just in case" or for undocumented purposes

### How to Check

1. Search codebase for functions without `@implements`
2. For each, ask: "Which ID does this serve?"
3. If no answer: either add the ID to SoT or delete the code

### Common Orphan Patterns

| Pattern | Why It Happens | Fix |
|---------|---------------|-----|
| Helper utilities | Created during development | Link to consuming ID or extract to shared utils |
| Dead code | Feature changed, code wasn't cleaned | Delete it |
| Copy-pasted code | Duplicated without understanding | Consolidate, add proper tags |
| "Future use" code | Premature abstraction | Delete (YAGNI) |

---

## Traceability Report Template

Generate at EPIC completion:

```
EPIC-XXX Traceability Report
============================

IDs Implemented:
- API-001: src/api/users/create.ts:15 ✓
- API-002: src/api/users/login.ts:12 ✓
- BR-001: src/api/users/create.ts:23 ✓
- BR-002: src/api/users/create.ts:18 ✓
- DBT-001: migrations/001_users.sql:1 ✓

Tests Mapped:
- TEST-001 → API-001 ✓ (passing)
- TEST-002 → API-001, BR-001 ✓ (passing)
- TEST-003 → API-002 ✓ (passing)

Coverage:
- APIs: 2/2 (100%)
- Business Rules: 2/2 (100%)
- Data Models: 1/1 (100%)
- Tests: 3/3 passing

Orphaned Code: None detected
```
