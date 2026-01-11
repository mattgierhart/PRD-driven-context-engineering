# Dashboard Design Guide

**Purpose**: Best practices for creating effective monitoring dashboards.

---

## Core Principles

### 1. Dashboards Answer Questions

Every dashboard should answer specific questions for a specific audience.

**Good Example**:
- **Dashboard**: "API Health"
- **Audience**: On-call engineers during incidents
- **Questions**: "Is the API up?", "What's the error rate?", "Which endpoint is slow?"

**Bad Example**:
- **Dashboard**: "Metrics"
- **Audience**: Everyone
- **Questions**: Unclear (kitchen sink of graphs)

**Fix**: Create multiple focused dashboards instead of one mega-dashboard.

---

### 2. Hierarchy: Overview → Detail

Design dashboards in layers:

**Layer 1: Overview Dashboard** (5-10 seconds to assess health)
- Service status (up/down)
- SLO compliance (green/yellow/red)
- Error budget remaining
- Traffic volume

**Layer 2: Service Dashboard** (diagnose which service/component)
- Per-service metrics (latency, errors, throughput)
- Service dependencies
- Recent deploys

**Layer 3: Deep Dive Dashboard** (root cause specific issue)
- Detailed logs
- Request traces
- Database query performance
- Infrastructure metrics (CPU, memory, disk)

**Usage**:
- Start at Layer 1 during incident
- Drill down to Layer 2 to identify affected service
- Use Layer 3 to find root cause

---

### 3. Prioritize Signal Over Noise

**Good Dashboard**:
- 6-8 panels max (fits on one screen)
- Clear "healthy" vs "unhealthy" visual signals
- Auto-refreshes every 30-60 seconds

