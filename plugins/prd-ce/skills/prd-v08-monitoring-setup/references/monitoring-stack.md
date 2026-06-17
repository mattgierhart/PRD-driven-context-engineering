# Monitoring Stack Selection Guide

**Purpose**: Help teams select the right monitoring tools for their context.

---

## Stack Categories

### Application Performance Monitoring (APM)

Tools that instrument your application code to track performance, errors, and user experience.

#### Datadog

**Best For**: Teams wanting all-in-one observability with strong infrastructure monitoring.

**Pros**:
- Unified platform (APM, logs, infrastructure, RUM, security)
- Excellent service map visualization
- Strong third-party integrations (AWS, GCP, Azure, databases)
- Built-in anomaly detection
- Good documentation

**Cons**:
- Expensive at scale (per-host + custom metrics pricing)
- Can be overkill for simple applications
- Vendor lock-in concerns

**When to Use**:
- Microservices architecture
- Multi-cloud or hybrid infrastructure
- Teams valuing unified dashboards over cost optimization

---

#### New Relic

**Best For**: Full-stack visibility with strong developer experience.

**Pros**:
- Intuitive UI for developers
- Excellent distributed tracing
- Good error tracking and alerting
- Free tier for small projects
- Strong mobile app monitoring

**Cons**:
- Pricing based on data ingestion (can get expensive)
- Query language (NRQL) has learning curve
- Less flexible than Prometheus for custom metrics

**When to Use**:
- Developer-centric teams
- Applications with complex transaction flows
- Need for mobile app monitoring

---

#### Grafana + Prometheus

**Best For**: Teams wanting open-source, cost-effective, highly customizable monitoring.

**Pros**:
- Open source (no vendor lock-in)
- Extremely flexible and customizable
- Cost-effective (self-hosted or Grafana Cloud)
- Strong Kubernetes integration
- Time-series optimized

**Cons**:
- Requires more setup and maintenance
- Steeper learning curve (PromQL)
- Alerting less polished than commercial tools
- Need to integrate separate tools for logs (Loki) and traces (Tempo)

**When to Use**:
- Kubernetes-native applications
- Cost-sensitive teams with DevOps expertise
- Need for custom metrics and dashboards
- Open-source philosophy preference

---

#### Sentry

**Best For**: Error tracking and crash reporting.

**Pros**:
- Best-in-class error tracking
- Excellent stack trace and context
- Release tracking (correlate errors with deploys)
- Affordable pricing
- Good open-source option

**Cons**:
- Not a full APM solution (focused on errors)
- Limited infrastructure monitoring
- Need to pair with other tools for full observability

**When to Use**:
- Error tracking is primary concern
- Want actionable error context (user sessions, breadcrumbs)
- Complement to infrastructure monitoring

---

### Logging Solutions

#### Elasticsearch + Kibana (ELK Stack)

**Best For**: Centralized log aggregation with powerful search.

**Pros**:
- Powerful full-text search
- Mature ecosystem
- Good for log analysis and investigation
- Self-hosted or managed (Elastic Cloud)

**Cons**:
- Resource intensive (especially Elasticsearch)
- Complex to operate at scale
- Licensing changes (no longer pure open source)

**When to Use**:
- Need powerful log search and analysis
- Have DevOps expertise for operation
- Large log volumes requiring indexing

---

#### Loki (Grafana)

**Best For**: Cost-effective logging for Kubernetes and cloud-native apps.

**Pros**:
- Cost-effective (indexes labels, not full text)
- Integrates seamlessly with Grafana
- Good for structured logs
- Lower resource requirements than ELK

**Cons**:
- Limited full-text search (indexes labels only)
- Newer, smaller ecosystem than ELK
- Query performance depends on label design

**When to Use**:
- Already using Grafana
- Cost-sensitive teams
- Structured logging practices
- Kubernetes environments

---

### Synthetic Monitoring / Uptime

#### Pingdom

**Best For**: Simple uptime monitoring and alerting.

**Pros**:
- Easy setup
- Reliable uptime checks
- Transaction monitoring
- Affordable

**Cons**:
- Limited compared to APM solutions
- Basic synthetic monitoring only

**When to Use**:
- External uptime monitoring
- Simple transactional checks
- Supplement to internal monitoring

---

#### Checkly

**Best For**: Headless browser monitoring with Playwright/Puppeteer.

**Pros**:
- Modern, developer-friendly
- Monitoring as code (TypeScript/JavaScript)
- Good CI/CD integration
- Reasonable pricing

**Cons**:
- Focused on browser-based checks only
- Smaller ecosystem

**When to Use**:
- Need to monitor complex user flows
- Want monitoring as code
- JavaScript/TypeScript team

---

## Decision Framework

### By Company Stage

**Early Startup (Pre-Product/Market Fit)**:
- **Recommendation**: Sentry (errors) + Simple logging (CloudWatch/Cloud Logging)
- **Rationale**: Focus on shipping, minimize overhead
- **Budget**: < $100/month

**Growth Stage (Post-PMF, Scaling)**:
- **Recommendation**: Datadog or New Relic (full APM) + Sentry (errors)
- **Rationale**: Need visibility into performance bottlenecks
- **Budget**: $500-2000/month

