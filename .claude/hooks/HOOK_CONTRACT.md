# Hook Contract Specification

> **Purpose**: Define the universal interface that all hooks implement, regardless of language.
> **Version**: 3.0.0
> **Reference**: [Hooks Reference](https://code.claude.com/docs/en/hooks) · [Hooks Guide](https://code.claude.com/docs/en/hooks-guide)

---

## Configuration Format

Hooks are defined in `.claude/settings.json` (project) or `~/.claude/settings.json` (user) using three-level nesting:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "optional-regex",
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/your-hook.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**Levels**: Event → Matcher group (optional `matcher` + `hooks` array) → Hook handlers.

Use `"$CLAUDE_PROJECT_DIR"` to reference scripts by absolute path.

---

## Universal Interface

All hooks follow the same contract. Implementations can be in any language (Python, Shell, Node.js, etc.) as long as they honor these rules.

### Input (stdin)

Hooks receive a JSON object on stdin. All events include these common fields:

| Field | Description |
|-------|-------------|
| `session_id` | Current session identifier |
| `transcript_path` | Path to conversation JSON |
| `cwd` | Current working directory |
| `permission_mode` | Current permission mode |
| `hook_event_name` | Name of the event that fired |

Event-specific additional fields:

| Event | Additional Fields | Description |
|-------|-------------------|-------------|
| `SessionStart` | `source`, `model` | `source`: `"startup"`, `"resume"`, `"clear"`, `"compact"` |
| `UserPromptSubmit` | `prompt` | The user's prompt text |
| `Stop` | `stop_hook_active` | `true` if already continuing from a stop hook |
| `PreToolUse` | `tool_name`, `tool_input`, `tool_use_id` | Tool about to execute |
| `PostToolUse` | `tool_name`, `tool_input`, `tool_response`, `tool_use_id` | Tool just completed |
| `SubagentStart` | `agent_id`, `agent_type` | Subagent being spawned |
| `SubagentStop` | `agent_id`, `agent_type`, `agent_transcript_path`, `stop_hook_active` | Subagent completed |

### Output (stdout)

Hooks output JSON to stdout. The format depends on the event type:

**SessionStart / UserPromptSubmit** — inject context for Claude:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Markdown string injected into agent context"
  }
}
```

**Stop** — show message to user or block Claude from stopping:

```json
{"systemMessage": "Reminder shown to the user"}
```

Or to prevent stopping:

```json
{"decision": "block", "reason": "Must complete X before stopping"}
```

**PreToolUse** — allow, deny, or escalate tool calls:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "Explanation"
  }
}
```

If the hook has nothing to output, exit 0 with no stdout.

### Exit Codes

| Code | Meaning | Effect |
|------|---------|--------|
| `0` | Success | Proceed normally; process stdout JSON |
| `2` | Block | Event-dependent: may prevent the action, show stderr to user, or feed stderr to Claude. See [Hooks Reference](https://code.claude.com/docs/en/hooks) for per-event behavior |
| Other | Error | Logged but non-blocking; hook is treated as a no-op |

### Timeout

- Default: `600` seconds for command hooks (configurable per hook in `settings.json`)
- Timeout value is in **seconds** (not milliseconds)
- Hooks that exceed the timeout are killed and treated as errors

---

## Hook Inventory

| Hook | Event | Script | Purpose |
|------|-------|--------|---------|
| Context Validation | `SessionStart` | `context-validation.sh` | Inject 3+1 file reading order |
| Context Density Gate | `UserPromptSubmit` | `context-density-gate.sh` | Assess epic/gate context readiness |
| SoT Update Trigger | `Stop` | `sot-update-trigger.sh` | Remind about spec updates |

All hooks are POSIX shell scripts requiring only `grep`, `sed`, `wc`, and `awk` (standard on macOS and Linux). No Python or external dependencies needed.

## Supported Events

Claude Code supports 14 hook events. This template uses 3 (SessionStart, UserPromptSubmit, Stop). See the [full reference](https://code.claude.com/docs/en/hooks#hook-events) for all events:

`SessionStart` · `UserPromptSubmit` · `PreToolUse` · `PermissionRequest` · `PostToolUse` · `PostToolUseFailure` · `Notification` · `SubagentStart` · `SubagentStop` · `Stop` · `TeammateIdle` · `TaskCompleted` · `PreCompact` · `SessionEnd`

## Writing Custom Hooks

1. Create your script in `.claude/hooks/` (any language)
2. Honor the stdin/stdout/exit-code contract above
3. Use `"$CLAUDE_PROJECT_DIR"` for absolute paths in `settings.json`
4. Create a matching `.md` documentation file
5. Wire it into `settings.json` under the appropriate event (with correct 3-level nesting)
6. Test: `echo '{}' | your-hook-script | python3 -m json.tool`
