---
title: "The Ontology of the Markdown Document Ecosystem"
version: 2.2
status: "Research input — not accepted product truth (PRD.md authority order, item 7)"
purpose: "Formalize the document ecosystem plane-first (owner direction, 2026-08-12): five planes of product memory as the organizing axis, the numbered lifecycle as one pack's guided walk, and the stage skills as playbooks behind a verb surface. Staged, gate-legal recommendations."
date: 2026-08-12
direction: "Owner-directed 2026-08-12: rework domain-first. In the blueprint's vocabulary the domains of product memory are its five *planes*; this document standardizes on 'plane' (see §0 naming note) and treats formal acceptance of the direction as its first recommendation (R0)."
inputs:
  - "External deep-research report: 'Ontologies + Agentic Information Systems' (2026-08; held in owner's files, not vendored — see Provenance)"
  - "docs/v2/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md — the owner+Codex v2 review (research input per PLAN:88)"
  - "docs/v2/PRD_CE_V2_BUILD_PLAN.md (contingent plan, subordinate to PRD.md)"
  - "Repository state at commit 45ae3a3 (branch prd-ce-v2)"
scope_guard: "Product Management ecosystem only. No universal enterprise ontology (PLAN non-goal), no SoT IDs minted, nothing authorized. Every recommendation requires PRD acceptance at the stated gate."
---

# The Ontology of the Markdown Document Ecosystem

> **Thesis**: The ecosystem's real structure is five planes of product memory — **Evidence,
> Intent, Delivery, Reality, Change**. The numbered lifecycle (v0.1→v1.0) is not the ontology;
> it is one pack's guided walk across the planes, and the walk is provably re-expressible as
> per-plane state conditions without loss. A true v2 — the direction the owner set 2026-08-12,
> contingent on the R0 acceptance record (§9) — would make the planes the primary *internal*
> structure, collapse the 41 stage skills into playbooks behind a seven-verb surface, and keep
> the numbered walk as a compatibility projection for every repository that already speaks it.
> The *audience-facing* stage vocabulary is the PM loop the same review defined — **Explore →
> Shape → Decide → Build → Learn**, with Check cross-cutting: "the graph compounds beneath those
> verbs" (BLUEPRINT:188).

---

## 0. Standing, scope, and what changed in this revision

This is a research-input concept paper (PRD authority order item 7 — inputs only until accepted).
It does not change scope, advance a gate, or create IDs.

**Revision note (progressive doc, one file).** Version 1 of this document (same day, commit
`1afe828`) followed the repository's committed truth precedence: the build plan demotes the
blueprint to research input (PLAN:88) and keeps the numbered lifecycle authoritative (PLAN:223),
so v1 treated the plane-first restructure as an open *tension*. The owner then directed
(2026-08-12) that the ontology be reworked domain-first — the direction the owner+Codex blueprint
review had already argued. This revision inverts the document's spine accordingly. The committed
record still says the opposite, which is why **R0 — record the direction decision — precedes every
other recommendation**: until a BR/ARC record and a build-plan revision land, plane-first is an
owner-stated direction, not accepted product truth.

**Naming note ("domain" is triple-booked).** The owner's phrase is *domain-first*. The blueprint
consistently calls the five buckets **planes** (BLUEPRINT:209, 666) and reserves *domain* for
three other meanings: the product's subject domain (BLUEPRINT:762), vertical **domain packs**
(`registry/domain-packs/`, BLUEPRINT:1857, 2302-2306), and the live registry's discipline sense
(`domain-profile.yaml`, "Derivatives customize this file for their domain"). Using "domain" for
the planes would collide with all three. This document therefore says **plane** throughout and
lists the final public naming as a vocabulary-registry decision (§10, Q1).

Intended consumers: the owner (R0 and the §10 decisions); the v0.6 Architecture gate (where the
contracts land, PLAN:230-233); the Compatibility Inspector design (ARC-003).

---

## 1. The two inversions

**First inversion — the research applies to us.** The external research's "executable domain
model" architecture (seven layers between an LLM and the systems it acts on) applies to PRD-CE
through a role swap: the repository is the enterprise system; each session is the agent; the
methodology is a domain pack for the practice of product management. That inversion made the
research's architecture questions *audit* questions, and the audit (§5) stands unchanged from v1.

**Second inversion — planes over stages.** Version 1 organized the ontology the way the
methodology currently presents itself: a numbered lifecycle that skills and gates walk in order.
The owner+Codex blueprint review inverted that: the durable structure is *what kinds of product
memory exist and how they relate* — the five planes — and any ordering of work across them is
policy, not ontology. The blueprint states the demotion plainly: *"10 lifecycle stages | Demote |
Optional guided journey and policy profiles"* (BLUEPRINT:606); *"Do not encode a rigid ten-stage
lifecycle into the kernel"* (BLUEPRINT:3259); *"This is a journey, not a hard gate system. Users
may enter anywhere"* (BLUEPRINT:558-560). §3 shows the inversion is lossless against the live
gate machinery.

