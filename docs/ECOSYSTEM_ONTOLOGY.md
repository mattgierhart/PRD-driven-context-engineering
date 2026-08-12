---
title: "The Ontology of the Markdown Document Ecosystem"
status: "Research input — not accepted product truth (PRD.md authority order, item 7)"
purpose: "Formalize what the PRD-CE document ecosystem already is as an executable domain model; extract the v2-relevant insights from the 2026-08 ontology/agentic-systems research; propose staged, gate-legal recommendations."
date: 2026-08-12
inputs:
  - "External deep-research report: 'Ontologies + Agentic Information Systems' (2026-08, synthesized from Frank Coyle's AIEWF 2026 talk and the W3C/industry standards landscape; held in owner's files, not vendored — see Provenance)"
  - "Repository state at commit 11297db (branch claude/markdown-ecosystem-ontology-862afe)"
  - "docs/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md (research input per PLAN:88)"
  - "docs/PRD_CE_V2_BUILD_PLAN.md (contingent plan, subordinate to PRD.md)"
scope_guard: "Product Management ecosystem only. This document proposes no universal enterprise ontology (PLAN non-goal), mints no SoT IDs, and authorizes nothing. Every recommendation requires PRD acceptance at the stated gate."
---

# The Ontology of the Markdown Document Ecosystem

> **Thesis**: The PRD-CE markdown ecosystem is not merely *close to* the research's
> "executable domain model" architecture — it already **is** one, specialized to a single domain:
> the practice of product management. The v2 work is therefore not to build an ontology but to
> **declare the layers we already have, wire the two that are dormant, and refuse the three we
> don't need.**

---

## 0. Standing and scope

This is a research-input concept paper in the tradition of
[`docs/DELIVERABLES_CONCEPT.md`](DELIVERABLES_CONCEPT.md). It sits at item 7 of the PRD's authority
order ("inputs only until their evidence is durable, reviewable, sanitized, and accepted" —
[PRD.md](../PRD.md)). It does not change scope, advance a gate, or create IDs. Its intended
consumers are:

1. The **owner**, deciding what enters v0.2+ gate evidence.
2. The **v0.6 Architecture gate**, where "parser, ID, relationship, temporal, projection…
   contracts" formally land (PLAN:230-233).
3. The **Compatibility Inspector** design (ARC-003), whose finding categories are exactly the
   states this document formalizes.

---

## 1. The inversion that makes the research applicable

The research report's destination is a market category — "Agent Domain Packs" that compile an
industry's semantics into the schemas, constraints, policies, action contracts, and tests an
enterprise agent needs to operate safely. Its architecture is a seven-layer
**executable domain model** standing between the LLM and the systems it acts on.

