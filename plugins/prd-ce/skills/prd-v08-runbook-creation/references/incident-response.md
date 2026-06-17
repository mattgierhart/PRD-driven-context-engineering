# Incident Response Patterns

**Purpose**: Framework for responding to incidents with severity-based response patterns.

---

## Severity Definitions

### P0 - Critical (Complete Outage)

**Definition**: Complete service unavailability or data loss risk

**Impact**:
- All users affected (100%)
- Revenue stopped completely
- Critical user journeys broken
- Data integrity at risk

**Examples**:
- Database down, all API requests failing
- Payment processing completely offline
- Authentication system down (no one can log in)
- Data deletion bug in production

**Response Time**: < 5 minutes (immediate)

**Escalation**: Auto-escalate to leadership immediately

**Communication**: External status page + internal war room

---

### P1 - High (Major Degradation)

**Definition**: Significant degradation affecting critical journeys

**Impact**:
- >25% of users affected
- Critical journeys degraded but not broken
- Revenue significantly impacted
- SLO breach imminent

**Examples**:
- Payment processing slow (timeout on 30% of requests)
- API latency spike (p95 from 200ms to 5s)
- Database replication lag causing stale data
- Critical third-party integration down

**Response Time**: < 15 minutes

**Escalation**: Notify on-call lead, escalate after 30 min if unresolved

**Communication**: Internal incident channel + consider external status update

---

### P2 - Medium (Partial Degradation)

**Definition**: Limited degradation affecting non-critical journeys

**Impact**:
- <25% of users affected
- Non-critical journeys degraded
- Workarounds available
- SLO impact minor

**Examples**:
- Email notifications delayed
- Search results incomplete
- Minor UI bugs affecting specific browsers
- Non-critical feature broken

**Response Time**: < 1 hour

**Escalation**: Only if can't resolve in 2 hours

**Communication**: Internal only, no external status update

---

### P3 - Low (Minor Issue)

**Definition**: Minimal impact, annoyance level

**Impact**:
- <5% of users affected
- Cosmetic or minor functional issues
- No revenue impact
- No SLO impact

**Examples**:
- Typo in UI text
- Non-critical analytics not recording
- Dark mode color inconsistency
- Admin panel minor bug

**Response Time**: Next business day

**Escalation**: None (fix in normal workflow)

**Communication**: None (ticket/bug tracking only)

---

## Incident Response Framework

### Phase 1: Detection & Acknowledgment (0-5 minutes)

**Goal**: Confirm incident and take ownership

**Actions**:
1. **Acknowledge Alert**
   - Acknowledge in monitoring tool (PagerDuty, Datadog)
   - Self-assign as incident commander
   - Note incident start time

2. **Initial Assessment**
   - Check dashboards for scope
   - Confirm severity (P0/P1/P2/P3)
   - Identify affected user journeys

3. **Declare Incident**
   - Post in #incidents channel
   - Format: "🚨 INCIDENT: [Service] [Issue] - Severity [PX] - Investigating - @[your-name]"
   - Set next update time (5-15 min depending on severity)

**Success Criteria**: Incident acknowledged, team aware, clock started

---

### Phase 2: Immediate Mitigation (5-30 minutes)

**Goal**: Stop the bleeding, reduce user impact

**Actions**:

**For Recent Deployments** (within 2 hours):
- [ ] Check deployment log for correlation
- [ ] If correlated: Rollback deployment (see DEP-XXX)
- [ ] Verify error rate drops within 5 minutes

**For Traffic Spikes**:
- [ ] Check traffic dashboard
- [ ] Scale infrastructure if capacity issue
- [ ] Enable rate limiting if abuse

**For External Dependencies**:
- [ ] Check third-party status pages
- [ ] Enable fallback/cache if available
- [ ] Enable circuit breaker

**For Database Issues**:
- [ ] Check connection pool utilization
- [ ] Check for deadlocks or slow queries
- [ ] Consider read-only mode if data integrity risk

**Communication**:
- Post update every 15 minutes (P0/P1) or 30 minutes (P2)
- Update status page if customer-facing

**Success Criteria**: User impact reduced, root cause hypothesis formed

