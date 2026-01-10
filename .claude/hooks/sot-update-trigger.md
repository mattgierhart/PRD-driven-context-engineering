---
name: sot-update-trigger
trigger: Stop
description: >
  Reminds about Source of Truth updates after execution completes.
  Non-blocking advisory for maintaining spec consistency.
---

# SoT Update Trigger Hook

**Trigger**: `Stop` (when agent finishes responding)
**Purpose**: Remind about SoT updates when implementation files are modified.

## What This Hook Does

After agent completes work, this hook:

1. Parses session for modified files (from tool outputs)
2. Identifies implementation files (.py, .ts, .js, etc.)
3. Checks if modified files contain SoT references (BR-, UJ-, API-)
4. If potential SoT impact detected, outputs reminder

## Detection Logic

**Implementation file patterns:**
- `.py`, `.ts`, `.js`, `.tsx`, `.jsx`
- `.go`, `.rs`, `.java`, `.rb`

**SoT reference pattern:**
- `BR-XXX`, `UJ-XXX`, `API-XXX`, `CFD-XXX`
- `KPI-XXX`, `COMP-XXX`, `UI-XXX`, `ERR-XXX`
- `SEC-XXX`, `PERF-XXX`, `TEST-XXX`

## Output Example

```markdown
## SoT Update Check

**Implementation files modified:** 3 file(s)

**SoT references found:** BR-101, API-045, UJ-012

**Action:** If this work affects documented specifications:
1. Check `README.md` -> SoT Directory for affected spec files
2. Update relevant Source of Truth files (SoT/)
3. Ensure Unique IDs remain consistent

*This is a reminder, not a blocker. Skip if changes are implementation-only.*
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Reminder only, no auto-update | Risky to auto-modify specs |
| Reference README for SoT location | Avoids enumerating files (maintenance burden) |
| Non-blocking | Work is already complete |
| Exit silently if no impact | Avoid noise on every stop |

## When It Fires

- Implementation code modified (any language)
- Modified files contain SoT ID references
- Both conditions trigger the reminder

## When It Stays Silent

- Only documentation modified
- No SoT references in modified files
- No files modified at all

## Configuration

```json
{
  "hooks": {
    "Stop": [
      {
        "type": "command",
        "command": "python3 .claude/hooks/sot-update-trigger.py",
        "timeout": 15000
      }
    ]
  }
}
```

## Testing

```bash
# Test with transcript containing file modifications
echo '{"transcript": "Modified: src/api/handler.py containing BR-101"}' | python3 .claude/hooks/sot-update-trigger.py

# Test with no modifications (should exit silently)
echo '{"transcript": "Just answered a question"}' | python3 .claude/hooks/sot-update-trigger.py
```

## Boundaries

**DO**:

- Detect SoT references in modified files
- Provide actionable reminder with specific IDs
- Stay silent when no SoT impact detected

**DON'T**:

- Auto-modify SoT files (too risky)
- Block session completion
- Fire on every stop event (noise reduction)
