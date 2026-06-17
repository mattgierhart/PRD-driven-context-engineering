# Rollback Procedures Guide

**Purpose**: Decision trees and procedures for safe, fast rollbacks during deployments.

---

## Core Principles

### 1. Rollback is Not Failure

Rollback is a **success state** of a well-designed deployment process.

**Bad Mindset**: "We failed, we had to rollback."
**Good Mindset**: "Our safety mechanisms worked, we protected users by rolling back quickly."

**Culture**: Teams that rollback confidently ship faster and safer.

---

### 2. Fast Decision, Fast Execution

The goal: **Decide to rollback within 5 minutes, execute within 15 minutes.**

**Slow rollback** = prolonged user impact
**Fast rollback** = minimal impact, learn and retry

---

### 3. Rollback First, Debug Later

When in doubt, **rollback**.

**Anti-Pattern**: "Let's investigate for 20 minutes, maybe we can fix it forward."
**Pattern**: "Rollback now (2 minutes), investigate offline (no user impact)."

---

## Rollback Decision Tree

### Step 1: Is There User Impact?

**Question**: Are users experiencing errors, slowness, or broken functionality?

**If NO**:
- Continue monitoring
- No rollback needed (yet)
- Example: Logs show errors but users unaffected (background job failures)

**If YES**:
- Proceed to Step 2

---

### Step 2: Assess Severity

**Question**: How many users are affected and how badly?

**Low Severity** (< 5% of users, non-critical journeys):
- **Action**: Monitor for 10 minutes
- **Example**: Minor UI glitch on settings page

**Medium Severity** (5-25% of users, or < 5% on critical journey):
- **Action**: Attempt quick fix (< 10 minutes), otherwise rollback
- **Example**: Search results slower for 10% of users

**High Severity** (> 25% of users, or any % on revenue-critical journey):
- **Action**: Rollback immediately
- **Example**: Checkout broken for any users

**Critical Severity** (data corruption, security breach, complete outage):
- **Action**: Rollback immediately + escalate to leadership
- **Example**: Payment processing failing, PII exposed

---

### Step 3: Can We Fix Forward Quickly?

**Question**: Can we deploy a fix in < 10 minutes with high confidence?

**If YES**:
- Deploy fix
- Monitor closely
- If fix doesn't resolve in 10 minutes → rollback

**If NO** (or UNSURE):
- Rollback immediately
- Debug offline
- Redeploy when fix is verified

**Example** (Fix Forward):
- Issue: Feature flag misconfigured (flag ON but should be OFF)
- Fix: Toggle flag OFF (< 1 minute)
- Outcome: Fixed forward successfully

**Example** (Rollback):
- Issue: High error rate, root cause unclear
- Fix: Would require 30+ minutes of investigation
- Outcome: Rollback (2 minutes), investigate offline

---

### Step 4: Execute Rollback

See strategy-specific procedures below.

---

## Rollback Triggers (Automate These)

Define **specific, measurable conditions** that automatically trigger rollback consideration.

### Error Rate Trigger

**Trigger**: Error rate > [threshold]% for > [duration] minutes

**Example**:
- Baseline error rate: 0.05%
- Trigger: Error rate > 1% for > 5 minutes
- Action: Auto-alert on-call, display "ROLLBACK RECOMMENDED" in dashboard

**Automation**:
```yaml
alert:
  name: "High Error Rate - Rollback Recommended"
  condition: error_rate > 1% for 5 minutes
  severity: critical
  action: page_oncall
  message: "Error rate {{ error_rate }}% exceeds threshold 1%. Consider rollback."
```

---

### Latency Trigger

**Trigger**: p95 latency > [threshold]ms for > [duration] minutes

**Example**:
- Baseline p95 latency: 200ms
- Trigger: p95 latency > 1000ms for > 5 minutes
- Action: Auto-alert on-call

**Automation**:
```yaml
alert:
  name: "High Latency - Rollback Recommended"
  condition: p95_latency > 1000ms for 5 minutes
  severity: critical
  action: page_oncall
  message: "Latency {{ p95_latency }}ms exceeds threshold 1000ms. Consider rollback."
```

---

### SLO Budget Trigger

**Trigger**: Error budget consumption > [X]% in [duration] hours

**Example**:
- Monthly error budget: 43.2 minutes (99.9% SLO)
- Trigger: > 10% budget consumed in 1 hour (4.3 minutes of errors)
- Action: Auto-alert on-call

**Automation**:
```yaml
alert:
  name: "SLO Budget Burn - Rollback Recommended"
  condition: budget_consumed > 10% in 1 hour
  severity: critical
  action: page_oncall
  message: "SLO budget {{ budget_consumed }}% consumed in 1 hour. Consider rollback."
```

---

### User Journey Trigger

