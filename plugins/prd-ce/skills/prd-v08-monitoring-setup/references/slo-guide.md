# SLO (Service Level Objective) Guide

**Purpose**: Teach teams how to define, calculate, and alert on SLOs with error budgets.

---

## Core Concepts

### SLI (Service Level Indicator)

A **metric** that measures a specific aspect of service quality.

**Examples**:
- Request success rate (non-500 responses / total responses)
- Request latency (p95 response time)
- Availability (uptime / total time)

**Good SLI Characteristics**:
- **Measurable**: Can be calculated from existing data
- **User-Centric**: Reflects user experience (not internal metrics)
- **Actionable**: Changes indicate when to improve vs ship features

---

### SLO (Service Level Objective)

A **target** for an SLI over a time window.

**Examples**:
- "99.9% of requests succeed (non-5xx) over rolling 30 days"
- "95% of requests complete in < 500ms (p95) over rolling 7 days"
- "99.5% uptime over calendar month"

**Good SLO Characteristics**:
- **Specific**: Exact threshold and time window
- **Realistic**: Achievable with current architecture
- **Meaningful**: Matches user expectations and business requirements

---

### Error Budget

The **allowed failure rate** implied by the SLO.

**Formula**:
```
Error Budget = 100% - SLO Target
```

**Examples**:
- 99.9% SLO = 0.1% error budget = 43.2 minutes downtime/month
- 99.5% SLO = 0.5% error budget = 3.6 hours downtime/month
- 99.0% SLO = 1.0% error budget = 7.2 hours downtime/month

**Purpose**:
- **Balances** reliability vs innovation
- **Quantifies** acceptable risk
- **Informs** feature vs stability tradeoffs

---

## Calculation Examples

### Example 1: Availability SLO

**SLO**: 99.9% availability over rolling 30 days

**Calculation**:
```
Total time in 30 days: 30 days × 24 hours × 60 minutes = 43,200 minutes
Error budget: 43,200 × (100% - 99.9%) = 43,200 × 0.1% = 43.2 minutes

Allowed downtime: 43.2 minutes per 30 days
```

**In Practice**:
- Track uptime monitoring (Pingdom, Checkly, etc.)
- Calculate: (uptime minutes / total minutes) × 100%
- Alert when: approaching 43 minutes downtime in rolling 30-day window

---

### Example 2: Request Success Rate SLO

**SLO**: 99.95% of API requests succeed (non-5xx) over rolling 7 days

**Calculation**:
```
Error budget: 100% - 99.95% = 0.05%

If you serve 10M requests/week:
Allowed failures: 10,000,000 × 0.05% = 5,000 failed requests/week
```

**In Practice**:
- Track: (non-5xx responses / total responses)
- Calculate over rolling 7-day window
- Alert when: > 2,500 failures in 7 days (50% budget consumed)

---

### Example 3: Latency SLO

**SLO**: 95% of requests complete in < 500ms (p95 latency) over rolling 24 hours

**Calculation**:
```
Error budget: 5% of requests can exceed 500ms

If you serve 1M requests/day:
Allowed slow requests: 1,000,000 × 5% = 50,000 slow requests/day
```

**In Practice**:
- Track p95 latency per request
- Calculate: (requests < 500ms / total requests)
- Alert when: p95 latency > 500ms or slow request count exceeds budget

---

## Choosing SLO Targets

### Start With User Expectations

**Question**: "What performance do users expect?"

**Good Pattern**:
1. Measure current performance for 2-4 weeks
2. Set SLO just below current performance (leaves improvement room)
3. Validate with user research or support tickets

**Example**:
- Current p95 latency: 300ms
- User research: Users frustrated when pages load > 1 second
- **Chosen SLO**: 95% of requests < 500ms (buffer between current and frustration point)

---

### Industry Benchmarks

**Web Applications**:
- **Availability**: 99.9% (43 min/month downtime) to 99.95% (21 min/month)
- **Latency (p95)**: < 500ms for interactive pages, < 200ms for API calls
- **Error Rate**: < 0.1% (99.9% success rate)

**Internal Tools**:
- **Availability**: 99% (7.2 hours/month) to 99.5% (3.6 hours/month)
- **Latency (p95)**: < 1s (less critical than customer-facing)
- **Error Rate**: < 1% (99% success rate)

**Critical Infrastructure (Payments, Health, Safety)**:
- **Availability**: 99.99% (4.3 min/month) to 99.999% (26 seconds/month)
- **Latency (p95)**: < 200ms
- **Error Rate**: < 0.01% (99.99% success rate)

---

### Cost-Benefit Tradeoff

