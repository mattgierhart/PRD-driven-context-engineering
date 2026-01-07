# Competitive Landscape Findings
ID: 2025-01-07_competitive-landscape-findings_v0 | Owner: Matt | Updated: 2025-01-07

## Good Examples Found

| PRD/Context | How Competitors Identified | Data Captured | How It Was Used |
|-------------|---------------------------|---------------|-----------------|
| ServiceAutopilot analysis | Perplexity search: "direct competitors (FSM for green industry)" + "adjacent competitors (general FSM, CRM)" | Full 5-dimension framework: platform, competitive landscape, commercial, unbundling opps, replication difficulty | Informed micro-SaaS unbundling decisions |
| JUUNO.co digital signage | Category search across ScreenCloud, Yodeck, OptiSigns, Rise Vision, Kitcast, NoviSign, Wallboard | Feature set, positioning, target segments, pricing approach, strengths/weaknesses from reviews | Created positioning map + niche opportunity identification |
| Physical Asset Mgmt (CMMS) | UpKeep, MaintainX, Coast, Xenia, Operium | Annual cost calculations, per-user pricing, free tier limitations, mobile-first features | 96% undercut opportunity identified via flat vs per-user pricing |
| AI Sports Logo (Looka) | Direct competitor analysis with pricing vulnerability | $65 premium package pricing, feature gaps (no jersey preview), weakness: generic business focus | Clone target selection + 60% price disruption strategy ($29 vs $65) |
| Review Management | BirdEye, ReviewTrackers, Podium via G2/Capterra | Cost complaints, contract lock-ins, feature gaps, UX friction | SMB-focused positioning + simplified feature set |

## Bad Examples Found

| PRD/Context | What Was Done | Why Insufficient | What Was Needed |
|-------------|---------------|------------------|-----------------|
| Pre-revenue website acquisitions | "Zero moat" statement without analysis | No evidence of competitive positioning or differentiation analysis | Actual competitor feature/pricing comparison |
| Early Digital Signage PRD | Listed "existing solutions" without pricing | Couldn't calculate undercut opportunity | Per-seat/per-location cost breakdowns |
| Cold Email v0.1 | Named competitors (Instantly, Smartlead) without depth | No complaint mining or gap identification | G2/Capterra review synthesis for pain points |
| Multiple PRDs | Ignored "do nothing" / spreadsheet competitors | Underestimated inertia as primary competitor | Quantified switching cost from manual processes |

## Hierarchy Observations

### Competitor Types (CONFIRMED + REFINED)

| Type | Definition | Research Method | Example |
|------|------------|-----------------|---------|
| **1. Direct** | Same problem, same solution approach | "[category] software pricing" | Yodeck vs OptiSigns (digital signage) |
| **2. Indirect** | Same problem, different approach | "[problem] how companies solve" | Canva templates vs digital signage software |
| **3. Adjacent** | Related problem, could expand | "[related category] enterprise features" | Toast adding asset management to POS |
| **4. Workaround** | Manual processes, spreadsheets, hired help | Reddit: "[task] spreadsheet template" | USB stick content updates |
| **5. Inertia** | Do nothing — THE DEFAULT | "[task] not worth it" / "good enough" | Tolerate USB management for 3 displays |

**Key insight**: Type 4-5 are most often overlooked but most frequently the actual competition for SMB micro-SaaS.

### Intelligence Tier Hierarchy (CONFIRMED)

| Tier | Description | Source | Confidence |
|------|-------------|--------|------------|
| **1** | Verified pricing/features | Public pricing page, free trial, direct quote | 90%+ |
| **2** | Inferred pricing | Job posts with budget, customer reviews mentioning cost | 70-80% |
| **3** | Reported pricing | G2, Capterra, analyst reports | 50-65% |
| **4** | Estimated pricing | Similar products, market norms | 30-45% |
| **5** | Unknown | No data — FLAG for research | <20% |

**Gate rule**: At least 2 competitors must have Tier 1-2 pricing intelligence before v0.2 completion.

## Data Capture Patterns

| Field | Always Needed | Sometimes Useful | How Used Downstream |
|-------|---------------|------------------|---------------------|
| Name + URL | ✅ | — | Reference, linking |
| Pricing model | ✅ | — | Undercut calculation |
| Pricing tiers (all) | ✅ | — | Tier matching, gap finding |
| Per-user vs flat cost | ✅ | — | SMB penalty identification |
| Core features | ✅ | — | MVP scope, parity matrix |
| Target market | ✅ | — | Niche identification |
| Market position | ✅ | — | Premium/mid/budget mapping |
| Top 3 complaints | ✅ | — | Gap exploitation |
| Customer count | — | ✅ | Market size validation |
| Funding/revenue | — | ✅ | Sustainability assessment |
| Integration ecosystem | — | ✅ | Lock-in analysis |
| Recent product updates | — | ✅ | Trend detection |

## Gap Identification Methods

### Pattern 1: Review Mining
```
Search: [competitor] reviews G2 Capterra "wish" OR "missing" OR "too expensive"
Extract: Feature gaps + price complaints
Convert to: Our enhancement list
```

### Pattern 2: Pricing Model Arbitrage
```
Identify: Per-user pricing that penalizes SMBs
Calculate: 5-user annual cost vs flat alternative
Quantify: "96% savings" messaging
```

### Pattern 3: Feature Subtraction
```
List: All competitor features
Mark: Which are table-stakes vs differentiators
Remove: Enterprise features SMBs don't need
Result: Simpler, cheaper, faster solution
```

### Pattern 4: Workaround Cost Calculation
```
Identify: Manual process competitor uses
Quantify: Time × frequency × hourly rate
Compare: Our solution cost
Prove: ROI in < 3 months
```

## Anti-Patterns Identified

| Pattern | Example | Frequency |
|---------|---------|-----------|
| Surface-level "they exist" | "Competitors include X, Y, Z" without analysis | 3/8 PRDs |
| Missing pricing intelligence | Named competitors, no cost data | 4/8 PRDs |
| Ignored workaround competitors | Focused on SaaS, missed spreadsheets/manual | 5/8 PRDs |
| No undercut calculation | Didn't quantify savings opportunity | 2/8 PRDs |
| Analysis didn't inform positioning | Competitive table created, not referenced in strategy | 2/8 PRDs |

## Downstream Connections

### v0.2 Product Type Classification
Competitive landscape informs:
- **Fast Follow**: Clear leader exists, undercut opportunity
- **Slice**: Feature-rich incumbents, simplify for niche
- **Innovation**: Gap in market, no direct competitors

### v0.3 Market Moat Analysis
From competitive analysis, extract:
- Competitor moats (data lock-in, integrations, brand)
- Moat gaps we can exploit
- Switching costs to overcome

### v0.3 Pricing Model Selection
Competitive pricing informs:
- Price anchor (what they pay now)
- Undercut target (% below anchor)
- Model innovation (flat vs per-user)
- Tier structure (what features gate payment)

## Open Questions

1. Should we include a "competitive response prediction" section (what happens if we succeed)?
2. How to handle competitors with opaque enterprise pricing (contact sales)?
3. Standard for "how many competitors is enough" analysis?
