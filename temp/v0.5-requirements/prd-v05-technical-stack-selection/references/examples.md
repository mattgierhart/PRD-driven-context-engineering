# TECH- Entry Examples

Three filled examples covering the most common decision categories: Reuse, Buy, and Research.

---

## Example 1: Reuse Decision

```
TECH-109: Application Authentication & SSO
Category: Reuse
Layer: Auth
Purpose: Enterprise SSO, user identity, role-based access control

Reuse From: enRoll — Keycloak deployment on IKS
Reuse Scope: Shared instance (separate realm for INTERPRET)
Current State: Keycloak is deployed and operational for enRoll on IBM Cloud
  Kubernetes. Team has existing operational experience. Supports SAML 2.0,
  OIDC, LDAP/AD federation.
Changes Needed: Create dedicated INTERPRET realm. Configure health plan
  IdP federations for INTERPRET customers. Add INTERPRET-specific roles
  (analyst, reviewer, admin).

Shared or Separate: Shared deployment, separate realm

Features Served: FEAT-103 (RBAC for approve/reject), all user-facing features
Risk Constraints: Enterprise customers require SSO

Cost: $0 (already running on IKS)
Integration Complexity: Low (team already operates Keycloak)
Lock-in Risk: Very Low (open-source, self-hosted, Red Hat project)

Product Family Notes: Shared Keycloak enables single sign-on across
  LightStack products if a customer uses both enRoll and INTERPRET.
  Consider if customers should have unified identity across products.
```

**Why this is a good Reuse entry:**
- Documents where the asset comes from and what state it's in
- Explicitly lists what changes are needed (not just "reuse it")
- Addresses shared vs. separate deployment
- Explains the product family implication (cross-product SSO)
- Cost is $0 because it's already running

---

## Example 2: Buy Decision

```
TECH-105: Primary Database
Category: Buy
Layer: Database
Purpose: Rule storage, document metadata, user data, version history, audit trails

Features Served: FEAT-100, FEAT-101, FEAT-102, FEAT-103, FEAT-104,
  FEAT-200, FEAT-201
Risk Constraints: RISK-006 (HIPAA onshore processing)

Decision: IBM Cloud Databases for PostgreSQL
Rationale: IBM-first constraint satisfied. HIPAA-ready with BAA. Dallas TX
  region meets onshore requirement. Standard PostgreSQL — no proprietary
  extensions. Supports pgvector extension for vector search (see TECH-106).
  JSONB handles semi-structured rule and document metadata.

Alternatives Considered:
  - Supabase: Higher developer velocity (auto-generated APIs, auth, real-time)
    but non-IBM, adds external dependency for HIPAA data
  - Self-managed PostgreSQL on IKS: Maximum control, cheapest long-term,
    but significant ops burden for a small team
  - MongoDB on IBM Cloud: Document store fits policy data shape but weaker
    for relational queries (rule → source linking)

Trade-offs:
  - Pro: IBM-first, HIPAA-ready, standard PostgreSQL, supports pgvector
  - Con: Lower developer velocity than Supabase, enterprise pricing

Cost: ~$100-300/month current scale. ~$500-1,500/month at 10x.
Integration Complexity: Low
Lock-in Risk: Low (standard PostgreSQL — portable to any PostgreSQL host)
```

**Why this is a good Buy entry:**
- Rationale explains WHY, not just WHAT (IBM-first + HIPAA + pgvector)
- Alternatives include a genuinely better option (Supabase) with honest rejection reason
- Cost includes both current AND 10x scale
- Lock-in risk is assessed with mitigation (standard PostgreSQL = portable)

---

## Example 3: Research Decision

```
TECH-100: AI Foundation Platform
Category: Buy (constrained) + Research
Layer: AI/ML
Purpose: Foundation model access, fine-tuning, RAG for policy interpretation

Features Served: FEAT-101 (AI Policy Interpretation), FEAT-102 (Citation
  Linking), FEAT-204 (Continuous Learning)
Risk Constraints: RISK-001 (AI accuracy target), RISK-003 (citation fragility),
  RISK-005 (watsonx.ai platform lock-in)

Decision: watsonx.ai as primary with model-agnostic abstraction layer
Rationale: Business constraint (IBM-first). Model Gateway provides multi-model
  access. RISK-005 mitigation requires abstraction layer to enable benchmarking
  against alternatives without architectural rework.

Alternatives Considered:
  - Azure OpenAI: Strong healthcare benchmarks (HealthBench). Consider for
    POC benchmark comparison.
  - Anthropic Claude (via Bedrock): Strong document analysis capabilities.
    Consider for POC benchmark comparison.
  - Direct OpenAI: GPT-4o strong on extraction tasks. Not IBM-aligned.

Trade-offs:
  - Pro: IBM relationship, Granite models, integrated governance ecosystem
  - Con: Healthcare policy accuracy unproven (RISK-001), lock-in without
    abstraction layer (RISK-005)

Cost: Enterprise pricing (existing IBM relationship)
Integration Complexity: Medium (SDK integration + abstraction layer)
Lock-in Risk: High without abstraction layer; Medium with it

Research Needed:
  - Benchmark watsonx.ai vs Azure OpenAI vs Claude on 5-10 real policy documents
  - Measure: rule extraction accuracy, citation quality, cost per document
  - Test fine-tuning ROI on healthcare policy domain

Evaluation Criteria:
  - Rule extraction accuracy >= 85% (go/no-go threshold)
  - Citation accuracy >= 80% at paragraph level
  - Cost per 100-page document < $50

Decision Deadline: After POC (before v0.7 Build Execution)
```

**Why this is a good Research entry:**
- Makes a default decision (watsonx.ai) while acknowledging uncertainty
- Research scope is specific (5-10 real docs, 3 providers, 3 metrics)
- Evaluation criteria are measurable (85% accuracy, $50/doc)
- Decision deadline is tied to a lifecycle milestone (before v0.7)
- Cross-references 3 RISK- entries that drive the research need
