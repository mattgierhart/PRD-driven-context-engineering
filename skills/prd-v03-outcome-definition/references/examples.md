# Outcome Definition Examples

## Good Examples

### Example 1: HomeFalcon "Issues Resolved per Household"

**Context**: Home product management app with savings tracker (B2C, Innovation-adjacent)

**KPI Entry**:
```
KPI-001: Issues Resolved per Household per Month
Type: Tier 1 (proxy for revenue value delivered)
Category: Leading
Definition: Count of issues marked "resolved" / active households / month
Target: ≥2 issues/household/month
Evidence: CFD-012 (user research showing 2+ issues = retained user)
Downstream Gate: v0.5 Red Team — if <1 at Week 4, simplify issue flow
Measurement: Weekly via Supabase query
```

**Why it works**:
- Directly tied to user value (saved money from resolved issues)
- Actionable (can improve through better issue discovery flows)
- Correlates with retention (users who resolve issues don't churn)
- Specific threshold with evidence base

**Transferable pattern**: Pick a metric that = user outcome achieved, not user actions taken.

---

### Example 2: GearHeart "Signal → $1: 14 days"

**Context**: Micro-SaaS portfolio philosophy (applies to all products)

**KPI Entry**:
```
KPI-002: Time to First Revenue
Type: Tier 1
Category: Lagging
Definition: Calendar days from market signal identification to first paying customer
Target: ≤14 days
Evidence: BR-001 (GearHeart methodology: revenue validates)
Downstream Gate: v0.5 Red Team — if Day 21 with no revenue, mandatory pivot review
Measurement: Manual tracking in PRD changelog
```

**Why it works**:
- Forces discipline on validation vs. building
- Creates clear pass/fail gate
- Aligns team on what matters (revenue, not features)
- Time-bounded with specific escalation

**Transferable pattern**: Time-bounded revenue targets beat abstract goals.

---

### Example 3: ServiceAutoPilot Follow-Up — Leading + Lagging Split

**Context**: B2B SaaS for estimate follow-up automation (Slice/Wrapper hybrid)

**KPI Entries**:
```
KPI-003: Estimate-to-Job Conversion Rate (Customer Success)
Type: Tier 2
Category: Leading
Definition: (Jobs won from followed-up estimates) / (Total estimates followed up) × 100
Target: >15% improvement vs. customer's baseline
Evidence: CFD-045 (industry baseline 30-40%, tool should lift 5-10 points)
Downstream Gate: Beta success gate — 60% of users must see improvement
Measurement: Weekly via platform integration

KPI-004: Monthly Churn Rate
Type: Tier 1
Category: Lagging
Definition: (Customers cancelled in month) / (Customers at month start) × 100
Target: <5% monthly
Evidence: CFD-048 (SMB SaaS benchmark 3-7% monthly)
Downstream Gate: Gate 4 Unit Economics — must pass before scaling
Measurement: Monthly via Stripe
```

**Why it works**:
- Leading indicator (conversion rate) lets you act before lagging (churn) confirms failure
- Customer success metric proves value proposition
- Both have specific thresholds with benchmark evidence
- Clear gate linkages

**Transferable pattern**: Always pair leading (actionable now) with lagging (validates strategy).

---

## Bad Examples

### Bad Example 1: "50K Users"

**Context**: Acquisition evaluation (LeadGrowly listing)

**What was proposed**:
```
KPI: Total Users
Target: 50,000
```

**Why it fails**:
- No revenue correlation — 50K users with 500 paying = 1% conversion
- Vanity metric that feels good but doesn't validate business
- No threshold for what "good" looks like
- No downstream gate linkage

**Anti-pattern**: User counts without revenue conversion are noise.

**Fix**: Replace with "Paying customers" or "Trial-to-paid conversion rate"

---

### Bad Example 2: Traffic Volume Without Quality

**Context**: LeadGrowly with "88% referral traffic"

**What was proposed**:
```
KPI: Monthly Traffic
Target: 10,000 visits
Evidence: Current analytics
```

**Why it fails**:
- 0.97% engagement rate hidden behind volume
- High traffic + low engagement = quality problem
- Metric masks the real issue (traffic source quality)
- No conversion tie

**Anti-pattern**: Traffic/volume metrics hide conversion quality issues.

**Fix**: Replace with "Qualified traffic" (engagement >30 sec) or "Traffic-to-trial conversion"

---

### Bad Example 3: Arbitrary "10% Improvement"

**Context**: Found in multiple PRD drafts

**What was proposed**:
```
KPI: Conversion Rate Improvement
Target: 10% improvement
```

**Why it fails**:
- No baseline specified (10% of what?)
- No evidence for why 10% vs. 15% vs. 5%
- Round number = pulled from air
- Can't verify success without starting point

**Anti-pattern**: Targets need competitive benchmarks OR evidence from user research, never round numbers.

**Fix**: "Conversion rate improvement from [baseline X%] to [target Y%], based on [CFD-XXX competitor benchmark]"

---

## Pattern Summary

| Good Pattern | Bad Pattern |
|--------------|-------------|
| Outcome achieved (issues resolved) | Actions taken (issues created) |
| Time-bounded revenue gate | Open-ended growth goal |
| Leading + lagging pair | Lagging only |
| Threshold with evidence source | Round number target |
| Downstream gate linkage | Standalone metric |
| Product-type aligned | Generic "engagement" |
