# RISK- Template

Copy and fill for each identified risk:

```
RISK-XXX: [Risk Title]
Category: [Market | Technical | Adoption | Resource | Dependency | Timing]
Description: [What could go wrong]
Trigger: [What would cause this to happen]
Impact: [High | Medium | Low]
Likelihood: [High | Medium | Low]
Priority: [1-9 based on Impact × Likelihood]

Early Signal: [How we'd know this is happening]
Response: [Mitigate | Accept | Avoid | Transfer]
Mitigation: [Specific action if Response = Mitigate]
Owner: [Who is responsible]

Linked IDs: [FEA-XXX, UJ-XXX, BR-XXX affected]
Review Date: [When to reassess]
```

## Priority Calculation

| | Low Impact (1) | Medium Impact (2) | High Impact (3) |
|---|---|---|---|
| **High Likelihood (3)** | 3 | 6 | 9 |
| **Medium Likelihood (2)** | 2 | 4 | 6 |
| **Low Likelihood (1)** | 1 | 2 | 3 |

Priority = Impact score × Likelihood score

## Response Decision Guide

| If... | Then Response is... |
|-------|---------------------|
| You can reduce impact or likelihood with reasonable effort | Mitigate |
| Impact is low enough to live with | Accept |
| Risk is so severe that avoiding the cause is worth scope change | Avoid |
| Someone else (vendor, partner, insurance) can own the risk | Transfer |

## Checklist Before Adding

- [ ] Is this a genuine risk with evidence, not just worry?
- [ ] Is the trigger specific and observable?
- [ ] Is impact/likelihood based on evidence, not gut feeling?
- [ ] Is the mitigation specific and actionable?
- [ ] Is there an owner who will monitor this?
- [ ] Will this be reviewed before launch?
