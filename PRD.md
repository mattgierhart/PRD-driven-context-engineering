---
version: 0.1
methodology_generation: 2
purpose: Product authority for PRD-Led Context Engineering V2.
last_updated: 2026-08-12
runtime_status: Proposed
---

# PRD-Led Context Engineering V2 · Product Requirements Document

> **Working public name:** “The Product Model” is a working name only. It is not an approved public
> product name, category, or release claim.
>
> **Current truth:** this repository is at PRD gate **v0.1 Spark** for V2. Wave 0B establishes
> product authority and clean packaging; it does not implement or release a V2 runtime.

## Authority and status

**Read order:** `CLAUDE.md` → `README.md` → `PRD.md` → accepted `SoT/` → active EPIC (v0.7+ only).
`CLAUDE.md` governs agent behavior; product-truth precedence starts with this PRD.

1. [`CLAUDE.md`](CLAUDE.md) — operating instructions and documentation discipline; not product fact authority.
2. [`README.md`](README.md) — repository orientation and current status.
3. `PRD.md` — this file; product strategy and lifecycle authorization.
4. Accepted records in [`SoT/`](SoT/SoT.README.md) — durable rules and decisions.
5. EPICs — approved execution records created only at v0.7 or later.
6. [`docs/PRD_CE_V2_BUILD_PLAN.md`](docs/PRD_CE_V2_BUILD_PLAN.md) — contingent sequencing,
   subordinate to this PRD and accepted SoT records.
7. Research and evaluation artifacts — inputs only until their evidence is durable, reviewable,
   sanitized, and accepted.

| Field | Current value |
|---|---|
| PRD lifecycle gate | v0.1 Spark |
| Lifecycle status | Discovery |
| V2 runtime status | Proposed; no V2 executable behavior exists |
| V2 public availability | Proposed; not a release or installable V2 capability |
| Branch status | Isolated pending explicit release-candidate and merge approval |
| Next target gate | v0.2, only after the v0.1 gate is approved |
| Related EPIC | None; EPIC creation is prohibited before v0.7 |
| Accepted SoT snapshot | BR-001–BR-005; ARC-001–ARC-004 |
| Accepted empirical evidence | None; private review findings remain provisional planning inputs |

## Version vocabulary

These dimensions answer different questions and must never be substituted for one another.

| Dimension | Meaning | Current V2 value |
|---|---|---|
| Methodology generation | Product-model evolution umbrella | V2 |
| PRD lifecycle gate | Evidence and authorization maturity | v0.1 Spark |
| Runtime release and status | Version and truth state of executable V2 behavior | No V2 release; Proposed |
| Downstream template version | Version of the generic install/fork scaffold | 3.3.0 |
| Provider package version | Provider-specific distribution release | Not assigned for V2; must be versioned independently |

## Lifecycle change log

| PRD gate | Date | Summary | Linked records |
|---|---|---|---|
| v0.1 Spark | 2026-08-08 | Initialized V2 product authority, scope, non-goals, open questions, and repository/template separation | BR-001–BR-005; ARC-001–ARC-004 |
| v0.1 Spark | 2026-08-12 | Owner resolved open decision 5 (publish history as-is); established `prd-ce-v2` as the V2 maturation branch and pushed it to origin | Open decision 5 |

No later lifecycle gate has been initialized.

---

## v0.1 Spark — Problem and outcomes

### Spark summary

PRD-Led Context Engineering V2 is a Product Management methodology and proposed local product
system for preserving what teams learned, decided, delivered, and observed. Its purpose is to let
each human or AI participant act from current, attributable context without flattening uncertainty,
erasing history, or silently replacing accepted product truth.

The first executable value, after the required lifecycle gates authorize implementation, is a
read-only inspection of an existing PRD-CE repository in place. It should reveal identity,
relationship, provenance, lifecycle, temporal, and local repository-divergence problems with exact
source citations and without changing authored files.

### Problem statement

- **Who is affected?** Product teams working across repeated human and AI sessions. The primary v0.2
  audience remains an owner decision.
- **What pain exists?** Product evidence, intent, delivery, reality, and learning drift across files,
  sessions, branches, and actors. Current meaning becomes hard to locate, provenance is lost, and
  inferred context can be mistaken for accepted truth.
- **Why now?** PRD-CE already provides a Markdown lifecycle and typed knowledge graph, but V2 planning
  must first place its own product definition inside the repository authority chain while keeping
  reusable downstream scaffolds generic and non-destructive.

### Product promise

Help product teams preserve what they learned, decided, delivered, and observed so each human or AI
agent can act from current, attributable context without erasing history.

### Desired outcomes

1. Preserve canonical product memory in human-reviewable Markdown across sessions, tools, branches,
   and future projections.
2. Keep typed IDs, explicit relationships, provenance, temporal meaning, lifecycle state, and process
   history intact rather than reducing them to a latest-state summary.
3. Let a Product Management user inspect an existing repository and reach reproducible findings with
   exact file/record evidence before any accepted-state mutation is possible.
4. Keep repository-specific PRD-CE decisions separate from generic downstream templates and prove
   clean installation plus non-destructive reinstallation.
5. Advance through one Progressive PRD lifecycle, with no implementation work before the v0.7 gate.

### Initial success signals

These are validation targets, not achieved runtime claims:

- Clean direct and plugin-native scaffolds receive the same generic PRD and SoT seeds, the smallest
  closed consumer-doc set, and no repository-maintainer or named downstream material.
- Reinstallation preserves consumer-owned `README.md`, `PRD.md`, `SoT/`, EPICs, and agent memory.
- A future read-only compatibility fixture demonstrates zero silently lost typed IDs or explicit
  relationships and leaves authored files and Git state unchanged.
