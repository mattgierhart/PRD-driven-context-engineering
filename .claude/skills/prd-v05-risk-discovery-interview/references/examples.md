# Risk Discovery Examples

## Good Example: Technical Dependency Risk

```
RISK-001: Stripe API Dependency
Category: Dependency
Description: Payment processing entirely depends on Stripe API availability
Trigger: Stripe outage, rate limiting, or API deprecation
Impact: High — All revenue blocked during outage
Likelihood: Low — Stripe 99.99% uptime SLA, but outages do occur
Priority: 3

Early Signal:
  - Stripe status page alerts
  - Payment failure rate >1%
  - Increased checkout abandonment

Response: Mitigate
Mitigation:
  1. Implement payment queue with 24h retry window
  2. Subscribe to Stripe status page webhooks
  3. Document manual invoicing fallback process
  4. Alert ops team if failure rate >0.5%
Owner: Backend Lead

Linked IDs: FEA-020 (payments), UJ-005 (checkout), BR-030 (pricing)
Review Date: Pre-launch, quarterly
```

**Why it's good:**
- Specific trigger, not vague
- Impact/likelihood clearly assessed
- Multiple early signals identified
- Mitigation is actionable, not "be careful"
- Clear owner and review date

---

## Good Example: Market Risk

```
RISK-002: Competitor Feature Launch
Category: Market
Description: Primary competitor (Notion) could launch similar automation feature
Trigger: Notion announces workflow automation in their roadmap/launch
Impact: Medium — Would reduce differentiation, not block launch
Likelihood: Medium — Notion has hinted at automation features
Priority: 4

Early Signal:
  - Notion changelog monitoring
  - User mentions "Notion has this now" in feedback
  - Competitor pricing page changes

Response: Mitigate
Mitigation:
  1. Accelerate launch timeline by 30 days if possible
  2. Double down on FEA-002 (offline mode) as unique delta
  3. Prepare messaging pivot: "Built for [niche], not general use"
Owner: Product Lead

Linked IDs: CFD-015 (competitive research), FEA-001, FEA-002, BR-010 (positioning)
Review Date: Weekly during development
```

---

## Good Example: Adoption Risk

```
RISK-003: Onboarding Abandonment
Category: Adoption
Description: Users may abandon onboarding before reaching first value moment
Trigger: Onboarding completion rate <40% after first 100 users
Impact: High — Blocks all downstream conversion
Likelihood: Medium — Current UJ-000 has 5 steps before value
Priority: 6

Early Signal:
  - Step-by-step drop-off analytics
  - "Too complicated" in user feedback
  - Support tickets about setup

Response: Mitigate
Mitigation:
  1. Reduce UJ-000 to 3 steps (defer optional setup)
  2. Add "skip for now" option on non-critical steps
  3. Implement progress indicator with time estimate
  4. A/B test guided vs. self-serve onboarding
Owner: Product Lead

Linked IDs: UJ-000 (onboarding), KPI-001 (activation), FEA-011 (personalization)
Review Date: After first 50 users, then weekly
```

---

## Good Example: Accepted Risk

```
RISK-004: Single Cloud Provider
Category: Technical
Description: All infrastructure on AWS; provider outage would affect entire product
Trigger: AWS region outage lasting >4 hours
Impact: High — Total product unavailability
Likelihood: Very Low — AWS us-east-1 has 99.99%+ uptime
Priority: 3

Early Signal:
  - AWS status page
  - CloudWatch alarms
  - User reports

Response: Accept
Rationale: Multi-cloud adds significant complexity and cost.
  - AWS outage would affect competitors equally
  - Recovery time acceptable for MVP stage
  - Will revisit if we reach >$100K MRR
Owner: CTO (monitoring only)

Linked IDs: All infrastructure
Review Date: When MRR >$100K
```

**Why acceptance is valid:**
- Likelihood is genuinely very low
- Mitigation cost (multi-cloud) exceeds benefit at current scale
- Explicit criteria for when to revisit
- Not an accident—documented decision

---

## Bad Example: Vague Risk

```
RISK-001: Something might go wrong
Category: Technical
Description: Technical problems could happen
Trigger: Problems
Impact: High
Likelihood: Medium
Priority: 6

Early Signal: Things don't work
Response: Mitigate
Mitigation: Be careful
Owner: Team
```

**Why it's bad:**
- "Something might go wrong" is not specific
- No actionable trigger
- "Be careful" is not a mitigation
- "Team" is not an owner

---

## Bad Example: Risk Theater

```
RISK-001: Server crash
RISK-002: Database corruption
RISK-003: Network failure
RISK-004: DNS issues
RISK-005: SSL certificate expiry
RISK-006: Docker container failure
RISK-007: Load balancer misconfiguration
RISK-008: Memory leak
RISK-009: CPU spike
RISK-010: Disk full
... (50 more technical failure modes)
```

**Why it's bad:**
- Exhaustive list of every possible technical failure
- No prioritization visible
- Most are standard ops concerns, not product risks
- Overwhelms the actual high-priority risks

**Fix:** Consolidate into:
```
RISK-001: Infrastructure Availability
Description: Any single infrastructure component failure could cause downtime
Mitigation: Standard monitoring + alerting + redundancy practices
```
