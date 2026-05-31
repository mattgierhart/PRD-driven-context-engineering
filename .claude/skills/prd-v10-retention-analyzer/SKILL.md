---
name: prd-v10-retention-analyzer
description: >
  Analyze retention cohorts, identify churn patterns, and define the growth optimization loop during PRD v1.0 Growth.
  Converts post-launch behavioral data into structured retention findings and an optimization roadmap.
  Triggers on requests to analyze retention, investigate churn, understand why users leave, optimize growth,
  or when user asks "retention analysis", "churn analysis", "why are users churning?", "growth loop",
  "retention cohorts", "optimize retention", "user lifecycle analysis", "activation to retention".
  Consumes KPI- (actuals), CFD- (post-launch), MON- entries. Outputs cohort analysis, churn hypotheses, and growth loop definition.
---

# Retention Analyzer

Position in workflow: v0.9 Go-to-Market → **v1.0 Retention Analyzer** → Growth iteration (cycle back to v0.7 for improvements)

This skill is the primary tool for the v1.0 Growth stage — the least-defined stage of the PRD lifecycle. It converts raw post-launch behavioral signals into structured retention insight and a prioritized optimization roadmap. Unlike earlier lifecycle stages (which are forward-looking), this skill works backward from observed reality to understand why users stay or leave.

The output of this skill feeds directly back into the lifecycle: churn hypotheses generate new FEA- items, updated KPI- targets, new CFD- entries, and potentially new EPICs in v0.7 for improvements.

## Consumes

This skill requires real post-launch data:

- **KPI-\* actuals** (from v0.9 Launch Metrics — measured, not targeted) — Real activation, retention D7/D30, revenue, and usage metrics vs. KPI- targets; the gap between target and actual is the starting point
- **CFD-\* post-launch feedback** (from v0.9 Feedback Loop Setup) — User signals post-launch: support tickets, NPS responses, churn surveys, interview transcripts; source of qualitative churn signal
- **MON-\* monitoring data** (from v0.8 Monitoring Setup) — Product usage patterns, error rates, feature adoption rates by cohort; source of quantitative behavioral signals
- **FEA-\* shipped features** (from v0.3, v0.7 Implementation) — Which features are live; used to segment retention by feature adoption cohorts
- **UJ-\* journey entries** (from v0.4) — The intended flow; compared against observed behavior to identify deviation points (drop-off analysis)
- **GTM-\* entries** (from v0.9) — Acquisition channels; used to segment retention by acquisition source (some channels acquire lower-quality users)

This skill requires at minimum 2 weeks of post-launch data and is most powerful with 30+ days.

## Produces

This skill creates:

- **Cohort retention table** — D1/D7/D30/D90 retention by user cohort (saved to `temp/retention-analysis-[date].md`)
- **Churn hypothesis register** — Structured hypotheses about why users churn, each with confidence rating and evidence
- **Activation-to-retention funnel** — Where in the UJ- flow users drop before reaching the retention-driving behavior
- **Growth loop definition** — The mechanism that drives sustainable retention (acquisition → activation → habit → referral)
- **Updated KPI-\* entries** — Revised targets informed by actual data (using `ghm-id-register` for changes)
- **New CFD-\* entries** — Post-launch behavioral observations registered as customer feedback
- **EPIC candidates** — Prioritized list of improvement EPICs to bring back to v0.7 Build Execution

---

## Step 1: Retention Baseline

Before diagnosing problems, establish what the numbers actually are.

### Cohort Retention Table

Organize users by the week they first activated (completed the core UJ- onboarding step). For each cohort, measure what % returned in subsequent weeks.

```markdown
## Cohort Retention Table

| Cohort (Activation Week) | N | D1 | D7 | D30 | D90 |
|---|---|---|---|---|---|
| Week 1 (launch) | [N] | [%] | [%] | [%] | [%] |
| Week 2 | [N] | [%] | [%] | [%] | — |
| Week 3 | [N] | [%] | [%] | — | — |
| Week 4 | [N] | [%] | — | — | — |
| **Average** | | [%] | [%] | [%] | [%] |

**KPI- targets** (from v0.3 Outcome Definition):
- D7 target: KPI-XXX = [X%] | Actual: [Y%] | Gap: [Z%]
- D30 target: KPI-XXX = [X%] | Actual: [Y%] | Gap: [Z%]
```

