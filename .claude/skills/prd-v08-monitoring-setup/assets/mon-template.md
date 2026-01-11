# MON-XXX: [Monitoring Rule Title]

**ID**: MON-XXX
**Type**: [Metric | Alert | Dashboard | SLO]
**Layer**: [Infrastructure | Application | Business | User Experience]
**Owner**: [Team responsible for this metric/alert]
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

---

## For Metric Type

**Name**: `[metric.name.format]`
**Description**: [What this measures and why it matters]
**Unit**: [count | ms | percentage | bytes | requests/sec]
**Source**: [Where this comes from - APM tool, logs, custom instrumentation]
**Aggregation**: [avg | sum | min | max | p50 | p95 | p99]
**Retention**: [How long to keep data - e.g., 90 days, 1 year]
**Collection Frequency**: [How often to collect - e.g., 10s, 1m, 5m]

**Baseline**: [Expected normal range under typical load]
**Context**: [Additional context that helps interpret this metric]

---

## For Alert Type

**Metric**: [MON-YYY reference or metric name]
**Condition**: [Threshold expression - e.g., > 500ms, < 95%, >= 10]
**Window**: [Time window for evaluation - e.g., 5 minutes, 15 minutes]
**Severity**: [Critical | Warning | Info]
**Runbook**: [RUN-XXX to follow when this alert fires]

**Notification**:
- **Channel**: [Slack (#channel), PagerDuty, Email, SMS]
- **Recipients**: [Team, role, or individuals - e.g., "Backend on-call", "Tech Lead"]
- **Escalation**: [If not acknowledged within X minutes, escalate to Y]

**Silencing**:
- **Conditions**: [When to suppress - e.g., during maintenance windows]
- **Windows**: [DEP-XXX references for planned maintenance]
- **Override**: [Who can manually silence and for how long]

**False Positive Handling**: [Known scenarios that trigger but aren't incidents]

---

## For Dashboard Type

**Purpose**: [What questions this dashboard answers]
**Audience**: [Who uses this dashboard - e.g., on-call engineers, leadership, ops team]
**URL**: [Link to dashboard in monitoring tool]

**Panels**:
1. [Panel name] - [What it shows and why]
2. [Panel name] - [What it shows and why]
3. [Panel name] - [What it shows and why]

**Refresh**: [How often to update - e.g., 30 seconds, 1 minute, 5 minutes]
**Time Range**: [Default time window - e.g., last 1 hour, last 24 hours]

**Usage Notes**: [How to interpret the dashboard, what to look for]

---

## For SLO Type

**Objective**: [What we promise - clear, measurable statement]
**Target**: [Percentage - e.g., 99.9%, 99.95%]
**Window**: [Evaluation period - e.g., Rolling 30 days, Calendar month]
**Error Budget**: [Calculated allowed downtime - e.g., 43.2 minutes/month for 99.9%]

**Measurement**:
- **Success Criteria**: [What counts as "good" - e.g., non-5xx responses, latency < 500ms]
- **Failure Criteria**: [What counts as "bad" - e.g., 5xx responses, latency >= 500ms]
- **Data Source**: [Where measurements come from]

**Alerting**:
- **50% budget consumed**: [Warning level action]
- **75% budget consumed**: [Critical level action]
- **90% budget consumed**: [Emergency level action]
- **100% budget consumed**: [Breach protocol]

**Burn Rate Alerts**:
- **Fast burn** (1 hour window): Alert if consuming budget at 14.4x rate
- **Slow burn** (6 hour window): Alert if consuming budget at 6x rate

---

## Linked IDs

**Related Specifications**:
- [API-XXX]: [How this relates to API contracts]
- [UJ-XXX]: [How this relates to user journeys]
- [KPI-XXX]: [How this relates to business metrics]
- [BR-XXX]: [How this enforces business rules]

**Related Operations**:
- [RUN-XXX]: [Runbooks triggered by this monitoring]
- [DEP-XXX]: [Deployment procedures that affect this]
- [MON-YYY]: [Related monitoring entries]

**Test Coverage**:
- [TEST-XXX]: [Tests that validate this monitoring works]

---

## Implementation

**Configuration**:
```yaml
# Example configuration for monitoring tool
# (Adjust syntax for your specific tool: Datadog, New Relic, Prometheus, etc.)

[Paste configuration here]
```

**Code Location**:
- **Instrumentation**: [File path where metric is emitted]
- **Alert Definition**: [File path or UI location where alert is configured]
- **Dashboard**: [File path or URL where dashboard is defined]

---

## Validation

**Before Deployment**:
- [ ] Metric collects successfully in staging
- [ ] Alert fires when condition is met (test in staging)
- [ ] Dashboard renders correctly
- [ ] Runbook linked and accessible
- [ ] Notification channels tested
- [ ] Baseline established from staging data

**After Deployment**:
- [ ] Metric appears in production monitoring
- [ ] Alert threshold tuned based on production traffic
- [ ] No false positives in first 7 days
- [ ] Team trained on runbook procedures

---

## Version History

| Version | Date | Change | Updated By |
|---------|------|--------|------------|
| 1.0 | YYYY-MM-DD | Initial creation | [Name] |
| | | | |

---

## Notes

[Any additional context, lessons learned, or edge cases worth documenting]

---

*Template: Use this to create MON-XXX entries in `SoT.deployment_playbook.md`*
