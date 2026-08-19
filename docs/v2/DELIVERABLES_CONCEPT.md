# Deliverables — Concept & Design Note

> **Status**: Concept only. Nothing in `SoT/html/` is changed by this document.
> **Branch**: `claude/prd-deliverables-concept-3r982d`
> **Scope**: Proposes a third artifact class for the PRD lifecycle — *deliverables* —
> interactive HTML surfaces where a human reviews or inputs judgment and the page emits
> paste-ready SoT markdown. This note argues the design and specs four reference deliverables.
> It does **not** build the HTML/JS; that is left to a future build EPIC (see §9).

---

## 1. Purpose & status

Today every PRD phase produces a **SoT output** (durable IDs in markdown). Most also have a
**read-only HTML companion** in [`SoT/html/`](../../SoT/html/README.md) that re-renders those IDs in
the format their natural reviewer already reads. Both are **agent-authored, one-directional**:
the markdown is authoritative and the HTML is a render of it.

A **deliverable** is the missing direction: a surface where the **human** contributes the judgment
an agent cannot fabricate — a risk severity, an acknowledgement, a ranking, a market read — and the
page hands back **markdown formatted as SoT entries** to commit. This gives each phase a *SoT output*
and, where human judgment is load-bearing, a *deliverable output*.

This document is the concept artifact. It does not change the lifecycle, the companion pages, or the
design contract. Where it recommends a future change (e.g. a contract amendment to allow a single
sanctioned script), it says so explicitly and defers it.

---

## 2. The three artifact directions

| Direction | Author | Flow | Authority | Example |
|---|---|---|---|---|
| **SoT** *(exists)* | Agent | writes durable IDs | **authoritative** | `RISK-003` block in `SoT.*.md` |
| **Companion HTML** *(exists)* | Agent | markdown → read-only render | render of SoT | `SoT.USER_JOURNEYS.html#UJ-001` |
| **Deliverable** *(new)* | **Human** | HTML form → markdown → back to SoT | input that *becomes* SoT | risk-ranking page emits a `RISK-` block |

The symmetry is the point. The companion renders SoT *outward* for review; the deliverable takes
human judgment *inward* and emits it in the exact shape SoT expects. A deliverable's output is not a
new format — it is a `BR-`, `UJ-`, `ARC-`, `RISK-`, or `CFD-` entry, ready for
[`ghm-id-register`](../../.claude/skills/ghm-id-register) to validate and commit.

**A deliverable doubles as the human gate.** Rule 05 (Lifecycle Gates) requires human sign-off
before advancing a stage. Completing a deliverable — ranking the risks, acknowledging the
architecture — *is* that sign-off, captured as a timestamped decision in the emitted markdown rather
than a side conversation.

---

## 3. Two species of deliverable

Naming the two kinds keeps the catalog honest, because they look different to the human even though
they share one mechanism.

| Species | The human's job | Pre-fill | Feeds | Examples |
|---|---|---|---|---|
| **Intake / Authoring** | Produce content from a guided form | mostly blank | *into* SoT | journey builder, market matrix, persona card |
| **Review / Acknowledge / Rank** | Apply judgment to agent-synthesized drafts | mostly pre-filled | *around* SoT | risk ranking, architecture sign-off |

Mechanically they are identical: form controls → live markdown preview → **Copy markdown** button.
The only difference is how much the agent pre-seeds. A Review deliverable arrives with the draft
already in the fields and asks the human to decide the few things only a human can (severity,
accept/mitigate, "yes this is right"). An Intake deliverable arrives blank and walks the human
through authoring a new entry. One engine serves both.

---

## 4. The round-trip loop

```
  ┌─ agent ─────────────┐      ┌─ human (browser, file://) ──────────────┐      ┌─ agent ───────────┐
  │ 1. run phase skill, │      │ 2. toggle "Input mode"                  │      │ 5. ghm-id-register │
  │    draft SoT IDs,   │ ───▶ │ 3. fill controls / rank / acknowledge   │ ───▶ │    validates,      │
  │    point human at   │      │ 4. JS builds live markdown → Copy       │      │    commits to SoT, │
  │    the page         │      │    (paste into chat or the SoT file)    │      │    mirrors render  │
  └─────────────────────┘      └─────────────────────────────────────────┘      └────────────────────┘
```

1. **Agent drafts.** The phase skill produces draft SoT entries and tells the human which companion
   page to open in Input mode (optionally pre-seeded with the draft).
