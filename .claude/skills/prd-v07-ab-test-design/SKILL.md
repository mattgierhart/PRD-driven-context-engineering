---
name: prd-v07-ab-test-design
description: >
  Design a rigorous A/B experiment for a feature before building it, defining hypothesis, sample size,
  success threshold, holdout group, and monitoring plan during PRD v0.7 Build Execution.
  Triggers on requests to design an experiment, set up A/B test, validate a feature hypothesis, define control/treatment groups,
  or when user asks "A/B test", "experiment design", "test this hypothesis", "how do we validate this feature?",
  "split test", "feature experiment", "run an experiment before building".
  Consumes FEA-, KPI-, UJ-, EPIC- entries. Outputs experiment spec with hypothesis, sample size, and monitoring plan.
---

# A/B Test Design

Position in workflow: v0.7 Epic Scoping → **v0.7 A/B Test Design** → v0.7 Test Planning

This skill designs a rigorous experiment **before code is written**, not after. The experiment spec defines what success looks like, how many users are needed to detect it, and what monitoring is required — becoming a gate that the EPIC must pass before the feature is considered validated.

Running this skill is optional but required whenever a FEA- item involves a behavioral assumption that could be tested rather than assumed (e.g., "users will click this CTA more", "this flow will improve activation", "this pricing will convert better").

## Consumes

This skill requires prior work from v0.3-v0.7:

- **FEA-\* feature entries** (from v0.3) — The feature being tested; its definition, priority, and the user value it claims to deliver
- **KPI-\* metric entries** (from v0.3 Outcome Definition) — Primary and guardrail metrics; the experiment must target at least one primary KPI-
- **UJ-\* user journey entries** (from v0.4) — The user flow being modified; defines what step the experiment changes
- **EPIC-\* entries** (from v0.7 Epic Scoping) — The work package scope; experiment parameters must fit within EPIC constraints
- **CFD-\* baseline data** (if available, from v0.1-v0.2) — Any existing behavioral data that informs baseline conversion rates for sample size calculation

This skill assumes FEA- is defined and at least one KPI- target exists before experiment design begins.

## Produces

This skill creates:

- **Experiment spec** (documented in the EPIC or temp/ as `temp/experiment-[FEA-XXX]-spec.md`) — Complete experiment definition with all fields below
- **Sample size calculation** — Minimum users per variant needed for statistical significance at 80% power, 95% confidence
- **Monitoring plan** — Which events to track, at what cadence, and what triggers early stopping
- **EPIC gate update** — Adds "Experiment validated" as a required gate condition in the relevant EPIC before marking feature complete

All experiment specs reference the FEA- and KPI- IDs they test.

## Experiment Spec Template

```markdown
## Experiment: [Short name]

**FEA- reference**: FEA-XXX ([feature name])
**KPI- target**: KPI-XXX ([metric being tested])
**UJ- reference**: UJ-XXX ([journey step being modified])
**Added**: v0.7 (date)
**Owner**: [Decision-maker who will call the result]

---

### Hypothesis

> **If** [specific change being made],
> **then** [expected behavior change] for [target user segment],
> **because** [underlying assumption being tested].

*Example:*
> If we move the CTA above the feature description in the onboarding flow,
> then activation rate will increase by ≥8% for new users completing step 3 (UJ-002),
> because users are deciding to proceed before reading the full description.

---

### Variants

| Variant | Description | Traffic |
|---|---|---|
| Control (A) | [Current experience — no change] | 50% |
| Treatment (B) | [Specific change being tested] | 50% |

*Constraints: test ONE change per variant. No compound tests unless explicitly approved.*

---

### Success Criteria

**Primary metric**: [KPI- metric]
**Minimum detectable effect (MDE)**: [% lift required to be meaningful]
**Success threshold**: [Specific value that defines Treatment wins]

| Outcome | Definition | Decision |
|---|---|---|
| Treatment wins | Primary metric ≥ MDE, p < 0.05 | Ship Treatment to 100% |
| No significant difference | p ≥ 0.05 after full run | Ship Control (no regression) or investigate |
| Treatment loses | Primary metric significantly worse | Do not ship; escalate to PM |

---

### Guardrail Metrics

Metrics that must NOT regress during the experiment. Violation triggers early stopping.

| Guardrail Metric | KPI- reference | Acceptable range | Action if violated |
|---|---|---|---|
| [e.g., error rate] | KPI-XXX | ≤ [baseline + 0.5%] | Stop experiment immediately |
| [e.g., session length] | KPI-XXX | ≥ [baseline - 10%] | Flag and investigate |

---

### Sample Size

**Baseline conversion rate**: [X%] — Source: [CFD- entry or historical data]
**Minimum detectable effect**: [X% relative lift]
**Statistical power**: 80%
**Confidence level**: 95% (two-tailed)
**Required sample per variant**: [N users]
**Total sample needed**: [2N users]
**Estimated runtime**: [N days at current traffic volume]

*If no baseline data exists: run a 1-week measurement sprint before experiment to establish baseline.*

---

### Assignment Logic

**Unit of randomization**: [user_id | session_id | device_id]
**Assignment rule**: [Sticky by user_id for logged-in users; session for anonymous]
**Holdout group**: [X%] of traffic excluded from experiment for long-term holdout analysis
**Exclusion criteria**: [New accounts < 24h | Returning users only | Specific cohort]

---

### Monitoring Plan

**Check frequency**: Daily during runtime
**Dashboard**: [Link or description of where metrics are tracked]
**Early stopping criteria**:
- Guardrail metric violated → stop immediately, escalate
- Treatment loses with p < 0.01 and N > 50% of target → consider early stop
- Sample ratio mismatch > 1% → investigate tracking issue before continuing

**Runtime**: [Start date] → [End date] ([X days])
**Results review date**: [Date + owner]

---

### Post-Experiment Decision Protocol

| Result | Who decides | Timeline | Documentation |
|---|---|---|---|
| Treatment wins | PM + Data | Within 48h of significance | Update FEA- status, log GTM- decision |
| Inconclusive | PM + Data | Review at runtime end | Document learnings in CFD- |
| Treatment loses | PM + stakeholders | Escalate within 24h | Add to RISK- register, update PRD |
```

