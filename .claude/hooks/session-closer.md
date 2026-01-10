---
name: session-closer
trigger: Stop
description: >
  Captures session state for seamless handoff at end of work session.
  Automatically validates EPIC Section 0 completeness before session ends.
---

# Session Closer Hook

**Trigger**: `Stop` (end of session)
**Purpose**: Capture session state for seamless handoff to next session.

## What This Hook Does

When a session ends, this hook:

1. Validates EPIC Section 0 is complete
2. Ensures progress is documented with ID references
3. Stages a session commit
4. Updates agent memory if patterns observed

## Protocol

### 1. Validate Section 0 Completeness

Check that EPIC Section 0 contains:

| Field | Required | Format |
|-------|----------|--------|
| Progress | Yes | What was done, with ID references |
| Stop Point | Yes | `file:line` where work ceased |
| Next Steps | Yes | Numbered list of actions |
| Context Notes | If applicable | Decisions, blockers |
| Files Changed | Yes | List of modified files |

### 2. Generate Session Commit

Format:
```
session: [EPIC-XX] {summary}
```

Example:
```
session: [EPIC-03] Implemented BR-101 rate limiting, stopped at api/ratelimit.ts:45
```

### 3. Update Agent Memory (Optional)

If patterns were observed during session:
- Add to agent's `## Project Memory` section
- Note the pattern with evidence IDs
- Mark as candidate for harvest if 3+ occurrences

## Integration with Other Hooks

This hook runs **after**:
- `SoT Update Trigger` (Stop) - SoT files already synced

This hook runs **before**:
- Session actually terminates

## Validation Checks

```
[ ] EPIC Section 0 has Progress field
[ ] Progress references at least one ID
[ ] Stop Point is specific (file:line or clear description)
[ ] Next Steps are numbered and actionable
[ ] Files Changed list matches git status
```

## On Validation Failure

If Section 0 is incomplete:

1. **Warn** the user about missing fields
2. **Prompt** for required information
3. **Do not block** session end (user may need to leave)
4. **Log** incomplete handoff for next session awareness

## Configuration

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "type": "command",
        "command": "echo 'Session closing - validating EPIC Section 0...'",
        "description": "Session Closer - validates handoff state"
      }
    ]
  }
}
```

> Note: Actual implementation will be a script or inline validation.

## Boundaries

**DO**:
- Validate Section 0 completeness
- Stage commits with proper format
- Update agent memory on significant patterns

**DON'T**:
- Continue work after session end
- Make decisions about next steps
- Block user from ending session