---

## 2. The five planes: the primary ontology

### 2.0 The plane model

The blueprint defines the planes and their flow topology (BLUEPRINT:209-215, 666-756):

| Plane | Question it answers | Stores | Flow into Change |
|---|---|---|---|
| **Evidence** | What did we observe, and from where? | Interviews, feedback, competitive analysis, research sources, experiment results | one-way (`E → C`) |
| **Intent** | What do we currently intend, require, or forbid? | Outcomes, decisions, constraints, requirements, policies, non-goals | bidirectional (`I ↔ C`) |
| **Delivery** | How is intent designed, built, verified, shipped? | Journeys, screens, architecture, API/data contracts, code units, tests, releases | bidirectional (`D ↔ C`) |
| **Reality** | What actually happens in production and market? | Telemetry, adoption signals, incidents, support patterns, measured outcomes | one-way (`R → C`) |
| **Change** | What is proposed to change, and how was it adjudicated? | Proposals, semantic deltas, reviews, adjudication events (`CHG-`) | writes SoT (`C → SoT`) |

Three structural rules carry the whole model:

1. **SoT is the accepted projection of *all* planes, not one plane's home.** An accepted SoT
   record "may represent a decision, business rule, journey, requirement, architecture
   constraint, contract, test specification, lesson, signal, or evidence summary"
   (BLUEPRINT:905). The plane is a property of the record, not of the directory.
2. **Only the Change plane writes accepted state** (`C → SoT`, BLUEPRINT:674) — every semantic
   mutation is proposed, adjudicated, then materialized. This is the read/write asymmetry the
   external research demands (write tools validate *proposals*), and it is why Wave 5's Change
   Set contract is not an add-on but the Change plane's own definition.
3. **The highest-value queries are cross-plane comparisons** (BLUEPRINT:750-756): intent vs
   implementation, implementation vs verification, intent vs observed reality, evidence vs
   accepted decisions. The diagnostic edges are typed: `D -.implementation coverage.-> I`,
   `R -.drift.-> I`, `E -.supports/contradicts.-> I` (BLUEPRINT:677-679). Note all three point at
   **Intent** — it is the hub plane the others are measured against.

### 2.1 The prefix→plane registry

Every live ID prefix maps onto a plane. Where the blueprint assigns one explicitly the row cites
it; the rest are inferred from the prefix's semantics; eight are genuinely ambiguous (§2.2).

| Prefix (live registry) | Plane | Basis |
|---|---|---|
| CFD | **Evidence** | Explicit — "Customer feedback" (BLUEPRINT:689); *but see A8: post-launch CFD straddles Reality* |
| BR | **Intent** | Effectively explicit — requirement/policy/constraint (BLUEPRINT:703-706); BR-104 is the running example |
| FEA | **Intent** | Inferred — a feature is a scoped requirement (BLUEPRINT:705) |
| KPI | **Intent** (target half) | The blueprint splits the concept — see A5 |
| PER | **Intent** | Inferred — the accepted persona is a normative model of who we serve (`designed-for` targets, BLUEPRINT:972) |
| RISK | **Intent** | Inferred — the durable content is the owner's disposition (constraint); see A3 |
| GTM | **Intent** | Inferred — strategy decisions; executable GTM assets lean Delivery; see A4 |
| UJ | **Delivery** | Explicit — "User journey" (BLUEPRINT:715) |
| SCR | **Delivery** | Explicit — "Screen or interaction contract" (BLUEPRINT:716) |
| DES | **Delivery** | Effectively explicit — UX flow artifacts (BLUEPRINT:788) |
| API | **Delivery** | Explicit — "API/data contract" (BLUEPRINT:718) |
| DBT | **Delivery** | Explicit — data contract (BLUEPRINT:718) |
| TECH | **Delivery** | Inferred — governs how the product is built; see the decision-vs-artifact note below |
| ARC | **Delivery** | Explicit — "Architecture" (BLUEPRINT:717) |
| ENV | **Delivery** | Inferred — build/release infrastructure profile |
| INT | **Delivery** | Inferred — a species of API/data contract |
| TEST | **Delivery** | Explicit — "Test" / verification record (BLUEPRINT:720, 922) |
| DEP | **Delivery** | Explicit — "Release" (BLUEPRINT:721) |
| RUN | **Delivery** | Inferred — designed operational artifact |
| SEC | **Delivery** | Inferred — an inventory of the delivered system; see A7 |
| MON | **Reality** | Explicit — "monitoring or production signal" (BLUEPRINT:923) |
| ADO | **Reality** | Explicit — "Adoption signal" (BLUEPRINT:730); strategy sub-entries leak Intent, see A2 |
| LL | **Evidence** | Inferred — a distilled episode that informs future claims; see A1 |
| EPIC | **Change** | Effectively explicit — "EPICs → active Change Sets" (BLUEPRINT:602, 2791); see A6 |
| Code nodes (module/class/function/table/endpoint) | **Delivery** | Explicit — "Code unit" (BLUEPRINT:719); bridge edges `implements`/`verifies` are Delivery-category predicates |

