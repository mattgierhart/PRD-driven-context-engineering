# KPI-XXX: [Launch Metric Name]

**ID**: KPI-XXX
**Type**: [Acquisition | Activation | Engagement | Retention | Revenue | Referral]
**Category**: [Leading Indicator | Lagging Indicator | Vanity Metric]
**Product/Feature**: [What's being measured - e.g., Dark Mode Launch, Premium Tier]
**Owner**: [Product Manager, Growth Lead]
**Created**: YYYY-MM-DD
**Launch Date**: YYYY-MM-DD
**Measurement Period**: [Week 1 | Month 1 | Quarter 1]
**Status**: [Tracking | Met | Missed | Iterating]

---

## Metric Definition

**What We're Measuring**:
[Specific, quantifiable metric - e.g., "Number of users who activate dark mode within 7 days of feature availability"]

**Why It Matters**:
[Connection to business outcome - e.g., "Feature adoption indicates product-market fit and validates development investment"]

**Target Value**: [Specific number - e.g., 1,000 activated users]

**Current Value**: [Actual number - updated regularly]

**Baseline** (if applicable):
[Pre-launch baseline for comparison - e.g., "0 (new feature)" or "500 users on old version"]

---

## Measurement Formula

**Calculation**:
```
[Numerator] ÷ [Denominator] × 100 (if percentage)

Example:
(Users who enabled dark mode) ÷ (Total active users) × 100 = 25% adoption rate
```

**Data Source**:
- **Primary**: [Tool/Database - e.g., Mixpanel event "dark_mode_enabled", User table column "dark_mode_preference"]
- **Backup**: [Alternative source - e.g., SQL query on user_settings table]

**Refresh Frequency**: [Real-time | Daily | Weekly | Monthly]

**Dashboard Location**: [Link to dashboard - e.g., Looker Dashboard "Launch Metrics" or Mixpanel Board "Dark Mode Launch"]

---

## Success Criteria

### Thresholds

**Success** (Green):
- **Target**: [Primary goal - e.g., ≥ 1,000 activated users]
- **Stretch**: [Aspirational - e.g., ≥ 1,500 activated users]

**Caution** (Yellow):
- **Range**: [Below target but not failure - e.g., 500-999 activated users]
- **Action**: Iterate messaging, improve onboarding

**Failure** (Red):
- **Threshold**: [Unacceptable - e.g., < 500 activated users]
- **Action**: Reassess product-market fit, consider pivot or kill

---

### Time-Bound Goals

**Week 1** (Early Indicator):
- **Goal**: [Short-term - e.g., 100 activated users]
- **Rationale**: On-track indicator (10% of monthly goal)

**Month 1** (Primary Target):
- **Goal**: [Main goal - e.g., 1,000 activated users]
- **Rationale**: Product-market fit validation

**Month 3** (Growth Indicator):
- **Goal**: [Scale indicator - e.g., 5,000 activated users]
- **Rationale**: Sustained growth, word-of-mouth working

---

## Segmentation

**By User Type**:
- **New Users**: [Goal - e.g., 30% adoption among new signups]
- **Existing Users**: [Goal - e.g., 20% adoption among existing active users]

**By Persona**:
- **[PER-101: Power Users]**: [Expected higher adoption - e.g., 50%]
- **[PER-102: Casual Users]**: [Expected lower adoption - e.g., 15%]

**By Channel**:
- **Email Campaign**: [Conversion - e.g., 5% of email clicks → activation]
- **In-App Prompt**: [Conversion - e.g., 25% of prompt views → activation]
- **Organic Discovery**: [Baseline - e.g., 2% discover and activate without prompt]

**By Geography** (if applicable):
- **US**: [Target - e.g., 40% of US users]
- **EU**: [Target - e.g., 35% of EU users]
- **APAC**: [Target - e.g., 25% of APAC users]

---

## Metric Type & Classification

### Leading vs Lagging

**Leading Indicator** (Predicts Future Success):
- Example: Email open rate (predicts signups)
- Use: Early signal, can course-correct quickly

**Lagging Indicator** (Confirms Past Success):
- Example: Revenue (confirms GTM worked)
- Use: Final validation, slower to change

**This Metric Is**: [Leading | Lagging | Both]

---

### Actionable vs Vanity

**Actionable Metric** (Can Improve Through Action):
- Example: Activation rate (improve onboarding → increase metric)
- Characteristic: Tied to specific action, clear causation

**Vanity Metric** (Looks Good, Doesn't Drive Decisions):
- Example: Total signups (doesn't show engagement or revenue)
- Characteristic: Goes up over time, not actionable

**This Metric Is**: [Actionable | Vanity]

**Why Actionable** (if applicable):
[What actions improve this metric - e.g., "Improve in-app onboarding → increase activation rate"]

---

## Related Metrics (North Star & Supporting)

### Primary KPI (This One):
[The main metric being tracked]

### Supporting Metrics (Context):

**Upstream** (Funnel Top):
- [Metric that leads to this - e.g., "Feature exposure" (users who saw dark mode option)]
- **Current**: [Value]
- **Target**: [Value]

**Downstream** (Funnel Bottom):
- [Metric this leads to - e.g., "Dark mode retention" (users still using after 30 days)]
- **Current**: [Value]
- **Target**: [Value]

**Quality** (Cohort Health):
- [Metric indicating quality - e.g., "NPS among dark mode users"]
- **Current**: [Value]
- **Target**: [Value]

---

## Benchmarks & Comparisons

### Industry Benchmarks

**Category**: [Industry - e.g., SaaS, E-commerce, Consumer Social]

**Comparable Metrics**:
- **Feature Adoption**: 10-30% (typical for optional features)
- **Activation Rate**: 30-50% (for core features)
- **Retention D30**: 20-40% (for new features)

**Our Target Position**: [Where we aim - e.g., "Top quartile (25%+ adoption)"]

---

### Internal Benchmarks

**Similar Past Launches**:
- **[Feature A]**: 15% adoption in Month 1
- **[Feature B]**: 25% adoption in Month 1
- **[Feature C]**: 10% adoption in Month 1

**Learning**: [Insight - e.g., "Features with in-app prompts get 2x adoption vs email-only"]

**This Launch Prediction**: [Estimate based on past - e.g., "20-25% adoption expected (in-app prompt planned)"]

---

## Tracking & Reporting

### Weekly Check-In

**When**: [Day/Time - e.g., Every Monday 10 AM]

**Who**: Product Manager, Engineering Lead, Marketing

**Format**:
```
KPI-XXX Weekly Update:
- Current: [Value] (was [Last Week Value])
- Target: [Value]
- Status: [On Track | Behind | Ahead]
- Blockers: [Any issues]
- Actions: [What we're doing this week]
```

---

### Dashboard View

**Visualization**: [Type - e.g., Line chart (adoption over time), Funnel (exposure → activation)]

**Filters**:
- Date range (Last 7 days, Last 30 days, Since launch)
- User segment (New, Existing, Power users)
- Channel (Email, In-app, Organic)

**Alerts**:
- **Red Alert**: Metric drops below [threshold] for [duration]
- **Yellow Alert**: Metric below target but above failure threshold
- **Green**: On track or exceeding

---

## Insights & Actions

### If Metric is Green (Exceeding Target):

**Hypotheses Why**:
1. [Reason 1 - e.g., "In-app prompt more effective than expected"]
2. [Reason 2 - e.g., "High demand for dark mode (users requested)"]

**Actions**:
- [ ] **Celebrate**: Share win with team
- [ ] **Analyze**: What worked? (for future launches)
- [ ] **Scale**: Increase promotion budget, expand to more users
- [ ] **Document**: Case study for marketing

---

### If Metric is Yellow (Below Target, Above Failure):

**Hypotheses Why**:
1. [Reason 1 - e.g., "Onboarding not clear enough"]
2. [Reason 2 - e.g., "Target audience smaller than expected"]

**Actions**:
- [ ] **Iterate**: A/B test new onboarding flows
- [ ] **Re-message**: Change email copy, in-app prompts
- [ ] **Extend timeline**: Give it 2 more weeks before pivot
- [ ] **User research**: Interview users who didn't adopt

---

### If Metric is Red (Failure Threshold):

**Hypotheses Why**:
1. [Reason 1 - e.g., "No demand for feature (wrong problem)"]
2. [Reason 2 - e.g., "Buggy implementation (users tried, failed, gave up)"]

**Actions**:
- [ ] **STOP promotion**: Don't acquire more users to broken feature
- [ ] **Root cause**: User interviews, check error logs
- [ ] **Pivot or Kill**: If no demand, kill feature
- [ ] **Fix & Relaunch**: If fixable bug, fix and re-promote

---

## Linked IDs

**GTM Strategy**:
- [GTM-XXX]: [Go-to-market plan for this launch]

**Product Features**:
- [FEA-XXX]: [Features being measured]

**User Journeys**:
- [UJ-XXX]: [User journey this metric tracks]

**Business Rules**:
- [BR-XXX]: [Business rules tied to success (e.g., pricing, feature access)]

**Personas**:
- [PER-XXX]: [Primary persona this metric targets]

**Competitive Analysis**:
- [CFD-XXX]: [Market validation for this metric]

**Tests**:
- [TEST-XXX]: [A/B tests running to improve this metric]

---

## Post-Launch Review

**Date**: [30 days post-launch]

**Final Results**:
- **Target**: [Original goal]
- **Actual**: [What we hit]
- **Status**: [Met | Missed | Exceeded]

**What Worked**:
- [Success factor 1]
- [Success factor 2]

**What Didn't Work**:
- [Failure factor 1]
- [Failure factor 2]

**Lessons for Next Launch**:
- [Learning 1 - e.g., "In-app prompts drive 3x more adoption than email"]
- [Learning 2 - e.g., "Week 1 adoption predicts Month 1 with 80% accuracy"]

**Recommendations**:
- [ ] Keep: [What to repeat]
- [ ] Improve: [What to fix]
- [ ] Kill: [What to stop]

---

## Version History

| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | YYYY-MM-DD | Initial KPI definition | [Name] |
| 1.1 | YYYY-MM-DD | Updated target based on Week 1 data | [Name] |
| | | | |

---

## Notes

[Any additional context, assumptions, dependencies, or caveats]

---

*Template: Use this to create KPI-XXX entries for launch metrics in SoT or separate metrics documents.*
