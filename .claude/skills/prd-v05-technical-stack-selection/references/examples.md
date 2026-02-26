# TECH- Entry Examples

Three filled examples covering the most common decision categories: Reuse, Buy, and Research.

---

## Example 1: Reuse Decision

```markdown
TECH-109: Application Authentication & Identity Management
Category: Reuse
Layer: Auth
Purpose: Enterprise SSO, user identity management, role-based access control

Reuse From: Product-A — OAuth 2.0 / OIDC identity provider deployment
Reuse Scope: Shared instance (separate tenant/realm for Product-B)
Current State: OAuth provider deployed and operational for Product-A on cloud infrastructure.
  Team has existing operational experience. Supports standard OIDC, SAML 2.0, and LDAP/AD federation.
Changes Needed: Create dedicated Product-B tenant. Configure identity provider federations for
  Product-B customer organizations. Add Product-B-specific roles (analyst, reviewer, admin).

Shared or Separate: Shared deployment, separate tenant/realm

Features Served: FEA-010 (User login), FEA-011 (User signup), FEA-012 (Social/Enterprise auth)
Risk Constraints: Enterprise customers require SSO and federation

Cost: $0 (already running; incremental cost only for tenant expansion)
Integration Complexity: Low (team already operates the provider)
Lock-in Risk: Very Low (using standard protocols, portable to other OIDC/SAML providers)

Product Family Notes: Shared identity provider enables single sign-on across Product-A and
  Product-B if a customer uses both products. Evaluate if cross-product identity should be unified.
```

**Why this is a good Reuse entry:**

- Documents where the asset comes from and what state it's in
- Explicitly lists what changes are needed (not just "reuse it")
- Addresses shared vs. separate deployment decision
- Explains the product family implication (cross-product SSO)
- Cost is transparent ($0 for reuse, not hidden)

---

## Example 2: Buy Decision

```markdown
TECH-105: Primary Data Store
Category: Buy
Layer: Database
Purpose: Store application data, user profiles, configuration, audit trails

Features Served: FEA-100, FEA-101, FEA-102, FEA-103, FEA-104, FEA-200, FEA-201
Risk Constraints: RISK-006 (data consistency requirement), RISK-007 (query performance <200ms)

Decision: Managed PostgreSQL (cloud-hosted with generous provisioning)
Rationale: For MVP, we optimize for speed-to-market and team velocity, not cost minimization.
  A managed service eliminates infrastructure overhead so the team can focus on product.
  Generous provisioning (vs. minimum viable) means we won't hit performance bottlenecks while
  learning usage patterns. We'll optimize costs in v2 once we understand unit economics.
  Lock-in risk is low (standard PostgreSQL — portable to any host when needed).

Alternatives Considered:
  - Cost-optimized self-managed PostgreSQL: Lowest cost but team would spend weeks on DevOps
    during MVP instead of shipping product. Not worth it.
  - MongoDB: Document store fits some data shapes but weaker for relational queries.
    Self-managed would add operational burden.
  - SQLite: Sufficient for MVP but forces painful migration at scale, defeating purpose of
    getting to market fast.

Trade-offs:
  - Pro: Managed removes ops burden, predictable costs, proven for MVP scale, fast iteration
  - Con: Higher monthly cost than self-managed, vendor dependency (mitigated by standard PostgreSQL)

Cost: ~$100-200/month current MVP scale (generous provisioning). Will optimize to ~$30-50/month
  once usage patterns are known and product-market fit is achieved. Don't pre-optimize.
Integration Complexity: Low (standard JDBC/psycopg drivers, mature ORM support)
Lock-in Risk: Low (standard PostgreSQL — data portable to any PostgreSQL-compatible host)
```

**Why this is a good Buy entry:**

- Rationale explicitly chooses speed-to-market over cost optimization for MVP (this is the right tradeoff)
- Acknowledges the decision is temporary: will optimize costs post-PMF when usage is understood
- Alternatives show the real cost of "being cheap": team ops burden during critical MVP phase
- Trade-offs are honest: higher cost now, but cheaper than lost time/velocity
- Lock-in risk is assessed with mitigation (standard PostgreSQL = portable when you do optimize)

---

## Example 3: Research Decision

