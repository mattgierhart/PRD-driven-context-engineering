# Launch Metrics Guide

**Purpose**: Framework for selecting and tracking launch-specific metrics vs growth metrics, with emphasis on early indicators and product-market fit signals.

---

## Launch Metrics vs Growth Metrics

| Dimension | Launch Metrics | Growth Metrics |
|-----------|---------------|----------------|
| **Time Horizon** | Days 1-90 | Months 3-12+ |
| **Focus** | Validation | Scale |
| **Questions** | "Does anyone want this?" | "How fast can we grow?" |
| **Key Metrics** | Activation, early retention, NPS | CAC, LTV, viral coefficient |
| **Decision** | Pivot, iterate, or scale | Optimize, invest, or maintain |

---

## AARRR Framework for Launches

### Acquisition (How Many Sign Up?)

**Launch Focus**: Initial traffic and signup rate

**Key Metrics**:
- **Signups** (absolute number)
- **Signup rate** (visitors → signups)
- **Source attribution** (which channel drove signups)

**Targets by Product Type**:
- **B2C**: 1,000-10,000 signups Month 1
- **B2B (self-serve)**: 100-1,000 signups Month 1
- **B2B (sales-led)**: 50-200 qualified leads Month 1

**Good**:
```
Week 1: 100 signups
Week 2: 150 signups (+ 50% growth)
Week 3: 250 signups (+ 67% growth)
Week 4: 400 signups (+ 60% growth)
→ Accelerating growth = good signal
```

**Bad**:
```
Week 1: 500 signups
Week 2: 300 signups (- 40%)
Week 3: 200 signups (- 33%)
Week 4: 150 signups (- 25%)
→ Decelerating = hype wore off, no sustained demand
```

---

### Activation (Do They Experience Value?)

**Launch Focus**: Do users "get it" and reach "aha moment"?

**Key Metrics**:
- **Activation rate** (signups → activated users)
- **Time to value** (how long to reach aha moment)
- **Onboarding completion** (% who finish setup)

**Activation Definitions** (Examples):
- **Slack**: Sent 2,000 messages (team engaged)
- **Dropbox**: Uploaded 1 file (saw value)
- **Facebook**: Added 7 friends in 10 days (network built)
- **Superhuman**: Achieved inbox zero (experienced speed)

**Targets**:
- **Good**: 40-60% activation rate
- **Great**: 60-80% activation rate
- **Exceptional**: 80%+ activation rate

**Time to Value**:
- **Immediate**: < 5 minutes (consumer apps)
- **Fast**: < 1 hour (simple SaaS)
- **Moderate**: < 1 day (complex SaaS)
- **Slow**: < 1 week (enterprise)

---

### Retention (Do They Come Back?)

**Launch Focus**: Early retention (Days 1, 7, 30)

**Key Metrics**:
- **D1 retention**: % who return Day 1
- **D7 retention**: % who return Week 1
- **D30 retention**: % who return Month 1

**Retention Curves**:

**Good Retention** (Plateaus):
```
D1: 60%
D7: 40%
D14: 35%
D30: 30%
→ Stabilizes around 30% = product-market fit
```

**Bad Retention** (Continuous Decline):
```
D1: 60%
D7: 30%
D14: 15%
D30: 5%
→ Heading to zero = no retention, no PMF
```

**Targets by Product Type**:
- **Social/Communication**: D30 > 50%
- **Productivity/SaaS**: D30 > 30%
- **E-commerce**: D30 > 20%
- **Content/Media**: D30 > 40%

---

### Revenue (Do They Pay?)

**Launch Focus**: Willingness to pay (conversion rate)

**Key Metrics**:
- **Free → Paid conversion** (% who upgrade)
- **Time to convert** (days from signup to paid)
- **ARPU** (Average Revenue Per User)

**Conversion Benchmarks**:
- **Freemium SaaS**: 2-5% conversion (good)
- **Free trial SaaS**: 10-25% conversion (good)
- **E-commerce**: 1-3% visitor → purchase (good)

**Time to Convert**:
- **Immediate**: < 1 day (impulse)
- **Short**: 1-7 days (trial/evaluation)
- **Medium**: 7-30 days (consideration)
- **Long**: 30+ days (enterprise)

