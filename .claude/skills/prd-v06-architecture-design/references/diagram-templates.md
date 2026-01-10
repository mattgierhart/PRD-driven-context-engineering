# Architecture Diagram Templates

## Basic System Diagram (ASCII)

```
┌─────────────────────────────────────────────────────────┐
│                    TRUST BOUNDARY                        │
│                                                          │
│  ┌─────────────┐     ┌─────────────┐    ┌────────────┐  │
│  │  Component  │────▶│  Component  │───▶│  Database  │  │
│  │     A       │     │     B       │    │            │  │
│  └─────────────┘     └─────────────┘    └────────────┘  │
│                                                          │
└──────────────────────────┬───────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
     ┌──────────┐   ┌──────────┐   ┌──────────┐
     │ External │   │ External │   │ External │
     │ Service  │   │ Service  │   │ Service  │
     └──────────┘   └──────────┘   └──────────┘
```

## Data Flow Diagram

```
User Request
     │
     ▼
┌──────────┐    ┌──────────┐    ┌──────────┐
│   CDN    │───▶│  Load    │───▶│   App    │
│  (cache) │    │ Balancer │    │ Server   │
└──────────┘    └──────────┘    └────┬─────┘
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
              ┌──────────┐    ┌──────────┐    ┌──────────┐
              │  Cache   │    │ Database │    │  Queue   │
              │ (Redis)  │    │ (Postgres)│   │ (SQS)   │
              └──────────┘    └──────────┘    └──────────┘
```

## Integration Pattern: Webhook

```
┌─────────────────────────────────────────────────────────┐
│                    External Service                      │
│                    (Stripe, GitHub, etc.)                │
└───────────────────────────┬──────────────────────────────┘
                            │ POST /webhooks/service
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    Webhook Endpoint                      │
│  1. Verify signature                                     │
│  2. Check idempotency key                                │
│  3. Acknowledge (200 OK)                                 │
│  4. Enqueue for processing                               │
└───────────────────────────┬──────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    Event Queue                           │
└───────────────────────────┬──────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    Event Handler                         │
│  1. Parse event type                                     │
│  2. Execute business logic                               │
│  3. Update database                                      │
│  4. Mark as processed                                    │
└─────────────────────────────────────────────────────────┘
```

## Integration Pattern: Circuit Breaker

```
┌─────────────┐     ┌─────────────────────┐     ┌─────────────┐
│  Your Code  │────▶│   Circuit Breaker   │────▶│  External   │
│             │     │                     │     │   Service   │
│             │◀────│  State: CLOSED      │◀────│             │
└─────────────┘     │        OPEN         │     └─────────────┘
                    │        HALF-OPEN    │
                    └──────────┬──────────┘
                               │
                               ▼ (if OPEN)
                    ┌─────────────────────┐
                    │  Fallback Response  │
                    │  - Cached data      │
                    │  - Default value    │
                    │  - Feature disable  │
                    └─────────────────────┘
```

## Module Structure

```
/app
├── /modules
│   ├── /auth           # ARC-003: Authentication module
│   │   ├── actions.ts
│   │   ├── queries.ts
│   │   └── types.ts
│   │
│   ├── /billing        # ARC-004: Billing module
│   │   ├── actions.ts
│   │   ├── webhooks.ts
│   │   └── types.ts
│   │
│   ├── /reports        # Core business logic
│   │   ├── actions.ts
│   │   ├── queries.ts
│   │   └── types.ts
│   │
│   └── /shared         # Cross-cutting concerns
│       ├── db.ts
│       ├── cache.ts
│       └── logger.ts
│
├── /api                # API routes
│   ├── /trpc
│   └── /webhooks
│
└── /components         # React components
```

## Security Boundary Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                     PUBLIC INTERNET                           │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐    │
│  │                   WAF / DDoS Protection               │    │
│  └──────────────────────────┬───────────────────────────┘    │
│                              │                                │
└──────────────────────────────┼────────────────────────────────┘
                               │
┌──────────────────────────────┼────────────────────────────────┐
│                    DMZ (Edge Layer)                           │
│  ┌──────────────────────────┐│                               │
│  │         CDN / Edge       ││                               │
│  │    (Static assets,       ││                               │
│  │     Edge functions)      ││                               │
│  └──────────────────────────┘│                               │
└──────────────────────────────┼────────────────────────────────┘
                               │
┌──────────────────────────────┼────────────────────────────────┐
│                  APPLICATION BOUNDARY                         │
│                              │                                │
│  ┌───────────────────────────▼──────────────────────────────┐│
│  │              Application Server                          ││
│  │   - Auth verification                                    ││
│  │   - Input validation                                     ││
│  │   - Business logic                                       ││
│  └───────────────────────────┬──────────────────────────────┘│
│                              │                                │
└──────────────────────────────┼────────────────────────────────┘
                               │
┌──────────────────────────────┼────────────────────────────────┐
│                    DATA BOUNDARY                              │
│  ┌───────────────────────────▼──────────────────────────────┐│
│  │              Database (Encrypted at rest)                ││
│  │   - Row-level security                                   ││
│  │   - Audit logging                                        ││
│  └──────────────────────────────────────────────────────────┘│
└───────────────────────────────────────────────────────────────┘
```