---

### Phase 3: Root Cause Diagnosis (30-60 minutes)

**Goal**: Identify underlying cause

**Investigation Path**:

1. **Timeline Analysis**
   - When did issue start? (exact time)
   - What changed around that time?
   - Gradual or sudden onset?

2. **Change Correlation**
   - Code deployments (last 24 hours)
   - Infrastructure changes (scaling, upgrades)
   - Configuration changes (feature flags, env vars)
   - External events (upstream API changes)

3. **Log Analysis**
   - Application logs (error messages, stack traces)
   - Database logs (slow queries, deadlocks)
   - Infrastructure logs (CPU, memory, disk)
   - External API logs (latency, errors)

4. **Metric Analysis**
   - Error rate (when did it spike?)
   - Latency (which percentile increased?)
   - Traffic (volume spike or normal?)
   - Resource utilization (CPU, memory, connections)

**Tools**:
- Distributed tracing (find slow services)
- Error tracking (group similar errors)
- Profiling (identify bottlenecks)

**Success Criteria**: Root cause identified with evidence

---

### Phase 4: Permanent Fix (Variable)

**Goal**: Resolve underlying issue, prevent recurrence

**For Code Bugs**:
- [ ] Write failing test that reproduces issue
- [ ] Fix bug
- [ ] Verify test passes
- [ ] Deploy fix (follow standard deployment process)

**For Infrastructure Issues**:
- [ ] Scale resources (if capacity)
- [ ] Optimize configuration (if misconfiguration)
- [ ] Add redundancy (if single point of failure)

**For Process Issues**:
- [ ] Update runbook (capture new scenario)
- [ ] Add monitoring (prevent future occurrence)
- [ ] Update deployment checklist

**Success Criteria**: Issue resolved, metrics return to baseline

---

### Phase 5: Post-Incident Review (Within 48 hours)

**Goal**: Learn and prevent recurrence

**Required for**:
- All P0 incidents
- P1 incidents lasting >30 minutes
- Any incident with data loss or customer complaints

**Post-Mortem Structure**:

1. **Timeline** (exact timestamps)
   - Detection time
   - Mitigation start time
   - Resolution time
   - Total duration

2. **Impact**
   - Users affected (count or %)
   - Revenue impact ($ lost)
   - SLO impact (error budget consumed)
   - Customer complaints (support tickets)

3. **Root Cause**
   - What happened (technical explanation)
   - Why it happened (underlying cause)
   - Why it wasn't caught earlier (detection gap)

4. **What Went Well**
   - Fast detection
   - Effective mitigation
   - Good communication

5. **What Went Poorly**
   - Slow diagnosis
   - Missing runbook
   - Unclear ownership

6. **Action Items** (with owners and deadlines)
   - Code fixes (prevent recurrence)
   - Monitoring improvements (detect earlier)
   - Runbook updates (respond faster)
   - Process changes (prevent similar issues)

**Success Criteria**: Post-mortem documented, action items assigned

---

## Communication Patterns

### Internal Communication (Slack)

**Initial Notification** (< 5 min):
```
🚨 INCIDENT: [Service] [Brief Description]
- Severity: P[0/1/2/3]
- User Impact: [Description]
- Affected Journeys: [UJ-XXX, UJ-YYY]
- Investigating: @[your-name]
- Next Update: [Time] (15 min)
```

**Progress Updates** (Every 15-30 min):
```
📊 UPDATE: [Service] Incident
- Status: [Investigating | Mitigating | Monitoring | Resolved]
- Root Cause: [If known, else "Still investigating"]
- Actions Taken: [What we've done]
- Current Impact: [Better/Worse/Same]
- Next Update: [Time]
```

**Resolution** (Final):
```
✅ RESOLVED: [Service] Incident
- Duration: [HH:MM] ([Start] - [End])
- Root Cause: [Brief explanation]
- Fix Applied: [What we did]
- User Impact: [X users for Y minutes]
- Post-Mortem: [Link or "Scheduled for [date]"]
```

---

### External Communication (Status Page)

**For Customer-Facing Outages Only** (P0/P1):