PRD-CE is not in that market (and v2 explicitly refuses "a universal enterprise knowledge platform
or ontology," PLAN:144). The research applies through an inversion:

| Research concept | PRD-CE realization |
|---|---|
| The enterprise system being governed | The repository itself (PRD, SoT, EPICs, code) |
| The agent proposing actions | Each Claude/Codex session |
| The domain being modeled | Product-management practice (evidence → intent → delivery → reality → learning) |
| The domain pack | The methodology: ID taxonomy + lifecycle + 47 skills + hooks + validators |
| The action surface | Skills, gate advancement, ID registration, harvest, (future) Change Sets |

Read this way, PRD-CE is a **domain pack for the product-management domain**, already deployed on
its own substrate. The research's architecture questions stop being aspirational and become
*audit* questions: which of the seven layers exist here, in what state, and with what enforcement?

The rest of this document answers that audit, then extracts what the research adds that our own
planning documents (the V2 blueprint and build plan) had not already arrived at independently.

---

## 2. The ecosystem's current formal model, named precisely

What follows is the ontology that already exists — scattered across files, here assembled in one
place. Citations are to the live corpus.

### 2.1 Entity layer (classes)

- **Typed records** — 24 registered ID prefixes mapped to owning files in the machine-readable
  registry ([domain-profile.yaml:22-51](../.claude/domain-profile.yaml)); grammar
  `[PREFIX]-[SUBTYPE?]-[NUMBER]` ([SoT.UNIQUE_ID_SYSTEM.md §1.1](../SoT/SoT.UNIQUE_ID_SYSTEM.md)).
- **Code nodes** — a second, *extracted* entity plane (`module`, `class`, `function`, `table`,
  `endpoint`), identity `{parent_dir}_{file}_{symbol}`, deliberately not ID-prefixed
  (domain-profile.yaml:59-64).
- **Files as aggregates** — each SoT file owns one or more prefixes and follows a seven-part
  Template Contract ([SoT.README.md:74-86](../SoT/SoT.README.md)).
- **Planes (implicit)** — the file taxonomy already encodes the blueprint's five planes
  (Evidence: CFD · Intent: BR/FEA/UJ/PER/SCR · Delivery: API/DBT/TEST/DEP · Reality: MON/RUN/LL ·
  Change: EPIC, gate log). The blueprint names them explicitly (BLUEPRINT:209-225); the live
  corpus realizes them without naming them.

### 2.2 Edge layer (relationships)

Two vocabularies exist, one live and one proposed:

- **Live (10 predicates)** — `informed-by`, `driven-by`, `implements`, `enforces`,
  `validated-by`, `uses`, `depends-on`, `supersedes`, `conflicts-with`, `designed-for`, organized
  by direction class (upstream/downstream/lateral/temporal)
  ([cross-reference-patterns.md:180-201](../.claude/skills/ghm-id-register/references/cross-reference-patterns.md)).
  Declared semantics: *"the type is a hint, not a straitjacket"* (:200) — i.e., this layer carries
  **meaning**, not validity. That is the correct division of labor (see §4), but it means the
  validity half must live elsewhere.
- **Proposed (17 predicates, 6 categories)** — adds `supports`, `contradicts`, `derived-from`,
  `requires`, `constrains`, `part-of`, `verifies`, `monitors`, `violates`, `deprecates`,
  `introduced-by`, with canonical-direction normalization and namespaced extensions
  (BLUEPRINT:962-1030).
- **Bridge edges (code→spec, machine-harvested)** — `implements` / `verifies` / `references` /
  `violates`, each carrying an extraction-confidence tier
  (`EXTRACTED` / `INFERRED` / `AMBIGUOUS`) (domain-profile.yaml:73-77).
- **Required edges (constraint rules)** — `required_edges:` schema with
  direction (outbound/inbound) × severity (warn/block), enforced by
  `scripts/validate-edges.py` — **currently an empty ruleset** (domain-profile.yaml:79-101).

### 2.3 State dimensions

The live corpus and the input docs together already distinguish:

| Dimension | Live realization | Notes |
|---|---|---|
| Lifecycle status | `Status:` field values — Active, Accepted, Proposed, Deprecated, Superseded ([SoT.BUSINESS_RULES.md:31](../SoT/SoT.BUSINESS_RULES.md), register tables) | Blueprint adds Draft/Rejected/Withdrawn + a state machine (BLUEPRINT:1185-1200) |
| Authority | `Authority: Owner-confirmed` field; acceptance boundary — only records named in PRD's **Accepted SoT snapshot** are product truth ([SoT.README.md:12-14](../SoT/SoT.README.md)) | The decisive dimension; currently prose + snapshot membership |
| Decision vs runtime | Register columns separate "Decision status" from "Runtime validation" ([SoT.TECHNICAL_DECISIONS.md:19-24](../SoT/SoT.TECHNICAL_DECISIONS.md)) | A PRD-CE-original two-plane distinction worth keeping |
| Freshness (transaction time) | Staleness protocol: <30d current / 30-90d review / >90d historical (SoT.UNIQUE_ID_SYSTEM.md §1.5) | Orthogonal to lifecycle — "accepted and stale at the same time" (BLUEPRINT:151) |
| Valid time | `Valid From` / `Valid To` / `Invalidated By` + supersede protocol + `scripts/asof.py` reconstruction (SoT.UNIQUE_ID_SYSTEM.md §1.6) | Built in the prior KG thread (U1) |
| Evidence strength | Confidence 1/5–5/5 with named evidence classes per tier ([PRINCIPLES.md:165-199](../.claude/skills/PRINCIPLES.md)) | Calibrated by definition — each number *is* an evidence class |

The V2 PRD compresses these into eight **finding states** the Inspector must distinguish:
*accepted, proposed, inferred, ambiguous, stale, deprecated, superseded, unknown*
([PRD.md:118-119](../PRD.md)). §5.5 below argues these are *derived* classifications computed
from the orthogonal dimensions — not a ninth status field.

### 2.4 Evidence and provenance model

- **Evidence tiers** — P4's 1–5 scale with type-specific progressions and the anti-leakage rule:
  a proposer "must never fabricate or back-fill evidence to clear a downstream gate"
  (PRINCIPLES.md:91).
- **Source links** — `Source Evidence:` / `Implementation Evidence:` fields with resolved links
  (SoT.BUSINESS_RULES.md:69-73, 116-123).
- **Forward evidence targets** — `Next Evidence Target:` names what would raise the tier — a
  PRD-CE-original mechanism the research has no equivalent for.
- **Absent**: assertion-level provenance (*who/what asserted this, derived from which activity*).
  Git tells you the commit; nothing distinguishes an agent-inferred entry from an owner-authored
  one except the `Authority` field where present.

### 2.5 Authority model (policy layer)

- **Truth precedence chain** — PRD → accepted SoT → approved EPIC; CLAUDE.md governs behavior,
  not facts (CLAUDE.md; PRD.md:19-30).
- **Acceptance boundary** — snapshot membership in PRD.md is what makes a record *accepted*
  (SoT.README.md:12-14).
- **Owner gates** — readiness PASS is *eligibility for owner review*, never authorization
  (PRINCIPLES.md P7; ghm-gate-check anti-pattern table).
- **Machine-referenceable policy fragments** — Wave 0B BR entries each carry
  `Enforcement:` (location, timing) and `Failure disposition:` with a **gate code**
  (`V2_SCOPE_EXPANSION`, `DISTRIBUTION_LEAK_OR_OVERWRITE`, `PREMATURE_V2_EPIC`,
  `VERSION_DIMENSION_CONFLATION`) (SoT.BUSINESS_RULES.md:53-64 et al.). This is a native
  proto-policy schema — the research's actor/action/condition/prohibition pattern, grown locally.

### 2.6 Action surface (execution layer)

- **47 skills** = the action types. Each declares prose `Consumes` / `Produces` sections
  (P5 connective tissue) and a depth mode (rule 08). The registry lists them
  (domain-profile.yaml:103-153) but holds **no contracts** — preconditions and effects live in
  prose only.
- **6 wired hooks** = the runtime guards ([HOOK_CONTRACT.md:120-127](../.claude/hooks/HOOK_CONTRACT.md)).
- **Deterministic scripts** = the measurement/validation tools (`readiness.py` three-layer scorer
  with causal `caused_by` ↔ `consumed_by_epics` links; `validate-ids.sh`; `validate-edges.py`;
  `asof.py`; `check-stage-gate.sh`).
- **Read/write asymmetry, already decided** — ARC-003 makes the first executable value read-only
  (`index`, `check`, `query`, `trace`); Wave 5 (on hold) holds the entire write side: Change Set
  schema, stale-base rejection, atomic apply, receipts, authorization
  (SoT.TECHNICAL_DECISIONS.md:131-184; PLAN:376-395).

---

## 3. The seven-layer audit

The research's central artifact is a stack of seven logically distinct layers. The audit verdict
per layer, against the live corpus (not the aspirational docs):

| # | Layer | Question it answers | Live mechanism | Proposed (input docs) | Verdict |
|---|---|---|---|---|---|
| 1 | **Semantic ontology** | What is this thing? How does it relate? | ID registry (24 prefixes → files); 10-predicate edge vocabulary; code-node plane | 5 named planes; 17-predicate vocabulary; kind-vs-prefix metadata | **Built.** Registry is machine-readable; edge semantics deliberately advisory |
| 2 | **Structural contract** | Does it have the right shape? | File-level frontmatter; Template Contract; de facto Wave-0B entry fields | `SoTRecord` field set + parser grammar (H2 + `- **Field:**` + `### Relationships`) | **Convention.** No declared per-entry schema; live corpus ≠ proposed grammar |
| 3 | **Semantic validation** | Is it valid for this domain? | `validate-ids.sh` (dup/dangling/orphan); `validate-edges.py` + `required_edges`; readiness `cross_ref_integrity` | Blueprint's 11-check deterministic validation list | **Built but dormant.** Wired to no hook, no CI; ruleset empty |
| 4 | **Policy & authority** | Who may do what, when? | Precedence chain; acceptance boundary; owner gates; BR gate codes; one soft "ask" gate | Authority dimension; four write channels; adjudication outcomes | **Prose-strong, machine-weak** |
| 5 | **Process & state** | What transitions are legal? | PRD gate lifecycle (readiness floor + owner approval); staleness; supersede + valid-time (`asof.py`) | Orthogonal state dimensions; entry lifecycle state machine; quarantine | **Partial.** Repo-level state machine real; entry-level states named but not computable |
| 6 | **Provenance & evidence** | Why do we believe it? | Confidence tiers + source links + `Authority` + `Verified` + git | `confidence_basis`; content hashes; `Introduced-By`; provenance-to-line | **Partial.** Evidence culture strong; assertion-level provenance absent |
| 7 | **Execution contract** | What actions exist, with what pre/postconditions? | Skills (prose contracts); hooks; gate-check; install manifest | Change Sets; adjudication receipts; `index`/`check`/`query`/`trace` | **Read side designed; write side deliberately deferred** |

Two observations before the insights:

1. **"We are not far off" is correct and now precise.** Layers 1, 5-temporal, and the measurement
   half of 3 are built — largely by the prior KG-research thread (U1/U2). Layers 2, 4, 6 are
   partially built with strong local idioms (gate codes, decision-vs-runtime columns,
   `Next Evidence Target`). Nothing needs to be imported wholesale; every gap has a native seed.
2. **The blueprint independently converged on most of the stack.** Orthogonal state dimensions,
   edge categories, Change-Set-as-proposal, provenance-to-line — the research validates these
   rather than adding them. What the research adds is sharper: §4 and §5.

---

## 4. The load-bearing finding: representation is strong, enforcement is undeclared

The research's most technical point is a correction: **OWL is a language for meaning and
inference; SHACL and executable rules are the right tools for guardrails.** Representation,
validation, and enforcement are *different jobs*, and conflating them produces systems that look
governed but aren't.

Generalized to PRD-CE: our "OWL" is the prose layer (CLAUDE.md, rules, PRINCIPLES, skill
instructions — semantics interpreted by an LLM), and our "SHACL" is the deterministic layer
(validators, hooks, CI). Both exist. The audit finding is that **the boundary between them is
undeclared, and the deterministic layer is mostly unwired**:

| Enforcement tier | Mechanism | What actually sits here today (verified) |
|---|---|---|
| T4 **Hard gate** (machine refuses) | CI failure, `deny`, exit 2 | Plugin payload drift; pytest; markdown links. **No lifecycle rule is here.** |
| T3 **Soft gate** (escalates to human) | `permissionDecision: "ask"` | One hook — `traceability-gate.sh` — which exempts `SoT/`, `epics/`, `temp/`, `.claude/`, and **all `*.md`** (traceability-gate.sh:36), so in a docs-first repo it almost never fires |
| T2 **Advisory check** (deterministic report, unconsumed) | Exit codes nothing reads | `readiness.py` (CI smoke is `continue-on-error: true` **and** `\|\| true`, readiness.yml:37-38); density gate |
| T1 **Injected reminder** | SessionStart/PostToolUse context | Read-order injection; SoT-sync reminder; memory-extraction directive |
| T0 **Prose principle** | LLM-interpreted text | Truth precedence; "SoT before code"; `@implements` "MANDATORY" (rule 04) with no checker; stage-gate script and `validate-ids.sh` **invoked by nothing**; `required_edges: []` |

The failure mode is not missing rules — it is **rules whose tier is implied by tone rather than
declared by design**. "MANDATORY" appears at T0/T1 where it carries no mechanism; two fully built
validators sit at T0 because no event binds them; three hand-synced copies of the gate criteria
exist (`references/gate-criteria.md`, `GATE_REQUIREMENTS` in `_readiness/stage.py:47-106`,
`check-stage-gate.sh`) with nothing testing their agreement; and `ghm-sot-builder` registers new
SoT files without updating `domain-profile.yaml` — a silent registry-drift channel, since the
scorer and hooks read only the profile.

**Proposal — the enforcement ladder as ontology metadata.** Every governance rule declares two
properties: its **tier** (T0–T4) and its **binding point** (session event · tool event · CI ·
gate review · inspector finding). Wave 0B's BR entries already model this natively
(`Enforcement:` location/timing + `Failure disposition:` gate code); the move is to generalize
that schema to all rules and hook docs, then treat *tier promotion* as an explicit, evidenced
decision (a rule earns T3/T4 when violations are observed, mirroring the blueprint's
edge-promotion discipline, BLUEPRINT:1022-1030).

Two important non-goals of this proposal:

- **Do not push everything to T4.** The neural/symbolic split is the architecture working as
  designed — the repo's own teeth are epistemic (measurement, causality, anti-Goodhart), not
  coercive. Advisory-first is a *feature* for a methodology template; the defect is only the
  undeclared tier.
- **Keep the deterministic layer LLM-free** (rule 07). The research agrees: validation must be
  cheap, reproducible, and boring.

---

## 5. What the research actually adds: six insights for v2

### 5.1 Declare the enforcement ladder (Layer 4)

Covered in §4. Cheapest structural insight with the highest leverage; pure definition work, legal
pre-v0.2. Also the correct frame for the v0.5 Red Team gate ("authority" is already in its threat
model, PLAN:229).

### 5.2 Build around actions, not nouns (Layer 7)

The research inverts traditional ontology practice: start from *consequential actions*, work
backward to the entities, states, evidence, and policy each action needs. PRD-CE's nouns are
mature; its actions are half-formal:

- **Skills are action types** with prose contracts. Machine-readable frontmatter
  (`consumes`, `produces`, `gate_preconditions`) would let the system answer *"which actions are
  legal in the current state?"* — turning the skill list into an **action registry** parallel to
  the ID registry, and giving the density gate and gate-check real inputs instead of regex
  heuristics.
- **Gate advancement is an action** whose precondition (readiness floor) and authority (owner)
  are clear but whose *receipt* is only a PRD change-log row. Naming it as an action with a
  recorded outcome closes the loop the research calls propose → validate → authorize → execute →
  verify.
- **Wave 5's Change Set is the write-action contract**, independently matching the research's
  loop (stale-base rejection = precondition check; receipts = provenance; add explicit
  **postcondition verification** after apply). The research's read/write asymmetry — read tools
  validate results, write tools validate *proposals* — is exactly ARC-003 vs Wave 5. v2 should
  state that asymmetry as a principle rather than an accident of sequencing.

### 5.3 Let the agent's blast radius set the formalization budget

The research's maturity curve — Answer → Interpret → Recommend → Decide → Act → Operate — maps
one-to-one onto the wave plan:

| Maturity | v2 surface | Layers that must be formal *at this level* |
|---|---|---|
| Answer | SoT HTML views | 1 (addresses render as anchors) |
| Interpret | **Inspector** (`index`/`check`/`query`/`trace`) | 1, 2, 3, 5, 6 — read-side complete |
| Recommend | Task workflows, Deliverables concept, change *proposals* | + 7 (proposal shape) |
| Decide | Owner gates, adjudication | + 4 (authority machine-checkable) |
| Act | Accepted-state writer (Wave 5, held) | + 7 write contracts, postconditions |
| Operate | *(out of scope)* | — |

This yields the bright-line rule that answers the blueprint's own "ontology bloat: HIGH" risk:
**no layer gets formalized without a deterministic consumer at the current maturity level.** It
also explains *why* the corpus feels "not far off": everything the Interpret level needs exists
at least as convention; what's missing is exactly what Recommend/Decide/Act need — which are
gated anyway.

### 5.4 Split the kernel from the method pack (Layer 1, and the tension-resolver)

The research's product architecture — a small universal kernel plus composable domain packs —
is the structure BR-001 already implies ("adjacent methodologies MUST remain separately governed
products or method packs") and PLAN:153-157 already constrains ("No future use case is allowed to
make Product Management users learn extra concepts"). Making the boundary explicit:

- **Kernel (methodology-generation-stable, domain-free):** ID grammar; edge vocabulary +
  direction classes; orthogonal state dimensions; provenance/evidence fields; valid-time +
  supersession; enforcement-ladder metadata; the action-contract *shape*; acceptance-boundary
  mechanism.
- **Product-Management pack:** the 24 prefixes and their files; the v0.1→v1.0 gate definitions
  and skill set; confidence *tier definitions* per record type; the agent squad; gate criteria
  tables.

This split cleanly resolves the sharpest blueprint↔plan contradictions: *gates* are pack content
(the PM pack ships ten; the kernel knows only "policy checkpoint"), reconciling PLAN:223 with
BLUEPRINT:3259. *EPIC vs Change Set* becomes kernel primitive ("reviewable unit of work") vs pack
projection. And ARC-004's authority/seed separation already gives the packaging mechanics the
split needs.

### 5.5 Make the eight truth-states computable (Layers 5+6 — the Inspector's spec)

The Inspector must classify findings as *accepted, proposed, inferred, ambiguous, stale,
deprecated, superseded, unknown* (PRD.md:118-119) — reproducibly, from the corpus alone. Those
eight are not a new status field; they are **derived classifications** over the orthogonal
dimensions in §2.3:

| State | Operational test (candidate) |
|---|---|
| accepted | Named in PRD's Accepted SoT snapshot ∧ lifecycle status Active/Accepted |
| proposed | Well-formed record not in the snapshot (incl. Change-Set content, post-Wave-5) |
| inferred | Asserted by an agent/extraction without owner authority (requires §5.5 provenance fields; bridge edges already carry `INFERRED`) |
| ambiguous | Parse succeeded but identity/relationship/status could not be resolved to one reading → quarantine, never silently normalize (PLAN:294-297) |
| stale | Freshness policy breach: `Verified` > 90d (§1.5) while lifecycle still current |
| deprecated / superseded | Lifecycle status + valid-time closure (`Valid To`, `Invalidated By`) — already computable via `asof.py` |
| unknown | Structure outside every compatibility profile → explicit unknown, never dropped |

Defining this matrix — states × operational tests × which authority may move a record between
them — is cheap definition work now and becomes the Inspector's classification spec at v0.6. It
also **re-ranks U6** from the prior KG thread: claim-level provenance was graded lowest-value
then; with the Inspector as first product, the `inferred`-vs-`accepted` distinction is
load-bearing, and it needs only two or three structured fields (`Asserted-By`,
`Accepted-By`/existing `Authority`, optionally `Derived-From`) at **record** granularity — not
sentence-level claims (the blueprint's own granularity caution, BLUEPRINT:905).

A tension this resolves: the blueprint discourages numeric confidence as false precision
(BLUEPRINT:1179). P4's numbers are not uncalibrated — each value *names an evidence class*
(PRINCIPLES.md:171-177), which is precisely the "calibrated" exception the blueprint allows. Keep
the 1–5 notation as the PM pack's calibrated band vocabulary; map it to kernel bands
(low/medium/high/verified) rather than dropping it.

### 5.6 One vocabulary, one registry (the SKOS move)

The research stack carries a dedicated vocabulary layer (SKOS) distinct from the ontology. v2
needs exactly that, cheaply: the input docs currently run **five product labels** (The Product
Model / Product Knowledge Graph / Product Model Runtime / PRD-CE V2 / GearHeart AI), **two public
concept budgets** (four vs five nouns), and **three vocabularies that reuse the tokens
"observed/inferred"** with different meanings (research labels; evaluation evidence classes
OBSERVED/PROXY/INFERRED/NOT-TESTED; record-level confidence basis). The evaluation protocol
already hunts this as a defect class (EVAL:362-363). A single concepts registry — every canonical
noun, its definition line, its plane, and its kernel/pack membership — is pure definition work,
directly consumable by the v0.3 naming gate and by the Inspector's reporting vocabulary.

---

## 6. What v2 should *not* adopt (anti-scope, reaffirmed)

The research also marks what to refuse, and the corpus already encodes most of these refusals:

| Refusal | Anchor |
|---|---|
| No OWL/RDF serialization, no triple store, no graph DB | Markdown canonical; SQLite/graph JSON are disposable projections (ARC-001). The research's own "semantic layer over existing systems, not migration" argument supports inspecting repos in place |
| No universal enterprise ontology; no adjacent-industry packs | PLAN:144; BR-001. The kernel/pack split (§5.4) is how future methodologies happen *without* broadening V2 |
| No LLM-judged validation dimensions | Rule 07; P7 anti-Goodhart. The research: constraints must be deterministic to be trustworthy |
| No reasoner-style inference as authority | "Generated or inferred knowledge never silently becomes authoritative" (BLUEPRINT:71; PRD desired outcome 3). Inference may *propose*; only adjudication accepts |
| No new public nouns beyond the budget | Blueprint kill criterion: "users cannot get value before learning the ontology." The ladder, states, and contracts in §5 are **internal** formalizations — none adds a concept a PM user must learn |
| Don't replace the numeric confidence tiers | They are calibrated evidence classes (§5.5); translate, don't delete |

---

## 7. Candidate resolutions to the documented tensions

The v2 input docs contain ten verified internal tensions. The kernel/pack lens (§5.4) resolves
most; the rest are open owner decisions (PLAN:582-590) this document deliberately does not answer:

| Tension | Candidate resolution | Owner decision? |
|---|---|---|
| Five competing product names | Vocabulary registry (§5.6); one name chosen at v0.3 | **Yes** (PLAN:582) |
| Root `SoT/` vs `product/SoT/` | Kernel defines the *acceptance boundary mechanism*, pack defines the path; alpha inspects in place (PLAN:148 stands) | Deferred by plan |
| EPIC vs Change Set | Kernel: "reviewable unit of work"; PM pack keeps EPIC as its projection; revisit at Wave 5 | At v0.7 |
| Gates in kernel vs removed | Gates are pack content; kernel has policy checkpoints only | No — resolvable now |
| 4 vs 5 public nouns | Count once, in the vocabulary registry | With naming gate |
| Numeric confidence vs basis+band | Keep tiers as calibrated bands; map to kernel vocabulary | No |
| Three "observed/inferred" vocabularies | Registry disambiguates (finding-classes ≠ confidence-basis ≠ research labels) | No |
| Record form: frontmatter vs `- **Field:**` | Entry-schema decision at v0.6, informed by the Wave 1 fixture matrix + loss inventory | At v0.6 |
| Readiness vs "fitness views" | Readiness stays (it is the deterministic floor, P7); goal-scoped views are *additional projections*, not replacements — no accepted decision authorizes removal | If ever raised |
| Build vs Deliver verb | Vocabulary registry marks it "undecided, owner-gated" | **Yes** (PLAN:585) |

---

## 8. Staged recommendations (gate-legal sequencing)

Ordered by lifecycle legality. Pre-v0.7, everything is definition work — files describing
contracts, no runtime (BR-004).

**Legal now (pre-v0.2, definition only):**

| # | What | Layer | Deterministic consumer | Effort |
|---|---|---|---|---|
| R1 | Vocabulary/concepts registry (§5.6) | 1 | Naming gate; EVAL defect hunt; all docs | S |
| R2 | Enforcement-ladder declaration over existing rules + hooks (§4) — tier + binding point per rule, generalizing the BR `Enforcement`/`Failure disposition` schema | 4 | v0.5 Red Team; humans | S |
| R3 | Truth-state matrix: 8 states × operational tests × transition authority (§5.5) | 5+6 | Inspector classification spec (v0.6) | M |
| R4 | Kernel/pack boundary memo (§5.4) | 1 | BR-001 governance; packaging (ARC-004); tension resolutions | M |

**At v0.6 Architecture (contracts land here, PLAN:230-233):**

| # | What | Layer | Consumer |
|---|---|---|---|
| R5 | Per-prefix entry schema (required fields), reconciled against the Wave 1 fixture matrix + loss inventory | 2 | Inspector parser/validator |
| R6 | Edge-vocabulary merge: live 10 + proposed 17 → one registry with categories, canonical directions, inverses, namespacing, promotion rule | 1/3 | Inspector; `validate-edges` v2 |
| R7 | Skill action contracts as machine-readable frontmatter (§5.2) | 7 | Context loading; gate-check; future action-graph validation |
| R8 | Provenance fields (`Asserted-By`; keep `Authority`; optional `Derived-From`) — adoption-incremental like valid-time | 6 | Inspector `inferred`-state test |

**At v0.7+ (runtime, EPIC-gated):**

| # | What | Notes |
|---|---|---|
| R9 | Wire the dormant validators: `validate-ids.sh` into CI at T2 (advisory), promote to T4 on evidence; enable a repo-local `required_edges` starter set | Repo profile only — seeds stay empty so templates validate clean (ARC-004 pattern) |
| R10 | Inspector implements state classification + provenance-to-line | Already ARC-003 scope; R3/R5/R8 are its spec inputs |
| R11 | Expose readiness dimensions as named competency queries under `check`/`query` (prior thread's U3) | Cheap; makes the "eval suite" a visible pack component |

**Wave 5 (held, unchanged):** the Change-Set loop is the write-action contract; add explicit
postcondition verification and align its receipts with the action registry (§5.2).

---

## 9. The prior KG thread, re-ranked under this lens

The 2026-06 KG-research re-grade proposed upgrades U1–U7. Status under the executable-model
frame:

| Upgrade | Then | Now |
|---|---|---|
| U1 valid-time | Built (`asof.py`, supersede protocol) | Layer-5 substrate for `superseded`/as-of tests — done |
| U2 required edges | Built, ruleset empty | The Layer-3 constraint engine — **wire it** (R9) |
| U3 competency queries | Partial (readiness dims unnamed) | R11 — cheap, Inspector-shaped |
| U4 six-layer eval | Genuine gap, lead workstream | Becomes the pack's **agent eval suite** component; intersects R3 (states) + R11 (queries) |
| U5 retrieval routes | Low priority | Unchanged — Wave 3/6 concern (task-scoped context, MCP) |
| U6 claim modeling | Graded lowest value | **Upgraded**: record-level provenance is load-bearing for the Inspector's `inferred` state (R8) — but stays record-granular, not sentence-claims |
| U7 confidence gate | Designed, unenforced | Subsumed by the enforcement ladder: a T2 check with a declared promotion path |

---

## 10. Open questions for the owner

1. **Home for the registries** — vocabulary registry (R1) and truth-state matrix (R3): governance
   sections in `SoT.UNIQUE_ID_SYSTEM.md`, a new `docs/` contract, or the blueprint's
   `product/schema/` shape? (Affects packaging under ARC-004.)
2. **Acceptance of this document** — remain input, or sanitize the external research report into
   `temp/v0.1-intake/` as reviewable evidence toward the v0.2 gate?
3. **Enforcement default** — do new rules declare a tier at creation (schema field), and is T2
   the default for anything with a deterministic checker?
4. **Repo-local `required_edges`** — enable a minimal set for *this* repository now (BR/ARC
   entries exist to constrain), or wait for the Inspector to be the first consumer?
5. **Kernel noun budget** — does the kernel/pack memo (R4) get its own concept budget so the
   split doesn't itself become ontology bloat?

---

## Provenance of this document

Synthesized 2026-08-12 from: the external deep-research report (not vendored — it carries
third-party consulting context; available from the owner on request), the two v2 input docs, and
direct file-level inspection of the live corpus (registry, entries, hooks, validators, CI) at
commit `11297db`. All enforcement-spectrum claims in §4 were verified against script source and
workflow files, not inferred from documentation. Findings about input-doc tensions cite the
documents' own lines and are reportable defects per the evaluation protocol, not new claims.
