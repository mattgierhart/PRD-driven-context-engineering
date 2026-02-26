# TECH- Template (Standard)

Use for Replace, Build, Buy, Integrate, and Research decisions.

```
TECH-XXX: [Technology/Capability Name]
Category: [Replace | Build | Buy | Integrate | Research]
Layer: [Derived from capability area — e.g., AI/ML, Database, Auth, Infrastructure]
Purpose: [What problem this solves]

Features Served: [FEA-XXX, FEA-YYY]
Screens Affected: [SCR-XXX, SCR-YYY] (if applicable)
Risk Constraints: [RISK-XXX that influenced this decision]

Decision: [Specific choice made, or "TBD after POC" for Research]
Rationale: [Why this choice over alternatives — explain the reasoning]

Alternatives Considered:
  - [Option A]: [Why rejected]
  - [Option B]: [Why rejected]

Trade-offs:
  - Pro: [Key advantage]
  - Con: [Key disadvantage]

Cost: [Pricing model, estimated cost at current scale AND 10x scale]
Integration Complexity: [Low | Medium | High]
Lock-in Risk: [Low | Medium | High — explain mitigation if Medium/High]

# For Replace category — document what's being replaced:
Replaces: [Current tool/service being replaced]
Replace Reason: [Why existing asset doesn't fit]

# For Research category — define evaluation scope:
Research Needed: [What must be learned before deciding]
Evaluation Criteria: [Specific metrics/benchmarks to evaluate against]
Decision Deadline: [When we must decide — tied to WAVE or milestone]

# Optional — if sibling products exist:
Product Family Notes: [Shared infrastructure, reuse decisions, cross-product impact]
```

## Category Selection Guide

| If... | Category is... |
|-------|----------------|
| Existing asset is wrong for this product | Replace |
| This is a core differentiator, nothing fits | Build |
| Proven solutions exist, not differentiating | Buy |
| Users expect connection to external service | Integrate |
| High uncertainty, multiple viable options | Research |

## Checklist Before Adding

- [ ] Purpose is clear and tied to FEA- entries
- [ ] Alternatives have been considered (at least 2)
- [ ] Cost is realistic (not just free tier — include 10x scale)
- [ ] Trade-offs are acknowledged honestly
- [ ] Does not conflict with any RISK- entry
- [ ] Cross-references are bidirectional (TECH → FEA, TECH → RISK)
- [ ] For Research: evaluation criteria and deadline are defined
