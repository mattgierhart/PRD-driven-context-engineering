# RUN-XXX: [Runbook Title]

**ID**: RUN-XXX
**Type**: [Incident Response | Deployment | Maintenance | Troubleshooting | On-Call Guide]
**Service/System**: [Which service/system this runbook covers]
**Severity**: [P0 - Critical | P1 - High | P2 - Medium | P3 - Low]
**Owner**: [Team responsible - e.g., Backend Team, DevOps]
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Last Tested**: YYYY-MM-DD

---

## Quick Reference

**When to Use**: [One-line description of when this runbook applies]

**Time to Resolve**: [Typical time to resolve - e.g., 5 minutes, 30 minutes, 2 hours]

**Escalation**: [Who to escalate to if stuck - e.g., @backend-lead, @cto]

**Related Runbooks**:
- [RUN-YYY]: [Related runbook - e.g., Database connection pool exhaustion]
- [RUN-ZZZ]: [Related runbook - e.g., API latency spike troubleshooting]

---

## Symptoms

**What You'll See** (one or more of these):

### Alerts
- [ ] [MON-XXX]: [Alert name - e.g., "High Error Rate"]
- [ ] [MON-YYY]: [Alert name - e.g., "API Latency SLO Breach"]

### User Reports
- [ ] Users reporting: [Description - e.g., "Can't log in", "Checkout failing"]
- [ ] Support tickets: [Pattern - e.g., Spike in "500 error" tickets]