**Decision-vs-artifact note (ARC, TECH):** an accepted decision record lives on the plane of the
artifact it governs — Delivery — matching the blueprint's own placement of "Architecture"
(BLUEPRINT:717). The deciding *act* is Change-plane history, recordable via `introduced-by`. RISK
stays Intent (A3) because its durable content is a constraint on intent, not a governed artifact.

The smallest machine-readable step toward plane-first is a `plane:` key on each entry of
`id_prefixes:` in [domain-profile.yaml](../../.claude/domain-profile.yaml) (R2). The readiness
scorer, the validators, and the future Inspector all already read that file; one key turns the
mapping above from prose into a queryable fact.

### 2.2 The eight ambiguities (real modeling decisions, not defects)

| # | Prefix | Competing planes | Recommended resolution |
|---|---|---|---|
| A1 | LL | Evidence vs Change | **Evidence** — a lesson's downstream function is to inform claims, not mutate them; it is *produced by* Change-plane history, which the `introduced-by` edge can record |
| A2 | ADO | Reality vs Intent | **Reality** primary; the beachhead/whole-product *strategy* sub-entries are Intent decisions and should carry the plane on the entry, not the prefix |
| A3 | RISK | Intent vs Evidence vs Change | **Intent** — the accepted record is the owner's disposition + mitigation (a constraint); the triggering observation is Evidence it links `informed-by` |
| A4 | GTM | Intent vs Delivery | **Intent** primary; shipped GTM artifacts (alternatives pages, outreach sequences, changelog) behave as Delivery and can be entry-level exceptions |
| A5 | KPI | Intent vs Reality | **Split the concept**, as the blueprint does: the target/threshold is Intent (its "desired outcome", BLUEPRINT:917); the measured reading is a Reality signal that `monitors` the target |
| A6 | EPIC | Change vs Delivery vs "just a view" | **Change** — an EPIC is a sized unit of proposed work; the blueprint also allows "an EPIC may remain an optional view/playbook" (BLUEPRINT:602), which is the compatibility answer (§3.3) |
| A7 | SEC | Delivery vs Intent | **Delivery** — the live file is an inventory of what exists; a secret-handling *rule* would be an Intent policy |
| A8 | CFD | Evidence vs Reality | **Evidence** pre-launch; post-launch feedback (the v0.9 feedback loop writes CFD-) is Reality-plane material — either a plane-on-entry override or a future signal prefix; owner call |

One wrinkle to carry into the edge-vocabulary merge (R8): the blueprint's predicate table has an
**"Experience" category** (`designed-for`, BLUEPRINT:972) corresponding to no plane — persona and
outcome targeting sits between Intent and Delivery without a declared home.

### 2.3 The kernel beneath the planes

The planes organize *content*. Beneath them sits the domain-free kernel — the primitives any
method pack would reuse, and exactly what the blueprint guards as core (BLUEPRINT:1565-1575:
schema, change semantics, temporal model, authority model, policy engine, compatibility rules):

- the **ID grammar** and prefix registry mechanism (not the PM prefixes themselves);
- the **edge vocabulary** with direction classes and canonical-direction normalization;
- the **orthogonal state dimensions** — lifecycle, authority, confidence basis, confidence band,
  freshness, valid time, transaction time, scope (BLUEPRINT:1166-1179) — with valid-time and
  supersession already live (`asof.py`, SoT.UNIQUE_ID_SYSTEM.md §1.6);
- the **evidence/provenance fields** and calibrated confidence tiers (PRINCIPLES.md:165-199);
- the **acceptance boundary** mechanism (only snapshot-named records are truth, SoT.README.md:12-14);
- the **enforcement ladder** (§6) and the policy engine that binds checks to events;
- the **action-contract shape** (§4).

The PM pack contributes: the 24 prefixes and their plane assignments, the playbooks (§4.2), the
guided journey, the gate criteria bundles as policy packs (§3.2), and the confidence-tier
definitions per record type.

### 2.4 The surface layer: where humans meet the planes (owner-raised, 2026-08-13)

The planes structure memory; humans need a layer **on top** — to see progress, review, decide,
and backtrack. The repo has built toward it in three generations (PRD.md as the interface → the
SoT HTML review pages → the decision-point pages of
[`docs/v2/DELIVERABLES_CONCEPT.md`](DELIVERABLES_CONCEPT.md)), and v2 makes it a first-class
element: **surfaces**, all derived from the planes, none canonical (ARC-001 — delete any surface
and it regenerates). Three kinds, keyed to the three human jobs:

| Surface | Human job | Direction | Today's ancestor |
|---|---|---|---|
| **Front door** | see progress, what needs me | render ↑ | README command center; blueprint's generated `PRODUCT.md` |
| **Views** | understand — per-plane renders in the reviewer's native shape, incl. the as-of time machine | render ↑ | `SoT/html/` companion pages; blueprint's derived-views list (BLUEPRINT:1244-1258) |
| **Deliverables** | act — rank, select, acknowledge, author | **emit ↓** | DELIVERABLES_CONCEPT's two species (Intake / Review) |

