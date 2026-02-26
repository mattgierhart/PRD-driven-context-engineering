# Skill Learnings: Technical Stack Selection for LightStack

**Purpose:** Improvements needed for the `prd-v05-technical-stack-selection` skill when used in the LightStack product ecosystem (enGen Interpret, enRoll, VERIFY, and future products).
**Author:** Matt (via workshop session 2026-02-24)
**For:** Simba — to improve this skill for LightStack-specific usage

---

## Problem Summary

The current skill assumes **greenfield** product development. It treats every technology layer as an open decision. In reality, LightStack has:

1. **Existing products** (enRoll) with established technology choices
2. **An IBM-first (not IBM-exclusive) strategic constraint**
3. **Shared infrastructure** across the product family
4. **Operational patterns** the team already knows and runs

The skill needs to account for these realities instead of evaluating every technology layer from scratch.

---

## Required Changes

### 1. Add "Existing Asset Discovery" Phase Before Evaluation

**Current behavior:** The skill jumps straight to "Inventory needs from FEA- and SCR-" and evaluates everything as a new decision.

**Required behavior:** Before evaluating options, the skill should:

1. **Ask about existing products and their tech stack:**
   - "What products already exist in this product family?"
   - "What is the current frontend framework?" (Answer for LightStack: React)
   - "What is the current backend language/framework?"
   - "What authentication system is in place?" (Answer for LightStack: Keycloak)
   - "Where is the product currently hosted?" (Answer for LightStack: IBM Cloud / IKS)
   - "What CI/CD pipeline exists?"
   - "What observability tools are in use?"

2. **Categorize each technology layer as one of:**
   - **Reuse** — existing asset covers this need (e.g., Keycloak for auth)
   - **Extend** — existing asset needs augmentation (e.g., React exists but needs new components)
   - **New** — no existing asset, greenfield decision needed (e.g., document parsing)
   - **Replace** — existing asset doesn't fit the new product's requirements

3. **Only do full evaluation for "New" and "Replace" categories.** For "Reuse" and "Extend", the TECH- entry should document the existing asset and what (if anything) needs to change.

### 2. Add IBM-Specific Product Knowledge

**Current behavior:** The "Common Options" column in the Technology Layers table lists generic SaaS products (React, Vue, Next.js, Vercel, Auth0, Stripe, etc.) that are startup-oriented.

**Required behavior:** For LightStack, the skill should:

1. **Know about IBM's product catalog** and be able to map IBM products to technology layers:
   - AI/ML → watsonx.ai, watsonx.governance
   - Database → IBM Cloud Databases (PostgreSQL, MongoDB, Redis, Elasticsearch)
   - Infrastructure → IBM Cloud Kubernetes Service (IKS), Code Engine (NOT HIPAA-ready!)
   - Secrets → IBM Cloud Secrets Manager
   - Messaging → IBM MQ, IBM Event Streams (Kafka)
   - Integration → Cloud Pak for Integration, App Connect Enterprise
   - Rules → IBM ODM
   - Governance → IBM Knowledge Catalog, watsonx.data
   - B2B → IBM Sterling B2B Integrator

2. **Know HIPAA compliance status of each IBM product** — some are HIPAA-ready (IKS, databases, MQ, Event Streams) and some are NOT (Code Engine). This is critical for healthcare products.

3. **Evaluate IBM products first** for each layer, then consider alternatives only where IBM has gaps or poor fit. The current skill has no IBM awareness at all.

### 3. Add "Product Family Architecture" Consideration

**Current behavior:** The skill treats the product in isolation.

**Required behavior:** For LightStack, tech stack decisions should consider:

1. **Shared vs. separate infrastructure** — Will the new product share a Kubernetes cluster with existing products? Share a database? Share authentication?

2. **Component reuse across products** — Can the new product reuse React components, API patterns, or operational tooling from existing products?

3. **Cross-product user experience** — If a customer uses multiple LightStack products, should they have single sign-on? Consistent UI? Unified dashboards?

4. **The TECH- template should include a "Reuse From" field:**

```
TECH-XXX: [Technology/Capability Name]
Category: [Build | Buy | Integrate | Research | Reuse]  ← Add "Reuse" category
Layer: [...]
Purpose: [...]
Reuse From: [existing product/asset name, e.g., "enRoll — Keycloak deployment"]
Reuse Scope: [Full reuse | Extend | Shared instance | Pattern only]
```

