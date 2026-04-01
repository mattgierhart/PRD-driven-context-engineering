---
alwaysApply: true
---

# Cross-Agent Communication Protocol

Agents in this project do NOT share a conversation or a mailbox. They communicate through files:

## Requesting work from another agent

Write a note in the EPIC's Agent Observations table:

| # | Observation | Proposed Action | Triage |
|---|---|---|---|
| 4 | Pricing page needs 3 tiers (from Horizon CFD-012) | Studio: design SCR for pricing tiers | Pending |

The EPIC lead (human) triages observations and routes work to the appropriate agent in the next session.

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

Write to the EPIC session state:

```
- **Context**: BLOCKED on Studio — need SCR-022 screen layout before implementing pricing page frontend
```

The next human session sees the blocker and routes accordingly.
