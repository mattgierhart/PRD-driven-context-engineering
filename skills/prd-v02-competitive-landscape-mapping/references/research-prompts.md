# Competitive Research Prompts

Deep research templates for competitor discovery and gap analysis.

---

## When to Use

Trigger competitive research when:
- Starting v0.2 Market Definition
- Competitor list has <3 entries
- Need to validate "no competitors" claim
- Gap analysis lacks evidence
- Preparing 1% better hypothesis

---

## Prompt 1: Direct Competitor Discovery

```
Find direct competitors solving [problem] for [segment]:

1. Product hunt / G2 / Capterra search
   - Search: "[problem] software" OR "[task] tool"
   - Extract: Product names, pricing, customer counts

2. Google search variations
   - "[problem] app"
   - "[task] platform"
   - "best [category] tools 2024"
   - "[competitor name] alternatives"

3. Funding/acquisition signals
   - Search Crunchbase: "[category] startup funding"
   - Extract: Funding amounts (validates market)

OUTPUT:
| Competitor | Pricing | Funding | Target Segment | Key Feature |
```

---

## Prompt 2: Adjacent Solution Discovery

```
Find adjacent solutions that solve related problems:

1. Horizontal platforms
   - What larger tools include [feature] as a sub-feature?
   - Search: "[broader category] platform"

2. Workflow analysis
   - What do users do BEFORE they need [our solution]?
   - What do they do AFTER?
   - Are there tools serving those adjacent steps?

3. Integration partners
   - What tools would we integrate with?
   - Do those tools have built-in [our feature]?

OUTPUT:
| Adjacent Tool | Related Feature | Why Not Primary | Integration Opportunity |
```

---

## Prompt 3: Workaround Discovery

```
Find DIY solutions users have built:

1. Reddit / Forum search
   - Search: "how I [task]" OR "[task] workflow"
   - Look for: Spreadsheet mentions, manual processes, tool combinations

2. Template marketplaces
   - Search: "[task] template" on Notion, Airtable, Google Sheets
   - Extract: Download counts, feature requests in comments

3. Freelance platforms
   - Search Upwork/Fiverr: "[task] help"
   - Extract: Hourly rates (validates willingness to pay)

OUTPUT:
| Workaround Type | Effort Level | Cost | Evidence Source |
```

---

## Prompt 4: Gap Analysis Research

```
Find evidence of competitor weaknesses:

1. Review mining
   - G2/Capterra: Filter by 2-3 star reviews for [competitor]
   - Extract: Specific complaints, missing features

2. Churn signals
   - Search: "[competitor] alternative" OR "switching from [competitor]"
   - Extract: Why users leave

3. Community complaints
   - Search Reddit: "[competitor] problems" OR "[competitor] frustrating"
   - Extract: Recurring themes

4. Pricing complaints
   - Search: "[competitor] expensive" OR "[competitor] pricing"
   - Extract: Price sensitivity signals

OUTPUT:
| Competitor | Complaint Theme | Frequency | Evidence Tier |
```

---

## Prompt 5: Segment Gap Analysis

```
Find underserved segments within the market:

1. Company size gaps
   - Do competitors serve Enterprise but ignore SMB?
   - Search G2 filters by company size, note review density

2. Industry gaps
   - Which industries have few tool reviews?
   - Search: "[tool] for [industry]" across industries

3. Geography gaps
   - Are competitors US-focused?
   - Search: "[tool] [country]" for non-US markets

4. Use case gaps
   - What specific use cases are mentioned but unsupported?
   - Mine feature request forums

OUTPUT:
| Segment | Current Options | Gap Evidence | Opportunity Size |
```

---

## Prompt 6: Feature Intelligence

```
Build detailed feature comparison:

1. Documentation mining
   - Review competitor help docs, feature pages
   - Create feature checklist

2. Pricing tier analysis
   - What features unlock at each tier?
   - Note artificial limitations

3. Roadmap signals
   - Check competitor changelog, roadmap pages
   - Search: "[competitor] roadmap" OR "[competitor] coming soon"

4. API/Integration review
   - What integrations exist?
   - What's missing that users request?

OUTPUT:
| Feature | Competitor A | Competitor B | Gap Notes |
```

---

## Conversation Search First

Before external research, search past chats:

```
Keywords to try:
- "[market] competitors" OR "[problem] alternatives"
- "CFD-" AND "competitor" OR "alternative"
- "[segment] tools" OR "[segment] software"
- "feature comparison" OR "versus"
```

---

## Output Template

After research, create CFD entry:

```
CFD-###: Competitive Intelligence — [Market/Competitor]
Date: YYYY-MM-DD
Type: Competitive Intelligence
Evidence Tier: [1-5]

Discovery Method: [Which prompts used]

Key Findings:
- [Finding 1]: [Source]
- [Finding 2]: [Source]
- [Finding 3]: [Source]

Gap Identified: [Description]
Confidence: [High/Medium/Low]
Next Steps: [What to validate]
```
