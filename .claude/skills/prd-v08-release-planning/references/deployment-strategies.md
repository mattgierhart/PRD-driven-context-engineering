# Deployment Strategies Guide

**Purpose**: Help teams select the right deployment strategy for their context.

---

## Strategy Overview

| Strategy | Risk Level | Rollback Time | Complexity | Best For |
|----------|-----------|---------------|------------|----------|
| **Big Bang** | High | Minutes-Hours | Low | Small apps, low traffic, dev/staging |
| **Rolling** | Medium | Minutes | Medium | Standard web apps, stateless services |
| **Blue-Green** | Low | Seconds | Medium | Zero-downtime required, easy rollback |
| **Canary** | Low | Seconds-Minutes | High | High-risk changes, gradual validation |
| **Feature Flag** | Very Low | Seconds | Medium-High | Experimental features, A/B testing |

---

## Big Bang Deployment

### Description

Deploy new version to all servers/instances at once, replacing the old version completely.

### How It Works

```
Before: [v1.0] [v1.0] [v1.0]  (all servers on old version)
During: [v1.1] [v1.1] [v1.1]  (all servers replaced)
After:  [v1.1] [v1.1] [v1.1]  (all servers on new version)
```

**Steps**:
1. Take down all servers (or queue requests)
2. Deploy new version to all servers
3. Start servers with new version
4. Route traffic to new version

**Downtime**: Usually 1-30 minutes (depending on deploy process)

---

### When to Use

**Good For**:
- Development and staging environments
- Internal tools with scheduled maintenance windows
- Low-traffic applications (< 100 users)
- Breaking changes that require downtime anyway
- MVP/prototypes where downtime is acceptable

**Avoid For**:
- Customer-facing production services
- High-traffic applications
- Services with SLAs requiring uptime

---

### Pros & Cons