```markdown
TECH-005: Vector Database for Semantic Search
Category: Research
Layer: Database
Purpose: Store and query embeddings for AI-powered semantic document search

Features Served: FEA-025 (semantic search), FEA-026 (document similarity recommendations)
Risk Constraints: RISK-012 (query latency <200ms P99), RISK-014 (scale to 10M+ documents)

Decision: TBD after POC (default to pgvector if feasible)
Rationale: Multiple viable options with different trade-offs. pgvector (Postgres extension)
  is attractive because it reuses existing database, but may not scale well. Managed services
  (Pinecone, Weaviate Cloud) trade cost for operational simplicity. Self-hosted Weaviate
  offers control but operational overhead. Need POC to validate performance and cost assumptions.

Alternatives to Evaluate:
  1. pgvector (PostgreSQL extension): Reuses existing Postgres, simpler stack, but uncertain
     scaling performance
  2. Pinecone: Fully managed, fast setup, good docs. Cost: $70/mo base + $0.10/vector-month.
     Vendor lock-in concern.
  3. Weaviate (self-hosted): Open source, more control. Cost: ~$200/mo infra, significant
     ops burden for tuning and scaling.

Trade-offs:
  - Pro for pgvector: No new vendor, reuses existing infrastructure, low cost
  - Con for pgvector: Scaling performance unproven at 10M vectors
  - Pro for managed (Pinecone): Operational simplicity, good support
  - Con for managed: Ongoing vendor dependency, cost at scale

Cost: Ranges from $0 (pgvector) to $500+/mo (Pinecone at scale). Ops cost: 0-40 hrs/month.
Integration Complexity: Low for pgvector, Medium for Pinecone, High for self-hosted
Lock-in Risk: Low (pgvector), High (Pinecone), Medium (Weaviate)

Research Needed:
  - Load 100K, 1M, and 10M vectors into each option
  - Benchmark query latency at P50, P95, P99 under realistic query patterns
  - Test with real documents (measure embedding quality, not just query speed)
  - Estimate cost at current scale, 10x, and 100x

Evaluation Criteria:
  - P99 query latency < 200ms at 10M vectors (go/no-go threshold)
  - Cost per 1M vectors stored < $50/month operational cost
  - Ops overhead < 20 hrs/month (team capacity constraint)

Decision Deadline: End of EPIC-02 (before Build Execution starts)
```

**Why this is a good Research entry:**

- Makes a default decision (pgvector if feasible) while acknowledging uncertainty
- Research scope is specific (3 options, 3 scale points: 100K/1M/10M vectors)
- Evaluation criteria are measurable (200ms P99, cost/vector, ops overhead)
- Decision deadline is tied to a lifecycle milestone (before Build Execution)
- Alternatives are detailed with realistic pros/cons and cost estimates

---

## Anti-Pattern Examples

### Resume-Driven Development (Bad)

```markdown
TECH-001: Backend Framework
Category: Build
Decision: Rust with Actix-web

Rationale: Rust is fast and I want to learn it
```

**Problem**: No evidence Rust is needed; team doesn't know Rust. Cost: weeks of learning curve.

**Better**:

```markdown
Decision: Node.js with Express (or your team's proven stack)
Rationale: Team expertise enables fast iteration. Performance adequate for MVP scale.
  Switch to compiled language only if profiling shows bottleneck.
```

---

### Build Everything (Bad)

```markdown
TECH-001: Authentication - Build custom login system
TECH-002: Payments - Build custom payment processor
TECH-003: Email - Build custom SMTP handler
TECH-004: Analytics - Build custom event tracking
TECH-005: Error tracking - Build custom logger
```

**Problem**: 5+ weeks building commodities instead of differentiators.

**Better**: Buy auth, payments, email, analytics, error tracking. Build your unique features.

---

### No Cost Awareness (Bad)

```markdown
TECH-001: Database
Decision: Enterprise cluster with all bells and whistles
Cost: TBD
```

**Problem**: No cost awareness. TBD costs blow up during implementation.

**Better**:

```markdown
Cost: Standard tier ~$50/mo MVP, scale to Professional tier ($200/mo) when >1K daily writes.
  Projected cost at 10x scale: ~$300-400/mo.
```

---

## Starter Stack Templates

**Note**: These templates show *example* stacks, not prescriptive choices. The total cost should be "affordable for your burn rate," not minimal. Choosing the cheapest tier in each category often forces team burden that slows shipping. During MVP, a $200-300/mo stack with good developer experience is often better than a $50/mo stack that requires constant ops work.

### Template: Simple MVP (<$100/mo infra)

| Layer | Choice | Cost |
| --- | --- | --- |
| Frontend | React or Vue on free tier host | Free |
| Database | Managed PostgreSQL (free tier) | Free-$15/mo |
| Auth | Built-in auth provider (free tier) | Free |
| Payments | Stripe (2.9% + $0.30/tx) | Usage-based |
| Email | Email service (free tier: 100/day) | Free-$25/mo |
| Analytics | Self-hosted or free tier | Free-$25/mo |
| Hosting | Cloud platform free tier | Free |

**Total**: ~$0-50/mo for MVP traffic

---

### Template: Scaling SaaS ($200-500/mo)

| Layer | Choice | Cost |
| --- | --- | --- |
| Frontend | Next.js on paid hosting | $20/mo |
| Database | Managed PostgreSQL (paid tier) | $25-50/mo |
| Auth | Managed auth service | $20-50/mo |
| Payments | Stripe | 2.9% + $0.30/tx |
| Email | Email service (paid) | $20/mo |
| Analytics | Self-hosted or paid tier | $0-50/mo |
| Hosting | Cloud platform paid | $20-50/mo |
| Monitoring/Logging | Error tracking, observability | $20-50/mo |
| Background jobs | Task queue service | $25/mo |

**Total**: ~$200-300/mo base + usage costs