**Launch Goal** (Month 1):
- Validate: At least 10 paying customers
- Early indicator: 2-5% conversion rate
- Prove: People will pay, not just use for free

---

### Referral (Do They Tell Others?)

**Launch Focus**: Word-of-mouth and viral coefficient

**Key Metrics**:
- **Viral coefficient (k)**: Avg invites per user × conversion rate
- **NPS**: Net Promoter Score (would recommend?)
- **Share rate**: % who share/invite

**Viral Coefficient**:
```
k = (Invites per user) × (Invite conversion rate)

Example:
- Each user invites 5 friends
- 20% of invites sign up
- k = 5 × 0.20 = 1.0

If k > 1.0: Viral growth (exponential)
If k = 0.5-1.0: Strong word-of-mouth (helpful)
If k < 0.5: Weak word-of-mouth (rely on paid)
```

**NPS Benchmarks**:
- **Exceptional**: NPS > 70 (Apple, Tesla)
- **Great**: NPS 50-70 (Netflix, Amazon)
- **Good**: NPS 30-50 (Most SaaS)
- **Poor**: NPS < 30 (churn risk)

**Launch Goal**:
- NPS > 40 (users like it enough to recommend)
- k > 0.3 (some organic growth)

---

## Leading vs Lagging Indicators

### Leading Indicators (Early Signals)

**Purpose**: Predict future success, course-correct quickly

**Week 1 Metrics**:
- **Email open rate** (20-30% = good)
  - Predicts: Signup interest
  - Action: If < 15%, rewrite subject lines

- **Landing page conversion** (10-20% = good)
  - Predicts: Product interest
  - Action: If < 5%, messaging unclear

- **Activation rate** (40-60% = good)
  - Predicts: D30 retention
  - Action: If < 30%, fix onboarding

- **D1 retention** (40-60% = good)
  - Predicts: D30 retention
  - Action: If < 30%, no aha moment

**Use Leading Indicators**:
- Week 1 data predicts Month 1 outcome
- If leading indicators off, pivot messaging/onboarding NOW
- Don't wait 30 days to realize launch failed

---

### Lagging Indicators (Confirm Success)

**Purpose**: Validate past decisions, measure ultimate outcome

**Month 1 Metrics**:
- **D30 retention** (confirms PMF)
- **Revenue** (confirms monetization)
- **LTV** (confirms unit economics)
- **CAC payback** (confirms scalability)

**Use Lagging Indicators**:
- Month 1: Confirm launch success or failure
- Month 3: Decide to scale or pivot
- Month 6: Decide to invest more or maintain

---

## Product-Market Fit Signals

### How to Know If Launch Succeeded

**Quantitative Signals**:
1. **Retention curve flattens** (D30 > 30%)
2. **Organic growth** (k > 0.5 or 20%+ referrals)
3. **Revenue grows** (MRR up-and-to-right)
4. **NPS > 40** (users love it)
5. **Usage increasing** (DAU/MAU ratio improving)

**Qualitative Signals**:
1. **Unsolicited testimonials** (users tweet/email praise)
2. **Press mentions** (organic, not from your PR)
3. **Feature requests** (users asking for more)
4. **Users paying** (upgrading without prompting)
5. **Hard to keep up** (inbound overwhelming)

---

### PMF Stages

**No PMF** (Pivot or Kill):
- D30 retention < 20%
- No organic growth
- Users don't care if product disappeared

**Weak PMF** (Iterate):
- D30 retention 20-30%
- Some organic growth (k = 0.2-0.5)
- Small group of power users, but not broad

**Strong PMF** (Scale):
- D30 retention > 30%
- Organic growth (k > 0.5)
- Users would be "very disappointed" if product went away

**Exceptional PMF** (Pour Gas on Fire):
- D30 retention > 50%
- Viral growth (k > 1.0)
- Users can't imagine life without product

---

## Metric Selection by Product Type

### B2C (Consumer)

**Primary Metrics**:
1. **DAU/MAU** (Daily Active / Monthly Active)
   - Target: > 20% (engaged user base)
