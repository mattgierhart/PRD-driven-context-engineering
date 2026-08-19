---
title: "The Key Moments — v2's Deliverable Canon & Design Briefing"
version: 1.2
status: "Research input — not accepted product truth (PRD.md authority order, item 7)"
purpose: "The canon of key moments (deliverables where clarity of expression matters most) inside the v2 ontology — now carrying the visual-expression direction from the 2026-08-13 design research, written as a self-contained briefing a design session executes in Claude Code."
date: 2026-08-13
origin: "Owner-articulated 2026-08-13 from 20 years of enterprise product management; visual direction from the commissioned design-research report (vendored at docs/v2/V2_KEY_MOMENTS_VISUAL_RESEARCH.md)."
companions:
  - "docs/v2/V2_KEY_MOMENTS_VISUAL_RESEARCH.md (the full design-research report with citations — read for any moment you design)"
  - "docs/v2/ECOSYSTEM_ONTOLOGY.md §2.4 (the surface layer)"
  - "docs/v2/DELIVERABLES_CONCEPT.md (the deliverable mechanism: two species, round-trip loop)"
  - "docs/v2/V2_SKILL_CONSOLIDATION_AUDIT.md (the playbook/policy-pack inventory these moments draw on)"
scope_guard: "Defines the canon's structure, ontology placement, and visual direction. No SoT IDs minted; the per-moment question banks and emitted-record shapes remain for the question-research session (§4)."
---

# The Key Moments — v2's Deliverable Canon

> **Thesis**: A product's development has a small number of moments where *clarity of expression
> is the product* — where a team either sees the problem, the person, the model, the journey, the
> risk, the sequence, and the launch sharply, or ships the blur. v2 gives each moment one
> structural home: a **deliverable** (the human face — where judgment is expressed and captured),
> a **policy pack** (the machine face — where completeness is checked deterministically), and the
> **playbooks** that prepare the material. The moment is the unit the user remembers; the planes
> do the bookkeeping underneath.

---

## 0. Standing and the one structural rule

Research input, contingent on R0. The owner named the seven moments below on 2026-08-13; his
articulations are quoted verbatim as each moment's charter — they are the requirements the future
question-research session must satisfy, not placeholders.

**The rule that makes a moment a moment** (and not just another page): it must pass the
deliverable value test already in [`DELIVERABLES_CONCEPT.md`](DELIVERABLES_CONCEPT.md) §6.0 — it
*extracts a decision or captures the right acknowledgement*. Every moment below terminates in an
adjudication: something the human ranks, chooses, accepts, or signs. Anything that doesn't is a
view, not a moment.

**How to use this document (for the design session).** This briefing is written to be handed to
a design-focused Claude session working in Claude Code. Your deliverables are **flat,
self-contained HTML template files** — opened from `file://`, no server, no build step, no
external fonts/CDNs/libraries — one per moment, plus the shared family shell (§2.1). Design the
*templates with slots*, per §2's living-template architecture: real data arrives later via
deterministic pull scripts, so every visual element must be specified against the moment's data
binding and its n=0 / n=1 / n-many / overflow states. Build in the §2.3 stage order (family
shell first), hold the §2.2 genre departures as decided, and treat each moment's **Visual
expression** block below as the direction — the full argument and citations for every choice are
in [`V2_KEY_MOMENTS_VISUAL_RESEARCH.md`](V2_KEY_MOMENTS_VISUAL_RESEARCH.md), which you should
read for any moment before designing it. Open design questions are listed in §4 — surface them,
don't silently resolve them.

Each moment entry declares:

- **Charter** — the owner's articulation, verbatim.
- **Loop position** — which verb(s) prepare it, which verb it terminates in (almost always
  `decide`).
- **Renders / Emits** — planes read for the pre-fill; records the completed deliverable emits.
- **Species mix** — Review (pre-filled, judge) vs Intake (guided authoring), per
  DELIVERABLES_CONCEPT §3.
- **Clarity anchor** — the single expression that must be crisp; the artifact the moment exists
  to produce.