The structural claim that makes this ontology-clean rather than bolt-on: **a Review deliverable
is the human half of `decide`** — the adjudication surface. Its output is not a new format but
the exact record the graph expects ("input that *becomes* SoT", DELIVERABLES_CONCEPT §2), and
"completing a deliverable **is** that sign-off, captured as a timestamped decision" (§2) — i.e.,
deliverables are how judgment enters the Change plane, and the sign-off record is adjudication
provenance (L6). Backtracking splits the same way: the as-of view is its read face (`asof.py`,
already built); a supersede deliverable is its write face — never deletion. Every verb terminates
in a surface (explore → evidence cards; decide → a Review deliverable; learn → the drift view;
check → fitness views and the freshness queue), which is what keeps the planes invisible (§10 Q2)
without leaving the human blind.

The deliverable canon — the owner-articulated key moments where clarity of expression matters
most (problem framing, persona, commercial model, journeys, tech & risk, sequencing, GTM, and a
proposed launch verdict) — lives in [`docs/v2/V2_KEY_MOMENTS.md`](V2_KEY_MOMENTS.md): each moment =
one deliverable (human face) + a policy-pack profile (machine face, possibly composing several
packs) + its preparation playbooks. Moment surfaces follow the **Graphify pattern** (canon §2):
a bespoke designed template hydrated by a deterministic, LLM-free pull script from the planes —
living projections rebuilt loop-by-loop, never hand-edited.

---

## 3. The numbered lifecycle, re-read as a plane walk

### 3.1 The translation is lossless

The live gate machinery already *is* per-plane conditions wearing version numbers. Each stage's
`GATE_REQUIREMENTS` entry (scripts/_readiness/stage.py:47-106) demands "N records of prefix P" —
and every required prefix resolves to a plane via §2.1:

| Gate | stage.py requires | Plane reading |
|---|---|---|
| v0.1→v0.2 | CFD×3 | **Evidence** baseline exists |
| v0.2→v0.3 | CFD×3, BR×1 | **Evidence** (competitive) + first **Intent** decision |
| v0.3→v0.4 | BR×3, KPI×1, CFD×5, FEA×1 | **Intent** commitments (pricing, outcome, scope) over a deeper **Evidence** pile |
| v0.4→v0.5 | PER×1, UJ×3 | **Intent** (who) + first **Delivery** contracts (journeys) |
| v0.5→v0.6 | RISK×5, TECH×3 | **Intent** constraints (RISK) + **Delivery** build/buy decisions (TECH) |
| v0.6→v0.7 | ARC×1, API×1, DBT×1 | **Delivery** contracts drafted |
| v0.7→v0.8 | EPIC×1, TEST×1 | **Change** unit open + **Delivery** verification |
| v0.8→v0.9 | DEP×1, RUN×1, MON×1 | **Delivery** ops + first **Reality** instrumentation |
| v0.9→v1.0 | GTM×1, KPI×3 | **Intent** distribution + targets whose evaluation is a **Reality** comparison |