**Pattern**: Each "9" of reliability increases cost significantly.

| SLO | Downtime/Month | Typical Cost Multiplier | When to Use |
|-----|---------------|-------------------------|-------------|
| 99% | 7.2 hours | 1x (baseline) | Internal tools, MVPs |
| 99.5% | 3.6 hours | 1.5-2x | Standard web apps |
| 99.9% | 43 minutes | 2-4x | Customer-facing SaaS |
| 99.95% | 21 minutes | 4-6x | Business-critical SaaS |
| 99.99% | 4.3 minutes | 8-12x | Payments, healthcare, safety-critical |

**Example Decision**:
- Early-stage SaaS: Start with 99.5% (prioritize features over reliability)
- Post-PMF SaaS: Move to 99.9% (reliability becomes competitive advantage)
- Enterprise contracts: Negotiate 99.95% (SLA requirements)

---

## Error Budget Policies

### Budget Consumption Thresholds

**50% Budget Consumed** (Warning):
- **Action**: Review incidents, identify trends
- **Decision**: Continue shipping features if no systemic issues
- **Alert**: Notify team via Slack (not page)

**75% Budget Consumed** (Critical):
- **Action**: Root cause analysis required
- **Decision**: Pause non-critical feature work, prioritize reliability
- **Alert**: Page on-call lead

**90% Budget Consumed** (Emergency):
- **Action**: Feature freeze except reliability work
- **Decision**: All hands on stability
- **Alert**: Escalate to engineering leadership

**100% Budget Exhausted** (Breach):
- **Action**: Post-mortem required, update SLO or architecture
- **Decision**: Continue feature freeze until budget resets or SLO revised
- **Communication**: Notify customers (if SLA attached)

---

### Burn Rate Alerting

**Problem**: Waiting to consume 50% of monthly budget means slow response to incidents.

**Solution**: Alert on **rate of consumption** (burn rate).

#### Fast Burn Alert (1-hour window)

**Trigger**: Consuming error budget at 14.4x normal rate

**Formula**:
```
For 30-day SLO with 0.1% error budget:
Fast burn = 0.1% × 30 days / 1 hour = 0.1% × 720 hours / 1 hour = 72× normal error rate

Practical threshold: 14.4× gives 2-hour MTTR before 10% budget consumed
```

**Action**: Page on-call immediately (potential outage)

**Example**:
- Normal error rate: 0.1%
- Fast burn threshold: 1.44% error rate over 1 hour
- If triggered: Major incident, page on-call

---

#### Slow Burn Alert (6-hour window)

**Trigger**: Consuming error budget at 6x normal rate

**Action**: Notify team via Slack (degraded performance, not outage)

**Example**:
- Normal error rate: 0.1%
- Slow burn threshold: 0.6% error rate over 6 hours
- If triggered: Investigate, may need rollback or fix

---

### Multi-Window Alerting (Recommended)

Combine fast and slow burn for balanced alerting:

```
Alert when:
  (Error rate > 14.4× normal over 1 hour) OR
  (Error rate > 6× normal over 6 hours)
```

**Benefits**:
- Fast burn: Catches outages quickly
- Slow burn: Catches gradual degradation
- Reduces false positives (requires sustained error rate)

---

## SLO Implementation Patterns

### Pattern 1: Start Simple (Single SLO)

**For**: Early-stage products, first SLO

**Recommended SLO**: Request success rate (availability)

**Why**:
- Easiest to measure (count 5xx vs non-5xx)
- Directly maps to user experience
- Easy to explain to stakeholders

**Example**:
```
SLI: (non-5xx responses / total responses)
SLO: 99.9% over rolling 30 days
Error Budget: 0.1% (43.2 min/month equivalent)
```

---

### Pattern 2: Multi-SLO (Mature Products)

**For**: Post-PMF products with clear user journeys

**Recommended SLOs**:
1. **Availability**: 99.9% request success rate
2. **Latency**: 95% of requests < 500ms (p95)
3. **Data Freshness**: 99% of data updated within 5 minutes (if applicable)

**Error Budget Policy**: Must satisfy **all** SLOs, not just average.

**Example**:
- If availability SLO met but latency SLO breached → still in error budget breach state
- Prevents "fast but broken" or "slow but up" scenarios

---

### Pattern 3: Per-Journey SLOs (Advanced)

**For**: Complex applications with distinct user journeys

**Approach**: Define SLOs per critical journey (UJ-XXX)

**Example** (E-commerce):
- **UJ-101 (Browse Catalog)**: 99.5% availability, < 1s latency (less critical)
- **UJ-102 (Checkout)**: 99.95% availability, < 500ms latency (critical revenue path)
- **UJ-103 (Order Status)**: 99% availability, < 2s latency (read-only, less critical)

