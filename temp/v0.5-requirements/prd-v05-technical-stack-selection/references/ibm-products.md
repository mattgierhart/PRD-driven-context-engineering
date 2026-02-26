# IBM Product Catalog for Technology Selection

Load this reference when the team has an IBM-first (or IBM-only) vendor constraint.

## IBM Products by Capability Area

| Capability | IBM Product | HIPAA-Ready | Fit for MVP | Notes |
|-----------|-------------|-------------|-------------|-------|
| **AI/ML — Foundation Models** | watsonx.ai | Yes | Yes | Granite models, RAG, fine-tuning, Model Gateway for multi-model |
| **AI/ML — Governance** | watsonx.governance | Yes | Post-MVP | Model monitoring, bias detection, EU AI Act compliance |
| **AI/ML — Data** | watsonx.data | Yes | Post-MVP | Lakehouse for training data management |
| **Kubernetes** | IBM Cloud Kubernetes Service (IKS) | Yes (HITRUST) | Yes | Managed K8s, Dallas TX region, FedRAMP |
| **Serverless** | IBM Cloud Code Engine | **NO** | **Disqualified** | Not HIPAA-ready — cannot use for PHI-adjacent workloads |
| **Database — PostgreSQL** | IBM Cloud Databases for PostgreSQL | Yes | Yes | Managed, supports pgvector extension |
| **Database — MongoDB** | IBM Cloud Databases for MongoDB | Yes | Maybe | Document store, good for unstructured policy data |
| **Cache — Redis** | IBM Cloud Databases for Redis | Yes | Yes | Session cache, rate limiting, Celery broker |
| **Search — Elasticsearch** | IBM Cloud Databases for Elasticsearch | Yes | Yes | Full-text search across policies and rules |
| **Secrets** | IBM Cloud Secrets Manager | Yes | Yes | Single-tenant HashiCorp Vault, ~$299/mo + $0.20/secret |
| **Messaging — MQ** | IBM MQ | Yes | Over-provisioned | Enterprise message queue, $thousands/mo. Consider for scale, not MVP. |
| **Messaging — Kafka** | IBM Event Streams | Yes | Over-provisioned | Managed Kafka. Consider for event sourcing or audit trail. |
| **Integration** | Cloud Pak for Integration | Yes | Premature | Enterprise integration platform. Only at multi-system scale. |
| **Rules Engine** | IBM Operational Decision Manager (ODM) | Yes | Premature | BRMS with testing/simulation. $50K-200K/yr. For rule execution, not generation. |
| **Data Governance** | IBM Knowledge Catalog | Yes | Post-MVP | Data lineage, quality. Relevant at 10+ customer scale. |
| **B2B Integration** | IBM Sterling B2B Integrator | Yes | Premature | EDI, supply chain. Only if healthcare EDI transactions needed. |
| **Monitoring** | IBM Cloud Monitoring (Sysdig) | Yes | Adequate | Infrastructure monitoring. Functional but less dev-friendly than Sentry. |
| **APM** | IBM Instana | Yes | Post-MVP | Application performance monitoring. Production-scale observability. |
| **CI/CD** | IBM Cloud Toolchains | N/A | Adequate | Functional but less developer-friendly than GitHub Actions. |

## Evaluation Order

When using this catalog:

1. **Check HIPAA status first.** If the capability handles PHI or PHI-adjacent data, only HIPAA-ready products qualify.
2. **Check MVP fit.** Products marked "Post-MVP", "Over-provisioned", or "Premature" should not be chosen for initial build — document as "Phase 2+" in the TECH- entry.
3. **Evaluate fit honestly.** IBM-first means IBM gets evaluated first, not that IBM always wins. If IBM's product is poor fit, document why and evaluate alternatives.

## Common IBM Gaps

These capability areas have no strong IBM product or IBM's product is poor fit for typical MVPs:

| Capability | IBM Gap | Typical Non-IBM Choice |
|-----------|---------|----------------------|
| Document parsing | No parsing service | Docling (IBM Research, open-source) or Unstructured.io |
| Vector database | No dedicated vector DB | pgvector (on IBM PostgreSQL) or Weaviate |
| Lightweight task queue | MQ/Event Streams over-provisioned | Celery + Redis |
| Product analytics | No self-hosted analytics | PostHog (self-hosted on IKS) |
| Error tracking (dev) | Instana is enterprise-scale | Sentry |
| Frontend framework | No frontend product | React, Vue, Angular (open-source) |
| Design system | IBM Carbon Design System | Carbon is React-native, open-source |

## Phase 2+ IBM Products

These become relevant as the product scales. Create TECH- entries with Category: Research and note when to revisit.

| Product | Trigger to Revisit | Phase |
|---------|-------------------|-------|
| watsonx.governance | First enterprise customer compliance review | Phase 2 |
| IBM ODM | Pilot customer requests rule execution or ODM-format output | Phase 2 |
| IBM Knowledge Catalog | 10+ customers with cross-customer data concerns | Phase 3 |
| IBM MQ | Audit requirements extend to pipeline-level guaranteed delivery | Phase 2 |
| IBM Event Streams | Event sourcing needed for full processing audit trail | Phase 2 |
| Cloud Pak for Integration | Customer requires HL7/FHIR or SAP integration | Phase 3 |
| IBM Instana | Production observability at scale beyond Sentry | Phase 2 |
