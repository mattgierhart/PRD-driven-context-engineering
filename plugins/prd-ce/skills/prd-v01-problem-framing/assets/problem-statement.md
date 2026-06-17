# Problem Statement Template

Copy and populate for each new PRD v0.1 Spark.

---

## Gap Assessment Table

| Element | Status | Source |
|---------|--------|--------|
| Who is hurting? | ⚠️ Hypothesis / ✅ Validated / ❌ Missing | |
| What pain exists? | ⚠️ / ✅ / ❌ | |
| Cost of problem | ⚠️ / ✅ / ❌ | |
| Why now? | ⚠️ / ✅ / ❌ | |
| What's impossible? | ⚠️ / ✅ / ❌ | |

**Gate check**: ≥2 elements must be ✅ before drafting.

---

## Problem Statement Table

| Element | Definition | Evidence |
|---------|------------|----------|
| **Who is hurting?** | [Specific persona: role + business type + size] | [Segment size or example] |
| **What pain exists today?** | [Observable behavior or workflow friction] | [CFD-###] |
| **Cost of problem** | [Time: X hrs/week OR Money: $X/month OR Risk: $X per incident] | [Calculation source] |
| **Why now?** | [Market trigger: regulation, technology, competitor move] | [Trend or event] |
| **What's impossible?** | [What they can't do today that they want to] | [User statement] |

---

## CFD Entry Template

```markdown
## CFD-###: [Short Title]

**Date:** YYYY-MM-DD
**Source:** [Platform / Person / Method]
**Evidence Tier:** [1-5]
**Confidence:** [High / Medium / Low]

### Verbatim Quote
> "[Exact words from source]"

### Pain Dimensions Extracted
1. [Dimension 1]: [Brief description]
2. [Dimension 2]: [Brief description]
3. [Dimension 3]: [Brief description]

### Cost Signals
- Time: [If mentioned]
- Money: [If mentioned]
- Risk: [If mentioned]

### Implications
- [How this affects problem statement]
```

---

## Evidence Tier Reference

| Tier | Type | Examples | Use |
|------|------|----------|-----|
| 1 | Buying behavior | Invoices, subscriptions, job budgets | ✅ Strong |
| 2 | Active workarounds | Spreadsheets, hired help, manual processes | ✅ Strong |
| 3 | Complaints with cost | "Costs me X hours", "Paying $Y" | ✅ Acceptable |
| 4 | General complaints | "This is annoying" | ⚠️ Weak |
| 5 | Speculation | "Users might want..." | ❌ Reject |

---

## Quality Gate Checklist

Before advancing to v0.2:

- [ ] At least 1 Tier 1-2 evidence item exists
- [ ] Cost is quantified (time, money, or risk)
- [ ] "Who" is specific enough to create a prospect list
- [ ] "Why now" has at least a Tier 3 hypothesis
- [ ] Can find 10 people with this problem in 48 hours
- [ ] Can observe the pain behavior (not just hear about it)

---

## Spark Summary Template

```markdown
### Spark Summary

[One-sentence problem statement]: [Who] faces [pain] costing [quantified amount] because [root cause]. [Why now trigger] creates urgency. Current solutions [gap or failure]. [CFD-###]
```

**Example**:
> SMBs with 1-10 display screens face a "sneakernet" problem costing 15-30 min per update because existing digital signage solutions price for enterprise scale. Streaming device ubiquity ($30 Fire TV) creates urgency. Current solutions require 100+ screen minimums or complex setup. [CFD-001]