**Benefits**:
- Prioritize reliability where it matters most
- Optimize costs (don't over-engineer low-impact journeys)
- Clear tradeoffs for product vs engineering

---

## Common Anti-Patterns

### Anti-Pattern 1: SLOs Without Error Budgets

**Problem**: Treating any downtime as unacceptable (SRE burnout, no innovation).

**Example**: "We must have 100% uptime" → Team afraid to deploy.

**Fix**: Explicitly define error budget, communicate it's **okay** to use budget for innovation.

---

### Anti-Pattern 2: Vanity SLOs (Too Ambitious)

**Problem**: Setting 99.99% SLO without architecture to support it.

**Example**: Monolith app with single DB, no failover, 99.99% SLO.

**Fix**: Set SLO based on current architecture, plan improvements if business requires higher SLO.

---

### Anti-Pattern 3: Internal Metrics as SLIs

**Problem**: Measuring server CPU % instead of user-facing latency.

**Example**: SLO of "CPU < 80%" instead of "p95 latency < 500ms".

**Fix**: Always measure user-facing outcomes (latency, errors, availability).

---

### Anti-Pattern 4: No Alerting on Error Budget

**Problem**: SLO defined but not monitored → reacts only after breach.

**Example**: SLO breach discovered in quarterly review.

**Fix**: Implement burn rate alerts (see Multi-Window Alerting above).

---

### Anti-Pattern 5: Ignoring Error Budget Policy

**Problem**: SLO breached but team continues shipping features without addressing root cause.

**Example**: "We're at 90% budget but this feature is important, ship it anyway."

**Fix**: Define and enforce error budget policy (feature freeze at thresholds).

---

## SLO Template (for MON-XXX Entries)

```markdown
## MON-XXX: [Service Name] Availability SLO

**ID**: MON-XXX
**Type**: SLO
**Layer**: Application
**Owner**: [Backend Team]
**Created**: YYYY-MM-DD

---

**Objective**: 99.9% of API requests succeed (non-5xx) over rolling 30 days
**Target**: 99.9%
**Window**: Rolling 30 days
**Error Budget**: 0.1% (43.2 minutes equivalent downtime/month)

**Measurement**:
- **Success Criteria**: HTTP status codes 200-499 (non-5xx)
- **Failure Criteria**: HTTP status codes 500-599
- **Data Source**: ALB access logs / APM tool (Datadog, New Relic)

**Alerting**:
- **50% budget consumed** (21.6 min used): Warning alert to #engineering-alerts (Slack)
- **75% budget consumed** (32.4 min used): Critical alert to #engineering-alerts, notify on-call lead
- **90% budget consumed** (38.9 min used): Page on-call via PagerDuty, escalate to engineering manager
- **100% budget consumed** (43.2 min used): Post-mortem required, feature freeze policy activated

**Burn Rate Alerts**:
- **Fast burn** (1 hour window): Alert if error rate > 1.44% (14.4× normal)
- **Slow burn** (6 hour window): Alert if error rate > 0.6% (6× normal)

**Linked IDs**:
- [UJ-101, UJ-102]: User journeys dependent on this service
- [API-045]: API contract for this service
- [RUN-025]: Runbook for SLO breach response
- [KPI-010]: Business metric tied to this SLO (revenue, retention)
```

---

## Validation Checklist

Before deploying an SLO:

- [ ] **SLI is measurable**: Can calculate from existing logs/metrics
- [ ] **SLI is user-centric**: Reflects actual user experience
- [ ] **SLO target is realistic**: Based on current performance and architecture
- [ ] **Error budget calculated**: Know exact allowed failure rate/downtime
- [ ] **Alerting configured**: Fast and slow burn rate alerts set up
- [ ] **Runbook linked**: Team knows what to do when budget consumed (RUN-XXX)
- [ ] **Error budget policy defined**: Clear actions at 50%, 75%, 90%, 100% thresholds
- [ ] **Stakeholder buy-in**: Product and engineering agree on target and policy

---

## Further Reading

- **Google SRE Book** (Chapter 4: Service Level Objectives): [https://sre.google/sre-book/service-level-objectives/](https://sre.google/sre-book/service-level-objectives/)
- **Alex Hidalgo's "Implementing Service Level Objectives"**: Practical SLO implementation guide
- **SLO Calculator**: [https://sre.google/workbook/implementing-slos/](https://sre.google/workbook/implementing-slos/)

---

*Reference: Use this guide when defining SLOs in `prd-v08-monitoring-setup` skill.*
