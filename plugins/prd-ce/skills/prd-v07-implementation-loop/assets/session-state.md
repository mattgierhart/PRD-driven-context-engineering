# Session State Template

Copy this to the EPIC Session State section and update at the END of every session:

```markdown
## 0. Session State (The "Brain Dump")

- **Last Action**: [What was just completed — reference IDs]
- **Stopping Point**: [Exact file:line or test failure]
- **Next Steps**: [Numbered list of exact instructions for next session]
- **Context**: [Key decisions made, blockers hit, questions open]
```

---

## Field Guidelines

### Last Action

Be specific about what was completed. Reference IDs.

| Good | Bad |
|------|-----|
| "Completed API-002 (login endpoint), all tests passing" | "Working on auth" |
| "Added BR-005 rate limiting to signup flow" | "Made some changes" |
| "Fixed TEST-003 failing assertion on line 47" | "Fixed tests" |

### Stopping Point

Provide enough detail to resume immediately.

| Good | Bad |
|------|-----|
| "src/api/auth/login.ts:47 — need to add rate limiting" | "Somewhere in the code" |
| "TEST-008 failing: expected 429, got 200" | "Tests failing" |
| "Window 2, task 3 — API-003 not started" | "Middle of Window 2" |

### Next Steps

Numbered, actionable instructions. A different agent should be able to resume.

| Good | Bad |
|------|-----|
| "1. Add rate limiter middleware per BR-005<br>2. Update TEST-008 to verify rate limiting<br>3. Move to API-003 (logout)" | "Continue working" |

### Context

Capture decisions, blockers, and open questions that future sessions need.

| Include | Exclude |
|---------|---------|
| Architecture decisions made | Obvious facts |
| Blockers encountered | Routine steps |
| Questions needing answers | Already-resolved issues |
| Deviations from spec | Standard implementations |

---

## Complete Example

```markdown
## 0. Session State (The "Brain Dump")

- **Last Action**: Completed API-002 (login endpoint), all tests passing
- **Stopping Point**: src/api/auth/login.ts:47 — need to add rate limiting per BR-005
- **Next Steps**:
  1. Add rate limiter middleware to login endpoint
  2. Update TEST-008 to verify rate limiting (expect 429 after 5 attempts)
  3. Move to API-003 (logout endpoint)
  4. Update Session State before stopping
- **Context**:
  - Decided to use Supabase's built-in rate limiting rather than custom middleware (simpler, fits free tier)
  - User suggested we might need refresh tokens — deferred to EPIC-03
  - All Window 1 tasks complete, starting Window 2
```

---

## Anti-Pattern Examples

### The Vague Handoff

```markdown
- **Last Action**: Working on auth
- **Stopping Point**: Somewhere in the code
- **Next Steps**: Continue
- **Context**: N/A
```

**Problem**: Next session has no idea what's done, what's next, or what decisions were made.

### The Overloaded Dump

```markdown
- **Last Action**: Did a bunch of stuff including setting up the database, writing migrations, creating the users table, adding RLS policies, testing locally, fixing a bug where emails weren't validating, updating the schema to add a created_at field...
- **Stopping Point**: Done with database I think?
- **Next Steps**: Move on
- **Context**: Lots of stuff happened
```

**Problem**: Too much narrative, not enough actionable detail. Which IDs? What's the exact stopping point?

### The Orphan

```markdown
- **Last Action**: Finished the feature
- **Stopping Point**: N/A — done
- **Next Steps**: Ship it
- **Context**: None needed
```

**Problem**: Skips validation phase. Where's the test verification? What about SoT updates?
