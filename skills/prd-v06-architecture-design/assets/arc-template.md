# ARC- Template

Copy and fill for each architecture decision:

```
ARC-XXX: [Decision Title]
Category: [Structure | Integration | Security | Performance | Data | DevOps]
Context: [What prompted this decision]
Decision: [What we decided]
Rationale: [Why this choice]

Alternatives Rejected:
  - [Option A]: [Why not]
  - [Option B]: [Why not]

Consequences:
  - Enables: [What this makes possible]
  - Constrains: [What this limits]

Related IDs: [TECH-XXX, RISK-XXX, FEA-XXX]
Status: [Proposed | Accepted | Superseded]
```

## Category Selection Guide

| If the decision is about... | Category is... |
|-----------------------------|----------------|
| How code/services are organized | Structure |
| How external services connect | Integration |
| Auth, authorization, encryption | Security |
| Speed, caching, scaling | Performance |
| Storage, flow, consistency | Data |
| Deployment, monitoring, CI/CD | DevOps |

## Status Workflow

```
Proposed → Accepted → (optionally) Superseded by ARC-XXX
```

- **Proposed**: Under discussion
- **Accepted**: Team agrees, implementing
- **Superseded**: Replaced by newer decision (link to replacement)

## Checklist Before Adding

- [ ] Is this a significant decision that affects multiple components?
- [ ] Have I documented the context (why now)?
- [ ] Have I considered alternatives?
- [ ] Are consequences (enables/constrains) clear?
- [ ] Is this linked to relevant TECH-, RISK-, FEA-?
- [ ] Would a new team member understand why we chose this?
