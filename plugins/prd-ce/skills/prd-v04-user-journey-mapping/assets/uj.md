# UJ- Template

Copy and fill for each user journey:

```
UJ-XXX: [Journey Title]
Persona: [PER-XXX]
Type: [Core | Onboarding | Recovery | Power User]
Trigger: [Event that initiates journey]
Goal: [What user wants to accomplish]

Steps:
  1. [Action] → FEA-XXX
  2. [Action] → FEA-XXX
  3. [Action] → FEA-XXX

Pain Points:
  - [Step X]: [Potential friction]
  - [Step Y]: [Potential friction]

Moment of Value: [When user achieves goal]
KPI Link: [KPI-XXX this journey drives]
Success Metric: [How we measure journey completion]
Dependencies: [BR-XXX, API-XXX, other UJ-XXX]
```

## Journey Type Selection Guide

| If the journey... | Type is... |
|-------------------|------------|
| Is required for first-time users | Onboarding |
| Delivers primary product value | Core |
| Handles errors, support, edge cases | Recovery |
| Enables advanced/expansion features | Power User |

## Checklist Before Adding

- [ ] Does this journey have a specific trigger (not "opens app")?
- [ ] Is every step linked to a FEA-?
- [ ] Are pain points identified?
- [ ] Is there a clear moment of value?
- [ ] Does this journey tie to a KPI-?
- [ ] Are dependencies on other journeys documented?
