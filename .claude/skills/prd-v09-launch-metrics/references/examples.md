# Launch Metrics Examples

**Purpose**: Good and bad patterns for defining and tracking launch metrics.

---

## Good Example 1: Slack - Clear Activation Metric

### Metric Definition

**KPI**: 2,000 messages sent by team

**Type**: Activation (leading indicator)

**Rationale**: "Teams that send 2,000 messages have experienced Slack's value and will retain"

**Data Source**: Message count per workspace (Slack's internal analytics)

---

### Why This Worked

✅ **Specific**: Exactly 2,000 messages (not "high usage")
✅ **Achievable**: Most teams hit this in 7-14 days
✅ **Predictive**: 93% of teams that hit 2,000 messages retained long-term
✅ **Actionable**: Can optimize onboarding to drive message sending

---

### Results

- Focused entire onboarding on "send your first message"
- Removed friction (no credit card, unlimited messages free)
- Growth: 15,000 users (2014) → 12M users (2019)

---

## Good Example 2: Facebook - 7 Friends in 10 Days

### Metric Definition

**KPI**: User adds 7 friends within 10 days

**Type**: Activation (leading indicator)

**Rationale**: "Users with 7 friends experience Facebook's network value and stick around"

---

### Why This Worked

✅ **Time-bound**: 10 days (not infinite)
✅ **Network-aware**: Recognized network effects as core value
✅ **Data-driven**: Tested various thresholds (5, 7, 10 friends), found 7 optimal

---

### Results

- Entire growth team focused on "get to 7 friends faster"
- Improved friend suggestions, contact imports, email invites
- Retention increased 20%+ among users who hit metric

---

## Good Example 3: Dropbox - Cohort-Based Launch

### Launch Metrics (Month 1)

**Primary KPI**: 100,000 signups

**Secondary KPIs**:
- Activation: 40% upload at least 1 file
- Retention: D30 > 30%
- Viral: k = 0.5 (referral program)

**Cohort Tracking**:
| Week | Signups | Activation | D7 Retention | D30 Retention |
|------|---------|------------|--------------|---------------|
| 1 | 25,000 | 45% | 50% | 35% |
| 2 | 30,000 | 42% | 48% | 33% |
| 3 | 25,000 | 40% | 45% | 30% |
| 4 | 20,000 | 38% | 42% | 28% |

**Insight**: Retention degrading week-over-week

**Action**: Investigated Week 1 cohort (what made them different?)
- Week 1: Mostly tech-savvy early adopters from Hacker News
- Week 2-4: Broader audience from ads, less technical

**Fix**: Improved onboarding for non-technical users, retention stabilized

---

### Why This Worked

✅ **Cohort analysis**: Caught degrading retention early
✅ **Segmented by source**: Realized different users need different onboarding
✅ **Acted quickly**: Fixed in Week 5, didn't wait for Month 3 data

---

## Bad Example 1: Vanity Metrics (Total Signups)

### What They Tracked

**Primary KPI**: Total signups (10,000 in Month 1)

**Dashboard**: Giant number "10,000 users!" (celebrating)

---

### What They Missed

**Activation**: Only 10% uploaded a file
**Retention**: D30 = 5% (95% churned)
**Reality**: 10,000 signups, but only 500 real users

---

### Why This Failed

❌ **Vanity metric**: Signups don't equal value
❌ **No activation tracking**: Didn't know users weren't "getting it"
❌ **No retention tracking**: Didn't know users leaving immediately
❌ **False success**: Team celebrated, didn't fix real problems

---

### Fix

Track activation and retention, not just signups:
- **Primary KPI**: Activated users (completed first value action)
- **Secondary KPI**: D30 retention > 30%
- **Reality check**: Only 500 activated = 95% failure rate = PIVOT NOW

---

## Bad Example 2: No Segmentation

### What They Tracked

**Overall Metrics**:
- Activation: 30%
- D30 Retention: 25%
- NPS: 35

**Conclusion**: "Metrics are okay, launch was mediocre success"

---

### What Segmentation Revealed

**By Persona**:
- Enterprise (20% of signups): 80% activation, 70% retention, NPS 60
- SMB (80% of signups): 20% activation, 15% retention, NPS 20

**Reality**: Product ONLY works for enterprise, SMB hates it

---

### Why No Segmentation Failed

❌ **Averaged away insights**: Aggregate hid that 80% of users hated it
❌ **Wrong positioning**: Marketed to everyone, should target enterprise only
❌ **Wasted budget**: Spent money acquiring SMB users who churned

---

### Fix

Segment ALL metrics by persona, channel, use case:
- Realize enterprise loves product
- Stop marketing to SMB (wasted CAC)
- Double down on enterprise (higher NPS, retention, ARPU)

---

## Bad Example 3: Waiting Too Long

### Timeline

- **Week 1**: 50 signups (target: 100) - "Let's wait, it's early"
- **Week 2**: 30 signups (target: 100) - "Hmm, concerning but wait"
- **Week 3**: 20 signups (target: 100) - "Okay now we're worried"
- **Week 4**: 10 signups (target: 100) - "Launch failed"

**Month 1 Total**: 110 signups (vs target 1,000)

---

### Why Waiting Failed

❌ **Ignored early indicators**: Week 1 data predicted Month 1 failure
❌ **No action**: Should have iterated messaging/channels by Week 2
❌ **Wasted time**: Burned 4 weeks on failing launch

---

### Fix

Act on Week 1 data:
- If Week 1 < 25% of target, something is WRONG
- Iterate immediately (new messaging, different channel, pivot)
- Don't wait for Month 1 to confirm failure

---

## Good Pattern Summary

### Launch Metric Checklist

A good launch metric has:

- [x] **Specific**: Exact number/threshold (not "high usage")
- [x] **Measurable**: Clear data source, auto-updated dashboard
- [x] **Predictive**: Leading indicator (activation predicts retention)
- [x] **Actionable**: Can improve through product/marketing changes
- [x] **Time-bound**: "Within X days" (not infinite)
- [x] **Segmented**: By persona, channel, cohort
- [x] **Realistic**: Based on benchmarks or past data
- [x] **Tied to PMF**: Metric proves users need/love product

---

## Bad Pattern Summary

### Common Launch Metric Mistakes

Avoid these anti-patterns:

- ❌ **Vanity metrics**: Total signups/downloads (not engagement)
- ❌ **No activation metric**: Don't know if users "get it"
- ❌ **No retention metric**: Don't know if users stick around
- ❌ **No segmentation**: Hide insights by averaging
- ❌ **No cohort tracking**: Miss degrading performance
- ❌ **No early indicators**: Wait 30 days to see failure
- ❌ **Too many metrics**: Track 50 things, act on none
- ❌ **Unrealistic targets**: "10x our best launch" (set up for failure)
- ❌ **No benchmark**: Don't know if 25% activation is good or bad
- ❌ **Metrics without action**: Track but don't iterate based on data

---

*Reference: Use these examples when defining launch KPIs in `prd-v09-launch-metrics` skill.*