**Bad Dashboard**:
- 50 graphs (scrolling required)
- Everything looks like noise (unclear what's actionable)
- Refresh disabled or too slow (stale data during incidents)

**Fix**: Apply the "Glance Test" — can you assess health in 5 seconds?

---

## Dashboard Patterns

### Pattern 1: RED Method (Requests, Errors, Duration)

**Best For**: HTTP services, APIs, microservices

**Panels**:
1. **Request Rate** (requests/second)
   - Shows traffic volume
   - Detects traffic spikes or drops

2. **Error Rate** (errors/second or % errors)
   - Shows reliability
   - Alerts when SLO at risk

3. **Duration** (p50, p95, p99 latency)
   - Shows performance
   - Detects slow endpoints

**Example Layout**:
```
┌─────────────────┬─────────────────┐
│ Request Rate    │ Error Rate      │
│ (requests/sec)  │ (% 5xx)         │
└─────────────────┴─────────────────┘
┌─────────────────────────────────┐
│ Duration (p50, p95, p99)        │
│ (ms)                            │
└─────────────────────────────────┘
```

**When to Use**: Default dashboard for any service handling requests

---

### Pattern 2: USE Method (Utilization, Saturation, Errors)

**Best For**: Infrastructure (servers, databases, queues)

**Panels**:
1. **Utilization** (% of resource used)
   - CPU %, Memory %, Disk %, Network %
   - Shows current load

2. **Saturation** (queue depth, wait time)
   - Database connection pool utilization
   - Message queue depth
   - Shows if resource is overloaded

3. **Errors** (error count or rate)
   - Disk errors, network errors, OOM kills
   - Shows reliability issues

**Example Layout**:
```
┌─────────────────┬─────────────────┐
│ CPU %           │ Memory %        │
└─────────────────┴─────────────────┘
┌─────────────────┬─────────────────┐
│ DB Pool Utiliz. │ Queue Depth     │
└─────────────────┴─────────────────┘
┌─────────────────────────────────┐
│ Infrastructure Errors           │
└─────────────────────────────────┘
```

**When to Use**: Database, cache, queue, server-level monitoring

---

### Pattern 3: SLO Dashboard

**Best For**: Executive/leadership visibility, quarterly reviews

**Panels**:
1. **SLO Compliance** (% in compliance)
   - Green if meeting SLO, red if breached
   - Shows overall health at a glance

2. **Error Budget Remaining** (%)
   - Shows how much budget left
   - Informs feature vs stability tradeoff

3. **Burn Rate** (current consumption rate)
   - Shows if consuming budget faster than expected
   - Early warning of SLO risk

4. **Time to Budget Exhaustion** (days/hours)
   - Projection of when budget will run out
   - Prioritization signal

**Example Layout**:
```
┌─────────────────────────────────┐
│ SLO Compliance: 99.92%          │
│ ✅ MEETING SLO (99.9% target)   │
└─────────────────────────────────┘
┌─────────────────┬─────────────────┐
│ Error Budget    │ Burn Rate       │
│ 78% Remaining   │ 1.2× (normal)   │
└─────────────────┴─────────────────┘
┌─────────────────────────────────┐
│ Time to Exhaustion: 22 days     │
└─────────────────────────────────┘
```

**When to Use**: Weekly leadership reviews, quarterly business reviews, public status pages

---

### Pattern 4: Deployment Dashboard

**Best For**: During and after deployments (linked to DEP-XXX)

**Panels**:
1. **Deployment Timeline** (markers on graph)
   - Shows when deploys happened
   - Correlate issues with specific deploys

2. **Request Rate** (before vs after)
   - Detect traffic drops (broken feature)
   - Detect unexpected spikes (retry storm)

3. **Error Rate** (before vs after)
   - Spot regressions immediately
   - Trigger rollback if errors spike

4. **Latency** (p95 before vs after)
   - Detect performance regressions
   - Validate performance improvements

5. **Rollback Trigger** (alert status)
   - Clear visual: "ROLLBACK NEEDED" vs "Healthy"

**Example Layout**:
```
┌─────────────────────────────────┐
│ Deployment Timeline             │
│ (markers on time series)        │
└─────────────────────────────────┘
┌─────────────────┬─────────────────┐
│ Request Rate    │ Error Rate      │
│ Before vs After │ Before vs After │
└─────────────────┴─────────────────┘
┌─────────────────┬─────────────────┐
│ p95 Latency     │ Rollback Trigger│
│ Before vs After │ ✅ Healthy       │
└─────────────────┴─────────────────┘
```

**When to Use**: Open during deploys, linked from DEP-XXX entries

---

### Pattern 5: User Journey Dashboard

**Best For**: Product-focused monitoring (linked to UJ-XXX)

**Panels** (one section per critical journey):
1. **Journey Success Rate** (% completed)
   - Track end-to-end success (signup, checkout, etc.)
   - Detect drop-offs at specific steps

2. **Journey Duration** (time to complete)
   - Measure user experience
   - Identify slow steps

3. **Drop-off Points** (funnel visualization)
   - Where users abandon the journey
   - Prioritize optimization work

**Example** (E-commerce Checkout - UJ-102):
```
┌─────────────────────────────────┐
│ Checkout Success Rate: 94.2%    │
│ (Target: 95% - SLO: MON-023)    │
└─────────────────────────────────┘
┌─────────────────┬─────────────────┐
│ Time to Checkout│ Drop-off Points │
│ p95: 45s        │ 1. Cart: 3%     │
│ (Target: 60s)   │ 2. Payment: 2%  │
│                 │ 3. Confirm: 1%  │
└─────────────────┴─────────────────┘
```

**When to Use**: Product analytics, KPI tracking (link to KPI-XXX)

---

## Panel Design Best Practices

### 1. Use Appropriate Visualizations

**Time Series Graph**: For trends over time
- Request rate, error rate, latency
- Good for: Spotting spikes, drops, patterns

**Gauge/Number**: For single current value
- SLO compliance %, error budget remaining
- Good for: At-a-glance status

**Heatmap**: For distribution over time
- Latency distribution (p50, p90, p95, p99)
- Good for: Spotting outliers, tail latency

**Table**: For top-N lists
- Slowest endpoints, most errors by route
- Good for: Prioritizing investigation

**Anti-Pattern**: Pie charts for time-series data (hard to spot trends)

---

### 2. Set Meaningful Y-Axis Ranges

**Good**:
- Y-axis starts at 0 for counts (requests/sec, errors)
- Y-axis starts just below SLO threshold for percentages (e.g., 98-100% for 99% SLO)

**Bad**:
- Auto-scaling Y-axis makes small changes look dramatic
- Fixed range that clips actual values

**Example**:
- For 99.9% SLO, set Y-axis range: 99%-100% (makes violations obvious)
- For latency, set Y-axis to expected max (e.g., 0-1000ms), not auto-scale

---

### 3. Add Threshold Lines

**Pattern**: Draw horizontal line at SLO threshold

**Example**:
- SLO: 99.9% success rate → Draw red line at 99.9%
- SLO: p95 latency < 500ms → Draw red line at 500ms

**Benefit**: Instantly see if metric is violating SLO

**Implementation**:
- Grafana: Add "Threshold" in panel settings
- Datadog: Add "Threshold" line in graph settings

---

### 4. Use Color Intentionally

**Standard Color Scheme**:
- **Green**: Healthy, meeting SLO
- **Yellow**: Warning, approaching threshold (50-75% error budget consumed)
- **Red**: Critical, breaching SLO or >75% error budget consumed
- **Blue**: Informational (traffic, deployments)

**Anti-Pattern**: Random colors (makes it hard to spot issues at a glance)

---

### 5. Include Context Markers

**Deployment Markers**: Vertical lines showing when deploys happened
- Correlate issues with changes
- Validate deploy success

**Incident Markers**: Annotations for known incidents
- Historical context for patterns
- Learn from past incidents

**Example** (Grafana):
```
Query: deployment_events (from CI/CD pipeline)
Display as: Vertical line annotation
Label: "Deploy: v1.2.3"
```

---

## Dashboard Hierarchy Example

### Example: E-Commerce SaaS

#### Layer 1: System Overview (NOC/Leadership)

**Audience**: Executives, on-call rotation, NOC
**Refresh**: 30 seconds
**URL**: `/dashboards/overview`

**Panels**:
1. Overall SLO Compliance (99.92% - green)
2. Error Budget Remaining (78%)
3. Active Incidents (0)
4. Request Volume (12.3k req/sec)

**Purpose**: "Is everything healthy?" (5-second glance)

---

#### Layer 2: Service Health (On-Call Engineers)

**Audience**: On-call engineers during incident
**Refresh**: 30 seconds
**URL**: `/dashboards/services`

**Panels** (per service):
1. API Service: Request rate, error rate, p95 latency
2. Web Service: Request rate, error rate, p95 latency
3. Background Jobs: Queue depth, processing rate, error rate
4. Database: Connection pool, query latency, deadlocks

**Purpose**: "Which service is affected?" (30-second diagnosis)

---

#### Layer 3: Deep Dive (Root Cause Analysis)

**Audience**: On-call engineers, postmortem investigators
**Refresh**: 10 seconds
**URL**: `/dashboards/api-deep-dive`

**Panels**:
1. Per-endpoint latency breakdown
2. Database query performance
3. External API call latency (dependencies)
4. Infrastructure metrics (CPU, memory, network)
5. Recent error logs (tail)
6. Request traces (distributed tracing)

**Purpose**: "What's the root cause?" (5-10 minute investigation)

---

## Anti-Patterns

### Anti-Pattern 1: Dashboard Sprawl

**Problem**: 50+ dashboards, no one knows which to use during incident.

**Example**: "API Dashboard", "API Dashboard v2", "API Dashboard Final", "API Dashboard FINAL FINAL"

**Fix**:
- Consolidate to 3 layers (Overview, Service, Deep Dive)
- Delete or archive unused dashboards
- Document which dashboard for which scenario (in RUN-XXX runbooks)

---

### Anti-Pattern 2: Vanity Metrics

**Problem**: Tracking metrics that don't inform action.

**Example**: "Total users ever" (always goes up, not actionable)

**Fix**: Only track metrics that inform decisions:
- SLO compliance → feature freeze or keep shipping?
- Error budget → invest in reliability or features?
- Request rate → scale up or investigate drop?

---

### Anti-Pattern 3: No Drill-Down Links

**Problem**: Overview dashboard shows problem but no way to investigate.

**Example**: "Error rate high" but no link to logs or traces.

**Fix**:
- Link overview panels to service dashboards
- Link service dashboards to deep dive
- Link graphs to log queries (filtered by time range)

**Example** (Grafana):
- Panel → Data Links → `/dashboards/api-deep-dive?from=${__from}&to=${__to}`

---

### Anti-Pattern 4: Stale Dashboards

**Problem**: Dashboard doesn't reflect current architecture (services added/removed).

**Example**: Dashboard still shows "Old API" service that was decommissioned 6 months ago.

**Fix**:
- Review dashboards during postmortems (are they helpful?)
- Update dashboards when architecture changes (link to ARC-XXX)
- Use templating for dynamic service lists (Grafana variables)

---

### Anti-Pattern 5: No Time Synchronization

**Problem**: Comparing metrics from different dashboards but time ranges don't match.

**Example**: "Error rate spiked at 2pm" but latency graph shows 1-3pm window (can't correlate).

**Fix**:
- Use dashboard time picker (applies to all panels)
- Link dashboards with time range parameters: `?from=${__from}&to=${__to}`
- Default to "Last 1 hour" or "Last 6 hours" for consistency

---

## Dashboard Checklist

Before finalizing a dashboard:

- [ ] **Purpose is clear**: Dashboard answers specific questions for specific audience
- [ ] **Glance test passes**: Can assess health in 5 seconds
- [ ] **Limited panels**: 6-8 panels max (fits on one screen without scrolling)
- [ ] **Appropriate visualizations**: Time series for trends, gauge for current value
- [ ] **Threshold lines**: SLO thresholds clearly marked
- [ ] **Color-coded**: Green (healthy), yellow (warning), red (critical)
- [ ] **Auto-refresh**: 30-60 seconds for active monitoring
- [ ] **Drill-down links**: Can navigate to deeper detail
- [ ] **Context markers**: Deployments and incidents annotated
- [ ] **Linked to runbooks**: Dashboard URL in RUN-XXX entries
- [ ] **Linked to SLOs**: Dashboard URL in MON-XXX SLO entries
- [ ] **Accessible**: Team knows where to find it (documented in RUN-XXX)

---

## Dashboard Templates

### Template 1: Service Dashboard (RED Method)

```
Dashboard: [Service Name] Health
Audience: On-call engineers
Refresh: 30 seconds

┌─────────────────────────────────────────────────────┐
│ [Service Name] Status: ✅ Healthy                   │
│ SLO Compliance: 99.95% (Target: 99.9%)              │
│ Error Budget: 82% Remaining                         │
└─────────────────────────────────────────────────────┘
┌─────────────────┬─────────────────┬─────────────────┐
│ Request Rate    │ Error Rate      │ p95 Latency     │
│ (requests/sec)  │ (% 5xx)         │ (ms)            │
│ ───────────     │ ───────────     │ ───────────     │
│ [graph]         │ [graph]         │ [graph]         │
│ Threshold: None │ Threshold: 0.1% │ Threshold: 500ms│
└─────────────────┴─────────────────┴─────────────────┘
┌─────────────────────────────────────────────────────┐
│ Recent Deployments (markers on timeline)            │
│ ────────────────────────────────────────────────────│
│ [deployment timeline]                               │
└─────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────┐
│ Top 5 Slowest Endpoints (p95 latency)               │
│ ────────────────────────────────────────────────────│
│ [table: endpoint, latency, volume]                  │
└─────────────────────────────────────────────────────┘

Links:
- Deep Dive Dashboard: /dashboards/[service]-deep-dive
- Runbook: RUN-XXX (Incident Response)
- SLO Definition: MON-XXX
```

---

### Template 2: SLO Executive Dashboard

```
Dashboard: Platform SLO Summary
Audience: Engineering leadership, executives
Refresh: 1 minute

┌─────────────────────────────────────────────────────┐
│ Overall Platform Health: ✅ Meeting All SLOs        │
└─────────────────────────────────────────────────────┘
┌─────────────────┬─────────────────┬─────────────────┐
│ API             │ Web             │ Background Jobs │
│ ✅ 99.93%       │ ✅ 99.91%       │ ✅ 99.95%       │
│ (Target: 99.9%) │ (Target: 99.9%) │ (Target: 99.9%) │
│ Budget: 85%     │ Budget: 91%     │ Budget: 78%     │
└─────────────────┴─────────────────┴─────────────────┘
┌─────────────────────────────────────────────────────┐
│ Error Budget Trend (Rolling 30 Days)                │
│ ────────────────────────────────────────────────────│
│ [graph showing budget consumption over time]        │
└─────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────┐
│ Incidents This Month: 2                             │
│ ────────────────────────────────────────────────────│
│ 1. 2026-01-05: API latency spike (5 min, resolved)  │
│ 2. 2026-01-08: DB connection pool exhaustion (12min)│
└─────────────────────────────────────────────────────┘

Links:
- Service Dashboards: /dashboards/services
- SLO Definitions: SoT.deployment_playbook.md (MON-XXX entries)
- Incident Postmortems: /docs/postmortems/
```

---

*Reference: Use this guide when creating dashboards in `prd-v08-monitoring-setup` skill.*
