# Session State Guide

## Why Session State Matters

Session State is the "brain dump" that enables:
- **Continuity**: Next session (human or AI) resumes exactly where you left off
- **Context preservation**: Decisions, blockers, and reasoning are captured
- **Debugging**: If something goes wrong, you know what changed

## Section 0 Template

```markdown
## 0. Session State (The "Brain Dump")

- **Last Action**: [What was just completed]
- **Stopping Point**: [Exact file:line or test failure]
- **Next Steps**: [Exact instructions for next session]
- **Context**: [Key decisions, blockers, open questions]
```

## Field Definitions

### Last Action
What you just finished. Be specific.

**Good:**
- "Completed API-002 (login endpoint), all 5 tests passing"
- "Fixed TEST-003 failure, was missing email normalization"
- "Reviewed API-003 spec, ready to implement"

**Bad:**
- "Working on stuff"
- "Made progress"
- "Done with auth" (which part?)

### Stopping Point
Exact location to resume. Include:
- File path
- Line number or function name
- Test name if stopped on failure

**Good:**
- `src/api/auth/login.ts:47` — need to add rate limiting after line 47
- `TEST-008: Rate limiting` — failing, need to implement middleware
- `Window 2, Task 3` — ready to start API-003

**Bad:**
- "Somewhere in auth"
- "In the code"
- "A test is failing"

### Next Steps
Explicit instructions. What should the next session do first?

**Good:**
```markdown
1. Add rate limiter middleware to login endpoint
2. Update TEST-008 to verify 5 requests/minute limit
3. If passing, move to API-003 (logout)
```

**Bad:**
- "Continue"
- "Keep going"
- "Finish auth"

### Context
Capture anything that isn't in the code or specs:
- Decisions made during the session
- Blockers encountered
- Open questions
- Trade-offs chosen

**Good:**
```markdown
- Decided to use Supabase's built-in rate limiting instead of custom
- BLOCKED: Need clarity on refresh token expiry (asked in #product)
- Trade-off: Using HTTP-only cookies over localStorage for security
```

**Bad:**
- "N/A"
- "Nothing to note"
- Leaving this blank

## Session State Lifecycle

### At Session Start
1. Read Section 0
2. Verify you understand the stopping point
3. Review Next Steps
4. Note any new Context to add
5. Proceed with first Next Step

### During Session
- Keep mental note of decisions/discoveries
- If hitting a blocker, note it immediately
- If changing approach, note the reason

### At Session End (MANDATORY)
1. Stop at a clean point (test passing, task complete)
2. Write Last Action
3. Write exact Stopping Point
4. Write specific Next Steps
5. Add any Context not captured elsewhere
6. Commit Session State update

## Examples

### Clean End of Session

```markdown
## 0. Session State

- **Last Action**: Completed Window 1 (Database Schema)
  - Created users table with RLS
  - Created sessions table
  - Verified in Supabase Studio
  - All migration tests pass

- **Stopping Point**: Ready to start Window 2 (API Endpoints)

- **Next Steps**:
  1. Write TEST-001–005 for signup endpoint
  2. Implement API-001 (POST /auth/signup)
  3. Verify tests pass

- **Context**:
  - Added 'deleted_at' column for soft deletes (not in original spec, added BR-015)
  - RLS policy uses auth.uid() — requires Supabase client for auth
```

### Mid-Task Stop (Acceptable)

```markdown
## 0. Session State

- **Last Action**: Partially implemented API-002 (login)
  - Basic flow works
  - TEST-004 passes
  - TEST-005 (rate limiting) not yet implemented

- **Stopping Point**: src/api/auth/login.ts:52
  - Need to add rate limiter before the password check

- **Next Steps**:
  1. Add rateLimiter middleware call at line 52
  2. Run TEST-005, expect it to pass
  3. Run full test suite
  4. If green, update EPIC checklist

- **Context**:
  - Rate limiter will use Supabase's built-in (not custom)
  - Limit is 5 attempts per minute per IP (from BR-005)
```

### Blocked Stop

```markdown
## 0. Session State

- **Last Action**: Attempted to implement API-003 (password reset)
  - BLOCKED: Unclear on email service configuration

- **Stopping Point**: BLOCKED before starting API-003

- **Next Steps**:
  1. Get answer on email service (Resend vs SendGrid)
  2. Once resolved, configure email client
  3. Then implement API-003

- **Context**:
  - Asked in #product Slack at 2:30pm
  - Can work on API-004 (profile update) in parallel if unblocked
  - API-003 blocks Window 3 (UI needs reset flow)
```

## Anti-Patterns

### Amnesia Session State
```markdown
## 0. Session State
- **Last Action**: Worked on auth
- **Stopping Point**: In the code
- **Next Steps**: Continue
- **Context**: N/A
```
**Problem**: Useless for resuming. Next session has to re-discover everything.

### Never-Updated Session State
```markdown
## 0. Session State
- **Last Action**: N/A (not started)
- **Stopping Point**: N/A
- **Next Steps**: Begin with Window 1
- **Context**: N/A
```
**Problem**: This is the initial state. If EPIC is in progress but Session State looks like this, something is wrong.

### Over-Detailed Session State
```markdown
## 0. Session State
- **Last Action**:
  At 2:15pm I opened VSCode
  At 2:17pm I ran npm install
  At 2:20pm I noticed a TypeScript error
  At 2:25pm I fixed the error by adding...
  [continues for 500 words]
```
**Problem**: Too much noise. Session State is a summary, not a log.

## Checklist Before Ending Session

- [ ] Is Last Action specific enough that someone else understands?
- [ ] Is Stopping Point an exact location?
- [ ] Are Next Steps actionable without re-reading everything?
- [ ] Is Context capturing decisions not in code/specs?
- [ ] Would an AI agent understand how to resume?
- [ ] Would YOU understand in a week?
