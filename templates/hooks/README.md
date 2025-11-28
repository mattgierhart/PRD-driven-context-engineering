# Session Hooks for GHM

This directory contains hook templates for enforcing session protocols in AI agent workflows.

## Overview

Hooks intercept agent actions at key points (session start, session end, pre-commit) to enforce the [Session Protocols](../../CLAUDE.md#10-session-protocols) defined in CLAUDE.md.

## Available Hooks

| Hook | Trigger | Purpose |
|------|---------|---------|
| `session-start.md` | Agent session begins | Prompt to read Session State before working |
| `session-end.md` | Agent session ends | Block exit until Session State is updated |
| `pre-commit.sh` | Before git commit | Validate EPIC changes are included |

## Claude Code Integration

For Claude Code, hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "preToolCall": [
      {
        "matcher": "exit|end|done|finish",
        "command": "cat templates/hooks/session-end.md"
      }
    ]
  }
}
```

## Generic Agent Integration

For other agent frameworks, adapt the hook logic to your harness:

### Session Start Hook

```python
# Before agent begins work
def on_session_start(agent, epic_path):
    session_state = extract_section_0(epic_path)
    agent.inject_context(f"""
    ## Session Start - Read Before Proceeding

    Previous session state:
    {session_state}

    Confirm you understand where work stopped before continuing.
    """)
```

### Session End Hook

```python
# Before agent session terminates
def on_session_end(agent, epic_path):
    if not epic_section_0_updated(epic_path):
        agent.block_exit("""
        ⚠️ Session State not updated!

        Before ending, you MUST update EPIC Section 0 with:
        - Work completed this session
        - Exact stopping point
        - Next session instructions

        Update the EPIC, then try again.
        """)
```

## Validation

Run `tools/validate-sessions.py` to check Session State compliance across all EPICs:

```bash
python tools/validate-sessions.py --epic epics/EPIC-03.md
python tools/validate-sessions.py --all
```

## Customization

Copy these templates to your project and modify as needed. The key enforcement points are:

1. **Session Start**: Ensure agent reads previous state before working
2. **Session End**: Block termination until Session State is current
3. **Pre-Commit**: Validate EPIC changes accompany code changes

See individual hook files for implementation details.
