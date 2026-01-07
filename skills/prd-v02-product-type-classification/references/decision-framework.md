# Product Type Decision Framework

## Detailed Decision Trees by Input Signal

### When Competitor Analysis Shows High Density (5+ competitors)

```
High competitor density detected
├── Are they all doing the same thing broadly?
│   YES → Market is commoditized
│   │   ├── Can you find underserved NICHE within?
│   │   │   YES → UNDERCUT (serve niche at lower price)
│   │   │   NO → Avoid this market
│   │   └── Is there a platform they all integrate with?
│   │       YES → SLICE (become the best integration)
│   │       NO → CLONE only if you have execution edge
│   │
│   NO → They serve different segments
│       ├── Is there an unserved segment?
│       │   YES → UNDERCUT (own that segment)
│       │   NO → CLONE the weakest competitor
│       └── Do they integrate poorly with each other?
│           YES → WRAPPER (connect them)
│           NO → Hard market, reconsider
```

### When Competitor Analysis Shows Low Density (0-2 competitors)

```
Low competitor density detected
├── Is there a horizontal platform doing this as one of many things?
│   YES → UNBUNDLE (extract and own the vertical)
│   NO → Continue
│
├── Are people using workarounds (spreadsheets, manual processes)?
│   YES → Validated pain exists
│   │   ├── Have others tried and failed?
│   │   │   YES → INNOVATION (but high risk)
│   │   │   NO → CLONE the workaround as product
│   │   └── Is there API/data to build on?
│   │       YES → WRAPPER
│   │       NO → Build from scratch
│   │
│   NO → No validated pain
│       └── STOP - insufficient market signal
```

### When Price Analysis Shows Opportunity

```
Price signals detected
├── Competitors charge $100+/month for SMB features
│   YES → UNDERCUT opportunity exists
│   │   ├── Can you deliver 80% of value at 30% of price?
│   │   │   YES → UNDERCUT confirmed
│   │   │   NO → Not viable undercut
│   │   └── Is the 20% you're cutting actually unused by niche?
│   │       YES → Strong UNDERCUT
│   │       NO → Risky UNDERCUT
│   │
│   NO → Pricing is reasonable
│       └── Compete on execution (CLONE) or features (INNOVATION)
```

### When Platform Ecosystem Detected

```
Target users live in a platform ecosystem (Shopify, Salesforce, HubSpot, etc.)
├── Does platform have app marketplace?
│   YES → SLICE is viable
│   │   ├── Is your category crowded in marketplace?
│   │   │   YES → Must differentiate on UX or niche
│   │   │   NO → Good SLICE opportunity
│   │   └── Does platform take >30% revenue share?
│   │       YES → Factor into unit economics
│   │       NO → Favorable SLICE economics
│   │
│   NO → Platform is closed
│       ├── Can you build integration anyway (API)?
│       │   YES → WRAPPER connecting to/from platform
│       │   NO → Not a Slice opportunity
│       └── Build standalone and position as complement
```

## Evidence Mapping Table

| If You Have This Evidence... | Consider This Type | Confidence Boost |
|-----------------------------|-------------------|------------------|
| Competitor G2 reviews citing "too expensive for SMB" | Undercut | +20% |
| Platform marketplace with <10 apps in category | Slice | +25% |
| Horizontal platform with 10+ categories | Unbundle | +15% |
| Reddit threads showing manual workarounds | Clone or Wrapper | +15% |
| Job postings mentioning budget for this category | Any (validates market) | +10% |
| Competitor recently acquired (signals validation) | Clone | +20% |
| Competitor churn data showing segment leaving | Undercut (for that segment) | +25% |
| API documentation publicly available | Wrapper | +30% |

## Risk Calibration by Type

| Type | Primary Risk | Early Warning Sign | Mitigation |
|------|-------------|-------------------|------------|
| Clone | Leader responds with feature parity | They ship your differentiator | Move faster, niche down |
| Unbundle | Vertical too small standalone | <$1M addressable | Expand adjacent verticals |
| Undercut | Race to bottom on price | Competitor matches price | Lock in with switching costs |
| Slice | Platform changes API/rules | Policy announcement | Diversify platform exposure |
| Wrapper | Data source becomes unavailable | API deprecation notice | Multiple data sources |
| Innovation | Market doesn't exist | Zero inbound interest | Pivot to Clone/Undercut |

## Confidence Threshold Decision Rules

```
IF confidence >= 85%:
  → Proceed to v0.3 immediately
  
IF confidence 70-84%:
  → Proceed to v0.3 with documented assumptions
  → Plan validation experiments in v0.4
  
IF confidence 50-69%:
  → Gather more evidence before proceeding
  → Specific gaps: [list what's missing]
  
IF confidence < 50%:
  → Return to v0.2 Competitive Landscape
  → Reclassify with additional research
```

## Type Transition Patterns

Sometimes classification changes as you learn more:

| Started As | Evidence Shifted | Reclassify To |
|------------|-----------------|---------------|
| Innovation | Found competitor with revenue | Clone or Undercut |
| Clone | Found niche severely underserved | Undercut |
| Undercut | Found platform ecosystem opportunity | Slice |
| Slice | Platform ecosystem weak/closed | Clone or Wrapper |
| Wrapper | API unavailable | Innovation or exit |
| Unbundle | Vertical too small | Undercut within vertical |
