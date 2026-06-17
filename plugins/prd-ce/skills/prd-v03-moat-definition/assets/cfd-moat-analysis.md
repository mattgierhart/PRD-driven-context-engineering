# CFD Moat Analysis Template

Copy this template for each competitor moat analysis. Store completed entries in `customer_feedback.md`.

---

## CFD-MOT-[XXX]: [Competitor Name] Moat Analysis

**Competitor**: [Name]
**URL**: [website]
**Analysis Date**: [YYYY-MM-DD]
**Upstream CFD**: [CFD-### from v0.2 Competitive Landscape]

### Moat Classification

**Primary Moat Type**: [Switching Costs / Network Effects / Data/IP / Brand/Trust / Scale/Cost / Regulatory]
**Secondary Moat Type**: [if applicable]
**Moat Strength**: [Impenetrable / Strong / Moderate / Weak / Eroding]

### Evidence Summary

| Evidence Type | Finding | Source | Tier |
|---------------|---------|--------|------|
| [Type] | [What you found] | [Where] | [1-5] |
| [Type] | [What you found] | [Where] | [1-5] |
| [Type] | [What you found] | [Where] | [1-5] |

### Switching Cost Inventory

| Cost Type | Rating | Evidence | Hours/$ Impact |
|-----------|--------|----------|----------------|
| **Financial** | [Strong/Moderate/Weak/None] | [contract terms, penalties] | $[amount] |
| **Time/Effort** | [Strong/Moderate/Weak/None] | [migration estimate] | [X] hours |
| **Data Migration** | [Strong/Moderate/Weak/None] | [export options, format] | [X] hours |
| **Workflow Retraining** | [Strong/Moderate/Weak/None] | [unique methodology?] | [X] hours |
| **Integration Rework** | [Strong/Moderate/Weak/None] | [API dependencies] | [X] hours |

**Total Switching Cost Estimate**: $[amount] + [X] hours

### Moat Strength Evidence

**Strength indicators** (why moat is [tier]):
1. [Evidence point]
2. [Evidence point]
3. [Evidence point]

**Weakness indicators** (where moat fails):
1. [Evidence point]
2. [Evidence point]
3. [Evidence point]

### Vulnerability Assessment

**Vulnerable Segment**: [Which customers/segment is NOT protected by moat]
**Why Vulnerable**: [Specific reason moat doesn't apply]
**Evidence**: [How you know this]

**Erosion Signals** (if applicable):
- [ ] New entrants gaining share
- [ ] Increasing complaints about [specific issue]
- [ ] Feature becoming commoditized
- [ ] Pricing pressure in market
- [ ] Technology shift undermining moat

### Targeting Implication

**Decision**: [Don't Compete / Wedge Strategy / Direct Competition]

**Rationale**: [1-2 sentences explaining why this decision given moat analysis]

**Wedge Entry Point** (if applicable): [Specific feature/segment to enter]

### Confidence & Gaps

**Overall Confidence**: [High / Medium / Low]
**Confidence Rationale**: [Why this confidence level]

**Gaps requiring validation**:
- [ ] [What we don't know]
- [ ] [What we assumed]

### Related IDs

- **Upstream**: CFD-[###] (Competitor intelligence from v0.2)
- **Downstream BR**: BR-TGT-[###] (Targeting rule this supports)

---

## Quality Checklist

Before marking complete:
- [ ] Moat type is specific (not "they're big")
- [ ] Moat strength has evidence (not assumed)
- [ ] All 5 switching cost types assessed
- [ ] Switching costs quantified (hours + $)
- [ ] Vulnerability identified (where moat doesn't apply)
- [ ] Targeting decision stated
- [ ] Confidence level with rationale
- [ ] Evidence tier noted for each claim

---

## Example Entry (HomeFalcon Context)

```
CFD-MOT-001: Home Warranty Company (American Home Shield) Moat Analysis

Competitor: American Home Shield
URL: ahs.com
Analysis Date: 2025-01-07
Upstream CFD: CFD-012 (AHS competitor profile)

Moat Classification:
- Primary: Brand/Trust
- Secondary: Scale/Cost
- Strength: Moderate

Evidence Summary:
| Evidence Type | Finding | Source | Tier |
|---------------|---------|--------|------|
| Brand awareness | #1 recognized name in home warranty | Google Trends | 2 |
| Switching friction | Monthly cancelable, no data lock-in | Pricing page | 1 |
| Customer complaints | "Claims denial" primary complaint | BBB reviews | 2 |

Switching Cost Inventory:
| Cost Type | Rating | Evidence | Hours/$ Impact |
|-----------|--------|----------|----------------|
| Financial | Weak | Month-to-month available | $0 penalty |
| Time/Effort | Weak | No setup required | <1 hour |
| Data Migration | None | No customer data stored | 0 hours |
| Workflow Retraining | None | Passive service | 0 hours |
| Integration Rework | None | No integrations | 0 hours |

Total Switching Cost: ~$0 + <1 hour

Vulnerability:
- Segment: DIY homeowners who want control
- Why: AHS moat is "trust to handle claims" — doesn't apply to users 
  who want to self-manage and just need tracking
- Evidence: Reddit threads "AHS denied my claim, need alternative"

Targeting Implication:
Decision: DIRECT COMPETITION on self-serve segment
Rationale: No switching friction + active pain (claims denial) = 
opportunity for tool that puts homeowner in control

Confidence: High — validated via complaint analysis + pricing page
```