### 4. Add "IBM-First Constraint" to Decision Framework

**Current behavior:** The Build vs. Buy framework doesn't account for strategic vendor constraints.

**Required behavior:** Add a new row to the Build vs. Buy Decision Framework:

| Factor | Favors Build | Favors Buy (IBM) | Favors Buy (Non-IBM) |
|--------|-------------|-------------------|---------------------|
| **Strategic alignment** | Core differentiator | IBM has a product for this | IBM has nothing, or IBM product is poor fit |
| **HIPAA compliance** | — | IBM product is HIPAA-ready | Non-IBM product has HIPAA BAA |
| **Existing asset** | — | IBM product already in use | Non-IBM already in use (e.g., Keycloak) |

The skill should default to this evaluation order:
1. Can we reuse an existing asset?
2. Does IBM have a product that fits?
3. If IBM has nothing or poor fit, what non-IBM options exist?
4. Do we need to build custom?

### 5. Replace Generic Examples with LightStack-Relevant Ones

**Current behavior:** Examples reference Clerk, Supabase, Vercel, Stripe — SaaS startup tools.

**Required behavior:** Examples should reference:
- IBM Cloud services (IKS, Cloud Databases, watsonx.ai)
- Open-source tools deployed on IBM Cloud (Keycloak, PostHog, Docling)
- Healthcare-specific constraints (HIPAA, BAA, onshore processing, PHI handling)
- Enterprise auth patterns (SAML, OIDC, LDAP — not social login)

### 6. Add Healthcare / Regulated Industry Layer

**Current behavior:** Technology layers don't include compliance or healthcare-specific layers.

**Required behavior:** Add these layers to the Technology Layers table:

| Layer | Questions to Answer | LightStack Default |
|-------|---------------------|-------------------|
| **Compliance** | HIPAA, BAA, data residency, PHI classification? | IBM Cloud (Dallas, TX), HIPAA BAA |
| **Document Processing** | Parse complex documents (PDF, Word, tables)? | Docling (IBM Research) |
| **AI Governance** | Model monitoring, bias detection, audit trail? | watsonx.governance (post-MVP) |
| **Business Rules** | Rule management, execution, testing? | IBM ODM (when needed) or custom |

### 7. Add "Existing Asset" TECH- Template Variant

For reuse decisions, the full TECH- template is overkill. Add a lighter variant:

```
TECH-XXX: [Technology/Capability Name]
Category: Reuse
Layer: [...]
Purpose: [...]

Reuse From: [product name — e.g., "enRoll"]
Current State: [What exists today]
Changes Needed: [What INTERPRET needs that doesn't exist yet]
Shared or Separate: [Shared deployment or separate instance]

Features Served: [FEA-XXX, FEA-YYY]
Risk Constraints: [RISK-XXX if any]

Cost: [Incremental cost, likely $0 for reuse]
Integration Complexity: [Low | Medium | High]
Lock-in Risk: [Already committed — this is sunk]
```

---

## Summary of What Changed During the Workshop

| Skill Assumption | Reality | Impact |
|-----------------|---------|--------|
| Frontend is a greenfield decision | Team is already on React (from enRoll) | Eliminated framework evaluation; focused on component reuse |
| Backend is a framework choice | It's an architecture decision (polyglot vs. Python-first vs. hybrid) | Changed from "pick a framework" to "3 architecture options for workshop" |
| Hosting is a vendor selection (Vercel, AWS, Cloudflare) | Everything runs on IBM Cloud IKS already | Eliminated hosting section entirely; it's just IKS |
| Auth is a vendor selection (Auth0, Cognito, Clerk) | Keycloak is already deployed and operational | Changed from "buy Auth0" to "continue with Keycloak" + when to consider Auth0 at scale |
| Every technology layer is open | 4 of 8 "gap" areas were already solved by enRoll assets | Reduced greenfield decisions from 8 to 4 |

---

## Suggested Skill Workflow (Revised)

1. **Discover existing assets** — Ask about current products, tech stack, infrastructure
2. **Categorize layers** — Reuse / Extend / New / Replace for each technology layer
3. **Evaluate IBM fit** — For "New" layers, check IBM products first
4. **Evaluate alternatives** — For gaps, research non-IBM options
5. **Consider product family** — Shared infrastructure, component reuse, cross-product UX
6. **Create TECH- entries** — Using appropriate template (standard or reuse variant)
7. **Map to risks** — Cross-reference every TECH- entry with RISK- constraints