### Retention Benchmarks by Product Type

Use these to calibrate whether gaps are critical or normal:

| Product Type | Good D7 | Good D30 | Source |
|---|---|---|---|
| Consumer social | 25-40% | 15-25% | Industry benchmarks |
| SaaS (B2B) | 50-65% | 35-50% | Industry benchmarks |
| Marketplace | 30-45% | 20-35% | Industry benchmarks |
| Consumer utility | 20-35% | 10-20% | Industry benchmarks |
| Gaming | 40-60% | 15-30% | Industry benchmarks |

---

## Step 2: Activation Funnel Analysis

"Activation" is the moment a user first experiences the core value. Users who don't activate can't retain.

Map the UJ- onboarding flow against observed drop-off:

```markdown
## Activation Funnel

| Step | UJ- reference | Expected % completing | Observed % completing | Drop-off |
|---|---|---|---|---|
| Sign up | UJ-001 step 1 | 100% | 100% | — |
| Complete profile | UJ-001 step 2 | 80% | 62% | -18% ⚠️ |
| First core action | UJ-001 step 3 | 60% | 31% | -29% 🚨 |
| Activation event | UJ-001 step 4 | 50% | 24% | -26% 🚨 |

**Activation rate**: [X%] of signups reach the activation event
**KPI- target**: KPI-XXX = [Y%] | Gap: [Z%]
```

**Activation diagnostic questions**:
- Where is the single biggest drop-off step?
- Is the drop-off consistent across cohorts or specific to one acquisition channel?
- What do users who complete activation do in the first session that non-activators don't?
- Is there a "magic action" — a behavior strongly correlated with D30 retention?

---

## Step 3: Churn Hypothesis Register

For each significant retention gap, form a falsifiable hypothesis about the cause.

```markdown
## Churn Hypothesis: [Short name]

**ID**: CHURN-XXX
**Metric impacted**: KPI-XXX ([metric and gap])
**Evidence type**: [Quantitative | Qualitative | Mixed]
**Confidence**: [High | Medium | Low]

**Hypothesis**:
> Users who [churn behavior] do so because [root cause assumption],
> as evidenced by [specific data point or CFD- entry].

**Evidence**:
- [CFD-XXX]: [Specific user quote or feedback signal]
- [MON-XXX]: [Behavioral data point supporting hypothesis]
- [Activation funnel]: [Specific drop-off point relevant to this hypothesis]

**Counter-evidence** (what would disprove this):
- [What data would suggest this hypothesis is wrong]

**Proposed test**:
- [Intervention to test this hypothesis — becomes EPIC candidate]

**Priority**: [P0 Blocking | P1 High | P2 Medium | P3 Low]
Added: v1.0 ([date])
```

### Common Churn Hypotheses by Category

Use these as prompts to generate hypotheses for your specific product:

**Activation failures**:
- Users don't understand the value before they're asked to invest effort
- Onboarding asks for too much information before showing value
- The "magic action" isn't surfaced clearly enough in the first session

**Habit failures**:
- No trigger brings users back after the first session
- The product doesn't fit naturally into existing user routines
- The core loop isn't rewarding enough to sustain repeated use

**Value delivery failures**:
- Promised value (from marketing/GTM) doesn't match delivered experience
- Core feature has friction that degrades with repeated use
- Users hit a paywall or limit before experiencing full value

**Competition failures**:
- A competitor delivers the same value with less friction
- Users switch to a workflow they already use that now covers this need
- Product pricing is not aligned with perceived value

---

## Step 4: Retention-Driving Behavior Identification

The "magic action" or "aha moment" is the behavior most predictive of long-term retention. Identify it:

1. Segment users into: retained at D30 vs. churned before D30
2. Compare their behavior in the first 3 sessions
3. Find the action that retained users took significantly more often

```markdown
## Retention-Driving Behavior Analysis

| Behavior | Retained (D30) users | Churned users | Lift |
|---|---|---|---|
| [Action A] | [X%] | [Y%] | [+Z%] |
| [Action B] | [X%] | [Y%] | [+Z%] |
| [Action C] | [X%] | [Y%] | [+Z%] |

**Identified magic action**: [Action with highest lift]
**Current % of new users reaching magic action**: [X%]
**Implication**: If we increase magic action completion by [X%], D30 retention should improve by ~[Y%]
```

---

## Step 5: Growth Loop Definition