**Pros**:
- Simple to implement (no complex routing)
- Fewer infrastructure resources (don't need blue + green)
- Easy to reason about (only one version active)
- Fast deployment process

**Cons**:
- Downtime required (not acceptable for most production services)
- High-risk (all users impacted if issues)
- Slow rollback (requires redeployment)
- No gradual validation

---

### Example

**Context**: Internal admin dashboard, 20 users, used during business hours only

**Deployment Plan**:
1. Schedule deployment for 6 PM (after hours)
2. Post maintenance notice in #admin-tools channel
3. Take down dashboard (show maintenance page)
4. Deploy new version
5. Run smoke tests
6. Bring dashboard back up
7. Notify users deployment complete

**Risk Mitigation**:
- Deploy after hours (no user impact)
- Have rollback script ready
- Test thoroughly in staging first

---

## Rolling Deployment

### Description

Deploy new version gradually, replacing old version instance-by-instance (or batch-by-batch).

### How It Works

```
Before: [v1.0] [v1.0] [v1.0] [v1.0]
Step 1: [v1.1] [v1.0] [v1.0] [v1.0]  (deploy to 25%)
Step 2: [v1.1] [v1.1] [v1.0] [v1.0]  (deploy to 50%)
Step 3: [v1.1] [v1.1] [v1.1] [v1.0]  (deploy to 75%)
After:  [v1.1] [v1.1] [v1.1] [v1.1]  (deploy to 100%)
```

**Steps**:
1. Take first instance out of load balancer
2. Deploy new version to that instance
3. Run health checks
4. Add instance back to load balancer
5. Repeat for next instance
6. Monitor between each step

**Downtime**: None (if done correctly)

---

### When to Use

**Good For**:
- Stateless web applications
- Microservices with multiple instances
- Standard production deployments
- Changes with medium risk

**Avoid For**:
- Database schema changes (backward compatibility required)
- Stateful services (session affinity issues)
- Breaking API changes
- High-risk changes (use canary instead)

---

### Pros & Cons

**Pros**:
- No downtime (if health checks work)
- Gradual rollout (limits blast radius)
- Moderate complexity (built into most platforms)
- Cost-effective (no extra infrastructure)

**Cons**:
- Multiple versions running simultaneously (compatibility required)
- Slower rollback than blue-green (must redeploy)
- Health checks must be reliable
- Session affinity can cause issues

---

### Example

**Context**: Web application with 12 EC2 instances behind ALB

**Deployment Plan**:
1. Deploy to 3 instances in AZ-1 (25% of traffic)
2. Monitor for 15 minutes (error rate, latency)
3. Deploy to 3 instances in AZ-2 (50% of traffic)
4. Monitor for 15 minutes
5. Deploy to 3 instances in AZ-3 (75% of traffic)
6. Monitor for 15 minutes
7. Deploy to remaining 3 instances (100%)
8. Monitor for 1 hour before declaring success

**Rollback**: If issues detected, stop rollout and redeploy old version to affected instances

---

## Blue-Green Deployment

### Description

Run two identical environments ("blue" and "green"). Deploy to inactive environment, then switch traffic.

### How It Works

```
Before:
  Blue:  [v1.0] [v1.0] [v1.0]  ← 100% traffic
  Green: [idle]

During Deploy:
  Blue:  [v1.0] [v1.0] [v1.0]  ← 100% traffic
  Green: [v1.1] [v1.1] [v1.1]  ← 0% traffic (deploying + testing)

After Switch:
  Blue:  [v1.0] [v1.0] [v1.0]  ← 0% traffic (keep as rollback)
  Green: [v1.1] [v1.1] [v1.1]  ← 100% traffic
```

**Steps**:
1. Deploy new version to green environment (while blue serves traffic)
2. Run smoke tests on green
3. Switch load balancer/DNS to route traffic to green
4. Monitor green environment
5. Keep blue environment running (instant rollback target)
6. Decommission blue after confidence period (e.g., 24 hours)

**Downtime**: Seconds (during traffic switch only)

---

### When to Use

**Good For**:
- Zero-downtime requirements
- Easy rollback critical (financial, healthcare)
- Deploying complex changes
- When you need production testing before full cutover

**Avoid For**:
- Stateful services with persistent connections (switch breaks connections)
- Database-heavy apps (blue and green share DB = complications)
- Cost-sensitive environments (doubles infrastructure during deploy)

---

### Pros & Cons

**Pros**:
- Near-zero downtime (only during traffic switch)
- Instant rollback (switch traffic back to blue)
- Full testing before cutover (green is production-like)
- Clean separation (only one version receiving traffic at a time)

**Cons**:
- Doubles infrastructure cost (blue + green)
- Database migration complexity (blue and green share DB)
- Requires sophisticated routing (load balancer/DNS)
- Stateful services challenging (active connections dropped during switch)

---

### Example

**Context**: Payment processing API (zero downtime required)

**Deployment Plan**:
1. Deploy v1.1 to green environment (blue still serving traffic)
2. Run full test suite on green (including payment tests with test credentials)
3. Switch 5% of traffic to green (canary within blue-green)
4. Monitor green for 30 minutes (error rate, latency, successful payments)
5. Switch 100% traffic to green
6. Monitor for 2 hours (critical period)
7. Keep blue running for 24 hours (in case issues discovered later)
8. Decommission blue environment

**Rollback**: Switch traffic back to blue (< 1 minute)

---

## Canary Deployment

### Description

Deploy new version to small subset of users/servers, monitor closely, then gradually expand if healthy.

### How It Works

```
Before: [v1.0] [v1.0] [v1.0] [v1.0] [v1.0]  ← 100% traffic

Canary (10%):
  [v1.1]  ← 10% traffic (canary)
  [v1.0] [v1.0] [v1.0] [v1.0]  ← 90% traffic

If healthy, expand to 50%:
  [v1.1] [v1.1] [v1.1]  ← 50% traffic
  [v1.0] [v1.0]  ← 50% traffic

If healthy, deploy to 100%:
  [v1.1] [v1.1] [v1.1] [v1.1] [v1.1]  ← 100% traffic
```

**Steps**:
1. Deploy new version to canary nodes (10% of fleet)
2. Route 10% of traffic to canary
3. Monitor canary closely (30-60 minutes)
4. If healthy, expand to 50%
5. Monitor for 30-60 minutes
6. If healthy, expand to 100%
7. Monitor full deployment

**Downtime**: None

---

### When to Use

**Good For**:
- High-risk changes (major refactors, new features)
- A/B testing and experimentation
- Gradual rollout required (validate with real users)
- Changes where automated testing insufficient

**Avoid For**:
- Breaking changes (incompatible with old version)
- Database schema changes (all nodes share DB)
- Low-traffic services (not enough data to validate canary)

---

### Pros & Cons

**Pros**:
- Lowest risk (small blast radius initially)
- Real user validation before full rollout
- Can catch issues automated tests miss
- Gradual confidence building

**Cons**:
- Complex to implement (traffic routing + monitoring)
- Requires high traffic (need statistical significance)
- Slower deployment process (wait between stages)
- Monitoring must be excellent (need to detect issues quickly)

---

### Example

**Context**: New search algorithm (high risk, need real-user validation)

**Deployment Plan**:
1. Deploy new search algorithm to 2 servers (10% of traffic)
2. Monitor canary metrics:
   - Search result click-through rate (expect: >= baseline)
   - Search latency (expect: < 200ms)
   - Error rate (expect: < 0.1%)
3. If metrics healthy after 1 hour, expand to 50%
4. Monitor for 2 hours
5. If metrics healthy, expand to 100%
6. Monitor for 24 hours before declaring success

**Rollback**: Route traffic away from canary nodes (< 1 minute)

**A/B Testing**: Keep 10% on old algorithm for 1 week, compare metrics, then full rollout

---

## Feature Flag Deployment

### Description

Deploy code with new features hidden behind toggles (flags). Enable features gradually via config, not code deploy.

### How It Works

```
Deploy code:
  [v1.1 + flag OFF] [v1.1 + flag OFF] [v1.1 + flag OFF]

Enable flag for 10% of users:
  Users 1-10:   See new feature (flag ON)
  Users 11-100: See old experience (flag OFF)

Enable flag for 100%:
  All users: See new feature (flag ON)

Later: Remove flag (feature now default)
  [v1.2 (flag removed)] [v1.2 (flag removed)]
```

**Steps**:
1. Develop feature behind feature flag
2. Deploy code with flag OFF (no user impact)
3. Verify deployment successful
4. Enable flag for internal users (10%)
5. Monitor for issues (1-24 hours depending on risk)
6. Enable flag for 50% of users
7. Monitor for issues
8. Enable flag for 100% of users
9. After confidence period, remove flag and make feature default

**Downtime**: None

---

### When to Use

**Good For**:
- Experimental features (need gradual rollout)
- A/B testing (compare old vs new)
- Risky features (need instant kill switch)
- Trunk-based development (merge unfinished features safely)
- Long-running feature development (deploy incrementally)

**Avoid For**:
- Infrastructure changes (can't toggle infrastructure)
- Database migrations (flags don't help with schema)
- Simple, low-risk changes (overhead not worth it)

---

### Pros & Cons

**Pros**:
- Instant rollback (toggle flag OFF, no deploy)
- Separate deploy from release (deploy anytime, release when ready)
- A/B testing built-in (control which users see feature)
- Gradual rollout with user-level control
- Kill switch for incidents (disable feature immediately)

**Cons**:
- Code complexity (if/else branches everywhere)
- Technical debt (old flags accumulate if not cleaned up)
- Testing complexity (must test all flag combinations)
- Requires feature flag infrastructure (LaunchDarkly, Unleash, custom)
- Not suitable for all change types

---

### Example

**Context**: New checkout flow (high revenue impact, need gradual rollout)

**Deployment Plan**:
1. Develop new checkout flow behind `new_checkout_enabled` flag
2. Deploy code with flag OFF (no user impact)
3. Enable flag for internal team (10 users)
4. Test checkout flow internally
5. Enable flag for 1% of users (100 users)
6. Monitor for 24 hours:
   - Checkout completion rate (expect: >= baseline)
   - Revenue per user (expect: >= baseline)
   - Error rate (expect: < 0.1%)
7. If healthy, enable for 10% of users (1,000 users)
8. Monitor for 48 hours
9. If healthy, enable for 50% (5,000 users)
10. Monitor for 1 week
11. If healthy (or better than baseline), enable for 100%
12. After 2 weeks of stability, remove flag (make new checkout default)

**Rollback**: Set flag to OFF (< 1 minute, no deploy)

**A/B Testing**: Keep 50/50 split for 1 month, compare metrics, choose winner

---

## Decision Framework

### By Risk Level

**Low Risk** (bug fixes, minor UI changes):
- **Recommended**: Rolling deployment
- **Alternative**: Big Bang (if low traffic)

**Medium Risk** (new features, refactors):
- **Recommended**: Canary deployment
- **Alternative**: Blue-Green (if zero-downtime critical)

**High Risk** (major changes, experiments):
- **Recommended**: Feature flag (gradual rollout)
- **Alternative**: Canary (if feature flags not available)

---

### By Downtime Tolerance

**No Downtime Allowed**:
- **Recommended**: Blue-Green or Rolling
- **Avoid**: Big Bang

**Scheduled Maintenance OK**:
- **Recommended**: Big Bang (simplest)
- **Alternative**: Rolling (if want to practice zero-downtime)

---

### By Traffic Level

**Low Traffic** (< 1,000 requests/hour):
- **Recommended**: Rolling or Big Bang
- **Avoid**: Canary (not enough data to validate)

**High Traffic** (> 10,000 requests/hour):
- **Recommended**: Canary (can validate quickly)
- **Alternative**: Blue-Green (instant rollback)

---

### By Architecture

**Stateless Services** (API, web servers):
- **Recommended**: Rolling or Canary
- Works Well: Blue-Green, Feature Flag

**Stateful Services** (databases, queues):
- **Recommended**: Blue-Green (with careful DB migration)
- **Avoid**: Rolling (schema compatibility issues)

**Microservices**:
- **Recommended**: Canary per service
- **Alternative**: Feature flag (cross-service features)

**Monolith**:
- **Recommended**: Blue-Green (simple cutover)
- **Alternative**: Rolling (if stateless)

---

## Combining Strategies

### Blue-Green + Canary

Deploy to green, switch 10% traffic to green (canary), then 100%.

**Benefits**:
- Risk reduction (canary validation before full cutover)
- Instant rollback (switch back to blue)

**Example**: Deploy payment API to green, route 10% of payments to green for 1 hour, then 100%.

---

### Feature Flag + Canary

Deploy code with flag OFF, enable flag for 10% (canary), then 100%.

**Benefits**:
- Instant rollback (toggle flag)
- Gradual validation (canary)

**Example**: Deploy new search algorithm with flag OFF, enable for 10% of users, monitor, then 100%.

---

### Rolling + Feature Flag

Deploy code with flag OFF using rolling deployment, then enable flag gradually.

**Benefits**:
- Safe code deployment (flag OFF)
- Gradual feature rollout (flag)

**Example**: Deploy new checkout flow (flag OFF) via rolling deployment, then enable flag for 1% → 10% → 100%.

---

## Anti-Patterns

### Anti-Pattern 1: Canary Without Metrics

**Problem**: Deploy to canary but don't monitor, just wait arbitrary time.

**Example**: "Let's canary for 1 hour" but don't check error rate, latency, or user metrics.

**Fix**: Define success criteria before canary (e.g., error rate < 0.1%, latency < 500ms). Automate checks.

---

### Anti-Pattern 2: Blue-Green Without Database Strategy

**Problem**: Switch blue to green but they share database, schema incompatible.

**Example**: Green requires new DB column, blue breaks when column added.

**Fix**: Deploy backward-compatible schema changes first, then application, then remove old code.

---

### Anti-Pattern 3: Feature Flags Never Removed

**Problem**: Feature flags accumulate, code becomes unmaintainable.

**Example**: 50 feature flags, half unused, `if/else` branches everywhere.

**Fix**: Define flag lifecycle (temporary vs permanent). Remove temporary flags within 30 days of 100% rollout.

---

### Anti-Pattern 4: Rolling Deployment Without Health Checks

**Problem**: Deploy to instance, add to load balancer before app ready.

**Example**: Instance added to LB while still booting, users get 503 errors.

**Fix**: Implement health check endpoint (`/health`). Load balancer only routes traffic when health check passes.

---

### Anti-Pattern 5: No Rollback Plan

**Problem**: Issues detected during deployment but no defined rollback procedure.

**Example**: Canary shows high errors, team debates what to do, users impacted.

**Fix**: Define rollback triggers and procedure BEFORE deployment (see rollback-procedures.md).

---

## Deployment Strategy Template

When planning a deployment (DEP-XXX), choose strategy based on:

```markdown
**Risk Level**: [Low | Medium | High]
**Downtime Tolerance**: [None | Minutes | Hours]
**Traffic Level**: [requests/hour]
**Architecture**: [Stateless | Stateful | Microservices | Monolith]
**Rollback Requirement**: [Instant | Fast (<15min) | Can Wait]

**Recommended Strategy**: [Based on decision framework above]

**Success Criteria**:
- Error rate < [threshold]%
- Latency p95 < [threshold]ms
- [Custom metric] within [range]

**Rollback Trigger**:
- Error rate > [threshold]% for > [duration] minutes
- Latency p95 > [threshold]ms for > [duration] minutes
- [Critical journey] broken
```

---

*Reference: Use this guide when planning deployments in `prd-v08-release-planning` skill.*
