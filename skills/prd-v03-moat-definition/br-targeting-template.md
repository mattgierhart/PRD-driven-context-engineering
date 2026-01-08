# BR Targeting Rules Template

Copy this template for targeting decisions based on moat analysis. Store completed entries in `BUSINESS_RULES.md`.

---

## BR-TGT-[XXX]: [Targeting Rule Name]

**Rule Type**: [Segment Target / Segment Avoid / Wedge Strategy / Feature Focus]
**Created**: [YYYY-MM-DD]
**Evidence**: [CFD-MOT-### that supports this rule]

### Rule Statement

**Rule**: [Clear, actionable statement of where to compete / not compete]

**Scope**: [Which product decisions this affects]

### Rationale

**Based on**: [Summary of moat analysis that led to this rule]

**Key insight**: [The specific moat weakness or strength driving this]

### Conditions

**Apply this rule when**:
- [Condition 1]
- [Condition 2]

**Don't apply when**:
- [Exception 1]
- [Exception 2]

### Review Triggers

Re-evaluate this rule if:
- [ ] Competitor moat strength changes
- [ ] New entrant appears in target segment
- [ ] Market conditions shift
- [ ] [Specific signal to watch]

**Next Review**: [Date or trigger event]

### Related IDs

- **Evidence**: CFD-MOT-[###]
- **Downstream**: [What this rule feeds into — pricing, GTM, etc.]

---

## Template Variants

### Variant A: Segment Targeting Rule

```
BR-TGT-###: [Segment]-First Targeting

Rule Type: Segment Target
Evidence: CFD-MOT-###

Rule Statement:
Target [specific segment] where [Competitor] moat is weakest due to [reason].

Rationale:
[Competitor] moat ([type]) applies to [segment they protect] but NOT to [our target]
because [specific reason moat doesn't apply].

Apply when: Marketing, sales targeting, feature prioritization
Don't apply when: Enterprise deals where [Competitor] is entrenched

Review Triggers:
- [Competitor] starts targeting [our segment]
- Our segment shows higher switching friction than expected
```

### Variant B: Segment Avoidance Rule

```
BR-TGT-###: Avoid [Segment] Until [Condition]

Rule Type: Segment Avoid
Evidence: CFD-MOT-###

Rule Statement:
Do NOT target [segment] until [specific condition] because [Competitor] moat
([type]) is [Impenetrable/Strong] there.

Rationale:
Switching costs in [segment] = [X hours + $Y]. Success requires overcoming
[specific friction]. Not viable until we have [capability/proof].

Apply when: Market expansion discussions, sales qualification
Exception: Inbound from [segment] customers already frustrated with [Competitor]

Review Triggers:
- [Competitor] moat shows erosion signals
- We achieve [milestone] that enables competition
```

### Variant C: Wedge Strategy Rule

```
BR-TGT-###: [Feature/Use Case] Wedge Entry

Rule Type: Wedge Strategy
Evidence: CFD-MOT-###

Rule Statement:
Enter market via [specific feature/use case] that bypasses [Competitor]
switching friction in [moat type].

Rationale:
[Competitor] moat protects [core use case] but [our wedge] allows:
- Coexistence (not replacement)
- Low switching cost entry point: [X hours, $Y]
- Expansion opportunity to [adjacent use case] once established

Execution:
1. Lead with [wedge feature]
2. Avoid positioning as [Competitor] replacement
3. Expand to [next feature] after [trigger]

Review Triggers:
- [Competitor] closes wedge opportunity
- Users request [replacement features] after adoption
```

### Variant D: Feature Focus Rule

```
BR-TGT-###: Lead with [Feature] — Bypasses [Moat Type]

Rule Type: Feature Focus
Evidence: CFD-MOT-###

Rule Statement:
Prioritize [feature] in marketing and product because it addresses
[pain point] without triggering [Competitor] switching costs.

Rationale:
[Competitor] switching friction = [moat type] protecting [their strength].
[Our feature] delivers value WITHOUT requiring users to:
- [Thing they don't have to do]
- [Another thing they don't have to do]

Apply when: Landing page, demo script, feature prioritization
Don't apply when: [Scenario where different positioning needed]
```

---

## Example Entries

### Example 1: SMB Targeting

```
BR-TGT-001: SMB-First Targeting for Warranty Management

Rule Type: Segment Target
Created: 2025-01-07
Evidence: CFD-MOT-001 (AHS moat analysis)

Rule Statement:
Target homeowners and small landlords (<10 properties) where home warranty
company moats don't apply.

Scope: Marketing, pricing tiers, feature prioritization

Rationale:
Home warranty companies (AHS, Choice, etc.) have Brand/Trust moat for
"hands-off" homeowners. This moat doesn't apply to:
- DIY homeowners who want control
- Small landlords managing multiple properties
- Homeowners burned by claims denial

These segments WANT self-management tools, not warranty services.

Apply when: Market messaging, customer acquisition targeting
Don't apply when: Partnership discussions with warranty companies

Review Triggers:
- Warranty companies launch self-serve tracking tools
- Our SMB segment shows unexpected churn

Next Review: 2025-04-01
```

### Example 2: Enterprise Avoidance

```
BR-TGT-002: Avoid Enterprise CRM Until Integration API Complete

Rule Type: Segment Avoid
Created: 2025-01-07
Evidence: CFD-MOT-002 (Salesforce moat analysis)

Rule Statement:
Do NOT target companies with >50 employees using Salesforce until our
Salesforce integration is production-ready.

Scope: Sales qualification, marketing targeting

Rationale:
Salesforce switching costs = 80-200 hours + integration dependencies.
Without integration, we require REPLACEMENT not addition.
With integration, we enable ENHANCEMENT (much lower friction).

Apply when: Qualifying inbound, outbound targeting
Exception: Companies actively churning from Salesforce (already eating the cost)

Review Triggers:
- Salesforce integration reaches production
- Competitor offers integration we don't have

Next Review: When integration shipped
```

---

## Quality Checklist

Before marking BR-TGT complete:
- [ ] Rule statement is actionable (not vague)
- [ ] Evidence CFD-MOT is referenced
- [ ] Rationale connects moat analysis to decision
- [ ] Apply/don't apply conditions are clear
- [ ] Review triggers specified
- [ ] Related IDs linked
