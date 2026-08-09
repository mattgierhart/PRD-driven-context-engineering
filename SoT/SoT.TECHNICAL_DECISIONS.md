---
version: 1.3
purpose: Accepted technical and architecture decisions for this repository and PRD-CE V2.
id_prefix: TECH-XXX, ARC-XXX, ENV-XXX
last_updated: 2026-08-08
authority: Accepted SoT records referenced by PRD.md and repository governance.
---

# Technical Decisions

> **Status:** Active Source of Truth
> **Capability note:** “Accepted” below is the status of the owner-confirmed normative decision.
> V2 runtime implementation and public capability status remain **Proposed**.
> **Lifecycle note:** ARC-001–ARC-004 are Wave 0B governance-bootstrap records at PRD v0.1. They do
> not initialize v0.6 architecture or authorize a v0.7 EPIC.

## Register

| ID | Decision | Decision status | Runtime validation |
|---|---|---|---|
| [ARC-001](#arc-001-markdown-is-the-canonical-accepted-and-recovery-model) | Markdown is the canonical accepted and recovery model | Accepted | Proposed / not implemented |
| [ARC-002](#arc-002-durable-product-memory-survives-v2) | Durable product memory survives V2 | Accepted | Proposed / not implemented |
| [ARC-003](#arc-003-first-executable-value-is-read-only-in-place-inspection) | First executable value is read-only in-place inspection | Accepted | Proposed / not implemented |
| [ARC-004](#arc-004-repository-authority-and-downstream-seeds-are-separate) | Repository authority and downstream seeds are separate | Accepted | Wave 0B packaging implementation; V2 runtime not implemented |

---

## ARC-001: Markdown Is the Canonical Accepted and Recovery Model

- **ID:** ARC-001
- **Category:** Patterns
- **Status:** Accepted (normative decision; V2 implementation Proposed)
- **Decision Date:** 2026-08-08
- **Last Reviewed:** 2026-08-08
- **Decision Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Context

V2 may need search, traversal, validation, and task-scoped context without making a generated system
the competing source of product truth or the only recovery path.

### Decision

Human-reviewable authored Markdown MUST remain the canonical accepted state and recovery model.
Generated databases, indexes, views, and context packages MUST be disposable projections that can be
rebuilt from the accepted Markdown without loss of meaning.

### Rationale

- **Chosen because:** Markdown keeps accepted truth reviewable, diffable, portable, and recoverable.
- **Alternatives considered:** A database or generated graph as primary authority.
- **Trade-off accepted:** Parsers must preserve heterogeneous authored structures and quarantine
  ambiguity rather than silently normalizing it.

### Consequences

Deleting a projection may lose performance or convenience but MUST NOT lose accepted product meaning.
Any future writer requires a separately authorized round-trip and recovery contract.

### Validation state

V2 parser, projection, and recovery behavior are **Proposed and not implemented**. No conformance pass
is claimed at PRD v0.1.

### Evidence and confidence

- **Source Evidence:** [Build plan §2, owner-confirmed boundaries](../docs/PRD_CE_V2_BUILD_PLAN.md#2-owner-confirmed-boundaries)
- **Confidence:** 1/5 — normative owner decision; recovery and round-trip behavior are not yet evidenced.
- **Next Evidence Target:** Wave 2 synthetic compatibility fixtures and deterministic rebuild proofs.

---

## ARC-002: Durable Product Memory Survives V2

- **ID:** ARC-002
- **Category:** Patterns
- **Status:** Accepted (normative decision; V2 implementation Proposed)
- **Decision Date:** 2026-08-08
- **Last Reviewed:** 2026-08-08
- **Decision Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Context

A latest-state summary is insufficient product memory. IDs and statements derive meaning from their
typed relationships, sources, authority, time, lifecycle, and the process records that explain how
accepted state changed.

### Decision

V2 MUST preserve typed IDs, explicit relationships, provenance, temporal meaning, lifecycle state,
and material process history. Unknown or ambiguous structures MUST be surfaced or quarantined, never
silently discarded or promoted.

### Rationale

- **Chosen because:** Durable identity and context make product findings attributable and allow past
  decisions to be reconstructed without confusing them with current truth.
- **Alternatives considered:** Flattened current-state records or inferred-only relationships.
- **Trade-off accepted:** Compatibility work precedes simplified public vocabulary and runtime speed.

### Consequences

Compatibility fixtures must cover IDs, edges, fields, tables, headings, filenames, lifecycle rows,
work sessions, checkpoints, and changelogs before mutation or migration is considered.

### Validation state

Preservation behavior is **Proposed and not implemented**. Private review findings remain provisional
and are not evidence for an accepted conformance verdict.

### Relationships

- **depends-on →** [ARC-001](#arc-001-markdown-is-the-canonical-accepted-and-recovery-model)

### Evidence and confidence

- **Source Evidence:** [Build plan §2 and product scope](../docs/PRD_CE_V2_BUILD_PLAN.md#4-product-scope)
- **Confidence:** 1/5 — normative owner decision; preservation behavior awaits synthetic fixture evidence.
- **Next Evidence Target:** Reviewed fixture coverage with zero silently lost typed IDs or explicit relationships.

---

## ARC-003: First Executable Value Is Read-Only In-Place Inspection

- **ID:** ARC-003
- **Category:** Patterns
- **Status:** Accepted (normative decision; V2 implementation Proposed)
- **Decision Date:** 2026-08-08
- **Last Reviewed:** 2026-08-08
- **Decision Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Context

Migration and accepted-state mutation multiply risk before compatibility, identity, relationship,
provenance, temporal, and repository-divergence behavior is understood.

### Decision

The first V2 executable value MUST inspect an existing PRD-CE repository in place, report
reproducible findings with exact source citations, and leave authored files and Git state unchanged.
It MUST NOT include migration, a writer, Change Set application, adjudication, MCP, hosted services,
V2 runtime/command-provider parity, or root `SoT/` relocation.

### Rationale

- **Chosen because:** Read-only inspection creates user value and compatibility evidence with the
  smallest authority and recovery surface.
- **Alternatives considered:** Migration-first, writer-first, graph-viewer-first, and platform-sized
  initial releases.
- **Trade-off accepted:** Mutation and broader access surfaces wait for separate contracts and gates.

### Consequences

One future alpha contract replaces competing first-release definitions: a compatibility parser,
typed identity/relationship registry, deterministic validator, disposable local projection, and
read-only `index`, `check`, `query`, and `trace` behavior after v0.7 authorization.

### Validation state

The Compatibility Inspector and all V2 commands are **Proposed and not implemented**. Wave 0B adds no
runtime, command, migration behavior, or EPIC.

### Relationships

- **depends-on →** [ARC-001](#arc-001-markdown-is-the-canonical-accepted-and-recovery-model)
- **depends-on →** [ARC-002](#arc-002-durable-product-memory-survives-v2)

### Evidence and confidence

- **Source Evidence:** [Build plan executive direction and Wave 2 contract](../docs/PRD_CE_V2_BUILD_PLAN.md#wave-2--read-only-compatibility-inspector)
- **Confidence:** 1/5 — normative owner decision; no V2 executable behavior exists.
- **Next Evidence Target:** v0.7 authorization followed by non-mutating fixture and Git-state proofs.

---

## ARC-004: Repository Authority and Downstream Seeds Are Separate

- **ID:** ARC-004
- **Category:** Patterns
- **Status:** Accepted (normative decision; V2 runtime Proposed)
- **Decision Date:** 2026-08-08
- **Last Reviewed:** 2026-08-08
- **Decision Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Context

Root `PRD.md` and `SoT/` are required repository authority, but the installer previously reused those
same paths as downstream seeds. Productizing root authority would therefore copy PRD-CE development
records into every new consumer repository.

### Decision

Root `PRD.md` and root `SoT/` MUST remain this repository's product authority. Generic downstream
content MUST live in explicit `PRD_template.md` and `SoT_template/` sources that seed canonical
consumer destinations once. Packaging MUST include the generic sources and MUST exclude root product
authority from the seed bundle.

### Rationale

- **Chosen because:** Separate source paths make authority and redistribution mechanically auditable.
- **Alternatives considered:** Leaving root authority blank, filtering repository entries during
  packaging, or moving root SoT.
- **Trade-off accepted:** Generic templates are intentionally duplicated source artifacts and must be
  protected by parity and leak tests.

### Consequences

The install manifest maps template sources to canonical consumer paths. Direct and plugin-native
installers copy the same deterministic seed bytes, and existing canonical consumer files remain
product-owned.

### Validation state

Wave 0B implements the packaging boundary. The decision remains subject to isolated clean-install,
reinstall, plugin-parity, link-closure, package-sync, and sensitive-reference tests. It does not make
any V2 runtime capability available.

### Relationships

- **driven-by →** [BR-002](SoT.BUSINESS_RULES.md#br-002-reusable-packages-stay-generic-and-non-destructive)

### Evidence and confidence

- **Source Evidence:** [Build plan §3, Wave 0B authority and packaging resolution](../docs/PRD_CE_V2_BUILD_PLAN.md#wave-0b-authority-and-packaging-resolution)
- **Implementation Evidence:** [Wave 0B distribution tests](../tests/test_distribution.py) pass against
  direct installation and the generated plugin payload.
- **Confidence:** 4/5 — owner decision plus passing seed-separation, parity, non-overwrite, link,
  package-sync, and leak proofs; release lifecycle evidence remains outstanding.
- **Next Evidence Target:** CI reproduction plus v0.8 upgrade, rollback, uninstall, and release proofs.

---

## Update protocol

- Never delete accepted decisions; deprecate or supersede them with valid-time fields and a
  replacement link.
- Keep decision status distinct from runtime implementation and public capability status.
- Update evidence, confidence, relationships, and the matching HTML companion in the same change.
- Before v0.7, record new decisions in the current PRD gate change log and accepted SoT snapshot;
  Wave 0B is an owner-authorized bootstrap example. From v0.7 onward, follow the normal EPIC
  Context & IDs protocol.
