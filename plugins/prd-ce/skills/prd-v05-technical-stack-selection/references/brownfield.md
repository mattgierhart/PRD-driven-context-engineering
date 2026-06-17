# Brownfield Discovery Workflow

Load this reference when the user confirms that existing products share infrastructure with the new product being evaluated.

## Purpose

When a product family already exists, many technology decisions are pre-made. This workflow helps discover those existing assets before evaluating new options — preventing the anti-pattern of re-evaluating settled decisions.

## Discovery Interview

Ask these questions in order. Record answers in the discovery summary table.

### 1. Product Family Overview

- "What products currently exist in this family?"
- "Which products share infrastructure (clusters, databases, services)?"
- "Is there a shared component library or design system?"
- "Who operates the current infrastructure? Same team or different?"

### 2. Per-Area Asset Discovery

For each area, ask what exists and its current state:

| Area | Discovery Questions |
|------|-------------------|
| **Frontend** | What framework? What design system? Shared component library? Hosting? |
| **Backend** | What language/framework? Monolith or microservices? API patterns? |
| **Database** | What database(s)? Managed or self-hosted? Shared or per-product? |
| **Auth** | What auth system? SSO? Identity provider federation? |
| **Infrastructure** | What cloud? What orchestration (K8s, serverless)? What region? |
| **CI/CD** | What pipeline? Shared or per-repo? What's automated? |
| **Monitoring** | What observability? Error tracking? Alerting? |
| **Messaging** | Any queue or event system? What patterns? |

### 3. Constraint Discovery

- "Are there vendor constraints (e.g., must use IBM, AWS, Azure)?"
- "Are there compliance requirements (HIPAA, SOC2, FedRAMP)?"
- "Are there team skill constraints (only know Python, only know React)?"
- "Are there cost constraints (budget ceiling for new services)?"

## Categorization Framework

After discovery, categorize each capability area:

| Category | Criteria | Example |
|----------|----------|---------|
| **Reuse** | Existing asset covers the new product's need as-is | "Our auth service handles auth for Product-A. Product-B needs the same auth patterns." |
| **Extend** | Existing asset works but needs additions | "React exists but needs new domain-specific components for Product-B workflows." |
| **New** | No existing asset for this capability | "No document processing service exists in the family." |
| **Replace** | Existing asset is wrong for the new product | "Current queue doesn't support the real-time processing Product-B needs." |

## Output Format

Create a summary table:

| Capability Area | Existing Asset | Source Product | Category | Notes |
|----------------|---------------|---------------|----------|-------|
| Frontend | React + Carbon Design | Product-A | Extend | Need new workflow-specific components |
| Auth | OAuth 2.0 provider | Product-A | Reuse | Separate realm/tenant for Product-B |
| Database | PostgreSQL on Cloud | Product-A | Reuse | May need additional schemas |
| Document processing | None | — | New | Greenfield evaluation needed |
| Batch processing | None | — | New | Pipeline orchestration needed |
| Task queue | None | — | New | Async job handling needed |

## Key Principle

**Discover before evaluating.** The most expensive mistake in brownfield contexts is re-evaluating technology that's already deployed, operational, and working. If the existing asset covers 80% of the need, extend it — don't replace it with something marginally better.

The exception: if the existing asset is fundamentally wrong for the new product's requirements (different scale, different compliance, different performance profile), then Replace is the correct categorization. But justify the replacement explicitly.
