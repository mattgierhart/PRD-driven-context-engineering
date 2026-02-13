# Hook Contract Specification

> **Purpose**: Define the universal interface that all hooks implement, regardless of language.
> **Version**: 3.0.0

---

## Universal Interface

All hooks follow the same contract. Implementations can be in any language (Python, Shell, Node.js, etc.) as long as they honor these rules.

### Input (stdin)

Hooks receive a JSON object on stdin. Contents vary by event type:

| Event | stdin JSON | Description |
|-------|-----------|-------------|
| `SessionStart` | `{}` | Empty or minimal object |
| `UserPromptSubmit` | `{"prompt": "user's message"}` | The user's prompt text |
| `Stop` | `{"transcript": "...", "tool_outputs": [...]}` | Session transcript and tool outputs |
| `SubagentStart` | `{"agent": "name", "task": "..."}` | Subagent identity and task |
| `SubagentStop` | `{"agent": "name", "result": "..."}` | Subagent identity and result |

### Output (stdout)

Hooks output a JSON object to stdout with an optional `additionalContext` field:

```json
{"additionalContext": "Markdown string injected into agent context"}
```

- If the hook has nothing to inject, it can output nothing or `{}`.
- The `additionalContext` value supports full Markdown formatting.

### Exit Codes

| Code | Meaning | Effect |
|------|---------|--------|
| `0` | Success | Proceed normally; inject `additionalContext` if present |
| `2` | Block | Prevent the action (e.g., block a prompt submission) |
| Other | Error | Logged but non-blocking; hook is treated as a no-op |

### Timeout

- Default: `10000` ms (configurable per hook in `settings.json`)
- Hooks that exceed the timeout are killed and treated as errors

---

## Hook Inventory

| Hook | Event | Python | Shell | Purpose |
|------|-------|--------|-------|---------|
| Context Validation | `SessionStart` | `context-validation.py` | `context-validation.sh` | Inject 3+1 file reading order |
| Context Density Gate | `UserPromptSubmit` | `context-density-gate.py` | `context-density-gate.sh` | Assess epic/gate context readiness |
| SoT Update Trigger | `Stop` | `sot-update-trigger.py` | `sot-update-trigger.sh` | Remind about spec updates |

## Choosing a Language

- **Python** (default): Use when the repo has Python installed. More expressive for JSON parsing and regex.
- **Shell**: Use when the repo has no Python dependency (e.g., dotfiles, infrastructure repos). Requires `grep`, `sed`, `wc` (standard POSIX).

To switch languages, update `settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "bash .claude/hooks/context-validation.sh",
        "timeout": 10000
      }
    ]
  }
}
```

## Writing Custom Hooks

1. Create your script in `.claude/hooks/` (any language)
2. Honor the stdin/stdout/exit-code contract above
3. Create a matching `.md` documentation file
4. Wire it into `settings.json` under the appropriate event
5. Test: `echo '{}' | your-hook-script | python3 -m json.tool`
