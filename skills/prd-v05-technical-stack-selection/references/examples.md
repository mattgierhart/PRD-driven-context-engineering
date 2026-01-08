# Technical Stack Selection Examples

## Example Stack: B2B SaaS Dashboard

**Product**: Analytics dashboard for SMB marketing teams

| Layer | Decision | Category | Rationale |
|-------|----------|----------|-----------|
| Frontend | Next.js 14 | Build | Need SSR for SEO, app router for performance |
| Hosting | Vercel | Buy | Seamless Next.js deployment, edge functions |
| Backend | Next.js API routes + tRPC | Build | Co-located with frontend, type-safe |
| Database | Supabase (Postgres) | Buy | Managed Postgres, auth included, real-time |
| Auth | Supabase Auth | Buy | Integrated with DB, social login included |
| Payments | Stripe | Buy | Industry standard, excellent docs |
| Analytics | PostHog | Buy | Self-hostable, privacy-friendly |
| Error Tracking | Sentry | Buy | Best-in-class, free tier sufficient |
| Email | Resend | Buy | Developer-friendly, React email templates |
| AI/ML | OpenAI API | Buy | GPT-4 for summaries, embeddings |
| DevOps | GitHub Actions | Buy | Integrated with repo, free for public |

**Build decisions (custom code)**:
- Dashboard visualizations (core differentiator)
- Custom report builder (unique to product)
- Marketing data connectors (proprietary logic)

---

## Example: Research Decision

```
TECH-005: Vector Database for Semantic Search
Category: Research
Layer: Database
Purpose: Store and query embeddings for AI-powered document search

Features Served: FEA-025 (semantic search), FEA-026 (similar documents)
Screens Affected: SCR-008 (search), SCR-012 (recommendations)
Risk Constraints: RISK-012 (query latency <200ms)

Decision: TBD after POC

Options to Evaluate:
1. Pinecone
   - Pro: Fully managed, fast setup
   - Con: $70/mo minimum, vendor lock-in

2. Weaviate (self-hosted)
   - Pro: Open source, more control
   - Con: Ops overhead, need to manage scaling

3. pgvector (Postgres extension)
   - Pro: Use existing Postgres, simpler stack
   - Con: May not scale for large vector counts

Research Plan:
- Week 1: Load 100K vectors into each option
- Week 2: Benchmark query latency at P50, P95, P99
- Week 3: Test with 1M vectors (projected scale)

Evaluation Criteria:
- P99 latency < 200ms at 1M vectors
- Cost < $200/mo at current scale
- Acceptable ops burden (max 4 hrs/month)

Decision Deadline: End of Week 3 of EPIC-02
```

---

## Anti-Pattern Examples

### Resume-Driven Development (Bad)

```
TECH-001: Backend Framework
Category: Build
Decision: Rust with Actix-web

Rationale: Rust is fast and I want to learn it
```

**Problem**: No evidence Rust is needed; team doesn't know Rust.

**Better**:
```
Decision: Node.js with Express
Rationale: Team expertise, fast iteration, adequate performance for MVP scale
```

---

### Build Everything (Bad)

```
TECH-001: Authentication - Build custom
TECH-002: Payments - Build custom
TECH-003: Email - Build custom SMTP handler
TECH-004: Analytics - Build custom event tracking
TECH-005: Error tracking - Build custom logger
```

**Problem**: 5+ weeks building commodities instead of differentiators.

**Better**: Buy auth, payments, email, analytics, error tracking. Build your unique features.

---

### No Cost Awareness (Bad)

```
TECH-001: Database
Decision: MongoDB Atlas M30 cluster
Cost: TBD
```

**Problem**: M30 is $500/mo—may not be needed for MVP.

**Better**:
```
Cost: M10 for MVP ($57/mo), upgrade to M30 when >10K daily writes
```

---

## Starter Stack Templates

### Template: Simple MVP (<$50/mo infra)

| Layer | Choice | Cost |
|-------|--------|------|
| Frontend | Next.js on Vercel | Free tier |
| Database | Supabase | Free tier |
| Auth | Supabase Auth | Included |
| Payments | Stripe | 2.9% + $0.30/tx |
| Email | Resend | Free tier (3K/mo) |
| Analytics | PostHog Cloud | Free tier |
| Hosting | Vercel | Free tier |

**Total**: ~$0-20/mo for MVP traffic

---

### Template: Scaling SaaS ($200-500/mo)

| Layer | Choice | Cost |
|-------|--------|------|
| Frontend | Next.js on Vercel Pro | $20/mo |
| Database | Supabase Pro | $25/mo |
| Auth | Clerk Growth | $25/mo |
| Payments | Stripe | 2.9% |
| Email | Resend Pro | $20/mo |
| Analytics | PostHog | $0 (self-host) or $50/mo |
| Hosting | Vercel Pro | $20/mo |
| Monitoring | Sentry | $26/mo |
| Background Jobs | Inngest | $25/mo |

**Total**: ~$200-250/mo base + usage