---

## Step 1: Hypothesis Writing

A strong hypothesis has all three components: **change → behavior → reason**.

Weak: "Moving the CTA will improve conversions."
Strong: "If we move the CTA above the feature description, then activation rate will increase ≥8% for users in UJ-002 step 3, because users decide to proceed before reading the full description."

Test your hypothesis:
- [ ] Is the change specific enough to build as exactly one treatment variant?
- [ ] Is the expected behavior measurable with an existing KPI- entry?
- [ ] Does the "because" state a falsifiable assumption?

## Step 2: Metric Selection

**Primary metric**: Choose the KPI- that most directly measures the behavior the treatment is trying to change. One primary metric per experiment.

**Guardrail metrics**: Choose 1-3 metrics that must not regress. These are typically:
- Revenue or conversion (if not primary)
- Error rates or technical performance
- Core retention metric

**Avoid**: Vanity metrics (page views, impressions) as primary metrics — they don't indicate behavior change.

## Step 3: Sample Size Calculation

Use the formula approach below (or reference `assets/sample-size-calculator.md`):

**Inputs needed**:
1. Baseline rate (from CFD- or historical data)
2. Minimum detectable effect (MDE) — the smallest lift worth shipping for
3. Power: 80% (standard)
4. Significance: 95% (standard)

**Rule of thumb**: For a 5% baseline and 10% relative MDE (wanting to detect a 5.5% rate), you need ~3,800 users per variant. For smaller baselines or smaller MDEs, sample size grows rapidly.

**If traffic is too low**: Either widen the MDE (accept only larger effects as meaningful) or extend runtime. Do not lower power or significance below 80%/95%.

## Step 4: Assignment & Holdout

**Randomization unit**: Always use `user_id` for logged-in products. Session-based randomization causes user assignment thrash and corrupts results.

**Holdout group**: Reserve 5-10% of traffic outside the experiment as a long-term holdout. This allows post-experiment measurement of whether the winning variant actually sustained its effect.

**Exclusion criteria**: Define who is excluded before the experiment starts:
- New accounts (to avoid novelty effect)
- Internal users / test accounts
- Users who triggered a known bug during the period

## Quality Gates

Before beginning EPIC implementation for the tested FEA-:

- [ ] Hypothesis has all three components (change → behavior → reason)
- [ ] Primary metric maps to an existing KPI-
- [ ] Guardrail metrics are defined with explicit thresholds
- [ ] Sample size is calculated with documented baseline rate
- [ ] Runtime is estimated based on current traffic
- [ ] Assignment logic is defined (randomization unit, holdout %)
- [ ] Owner is named for the results decision
- [ ] Early stopping criteria are documented
- [ ] Experiment spec is linked from the relevant EPIC

## Anti-Patterns to Avoid

| Anti-Pattern | Signal | Fix |
|---|---|---|
| **Compound tests** | Treatment changes CTA text AND color AND position | Test one change per variant |
| **No guardrails** | Only measuring the primary metric | Always define 1-3 guardrail metrics |
| **Peeking** | Calling the result before target sample is reached | Set a fixed end date; resist early calls |
| **No baseline** | Sample size based on assumption, not data | Measure baseline first; run calibration sprint if needed |
| **Session randomization on logged-in product** | Users flip between variants across sessions | Always use user_id for logged-in features |
| **Experiment as justification** | Design experiment to prove a decision already made | Hypothesis must be written before seeing any data |
| **Missing holdout** | Immediately ship winner to 100% | Retain holdout group through ramp-up to verify sustained effect |

## Downstream Connections

A/B Test Design feeds into:

| Consumer | What It Uses | Example |
|---|---|---|
| **v0.7 Test Planning** | TEST- entries for experiment validation | TEST- for tracking events, assignment logic, and data quality |
| **v0.7 Implementation Loop** | EPIC gate: experiment instrumentation required | Tracking events must be implemented before experiment launch |
| **v0.8 Monitoring Setup** | Monitoring plan → MON- entries | Dashboard and alert thresholds from experiment spec |
| **v0.9 Launch Metrics** | Experiment results as evidence for KPI- | Winning variant data anchors launch baseline |
| **v1.0 Retention Analyzer** | Long-term holdout results | Determines whether experiment effect was durable |
