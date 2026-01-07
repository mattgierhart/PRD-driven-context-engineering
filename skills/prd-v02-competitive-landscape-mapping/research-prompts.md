# Value Evidence Research Prompts

Use when value evidence is Tier 4-5 and needs upgrading to Tier 1-3.

---

## When to Use

Trigger research when:
- Value statement has only Tier 4-5 evidence
- No proof users want this specific outcome
- Quantification is assumed, not sourced
- Need to validate value before v0.2

---

## Prompt 1: Find Existing Spend (→ Tier 1)

```
Find evidence that [target segment] is already paying for [value outcome]:

1. Competitor products claiming to deliver [outcome]
   - Search: "[outcome] software" OR "[outcome] tool" pricing
   - Extract: Price points, customer counts, testimonials

2. Service providers selling [outcome] manually
   - Search: "[outcome] service" OR "[outcome] consultant"
   - Extract: Hourly rates, project costs

3. Job postings for roles that deliver [outcome]
   - Search: "[role that provides outcome]" salary
   - Extract: Salary ranges, job frequency

OUTPUT:
| Source | What They're Paying | Amount | Tier |
```

---

## Prompt 2: Find Active Workarounds (→ Tier 2)

```
Find evidence that [target segment] is building workarounds to achieve [outcome]:

1. Spreadsheet/template mentions
   - Search Reddit/forums: "[task] spreadsheet" OR "[task] template"
   - Extract: Descriptions of DIY solutions

2. Process documentation
   - Search: "how I [achieve outcome] manually"
   - Extract: Step counts, time estimates

3. Tool combinations
   - Search: "[task] workflow" OR "[task] stack"
   - Extract: Tool combinations being duct-taped together

OUTPUT:
| Source | Workaround Description | Effort Level | Tier |
```

---

## Prompt 3: Find Unprompted Desire (→ Tier 3)

```
Find evidence that [target segment] articulates wanting [outcome] without being asked:

1. Forum wish lists
   - Search Reddit: "I wish I could [outcome]" OR "would be nice if [outcome]"
   - Filter: Unprompted (not responding to survey)

2. Review complaints implying desire
   - Search G2/Capterra: [competitor] reviews mentioning [outcome gap]
   - Extract: "I wish it would..." or "Missing feature: ..."

3. Community feature requests
   - Search: [product] feature request [outcome]
   - Extract: Upvotes, comment agreement

OUTPUT:
| Source | Quote | Implied Value | Tier |
```

---

## Prompt 4: Validate Quantification

```
Find evidence to validate that [outcome] saves [claimed amount]:

1. Industry benchmarks
   - Search: "[task] time study" OR "[task] benchmark"
   - Extract: Average time/cost data

2. Before/after case studies
   - Search: "[solution] case study" OR "[solution] ROI"
   - Extract: Claimed improvements with methodology

3. User-reported savings
   - Search forums: "saves me [time unit]" AND [task]
   - Extract: Self-reported numbers with context

OUTPUT:
| Source | Claimed Savings | Calculation Method | Confidence |
```

---

## Conversation Search First

Before external research, search past chats:

```
Keywords to try:
- "[product] value" OR "[market] outcome"
- "CFD-" AND "saves" OR "reclaim"
- "[competitor] benefit" OR "[competitor] ROI"
- "willingness to pay" AND "[market]"
```

---

## Output Template

After research, create upgraded CFD entry:

```
CFD-###: Value Hypothesis — [Title] (Upgraded)
Date: YYYY-MM-DD
Type: Value Hypothesis
Evidence Tier: [New tier]
Previous Tier: [Old tier]

Value Statement: "[Updated based on research]"

Evidence Found:
- [Source 1]: [Finding]
- [Source 2]: [Finding]

Quantification Source: [How derived]
Confidence: [High/Medium/Low]
```