2. **D30 Retention**
   - Target: > 40%
3. **Viral Coefficient**
   - Target: k > 0.5

**Why**: Consumer products need engagement + virality to scale

---

### B2B Self-Serve (PLG - Product-Led Growth)

**Primary Metrics**:
1. **Activation Rate**
   - Target: > 40%
2. **Free → Paid Conversion**
   - Target: > 2%
3. **D30 Retention**
   - Target: > 30%

**Why**: Self-serve needs fast onboarding + clear value to convert

---

### B2B Sales-Led (Enterprise)

**Primary Metrics**:
1. **Qualified Leads**
   - Target: 50-200 MQLs/month
2. **Demo Conversion**
   - Target: > 20% (demo → pipeline)
3. **Sales Cycle Length**
   - Target: < 90 days

**Why**: Enterprise has longer cycle, focus on pipeline quality

---

### Marketplace (Two-Sided)

**Primary Metrics**:
1. **Supply Activation** (sellers listing items)
   - Target: > 30%
2. **Demand Activation** (buyers purchasing)
   - Target: > 5%
3. **Liquidity** (% of listings that sell)
   - Target: > 50% sell within 30 days

**Why**: Marketplaces need both sides, measure balance

---

## Cohort Analysis

### Why Cohorts Matter

**Aggregate Metrics Lie**:
```
Total Users: 10,000 (looks good!)

But by cohort:
- January: 1,000 users, D30 retention 50% (great!)
- February: 2,000 users, D30 retention 30% (okay)
- March: 7,000 users, D30 retention 10% (terrible!)

→ Recent cohorts terrible, but total users growing = hidden problem
```

---

### Cohort Table Example

| Cohort | D1 | D7 | D14 | D30 |
|--------|----|----|-----|-----|
| **Week 1** | 60% | 40% | 35% | 30% |
| **Week 2** | 55% | 35% | 28% | 22% |
| **Week 3** | 50% | 30% | 20% | 15% |
| **Week 4** | 45% | 25% | 15% | 10% |

**Insight**: Retention degrading week-over-week = product getting worse or wrong users acquired

**Action**: Investigate why Week 1 cohort retained better (different messaging? different user type?)

---

## Dashboard Design

### Launch Dashboard (First 30 Days)

**Top Section** (At-a-Glance):
- Total Signups: [Number] (vs target)
- Activation Rate: [%] (vs target)
- D7 Retention: [%] (vs target)
- NPS: [Score]

**Acquisition**:
- Signups by Day (line chart)
- Signups by Channel (bar chart)

**Activation**:
- Activation Rate by Cohort (table)
- Time to Activate (histogram)

**Retention**:
- Retention Curve (line chart: D1, D7, D14, D30)
- Cohort Retention Table

**Revenue** (if applicable):
- Free → Paid Conversion (%)
- MRR (line chart)

---

### Red Flags (Alert When)

- **Signups declining** week-over-week
- **Activation rate < 30%** (users not getting value)
- **D7 retention < 30%** (users not coming back)
- **Retention curve not flattening** (no PMF)
- **NPS < 20** (users unhappy)

---

## Common Mistakes

### Mistake 1: Focusing on Vanity Metrics

**Bad**: "We got 10,000 signups!" (but 95% churned)

**Good**: "We got 1,000 signups, 50% activated, 40% retained D30"

---

### Mistake 2: Ignoring Cohorts

**Bad**: Looking at total users (aggregate)

**Good**: Comparing Week 1 vs Week 2 vs Week 3 cohorts

---

### Mistake 3: Waiting Too Long

**Bad**: Wait 90 days to see D30 retention

**Good**: Look at D1, D7 retention in Week 1 (early indicators)

---

### Mistake 4: Not Segmenting

**Bad**: Overall activation rate 30%

**Good**: Power users 60%, casual users 15% (different products for different users)

---

### Mistake 5: Measuring Everything

**Bad**: Tracking 50 metrics, paralysis by analysis

**Good**: Pick 3-5 primary metrics, ignore the rest for launch

---

*Reference: Use this guide when defining launch KPIs in `prd-v09-launch-metrics` skill.*
