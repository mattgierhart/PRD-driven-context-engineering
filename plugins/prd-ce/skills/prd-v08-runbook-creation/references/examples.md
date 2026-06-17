# Runbook Examples

**Purpose**: Good and bad patterns for creating operational runbooks (RUN-XXX entries).

---

## Good Example 1: API Latency Spike Runbook

### RUN-012: API Latency Spike Troubleshooting

**ID**: RUN-012
**Type**: Troubleshooting
**Service/System**: Backend API
**Severity**: P1 - High
**Owner**: Backend Team
**Created**: 2026-01-10
**Last Updated**: 2026-01-10
**Last Tested**: 2026-01-05

---

**Quick Reference**:
- **When to Use**: MON-023 alerts (p95 latency > 1000ms) or user reports of slow pages
- **Time to Resolve**: 15-30 minutes typical
- **Escalation**: @backend-lead if unresolved after 30 minutes

**Related Runbooks**:
- [RUN-015]: Database slow query troubleshooting
- [RUN-008]: Deployment rollback procedure

---

**Symptoms** (one or more):
- [x] MON-023 alert: "API p95 latency > 1000ms"
- [x] User reports: "Pages loading slowly"
- [x] Support tickets: Spike in "app is slow" complaints

**Dashboards**:
- API Performance Dashboard shows p95 latency spike from 200ms → 2000ms

**Logs**:
- Application logs may show: `WARN: Request took 2.5s for /api/users/123`

---

**Impact Assessment**:
- **Severity P1**: Major degradation, most users affected, critical journeys slow but not broken
- **Affected Journeys**: [UJ-101] User Profile Page, [UJ-104] Dashboard Load
- **Business Impact**: User frustration, potential churn if prolonged

---

**Immediate Actions (First 5 Minutes)**:

**Step 1: Acknowledge**
- [x] Acknowledge alert in Datadog
- [x] Post in #incidents: "Investigating API latency spike - @yourname - Update in 15 min"

**Step 2: Check Recent Changes**
- [x] Check #deployments channel for recent deploys (last 2 hours)
- [x] If deploy within last hour AND latency spike correlates exactly:
  - **ROLLBACK IMMEDIATELY** (see RUN-008)
  - Skip to monitoring step
- [x] If no recent deploy, continue to diagnosis

**Step 3: Quick Triage**
- [x] Check traffic: Is this a traffic spike? (Datadog Metrics → Requests/sec)
  - If traffic 2x+ normal: Go to "Traffic Spike" scenario
- [x] Check error rate: Are we also seeing errors? (Datadog Metrics → Error rate)
  - If error rate high: This might be RUN-011 (High Error Rate) instead

---

**Diagnosis Steps**:

**Step 1: Identify Slow Layer (Use Datadog APM Traces)**
- [x] Open Datadog APM → Traces
- [x] Filter: Latency > 1000ms, Time range: Last 15 minutes
- [x] Sort by duration, pick slowest trace
- [x] Identify bottleneck:
  - Database queries slow? → Continue to Database Diagnosis
  - External API slow? → Continue to External API Diagnosis
  - Application code slow? → Continue to Code Diagnosis

---

**Scenario 1: Database Queries Slow**

**Diagnosis**:
- [x] Datadog APM shows: Database queries taking 1.5s (normally 50ms)
- [x] Check Database Dashboard:
  - CPU: Normal (30%) or High (>80%)?
  - Connection pool: 180/200 (near limit) or normal (50/200)?

**Resolution**:

**If Connection Pool Near Limit**:
1. [x] Increase connection pool: `DB_POOL_SIZE=300` (currently 200)
2. [x] Redeploy backend service (or hot-reload config if supported)
3. [x] Monitor: Connection pool utilization should drop below 70%

**If Slow Queries**:
1. [x] Check slow query log (RDS Console → Logs)
2. [x] Identify query pattern (missing index?)
3. [x] If obvious fix (add index): Add index online (non-blocking)
   ```sql
   CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
   ```
4. [x] If complex query issue: File ticket, optimize query in next release
5. [x] Temporary fix: Scale up database (vertical scaling) if CPU high

**Success Criteria**: Latency returns to < 500ms within 15 minutes

**Time to Resolve**: 10-20 minutes

---

**Scenario 2: External API Slow**

**Diagnosis**:
- [x] Datadog APM shows: Stripe API calls taking 3s (normally 500ms)
- [x] Check third-party status: https://status.stripe.com

**Resolution**:

**If Known Outage**:
1. [x] Post in #incidents: "Stripe degradation (status.stripe.com), enabling fallback"
2. [x] Enable feature flag: `use_cached_payment_status = true`
3. [x] Update status page: "Payment status may be delayed due to third-party issue"
4. [x] Monitor Stripe status page, disable fallback when recovered

**If No Known Outage**:
1. [x] Increase timeout: `STRIPE_TIMEOUT_MS=5000` (from 3000)
2. [x] Redeploy or hot-reload config
3. [x] If still slow after 30 min: Escalate to Stripe support (Enterprise contract)

**Success Criteria**: Latency acceptable (< 1s) or fallback enabled

**Time to Resolve**: 10-30 minutes (or wait for Stripe recovery)

---

**Scenario 3: Application Code Slow**

**Diagnosis**:
- [x] Datadog APM shows: Specific controller action slow (e.g., `UserController#show`)
- [x] No database or external API bottleneck

**Resolution**:

**If Recent Deployment**:
1. [x] Rollback deployment (RUN-008)
2. [x] Verify latency returns to normal
3. [x] Schedule post-mortem to fix code issue

**If No Recent Deployment**:
1. [x] Check for N+1 query pattern (common Rails/Django issue)
   - Look for many small database queries instead of one JOIN
2. [x] Check for inefficient loop (processing large array)
3. [x] Profile code (New Relic, Scout APM, etc.) to find hot path
4. [x] If fixable quickly (< 30 min): Deploy hotfix
5. [x] If complex: Revert to previous known-good version, fix offline

**Success Criteria**: Latency returns to < 500ms

**Time to Resolve**: 15-60 minutes (depends on code complexity)

---

**Communication Plan**:

**Internal** (#incidents channel):
```
📊 UPDATE: API Latency Spike
- Root Cause: Database connection pool exhausted
- Action: Increased pool size 200 → 300, redeployed
- Status: Latency back to 300ms (normal ~200ms), monitoring
- Next Update: 30 min (if still stable, will close incident)
```

**External** (Status Page - only if >30 min):
```
Identified: We identified a database performance issue causing slow page loads.
We have applied a fix and are monitoring. Expected full resolution within 15 minutes.
```

---

**Prevention**:
- [x] MON-023 alert exists (latency threshold monitoring)
- [x] Connection pool utilization alert (warn at 80%)
- [x] Database query performance tests in CI

---

**Why This is Good**:

✅ **Clear symptoms** (specific alert, user reports)
✅ **Immediate actions prioritized** (rollback first if recent deploy)
✅ **Multiple scenarios covered** (database, external API, code)
✅ **Specific commands included** (SQL to add index, config to change)
✅ **Success criteria defined** (latency < 500ms)
✅ **Time estimates realistic** (10-60 min depending on scenario)
✅ **Communication templates** (copy-paste ready)
✅ **Prevention section** (how to avoid recurrence)

---

## Good Example 2: Deployment Rollback Runbook

### RUN-008: Emergency Deployment Rollback

**ID**: RUN-008
**Type**: Deployment
**Service/System**: All Services
**Severity**: P0/P1 (use for critical issues)
**Owner**: DevOps Team
**Created**: 2025-12-15
**Last Updated**: 2026-01-10
**Last Tested**: 2026-01-08

---

**Quick Reference**:
- **When to Use**: Recent deployment causing errors, latency, or data issues
- **Time to Resolve**: 5-15 minutes
- **Escalation**: @devops-lead if rollback fails

---

**Symptoms**:
- Error rate spike after deployment
- Latency spike after deployment
- Service unavailable after deployment
- Data corruption after deployment

---

**Pre-Flight Check** (Before Rolling Back):

**Confirm Deployment Timing**:
- [x] When was deployment? (check #deployments channel or CI/CD logs)
- [x] When did issue start? (check monitoring dashboard)
- [x] Do timings correlate? (within 15 minutes of each other)

**If timings DON'T correlate**: This might not be deployment-related, investigate other causes first

**If timings DO correlate**: Proceed with rollback

---

**Rollback Procedure**:

**For Kubernetes Deployments**:

```bash
# 1. Check current version
kubectl get deployment api-backend -n production -o yaml | grep image:

# 2. Get rollout history (find previous version)
kubectl rollout history deployment/api-backend -n production

# 3. Rollback to previous version
kubectl rollout undo deployment/api-backend -n production

# 4. Watch rollout status
kubectl rollout status deployment/api-backend -n production

# Expected: "deployment 'api-backend' successfully rolled out" (< 5 min)
```

**Success Criteria**:
- Deployment shows previous version
- Health checks passing
- Error rate returns to baseline within 5 minutes

---

**For AWS ECS Deployments**:

```bash
# 1. Get current task definition
aws ecs describe-services --cluster production --services api-backend

# 2. Get previous task definition version
aws ecs list-task-definitions --family-prefix api-backend --max-results 10

# 3. Update service to previous task definition
aws ecs update-service \
  --cluster production \
  --service api-backend \
  --task-definition api-backend:123  # Previous version number

# 4. Wait for deployment (< 10 min)
aws ecs wait services-stable --cluster production --services api-backend
```

**Success Criteria**: Service running previous task definition, health checks passing

---

**For Traditional VMs (Blue-Green Deployment)**:

```bash
# 1. Switch load balancer to previous environment
# Example: Route53 weighted routing
aws route53 change-resource-record-sets \
  --hosted-zone-id Z123456 \
  --change-batch file://switch-to-blue.json

# 2. Wait for DNS propagation (< 5 min)
# 3. Verify traffic routed to old version
```

---

**Post-Rollback Verification**:

**Step 1: Check Metrics (5 minutes after rollback)**
- [x] Error rate: Back to < 0.1% (baseline)
- [x] Latency p95: Back to < 500ms (baseline)
- [x] Traffic: Normal distribution

**Step 2: Check User Journeys**
- [x] Test critical user journeys manually:
  - Login
  - Checkout (if e-commerce)
  - Data submission

**Step 3: Communicate**
- [x] Post in #incidents:
  ```
  ✅ ROLLBACK COMPLETE: [Service] v[new] → v[old]
  - Error rate back to normal (0.1%)
  - Latency back to baseline (200ms p95)
  - Monitoring for 30 min to ensure stability
  ```

---

**If Rollback Doesn't Fix Issue**:

**Problem**: Rolled back but errors/latency still high

**Next Steps**:
1. [x] Issue might not be deployment-related
2. [x] Check for:
   - Traffic spike (scale infrastructure)
   - External dependency failure (enable fallback)
   - Database issue (check connection pool, slow queries)
3. [x] Escalate to on-call lead
4. [x] Consider rolling back FURTHER (to version before previous)

---

**Database Migrations** (SPECIAL CASE):

**Problem**: Deployment included database migration, can't just rollback code

**Procedure**:
1. [x] **Do NOT rollback code** if migration is irreversible (dropped column, renamed table)
2. [x] Check migration reversibility:
   - **Reversible**: Added column (default value), new index, new table
   - **Irreversible**: Dropped column, renamed column, data transformation
3. [x] If reversible:
   - Run reverse migration first
   - Then rollback code
4. [x] If irreversible:
   - **Do NOT rollback code** (old code won't work with new schema)
   - Fix forward (hotfix deployment)
   - Or restore database from backup (extreme, data loss)

**Escalate immediately** if database migration involved

---

**Communication Templates**:

**Rolling Back**:
```
🔄 ROLLING BACK: [Service] v[new] → v[old]
- Reason: [Error rate spike | Latency spike | Service down]
- ETA: 5 minutes
- Next Update: After rollback complete
```

**Rollback Complete**:
```
✅ ROLLBACK COMPLETE: [Service] back to v[old]
- Metrics returning to normal
- Monitoring for 30 min
- Post-mortem scheduled for [date]
```

---

**Why This is Good**:

✅ **Platform-specific commands** (Kubernetes, ECS, VM)
✅ **Pre-flight check** (confirm correlation before rolling back)
✅ **Success criteria clear** (metrics return to baseline)
✅ **Special cases covered** (database migrations, rollback doesn't fix issue)
✅ **Communication templates** (keep team informed)
✅ **Time estimates** (5-15 min typical)

---

## Bad Example 1: Vague Runbook

### RUN-999: Fix Production Issues (BAD)

**ID**: RUN-999
**Type**: Troubleshooting
**Service**: Production
**Owner**: Engineering

---

**When to Use**: When production is broken

**Steps**:
1. Check logs
2. Find the problem
3. Fix it
4. Deploy

**Rollback**: Rollback if needed

---

**Why This is Bad**:

❌ **No specific symptoms** (what does "broken" mean?)
❌ **No severity level** (P0? P3? How urgent?)
❌ **No specific commands** (which logs? how to check?)
❌ **No success criteria** (how do you know it's fixed?)
❌ **No time estimates** (how long should this take?)
❌ **No escalation path** (who to call if stuck?)
❌ **No communication plan** (who to notify?)

**Fix**: Use the RUN-XXX template, define specific symptoms, provide exact commands, set success criteria

---

## Bad Example 2: Missing Critical Information

### RUN-888: Database Connection Pool Exhaustion (BAD)

**ID**: RUN-888
**Type**: Troubleshooting
**Service**: API Backend
**Severity**: P1

---

**Symptoms**: Database connection errors

**Solution**: Increase connection pool size

---

**Why This is Bad**:

❌ **No specific error messages** (what do logs say?)
❌ **No diagnostic steps** (how to confirm it's connection pool issue?)
❌ **No specific configuration** (which file? which variable? what value?)
❌ **No immediate mitigation** (what to do while waiting for config change?)
❌ **No rollback plan** (what if increasing pool doesn't fix it?)
❌ **No related runbooks** (what if it's a different database issue?)
❌ **No prevention** (how to avoid this in future?)

**Fix**:
- Add specific log patterns to look for
- Provide commands to check current pool utilization
- Specify exact config file and variable name
- Include immediate mitigation (restart service)
- Add monitoring to prevent recurrence

---

## Bad Example 3: No Rollback Strategy

### RUN-777: Deploy New Payment Integration (BAD)

**ID**: RUN-777
**Type**: Deployment
**Service**: Payment Service

---

**Steps**:
1. Deploy new code to production
2. Test payment processing
3. If it works, celebrate!

---

**Why This is Bad**:

❌ **No rollback plan** (what if payments fail?)
❌ **No pre-deployment checks** (did you test in staging?)
❌ **No success criteria** (how many test transactions? which payment methods?)
❌ **Testing AFTER deployment** (should test BEFORE in staging)
❌ **No communication plan** (notify finance team? support team?)
❌ **No monitoring plan** (which metrics to watch?)
❌ **Production testing** (never test critical systems in production first time)

**Fix**:
- Test thoroughly in staging BEFORE production
- Define rollback plan (feature flag, code rollback)
- Set up monitoring BEFORE deployment (payment success rate, error rate)
- Communicate with stakeholders BEFORE deploying
- Use gradual rollout (10% of users first, then 100%)

---

## Good Pattern Summary

### Runbook Quality Checklist

A good runbook (RUN-XXX) has:

- [x] **Specific ID and metadata** (severity, owner, last tested date)
- [x] **Clear symptoms** (specific alerts, error messages, user reports)
- [x] **Quick reference** (when to use, time to resolve, who to escalate to)
- [x] **Immediate actions** (what to do in first 5 minutes)
- [x] **Diagnosis steps** (how to find root cause)
- [x] **Multiple scenarios** (common causes and solutions)
- [x] **Specific commands** (copy-paste ready, no "check the thing")
- [x] **Success criteria** (how to know issue is resolved)
- [x] **Time estimates** (realistic expectations)
- [x] **Rollback plan** (what if fix doesn't work?)
- [x] **Communication templates** (internal and external)
- [x] **Escalation path** (who to call when)
- [x] **Prevention section** (how to avoid recurrence)
- [x] **Related runbooks** (links to related issues)
- [x] **Testing record** (last tested date, prove it works)

---

## Bad Pattern Summary

### Common Runbook Mistakes

Avoid these anti-patterns:

- ❌ **Vague symptoms** ("when it's broken")
- ❌ **No commands** ("check the database")
- ❌ **Assuming knowledge** ("you know how to do this")
- ❌ **No time estimates** (team doesn't know if stuck)
- ❌ **No escalation** (on-call stuck with no help)
- ❌ **No testing** (runbook never verified, might be wrong)
- ❌ **Out of date** (commands reference old systems)
- ❌ **Missing rollback** (fix makes things worse, no undo)
- ❌ **No communication** (team in dark during incident)
- ❌ **Testing in production** (for critical systems like payments)

---

## Runbook Maintenance

**Quarterly Review**:
- [ ] Test each P0/P1 runbook in staging
- [ ] Update commands if systems changed
- [ ] Update escalation contacts
- [ ] Archive runbooks for deprecated systems

**After Every Incident**:
- [ ] Update runbook if new scenario encountered
- [ ] Add commands that were useful
- [ ] Remove steps that didn't help
- [ ] Update time estimates based on actual resolution time

**When Systems Change**:
- [ ] Update all affected runbooks immediately
- [ ] Test updated runbooks in staging
- [ ] Notify team of changes

---

*Reference: Use these examples when creating RUN-XXX runbooks in `prd-v08-runbook-creation` skill.*