**Investigating**:
```
[YYYY-MM-DD HH:MM UTC] Investigating
We are investigating issues with [feature/service].
Some users may experience [specific impact].
We will provide updates every 30 minutes.
```

**Identified**:
```
[YYYY-MM-DD HH:MM UTC] Identified
We have identified the issue as [brief non-technical explanation].
We are working on a fix.
Expected resolution: [Time or "within X hours"]
```

**Monitoring**:
```
[YYYY-MM-DD HH:MM UTC] Monitoring
A fix has been applied and we are monitoring the situation.
Service should be returning to normal.
```

**Resolved**:
```
[YYYY-MM-DD HH:MM UTC] Resolved
The issue has been fully resolved.
All services are operational.
We apologize for the inconvenience.
```

---

## Escalation Patterns

### When to Escalate

**Escalate Immediately**:
- P0 incidents (always)
- Data loss risk
- Security breach
- Can't diagnose after 15 minutes (P0/P1)

**Escalate After Time Threshold**:
- P1: After 30 minutes unresolved
- P2: After 2 hours unresolved
- P3: Don't escalate (handle in normal workflow)

**Escalate for Decisions**:
- Full rollback needed (affects other features)
- Customer communication needed
- Feature freeze decision
- Trade-off between mitigation strategies

---

### Escalation Ladder

**Level 1: On-Call Engineer** (You)
- **Role**: First responder, initial diagnosis, standard mitigation
- **Authority**: Rollback recent deploys, scale infrastructure, enable fallbacks
- **Escalate When**: Can't resolve in time threshold OR P0

**Level 2: On-Call Lead / Senior Engineer**
- **Role**: Senior diagnosis, architectural decisions, non-standard mitigation
- **Authority**: All of Level 1 + schema changes, major rollbacks, customer communication
- **Escalate When**: Can't resolve after 1 hour OR data loss risk

**Level 3: Engineering Manager / CTO**
- **Role**: Executive decisions, customer relations, vendor escalation
- **Authority**: All of Level 2 + feature freeze, contract negotiations, public statements
- **Escalate When**: >1 hour outage OR revenue impact >$X OR data breach

---

## War Room Pattern

**When to Use**: P0 incidents or P1 lasting >30 minutes

