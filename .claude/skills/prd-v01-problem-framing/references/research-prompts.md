# Problem Framing Research Prompts

Reference file for evidence-gathering research when gap assessment shows missing elements.

## Deep Research Prompts by Gap Type

### Gap: "Who is hurting?" unclear

```
TASK: Identify specific buyer segments actively experiencing [problem area]

RESEARCH SEQUENCE:
1. Search job boards for roles that solve this problem manually
   - Keywords: "[task] coordinator", "[task] manager", "[industry] operations"
   - Extract: Company sizes, industries, salary ranges (budget signal)

2. Search G2/Capterra for tool categories related to [problem]
   - Look at: Who writes reviews (titles, company sizes)
   - Extract: Common job titles, company characteristics

3. Search Reddit/forums for complaints about [workflow]
   - Target subreddits: r/[industry], r/smallbusiness, r/[role]
   - Extract: Self-identified roles, business types, team sizes

OUTPUT FORMAT:
| Segment | Evidence | Size Signal | Pain Intensity |
|---------|----------|-------------|----------------|
| [Title + Business Type] | [Source quote] | [# of similar posts/reviews] | [High/Med/Low] |
```

### Gap: "What pain exists?" not validated

```
TASK: Find direct evidence of [suspected pain point] with verbatim quotes

RESEARCH SEQUENCE:
1. G2/Capterra 1-3 star reviews for [competitor tools]
   - Filter: Reviews mentioning [problem keywords]
   - Extract: Exact complaint language, context

2. Reddit search: "[tool category] frustrating" OR "[workflow] hate"
   - Target: Posts with 10+ upvotes (validated by community)
   - Extract: Specific workflow steps causing friction

3. Support forums for [competitor tools]
   - Search: Common complaints, feature requests
   - Extract: What users tried that didn't work

OUTPUT FORMAT:
| Source | Verbatim Quote | Pain Dimension | Evidence Tier |
|--------|---------------|----------------|---------------|
| [Platform + link] | "[Exact quote]" | [Category] | [1-5] |
```

### Gap: "Cost of problem" not quantified

```
TASK: Quantify the time, money, or risk cost of [problem]

RESEARCH SEQUENCE:
1. Job postings for roles that solve this manually
   - Extract: Salary ranges = annual cost of manual solution
   - Calculate: $X/year ÷ 2080 hours = hourly cost

2. Service provider pricing for [manual solution]
   - Search: Freelancer rates, agency quotes, consultant fees
   - Extract: Per-hour or per-project costs

3. Penalty/risk research (if compliance-related)
   - Search: "[regulation] penalty amounts 2024"
   - Extract: Fine ranges, enforcement frequency

4. Time-motion estimates from user discussions
   - Search: "how long does [task] take"
   - Extract: Self-reported time per occurrence

OUTPUT FORMAT:
| Cost Type | Amount | Source | Calculation |
|-----------|--------|--------|-------------|
| Time | X hrs/week | [Source] | [How derived] |
| Money | $X/month | [Source] | [How derived] |
| Risk | $X per incident | [Source] | [Regulation ref] |
```

### Gap: "Why now?" missing market trigger

```
TASK: Identify market triggers creating urgency for [solution category]

RESEARCH SEQUENCE:
1. Recent regulation/policy changes
   - Search: "[industry] regulation 2024 2025"
   - Extract: Effective dates, compliance requirements

2. Technology enablers
   - Search: "[enabling technology] adoption rate"
   - Extract: Cost drops, capability improvements

3. Competitive activity
   - Search: "[category] funding rounds 2024"
   - Extract: Investment signals, new entrants

4. Market events
   - Search: "[industry] trends 2025"
   - Extract: Shifts in buyer behavior, new pain points

OUTPUT FORMAT:
| Trigger Type | Specific Event | Timeline | Impact on Urgency |
|--------------|---------------|----------|-------------------|
| [Regulation/Tech/Market] | [Description] | [Date] | [How it creates urgency] |
```

## Evidence Tier Quick Reference

| Tier | Description | Examples | Weight |
|------|-------------|----------|--------|
| 1 | Buying behavior | Invoices, subscriptions, job posts with budgets | Highest |
| 2 | Active workarounds | Spreadsheets, hired help, manual processes | High |
| 3 | Complaints with cost | "Costs me X hours" or "Paying $Y for this" | Medium |
| 4 | General complaints | "This is annoying" without cost | Low |
| 5 | Speculation | "Users might want..." | Reject |

## CFD Entry Template

```markdown
## CFD-###: [Short Title]

**Date:** YYYY-MM-DD
**Source:** [Platform/Person/Method]
**Evidence Tier:** [1-5]
**Confidence:** [High/Medium/Low]

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

### Implications for Problem Statement
- [How this affects "Who"]
- [How this affects "What pain"]
- [How this validates/invalidates hypothesis]
```

## Conversation Search Patterns

Before starting research, search past chats for existing evidence:

```
Keywords to try:
- "[vertical] pain" OR "[vertical] problem"
- "CFD-" AND "[market]"
- "v0.1" AND "[similar product]"
- "[competitor name] complaints"
- "evidence" AND "[workflow]"
```

## Research Session Checklist

Before closing a research session:

- [ ] Created CFD entries for all findings
- [ ] Assigned evidence tiers to each entry
- [ ] Extracted pain dimensions (not just quotes)
- [ ] Quantified costs where possible
- [ ] Updated gap assessment table
- [ ] Identified remaining gaps for follow-up
