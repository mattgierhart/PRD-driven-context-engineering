# TEST- Template

Copy and fill for each test case:

```
TEST-XXX: [Test Name]
Type: [Unit | Integration | E2E | Contract | Performance]
Tests: [API-XXX | BR-XXX | UJ-XXX | DBT-XXX]
EPIC: [EPIC-XXX]

Given: [Preconditions]
When: [Action/trigger]
Then: [Expected outcome]

Validation Method: [Automated | Manual | Both]
Automation: [Test file path]
Priority: [Critical | High | Medium | Low]
```

## Type Selection Guide

| If testing... | Type is... | Example |
|---------------|------------|---------|
| A single function in isolation | Unit | Password validation |
| An API endpoint with database | Integration | POST /users creates record |
| A complete user workflow | E2E | Signup → verify → dashboard |
| API response shape | Contract | Response matches schema |
| Speed or load handling | Performance | API responds in <200ms |

## Priority Selection Guide

| If failure would... | Priority is... |
|---------------------|----------------|
| Cause data loss or security breach | Critical |
| Block core user journey | Critical |
| Break main product features | High |
| Degrade experience with workaround | Medium |
| Affect edge cases or admin features | Low |

## Given-When-Then Tips

**Given** (Preconditions):
- Database state (records exist/don't exist)
- User state (logged in/out, role)
- System state (feature flags, config)

**When** (Trigger):
- User action (click, submit, navigate)
- API call (method, path, body)
- System event (cron, webhook)

**Then** (Outcome):
- Response status and body
- Database changes
- UI state changes
- Side effects (email sent, event tracked)

## Checklist Before Adding

- [ ] Is this test linked to an API-, BR-, UJ-, or DBT-?
- [ ] Is the Given specific enough to reproduce?
- [ ] Is the When a single, clear action?
- [ ] Is the Then measurable and specific?
- [ ] Is the priority appropriate?
- [ ] For Critical tests: Is automation path defined?
