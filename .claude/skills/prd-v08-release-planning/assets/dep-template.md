# DEP-XXX: [Deployment Title]

**ID**: DEP-XXX
**Type**: [Release | Hotfix | Rollback | Migration]
**Environment**: [Staging | Production | Canary | All]
**Strategy**: [Blue-Green | Canary | Rolling | Feature Flag | Big Bang]
**Owner**: [Team/Person responsible for deployment]
**Created**: YYYY-MM-DD
**Target Date**: YYYY-MM-DD
**Status**: [Planned | In Progress | Completed | Rolled Back]

---

## Summary

**What**: [Brief description of what is being deployed]

**Why**: [Business or technical reason for this deployment]

**Risk Level**: [Low | Medium | High | Critical]

**Deployment Window**: [Date/time range - e.g., 2026-01-15 02:00-04:00 UTC]

**Estimated Duration**: [Expected time to complete - e.g., 30 minutes, 2 hours]

**Rollback Estimated Duration**: [Time to rollback if needed - e.g., 5 minutes, 15 minutes]

---

## Changes Included

**Features**:
- [FEA-XXX]: [Feature description]
- [FEA-YYY]: [Feature description]

**Bug Fixes**:
- [Issue #123]: [Bug description]
- [Issue #456]: [Bug description]

**Infrastructure Changes**:
- [ARC-XXX]: [Architecture change description]
- [Infrastructure change description]

**Database Migrations**:
- [DBT-XXX]: [Migration description - e.g., add index, add column, data backfill]

**Dependencies**:
- [External service upgrade - e.g., PostgreSQL 14 → 15]
- [Library upgrade - e.g., React 17 → 18]

---

## Pre-Deployment Checklist

**Code Quality**:
- [ ] All tests passing (TEST-XXX)
- [ ] Code review approved
- [ ] Security scan passed
- [ ] Performance testing completed (if applicable)

**Documentation**:
- [ ] Changelog updated
- [ ] API documentation updated (if API changes)
- [ ] Runbook updated (RUN-XXX)
- [ ] Monitoring updated (MON-XXX) for new metrics/alerts

**Infrastructure**:
- [ ] Infrastructure changes applied to staging
- [ ] Database migrations tested in staging
- [ ] Capacity planning reviewed (traffic projections)
- [ ] DNS/CDN changes prepared (if applicable)

**Communication**:
- [ ] Stakeholders notified (product, support, customers if downtime)
- [ ] On-call schedule confirmed
- [ ] Incident channel prepared (#incidents)
- [ ] Status page updated (if customer-facing downtime expected)

**Rollback Plan**:
- [ ] Rollback procedure documented (see Rollback Plan section)
- [ ] Rollback tested in staging
- [ ] Database rollback plan ready (if schema changes)
- [ ] Feature flags configured (if applicable)

---

## Deployment Steps

### Step 1: Pre-Deployment Validation

**Actions**:
1. [ ] Verify all pre-deployment checklist items complete
2. [ ] Confirm monitoring dashboards accessible (MON-XXX)
3. [ ] Confirm on-call team ready
4. [ ] Take database backup (if schema changes)
5. [ ] Record baseline metrics (request rate, error rate, latency)

**Success Criteria**: All checklist items checked, baselines recorded

**Rollback Trigger**: N/A (not yet deployed)

---

### Step 2: [Deployment Strategy Specific Steps]

**For Blue-Green**:
1. [ ] Deploy to green environment
2. [ ] Run smoke tests on green
3. [ ] Switch 10% traffic to green (canary within blue-green)
4. [ ] Monitor for 15 minutes
5. [ ] Switch 100% traffic to green
6. [ ] Monitor blue environment (keep as rollback target)

**For Canary**:
1. [ ] Deploy to canary nodes (10% of fleet)
2. [ ] Monitor canary metrics for 30 minutes
3. [ ] If healthy, deploy to 50% of fleet
4. [ ] Monitor for 30 minutes
5. [ ] Deploy to 100% of fleet

**For Rolling**:
1. [ ] Deploy to first availability zone (AZ-1)
2. [ ] Monitor AZ-1 for 15 minutes
3. [ ] Deploy to second availability zone (AZ-2)
4. [ ] Monitor AZ-2 for 15 minutes
5. [ ] Deploy to third availability zone (AZ-3)
6. [ ] Monitor full deployment for 30 minutes

**For Feature Flag**:
1. [ ] Deploy code with feature flag OFF
2. [ ] Verify deployment successful (no errors)
3. [ ] Enable feature flag for internal users (10%)
4. [ ] Monitor for 1 hour
5. [ ] Enable for 50% of users
6. [ ] Monitor for 4 hours
7. [ ] Enable for 100% of users

**Success Criteria**: [Specific metrics - e.g., error rate < 0.1%, p95 latency < 500ms, no increase in 5xx]

**Rollback Trigger**: [Specific conditions - e.g., error rate > 1%, p95 latency > 1000ms, 5xx errors > 10/minute]

---

### Step 3: Post-Deployment Validation

**Actions**:
1. [ ] Run smoke tests on production
2. [ ] Verify critical user journeys (UJ-XXX)
   - [ ] [UJ-101]: [Journey name - e.g., User signup]
   - [ ] [UJ-102]: [Journey name - e.g., Checkout flow]
3. [ ] Check monitoring dashboards (MON-XXX)
   - [ ] Request rate within expected range
   - [ ] Error rate < threshold (SLO compliance)
   - [ ] Latency within expected range
4. [ ] Verify database migrations completed (if applicable)
5. [ ] Check logs for unexpected errors
6. [ ] Confirm feature flags in expected state (if applicable)

**Success Criteria**: All critical journeys working, metrics within SLO, no unexpected errors

**Rollback Trigger**: Critical journey broken, SLO breached, data corruption detected

---

### Step 4: Monitoring Period

**Duration**: [Time to monitor before declaring success - e.g., 2 hours, 24 hours]

**Metrics to Watch**:
- [ ] Request rate (expect: [baseline ± X%])
- [ ] Error rate (expect: < [threshold]%)
- [ ] p95 latency (expect: < [threshold]ms)
- [ ] Database query performance (expect: < [threshold]ms)
- [ ] Error budget consumption (expect: < [X]% of monthly budget)

**Actions**:
- [ ] Monitor dashboards every 15 minutes for first hour
- [ ] Monitor dashboards every hour for next [duration]
- [ ] Review logs for new error patterns
- [ ] Check support channels for user-reported issues

**Success Criteria**: All metrics within expected range, no user-reported critical issues

**Rollback Trigger**: [Specific conditions that require rollback during monitoring]

---

### Step 5: Deployment Completion

**Actions**:
1. [ ] Update status page (deployment complete)
2. [ ] Notify stakeholders (deployment successful)
3. [ ] Document any issues encountered and resolutions
4. [ ] Update runbooks (RUN-XXX) if procedures changed
5. [ ] Schedule post-deployment review (if high-risk deployment)
6. [ ] Clean up old resources (e.g., decommission blue environment after 24 hours)

**Success Criteria**: Deployment marked complete, stakeholders notified

---

## Rollback Plan

### Rollback Decision Tree

**Trigger Conditions** (any of these requires rollback consideration):
- [ ] Error rate > [threshold]% for > [duration] minutes
- [ ] p95 latency > [threshold]ms for > [duration] minutes
- [ ] Critical user journey (UJ-XXX) broken
- [ ] Data corruption detected
- [ ] SLO budget consumption > [X]% in [duration] hours
- [ ] Security vulnerability discovered in deployed code

**Decision Process**:
1. **Assess Impact**: How many users affected? Is it getting worse?
2. **Attempted Fix**: Can we fix forward quickly? (< 15 minutes)
3. **Rollback Decision**: If fix > 15 minutes or impact severe, rollback

**Decision Makers**: [On-call lead, Engineering Manager, CTO (for critical deployments)]

---

### Rollback Procedure

**Strategy-Specific Rollback**:

**Blue-Green**:
1. [ ] Switch traffic back to blue environment (< 1 minute)
2. [ ] Verify blue environment healthy
3. [ ] Monitor for 15 minutes
4. [ ] Investigate issue in green environment (offline)

**Canary**:
1. [ ] Stop deployment (prevent further rollout)
2. [ ] Route traffic away from canary nodes
3. [ ] Revert canary nodes to previous version
4. [ ] Monitor for 15 minutes

**Rolling**:
1. [ ] Stop deployment (prevent rollout to remaining nodes)
2. [ ] Revert deployed nodes to previous version (one AZ at a time)
3. [ ] Monitor each AZ after revert
4. [ ] Verify all nodes on previous version

**Feature Flag**:
1. [ ] Turn feature flag OFF (< 1 minute)
2. [ ] Verify feature disabled for all users
3. [ ] Monitor for 15 minutes
4. [ ] Investigate issue with feature code (offline)

**Database Migration Rollback**:
1. [ ] Run reverse migration script (TEST IN STAGING FIRST)
2. [ ] Verify data integrity
3. [ ] Revert application code to previous version
4. [ ] Monitor for data consistency issues

**Estimated Rollback Time**: [e.g., 5 minutes (feature flag), 15 minutes (code rollback), 1 hour (database rollback)]

---

### Post-Rollback Actions

1. [ ] Update status page (deployment rolled back)
2. [ ] Notify stakeholders
3. [ ] Preserve logs and metrics from failed deployment
4. [ ] Create incident report (if SLO impacted)
5. [ ] Schedule post-mortem (if high-impact)
6. [ ] Fix identified issues in development environment
7. [ ] Re-test before next deployment attempt

---

## Go/No-Go Criteria

**Go Criteria** (all must be true):
- [ ] All pre-deployment checklist items complete
- [ ] All tests passing in staging
- [ ] On-call team available and ready
- [ ] Rollback plan tested and ready
- [ ] No active incidents (P0 or P1)
- [ ] Not during high-traffic period (unless scheduled maintenance)
- [ ] Stakeholders notified and aligned

**No-Go Criteria** (any of these blocks deployment):
- [ ] Tests failing in staging
- [ ] Active P0/P1 incident
- [ ] On-call team unavailable
- [ ] Rollback plan not tested
- [ ] Database backup failed
- [ ] Dependency service unstable
- [ ] High-traffic period (Black Friday, product launch, etc.) without explicit approval

---

## Monitoring & Alerting

**Dashboards to Monitor**:
- [MON-XXX]: [Dashboard name - e.g., API Health Dashboard]
- [MON-YYY]: [Dashboard name - e.g., Database Performance Dashboard]

**Alerts to Watch**:
- [MON-XXX]: [Alert name - e.g., High Error Rate Alert]
- [MON-YYY]: [Alert name - e.g., Latency SLO Breach Alert]

**Silenced Alerts** (during deployment window):
- [Alert name]: [Reason for silencing - e.g., Expected brief downtime during blue-green switch]

**Runbooks**:
- [RUN-XXX]: [Runbook for common deployment issues]
- [RUN-YYY]: [Runbook for rollback procedure]

---

## Communication Plan

**Before Deployment**:
- [ ] [Target audience]: [Message - e.g., "Scheduled maintenance 2026-01-15 02:00-04:00 UTC, expect brief downtime"]
- [ ] Internal teams: Engineering, Product, Support, Sales (if customer impact)
- [ ] External: Customers via email/status page (if downtime expected)

**During Deployment**:
- [ ] Post updates in #deployments Slack channel every 15 minutes
- [ ] Update status page if customer-facing impact

**After Deployment**:
- [ ] [Target audience]: [Message - e.g., "Deployment complete, new features now available"]
- [ ] Internal teams: Deployment summary (duration, issues, outcome)
- [ ] External: Customers via email/status page (if notified beforehand)

**Rollback Communication**:
- [ ] Immediate update in #incidents channel
- [ ] Update status page (if customer-facing)
- [ ] Notify stakeholders of rollback and next steps

---

## Linked IDs

**Related Specifications**:
- [FEA-XXX]: [Features being deployed]
- [API-XXX]: [API contracts affected]
- [DBT-XXX]: [Database migrations included]
- [ARC-XXX]: [Architecture changes]

**Related Operations**:
- [RUN-XXX]: [Runbooks for deployment and rollback]
- [MON-XXX]: [Monitoring and alerting]
- [TEST-XXX]: [Tests validating this deployment]

**Related Business**:
- [KPI-XXX]: [KPIs expected to be impacted by this deployment]
- [UJ-XXX]: [User journeys affected]

---

## Post-Deployment Review

**Scheduled**: [Date/time for review - e.g., 2026-01-16 10:00 AM]

**Attendees**: [Deployment owner, on-call engineers, product manager (if high-impact)]

**Agenda**:
1. Review deployment timeline (planned vs actual)
2. Discuss any issues encountered
3. Review metrics (SLO impact, user feedback)
4. Identify improvements for future deployments
5. Update runbooks/procedures if needed

**Outcomes**:
- [ ] Lessons learned documented
- [ ] Action items assigned (if improvements identified)
- [ ] Runbooks updated (if procedures changed)

---

## Version History

| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | YYYY-MM-DD | Initial deployment plan | [Name] |
| | | | |

---

## Notes

[Any additional context, dependencies, or risks worth documenting]

---

*Template: Use this to create DEP-XXX entries in `SoT.deployment_playbook.md`*