2. **Human toggles Input mode.** The read-only render becomes editable (see §5).
3. **Human contributes judgment.** Selections, sliders, rankings, free text, acknowledgement.
4. **Page emits markdown.** A live `<textarea>` shows the SoT-formatted entry; **Copy markdown**
   puts it on the clipboard. The human pastes it into the chat or directly into the `SoT/*.md` file.
5. **Agent re-absorbs.** `ghm-id-register` validates IDs and cross-references, commits to the
   authoritative markdown, and the companion render is updated to match — closing the loop.

No server, no database, no build step. The page works from `file://`, exactly like the companion
pages do today.

---

## 5. Architecture — extend the companion pages (progressive enhancement)

**Decision: deliverables are an _input mode_ added to the existing `SoT/html/*.html` pages, not a
parallel directory.** This reuses the design language, the per-persona layouts, and the ID anchors
that already exist — a journey deliverable *is* `SoT.USER_JOURNEYS.html` with the gloves off.

### The tension, and how it's resolved

The companion design contract ([`SoT/html/README.md`](../../SoT/html/README.md)) is emphatic:

> *"If a device needs JavaScript, a shadow, a gradient, or a second accent color to read, it has
> left the system."*

Input mode needs JavaScript. The resolution is **progressive enhancement, not violation**:

- The *render* never depends on JS. With JavaScript disabled, every companion page is byte-for-byte
  the read-only review tool it is today. The contract's intent — "the render reads without script" —
  holds.
- Input mode is a strictly additive layer: one shared script, one toggle, revealed only when JS runs.

This warrants a **small, explicit amendment** to the contract carving out a single sanctioned
exception (one shared `deliverable.js`, enhancement-only). That amendment is *recommended here and
deferred* — it is not applied by this concept note.

### The mechanism

- **One shared script**: `SoT/html/assets/deliverable.js`, loaded the way `assets/sot.css` is shared
  across all pages. No per-page script, no framework, no bundler.
- **An "Input mode" toggle** in the top nav. Off by default → the page is the existing render. On →
  the page's placeholders become controls and a live-markdown panel + **Copy markdown** button appear.
- **The `.ph` alignment — the core insight.** Companion pages already mark every fillable slot with
  `<span class="ph">{slot}</span>` (italic dashed-underline placeholders). *Those are exactly the
  fields a deliverable needs.* Input mode turns each `.ph` into an editable control; the read-only
  page already knew where every input goes.
- **Declarative serialization.** A field carries `data-md-field` (which SoT field it is) and its
  parent entry carries `data-md-template` (the entry skeleton). One generic serializer walks the
  entry, substitutes field values, computes derived values (e.g. Raw Score = Impact × Likelihood),
  and assembles the markdown. Deliverables stay **"just markup"** — the same authoring model that
  makes the companion pages copy-a-block simple.

Sketch (illustrative, not final):

```html
<!-- read-only today: a placeholder slot -->
<dd><span class="ph">{Impact}</span></dd>

<!-- input mode (JS-enhanced): the same slot, now a control -->
<dd data-md-field="impact">
  <select><option value="3">High</option><option value="2">Medium</option>
          <option value="1">Low</option></select>
</dd>
```

```js
// deliverable.js — one serializer for every page
function emit(entryEl) {
  const tpl = entryEl.dataset.mdTemplate;            // SoT entry skeleton
  const fields = readFields(entryEl);                // {impact:3, likelihood:2, ...}
  fields.raw_score = fields.impact * fields.likelihood;   // derived
  return fill(tpl, fields);                           // → markdown string
}
```

---

## 6. Deliverable catalog

Four reference deliverables, specced field-by-field. Field tables match the **authoritative SoT
files** (`SoT/*.md` and `PRD.md`) — where a skill asset template disagrees with the SoT, the SoT
wins. Each lists species, the companion page it extends, the ID(s) it emits, the fields (control
type + allowed values), and a sample emitted block.

A note on what's *not* fully specced: the same pattern covers the remaining phases (v0.3 pricing/
feature-priority board, v0.9 positioning/offer canvas, v1.0 adoption-stage assessment). They are
named once here and left to the build EPIC — the four below establish the pattern.

### 6.0 The value test — a deliverable must extract a decision or capture the right acknowledgement

A deliverable that only re-types what the agent already produced is **waste** — it adds a click
without adding judgment. Each one must pass one of two tests:

- **Decision test** — does it capture a call only the human can make? (a severity, a price, a
  go/no-go, a "this is our advantage")
