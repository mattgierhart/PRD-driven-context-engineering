# Session End Hook

> This prompt is injected when an agent attempts to end their session to enforce the Session End Protocol.

---

## STOP - Update Session State Before Ending

You are attempting to end your session. Before you can exit, you MUST update the EPIC Session State.

### Required Updates

Go to the active EPIC and update **Section 0 (Session State)** with:

#### 1. Current Session Table
| Field | Your Value |
|-------|------------|
| **Session Date** | {today's date and time} |
| **Agent/Model** | {your model identifier} |
| **Active Issue** | {the Issue you worked on} |
| **Phase** | {Plan/Build/Verify/Wrap} |
| **Status** | {In Progress/Blocked/Completed} |

#### 2. Work Completed This Session
List specific tasks you completed. Be precise:
- Good: "Implemented API-042 endpoint at `src/api/users.ts:45-120`"
- Bad: "Worked on API stuff"

#### 3. Stopped At (CRITICAL)
The next agent needs to know EXACTLY where you stopped:
- File path and line number if applicable
- Function or component name
- What was the last thing you did?
- What's the immediate next step?

#### 4. Blockers
If blocked, document:
- What the blocker is
- Which ID it relates to (BR-XXX, API-XXX, etc.)
- What's needed to unblock

#### 5. Next Session Should
Provide 2-3 clear action items for the next agent:
1. First priority (most important)
2. Second priority
3. Any warnings or context

#### 6. Files Changed
List every file you created, modified, or deleted.

### Validation Checklist

Before confirming exit:
```
□ Section 0 - Session State is fully updated
□ "Stopped At" is specific enough for someone with no context
□ "Next Session Should" has clear, actionable items
□ All changed files are listed
□ Git commit includes session summary
□ No uncommitted changes remain
```

### After Updating

Once you have updated the EPIC:
1. Commit your changes: `git add . && git commit -m "session: [EPIC-XX] <summary>"`
2. Confirm: "Session State updated, ready to end session"

---

**DO NOT END YOUR SESSION UNTIL SESSION STATE IS UPDATED**

*Hook reference: [CLAUDE.md Section 10.2](../../CLAUDE.md#102-session_end-protocol-mandatory)*