**Trigger**: Critical user journey success rate < [threshold]%

**Example**:
- Baseline checkout success rate: 95%
- Trigger: Checkout success rate < 90% for > 3 minutes
- Action: Auto-alert on-call + notify product lead

**Automation**:
```yaml
alert:
  name: "Checkout Broken - Rollback Immediately"
  condition: checkout_success_rate < 90% for 3 minutes
  severity: critical
  action: page_oncall
  message: "Checkout success {{ success_rate }}% below threshold 90%. ROLLBACK IMMEDIATELY."
```

---

## Strategy-Specific Rollback Procedures

### Big Bang Rollback

**Scenario**: Deployed new version to all servers, issues detected.

**Procedure**:
1. Stop traffic to application (maintenance mode or LB health check failure)
2. Redeploy previous version to all servers
3. Start servers with previous version
4. Restore traffic
5. Verify application healthy

**Estimated Time**: 10-30 minutes (depending on deploy process)

**Prerequisites**:
- [ ] Previous version artifact available (Docker image, build artifact)
- [ ] Database compatible with previous version (or rollback migration ready)

**Commands** (example with Docker):
```bash
# 1. Stop traffic (set health check to fail)
kubectl scale deployment app --replicas=0

# 2. Redeploy previous version
kubectl set image deployment/app app=myapp:v1.0

# 3. Scale up
kubectl scale deployment app --replicas=3

# 4. Verify health
kubectl rollout status deployment/app

# 5. Check application responding
curl https://api.example.com/health
```

---

### Rolling Rollback

**Scenario**: Partially deployed via rolling deployment, issues detected.

**Procedure**:
1. **Stop rollout** (prevent deploying to more instances)
2. **Revert deployed instances** (one AZ at a time, like forward deploy)
   - Take instance out of LB
   - Redeploy previous version
   - Health check passes → add back to LB
3. **Verify** each batch before proceeding
4. **Monitor** after full rollback

**Estimated Time**: 15-45 minutes (depends on number of instances)

**Prerequisites**:
- [ ] Know which instances are on new version vs old version
- [ ] Previous version artifact available
- [ ] Health checks reliable

**Commands** (example with Kubernetes):
```bash
# 1. Pause rollout
kubectl rollout pause deployment/app

# 2. Rollback to previous version
kubectl rollout undo deployment/app

# 3. Monitor rollback progress
kubectl rollout status deployment/app

# 4. If successful, resume normal state
kubectl rollout resume deployment/app
```

**Manual** (example with EC2 Auto Scaling):
1. Stop ASG from launching new instances
2. Terminate instances with new version (ASG launches new ones with old AMI)
3. Verify new instances healthy before terminating next batch

---

### Blue-Green Rollback

**Scenario**: Switched traffic from blue to green, issues detected.