- **Machine face** — the policy pack(s) that check the moment's completeness. A moment's machine
  face MAY compose several audit-inventory packs into one named check profile; where a named
  pack is new (not yet in the audit's roster), it is flagged.
- **Feeds from** — the distilled-experience assets (richness ledgers) that become the moment's
  preparation playbooks.
- **Visual expression** — the researched genre direction for the flat-HTML template: primary
  genre, what to steal from named exemplars, the signature interaction, and the load-bearing
  empty/overflow states. (Added v1.2 from the design research.)

---

## 1. The canon

### M1 · Problem Framing

- **Charter**: *"clarity of what problem we are trying to solve."*
- **Loop position**: `explore` prepares (evidence gathering, tiering); terminates in `decide`
  (accept the problem statement).
- **Renders**: Evidence (tiered pain records, each with its upgrade condition). **Emits**: the
  accepted problem statement (Intent) + evidence acknowledgements + the adjudication record.
- **Species mix**: Review-dominant — the agent drafts; the human validates the "who," ranks the
  pains, rejects speculation, accepts the statement.
- **Clarity anchor**: the one-sentence spark formula — *[Who] faces [pain] costing [amount]
  because [root cause]; [trigger] creates urgency; current solutions [gap]* — with every clause
  citing evidence.
- **Machine face**: `spark-exit` pack (evidence-tier floor, gap gate, testability checks).
- **Feeds from**: problem-framing and pain-to-value playbooks, five-element problem table (incl.
  "What's impossible" / "Why now"), evidence tiers with tier-5 reject, 48-hour findability test,
  gap-typed research recipes.
- **Visual expression**: the **annotated, evidence-footnoted sentence** — the spark sentence set
  large as the hero, each clause an interactive span opening its evidence card (Genius-style
  close reading; tier-5 speculation renders struck-through, legal-redline style). Steal: GRADE's
  tier dot per citation; IPCC's "lead with what you know" register — confident clauses plain,
  weak ones honestly hedged. Signature interaction: click a clause → evidence card; drag-rank
  the pains; "Accept problem statement" with full ceremony. States: a clause with no evidence
  renders "needs Explore" in amber (a gap, not an error). *Fallback (Medium confidence,
  prototype-test it): if authoring speed suffers, the five-element table takes over as hero.*
  Register: quietly authoritative — *weighted*, not dramatic.

### M2 · Persona

- **Charter**: *"Who are we solving this problem for, what are their pain points."*
- **Loop position**: `explore` (interviews) → `shape` (synthesis) → `decide` (accept ≤5 personas,
  incl. the negative persona).
- **Renders**: Evidence (interview records, segment signals). **Emits**: PER- records with their
  evidence links; the "not for" boundary as Intent.
- **Species mix**: Review (rank/merge candidate personas; confirm behavioral claims against
  evidence) with an Intake path for founder-known segments.
- **Clarity anchor**: the persona card — behavioral, evidence-linked, with pains ranked — plus
  the **negative persona** ("we will not chase this buyer").
- **Machine face**: persona rules inside the `experience-coverage` pack (evidence-requirements
  matrix, 5-max cap, traceability).
- **Feeds from**: behavioral-persona playbook, mom-test confidence ladder, negative-persona
  concept.
- **Visual expression**: the **behavioral persona card set** (Cooper/Goodwin goals-over-
  demographics; JTBD as a field *on* the card, not a rival genre) — ≤5 cards in a row, each with
  a name, one behavioral sentence, and ranked pains; the **negative persona** as a deliberately
  cool, muted "not for" card — a line drawn. Steal: Mom-Test confidence indicators per claim
  (observed behavior vs flattering interview). Signature interaction: **drag-to-merge** against
  a visible "n of 5" cap counter; per-claim accept/reject against evidence. States: >5 candidates
  forces merge-or-cut; an unevidenced claim renders amber "unverified" and blocks accept; n=1
  still shows the negative-persona slot. Register: warm but disciplined — every warm detail
  earns its place with evidence.

### M3 · Commercial Model

- **Charter**: *"What is the engagement model with this product or service. Is this something
  they use frequently, it plugs into an existing ecosystem, do they switch from something to the
  product we are building and even tactical things like pricing."*
- **Loop position**: `explore` (landscape, moat/switching, WTP) → `shape` (outcome metrics,
  pricing) → `decide` (the product-type + engagement-model adjudication — the walkthrough's
  Scene 4).
- **Renders**: Evidence (competitive records, switching-cost inventory, WTP signals) + Intent
  drafts. **Emits**: the engagement-model decision (type classification + inherited guardrails,
  as a Change record), pricing rules, KPI targets, moat/targeting rules — all Intent.
- **Species mix**: Review-dominant — types side by side with evidence and guardrail previews;
  pricing locked only behind the WTP gate.
- **Clarity anchor**: the **engagement-model statement**: how this product lives in the
  customer's world — frequency of use, ecosystem it plugs into, what it replaces and what the
  switch costs — plus the type and the price. (The owner's framing here is *broader than
  pricing* and should drive the expression: the engagement model is the sentence; pricing is a
  clause.)
- **Machine face**: `product-type-guardrails` + `wtp-before-price-lock` + `kpi-gate-linkage`.
- **Feeds from**: six-type taxonomy with GTM constraints matrix, anti-metrics/anti-models per
  type, quantified switching-cost inventory + behavioral-inertia analysis ("your real competitor
  is a spreadsheet"), SMB-penalty calculation, WTP hierarchy.
- **Visual expression**: the **engagement-model statement as hero**, backed by three under-served
  visuals: a **frequency strip** (day/week-in-the-life usage band), an **ecosystem diagram**
  (named systems only — no decorative clouds), and a **switching-cost bar** (length = quantified
  switch cost; the honest reckoning with inertia, spreadsheet included). Type choice uses the
  shared comparison component — only differing attributes shown, exactly one recommended column
  highlighted (NN/g). **Pricing is visibly demoted to a single locked clause**: a padlock that
  opens only when WTP evidence exists — the owner's "pricing is a clause" premise enforced by
  the design itself. States: missing frequency → "usage frequency: unknown (Explore)";
  unquantified switching cost → "not yet quantified". Register: confident and concrete; the
  price clause deliberately understated.

### M4 · User Journeys

- **Charter**: *"What key missions does a user have when they use this tool, what steps per
  mission, how many screens are there, what moments of delight exist in the user journey vs what
  parts should feel very utilitarian. What key features that the user would recognize will make
  this product attractive."*
- **Loop position**: `shape` (the experience-design pipeline: personas → journeys → screens →
  prototype) → `decide` (coverage + scope sign-off; the money shot).
- **Renders**: Intent (features, constraints) + Delivery drafts (journeys, screens). **Emits**:
  UJ/SCR records, the recognizable-feature cut (FEA parity/delta), the delight-vs-utilitarian
  markings, the scope acceptance.
- **Species mix**: both — the journey builder is the canonical Intake deliverable
  (DELIVERABLES_CONCEPT §6.2); the coverage/scope sign-off is Review.
- **Clarity anchor**: the **journey map with emotional temperature** — missions → steps →
  screens, with delight moments and deliberately utilitarian stretches marked as design
  decisions, and the "money shot" (the screen that sells the product) named. The
  delight-vs-utilitarian axis rhymes with impeccable's surface modes (Persuade vs Operate) —
  a proven expression pattern to borrow at research time.
- **Machine face**: `experience-coverage` (feature↔journey↔screen bidirectional matrices,
  dead-end check, screen caps) + `mvp-scope-integrity`.
- **Feeds from**: journey-mapping, screen-flow, and feature-value-mapping playbooks,
  emotional-beat mapping, money-shot concept, <15-page cap, coverage matrices.
- **Visual expression**: a **journey map with an emotional-temperature band on a story-map
  backbone** — missions across the top (Patton's backbone), steps and screens hanging below,
  the emotion band as a first-class row beneath (Kalbach/NN/g curve), the money shot elevated
  as the page's emotional peak. Delight ▲ and utilitarian ▬ stretches are *labeled decisions*,
  not moods; emotion is dual-encoded (height + label, never color alone), with assumption-based
  emotion marked as hypothesis. **One template, two explicit modes** — a build (Intake) mode and
  a decide (Review) mode sharing one data model — resolving this moment's two-species tension;
  if forced to one, the decide view wins. States: >15 screens = cap breach blocking scope
  sign-off; a mission with 0 screens = dead-end flag; no money shot named = a visible absence
  flag (it's a human declaration no machine check can make). Register: the page *allowed*
  warmth and drama — the band is the point. Anti-pattern to design against: the wall-sized map
  that becomes wallpaper.

### M5 · Technology & Development Risk

- **Charter**: *"how will we build this, what architecture, where do we need to invest to ensure
  it's a good experience vs what areas should we optimize cost or complexity. What market and
  user behavior risks are there."*
- **Loop position**: `explore` (red-team interview — deliberately covering market and behavior
  risks, not just technical) → `shape` (architecture and contract drafting) → `decide`
  (build/buy/reuse; risk dispositions; architecture sign-off).
- **Renders**: Intent (features, constraints) + Evidence (brownfield assets, risk observations).
  **Emits**: TECH decisions with rationale, the risk register with owner dispositions
  (accept/mitigate + early-warning signals), ARC records with conformance rules, the API-/DBT-
  contract drafts the sign-off covers, and the **invest-vs-optimize map** as explicit Intent.
- **Species mix**: Review — risk ranking (DELIVERABLES_CONCEPT §6.1) and architecture map
  sign-off (§6.3) are the two already-designed deliverables in this moment.
- **Clarity anchor**: the invest-vs-optimize map — where quality is bought and where cost is
  deliberately optimized — sitting on top of the risk register and the architecture picture.
- **Machine face**: `risk-register` + `tech-decisions` + `contract-closure` (every high risk has
  a response; no orphan decisions).
- **Feeds from**: red-team-interview, build-buy-reuse, architecture-adr, and api-contracts
  playbooks; risk question bank with status-weighted scoring; the 80% brownfield rule; the MVP
  cost stance ("$200–300/mo with good DX beats $50/mo with constant ops"); conformance-rule
  mechanism.
- **Visual expression** *(the flagship departure)*: **no 5×5 heat map anywhere** — Cox (2008)
  showed typical risk matrices correctly compare only a small fraction (e.g., under 10%) of
  randomly selected hazard pairs and can misrank quantitatively larger risks; Hubbard's chapter
  title is "Worse Than Useless." Instead: the
  **invest-vs-optimize map as hero** (a deliberate-tradeoff quadrant — where quality is bought
  vs where cost is deliberately optimized; if everything says "invest," it's a wish list), over
  a **sortable, quantified risk register** ranked by the computed status-weighted score, with a
  **tornado view** for which risk moves the outcome most. Build/buy/reuse dispositions render as
  ADR-style cards (Nygard: Status/Context/Decision/Consequences). Severity is never color-only
  (rank position + label + magnitude). States: a high risk without a response = red flag
  blocking sign-off; missing exposure → still ranks, bar marked "qualitative"; legible at n=50
  (top-N + collapsed rest). Register: **the most sober page in the system** — gravity from
  honesty, not red cells.

### M6 · Build Sequencing

- **Charter**: *"What is the sequencing of build and why. How do we break the development cycle
  into bodies of work that can emphasize testing (both functional and non-functional) and
  getting a beta in the hands of users fast."*
- **Loop position**: `build` (work packaging) → `decide` (accept the sequence and its rationale).
- **Renders**: Delivery (contracts, dependency DAG) + Intent (scope boundary). **Emits**: the
  work-unit sequence as Change-plane units, the test strategy (functional + non-functional
  emphasis per unit), and the **beta gate** — the explicitly named earliest point real users
  touch the product.
- **Species mix**: Review — the sequence is drafted mechanically from the dependency graph; the
  human judges the *why* (what's first and what that ordering buys, where beta lands, what risk
  each unit retires).
- **Clarity anchor**: the sequencing map — bodies of work in order, each annotated with *why
  this order* (risk retired, dependency unlocked, test emphasis) and the beta line drawn on it.
- **Machine face**: `build-readiness` (all specs assigned, DAG sound, measurable deliverables —
  sourced from the epic-scoping quality gates in the v07 ledger; now added to the audit's pack
  roster) + `test-coverage`.
- **Feeds from**: work-unit sizing calibration (3–5 APIs / 2–4 tables / 3–7 units per MVP),
  dependency patterns, test-first discipline and the 60/30/10 pyramid, release-engineering
  phased-rollout patterns.
- **Visual expression**: a **pre-computed dependency DAG**, left-to-right, with the **beta line**
  drawn vertically across it — everything left of the line ships before real users touch it
  (Patton's walking skeleton as the beta's ancestor). Each unit annotated with *why this order*:
  risk retired, dependency unlocked, test emphasis. **Gantt rejected** — dates manufacture false
  precision and read as commitments (Bastow/ProdPad, Cagan); order ≠ date. Layout is Sugiyama
  layered drawing (the Graphviz `dot` standard) **computed in the pull script and shipped as
  coordinates** — the template only draws inline SVG. Signature interaction: **moving the beta
  line** — the earliest-user-contact decision. States: a dependency cycle surfaces its reversed
  edge as "review this dependency"; large graphs collapse into phases; zero hairballs at n=20
  is the benchmark. Register: purposeful, engineering-calm; mild satisfaction at the beta line.

### M7 · Go to Market

- **Charter**: *"how will we launch, what are the goals of launch, how do we get the first
  users, what onboarding needs are there. what distribution channels do we need to consider. How
  do we capture feedback both in analytics and direct user response."*
- **Loop position**: `shape` (positioning, offer, launch goals) → `decide` (channel mix, launch
  strategy) → `build` (execution artifacts, onboarding, instrumentation).
- **Renders**: Intent (positioning candidates, type guardrails, KPI targets) + Evidence
  (channel economics). **Emits**: positioning + offer decisions, the channel-mix decision with
  fit rationale, launch goals as Intent, onboarding needs and operational readiness (runbooks)
  as Delivery scope, and the **feedback contract** — which analytics (Reality instrumentation)
  and which direct channels will exist at launch. (Post-launch direct feedback straddles
  Evidence/Reality — the ontology's A8 ambiguity, owner call pending; this moment inherits
  whichever reading A8 settles on.)
- **Species mix**: Review (channel mix against ORB fit floors; positioning against the
  guardrails) with Intake elements (onboarding-needs capture).
- **Clarity anchor**: the launch one-pager — goals, first-users plan, channel mix with reasons,
  onboarding needs, and the feedback contract, each traceable to the engagement model (M3).
- **Machine face**: `gtm-coherence` (the reconciliation table — positioning, offer, channels,
  metrics must not contradict) + `launch-readiness`.
- **Feeds from**: ORB allocation principles + product-type→channel mapping, positioning/offer
  playbooks, channel-economics reference (CAC tiers, $500×3 testing cadence), feedback→ID
  circulation, lead-lifecycle playbook, ops-runbooks + slo-error-budget (operational readiness),
  and the AEO/alternatives/outreach execution playbooks.
- **Visual expression**: a **launch one-pager with the reconciliation table as its spine** —
  PR/FAQ-discipline narrative frame (goals, first-users plan) over a table putting positioning ·
  offer · channels · metrics in columns with contradiction flags; **the all-green table is the
  "we are coherent" moment**. Channels use the shared comparison component against fit floors
  (below-floor channels flagged and excluded by default); any timeline renders as
  **Now/Next/Later confidence horizons, never dates**; the positioning canvas (Dunford) is a
  drill-in, with every message tracing back to it and to M3's engagement model. The feedback
  contract reads as a promise, not a footnote. States: no channels evaluated → "(Shape)"; a
  reconciliation contradiction (e.g., enterprise positioning + self-serve channel) = red flag
  blocking launch sign-off; missing feedback contract = "launching blind" warning. Register:
  energized but accountable — tempered by the sober table.

### M8 · Launch Verdict *(proposed addition — the owner's list stops at launch; the loop doesn't)*

- **Rationale**: M7 launches; something must then *judge* the launch — the corpus already
  contains a complete, deterministic adjudicator for exactly this (the launch-validation rubric:
  go/no-go thresholds, A–F grading, pivot-vs-kill taxonomy, week-1 early warnings), and the
  ontology gives it a natural home as the loop-closer.
- **Charter (proposed)**: what did reality teach, and what do we do — scale, iterate, pivot, or
  kill — with the same clarity discipline as every other moment.
- **Loop position**: `learn` (drift view: reality vs the M3/M7 targets) → `decide`.
- **Renders**: Reality (measured outcomes; feedback records per the A8 reading M7 inherits)
  against Intent (KPI targets).
  **Emits**: the verdict as a Change record with its evidence; superseded intent where the
  verdict demands it; the next cycle's opening evidence.
- **Species mix**: Review — the scorecard arrives computed; the human owns the verdict.
- **Clarity anchor**: the launch scorecard — targets vs actuals, the grade, the verdict, and the
  reasoning that will stop a future session from re-litigating it.
- **Machine face**: `launch-validation`.
- **Feeds from**: validation-criteria rubric, drift baselines, adoption-stage diagnostic.
- **Visual expression**: a **target-vs-actual scorecard of bullet graphs** (Few — one per KPI:
  actual bar, target marker, qualitative bands; gauges and speedometers explicitly rejected)
  with a computed drift column, one **grade** (OKR-style bands, re:Work's 0.6–0.7 sweet spot,
  dual-encoded), and the **verdict as the hero** — scale / iterate / pivot / kill, stated
  plainly. This is the **heaviest ceremony in the system**: a literal-verb button per verdict
  ("Record verdict: Pivot"), signer + immutable timestamp, and **recorded reasoning**
  (ADR-style) so no future session re-litigates it — a dashboard with no verdict is the
  anti-pattern. States: target without actual = "not yet measured" (never a zero); missing
  target = ungradeable, flagged; grade "provisional" until a reporting threshold of KPIs is met.
  Register: consequential and honest — the reckoning; the emotional bookend to M1's thesis;
  deliberate plainness where results are bad, because fairness is what prevents re-litigation.

---

## 2. The expression architecture — living templates (the Graphify pattern)

**Owner direction (2026-08-13)**: each moment's HTML expression takes the
[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) approach. Graphify's contract:
one command runs a deterministic, LLM-free extraction and emits three artifacts — `graph.json`
(the full data model, "query it anytime without re-reading your files"), `graph.html` (a bespoke,
clickable visual), and a markdown report — with every edge provenance-tagged
`EXTRACTED`/`INFERRED`. This repo has borrowed the pattern once already: the devgraph is
"Graphify-style AST parsing, deterministic and free" (domain-profile.yaml) and its bridge edges
carry the same confidence tags. v2 generalizes it to every key moment:

| Artifact | Job | Graphify analog |
|---|---|---|
| **The data pull** (`<moment>.json`) | A deterministic script resolves the moment's *Renders* list through the registry — the records, their edges, their state dimensions (lifecycle, authority, freshness, confidence), each fact carrying its record ID and provenance tag | `graph.json` |
| **The bespoke visual** (`<moment>.html`) | A *designed-per-moment* template hydrated from the JSON — the visual layer is real design work, unique to the moment (a journey map does not look like a risk register); template design is in the research session's scope (§4) | `graph.html` |
| **The emit path** | Input mode captures judgment and emits plane records — the DELIVERABLES_CONCEPT §4–5 round-trip; this half is ours, Graphify has no write side | — |

Four rules govern the pattern:

1. **Template and data never mix.** The template is designed once and versioned; the data is
   regenerated constantly. Today's hand-authored companion pages are the templates' ancestors —
   v2 splits their content out as data. CLAUDE.md's conflict rule ("markdown wins; fix the HTML")
   becomes automatic: you don't fix a stale page, you rebuild it.
2. **The pull script is deterministic and LLM-free** — rule 07's scorer discipline extended to
   surfaces. Registry-driven record selection, edge traversal, state stamps. Some pulls are
   *computed*, not just selected — coverage matrices, the dependency DAG, drift deltas — exactly
   the devgraph/readiness precedent, still deterministic. **All expensive layout is pre-computed
   in the pull script** (the no-library constraint rules out force-directed graphs and charting
   libraries): Sugiyama layered coordinates for DAGs, emotion-band coordinates for journey maps,
   shipped as x/y in the JSON — the template only draws inline SVG.
3. **Rebuilds are loop-driven, not manual.** Three loops carry the architecture:
   - **The rebuild loop** — any verb pass that writes records a moment renders marks that
     surface stale and re-runs its pull (affected-based, like Graphify's incremental rebuilds).
     Enforcement climbs the ladder: a T1 reminder at first, a CI drift gate later — the same
     source-vs-generated discipline as the plugin-sync check.
   - **The render loop** — templates iterate over record sets: five risks or fifty, same
     template. The page scales by data, never by editing HTML.
   - **The adjudication loop** — render → judge on the page → emit → planes update → rebuild
     shows the new accepted state. Each revolution of the PM loop refreshes the canon's
     surfaces, so session 50 opens current pages, not stale ones.
4. **Staleness is detectable.** The page embeds its data-model fingerprint; `check` compares it
   against a fresh pull. A stale surface is a finding, not a surprise.

**Per-moment pulls and rebuild triggers** (derived from each moment's Renders list; the research
session refines the exact record selections):

| Moment | Data pull (records + computed fields) | Rebuilt when |
|---|---|---|
| M1 | Tiered evidence + problem-statement draft + upgrade conditions | `explore`/`learn` write evidence |
| M2 | Interview records, persona candidates + evidence links | `explore`/`shape` |
| M3 | Competitive records, switching-cost inventory, WTP signals, engagement-model draft (incl. `frequency` field), type candidates + guardrail previews | `explore`/`shape`/`decide` |
| M4 | Features, journey/screen drafts + **computed** coverage matrices | `shape` |
| M5 | Risk register + **computed** status-weighted scores, brownfield assets, architecture/contract drafts | `explore`/`shape` |
| M6 | **Computed** dependency DAG, unit sizing, test-coverage map, beta criteria | `shape`/`build` |
| M7 | Positioning/offer/channel candidates + fit scores, launch goals, feedback contract | `shape`/`decide`/`build` |
| M8 | KPI targets vs Reality actuals (**computed** drift), scorecard grade | `learn` |

**Alpha-legality note**: the pull scripts are read-only by construction — exactly ARC-003's
`index`/`query` behavior — so the JSON + HTML halves of every moment are legal in the read-only
alpha. The emit half rides Wave 5's Change-plane contract, as the surface layer already declares.

### 2.1 The one-family system (from the design research; the family lives in chrome, not heroes)

The eight pages must feel like one family while each genre stays distinct. Shared components,
all buildable single-file:

- **Tokens**: system font stack (no web fonts — `file://`), a ~6-step type scale with each
  page's hero at the top step, an 8px grid, CSS grid for every matrix so tables scale by data.
  One accent color per loop verb so a page signals where in the loop it sits — **muted on M5**,
  whose sobriety must not be drowned by chrome. Severity and grade encodings are always
  dual-channel (position/label + color, WCAG).
- **The provenance chip** — the family signature, on every fact of all eight pages: the typed ID
  always visible; evidence tier (GRADE-style four-level dot) and confidence (IPCC's five
  qualifiers) revealed on hover/click, C2PA-style badge-to-inspect. Print renders chips as
  footnotes.
- **The staleness stamp** — "data as of ⟲" top-right on every page, backed by the embedded
  data-model fingerprint (§2 rule 4); a mismatch renders a visible "may be out of date —
  rebuild" banner.
- **The navigation rail** — a persistent, ordered M1→M8 rail, each moment with its own freshness
  dot, so the eight read as one narrative arc from thesis (M1) to reckoning (M8).
- **The sign-off ceremony** — one shared grammar, weight-calibrated: a reserved signal color for
  the commit action; **literal-verb buttons, never "OK"** (Carbon); staged friction proportional
  to consequence (M8's kill/pivot heaviest, M2's persona-accept lighter); signer attribution +
  immutable timestamp; and **binding to a data state** — like GitHub dismissing PR approval on a
  new commit, a sign-off goes stale if its underlying records change (re-open tuning is an open
  question, §4). Acknowledgement ("I've seen this", low friction) and decision ("I choose",
  full ceremony) are visually distinct (Material's confirmation-vs-acknowledgement split).
- **The comparison component** — shared by M3 (types), M5 (build/buy), M7 (channels): columns =
  options, rows = only attributes that *differ* (NN/g), exactly one recommended column
  highlighted, weighted drill-ins traceable.
- **Print/PDF** expands all detail-on-demand; **light/dark** via custom properties +
  `currentColor` SVG.

Named family tensions (design with them, don't paper over): M4's two-mode seam; M5's sobriety vs
the verb accents; the ink-density gulf between the sentence-heroes (M1/M3) and the data-dense
pages (M5/M6) — the shared chrome carries the family so hero zones can diverge sharply.

### 2.2 Accepted genre departures (decided by the research, adopted by this briefing)

| Departure | Ruling | Confidence |
|---|---|---|
| **No 5×5 risk heat map** (M5) | Sortable quantified register + tornado ranking. Cox 2008 (*Risk Analysis*): typical matrices correctly compare only a small fraction (e.g., <10%) of randomly selected hazard pairs, and can misrank; Hubbard: "Worse Than Useless." If the audience demands one, it may exist only as a clearly-labeled non-authoritative overview with the Cox caveat — never driving rank | Very High |
| **No date-based Gantt** (M6) | Dependency DAG carries the *why*; order ≠ date. Now/Next/Later handles any M7 timeline | Very High |
| **No canvas as M1's hero** | The annotated sentence is the hero; the five-element table is the fallback if authoring speed suffers — prototype-test with 3–5 PMs | Medium |

### 2.3 Build staging (flat HTML files, in this order)

1. **The family shell first** — provenance chip, staleness stamp, tokens, sign-off ceremony,
   comparison component. *Benchmark*: chip renders ID-only by default, expands on demand; the
   stamp flips on fingerprint mismatch.
2. **The sentence moments + the scorecard** (M1, M3, M8) — no layout engines; they validate the
   annotated-sentence departure (§2.2) plus the pricing-as-clause and scorecard-not-dashboard
   calls. *Benchmark*: a non-author PM reaches every M1 clause's evidence in one click; M3 reads
   engagement-first with price visibly demoted.
3. **The map moments** (M4, M6) — need pull-script pre-computed layout. *Benchmark*: the DAG
   renders with zero hairballs at n=20 and redraws identically from the same JSON; the journey
   map marks money-shot and delight/utilitarian as labeled decisions.
4. **The register/decision moments** (M5, M2, M7) — M5 is the flagship departure. *Benchmark*:
   no 5×5 grid anywhere; every high risk has a response or sign-off is blocked; legible at n=50.

## 3. Coverage check — the moments against the machinery

**Against the numbered gates** (per the ontology §3.1 translation table, keyed to each gate's
required prefixes): v0.1 → M1, v0.2 → M3 (competitive evidence + the first type decision),
v0.3 → M3+M4 (pricing/KPI to M3; the FEA feature cut to M4), v0.4 → M2+M4 (PER- is gated here),
v0.5 → M5, v0.6 → M5 (contract drafts land in its sign-off), v0.7 → M6, v0.8 → M6+M7 (DEP to
the beta gate; RUN/MON to launch readiness), v0.9 → M7, v1.0 → M8 *(contingent on M8's
promotion — if declined, the launch-verdict adjudication needs another home and v1.0 is
orphaned)*. The guided journey (ontology §3.2) becomes, in practice, the walk from M1 to M8
(M8 pending).

**Against the playbook registry**: every audit-§3 playbook feeds at least one moment as
preparation, **except the growth-cycle cluster** — crossing-the-chasm (commitment half),
social-proof, continuous-discovery, changelog-marketing — which serves the loop's *second
revolution* and awaits the shorter post-M8 canon named below. The kernel verbs and their
invariants (harvest, drift, ID registration, projection) sit *between* moments — they are how
the planes stay healthy while the moments punctuate.

**Candidates deliberately not promoted** (revisit at the research session): MVP scope freeze
(currently the closing act of M4; could stand alone), positioning (currently inside M7; Dunford
purists may want it as its own moment), beachhead/chasm commitment (a post-M8 moment for the
growth cycle — the canon above covers idea → launch, and the loop's second revolution likely
deserves its own shorter canon).

## 4. What remains open (and for whom)

**Settled by the design research (v1.2)**: the visual genre per moment, the family system, the
three departures, and the build staging — the design session executes §§2.1–2.3 and the
per-moment Visual expression blocks, producing the flat HTML templates.

**For the design session to surface (not silently resolve)**:
1. M1's annotated-sentence hero vs the five-element-table fallback — prototype-test with
   experienced PMs (research confidence: Medium).
2. M4's two-mode template (build/decide) vs two pages — usability-test the seam.
3. Sign-off staleness tuning — data-state-bound sign-offs re-open when records change; how much
   churn before the ceremony's weight erodes? Needs a policy, not a default.
4. The style tile must stretch from M4's warmth through M5's sobriety to M8's gravity — build
   the tile spanning the extremes first.
5. Human-declaration flags — the money shot and the negative persona have no computed check;
   their *absence* must be visible on the page.

**Still for the question-research session (unchanged)**: the per-moment question banks (from the
richness ledgers), the emitted-record shapes (extending DELIVERABLES_CONCEPT §5 to plane
records), each moment's pass/fail line in its policy pack, M8's formal promotion, and the three
candidate moments. If quantification proves rare in practice, M5's tornado and M8's drift
degrade to ranked lists / RAG — still better than the rejected genres (research: High
confidence).

Evolution is expected; this canon fixes the *structure* (moment = deliverable + pack + playbooks
+ living template, terminating in adjudication) and now the *visual direction* — not the
question content.

---

## Provenance

Owner articulation 2026-08-13 (verbatim charters above); structural mapping from the session's
v2 corpus: ontology doc v2.2 (planes/verbs/surfaces), consolidation audit (playbooks, policy
packs, richness ledgers at `temp/v2-audit/inventory/`), DELIVERABLES_CONCEPT (mechanism and
value test), impeccable Northstar analysis (expression patterns worth borrowing). **v1.2**: the
Visual expression blocks, §§2.1–2.3, and §4 incorporate the commissioned design-research report
(received 2026-08-13, vendored with full citations at
[`V2_KEY_MOMENTS_VISUAL_RESEARCH.md`](V2_KEY_MOMENTS_VISUAL_RESEARCH.md)). Research input
pending R0; the surface-layer spec (to-do 15b) is this canon's v0.6 landing zone.

| Version | Date | Change |
|---|---|---|
| 1 | 2026-08-13 | Canon: eight moments, ontology mapping, verified |
| 1.1 | 2026-08-13 | Living-template expression architecture (Graphify pattern) |
| 1.2 | 2026-08-13 | Design briefing: per-moment visual direction, one-family system, genre departures, build staging — from the vendored design research |
