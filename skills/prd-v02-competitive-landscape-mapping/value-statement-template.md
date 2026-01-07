# Value Statement Template

Copy-paste templates for documenting value articulation.

---

## Value Statement Table

Copy for each pain point:

```markdown
| Element | Entry |
|---------|-------|
| **Pain (source)** | CFD-### |
| **Pain Statement** | "[Quote or summary]" |
| **Value Statement** | "[If we solve X, users gain Y]" |
| **Value Unit** | [Time / Money / Risk / Capability] |
| **Quantification** | [X hrs/week, $Y/month, Z% reduction] |
| **Framing Type** | [Negative Removal / Positive Gain / Capability Unlock / Risk Reduction] |
| **Evidence Tier** | [1-5] |
| **Supporting CFD** | CFD-### |
```

---

## CFD Entry (Value Hypothesis)

```markdown
## CFD-###: Value Hypothesis — [Short Title]

**Date:** YYYY-MM-DD
**Type:** Value Hypothesis
**Source Pain:** CFD-###
**Evidence Tier:** [1-5]
**Confidence:** [High / Medium / Low]

### Value Statement
> "[Complete sentence describing user gain]"

### Transformation
- **Pain:** [Original from CFD-###]
- **Value:** [Transformed statement]
- **Framing:** [Type selected]

### Evidence
- Quote: "[Verbatim if available]"
- Source: [Platform / Interview]
- Why this indicates value: [Explanation]

### Quantification
- Unit: [Time / Money / Risk / Capability]
- Amount: [Number]
- Calculation: [Show work]
```

---

## Quick Transformation Reference

| Pain | → | Value |
|------|---|-------|
| Costs X hours | → | Reclaim X hours for [activity] |
| Costs $X/month | → | Save $X/month |
| Risks $X penalty | → | Eliminate $X exposure |
| Cannot do X | → | Now able to X |
| Takes X steps | → | Complete in Y steps |
| Manual process | → | Automatic + verified |
| Delayed by W | → | Instant/real-time |
| Error-prone | → | Error-free with [metric] |

---

## Framing Selection

| If Evidence Shows | Use |
|-------------------|-----|
| "Hate", "wasting", "losing" | Negative Removal |
| "I wish I could..." | Positive Gain |
| "We can't..." | Capability Unlock |
| Regulatory/penalty context | Risk Reduction |

---

## Evidence Tier Check

| Question | If Yes |
|----------|--------|
| Paying for this elsewhere? | Tier 1 |
| Building workarounds? | Tier 2 |
| Said they want (unprompted)? | Tier 3 |
| Agreed when asked? | Tier 4 |
| We're assuming? | Tier 5 ❌ |

---

## Quality Self-Check

Before v0.2:

- [ ] No features in value statement
- [ ] Value is quantified
- [ ] Value unit matches pain unit
- [ ] Evidence tier 1-3 (or flagged)
- [ ] Can test with landing page
- [ ] Transformation documented