- **Acknowledgement test** — if the agent drafted it, does the surface make the human *actually
  read and own* the thing being signed off, rather than rubber-stamp it?

Graded against what each PRD stage and its SoT actually hold:

| Deliverable | What it captures | Value | The human-only input that justifies it |
|---|---|---|---|
| **Risk ranking** (§6.1) | **Decision** | **High** | Impact, Likelihood, Status, accept/mitigate — the v0.5 register marks these *user-decided*; the page then computes Raw and **Effective Score** the human would otherwise do by hand. |
| **Market analysis** (§6.4) | **Decision** | Med-High | The decision is the per-competitor **Product decision** (Implement/Defer/Decline), the **feature-matrix cells**, and the **positioning rule** — *not* the research (which the agent gathers). |
| **Architecture map** (§6.3) | **Acknowledgement** | Med-High | Sign-off that gates v0.7, plus the human-authored **Conformance Rule** (a structural claim the build is later checked against). |
| **Journey builder** (§6.2) | **Acknowledgement** | Medium | Weakest case — journeys are largely agent-draftable. It earns its place *only* if it forces the human-only fields: the real **pain points** and the true **moment of value**. Otherwise it is a rubber-stamp; see §6.2. |

The lesson the grade teaches: lead a deliverable with the human-only fields, and let the agent
pre-fill everything else. Where there is no human-only field, there should be no deliverable —
which is exactly why v0.7 Build has none (§8).

### 6.1 Risk acknowledgement & ranking  — *Review species*

- **Extends**: the RISK view (rendered in the `SoT.TECHNICAL_DECISIONS.html` family / a dedicated
  RISK companion). **Emits**: `RISK-`.
- **Why this is the strongest first prototype**: the v0.5 risk register (`PRD.md` §v0.5) marks
  Impact, Likelihood, and Status as *user-decided*. This is the one place an agent genuinely cannot
  fill the answer — the deliverable captures the human's call, then **does the arithmetic the human
  would otherwise do by hand**: Raw = Impact × Likelihood and Effective Score = Raw × Status weight,
  the value that rolls up into the README Risk Scorecard. Decision capture *and* a real computation:
  the clearest pass of the §6.0 value test.

| Field | Control | Allowed values | Required |
|---|---|---|---|
| Title | text | free | yes |
| Scoring category | select | Market / User / Technical | yes |
| Discovery category | select | Market / Technical / Adoption / Resource / Dependency / Timing | yes |
| Description | textarea | free | yes |
| Trigger | textarea | free | yes |
| **Impact** | select | High (3) / Medium (2) / Low (1) | **yes** |
| **Likelihood** | select | High (3) / Medium (2) / Low (1) | **yes** |
| Raw score | *derived* | 1–9 (= Impact × Likelihood) | auto |
| Status | select | open / mitigating / mitigated / resolved / accepted | yes (default open) |
| Effective score | *derived* | Raw × Status weight (open/accepted = 1.0 · mitigating = 0.5 · mitigated = 0.25 · resolved = 0.0) | auto |
| Response | select | Mitigate / Accept / Avoid / Transfer | yes |
| Mitigation | textarea | free (required if Response = Mitigate) | conditional |
| Early signal | textarea | free | yes |
| Owner | text | free | yes |
| Linked IDs | text | `FEA-`,`UJ-`,`BR-`,… (comma-sep) | no |
| Review date | date | YYYY-MM-DD | yes |

```markdown
### RISK-001: Stripe API Dependency
- **Scoring category**: Technical
- **Discovery category**: Dependency
- **Description**: Payment processing depends entirely on Stripe API availability.
- **Trigger**: Stripe outage, rate limiting, or API deprecation.
- **Impact**: High (3) · **Likelihood**: Low (1) · **Raw score**: 3
- **Status**: open · **Effective score**: 3.0
- **Response**: Mitigate
- **Mitigation**: Payment queue with 24h retry; subscribe to Stripe status webhooks; manual-invoice fallback.
- **Early signal**: Payment failure rate > 0.5%; Stripe status-page alert.
- **Owner**: Backend Lead
- **Linked IDs**: FEA-020, UJ-005, BR-030
- **Review date**: 2026-03-01
```

### 6.2 User-journey builder  — *Intake species*

- **Extends**: `SoT.USER_JOURNEYS.html`. **Emits**: `UJ-` (and `PER-` when a new persona is authored).
- The page already renders journeys as a trigger → steps → value-moment track; Input mode lets the
  human *build* that track instead of reading it.
