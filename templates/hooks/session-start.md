# Session Start Hook

> This prompt is injected at the start of an agent session to enforce the Session Start Protocol.

---

## STOP - Read Session State First

Before doing any work, you MUST:

1. **Load the active EPIC** (check README.md for which EPIC is active)
2. **Read Section 0 (Session State)** completely
3. **Understand** where the previous session stopped
4. **Confirm** what the previous agent said you should do

### Quick Checklist

```
□ Found and read active EPIC
□ Read Section 0 - Session State
□ Understand the stopping point from last session
□ Know what Issue/Phase I'm working on
□ Loaded any SoT IDs mentioned in Session State
```

### If Session State is Empty or Unclear

If this is a new EPIC or the Session State is empty:
1. Read the full EPIC to understand scope
2. Start with Issue #1 in the Issue Manifest
3. YOU will be responsible for initializing Session State

### Confirm Before Proceeding

Reply with a brief summary:
- What was the previous session working on?
- Where did they stop?
- What should you do first?

Only proceed with work after confirming this understanding.

---

*Hook reference: [CLAUDE.md Section 10.1](../../CLAUDE.md#101-session-start-protocol)*