**Procedure**:
1. **Switch traffic back to blue** (reverse of cutover)
2. **Verify blue healthy** (should be, hasn't changed)
3. **Monitor for 15 minutes**
4. **Keep green for investigation** (debug offline)

**Estimated Time**: 1-5 minutes (traffic switch only)

**Prerequisites**:
- [ ] Blue environment still running (DO NOT terminate blue immediately after deploy)
- [ ] Load balancer/DNS can switch back instantly

**Commands** (example with AWS ALB):
```bash
# 1. Update target group (point LB back to blue)
aws elbv2 modify-listener \
  --listener-arn <listener-arn> \
  --default-actions TargetGroupArn=<blue-target-group-arn>

# 2. Verify traffic routing to blue
aws elbv2 describe-target-health \
  --target-group-arn <blue-target-group-arn>
```

**DNS-based** (e.g., Route53):
```bash
# 1. Update DNS to point to blue (TTL dependent, can take minutes)
aws route53 change-resource-record-sets \
  --hosted-zone-id <zone-id> \
  --change-batch file://rollback-to-blue.json

# Note: DNS rollback slower (TTL dependent), prefer LB-based switching
```

---

### Canary Rollback

**Scenario**: Deployed to canary nodes, issues detected.

**Procedure**:
1. **Stop canary expansion** (don't deploy to more nodes)
2. **Route traffic away from canary** (back to stable nodes)
3. **Revert canary nodes to previous version** (or terminate them)
4. **Verify stable nodes handling traffic**
5. **Investigate canary issues offline**

**Estimated Time**: 2-10 minutes

**Prerequisites**:
- [ ] Can route traffic away from canary nodes (traffic routing rules)
- [ ] Stable nodes still running previous version

**Commands** (example with Kubernetes + Istio):
```bash
# 1. Route 100% traffic to stable version (0% to canary)
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: app
spec:
  hosts:
  - app
  http:
  - route:
    - destination:
        host: app
        subset: stable
      weight: 100
    - destination:
        host: app
        subset: canary
      weight: 0
EOF

# 2. Delete canary deployment
kubectl delete deployment app-canary

# 3. Verify stable handling all traffic
kubectl get pods -l version=stable
```

---

### Feature Flag Rollback

**Scenario**: Feature enabled via flag, issues detected.

**Procedure**:
1. **Turn flag OFF** (via feature flag dashboard/API)
2. **Verify flag propagated** (check feature flag service)
3. **Monitor for issue resolution**
4. **Communicate to users** (if feature was announced)

**Estimated Time**: < 1 minute (instant if flag service fast)

**Prerequisites**:
- [ ] Feature flag service accessible
- [ ] Flag can be toggled instantly (not requiring code deploy)
- [ ] Application respects flag changes (checks frequently, not cached)

**Commands** (example with LaunchDarkly):
```bash
# 1. Turn flag OFF via API
curl -X PATCH https://app.launchdarkly.com/api/v2/flags/default/new-checkout \
  -H "Authorization: <api-key>" \
  -d '{"instructions": [{"kind": "turnFlagOff"}]}'

# 2. Verify flag state
curl https://app.launchdarkly.com/api/v2/flags/default/new-checkout \
  -H "Authorization: <api-key>"
```

**Manual** (feature flag dashboard):
1. Log into LaunchDarkly/Unleash/custom dashboard
2. Find flag `new_checkout_enabled`
3. Toggle to OFF
4. Confirm change
5. Monitor application (feature should disappear immediately)

---

## Database Migration Rollback

**Scenario**: Deployed code with database migration, issues detected.

### Safe Migrations (Backward Compatible)

**Example**: Add column (doesn't break old code)

**Rollback Procedure**:
1. Rollback application code (column unused by old code, safe to leave)
2. Optional: Remove column later (not urgent)

**Estimated Time**: 5-15 minutes (code rollback only)

---

### Unsafe Migrations (Breaking Changes)

**Example**: Drop column (breaks old code if rolled back)

**Prevention**: Use multi-step migration
1. **Deploy 1**: Add new column, old code ignores it
2. **Deploy 2**: New code uses new column, writes to both old and new
3. **Deploy 3**: New code uses new column only
4. **Deploy 4**: Drop old column (safe, no code references it)

**Rollback**:
- If rollback needed after Deploy 1 → Safe (just remove column)
- If rollback needed after Deploy 2 → Safe (old code still works)
- If rollback needed after Deploy 3 → Harder (old code needs old column)

**Procedure** (if must rollback Deploy 3):
1. Rollback application code to Deploy 2 (writes to both columns)
2. Run data migration (backfill old column from new column)
3. Rollback to Deploy 1 (old code using old column)
4. Optional: Remove new column

**Estimated Time**: 30 minutes - 2 hours (depends on data volume)

**Better Approach**: Don't deploy Deploy 3 until confident (keep Deploy 2 for days/weeks)

---

### Migration Rollback Template

```sql
-- Always create reverse migration BEFORE deploying forward migration

-- Forward migration (V1_add_user_email_column.sql)
ALTER TABLE users ADD COLUMN email VARCHAR(255);

-- Reverse migration (V1_add_user_email_column_rollback.sql)
ALTER TABLE users DROP COLUMN email;
```

**Test** in staging:
1. Apply forward migration
2. Deploy code
3. Test application
4. Apply reverse migration
5. Test application (should still work if backward compatible)

---

## Rollback Communication

### Internal Communication

**Before Deployment**:
```
#deployments channel:
🚀 Deploying v1.2.0 to production at 14:00 UTC
- Changes: New checkout flow (UJ-102)
- Strategy: Canary (10% → 50% → 100%)
- Rollback plan: Feature flag toggle (< 1 min)
- Monitoring: #incidents channel + @oncall
```

**During Rollback**:
```
#incidents channel:
🚨 ROLLING BACK v1.2.0
- Reason: Checkout error rate 5% (baseline 0.1%)
- Action: Feature flag `new_checkout` OFF
- ETA: 1 minute
- Status: Monitoring...

[1 minute later]
✅ Rollback complete
- Checkout error rate back to 0.1%
- All users on old checkout flow
- Investigating issue offline
```

---

### External Communication (Customer-Facing)

**If Downtime Occurred**:
```
Status Page:
"We deployed a new feature that caused some users to experience errors during checkout. We rolled back the change within 5 minutes. All systems are now stable. We apologize for the inconvenience."
```

**If No Downtime But Feature Removed**:
```
Email to users who saw feature:
"We briefly launched a new checkout experience. We rolled it back to make some improvements based on early feedback. We'll re-launch soon. Thank you for your patience."
```

---

## Rollback Checklist

Use this during rollback:

- [ ] **Decision made**: Rollback approved by [on-call lead / engineering manager]
- [ ] **Incident channel active**: #incidents channel open, team aware
- [ ] **Rollback executed**: Followed strategy-specific procedure
- [ ] **Rollback verified**: Application healthy (error rate, latency normal)
- [ ] **Monitoring confirmed**: Metrics back to baseline for 15+ minutes
- [ ] **Stakeholders notified**: Product, support, leadership aware
- [ ] **Customers notified** (if customer impact): Status page updated
- [ ] **Logs preserved**: Captured logs/metrics from failed deployment
- [ ] **Post-mortem scheduled**: If SLO impacted or high-impact rollback

---

## Post-Rollback Actions

### Immediate (Within 1 Hour)

1. **Document What Happened**:
   - What was deployed?
   - What went wrong?
   - What metrics triggered rollback?
   - How long until rollback decision?
   - How long to execute rollback?

2. **Preserve Evidence**:
   - Save logs from failed deployment
   - Screenshot metrics showing issue
   - Export traces for investigation

3. **Communicate Status**:
   - Update status page (if used)
   - Notify stakeholders
   - Post summary in #incidents channel

---

### Short-Term (Within 24 Hours)

1. **Root Cause Analysis**:
   - Why did issue occur?
   - Why didn't testing catch it?
   - What conditions triggered it?

2. **Fix Identified Issue**:
   - Develop fix
   - Test thoroughly (include new test case for this issue)
   - Verify in staging

3. **Plan Re-Deployment**:
   - When to retry?
   - Same strategy or different?
   - Additional monitoring needed?

---

### Long-Term (Within 1 Week)

1. **Post-Mortem** (if SLO impacted):
   - Timeline of events
   - Root cause
   - User impact (how many users, how long)
   - Lessons learned
   - Action items (with owners)

2. **Process Improvements**:
   - Should we have caught this in testing?
   - Should we have rolled back faster?
   - Do we need better monitoring?
   - Should we change deployment strategy?

3. **Update Documentation**:
   - Update runbook (RUN-XXX) if procedure changed
   - Update deployment plan template (DEP-template.md)
   - Add to rollback examples (see examples.md)

---

## Anti-Patterns

### Anti-Pattern 1: Debating During Incident

**Problem**: Team debates whether to rollback while users impacted.

**Example**:
- Engineer 1: "Let's rollback"
- Engineer 2: "Wait, maybe we can fix it forward"
- Engineer 3: "Let me investigate for 10 minutes"
- [20 minutes pass, users still impacted]

**Fix**: Define rollback triggers and decision maker BEFORE deployment. When trigger met, rollback immediately.

---

### Anti-Pattern 2: No Rollback Plan

**Problem**: Issues detected, but no documented rollback procedure.

**Example**: "How do we rollback? Do we have the old Docker image? Where is it?"

**Fix**: Document rollback procedure in DEP-XXX BEFORE deployment. Test rollback in staging.

---

### Anti-Pattern 3: Terminating Blue Environment Immediately

**Problem**: Switch to green, terminate blue, issues discovered later (no easy rollback).

**Example**: Green deployed at 2 PM, blue terminated at 2:15 PM, issue discovered at 4 PM (2 hours later).

**Fix**: Keep blue environment for 24-48 hours after cutover (instant rollback target).

---

### Anti-Pattern 4: Database Rollback Without Testing

**Problem**: Run reverse migration without testing, causes data loss.

**Example**: Reverse migration script has bug, drops wrong column.

**Fix**: ALWAYS test reverse migration in staging before deploying forward migration to production.

---

### Anti-Pattern 5: Rollback Without Communication

**Problem**: Engineers rollback but don't notify product/support teams.

**Example**: Support team still telling users "new feature available" but it was rolled back.

**Fix**: Communicate rollback immediately to #incidents, product, support, and leadership.

---

## Rollback Metrics

Track these to improve rollback process:

### Time to Decision

**Metric**: Time from issue detection to rollback decision

**Target**: < 5 minutes

**How to Improve**:
- Define clear rollback triggers (automated alerts)
- Empower on-call to make decision (no approval needed for clear triggers)
- Practice rollback scenarios in gameday exercises

---

### Time to Rollback

**Metric**: Time from rollback decision to rollback complete

**Target**: < 15 minutes (< 1 minute for feature flags)

**How to Improve**:
- Automate rollback procedures
- Practice rollback in staging regularly
- Keep rollback targets accessible (blue environment, previous version artifacts)

---

### Rollback Success Rate

**Metric**: % of rollbacks that successfully restore service

**Target**: 100%

**How to Improve**:
- Test rollback procedures in staging
- Ensure previous versions compatible (backward-compatible migrations)
- Keep rollback artifacts (Docker images, AMIs) accessible

---

*Reference: Use this guide when planning rollback procedures in `prd-v08-release-planning` skill.*