- **Rubber-stamp risk** (§6.0): journeys are largely agent-draftable from personas + features, so
  this is the weakest value case. It earns its place only if the surface **foregrounds the
  human-only fields** — the true **moment of value** and the real **pain points** (what actually
  frustrates the user, which the agent can only guess) — and lets the agent pre-fill the
  mechanical step list. If the human just confirms an agent draft, drop the deliverable and keep the
  read-only render.

| Field | Control | Allowed values | Required |
|---|---|---|---|
| Journey name | text | free | yes |
| Persona | select/ref | `PER-` | yes |
| Type | select | Core / Onboarding / Recovery / Power User | yes |
| Trigger | textarea | free (specific, not "opens app") | yes |
| Goal | textarea | free | yes |
| Steps | repeatable rows | Action text + Feature link (`FEA-`) | yes (≥3) |
| Pain points | repeatable rows | Step # + description | recommended ≥1 |
| Value moment | textarea | free | yes |
| KPI link | select/ref | `KPI-` | yes |
| Success metric | textarea | free | yes |
| Dependencies | text | `UJ-`,`BR-`,`API-` (comma-sep) | no |
| Confidence | select | High / Medium / Low | no |

```markdown
### UJ-001: First Report Generation
- **Persona**: PER-001 · **Type**: Core
- **Trigger**: User finishes onboarding and lands on the empty-dashboard prompt.
- **Goal**: Generate a first automated report to prove the time-saving value.
- **Steps**:
  1. Click "Create Report" → FEA-003
  2. Select connected data source → FEA-001
  3. Choose a template → FEA-008
  4. Preview with real data → FEA-003
  5. Export PDF → FEA-009
- **Pain points**: Step 2 — user may not have connected data yet (dep UJ-002).
- **Value moment**: Seeing a finished report built from their own data.
- **KPI link**: KPI-002 · **Success metric**: click→export ≤ 5 min; 70% Day-1 completion.
- **Dependencies**: UJ-002, BR-015 · **Confidence**: High
```

### 6.3 Architecture map  — *Review / sign-off species*

- **Extends**: `SoT.TECHNICAL_DECISIONS.html`. **Emits**: `ARC-`.
- The agent drafts the ADR; the human reviews the topology, **acknowledges** each decision, and flags
  concerns. The acknowledgement stamp is the gate signal.

| Field | Control | Allowed values | Required |
|---|---|---|---|
| Title | text | free (action-title sentence) | yes |
| Category | select | Data Flow / Security / Scaling / Integration / Patterns | yes |
| Context | textarea | free | yes |
| Decision | textarea | free | yes |
| Rationale (chosen because / alternatives / consequences) | textarea | free | yes |
| Conformance rule | group | Rule (plain claim) + Check (type · scope · target); **Verdict is computed** (`pass`/`violate`/`unknown`), not entered | no |
| Status | select | Accepted / Deprecated / Superseded | yes |
| Acknowledged by / date | text + date | reviewer + YYYY-MM-DD | yes (sign-off) |

