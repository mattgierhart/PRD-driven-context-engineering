---
alwaysApply: true
---

# Cross-Agent Communication Protocol

Agents in this project do NOT share a conversation or a mailbox. They communicate through files:

Before v0.7, coordination belongs in the current PRD gate log, open questions, and accepted SoT
snapshot because no EPIC exists. From v0.7 onward, the approved active EPIC becomes the execution
coordination record.

## Requesting work from another agent

Before v0.7, write a note in the current PRD gate's open questions or change log. From v0.7 onward,
write it in the EPIC's Agent Observations table:

| # | Observation | Proposed Action | Triage |
|---|---|---|---|
| 4 | Pricing page needs 3 tiers (from Horizon CFD-012) | Studio: design SCR for pricing tiers | Pending |

The product owner (pre-v0.7) or EPIC lead (v0.7+) triages observations and routes work to the
appropriate agent in the next session.

## Sharing decisions across agents

Write to the relevant SoT file with a cross-reference:

```
### BR-015: Rate Limit Tiers
- Free: 100 req/day (Horizon CFD-008)
- Pro: 10,000 req/day (Horizon CFD-009)
- @see API-045 (DevLab implementation)
- @see SCR-022 (Studio pricing page)
```

The ID cross-references ARE the communication. When Studio reads SCR-022, it sees the link to BR-015 and API-045, pulling in the full context without needing a direct message from DevLab.

## Flagging blockers

Before v0.7, write the blocker in the PRD gate state. From v0.7 onward, write it to the EPIC session state:

```
- **Context**: BLOCKED on Studio — need SCR-022 screen layout before implementing pricing page frontend
```

The next human session sees the blocker in the lifecycle-appropriate record and routes accordingly.