A growth loop is a self-reinforcing cycle that drives sustainable retention and acquisition. Define it:

```markdown
## Growth Loop

**Loop type**: [Viral | Paid | Content | Product-led]

**Loop mechanics**:
1. [Acquisition trigger]: User discovers product via [channel]
2. [Activation]: User experiences [magic action] within [N sessions]
3. [Habit formation]: User returns for [specific trigger] [X times/week]
4. [Value amplification]: Repeated use makes the product more valuable (e.g., more data, more connections, more output)
5. [Referral / Expansion]: User [invites others | upgrades | advocates] because [specific reason]
6. → Loop restarts at step 1 via referral, or expands at step 5 via upgrade

**Bottleneck**: [Step in the loop with the weakest conversion — where to focus next]
**KPI- implications**: [How fixing the bottleneck maps to KPI- improvement]
```

---

## Step 6: Optimization Roadmap

Translate retention findings into prioritized EPIC candidates for v0.7 Build Execution.

```markdown
## Retention Optimization Roadmap

| Priority | Churn Hypothesis | Proposed EPIC | KPI- impact | Effort estimate |
|---|---|---|---|---|
| P0 | CHURN-001 | Redesign activation step 3 (UJ-001) | D7 +8-12% | Medium |
| P1 | CHURN-002 | Add D3 re-engagement email trigger | D30 +5-8% | Low |
| P2 | CHURN-003 | Surface magic action earlier in onboarding | Activation +15% | Medium |
| P3 | CHURN-004 | Add usage summary notification (habit trigger) | D90 +5% | Low |

**Next EPIC**: [EPIC-XX title] — addresses [CHURN-XXX] by [intervention description]
```

---

## KPI- Update Protocol

When actual data materially differs from KPI- targets, update the entries:

1. Do not delete the original target — add an "Actuals" row
2. Document the gap and rationale for any target revision
3. Register changes with `ghm-id-register` noting `Added: v1.0`
4. Update README.md KPI dashboard via `ghm-status-sync`

---

## Quality Gates

Before closing a retention analysis cycle:

- [ ] Cohort retention table complete for all cohorts with ≥2 weeks of data
- [ ] Activation funnel mapped against UJ- entries with observed drop-off rates
- [ ] At least 3 churn hypotheses documented with evidence and confidence ratings
- [ ] Retention-driving behavior (magic action) identified and quantified
- [ ] Growth loop defined with bottleneck identified
- [ ] Optimization roadmap produced with at least 1 P0 EPIC candidate
- [ ] KPI- entries updated with actuals (not just targets)
- [ ] New CFD- entries registered for qualitative signals from post-launch feedback
- [ ] Findings saved to `temp/` pending harvest to SoT via `ghm-harvest`

## Anti-Patterns to Avoid

| Anti-Pattern | Signal | Fix |
|---|---|---|
| **Aggregate-only analysis** | "Our D30 is 25%" with no cohort breakdown | Break by acquisition week, channel, and feature adoption |
| **Hypothesis without evidence** | "Users churn because the UI is confusing" | Every hypothesis needs at least one CFD- or MON- data point |
| **Optimization without prioritization** | 20 EPIC candidates with no priority | Force-rank by (KPI- impact × confidence) / effort |
| **No magic action search** | Skip step 4 | The retention-driving behavior is the highest-leverage intervention |
| **Retention theater** | Analysis produced but never leads to EPICs | Retention analysis must always produce at least one EPIC candidate |
| **Ignoring acquisition quality** | Aggregating all cohorts | Segment by acquisition channel; bad-fit users inflate churn |

## Downstream Connections

Retention Analyzer feeds back into the lifecycle:

| Consumer | What It Uses | Example |
|---|---|---|
| **v0.7 Implementation Loop** | EPIC candidates from optimization roadmap | CHURN-001 → new EPIC-XX for onboarding redesign |
| **v0.3 Outcome Definition** | Revised KPI- targets | D30 target revised from 40% to 30% based on actuals |
| **SoT/CFD** | New post-launch behavioral observations | CFD entries for churn survey responses |
| **v0.9 Feedback Loop Setup** | Gaps in feedback channels revealed by analysis | Add churn exit survey if not already in place |
| **v0.5 Multi-Perspective Review** | Retention data as evidence for future reviews | Retention cohort data as CFD- input for next product iteration |