> Enums match the authoritative `SoT.TECHNICAL_DECISIONS.md` ARC- template (not the looser skill
> asset). The human's load-bearing inputs are the **acknowledgement stamp** and the optional
> **Conformance Rule** — a structural claim (e.g. *"the `engine/` layer must not import the UI
> framework"*) the v0.7 build is later checked against, feeding the `architecture_conformance`
> readiness dimension. The agent drafts Context/Decision/Rationale; the human owns the sign-off and
> the rule.

```markdown
### ARC-001: Monolith with Module Boundaries
- **Category**: Patterns
- **Context**: App structure for an MVP, team of 2, ~100 target users.
- **Decision**: Single Next.js app with a `/modules` folder structure.
- **Rationale**: Chosen because one deployment minimises ops burden and domain boundaries are
  unclear until real usage. Alternatives: microservices (premature complexity), serverless-first
  (cold starts hurt the dashboard). Consequences: enables fast iteration and simple deploy;
  constrains to a single scaling unit and shared deploy cycle.
- **Conformance rule**: `modules/*` must not import across module boundaries — Check:
  `forbidden_import` · `modules/**` · `../*/internal`. Verdict: *computed*.
- **Status**: Accepted
- **Acknowledged by**: Tech Lead · 2026-06-15
```

### 6.4 Market analysis  — *Intake species*

- **Extends**: `SoT.customer_feedback.html` (competitive intelligence) + `SoT.BUSINESS_RULES.html`
  (positioning). **Emits**: `CFD-` and `BR-` (a v0.2 *Enabling Business Rule* per `PRD.md` §v0.2;
  the `BR-POS-` positioning-rule sub-ID is the **v0.9 Dunford refinement** of the same rule, not a
  v0.2 output).
- Two coupled sub-forms plus a **feature matrix** the human fills cell-by-cell.
- **Where the value is** (§6.0): the agent gathers the competitive research; the human's calls are
  the per-competitor **Product decision**, the **feature-matrix cells**, and the **positioning rule**.
  Lead the surface with those three.

`CFD-` (competitive intelligence) fields:

| Field | Control | Allowed values | Required |
|---|---|---|---|
| Title / competitor | text | free | yes |
| Type | select | Competitive Intelligence (fixed here) | yes |
| Status | select | New / Analyzed / Actioned / Declined | yes |
| Priority | select | Critical / High / Medium / Low | no |
| Reported by | text | source + count | yes |
| Target segment | textarea | free | yes |
| Pricing model | textarea | free | yes |
| Key weakness | textarea | free | yes |
| Market data | textarea | funding / revenue / evidence | no |
| Evidence tier | select | Tier 1 (interviews) / Tier 2 (reviews) / Tier 3 (inference) | yes |
| Product decision | select | Implement / Defer / Decline / Needs Research | no |

`BR-` (positioning / enabling rule) fields: Rule statement (textarea, imperative) · Category
(select: Pricing/Data/Permissions/Compliance/Performance) · Severity (Critical/High/Medium/Low) ·
Source (`CFD-` ref) · Rationale (driver + UX impact) · Enforcement location (Server/Client/Both) ·
Enforcement timing (On action/Background/Real-time). Fields match `SoT.BUSINESS_RULES.md`.

**Feature matrix** (one editable table; each cell a select): rows = features, columns = Us + each
competitor, cell ∈ { ✅ Has / ❌ Missing / 🔄 Planned / ⚠️ Partial }, plus a Gap-notes column.

```markdown
### CFD-042: Competitor — Yodeck
- **Type**: Competitive Intelligence · **Status**: Analyzed · **Priority**: High
- **Reported by**: G2 reviews (50+ users)
- **Target segment**: Enterprise digital signage (100+ screens)
- **Pricing model**: $8 / screen / month
- **Key weakness**: Prohibitively expensive for SMB (5–20 screens)
- **Evidence tier**: Tier 1 · **Product decision**: Implement (flat-pricing wedge for the SMB gap)

### BR-001: SMB-First Flat Pricing
- **Category**: Pricing · **Severity**: High · **Source**: CFD-042
- **Rule**: All self-serve tiers MUST support unlimited screens at a flat monthly rate; no per-screen upsell.
- **Rationale**: Competitors charge per-screen; SMB users churn at 10+ screens. Flat pricing is the 1%-better wedge.
- **Enforcement**: Server (billing engine) · On subscription create/upgrade

| Feature | Us (planned) | Yodeck | ScreenCloud | Gap notes |
|---|:--:|:--:|:--:|---|
| Unlimited screens (flat) | ✅ | ❌ | ❌ | Our advantage |
| Template library | 🔄 | ✅ | ✅ | Must have |
| Mobile app | ❌ | ✅ | ✅ | Not for MVP |
```

---

## 7. Gate & readiness tie-in

A deliverable is the natural home for the **human sign-off** that gates require (rule 05). Two ways
it connects to the existing machinery:

- **As gate evidence.** The emitted markdown carries the decision and a reviewer + date stamp (see
  `Acknowledged by` in §6.3, `Review date` in §6.1). That stamp is the artifact a gate review points
  at — "the risks were ranked and accepted on 2026-06-15" — instead of an untracked conversation.
- **As an optional future readiness signal.** Readiness ([rule 07](../../.claude/rules/07-readiness-protocol.md))
  could later credit a "human acknowledgement present" dimension. **Constraint**: it must stay
  deterministic and LLM-free — a boolean "stamp present / absent" check, never a model-judged quality
  score. Anything more would violate the anti-Goodhart discipline in rule 07. This is noted as a
  *possible* extension, not a recommendation to add a dimension now.

Deliverables do not change thresholds or the scorer. They give the human decision a durable place to
live so the gate has something real to read.

---

## 8. Phase-collapse analysis

The deliverable lens doubles as a **diagnostic for the lifecycle itself**. The premise:

> **A phase earns independence if it carries a distinct human decision (a deliverable). Adjacent
> phases that would share one deliverable are collapse candidates.**

This is a *question generator*, not a verdict. The table below is a first read; each "merge?" row is a
question for the human owner, not a proposed edit to the lifecycle.

| Stage | Distinct human decision(s) | Deliverable | Verdict |
|---|---|---|---|
| v0.1 Spark | Is the problem real / does the value land? | Problem validation | **merge-candidate** w/ v0.2 |
| v0.2 Market | How do we position vs alternatives? | Market analysis (§6.4) | **merge-candidate** w/ v0.1 |
| v0.3 Commercial | Pricing **and** feature priority **and** KPI targets | 3 distinct surfaces | **keep** — dense |
| v0.4 Journeys | Author journeys + personas | Journey builder (§6.2) | **keep** |
| v0.5 Red Team | Rank/accept risks **and** stack build-vs-buy | Risk ranking (§6.1) + stack | **keep** — 2 deliverables |
| v0.6 Architecture | Acknowledge topology | Architecture map (§6.3) | **keep** |
| v0.7 Build | *(none — test/code-gated)* | — | **no-deliverable phase** (expected) |
| v0.8 Ops | Review runbooks / monitoring | thin | **merge-candidate** w/ release half |
| v0.9 GTM | Positioning + offer | Positioning/offer canvas | **keep** |
| v1.0 Adoption | Where are we on the Moore curve? | Adoption-stage assessment | **keep** |

**Findings to weigh (open questions, not changes):**

1. **v0.1 + v0.2 → one "Opportunity" canvas?** Both answer "is there a real problem and a market for
   it?", both run on `CFD-` evidence, both are owned by the `horizon` agent. A single intake
   deliverable could plausibly carry both decisions. *Question for the owner: are Spark and Market
   genuinely two human decisions, or one decision split across two stages?*
2. **v0.7 Build is legitimately deliverable-free.** Its gate is tests and `@implements` coverage, not
   a human sign-off form. The absence of a deliverable here is correct, not a gap — useful evidence
   that the lens distinguishes "human-judgment phases" from "execution phases."
3. **v0.8 Ops has a thin human-decision surface.** Most of its output (`DEP-`,`RUN-`,`MON-`) is agent
   authored and machine-checked; the human mostly *reviews*. *Question: does Ops need its own stage,
   or is it the back half of a combined Release stage?*
4. **v0.3 and v0.5 are the densest.** Each bundles multiple independent human decisions, which both
   justifies their standalone stages *and* argues they should ship **multiple** deliverables rather
   than one — the inverse of the collapse question.

The lens does not say "collapse these." It says **a phase with no distinct human decision, or one
that shares its decision with a neighbour, deserves a second look.** The owner decides.

---

## 9. Open questions & next steps (deferred to a build EPIC)

This note builds nothing in `SoT/html/`. A future build EPIC would, in order:

1. **Amend the contract** — add the single sanctioned `deliverable.js` enhancement exception to
   [`SoT/html/README.md`](../../SoT/html/README.md), preserving "render never depends on JS."
2. **Build the shared engine** — `SoT/html/assets/deliverable.js`: the Input-mode toggle, the
   `.ph`→control promotion, the `data-md-*` serializer, derived fields, and **Copy markdown**.
3. **Ship one reference deliverable** — risk ranking (§6.1) on the RISK view, end-to-end, as the
   proof. It is the strongest case because severity is human-only.
4. **Wire the round-trip** — confirm `ghm-id-register` cleanly absorbs pasted output and mirrors it
   back to the read-only render.
5. **Then templatize** — extend the remaining three (§6.2–6.4) and the named-but-unspecced phases.

Open questions for that EPIC:
- Should Input mode pre-seed from the current SoT (requires generating the page from markdown) or
  start blank? (Recommend: blank/template for v1, pre-seed later.)
- Clipboard vs. file-download vs. direct-to-chat as the hand-off? (The "copy-paste markdown" framing
  points at clipboard first.)
- Does the phase-collapse analysis (§8) warrant a separate lifecycle-review session before any
  deliverable is built?

---

*Companion concept note. Authoritative design contract for the HTML layer remains
[`SoT/html/README.md`](../../SoT/html/README.md); lifecycle authority remains [`PRD.md`](../../PRD.md) and
[`README.md`](../../README.md).*