### Dashboards
- [ ] [MON-XXX Dashboard]: [What you'll see - e.g., Error rate > 5%, normally 0.1%]
- [ ] [MON-YYY Dashboard]: [What you'll see - e.g., p95 latency > 2s, normally 200ms]

### Logs
- [ ] Error pattern: `[Example error message or pattern]`
- [ ] Log location: [Where to find logs - e.g., CloudWatch /aws/lambda/api, Datadog]

---

## Impact Assessment

**User Impact**:
- **Severity P0 (Critical)**: Complete outage, all users affected, revenue stopped
- **Severity P1 (High)**: Major degradation, >25% users affected, critical journeys broken
- **Severity P2 (Medium)**: Partial degradation, <25% users affected, non-critical journeys
- **Severity P3 (Low)**: Minor issue, <5% users affected, workarounds available

**Affected User Journeys**:
- [UJ-XXX]: [Journey name - e.g., User Login]
- [UJ-YYY]: [Journey name - e.g., Checkout Flow]

**Business Impact**:
- **Revenue**: [Direct impact - e.g., "Checkout down = $10k/hour revenue loss"]
- **Reputation**: [User trust impact - e.g., "Payment failures damage trust"]
- **SLO**: [SLO impact - e.g., "Consumes 10% of monthly error budget per hour"]

---

## Immediate Actions (First 5 Minutes)

**Goal**: Stop the bleeding, minimize user impact.

### Step 1: Acknowledge Alert
- [ ] Acknowledge alert in monitoring tool (PagerDuty, Datadog, etc.)
- [ ] Post in #incidents channel: "Investigating [issue], ETA update in 5 min"
- [ ] Assign yourself as incident commander (if not already assigned)

### Step 2: Assess Scope
- [ ] Check dashboard ([MON-XXX]): How many users affected?
- [ ] Check error rate: What's current % vs baseline?
- [ ] Check recent changes: Any deploys in last 2 hours? (Check #deployments channel or deployment log)

### Step 3: Immediate Mitigation (If Applicable)
- [ ] **If recent deploy**: Consider rollback (see [DEP-XXX rollback procedure])
  - Rollback if: Error rate > [threshold]%, latency > [threshold]ms, critical journey broken
- [ ] **If traffic spike**: Scale up infrastructure (see Infrastructure Scaling section)
- [ ] **If external dependency down**: Enable fallback/cache (see Fallback Procedures section)
- [ ] **If unknown cause**: Continue to Diagnosis section

---

## Diagnosis (Next 15-30 Minutes)

**Goal**: Find root cause.

### Step 1: Check Recent Changes
- [ ] **Code Deploys**: Check deployment log or #deployments channel
  - Last deploy: [When? What changed?]
  - Correlate timing with issue start
- [ ] **Infrastructure Changes**: Check Terraform/CloudFormation logs
  - Database upgrades? Server scaling? DNS changes?
- [ ] **Configuration Changes**: Check feature flags, environment variables
  - Did someone toggle a flag? Change a config value?

### Step 2: Check Logs
- [ ] **Application Logs**: [Log location - e.g., CloudWatch /aws/ecs/api]
  - Search for: `[error pattern - e.g., "ERROR" or "Exception"]`
  - Filter by time: [Issue start time to now]
  - Look for: Stack traces, error messages, correlation IDs
- [ ] **Database Logs**: [Log location - e.g., RDS slow query log]
  - Search for: Slow queries, deadlocks, connection errors
- [ ] **External API Logs**: [If applicable]
  - Are third-party APIs slow/failing? (Stripe, Sendgrid, etc.)

### Step 3: Check Infrastructure
- [ ] **Compute Resources**:
  - CPU: [Normal range vs current - e.g., 30-40% normal, 95% now = problem]
  - Memory: [Normal range vs current]
  - Disk: [Check disk space, IOPS]
- [ ] **Database**:
  - Connection pool: [Utilization - e.g., 180/200 connections = near limit]
  - Query performance: [Slow query log]
  - Replication lag: [For read replicas]
- [ ] **Network**:
  - Latency to dependencies: [Ping external APIs, databases]
  - DNS resolution: [Check DNS working]
  - Load balancer health: [Are all targets healthy?]

### Step 4: Check Monitoring & Traces
- [ ] **Distributed Tracing**: [Tool - e.g., Datadog APM, New Relic]
  - Find slow requests: Filter by latency > [threshold]
  - Identify bottleneck: Which service/function is slow?
- [ ] **Error Tracking**: [Tool - e.g., Sentry]
  - Group similar errors
  - Find common pattern (user type, browser, endpoint, etc.)

---

## Resolution Steps

### Scenario 1: Caused by Recent Deployment

**Diagnosis**: Error rate spiked after deploy at [time], correlates exactly.

**Resolution**:
1. [ ] Rollback deployment (see [DEP-XXX] rollback procedure)
2. [ ] Verify error rate returns to baseline within 5 minutes
3. [ ] Post in #incidents: "Rolled back [deploy], monitoring"
4. [ ] If error rate normal: Mark incident resolved, schedule post-mortem
5. [ ] If error rate still high: Continue to Scenario 2

**Time to Resolve**: 5-15 minutes

---

### Scenario 2: Infrastructure Overload (CPU/Memory/Disk)

**Diagnosis**: CPU > 90%, memory > 95%, or disk > 90% on [service] servers.

**Resolution**:
1. [ ] **Immediate**: Scale up infrastructure
   - **Kubernetes**: `kubectl scale deployment [service] --replicas=[current + 5]`
   - **Auto Scaling Group**: Increase desired capacity via AWS Console or CLI
   - **Manual**: Add servers to load balancer
2. [ ] Monitor for 5 minutes: Did error rate drop? Latency improve?
3. [ ] If improved: Keep scaled up, investigate root cause (why sudden load?)
4. [ ] If not improved: Check for resource leak (memory leak, connection leak)

**Time to Resolve**: 10-20 minutes (scaling) + investigation time

---

### Scenario 3: Database Connection Pool Exhausted

**Diagnosis**: Logs show "Cannot acquire connection" or connection pool at max (200/200).

**Resolution**:
1. [ ] **Immediate**: Increase connection pool size
   - Update environment variable: `DB_POOL_SIZE=[current × 1.5]`
   - Redeploy or restart service (depends on config hot-reload)
2. [ ] **Alternative**: Restart database connection pool (if service supports it)
3. [ ] **Investigate**: Why are connections not released?
   - Check for long-running transactions (slow queries)
   - Check for connection leaks (code not closing connections)
4. [ ] Monitor: Connection pool utilization should drop below 80%

**Time to Resolve**: 10-30 minutes

**Follow-up**: Fix connection leaks in code, optimize slow queries

---

### Scenario 4: External Dependency Down

**Diagnosis**: Third-party API (Stripe, Sendgrid, etc.) returning errors or timing out.

**Resolution**:
1. [ ] **Check Status Page**: [External service status - e.g., status.stripe.com]
2. [ ] **Enable Fallback** (if available):
   - Feature flag: `use_fallback_[service]` to TRUE
   - Example: Use cached data instead of live API call
3. [ ] **Circuit Breaker** (if implemented):
   - Verify circuit breaker opened (stops calling failing service)
   - Users see graceful degradation (not 500 errors)
4. [ ] **Communicate**:
   - Update status page: "Experiencing issues with [service], investigating"
   - Post in #incidents: "External dependency down, fallback enabled"
5. [ ] **Monitor External Service**:
   - When service recovers, disable fallback
   - Run smoke tests to verify integration working

**Time to Resolve**: 5-10 minutes (enable fallback), then wait for external service recovery

---

### Scenario 5: Database Deadlock

**Diagnosis**: Logs show "Deadlock detected" or "Lock wait timeout exceeded".

**Resolution**:
1. [ ] **Immediate**: Kill long-running transactions
   - Find blocking queries: `SHOW PROCESSLIST;` (MySQL) or `pg_stat_activity` (PostgreSQL)
   - Kill query: `KILL [process_id];`
2. [ ] **Identify Cause**:
   - Which tables involved? (Check deadlock log)
   - Which transactions conflicting? (Application logs)
3. [ ] **Prevent Recurrence**:
   - Reorder transactions (acquire locks in same order)
   - Add index (if missing index causing long lock)
   - Reduce transaction scope (lock fewer rows)
4. [ ] Monitor: Deadlock count should drop to zero

**Time to Resolve**: 5-10 minutes (kill queries), hours-days (prevent recurrence via code fix)

---

### Scenario 6: Unknown Cause

**Diagnosis**: No clear root cause after 30 minutes of investigation.

**Resolution**:
1. [ ] **Escalate**: Call in [escalation contact - e.g., @backend-lead, @cto]
2. [ ] **War Room**: Set up video call, collaborate on investigation
3. [ ] **Expand Search**:
   - Check less obvious logs (CDN logs, DNS logs, network logs)
   - Check earlier time range (did issue start earlier, unnoticed?)
   - Correlate with external events (AWS outage, DDoS attack?)
4. [ ] **Mitigation**:
   - If revenue-critical, consider full rollback (revert to last known good state)
   - If non-critical, monitor and investigate offline
5. [ ] **Document**: Capture all findings in incident log for post-mortem

**Time to Resolve**: Variable (hours), depends on complexity

---

## Communication Plan

### Internal Communication

**#incidents Channel Updates**:

**Initial** (< 5 minutes):
```
🚨 INCIDENT: [Service] [Issue Description]
- Severity: [P0/P1/P2/P3]
- Impact: [User impact description]
- Investigating: @[your-name]
- ETA update: 5 minutes
```

**Updates** (every 15-30 minutes):
```
📊 UPDATE: [Service] Incident
- Status: [Investigating | Mitigating | Resolved]
- Root Cause: [If known]
- Action Taken: [What we did]
- Next Update: [Time]
```

**Resolution**:
```
✅ RESOLVED: [Service] Incident
- Duration: [Start time - End time]
- Root Cause: [Brief description]
- User Impact: [How many users, how long]
- Follow-up: [Post-mortem scheduled, link to doc]
```

---

### External Communication (Customer-Facing)

**Status Page** (if customer-facing outage):

**Initial**:
```
Investigating: We are currently investigating issues with [feature/service].
Updates will be posted every 30 minutes.
```

**Updates**:
```
Identified: We have identified the issue and are working on a fix.
Expected resolution: [Time or "within 1 hour"].
```

**Resolution**:
```
Resolved: The issue has been resolved. All services are operational.
We apologize for the inconvenience.
```

---

## Escalation Path

**Level 1**: On-call engineer (you)
- **Responsibility**: Initial response, diagnosis, resolution
- **Escalate if**: Can't resolve in 30 minutes OR severity P0

**Level 2**: [Team Lead - e.g., @backend-lead]
- **Contact**: [Slack, Phone]
- **Responsibility**: Senior diagnosis, architectural decisions
- **Escalate if**: Can't resolve in 1 hour OR severity P0 unresolved

**Level 3**: [Engineering Manager / CTO]
- **Contact**: [Slack, Phone]
- **Responsibility**: Executive decisions (full rollback, customer communication)
- **Escalate if**: Major outage (> 1 hour) OR data loss risk

---

## Post-Incident Checklist

After incident resolved:

- [ ] **Update Status Page**: Mark incident resolved
- [ ] **Post Final Update**: #incidents channel with resolution summary
- [ ] **Notify Stakeholders**: Product, support, leadership
- [ ] **Preserve Evidence**: Save logs, metrics, screenshots
- [ ] **Schedule Post-Mortem**: If P0/P1 or >30 min downtime
  - **When**: Within 48 hours
  - **Who**: Incident commander, on-call, relevant team leads
  - **Agenda**: Timeline, root cause, user impact, action items
- [ ] **Update This Runbook**: Add new scenarios, improve procedures
- [ ] **Create Action Items**: Assign follow-up work (bug fixes, monitoring improvements)

---

## Linked IDs

**Monitoring & Alerts**:
- [MON-XXX]: [Alert or dashboard that triggers this runbook]
- [MON-YYY]: [Related monitoring entry]

**User Journeys Affected**:
- [UJ-XXX]: [User journey impacted by this issue]
- [UJ-YYY]: [User journey impacted by this issue]

**Deployments**:
- [DEP-XXX]: [Deployment procedure - for rollback scenarios]

**Business Rules**:
- [BR-XXX]: [Business rule related to this issue]

**Tests**:
- [TEST-XXX]: [Test that should catch this issue in future]

---

## Prevention

**How to Prevent This Issue in Future**:

1. **Monitoring**:
   - [ ] Alert exists: [MON-XXX] for early warning
   - [ ] Dashboard shows: [Metric] to track health

2. **Testing**:
   - [ ] Test exists: [TEST-XXX] to catch in staging
   - [ ] Load test includes: [Scenario that triggers this issue]

3. **Code/Architecture**:
   - [ ] Circuit breaker implemented (for external dependency failures)
   - [ ] Graceful degradation (fallback behavior)
   - [ ] Resource limits set (prevent runaway resource consumption)

4. **Process**:
   - [ ] Deployment checklist includes: [Check that would catch this]
   - [ ] Code review looks for: [Pattern that causes this issue]

---

## Testing This Runbook

**Last Tested**: YYYY-MM-DD
**Tested By**: [Name]
**Test Procedure**:
1. Simulate incident in staging (e.g., kill database connections, deploy broken code)
2. Follow this runbook step-by-step
3. Measure time to resolve
4. Document gaps or unclear steps
5. Update runbook based on findings

**Next Test Due**: YYYY-MM-DD (recommend: quarterly for critical runbooks)

---

## Version History

| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | YYYY-MM-DD | Initial creation | [Name] |
| | | | |

---

## Notes

[Any additional context, edge cases, or known issues worth documenting]

---

*Template: Use this to create RUN-XXX entries in `SoT.deployment_playbook.md` or separate runbook repository.*