**Setup**:
1. **Create Zoom/Meet link** (posted in #incidents)
2. **Assign Roles**:
   - **Incident Commander**: Coordinates response, makes decisions
   - **Scribe**: Documents timeline and actions in real-time
   - **Communications**: Updates Slack, status page, stakeholders
   - **Engineers**: Investigate and fix (1-3 people depending on complexity)

3. **Ground Rules**:
   - Scribe logs every action with timestamp
   - Commander makes all decisions (no design by committee)
   - Side conversations in separate thread
   - Regular status updates (every 15 min)

**Exit Criteria**: Issue resolved OR downgraded to P2 (can handle async)

---

## Good Pattern Examples

### Good Pattern 1: Fast Rollback

**Incident**: Error rate spike to 5% after deployment

**Response**:
- **T+0 min**: Alert triggered, on-call acknowledges
- **T+2 min**: Checked deployment log, new deploy 10 min ago
- **T+3 min**: Posted in #incidents: "Rolling back v2.4.5, error rate spike"
- **T+5 min**: Rollback complete
- **T+7 min**: Error rate back to 0.1% baseline
- **T+10 min**: Posted resolution, scheduled post-mortem

**Why Good**:
✅ Correlated deployment quickly
✅ Didn't over-investigate (clear cause = fast action)
✅ Communicated before acting
✅ Verified fix worked

**Time to Resolve**: 7 minutes

---

### Good Pattern 2: Systematic Diagnosis

**Incident**: API latency spike (p95 from 200ms to 3s), no recent deployment

**Response**:
- **T+0 min**: Alert, acknowledge
- **T+3 min**: Checked deployment log (nothing in 24 hours)
- **T+5 min**: Checked traffic (normal volume)
- **T+8 min**: Checked database (CPU 95%, normally 30%)
- **T+10 min**: Slow query log shows new pattern (missing index)
- **T+12 min**: Killed long-running queries (latency drops to 500ms)
- **T+15 min**: Added index (latency back to 200ms)
- **T+20 min**: Investigating why query pattern changed
- **T+30 min**: Found: Marketing sent email, drove traffic to un-indexed report page

**Why Good**:
✅ Systematic checklist (deployment → traffic → infrastructure)
✅ Immediate mitigation (killed queries) before permanent fix
✅ Root cause investigation continued after mitigation
✅ Found underlying cause (email campaign)

**Time to Resolve**: 15 minutes (mitigation), 30 minutes (root cause)

---

## Bad Pattern Examples (Anti-Patterns)

### Bad Pattern 1: Premature Rollback

**Incident**: Error rate spike

**Bad Response**:
- **T+0 min**: Alert
- **T+1 min**: "Rolling back!"
- **T+5 min**: Rollback complete, error rate still high
- **T+10 min**: "Rollback didn't work, trying another rollback"
- **T+20 min**: "Maybe it's not deployment?"

**Problems**:
❌ Didn't verify correlation with deployment
❌ Acted without diagnosis
❌ Multiple rollbacks caused more instability
❌ No communication

**Fix**: Check deployment log FIRST, correlate timing before rollback

---

### Bad Pattern 2: Analysis Paralysis

**Incident**: Complete outage (P0)

**Bad Response**:
- **T+0 min**: Alert
- **T+5 min**: Reading logs
- **T+15 min**: Still reading logs
- **T+30 min**: "Found interesting error, let me trace this..."
- **T+45 min**: "Actually might be this other thing..."
- **T+60 min**: Still diagnosing, users still down

**Problems**:
❌ No immediate mitigation attempted
❌ Over-investigating instead of acting
❌ No escalation despite P0
❌ Users down for 60+ minutes

**Fix**: For P0, try standard mitigations FIRST (rollback, scale up, enable fallback), diagnose while mitigating

---

### Bad Pattern 3: No Communication

**Incident**: Payment processing down (P0)

**Bad Response**:
- **T+0 min**: Alert acknowledged (no Slack post)
- **T+20 min**: Fixed issue
- **T+21 min**: "Fixed!" (first communication)

**Problems**:
❌ Team didn't know issue was happening
❌ Support got angry customer calls with no context
❌ Leadership found out from customers
❌ No status page update (customers in the dark)

**Fix**: Communicate IMMEDIATELY in #incidents, update every 15 min, update status page

---

## Runbook Testing Pattern

**Frequency**: Quarterly for P0/P1 runbooks, annually for P2/P3

**Test Procedure**:

1. **Schedule Game Day**
   - Calendar block (1-2 hours)
   - Team assembled
   - Staging environment ready

2. **Simulate Incident**
   - Deploy broken code to staging, OR
   - Kill database connections, OR
   - Inject high latency/errors

3. **Follow Runbook**
   - On-call engineer follows runbook step-by-step
   - Observer takes notes (gaps, unclear steps)
   - Timer tracks time to resolve

4. **Debrief**
   - What worked well?
   - What was unclear?
   - What's missing?
   - Update runbook based on findings

5. **Update Runbook**
   - Clarify ambiguous steps
   - Add missing scenarios
   - Update "Last Tested" date

**Success Criteria**: Can follow runbook to resolution without external help

---

## Prevention Patterns

**After Every Incident**, ask:

1. **Detection**: How can we detect this faster?
   - Add monitoring/alerting (MON-XXX)
   - Lower alert threshold

2. **Prevention**: How can we prevent this?
   - Add test (TEST-XXX)
   - Add validation (API contract, schema validation)
   - Add circuit breaker/fallback

3. **Mitigation**: How can we respond faster?
   - Update runbook (add scenario)
   - Automate common actions
   - Pre-bake rollback procedures

4. **Architecture**: What systemic change prevents this class of issue?
   - Add redundancy
   - Improve graceful degradation
   - Reduce coupling

**Action Items**: Assign with deadlines, track in backlog

---

*Reference: Use these patterns when creating RUN-XXX runbooks in `prd-v08-runbook-creation` skill.*