Read down the right column: the gate sequence encodes a fixed **plane-population order** —
Evidence → Intent → Delivery → Change + Reality. The remaining stage score weight,
`cross_ref_integrity` at 0.20 (stage.py:36-41), is cross-plane edge checking — the blueprint's
highest-value queries in miniature. Nothing about the numbered walk exceeds "per-plane state
conditions plus cross-plane integrity, evaluated in a fixed order." That is what makes the
inversion safe: **v2 would keep the conditions and drop the mandated order** ("Users may enter
anywhere," BLUEPRINT:560).

Two honesty notes from the same comparison: `gate-criteria.md` demands materially more than
stage.py checks (SCR entries at v0.4, code coverage at v0.7, a feedback loop at v0.9 — none
ID-counted), confirming v1's three-hand-synced-copies finding; and the richer criteria are
*also* plane-typed, so the policy-pack translation below covers them too.

### 3.2 What each part of the gate system becomes

Applying the blueprint's own merge-time test — core primitive, derived view, or playbook
(BLUEPRINT:3268-3271):

| Today | Plane-first disposition | Basis |
|---|---|---|
| Gate *enforcement machinery* (readiness engine, hooks, validators) | **Kernel** — the policy engine ("Hooks \| Keep \| Runtime policy enforcement", BLUEPRINT:609) | core primitive |
| Each gate's *criteria bundle* (GATE_REQUIREMENTS row + gate-criteria.md detail) | **Policy pack** — named, installable, invoked as `check --policy=<profile>` (BLUEPRINT:2002, 2308-2309) | configuration |
| The v0.1→v1.0 *ordering* | **Guided journey** — documentation narrative (`docs/journey/`, BLUEPRINT:2030-2035), optional; its public names are the PM loop stages (Explore → Shape → Decide → Build → Learn) | playbook/docs |
| The readiness *score* | **Goal-scoped fitness + graph-integrity views** (BLUEPRINT:610) — computed per active change, "no universal readiness grade" (BLUEPRINT:2538) | derived view |
| Owner gate *approval* | Unchanged — **adjudication on the Change plane**; P7 stands (a view is eligibility, only the owner authorizes) | authority model (kernel) |

The readiness reconciliation deserves emphasis because v1 left it as a tension: the deterministic
three-layer scorer is not discarded — its dimensions would be **re-keyed by plane and scoped to a
goal** (an active change, a target policy profile) instead of averaged into one global grade.
That satisfies the blueprint's anti-Goodhart objection ("Teams optimize numbers instead of
outcomes") *and* P7's floor discipline with the same deterministic, LLM-free engine. Because this
revises rule 07's committed universal grade (PASS/WARN/BLOCK over `status/readiness.json`), it
belongs inside R0's record content, not in a footnote (§8, §9).

### 3.3 The compatibility projection (both directions)

Plane-first must be additive, per ARC-002/003 and BR-005:

- **Installed repos speak stage numbers.** The Inspector parses them unchanged — the fixture
  matrix already requires preserving lifecycle rows, sessions, and changelogs as process truth
  (PLAN:460; matrix at PLAN:450-464). `stage: v0.4` remains a valid coordinate; the projection
  *computes* it from plane states exactly as §3.1 reads it today.
- **EPICs remain a valid view** of Change-plane units (BLUEPRINT:602) — no renaming of existing
  EPIC files, ever ("Moving a record between SoT files must not change its ID," and by extension
  a re-planed record keeps its address).
- **BR-005 discipline**: plane-first is methodology-generation-2 *semantics*. It changes no
  runtime status, no template version, no release claim. A numbered-lifecycle consumer repo and a
  plane-first repo differ in projection, not in canonical Markdown.

---

## 4. The verb surface and the action layer

**The loop is the public face; the planes sit beneath it.** The five loop stages are what the
target audience meets — the site brief leads its homepage with "the Product Management loop:
Explore → Shape → Decide → Build → Learn, with Check as a cross-cutting action"
(GEARHEARTAI_PRD_CE_V2_SITE_BRIEF.md:158-159, 273-276) and instructs that the homepage serve
those jobs "before teaching ontology or lifecycle stages" (SITE:151). The planes never need to
appear in the first-run experience at all. **Owner preference recorded 2026-08-12:** the loop
stages are the audience-facing stage vocabulary — the successor to Spark → … → Market Adoption —
and the plane names remain internal record classification. The two axes are not rivals: each loop
stage reads and writes specific planes (the "Primary plane" column below), which is what makes
`check`'s cross-plane comparisons and the context compiler work.

### 4.1 Seven verbs, one router

The blueprint's command surface (BLUEPRINT:190-205, 1888-1975) — one root, seven verbs:

| Verb | Function | Primary plane |
|---|---|---|
| `init` | scan an existing repo, establish baseline, mark extracted vs inferred | all (read) |
| `explore` | capture evidence and hypotheses; no silent accepted decisions | Evidence |
| `shape` | draft an outcome and a semantic Change Set | Intent → Change |
| `decide` | accept / reject / withdraw / deprecate / supersede, with diff + evidence + authority | Change |
| `build` | compile context pack, implement against accepted intent, trace, verify | Delivery |
| `learn` | ingest telemetry, feedback, incidents; compare reality with intent | Reality |
| `check` | conflicts, freshness, coverage, drift, goal-scoped fitness | cross-plane |

The bare root answers, recommends "two or three next actions," and routes plain language
(BLUEPRINT:1911-1919); *"Specialist commands are verbs, not separate products"* (BLUEPRINT:409).
`decide` is "the product's defining verb" (BLUEPRINT:2013-2017) — the only path by which
generated information becomes governed memory. Operational mechanics stay off the slash menu as
CLI reference verbs: `query, trace, graph, diff, as-of, migrate, sync, schema, export, doctor`
(BLUEPRINT:1977-1992).

Two alignments worth naming:

- **ARC-003 is already verb-shaped.** The accepted read-only contract — `index / check / query /
  trace`, "after v0.7 authorization" — never uses verb-surface vocabulary; but under R6
  (proposed, v0.6) it would map onto the read half of the surface: `init` (scan-and-baseline),
  `check`, and two CLI reference verbs. The alpha would thus ship the read half first — exactly
  the blast-radius discipline (§7): read verbs before write verbs (`shape`/`decide`/`build`),
  which wait on Wave 5's Change-plane contract.
- **The verbs are plane traversals.** Each verb is an action contract whose preconditions and
  effects are plane states — `learn` reads Reality and proposes into Change; `decide` is the only
  writer of accepted state. The action registry v1 proposed becomes: **kernel = seven verb
  contracts; pack = playbooks parameterizing them.**

### 4.2 The stage skills become playbooks

The blueprint's disposition is explicit: *"47 skills | Collapse | Seven verbs plus optional
registry playbooks"* (BLUEPRINT:605 — the "47" is the blueprint's own stale count; the live
registry lists 41 stage skills plus the `ghm-*` operators); *"Remove stage numbers and named
methodologies from the core command surface"* (BLUEPRINT:489); methods survive as parameters — `explore
--playbook=mom-test`, `shape --playbook=dunford-positioning` (BLUEPRINT:1999-2002) — living in a
registry (`registry/playbooks/`, BLUEPRINT:1855-1859).

What this preserves from the current system, deliberately:

- **The methods themselves.** Nothing about Dunford, Hormozi, Moore, Torres, or the stage
  know-how is deleted — each `prd-vXX-*` skill's content would re-home as a playbook keyed by
  **verb × plane** instead of stage number (mom-test → `explore`/Evidence; positioning → `shape`/Intent;
  release planning → `build`/Delivery; feedback loops → `learn`/Reality).
- **Consumes/Produces (P5)** become the playbook's machine-readable contract — which plane states
  it needs, which records it proposes. This is v1's action-registry insight, now with a home.
- **Execution modes (rule 08)** survive as the depth escape hatch: `--depth=quick|standard|deep`
  (BLUEPRINT:2005-2011), with the same "must not multiply the skill taxonomy" discipline.
- **The `ghm-*` operators** map to kernel verbs, not playbooks: gate-check → `check`;
  id-register → the Change-plane write path; harvest → `learn`; status-sync → a derived view;
  sot-builder → schema extension (kernel, rare).

The full skill-by-skill disposition map — all 50 directories, hooks, rules, and agent personas,
with per-asset richness ledgers — lives in
[`docs/v2/V2_SKILL_CONSOLIDATION_AUDIT.md`](V2_SKILL_CONSOLIDATION_AUDIT.md).

Distinct from the verbs: the blueprint's six constitutional operations — Observe, Propose,
Adjudicate, Materialize, Validate, Compile (BLUEPRINT:580-591) — are the *write-channel* model
the verbs sit on. `decide` fronts Adjudicate; `shape` fronts Propose; hooks and validators front
Validate. Keeping the two lists distinct avoids re-inflating the public noun budget.

---

## 5. The seven-layer audit, plane-first

The empirical verdicts from v1 stand — they described the live corpus, which has not changed.
What changes is each layer's v2 implication:

| # | Layer | Verdict (unchanged) | Plane-first implication |
|---|---|---|---|
| 1 | Semantic ontology | **Built** | Add `plane:` to the prefix registry (R2); merge the two edge vocabularies with plane-typed categories (R8) |
| 2 | Structural contract | **Convention** | Per-prefix entry schema declares its plane + plane-specific required fields (R7) |
| 3 | Semantic validation | **Built but dormant** | `required_edges` rules become cross-plane integrity rules (a UJ must serve Intent; a TEST must verify Delivery-or-Intent); wire at v0.7+ (§9) |
| 4 | Policy & authority | **Prose-strong, machine-weak** | Gate bundles become named policy packs; the enforcement ladder (§6) is how packs bind |
| 5 | Process & state | **Partial** | The plane flow topology (§2.0) plus the orthogonal dimensions replace stage number as the state model; truth-state matrix unchanged (R3) |
| 6 | Provenance & evidence | **Partial** | Unchanged (R9); note Evidence-plane records are provenance *carriers* — the `Asserted-By` gap concentrates on Intent-plane records |
| 7 | Execution contract | **Read designed, write deferred** | The seven verbs are the action layer; write verbs wait on the Change-plane contract (Wave 5) |

---

## 6. Enforcement: the ladder binds the policy packs

Unchanged in substance from v1 — the empirical finding stands: the ecosystem is advisory-first
with a strong deterministic measurement layer, one soft gate (`traceability-gate.sh`, which
exempts all `*.md`), fully built validators wired to nothing, and a doubly neutralized CI smoke
job (readiness.yml:37-38). The tier model:

**T0** prose principle → **T1** injected reminder → **T2** advisory check → **T3** soft gate
(ask) → **T4** hard gate (deny / CI-fail)

What plane-first adds is the *binding* story: a **policy pack** is a set of checks, each declared
at a tier with a binding point (session event · tool event · CI · `check` invocation ·
adjudication). The Wave-0B BR entries' native `Enforcement:` + `Failure disposition:` + gate-code
schema remains the template to generalize (R0's record should itself carry one). The two standing
non-goals also stand: don't push everything to T4 (advisory-first is a feature), and keep every
checker deterministic and LLM-free (rule 07; BLUEPRINT:1446).

---

## 7. What carries over from v1 unchanged

Stated compactly; the reasoning lives in v1's git history (`1afe828`) and remains valid:

- **Blast-radius budget.** No layer gets formalized without a deterministic consumer at the
  current maturity level. Read verbs (Interpret) need planes, schemas, states, provenance;
  write verbs (Act) wait for the Change-plane contract. The wave plan already sequences this.
- **Truth-state matrix.** The Inspector's eight finding states (accepted, proposed, inferred,
  ambiguous, stale, deprecated, superseded, unknown — PRD.md:118-119) are derived classifications
  over the orthogonal dimensions; each needs an operational test (R3). Plane-first doesn't change
  the states; it scopes findings ("Intent-plane conflict", "Reality-drift against Intent").
- **Provenance fields.** Record-granular `Asserted-By` (+ existing `Authority`, optional
  `Derived-From`) so `inferred` is computable (R9). The prior KG thread's U6 stays upgraded.
- **Vocabulary registry.** Now carrying more weight: it must resolve the "domain" triple-booking,
  name the planes publicly, and hold the public-noun budget line (the blueprint's own concept
  budget is 4–5 nouns; five plane names + verbs + packs must be counted honestly, §10 Q2).
- **Anti-scope.** No OWL/RDF, no graph DB (SQLite stays a disposable projection, ARC-001), no
  universal ontology, no LLM-judged validation, no deletion of the calibrated 1–5 confidence
  tiers, no new agent personas as navigation (BLUEPRINT:3260).

---

## 8. The v1 tensions, as the direction would resolve them (contingent on R0)

| Tension (v1 §7) | Plane-first resolution | Owner decision still needed? |
|---|---|---|
| Gates in kernel vs removed | Machinery = kernel policy engine; bundles = policy packs; ordering = journey docs (§3.2) | R0 records it |
| EPIC vs Change Set | EPIC = PM pack's view of a Change-plane unit; existing EPICs keep IDs (§3.3, A6) | At v0.7, choose the authoring surface |
| Readiness vs fitness | Same engine, re-keyed per plane and goal-scoped; no universal grade (§3.2) | **Yes** — a material revision of rule 07's universal grade; fold into R0's record content |
| Stage skills vs verb surface | Collapse to playbooks behind seven verbs; methods and modes survive (§4.2) | R0 records it |
| Record form (frontmatter vs `- **Field:**`) | Unchanged — v0.6 entry-schema decision, informed by Wave 1 fixtures (R7) | At v0.6 |
| Numeric confidence vs basis+band | Unchanged — tiers are calibrated bands; translate, don't delete | No |
| Five product names / noun budget / "observed-inferred" overloads | Vocabulary registry (R1), now also owning the plane/domain naming | **Yes** (naming gate) |
| Root `SoT/` vs `product/SoT/` | Unchanged — alpha inspects in place (PLAN:148); plane is record-level, so no relocation is ever *required* by plane-first | Deferred by plan |
| Build vs Deliver verb | Now concrete: the verb set ships `build` (BLUEPRINT:1904); renaming to `deliver` is a one-word registry decision | **Yes** (PLAN:585) |

---

## 9. Staged recommendations (re-sequenced for plane-first)

**R0 — Record the direction (the gate for everything else).** An owner-confirmed BR/ARC record
(Wave-0B style, with Enforcement + Failure disposition + gate code) stating: planes are the
primary ontology; the numbered lifecycle becomes a compatibility projection + guided journey;
stage skills collapse to playbooks behind the verb surface; the PM loop (Explore → Shape →
Decide → Build → Learn, Check cross-cutting) is the audience-facing stage vocabulary while the
planes remain internal structure; readiness re-keys per plane into goal-scoped views (revising
rule 07's universal grade). Touch list at acceptance: build plan
(PLAN:223's "single gate system" sentence), rules 01/05/07/08 (stage-number references), README
lifecycle table. Until R0 lands, everything below is contingent.

**Legal now (pre-v0.2, definition only):**

| # | What | Consumer |
|---|---|---|
| R1 | Vocabulary registry — candidate inventory and collision analysis (the "domain" triple-booking, noun-budget accounting). Canonical *selection* of public names is a v0.3 naming-gate decision the registry records, not a pre-v0.2 act | naming gate; EVAL defect hunt |
| R2 | `plane:` key on every `id_prefixes:` entry in domain-profile.yaml, with the eight ambiguity resolutions (A1–A8) recorded as comments or entry-level overrides | readiness, validators, Inspector — all already read this file |
| R3 | Truth-state matrix (8 states × operational tests × transition authority) | Inspector classification spec |
| R4 | Kernel/pack boundary memo — now concretely: kernel primitives (§2.3) vs PM pack (prefixes, playbooks, journey, policy packs) | BR-001 governance; packaging (ARC-004) |

**At v0.6 Architecture (contracts land, PLAN:230-233):**

| # | What | Consumer |
|---|---|---|
| R5 | Gate→policy-pack spec: each GATE_REQUIREMENTS row + gate-criteria.md detail rewritten as a named per-plane policy profile; reconciles the three hand-synced copies into one source | `check --policy=`; readiness re-keying |
| R6 | Verb-surface spec: map ARC-003's `index/check/query/trace` into the verb set; declare the read/write split; playbook contract format (Consumes/Produces as plane states) | Inspector; future skill migration |
| R7 | Per-prefix entry schema (plane + required fields), reconciled against Wave 1 fixture matrix | Inspector parser/validator |
| R8 | Edge-vocabulary merge (live 10 + proposed 18, BLUEPRINT:962-981) with plane-typed categories; give `designed-for` (the plane-less "Experience" category) a declared home | Inspector; `validate-edges` v2 |
| R9 | Provenance fields (`Asserted-By`, keep `Authority`, optional `Derived-From`) | Inspector `inferred` test |

**At v0.7+ (runtime, EPIC-gated):** wire the dormant validators as cross-plane integrity checks
(repo profile only; seeds stay empty per ARC-004); Inspector implements plane-scoped state
classification with provenance-to-line; expose readiness dimensions as named competency queries
under `check` (the prior thread's U3). **Wave 5 (held):** the Change-plane contract — the write
verbs' preconditions, adjudication receipts, postcondition verification.

---

## 10. Open questions for the owner

1. **Plane naming.** Keep the blueprint's "plane" internally and publicly? Or brand the five as
   "domains" and rename the colliding uses (domain packs → vertical packs; domain-profile →
   method-profile)? R1 inventories the candidates and collisions; the v0.3 naming gate picks
   exactly one.
2. **Noun budget accounting.** Do the five plane names count against the 4–5 public-noun budget
   (BLUEPRINT:619-625 vs 2525), or are they structure beneath the nouns? The blueprint's kill
   criterion — "users cannot get value before learning the ontology" — suggests planes should be
   *invisible* in the first-run experience (`init`/`check` work without teaching them).
   **Owner preference recorded 2026-08-12 (pending R0):** resolved in the invisible direction —
   the PM loop stages are the public vocabulary; plane names stay internal and off the noun
   budget.
3. **"More domains."** The reviewed baseline is five planes, and **BR-001 governs any
   expansion**: a candidate division serving a non-PM methodology is a separately governed method
   pack, never a new plane (gate code `V2_SCOPE_EXPANSION`). For PM-internal candidates, the
   blueprint's admission heuristic ("serves at least three materially different domains,"
   BLUEPRINT:1645 — research input, not authority) argues most new material enters as namespaced
   extensions rather than planes. Which PM-internal candidates, if any, does the owner see?
4. **The A5/A8 splits.** KPI target vs reading, and pre- vs post-launch CFD: split the prefixes,
   or carry plane-on-entry overrides? (Affects R2's shape.)
5. **EPIC disposition timing.** Change-plane citizen now (R0 language) or at v0.7 when the
   authoring surface is chosen?
6. **This document's standing.** Accept (with R0) as v0.2 gate evidence, or hold as input? And
   should the external research report be sanitized into `temp/v0.1-intake/` as reviewable
   evidence?

---

## 11. The prior KG thread under plane-first

| Upgrade | Status | Plane-first note |
|---|---|---|
| U1 valid-time | Built | Kernel state dimension; unchanged |
| U2 required edges | Built, dormant | Becomes the cross-plane integrity engine — wire at v0.7+ |
| U3 competency queries | Partial | Named queries under `check`; cheap |
| U4 six-layer eval | Greenfield | The pack's eval suite; now plane-scoped (per-plane health + cross-plane drift) |
| U5 retrieval routes | Low priority | The context compiler is kernel (BLUEPRINT:1570); still Wave 3/6 |
| U6 claim modeling | **Upgraded** | Record-level provenance, concentrated on Intent-plane records (R9) |
| U7 confidence gate | Designed | A policy-pack check on the ladder (T2 → promotion path) |

---

## Provenance of this document

**v2 (this revision), 2026-08-12:** reworked plane-first on owner direction, from a three-agent
extraction pass over the blueprint (verb surface BLUEPRINT:190-205/1888-1975; plane model
BLUEPRINT:209-215/666-756; gate translation vs scripts/_readiness/stage.py:47-106 and
gate-criteria.md) plus the v1 corpus audit. **v1, 2026-08-12 (commit `1afe828`):** synthesized
from the external deep-research report (not vendored — third-party consulting context), the two
v2 input docs, and direct file-level inspection of registry, entries, hooks, validators, and CI
at commit `11297db`; all enforcement-spectrum claims verified against script source. Input-doc
tensions cite the documents' own lines and are reportable defects per the evaluation protocol.

| Version | Date | Change |
|---|---|---|
| 1 | 2026-08-12 | Initial: layer-first audit; plane restructure treated as open tension |
| 2 | 2026-08-12 | Domain-first rework per owner direction: planes primary, lifecycle as projection, skills as playbooks; R0 added |
| 2.1 | 2026-08-12 | Two-axis clarification per owner preference: the PM loop (Explore → Shape → Decide → Build → Learn, Check cross-cutting) is the audience-facing stage vocabulary; planes are internal structure, invisible at first run |
| 2.2 | 2026-08-13 | Surface layer added (§2.4, owner-raised): front door / views / deliverables as derived, non-canonical human interface; Review deliverables = the human half of `decide`; as-of + supersede as backtracking's two faces |
