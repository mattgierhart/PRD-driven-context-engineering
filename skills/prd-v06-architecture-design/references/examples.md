# Architecture Design Examples

## Example: Complete MVP Architecture

### Context
B2B SaaS dashboard for marketing analytics. Team of 2. MVP target: 100 users.

### Architecture Decisions

```
ARC-001: Monolith with Module Boundaries
Category: Structure
Context: Choosing application structure for MVP
Decision: Single Next.js app with /modules folder structure

Rationale:
  - Small team, single deployment reduces ops burden
  - Domain boundaries unclear until real usage
  - Can extract to services later with evidence

Alternatives Rejected:
  - Microservices: Premature complexity
  - Serverless-first: Cold starts problematic for dashboard

Consequences:
  - Enables: Fast iteration, simple deployment
  - Constrains: Single scaling unit

Related IDs: TECH-001
Status: Accepted
```

```
ARC-002: tRPC for Internal API
Category: Structure
Context: Need type-safe communication between frontend and backend
Decision: Use tRPC with Zod validation

Rationale:
  - End-to-end type safety catches errors at compile time
  - No API client generation needed
  - Works seamlessly with Next.js app router

Alternatives Rejected:
  - REST: Requires manual type definitions
  - GraphQL: Overkill for internal API, adds complexity

Consequences:
  - Enables: Type-safe API calls, great DX
  - Constrains: Not suitable for public API (use REST for that)

Related IDs: TECH-001, TECH-002
Status: Accepted
```

```
ARC-003: Supabase for Auth + Database
Category: Integration
Context: Need managed auth and database with real-time capabilities
Decision: Use Supabase for both auth and primary database

Rationale:
  - Integrated auth reduces complexity
  - Real-time subscriptions for dashboard updates
  - Postgres gives flexibility for analytics queries
  - Row-level security for multi-tenant data

Alternatives Rejected:
  - Separate auth (Clerk) + DB: More moving parts
  - Firebase: Firestore query limitations for analytics

Consequences:
  - Enables: Integrated auth/db, real-time, RLS
  - Constrains: Supabase-specific patterns (RLS policies)

Related IDs: TECH-002, TECH-003, RISK-001
Status: Accepted
```

```
ARC-004: Stripe with Webhook Handler
Category: Integration
Context: Need payment processing with subscription management
Decision: Stripe Checkout + Customer Portal, webhooks for sync

Rationale:
  - Stripe Checkout handles PCI compliance
  - Customer Portal reduces our UI work
  - Webhooks ensure data consistency

Pattern:
  Stripe Webhook → /api/webhooks/stripe → Verify signature → Enqueue → Process

Alternatives Rejected:
  - Build custom checkout: PCI compliance burden
  - Paddle: Less flexible, fewer payment methods

Consequences:
  - Enables: Reliable payments, less custom code
  - Constrains: Must handle webhook idempotency

Related IDs: TECH-004, FEA-020
Status: Accepted
```

### System Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     TRUST BOUNDARY                            │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                    Next.js App                          │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  │  │
│  │  │  Pages   │  │  tRPC    │  │ Modules  │  │ Cron   │  │  │
│  │  │ (React)  │─▶│  Router  │─▶│ /reports │  │ Jobs   │  │  │
│  │  └──────────┘  └──────────┘  │ /data    │  └────────┘  │  │
│  │                              │ /billing │              │  │
│  │                              └──────────┘              │  │
│  └───────────────────────┬────────────────────────────────┘  │
│                          │                                    │
│  ┌───────────────────────▼────────────────────────────────┐  │
│  │                    Supabase                             │  │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐             │  │
│  │   │   Auth   │  │ Postgres │  │ Real-time│             │  │
│  │   └──────────┘  └──────────┘  └──────────┘             │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                               │
└───────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌──────────┐        ┌──────────┐        ┌──────────┐
    │  Stripe  │        │  Resend  │        │ PostHog  │
    │(payments)│        │ (email)  │        │(analytics│
    └──────────┘        └──────────┘        └──────────┘
                  EXTERNAL SERVICES
```

---

## Example: Risk-Driven Architecture Decision

```
ARC-010: Circuit Breaker for External APIs
Category: Performance
Context: RISK-001 identified API dependency outage as high-impact risk
Decision: Implement circuit breaker pattern for all external API calls

Rationale:
  - Prevents cascade failures when external service is down
  - Allows graceful degradation (show cached data, disable features)
  - Fast fail instead of timeout accumulation

Pattern:
  API Call → Circuit Breaker → External Service
       ↓ (if open)
  Fallback Response (cached data or feature disable)

Implementation:
  - Use opossum library for circuit breaker
  - Open circuit after 5 consecutive failures
  - Half-open retry after 30 seconds
  - Log all circuit state changes

Alternatives Rejected:
  - Simple retry: Doesn't prevent cascade failure
  - No protection: Unacceptable given RISK-001 severity

Consequences:
  - Enables: Graceful degradation, faster failure detection
  - Constrains: Must define fallback behavior for each integration

Related IDs: RISK-001, TECH-003, TECH-004
Status: Accepted
```

---

## Anti-Pattern Example: Architecture Astronaut

**Bad:**
```
ARC-001: Kubernetes with Service Mesh
Context: MVP for 100 users
Decision: Deploy on Kubernetes with Istio service mesh

Rationale: We might need to scale
```

**Why it's bad:**
- 100 users doesn't need Kubernetes
- Istio adds massive ops complexity
- "Might need" is not evidence

**Better:**
```
ARC-001: Single Vercel Deployment
Context: MVP for 100 users
Decision: Deploy as single Vercel app

Rationale:
  - Zero ops burden for small team
  - Auto-scaling handles 100-10K users
  - Can migrate to containers when we have evidence of need

Revisit trigger: >10K DAU or complex background job needs
```