- Future findings cite exact source locations and distinguish accepted, proposed, inferred,
  ambiguous, stale, deprecated, superseded, and unknown states.

### Product Management scope

V2 serves the **Product Management lifecycle only** ([BR-001](SoT/SoT.BUSINESS_RULES.md#br-001-product-management-is-the-sole-v2-lifecycle)). In scope at the product-definition level:

- discovery evidence, uncertainty, assumptions, decisions, outcomes, and business rules;
- personas, journeys, requirements, and experience intent;
- delivery plans, architecture, code/test traceability, releases, and operational reality when they
  inform product decisions;
- customer and operational learning that challenges current intent;
- current, proposed, rejected, stale, deprecated, and superseded meaning;
- task-scoped context with exact provenance;
- new-project initialization and non-destructive brownfield adoption;
- human-reviewed change proposals only after the read-only foundation is proven and separately
  authorized.

Possible future methodologies are separate products and method packs with their own governance.
They do not broaden V2 scope or justify speculative abstractions now.

### Durable product-memory contract

- Markdown is the canonical accepted state and recovery model; databases, views, indexes, and context
  packages are disposable projections ([ARC-001](SoT/SoT.TECHNICAL_DECISIONS.md#arc-001-markdown-is-the-canonical-accepted-and-recovery-model)).
- Durable identity, relationships, provenance, time, and process history must survive V2
  ([ARC-002](SoT/SoT.TECHNICAL_DECISIONS.md#arc-002-durable-product-memory-survives-v2)).
- The first executable contract is read-only, in-place inspection
  ([ARC-003](SoT/SoT.TECHNICAL_DECISIONS.md#arc-003-first-executable-value-is-read-only-in-place-inspection)).
- Repository authority and downstream seeds are separate
  ([ARC-004](SoT/SoT.TECHNICAL_DECISIONS.md#arc-004-repository-authority-and-downstream-seeds-are-separate)).

### Governance rules

- Reusable packages must remain generic and non-destructive
  ([BR-002](SoT/SoT.BUSINESS_RULES.md#br-002-reusable-packages-stay-generic-and-non-destructive)).
- V2 remains Proposed and branch-isolated until explicit approval
  ([BR-003](SoT/SoT.BUSINESS_RULES.md#br-003-v2-remains-proposed-and-branch-isolated)).
- Implementation EPICs begin only at v0.7
  ([BR-004](SoT/SoT.BUSINESS_RULES.md#br-004-implementation-epics-begin-only-at-v07)).
- Version dimensions remain distinct
  ([BR-005](SoT/SoT.BUSINESS_RULES.md#br-005-version-dimensions-remain-distinct)).

### Explicit non-goals at v0.1

- Implementing the Compatibility Inspector or any other V2 runtime.
- Moving or normalizing root `SoT/`.
- Building a migration engine, accepted-state writer, Change Set application/adjudication path, or
  silent promotion of inferred knowledge.
- Building an MCP server, hosted service, cloud graph, marketplace requirement, portfolio dashboard,
  generic node canvas, or GearHeartAI site.
- V2 runtime/command-provider parity, public performance claims, automatic strategic decisions, adjacent business
  methodologies, or a universal enterprise ontology.
- Publishing this branch before a separate history-sanitization decision and release-candidate gate.

### Empirical evidence state

No empirical evidence record is accepted at v0.1. The private review findings that shaped the
contingent build plan remain provisional, are not copied into SoT, and do not validate the problem,
audience, or a V2 runtime. Before advancing to v0.2, the owner must accept durable, reviewable
evidence records for the problem and initial Product Management audience or explicitly hold the gate.
The owner-confirmed BR/ARC records above are normative decisions, not substitutes for user evidence.

### Open owner decisions and target boundaries

The following are deliberately unresolved:

1. Approve, reject, or replace “The Product Model” as the public name before its v0.3 category and
   packaging gate or any public use.
2. Choose the canonical user-facing term for Build versus Deliver before that term gates execution
   or public lifecycle copy; the owner has not assigned an earlier gate.
3. Select the primary v0.2 Product Management audience, segment, and “not for” boundary; this is a
   v0.1 → v0.2 gate decision supported by accepted evidence.
4. Decide when website proof may move from planning to public evidence before any website
   implementation or publication; it is not a v0.2 gate by default.
5. ~~Choose a history-sanitization strategy for the ancestor commit that exposed named private
   evaluation targets before any push or public review; it is not a product-discovery gate.~~
   **Resolved 2026-08-12 (owner decision):** publish the branch with unmodified history. The
   exposure — private evaluation-target names (PetPass, Koisk-Browser) and local filesystem paths
   in the ancestor commit's evaluation prompt (`84e040f`) — is accepted; no sanitization will
   occur. The v2 maturation branch is `prd-ce-v2`, pushed to the public origin; it remains
   branch-isolated per BR-003 until a separate merge decision.

No other answer is inferred by this PRD.

### v0.1 gate condition

Wave 0B may close repository authority and packaging mechanics, but advancing to v0.2 still requires
owner review of this Spark, its outcomes, its accepted SoT records, accepted initial evidence, and
the primary-audience boundary. Deferred naming, lifecycle-copy, website-proof, and history decisions
remain open at the boundaries stated above; they do not silently become v0.2 blockers.
No V2 runtime work is authorized by this document at v0.1.

---

## Later gates — not initialized

v0.2 through v1.0 remain governed by the Progressive PRD lifecycle and the contingent build plan.
They contain no accepted product definition here yet. In particular, no EPIC exists and none may be
created before v0.7.
