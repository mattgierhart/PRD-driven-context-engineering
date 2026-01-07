# Product Type Classification Examples

## Good Classifications (From GearHeart Portfolio)

### ReviewMaster — UNDERCUT ✓

**Context**: BirdEye dominates SMB review management at $299/month

**Classification Evidence**:
- CFD-012: G2 reviews show "too expensive for single-location restaurants"
- CFD-013: Feature analysis shows 60% of BirdEye features unused by SMBs
- CFD-014: Price sensitivity confirmed via Reddit r/smallbusiness threads
- Price gap: $299 → $49 (83% reduction viable)

**Why UNDERCUT (not Clone)**:
- Not trying to match BirdEye feature-for-feature
- Deliberately cutting features SMBs don't use
- Targeting specific niche (local restaurants) vs broad market
- Price is the primary competitive weapon

**BR Entry Created**:
```
BR-045: Product Type Classification
Type: Undercut
Confidence: 75%
Primary Evidence: CFD-012, CFD-013, CFD-014
Rationale: BirdEye validated market but overserves SMBs. 
83% price reduction sustainable by cutting enterprise features 
(multi-location, API, white-label) that single-location 
restaurants don't need.
```

**Outcome**: Gate 2 approved, development in progress

---

### Digital Sports Branding AI — CLONE + UNDERCUT ✓

**Context**: Looka dominates AI logo generation at $65/premium

**Classification Evidence**:
- CFD-018: Looka has no sport-specific training
- CFD-019: Youth sports teams searching "team logo generator" (high volume)
- CFD-020: Looka premium at $65, target $29 (55% reduction)
- Niche enhancement possible: jersey mockups, team color psychology

**Why CLONE + UNDERCUT (hybrid)**:
- Cloning core AI logo workflow (proven model)
- Undercutting on price for specific niche (sports teams)
- Adding niche features Looka won't build (too vertical)

**BR Entry Created**:
```
BR-052: Product Type Classification
Type: Clone + Undercut (hybrid)
Confidence: 70%
Primary Evidence: CFD-018, CFD-019, CFD-020
Rationale: Looka validated AI logo market. Sports teams 
underserved—no competitor offers sport-specific features. 
Clone core workflow, undercut price 55%, add vertical 
features (jersey preview, team colors).
```

**Outcome**: Gate 2 approved, active development

---

### Craigslist → Airbnb — UNBUNDLE ✓ (Historical Example)

**Context**: Craigslist had 50+ categories including vacation rentals

**Classification Evidence**:
- Craigslist vacation rental UX was terrible (no photos, no payments)
- Category had massive volume but poor experience
- Users were already there, just underserved
- Horizontal platform couldn't prioritize one vertical

**Why UNBUNDLE (not Clone)**:
- Didn't copy Craigslist broadly
- Extracted ONE category and made it 10x better
- Competed AGAINST the platform for that vertical
- Built features Craigslist would never add (reviews, payments, photos)

**Pattern to Replicate**:
```
IF: Horizontal platform exists with many categories
AND: Your category is high-volume but poorly served
AND: Platform won't prioritize your category
THEN: UNBUNDLE
```

---

### Tinder → Bumble — CLONE ✓ (Historical Example)

**Context**: Tinder dominated dating apps

**Classification Evidence**:
- Tinder validated swipe-based dating
- Women reported harassment/safety issues
- Opportunity: same model, different power dynamic
- Feature differentiation: women message first

**Why CLONE (not Innovation)**:
- Core mechanic identical (swipe matching)
- Not creating new category
- Executing better on specific user segment (women)
- Fast-follow into validated market

**Pattern to Replicate**:
```
IF: Leader validated market and model
AND: Specific segment underserved by leader
AND: Execution improvement possible (not just price)
THEN: CLONE with segment focus
```

---

## Bad Classifications (Lessons Learned)

### Physical Therapy Documentation AI — INNOVATION ✗

**Original Classification**: Innovation (new AI solution)

**What Went Wrong**:
- Positioned as "new approach to PT documentation"
- Ignored existing EMR competitors with documentation features
- Assumed need for category education
- Planned long B2B sales cycle

**Should Have Been**: CLONE + UNDERCUT
- EMR competitors exist (validated market)
- PT-specific workflows underserved (niche)
- Price opportunity vs enterprise EMRs
- No need to educate market—they know they need documentation

**Lesson**: If ANY competitor has revenue solving similar problem, you're not innovating. You're cloning or undercutting.

**Corrected BR Entry**:
```
BR-XXX: Product Type Classification
Type: Undercut (corrected from Innovation)
Confidence: 60%
Primary Evidence: [Need to gather EMR pricing, PT segment pain]
Rationale: Documentation tools exist. Position as 
"like [EMR] but built for PT at 60% lower cost" not 
"revolutionary new approach."
```

---

### Consumer Advocate Platform — INNOVATION ✗

**Original Classification**: Innovation (new consumer intelligence platform)

**What Went Wrong**:
- No existing market (red flag, not feature)
- Required market-making and education
- Unclear buyer (consumers? businesses?)
- No budget line existed for this

**Why It Failed**: Innovation classification was accurate, but Innovation itself was wrong choice given:
- No evidence of budget for this category
- High education costs with unclear payoff
- B2C innovation is extremely capital-intensive

**Lesson**: Innovation type requires VERY HIGH confidence (85%+) and clear budget evidence. If you can't find existing spend, the market may not exist.

**Outcome**: Archived

---

### Generic Review Management Tool — CLONE ✗

**Original Classification**: Clone (copy BirdEye)

**What Went Wrong**:
- Tried to match BirdEye feature-for-feature
- No niche focus
- No price differentiation
- Competing against well-funded incumbent on their terms

**Should Have Been**: UNDERCUT with niche focus
- Pick specific segment (restaurants, not "SMBs")
- Cut features aggressively (not match them)
- Lead with price (not feature parity)

**Lesson**: Clone without differentiation = death. Clone must have execution edge OR become Undercut with niche.

---

## Classification Anti-Pattern Summary

| Anti-Pattern | Signal You're Doing It | Correction |
|--------------|----------------------|------------|
| "Innovation" for validated market | Competitor has revenue | Reclassify as Clone/Undercut |
| Clone without edge | "We'll just do it better" | Add niche (Undercut) or exit |
| Undercut without math | Can't show 50%+ savings | Validate unit economics first |
| Slice without ecosystem | Platform has no marketplace | Reclassify as Clone/Wrapper |
| Unbundle from small platform | Platform has <1M users | Not enough volume to extract |
| Wrapper without API | "We'll scrape it" | High risk, reconsider |

## Evidence Strength Examples

### Strong Evidence (Tier 1) — Use Heavily
- Competitor pricing pages (exact numbers)
- Job postings with budget ranges
- G2/Capterra reviews with specific complaints
- Platform marketplace with app counts
- API documentation (confirms Wrapper viability)

### Moderate Evidence (Tier 2) — Use with Caution
- Reddit/forum discussions (sentiment, not budget)
- Analyst reports (often outdated)
- Competitor landing page claims (may be aspirational)
- LinkedIn job titles (shows roles exist, not budget)

### Weak Evidence (Tier 3) — Supplement Only
- User interviews (what they say vs. do)
- Survey responses (aspirational)
- Social media mentions (volume, not intent)
- Your own intuition (must be validated)
