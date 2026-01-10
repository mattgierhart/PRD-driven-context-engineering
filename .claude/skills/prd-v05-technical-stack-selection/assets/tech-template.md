# TECH- Template

Copy and fill for each technology decision:

```
TECH-XXX: [Technology/Capability Name]
Category: [Build | Buy | Integrate | Research]
Layer: [Frontend | Backend | Database | Auth | Payments | Infrastructure | Integrations | AI/ML | Analytics | DevOps]
Purpose: [What problem this solves]

Features Served: [FEA-XXX, FEA-YYY]
Screens Affected: [SCR-XXX, SCR-YYY]
Risk Constraints: [RISK-XXX that influenced this]

Decision: [Specific choice or TBD]
Rationale: [Why this choice]
Alternatives Considered:
  - [Option A]: [Why rejected]
  - [Option B]: [Why rejected]

Trade-offs:
  - Pro: [Advantage]
  - Con: [Disadvantage]

Cost: [Pricing model, estimated cost]
Integration Complexity: [Low | Medium | High]
Lock-in Risk: [Low | Medium | High]

# For Research category only:
Research Needed: [What must be learned]
Evaluation Criteria: [How to decide]
Decision Deadline: [When we must decide]
```

## Category Selection Guide

| If... | Category is... |
|-------|----------------|
| This is a core differentiator | Build |
| Proven solutions exist and it's not differentiating | Buy |
| Users expect connection to external service | Integrate |
| Multiple options exist and stakes are high | Research |

## Checklist Before Adding

- [ ] Is the purpose clear and tied to FEA-?
- [ ] Have I considered alternatives?
- [ ] Is the cost realistic (not just free tier)?
- [ ] Have I acknowledged trade-offs?
- [ ] Does this conflict with any RISK-?
- [ ] For Research: Is there a deadline?