**Enterprise / Cost-Sensitive Teams**:
- **Recommendation**: Prometheus + Grafana + Loki (self-hosted or Grafana Cloud)
- **Rationale**: Cost control, flexibility, no vendor lock-in
- **Budget**: $200-1000/month (Grafana Cloud) or infrastructure costs (self-hosted)

---

### By Architecture

**Monolith**:
- New Relic or Datadog (simpler distributed tracing less important)

**Microservices**:
- Datadog (best service maps) or Grafana + Tempo (cost-effective)

**Serverless**:
- Datadog (good Lambda support) or native cloud provider tools (CloudWatch, Azure Monitor)

**Kubernetes**:
- Prometheus + Grafana (native integration) or Datadog (easier setup)

---

### By Team Expertise

**Limited DevOps Resources**:
- Datadog or New Relic (managed, low maintenance)

**Strong DevOps Team**:
- Prometheus + Grafana + Loki (flexibility, cost control)

**Developer-Focused Team**:
- New Relic (intuitive UI) + Sentry (error tracking)

---

## Common Patterns

### Minimal Stack (Early Stage)

```
Error Tracking: Sentry
Uptime: Pingdom or built-in cloud provider
Logs: Cloud provider (CloudWatch, Cloud Logging, Azure Monitor)
Infrastructure: Cloud provider dashboards
```

**Cost**: ~$50-100/month
**Maintenance**: Low
**Coverage**: Errors + uptime only

---

### Recommended Stack (Growth Stage)

```
APM: Datadog or New Relic
Error Tracking: Sentry (better error context than APM-only)
Uptime: Pingdom or Checkly
Logs: Included in APM tool
```

**Cost**: ~$500-2000/month
**Maintenance**: Low-Medium
**Coverage**: Full observability

---

### Cost-Optimized Stack (DevOps-Savvy Team)

```
Metrics: Prometheus
Dashboards: Grafana
Logs: Loki
Traces: Tempo
Error Tracking: Sentry (open source or cloud)
Uptime: Pingdom or self-hosted (Uptime Kuma)
```

**Cost**: ~$200-500/month (Grafana Cloud) or infrastructure only (self-hosted)
**Maintenance**: High (self-hosted) or Medium (Grafana Cloud)
**Coverage**: Full observability with flexibility

---

## Anti-Patterns

### Anti-Pattern 1: Over-Tooling Early

**Problem**: Paying for enterprise APM before finding product-market fit.

**Example**: $2000/month Datadog contract for a 2-person startup.

**Fix**: Start with Sentry + cloud provider tools, upgrade when revenue justifies it.

---

### Anti-Pattern 2: No Centralized Logging

**Problem**: SSH-ing into servers to tail logs during incidents.

**Example**: "Which server had that error? Let me check all 10..."

**Fix**: At minimum, use cloud provider log aggregation (CloudWatch Insights, GCP Logs Explorer).

---

### Anti-Pattern 3: Metrics Without Context

**Problem**: Tracking metrics without linking to user impact or business outcomes.

**Example**: Monitoring CPU % without knowing which user journeys are affected.

**Fix**: Tag metrics with journey IDs (UJ-XXX) and link to KPIs (KPI-XXX).

---

### Anti-Pattern 4: Alert Fatigue

**Problem**: Too many alerts, team ignores them.

**Example**: Alerting on every non-200 response including expected 404s.

**Fix**: Alert on SLO budget consumption (see `slo-guide.md`), not individual events.

---

### Anti-Pattern 5: Monitoring Without Runbooks

**Problem**: Alerts fire but team doesn't know how to respond.

**Example**: "API latency high" alert with no next steps.

**Fix**: Every alert (MON-XXX) must link to a runbook (RUN-XXX).

---

## Migration Patterns

### From Cloud Provider to APM Tool

**Trigger**: Outgrow cloud provider dashboards (multiple services, complex flows).

**Steps**:
1. Start with APM trial (Datadog, New Relic) on one critical service
2. Validate value (reduced MTTR, better visibility)
3. Expand to other services
4. Deprecate custom CloudWatch/Cloud Logging dashboards

**Timeline**: 2-4 weeks
**Risk**: Low (run in parallel during trial)

---

### From Commercial APM to Open Source

**Trigger**: Cost concerns, vendor lock-in, need for customization.

**Steps**:
1. Set up Prometheus + Grafana in parallel
2. Migrate dashboards (start with most-used)
3. Migrate alerts (test thoroughly)
4. Run in parallel for 2-4 weeks
5. Deprecate commercial tool

**Timeline**: 1-3 months
**Risk**: Medium (alerting gaps during transition)

---

## Validation Checklist

Before committing to a monitoring stack:

- [ ] **Trial Period**: Run 2-4 week trial with real production traffic
- [ ] **Alert Test**: Trigger alerts intentionally, verify notifications work
- [ ] **MTTR Test**: Simulate incident, measure time to identify root cause
- [ ] **Cost Projection**: Calculate cost at 2x, 5x, 10x current scale
- [ ] **Team Training**: Can on-call team use the tool without documentation?
- [ ] **Integration**: Does it integrate with your deploy pipeline (DEP-XXX)?
- [ ] **Runbook Linking**: Can you link alerts (MON-XXX) to runbooks (RUN-XXX)?

---

*Reference: Use this guide when selecting monitoring tools in `prd-v08-monitoring-setup` skill.*
