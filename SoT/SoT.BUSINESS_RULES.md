---
version: 1.1
purpose: Accepted business rules and operational constraints for this repository and PRD-CE V2.
id_prefix: BR-XXX
last_updated: 2026-08-08
authority: Accepted SoT records referenced by PRD.md and repository governance.
---

# Business Rules

> **Status:** Active Source of Truth
> **Lifecycle note:** BR-001–BR-005 are owner-authorized Wave 0B governance-bootstrap records at
> PRD v0.1. They establish constraints; they do not advance the product to v0.2 or create an EPIC.

## Register

| ID | Rule | Severity | Status |
|---|---|---|---|
| [BR-001](#br-001-product-management-is-the-sole-v2-lifecycle) | Product Management is the sole V2 lifecycle | Critical | Active |
| [BR-002](#br-002-reusable-packages-stay-generic-and-non-destructive) | Reusable packages stay generic and non-destructive | Critical | Active |
| [BR-003](#br-003-v2-remains-proposed-and-branch-isolated) | V2 remains Proposed and branch-isolated | Critical | Active |
| [BR-004](#br-004-implementation-epics-begin-only-at-v07) | Implementation EPICs begin only at v0.7 | Critical | Active |
| [BR-005](#br-005-version-dimensions-remain-distinct) | Version dimensions remain distinct | High | Active |

---

## BR-001: Product Management Is the Sole V2 Lifecycle

- **ID:** BR-001
- **Category:** Methodology Governance
- **Status:** Active
- **Severity:** Critical
- **Created:** 2026-08-08
- **Reviewed:** 2026-08-08
- **Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Rule

PRD-CE V2 MUST serve the Product Management lifecycle only. GearHeartAI planning MAY present that
path, but adjacent methodologies MUST remain separately governed products or method packs and MUST
NOT broaden V2 scope or drive speculative abstractions.

### Rationale

A single lifecycle keeps the product promise, vocabulary, validation, and first user experience
coherent. Reuse is permitted only after a primitive is proven and without adding concepts Product
Management users must learn.

### Enforcement

- **Location:** Root PRD scope, lifecycle gates, reusable artifacts, and public claims.
- **Timing:** Every scope decision, gate review, package change, and release review.
- **Owner action:** Reject or separately govern adjacent-methodology work.

### Failure disposition

- **Gate code:** `V2_SCOPE_EXPANSION`
- **Disposition:** Block lifecycle advancement or release evidence until the expansion is removed or
  approved under a separate product authority.

### Relationships

No typed-ID dependency is asserted; this rule directly constrains the root PRD.

### Evidence and confidence

- **Source Evidence:** [Build plan §2, owner-confirmed boundaries](../docs/PRD_CE_V2_BUILD_PLAN.md#2-owner-confirmed-boundaries)
- **Confidence:** 1/5 — normative owner decision; market and runtime evidence are not yet established.
- **Next Evidence Target:** v0.2 audience research and owner approval of the Product Management segment.

---

## BR-002: Reusable Packages Stay Generic and Non-Destructive

- **ID:** BR-002
- **Category:** Patterns
- **Status:** Active
- **Severity:** Critical
- **Created:** 2026-08-08
- **Reviewed:** 2026-08-08
- **Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Rule

Tracked reusable artifacts and generated packages MUST remain generic, MUST exclude named downstream
products, client facts, machine-specific target paths, private evaluation details, and repository
maintainer records, and MUST NOT overwrite consumer-owned product content on reinstall.

### Rationale

This repository is both a methodology source and a redistribution source. Product-specific authority
inside reusable seeds creates false downstream truth; directory-wide replacement can destroy valid
consumer work.

### Enforcement

- **Location:** Install manifest, direct installer, plugin initializer, packager, and distribution tests.
- **Timing:** Every package build, clean install, reinstall, and provider release.
- **Protected destinations:** `README.md`, `PRD.md`, `SoT/`, `EPIC-*.md`, agent memory,
  `.claude/domain-profile.yaml`, and unrelated consumer additions inside framework directories.

### Failure disposition

- **Gate code:** `DISTRIBUTION_LEAK_OR_OVERWRITE`
- **Disposition:** Block packaging and release until the leak or destructive behavior is removed and
  the isolated install proof passes.

### Evidence and confidence

- **Source Evidence:** [Build plan §2 and §3](../docs/PRD_CE_V2_BUILD_PLAN.md#3-status-and-authority)
- **Implementation Evidence:** [Wave 0B distribution tests](../tests/test_distribution.py) cover clean
  install, forced reinstall, plugin parity, link closure, package completeness, and sensitive references.
- **Confidence:** 4/5 — owner decision plus passing isolated distribution proofs; public release and
  long-term upgrade evidence remain outstanding.
- **Next Evidence Target:** CI reproduction plus v0.8 upgrade, rollback, uninstall, and release proofs.

---

## BR-003: V2 Remains Proposed and Branch-Isolated

- **ID:** BR-003
- **Category:** Methodology Governance
- **Status:** Active
- **Severity:** Critical
- **Created:** 2026-08-08
- **Reviewed:** 2026-08-08
- **Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Rule

V2 runtime and public capability status MUST remain `Proposed`, and V2 work MUST remain on its branch,
until executable evidence supports a release candidate and the owner makes an explicit merge and
publication decision.

### Rationale

Committed plans are not executable behavior. Branch isolation prevents design claims from being
mistaken for a stable release and leaves historical publication risk subject to explicit review.

### Enforcement

- **Location:** README, PRD, build plan, site claims, branch/release workflow, and provider metadata.
- **Timing:** Every status report, capability claim, merge proposal, and publication action.

### Failure disposition

- **Gate code:** `UNPROVEN_V2_RELEASE_CLAIM`
- **Disposition:** Revert the claim to Proposed and block merge/publication until the evidence package
  and owner approval exist.

### Relationships

- **depends-on →** [BR-005](#br-005-version-dimensions-remain-distinct)

### Evidence and confidence

- **Source Evidence:** [Build plan §2, owner-confirmed boundaries](../docs/PRD_CE_V2_BUILD_PLAN.md#2-owner-confirmed-boundaries)
- **Confidence:** 1/5 — normative owner decision; no V2 runtime or release-candidate evidence exists.
- **Next Evidence Target:** A separately authorized release-candidate evidence package and merge decision.

---

## BR-004: Implementation EPICs Begin Only at v0.7

- **ID:** BR-004
- **Category:** Methodology Governance
- **Status:** Active
- **Severity:** Critical
- **Created:** 2026-08-08
- **Reviewed:** 2026-08-08
- **Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Rule

No V2 implementation EPIC MAY be created before the Progressive PRD reaches and receives approval
at v0.7. Pre-v0.7 work MUST be limited to authorized product definition, governance, evidence,
compatibility research, and disposable architecture experiments.

### Rationale

The Progressive PRD is the sole authorization system. Creating implementation work packages early
would let a delivery sequence bypass unresolved product, market, risk, and architecture gates.

### Enforcement

- **Location:** `epics/`, PRD lifecycle review, and build-plan wave authorization.
- **Timing:** Before any V2 implementation task or EPIC file is created.

### Failure disposition

- **Gate code:** `PREMATURE_V2_EPIC`
- **Disposition:** Stop implementation and remove the unapproved work package through an explicitly
  reviewed change; do not treat it as product authority.

### Relationships

- **depends-on →** [BR-003](#br-003-v2-remains-proposed-and-branch-isolated)

### Evidence and confidence

- **Source Evidence:** [Build plan §2 and authorization matrix](../docs/PRD_CE_V2_BUILD_PLAN.md#7-progressive-prd-authorization-matrix)
- **Confidence:** 1/5 — normative owner decision; lifecycle outcomes remain to be evidenced.
- **Next Evidence Target:** Owner-approved v0.7 gate with bounded implementation scope.

---

## BR-005: Version Dimensions Remain Distinct

- **ID:** BR-005
- **Category:** Methodology Governance
- **Status:** Active
- **Severity:** High
- **Created:** 2026-08-08
- **Reviewed:** 2026-08-08
- **Authority:** Owner-confirmed
- **Lifecycle Origin:** Wave 0B governance bootstrap
- **Valid From:** PRD v0.1
- **Valid To:** —
- **Invalidated By:** —

### Rule

Methodology generation, Progressive PRD gate, executable runtime release/status, downstream template
version, and provider package version MUST be named and reported as separate dimensions. A change or
approval in one dimension MUST NOT imply a change or approval in another.

### Rationale

Using “V2” for strategy, maturity, executable release, scaffold version, and provider package state
would turn a truthful planning label into an unsupported runtime or availability claim.

### Enforcement

- **Location:** PRD metadata, README status, template frontmatter, provider manifests, release notes,
  and website claims.
- **Timing:** Every gate transition, package version change, capability claim, and release decision.

### Failure disposition

- **Gate code:** `VERSION_DIMENSION_CONFLATION`
- **Disposition:** Block the status or release update until every dimension is stated independently.

### Evidence and confidence

- **Source Evidence:** [Build plan Wave 0B](../docs/PRD_CE_V2_BUILD_PLAN.md#wave-0b--owner-approved-governance-bootstrap)
- **Confidence:** 1/5 — normative owner decision; consistent use across future releases is not yet evidenced.
- **Next Evidence Target:** Release and provider-package documentation that applies the vocabulary without conflation.

---

## Update protocol

- Never delete an accepted ID; deprecate or supersede it with valid-time fields and a replacement link.
- Update `Reviewed`, evidence, confidence, relationships, and the matching HTML companion together.
- Reference new records from the PRD or another authoritative consumer so they are not orphans.
- Before v0.7, record new decisions in the current PRD gate change log and accepted SoT snapshot;
  Wave 0B is an owner-authorized bootstrap example. From v0.7 onward, follow the normal EPIC
  Context & IDs protocol.
