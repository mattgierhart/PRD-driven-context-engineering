---
name: sot-update-trigger
trigger: Stop
description: >
  Provides context-specific cascade checklists after execution completes.
  Replaces generic "update SoT" reminders with file-specific cascade steps.
  Also checks for metrics drift introduced during the session.
---

# SoT Update Trigger Hook

**Trigger**: `Stop` (when agent finishes responding)
**Purpose**: Provide context-specific cascade checklists when files are modified.

## What This Hook Does

After agent completes work, this hook:

1. Parses session for modified files (from tool outputs)
2. Identifies implementation files (.py, .ts, .js, etc.)
3. Checks if modified files contain SoT references (BR-, UJ-, API-)
4. Generates **context-specific cascade checklists** via `cascade_checklist.py`
5. Checks for metrics drift via `metrics_drift_check.py`

## Detection Logic

**Implementation file patterns:**
- `.py`, `.ts`, `.js`, `.tsx`, `.jsx`
- `.go`, `.rs`, `.java`, `.rb`

**ID reference pattern:**
- `BR-101`, `API-045`, `BR-FEA-001`, `CFD-MOT-123` (case-insensitive)

## Output Example

```markdown
## SoT Update Check

**Implementation files modified:** 3 file(s)

**SoT references found:** BR-101, API-045, UJ-012

## Cascade Checklist

The following files were modified. Complete these cascade steps:

### Test Changes
*Triggered by: `tests/test_auth.py`*

1. Verify `status/metrics.json` was updated (posttest hook should handle this automatically)
2. Update README `<!-- SECTION: truth-table -->` if test count or coverage changed
3. Update `SoT/SoT.TESTING.md` if test structure changed

### Api Changes
*Triggered by: `src/api/handler.py`*

1. Update `SoT/SoT.API_CONTRACTS.md` with new/changed endpoints
2. Update relevant `TEST-` entries if contract shape changed
3. Check if `API-` IDs need new entries or version bumps

*Skip steps that don't apply. These are context-specific reminders, not blockers.*
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Context-specific checklists | Generic "update SoT" was too abstract for subagents |
| Section anchors, not line numbers | Line numbers drift; markers are stable |
| Graceful fallback to generic | Works even without cascade_checklist.py |
| Drift check at stop | Catches drift introduced during the session |
| Non-blocking | Work is already complete |
| Exit silently if no impact | Avoid noise on every stop |

## When It Fires

- An implementation file was modified (any supported language)

## When It Stays Silent

- Only documentation modified
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

- Detect ID references in modified implementation files
- Provide actionable reminder with specific IDs
- Stay silent when no implementation files were modified

**DON'T**:

- Auto-modify SoT files (too risky)
- Block session completion
- Fire on every stop event (noise reduction)
