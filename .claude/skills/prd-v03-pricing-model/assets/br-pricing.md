# BR- Pricing Rules Template

Use this template to document pricing decisions as enforceable business rules.

---

## Pricing Constraints (BR-PRC-)

### BR-PRC-XXX: Entry Price Floor
```
Rule: [Entry tier minimum price]
Rationale: [Unit economics justification — CAC payback, margin target]
Enforcement: [Where — Stripe config, pricing page, sales process]
Evidence: [Cost calculation, competitive analysis]
Exception: [Discount policy, approval required]
```

**Fill in**:
- Entry tier minimum: $____/mo (monthly) or $____/year (annual)
- CAC estimate: $____
- Target payback: ____ months
- Floor calculation: Entry price × retention months ≥ CAC × [margin]

---

### BR-PRC-XXX: Discount Cap
```
Rule: Maximum discount of [X]% on any tier
Rationale: [Protect pricing integrity, prevent race to bottom]
Enforcement: [Approval workflow, system limits]
Evidence: [Margin analysis, competitor discount norms]
Exception: [Strategic accounts, Matt approval required]
```

**Fill in**:
- Maximum discount: ____%
- Annual prepay discount: ____%
- Founding customer discount: ____% (if applicable)
- Approval required above: ____%

---

### BR-PRC-XXX: Price Increase Policy
```
Rule: [How and when prices can change]
Rationale: [Customer trust, grandfathering decisions]
Enforcement: [Communication timeline, system configuration]
Evidence: [Industry norms, customer feedback]
Exception: [None — customers need predictability]
```

**Fill in**:
- Existing customers: [Grandfather / Phase in over X months / Immediate]
- New customers: [Effective date for new pricing]
- Notice period: ____ days minimum

---

## Packaging Rules (BR-PKG-)

### BR-PKG-XXX: Free Tier Boundaries
```
Rule: Free tier limited to [specific limits]
Rationale: [Demonstrate value + create upgrade trigger]
Enforcement: [Usage tracking, UI prompts at threshold]
Evidence: [Competitor analysis, conversion optimization data]
Exception: [None — critical for funnel]
```

**Fill in**:
| Limit | Value | Upgrade Prompt At |
|-------|-------|-------------------|
| [Units] | | (80% of limit) |
| Users | | |
| Storage | | |
| API calls | | |

---

### BR-PKG-XXX: Tier Feature Gates
```
Rule: [Which features gate which tiers]
Rationale: [Value progression, upgrade motivation]
Enforcement: [Feature flags, entitlement system]
Evidence: [User research, competitor tier analysis]
Exception: [Beta features may be unlocked temporarily]
```

**Fill in**:
| Feature | Free | Starter | Pro | Enterprise |
|---------|------|---------|-----|------------|
| | ✓ | ✓ | ✓ | ✓ |
| | ✗ | ✓ | ✓ | ✓ |
| | ✗ | ✗ | ✓ | ✓ |
| | ✗ | ✗ | ✗ | ✓ |

---

### BR-PKG-XXX: Upgrade Trigger Events
```
Rule: Show upgrade prompt when [specific event occurs]
Rationale: [Capture value moment, not interrupt workflow]
Enforcement: [Event tracking, modal/banner logic]
Evidence: [Conversion data, user research]
Exception: [Don't show during critical workflows]
```

**Fill in**:
| Trigger Event | Prompt Type | CTA |
|---------------|-------------|-----|
| Hit 80% of free limit | In-app banner | "Upgrade for unlimited" |
| First success moment | Celebration modal | "Get more wins with Pro" |
| After X days active | Email | "Ready to go Pro?" |

---

## Competitive Positioning (BR-CMP-)

### BR-CMP-XXX: Price Anchor Target
```
Rule: Maintain [X]% savings vs [Competitor] at [comparison basis]
Rationale: [Price leadership is core differentiator]
Enforcement: [Quarterly competitive review]
Evidence: [Competitor pricing data, CFD-XXX]
Exception: [Price floor takes precedence if competitor drops]
```

**Fill in**:
- Anchor competitor: ____________________
- Comparison basis: ____ users / ____ [units] / annual cost
- Their cost: $____/year
- Our cost: $____/year
- Savings: ____%
- Minimum savings to maintain: ____%

---

### BR-CMP-XXX: Competitive Response Policy
```
Rule: [How to respond if competitor changes pricing]
Rationale: [Maintain positioning without reactive panic]
Enforcement: [Review trigger, decision process]
Evidence: [Market norms, margin requirements]
Exception: [None — process must be followed]
```

**Fill in**:
- If competitor raises prices: [Opportunity to increase margin / Maintain gap]
- If competitor lowers prices: [Match to floor / Hold position / Differentiate on value]
- Review frequency: [Monthly / Quarterly]
- Decision maker: ____________________

---

## Quality Checklist

Before finalizing pricing BR- entries:

- [ ] **Entry price validated**: Unit economics work (CAC payback ≤3 months)
- [ ] **Anchor documented**: Specific competitor with CFD- reference
- [ ] **Free tier justified**: Clear upgrade trigger OR explicitly "no free tier"
- [ ] **Tiers make sense**: Each tier has clear value step
- [ ] **Enforcement clear**: Where/how each rule is implemented
- [ ] **Exceptions defined**: What overrides rules and who approves
- [ ] **Evidence linked**: CFD- or other sources for key claims

---

## Example Completed BR- Set

```
BR-PRC-001: Entry Price Floor
Rule: Starter tier minimum $15/mo annual ($180/yr) or $19/mo monthly
Rationale: CAC estimated at $50, need 3-month payback at 90% margin
Enforcement: Stripe product config, cannot create lower-priced products
Evidence: CAC model v1.0, competitor analysis CFD-023
Exception: 50% founding discount (max 100 customers, Matt approval)

BR-PKG-001: Free Tier Product Limit  
Rule: Free tier capped at 5 products; show upgrade banner at product 4
Rationale: 5 products demonstrates value; upgrade prompt at success moment
Enforcement: Product count tracking, banner component at 4+
Evidence: CFD-019 (Notion blocks model), conversion funnel analysis
Exception: None — critical for conversion

BR-CMP-001: UpKeep Price Anchor
Rule: Maintain ≥90% savings vs UpKeep at 5-user annual comparison
Rationale: "96% less" headline is primary acquisition message
Enforcement: Quarterly UpKeep pricing check, pricing page review
Evidence: CFD-001 (UpKeep $45/user/mo = $2,700/yr for 5 users)
Exception: If floor violated, maintain floor and adjust messaging
```
