---
title: "GearHeartAI.org · PRD-Led Context Engineering Site Brief — the home of the thinking"
brief_version: 2.0
date: "2026-08-19"
supersedes: "v1.0 (2026-08-08) — a product-marketing brief organised around the working name 'The Product Model' and a hero proof interaction"
status: "Planning brief — V2 proposed; owner review required before implementation or release (PRD.md v0.1 non-goal: building the site; PRD open decision 4: when website proof may move from planning to public evidence)"
audience: "Coding agent responsible for GearHeartAI.org; the owner as publisher"
product_generation: 2
source_repository_branch: "prd-ce-v2"
source_review_commit: "REQUIRED_AT_SITE_EXECUTION — record the exact commit the site agent reviewed. The branch-history publication question was resolved by the owner on 2026-08-12 (PRD.md open decision 5: publish as-is); no sanitization step remains."
research_blueprint_original_sha256: "afe50856ff70f9dcf00eafe9ecc41df7eaea5310c395c936af16cb8e706e45a5"
research_blueprint_file_sha256: "e32ecaba7db51ffbcabee8f29550a63b7cb828bd781567ba23bd690f146c4f83"
research_blueprint_path: "docs/v2/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md"
build_plan_path: "docs/v2/PRD_CE_V2_BUILD_PLAN.md"
companions:
  - "docs/v2/V2_KEY_MOMENTS.md (v1.2) and docs/v2/V2_KEY_MOMENTS_VISUAL_RESEARCH.md — the canon this site publishes"
  - "docs/v2/ECOSYSTEM_ONTOLOGY.md §2.4 (surfaces) and §4 (the public loop vocabulary)"
  - "docs/v2/V2_GO_LIVE_POLISH_PLAN.md — the repo-side go-live plan this brief pairs with"
  - "docs/v2/audit/v2-walkthrough.html — the owner's private walkthrough; a future public page once re-tokenised"
---

# GearHeartAI.org · PRD-Led Context Engineering Site Brief

> **What changed in v2.0.** The site's job is no longer to market a product surface. It is to be the
> **home of the thinking behind PRD-Led Context Engineering** — the thesis, the eight Key Moments, and an
> essay series — with the open repository as the proof and the plugin as the install. The outcome hero from
> v1.0 stays; the interactive proof demo moves to a later phase (Appendix B); "The Product Model" moves to an
> appendix as a working name only (Appendix A). The truth boundary stays as strict as before and gains a
> claim-class model so that opinion can be published now without a single unbuilt capability being implied.

## 1. Assignment

Make GearHeartAI.org the place where the thinking behind **PRD-Led Context Engineering** lives: one
promise, one thesis, eight moments, a living essay series, and one honest next step into the open
repository. Most visitors will arrive from a LinkedIn post. They should leave able to explain the idea in a sentence,
having read something worth their time, and knowing exactly where the method lives and how to start.

The site introduces the method through one memorable promise:

> **Your product should remember.**

The first viewport keeps that outcome tangible — a team can inspect what is current, why it is true, what
contradicts it, what depends on it, and what decision should happen next — and then hands the visitor to
the body of thought: the thesis ("Memory as Infrastructure"), the Product Management loop, the eight Key
Moments where clarity of expression is the product, and the essays. The deeper architecture — Markdown
Source of Truth, typed IDs, relationships, provenance, temporal history, skills, hooks, policies — is
progressively disclosed, and the repository carries it.

> **Truth boundary:** This brief defines the eventual scope of an illustrative website experience;
> current approval covers planning and shaping only. Implementation requires separate owner
> approval. The site may not present a working V2 parser, index, Change Set runtime, `/product`
> command, MCP tool, or hosted service. No V2 runtime existed on the source branch when this brief
> was prepared.

When implementation is separately approved, this brief limits changes to the GearHeartAI.org
codebase. It does not authorize changes to the PRD-CE repository, production data, external
accounts, analytics providers, email systems, or public release settings unless those are
separately requested.

### 1.1 The site as observed on 2026-08-19 (what the agent will find)

A single page on Next.js (App Router) deployed on Vercel, Tailwind, `next/font` (three faces), Vercel
Analytics; `<title>` "GearHeart AI - Context Engineering for AI-Led Teams"; H1 **"Memory is
Infrastructure."** with sections The Cognitive Shift · Documentation Ecosystem (L0–L3) · PRD-Driven
Lifecycle · Shared Memory · Context Automation & Governance · Durable IDs · Continuity; CTAs "Get Started"
and "Subscribe"; footer links to a personal GitHub profile, a LinkedIn company page, Substack, and Twitter.
Findings the redesign must close: the declared `og-image.png` returns 404 (every LinkedIn share is
imageless); the page never links the PRD-CE repository; `/blog`, `/essays`, `/docs` and similar redirect to
`/` (no writing surface); no `sitemap.xml` or `robots.txt`; the live palette is the deprecated dark/cyan
language, not the owner's current editorial system (§9); and the H1 says "is" where the thesis says "as".

## 2. Product and naming architecture

| Level | Name | Role | Public status |
|---|---|---|---|
| Publisher | **GearHeart AI** | Creates AI-native operating methods and products; author of the essays | Existing |
| The method | **PRD-Led Context Engineering** (short: PRD-CE) | The open methodology and repository; the thing the site is about | Available now, subject to claim verification |
| The thesis line | **Memory as Infrastructure** | The idea the method is built on; the title of the founding essay | Publishable now as the owner's position |
| Generation label | **V2** (as in "PRD-CE V2") | Connects the proposed next generation to the existing repository and community | Proposed; label only |
| The canon | **The Key Moments** (M1–M8) | The eight moments where clarity of expression is the product — the site's editorial spine | Design direction — research input pending R0 |

Usage rules:

- **PRD-Led**, never "PRD-driven" in prose. The repository slug `PRD-driven-context-engineering` is an
  immutable URL and the only sanctioned use of "driven"; the GitHub description and the live site's
  metadata should be corrected to "PRD-Led" (repo-side item in the polish plan).
- **Memory *as* Infrastructure**, never "Memory is Infrastructure" — the live H1 drifts.
- **"The Product Model"** is a working name only, pending PRD open decision 1; it does not appear on the
  site outside an explicitly labeled note, and it never leads (Appendix A).
- Do not name, market, preview, or measure future GearHeart products. Do not rename repositories,
  packages, commands, or the organization from this brief. In code and metadata keep
  `product_generation: 2` distinct from PRD lifecycle gate, repository, template, plugin, and package
  versions.

Recommended first public reference:

> **PRD-Led Context Engineering — Memory as Infrastructure.** An open method for building products with
> AI agents, published by GearHeart AI.

## 3. Source basis and authority

The coding agent must read the target site's local instructions and source before changing it. Treat the
following as the content basis:

- The canonical root [`PRD.md`](../../PRD.md), at v0.1, plus its accepted BR/ARC records.
- The proposed [V2 build plan](PRD_CE_V2_BUILD_PLAN.md) — contingent sequencing subordinate to the PRD.
- **The canon**: [`V2_KEY_MOMENTS.md`](V2_KEY_MOMENTS.md) (v1.2 — charters, loop positions, clarity
  anchors, visual direction) and its vendored research report
  [`V2_KEY_MOMENTS_VISUAL_RESEARCH.md`](V2_KEY_MOMENTS_VISUAL_RESEARCH.md). Both are research input
  pending R0; the site quotes the owner's charters verbatim and labels the rest as design direction.
- The public vocabulary of the loop — Explore → Shape → Decide → Build → Learn, with Check cross-cutting —
  from [`ECOSYSTEM_ONTOLOGY.md`](ECOSYSTEM_ONTOLOGY.md) §4 (owner preference; the five internal planes
  stay off the site).
- The preserved [V2 research blueprint](MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md),
  version 2.1, fingerprinted in this document's frontmatter — input only.
- The canonical [PRD-CE repository](https://github.com/mattgierhart/PRD-driven-context-engineering) and its
  README, CHANGELOG, and `SoT/html/` review layer, at the commit recorded in `source_review_commit`.
- The owner's portfolio design language for this surface — **"Editorial Luxury"** (`tokens.css`,
  `voice.md`, `components.md`, `shopping-log.md`), which names GearHeartAI.org as its canonical home. The
  values the site needs are inlined in §9; vendor the files into the site repository rather than linking
  to a machine-local path.
- The current [GearHeartAI.org site](https://www.gearheartai.org/) (§1.1).
- The [Impeccable](https://impeccable.style/) workflow documentation, for process only (§10).

This brief is self-contained for website planning. At execution time, record the exact reviewed
source-branch commit in the site repository's provenance config; do not use a mutable branch name as
public evidence. If a source document is unavailable, do not invent missing detail or represent a
proposal as implemented. Do not link a public site to a machine-local path.

Authority rules:

1. PRD-CE remains the canonical methodology source. GearHeartAI.org is a presentation and distribution surface, not a competing Source of Truth.
2. The root PRD and accepted SoT govern product truth. The build plan is proposed sequencing and the
   research blueprint is input; none of them proves that a feature ships without executable evidence.
3. Website copy must resolve from a small, explicit capability-status model. Each public capability record must include `status`, `sourceUrl`, `sourceCommitOrRelease`, and `verifiedAt`; validation must reject factual claims whose provenance is missing or stale under the site's policy. Do not duplicate changing counts or release claims across components.
4. Never invent customers, testimonials, adoption metrics, benchmarks, installation commands, working integrations, or product screenshots.
5. Every factual product claim must link to a current artifact, release, demo, or repository source. Clearly labeled illustrative fixture data is exempt because it is not a product claim, but it must never be mixed with real evidence.

For this implementation, missing provenance is a build failure **for capability records** (claim class A
and C below). Reverify time-bound claims — release status, install commands, counts, compatibility, dates,
and "current" availability — in the same implementation session and whenever `sourceCommitOrRelease`
changes. Stable principles and essays may cite an immutable source without an invented time-to-live. Age
review beyond those triggers remains manual until the site defines a separate owner-approved staleness
policy.

## 4. Truth boundary: what the site may say

### 4.1 Three claim classes

The thought-leadership home and the truth boundary coexist by separating three kinds of statement:

| Class | What it covers | Rule |
|---|---|---|
| **A · Practice** | What `main` ships today: the methodology, templates, skills, hooks, readiness scoring, the SoT HTML review layer, the fork/template/installer paths; the plugin only after a verified end-to-end install | The full provenance model applies (`status`, `sourceUrl`, `sourceCommitOrRelease`, `verifiedAt`); missing provenance fails the build; counts only when generated from one canonical registry |
| **B · Thesis** | The owner's positions: "Memory as Infrastructure", the Cognitive Shift, the loop, the Key Moments canon, the v2 architecture *as argued*, every essay | Publishable now as **dated, attributed opinion**. Each piece carries its date, author, a truth label ("Design direction — proposed" where it describes v2), and a provenance footer (source document + commit). It may not contain counts, commands, or screenshots of unbuilt things. Until R0 lands, canon pages use only the public vocabulary (the loop verbs) and state "research input, not accepted product truth" |
| **C · Runtime** | The Compatibility Inspector, the moment templates and pull scripts, `/product`, Change Sets, MCP, graph JSON, viewer, context compilation | "Not yet built." Explained or illustrated, never rendered as shipped; no runnable-looking commands, no copy buttons, no screenshots until an artifact exists — and then labeled **Illustrative preview** |

### 4.2 Capability and content matrix

Before implementation, verify every row against the current PRD-CE checkout and public release surface.
Store the result in one typed content/config object so badges, buttons, metadata, and copy cannot drift.

| Item | Class | Default website status | Copy rule |
|---|---|---|---|
| Markdown Source of Truth, typed IDs, relationship model, lifecycle, existing skills and hooks | A | **Available in the current methodology** | Link to exact repository documentation; no skill count until generated from one canonical registry |
| Fork / "Use this template" / deterministic self-install prototype | A | **Available / prototype**, after live verification | Exact verified commands only; identify prototype status |
| Packaged Claude Code plugin / marketplace install | A | **Unverified release status** | No install CTA until an end-to-end public install succeeds |
| Human-facing SoT HTML review layer | A | **Available as a review view** | A derived human-review surface, not the canonical editor; screenshots allowed (they are real renders) |
| "Memory as Infrastructure" thesis, the Cognitive Shift, the essays | B | **Owner position — publishable now** | Dated, attributed, provenance footer; no capability implied |
| The Product Management loop (Explore → Shape → Decide → Build → Learn · Check) | B | **Design direction — proposed** | Label until R0; `Build` remains a working verb (PRD open decision 2) |
| The Key Moments canon (M1–M8) | B | **Design direction — research input pending R0** | Owner charters verbatim; visual direction as prose; M8 marked "proposed addition" |
| Key Moment HTML templates and pull scripts | C | **Not built** | Never shown as screenshots until they exist; then "Illustrative preview", fixture data only |
| The v2 walkthrough page | B | **Illustrative concept** | Publish only after re-tokenising to the house system and labeling the product ("Signal") as fictional |
| Interactive deliverables / input mode | C | **Concept** | Not shipped functionality |
| Development Graph extraction | C | **Planned unless an extractor is verified** | Do not imply an AST extractor ships |
| Read-only Compatibility Inspector (`index`, `check`, `query`, `trace`) | C | **Proposed alpha** | Explain or illustrate; no runnable styling |
| V2 `/product` interface, Change Set runtime, accepted-state mutation, MCP, graph JSON, viewer, context compilation | C | **Proposed later work** | Out of the primary proof |
| Hosted graph, continuous sync, cloud, registry/marketplace, enterprise governance, portfolio analytics | — | **Outside the current release** | Do not market, navigate to, price, or collect demand |

Use plain labels: `Available now`, `Prototype`, `Design direction`, `Illustrative preview`, `V2 proposed`.
Do not use `New`, `Live`, `In development`, or `Coming soon` without a verified release target.

## 5. Audience and jobs to be done

### Proposed site-shaping audience (pending v0.2 evidence and owner decision)

Product managers, product leaders, and product operations leaders responsible for a long-lived
product that is increasingly shaped with multiple AI agents. They have evidence, decisions,
requirements, delivery state, release learning, and rationale spread across PRDs, tickets, code,
tests, chats, dashboards, and individual memory. They want each human and agent to work from current
context without re-briefing or silent invention.

This is a content-shaping hypothesis, not the accepted v0.2 primary segment. The product owner must
select the primary audience and "not for" boundary from accepted, reviewable evidence before the
PRD advances to v0.2; implementation agents must not infer that decision from this brief.

### The reader path this site is built for

**LinkedIn reader → essay reader → repository adopter.** Most first visits arrive from a post. The
landing page for a post is usually an essay or a canon page, not the homepage; every such page must stand
alone (promise, provenance, one next step) and lead to the repository in one click.

### Secondary audiences

- Solo product builders who have outgrown one-shot prompting.
- Engineering, design, research, data, and operations collaborators who consume or update product context.
- Teams in regulated or dependency-heavy domains that need provenance and change history.
- Framework and agent-tooling contributors evaluating an open, local-first foundation.

### Core jobs

1. Tell me what the product currently believes.
2. Show me why that belief exists and where it came from.
3. Show me what contradicts it or has become stale.
4. Show me which journeys, requirements, delivery artifacts, tests, releases, and learning depend on it.
5. Help me propose and review a change without erasing history.
6. Give the next human or agent only the context needed for the work at hand.
7. **Help me think about this discipline** — give me the argument, the moments, and the vocabulary, written by someone who has done it.

The homepage serves jobs 1–6 in the hero and job 7 in the body, before teaching ontology or lifecycle stages.

## 6. Release scope for the website

### Phase 1 — the thought-leadership home (this brief's implementation scope)

- A redesigned homepage: outcome hero, the static "what remembering looks like" exhibit, the problem,
  the loop, the eight-moments teaser, the latest essays, the honest status block, one final action (§8).
- **The Method** page: the loop in five verbs and a Check; what exists today; how to start (links).
- **The Key Moments**: an index (the M1→M8 arc from thesis to reckoning) and one canon page per moment (§8b).
- **Essays**: an index and an article template, with the first six to eight pieces from Appendix C.
- Fixes: `og-image.png` exists (1200×630) and shows the promise, not generic AI imagery; `sitemap.xml`,
  `robots.txt`, RSS/Atom; canonical host; repository links everywhere a method claim is made; "as" not "is".
- Migration to the Editorial Luxury visual system (§9) within the existing stack.
- Working links to verified documentation, source, and contact surfaces; responsive, accessible,
  reduced-motion, and no-JavaScript fallbacks for essential content; SEO and social metadata aligned to
  the promise; automated content, accessibility, performance, and visual checks proportionate to the stack.

### Phase 2 — proof and previews (separately approved)

- The hero proof interaction (Appendix B).
- Moment previews (screenshots of built templates, labeled illustrative) embedded on canon pages.
- The public walkthrough page.

### Phase 3 — install and runtime (when verified)

- Install CTAs (plugin / template / installer) once each path is verified end to end.
- The read-only Compatibility Inspector as the first runtime-backed proof (build plan Wave 2).

### Preserve

- The GearHeart AI name and existing logo unless the user separately approves a brand change.
- Working privacy, terms, contact, newsletter, and analytics behavior. If a surface cannot be verified, retain it unchanged or remove the new call-to-action rather than simulate success.
- The current technical stack, routing model, package manager, deployment path, and component conventions unless a change is necessary and justified. Adding content routes, RSS, and sitemap generation is within scope; a framework rewrite is not.

### Do not build in this pass

- A real graph database, V2 query backend, authentication, user accounts, cloud dashboard, marketplace, pricing system, or adjacent methodology workflow.
- A CMS, comments system, chat, paywall, or any backend for essays — essays and canon pages are files in the site repository.
- A general node-link graph canvas.
- Fake terminal output presented as a live system; fake metrics, fake testimonials, fake adoption counts.
- Empty navigation destinations.
- A clone of Impeccable's site, assets, layout, command names, dark/gold identity, or motion choreography.
- A second editable copy of PRD-CE product facts inside arbitrary components.

## 7. Information architecture

Keep the first release shallow and real. Every destination below ships with maintained content or does not ship.

### Primary navigation

1. **The Method** — the loop, what exists today, how to start.
2. **Key Moments** — the M1→M8 index and canon pages.
3. **Essays** — the series, newest first, with RSS.
4. **GitHub** — the canonical repository (external).
5. **Install** — only after a path is verified (Phase 3); until then this slot does not exist.

Keep one strong header action. Before V2 installation is verified, use **Read the thesis** (or **View on
GitHub**), not **Install V2**.

### Footer

Repository · Releases/Changelog (when they exist) · LinkedIn (the owner's profile as primary; company page
secondary — owner decision) · RSS · Substack · Contact · Privacy · Terms.

### Possible later navigation, not required now

Walkthrough · Proof/Explorer · Changelog · Research. Add each only when its destination contains real,
maintained content. Do not reserve empty navigation for speculative platform surfaces or future products.

## 8. Homepage narrative and content contract

### Section 1 — Hero: outcome, one exhibit, one action

**Headline**

> Your product should remember.

**Recommended subhead**

> GearHeart AI publishes the thinking behind PRD-Led Context Engineering — an open method that keeps what
> your team learns, decides, delivers, and observes current and attributable, for every human and agent
> who touches the product.

**Actions**

- Primary: **Read the thesis** → the "Memory as Infrastructure" essay (alternative: **See the eight moments**).
- Secondary: **View PRD-CE on GitHub** → verified repository URL.
- Nearby status text, not a decorative pill: **The methodology is available today. V2 is proposed and
  being validated.**

**Hero exhibit (static in Phase 1).** In place of the v1.0 interactive proof, render one complete,
static, clearly illustrative answer — the same fixture the rest of the site uses — so the promise is
concrete in the first viewport without simulating a runtime:

- **Current decision:** Free workspaces allow five active members.
- **Why:** The original decision cites a support-cost threshold and a conversion experiment.
- **New evidence:** A later cohort result contradicts the original cost assumption.
- **Impact:** The entitlement API, onboarding copy, pricing page, and tests depend on the decision.
- **Next action:** Review the proposed change from five to seven members.
- **Source:** `Illustrative fixture — not customer or production data.`

It carries the labels `Illustrative` and `V2 direction`. It is static markup; the interactive version is
Appendix B, Phase 2.

### Section 2 — The problem: product archaeology

Lead with the consequence, not a history lesson:

> Every agent session starts smart and forgets the product. Teams pay for that amnesia through repeated briefings, re-litigated decisions, unexplained code, and documentation that cannot say what is current.

Use a compact before/after comparison:

| Without durable product memory | With durable product memory |
|---|---|
| Context scattered across files, tools, and conversations | Accepted knowledge has durable addresses and provenance |
| Proposed changes overwrite or bypass current truth | Current and proposed meaning remain distinct |
| An agent sees prose but not authority or history | Context includes evidence, status, relationships, and supersession |
| Release learning disappears into chat and dashboards | Reality can challenge intent and propose the next change |

The Waterfall → Agile → Context Engineering manifesto is an essay (Appendix C #3–4), not the homepage
opener. Link to it; do not repeat it before the visitor has seen concrete value.

### Section 3 — The Product Management loop

Render the loop as five user verbs, with Check visibly crossing the sequence:

1. **Explore** — gather evidence and surface uncertainty.
2. **Shape** — turn evidence into a coherent proposed change.
3. **Decide** — accept, reject, revise, deprecate, or supersede with rationale.
4. **Build** — compile relevant context, implement, trace, and verify.
5. **Learn** — compare intent with customer and operational reality.
6. **Check** — detect conflicts, stale assumptions, missing evidence, and drift at every stage.

Label it `Design direction` until R0. Avoid presenting the current ten lifecycle stages or dozens of
skills as primary navigation; they remain valuable playbooks behind the simpler surface, and the
repository documents them.

### Section 4 — The decision boundary (static specimen)

Continue the hero's fixture as one small semantic-change specimen, labeled `Proposed later workflow`:

```text
CURRENT      BR-104 · Free plan member limit · Accepted
EVIDENCE     CFD-140 · New cohort result · Contradicts current assumption
PROPOSED     CHG-142 · Change limit from five to seven
IMPACT       API contract · onboarding copy · pricing page · tests
DECISION     Accept · Reject · Revise
HISTORY      Original decision and rationale remain queryable
```

This is illustrative data. Never imply it is GearHeart customer evidence or a live customer system. Explain
the point in one sentence:

> AI can generate options; only an attributable decision turns an option into organizational memory.

### Section 5 — The eight moments (teaser)

The M1→M8 arc as a single row or rail — Problem · Persona · Commercial · Journeys · Tech & Risk ·
Sequencing · Go to Market · Verdict — each with its one-line clarity anchor and a link to its canon page.
The status chip reads `Design direction — research input`. No template screenshots until they exist.

### Section 6 — V2 promises being proven

Present these as commitments being proven, not shipped behavior:

- **Markdown you own** — accepted product memory stays inspectable and version-controlled.
- **Local by default** — usable in files and Git; the current product path does not depend on a hosted service.
- **Durable addresses** — typed IDs keep decisions, journeys, contracts, evidence, code, and tests referable.
- **History without erasure** — rejected and superseded meaning remains available.
- **Derived speed** — query indexes and views can be rebuilt from the canonical files.

Do not lead this section with database brands or a file tree.

### Section 7 — Latest essays

The three newest pieces (title, dek, date, reading time). Link to the Essays index and RSS.

### Section 8 — Current foundation and V2 direction

An honest transition block:

- **Available today:** the open PRD-Led Context Engineering methodology on GitHub — templates, skills,
  hooks, readiness scoring, the human review layer. Present its adoption path only after the public
  commands and links are verified.
- **Being proven next:** a smaller product surface over the same Markdown SoT, IDs, relationships,
  temporal history, and governance principles — first as read-only inspection of an existing repository.
- **First proof:** useful findings from an existing repository before a user learns the ontology.

Link the canonical repository and, when they exist, Releases/Changelog. Do not use stale readiness files,
old skill counts, or roadmap prose as live telemetry. The Compatibility Inspector may be named in one
sentence here; its four-outcome table from v1.0 moves to The Method page under `Proposed alpha`.

### Section 9 — Final action

**Headline:** Build with memory now. Follow the thinking as V2 becomes real.

- Primary: **Use the template** (the repository's "Use this template" path, once verified) or **Explore the methodology**.
- Secondary: **Read the essays** · **Follow on LinkedIn**.
- Tertiary: **Subscribe** (RSS / newsletter) — only where a real destination exists.

After a verified V2 release, replace these actions through the central status/config model rather than
editing multiple page sections.

## 8b. The editorial spine: canon pages and the essay series

### Canon page anatomy (one page per moment, M1–M8)

Every canon page has the same skeleton so the eight read as one arc:

1. **Kicker and title** — "Key Moment 03 · Commercial Model".
2. **The charter** — the owner's articulation, verbatim, set as a pull quote. These sentences are the
   requirements; do not paraphrase them.
3. **What this moment settles** — the clarity anchor in one paragraph (e.g. M3: the engagement-model
   statement — frequency, ecosystem, what it replaces and what the switch costs — with pricing as a clause).
4. **Where it sits in the loop** — which verbs prepare it and which it terminates in, using only the
   public vocabulary.
5. **What the page reads and what it writes** — in plain words ("it reads the evidence you gathered;
   completing it records the decision"), never plane names or record prefixes.
6. **How it will look** — the visual direction as a prose sketch drawn from the canon's *Visual expression*
   block (the annotated sentence; the negative persona card; the engagement statement with a frequency
   strip; the journey map with an emotional-temperature band; the invest-vs-optimize map over a sortable
   register — no 5×5 heat map; the dependency DAG with the beta line — no Gantt; the one-pager with the
   reconciliation table; the scorecard with the verdict as hero). Prose only until templates exist; then a
   labeled `Illustrative preview` screenshot.
7. **Status chip** — `Design direction — research input pending R0` (M8 additionally: `proposed addition`).
8. **The essays that go with it** — links into Appendix C.
9. **Provenance footer** — source document, section, and the reviewed commit; the brief's claim class.

### Essay anatomy

Title · dek · author · date · reading time · truth class chip (`Position` / `Design direction` /
`Practice`) · a **"What exists today"** box fed by the central status model whenever an essay touches a
capability · body · a single next step (repository, a canon page, or the next essay) · provenance footer
(source document + commit where the essay draws on the repository) · the `linkedinCut` (the 150–300-word
LinkedIn version, stored with the essay, §8c).

Voice: the Editorial Luxury voice guide (§9.3) — contemplative, editorial, human-problem-first, precise,
restrained. Complete sentences; paragraphs that breathe; no bullet salad; the confidence to under-claim.

### Cadence

Phase 1 ships with the thesis essay plus five to seven more (Appendix C, series 1 and the canon
overview). Thereafter one essay per one to two weeks, alternating series; each Key Moment spotlight is
timed with its template's design session so the essay can carry a real illustrative preview when one exists.

## 8c. Distribution: LinkedIn → essay → repository

- **LinkedIn is the primary channel**, posting from the owner's personal profile (company page secondary —
  owner decision). Post types rotate: thesis long-form, story, contrarian short, carousel/diagram,
  aphorism, build-in-public (releases, readiness, the review layer), list, moment spotlight, and
  "why we rejected X" departures.
- Every essay stores its own `linkedinCut`; the post links to the essay with a UTM convention
  (`utm_source=linkedin&utm_medium=social&utm_campaign=<series>&utm_content=<slug>`).
- **Canonical rules**: the site is canonical for every essay. LinkedIn and Substack carry an excerpt plus a
  link (or a full cross-post with `rel=canonical` back to the site where the platform allows it) — owner
  decision on Substack's role.
- No paid promotion, automation, or engagement claims are implied on the site.
- The repository's Releases page is a post source too (build-in-public); the polish plan's release hygiene
  feeds this.

## 9. Visual direction

### 9.1 Direction selected: Editorial Luxury

The site adopts the owner's **Editorial Luxury** design language in full — the language names
GearHeartAI.org as its canonical home, and today the live site is the one surface not running it. The
homepage's visitor mode is still **Persuade**: intelligible, desirable, provable, and actionable in the
first viewport; readability governs everything below. Nested sections do not become separate visual
worlds.

Tokens to vendor into the site repository (values as of 2026-08-19; the vendored `tokens.css` is the
source of truth):

| Token | Value | Role |
|---|---|---|
| luxury cream | `#F9F8F6` | page background |
| ink black | `#1A1A1A` | primary text |
| antique gold | `#C5A065` | the single accent |
| paper white | `#FFFFFF` | elevated surface |
| cream dark | `#F5F5F0` | recessed surface |
| gold wash | `rgba(197,160,101,0.2)` | soft overlay |
| ink soft | `rgba(26,26,26,0.6)` | secondary text |
| editorial navy | `#1E3A5F` | optional, editorial spreads only |

Typography: **Playfair Display** for headlines, **Inter** for body, **JetBrains Mono** for data, code, and
IDs (never decorative). Scale: hero 72/1.1 · section 48/1.2 · subsection 32/1.3 · body-lg 20/1.6 · body
16/1.7 · label 12/1.4. Spacing on a 4-pt grid. Radius 0/2/4/6 px — no pill buttons, no rounded-xl cards.
Shadows near-none (`0 1px 2px` → `0 8px 24px` at 4–8 % ink); no glow, no coloured shadows. Motion:
`fade-in` 0.4 s, `fade-up` 0.6 s, `reveal-line` 0.8 s, ease-out / `cubic-bezier(.4,0,.6,1)` — mechanical,
not playful, nothing spring-based; no hover motion (colour only, never scale or position). **Light-first;
no dark mode.** Photography-forward over iconography where imagery is used at all.

Components already specified in the language: `Button` (ink on cream or gold on ink; 4 px radius; no
shadow), `ID Pill` (JetBrains Mono, ink on gold wash — a PRD-CE signature element), `Pull Quote` (Playfair,
`reveal-line` on scroll, no quote glyphs), `Section Title` (ink underline animating in), `Bento Grid Card`.

**Deprecated — migrate off, do not carry forward**: electric cyan `#64ffda`, heart orange `#FF7A3D`,
obsidian / midnight-slate / deep-indigo backgrounds, `pulse-soft`, glow shadows, Poppins — i.e. the live
site's current look.

### 9.2 Relationship to the repository's own HTML system

The repository's review layer (`SoT/html/`) and the future Key Moment templates use a *cousin* system —
warm paper, ink, a single ochre spot, serif/grotesque/mono — governed inside the repo. **Embedded repo
specimens keep their own tokens**: a screenshot of the Atlas or a moment preview is an artifact, framed
and captioned, not restyled. The site chrome is Editorial Luxury; the artifacts inside it are the
method's.

### 9.3 Voice

Every piece reads as at least three of: **contemplative** (complete sentences, paragraphs breathe),
**editorial** (magazine essay, not product pitch), **human-problem-first** (open with the friction),
**precise**, **restrained** (the confidence to under-claim; never shouts). Banned: "unlock the power of",
"blazing-fast", "revolutionary / disruptive / game-changing", "AI-first", "superpowers", "out of the box /
plug and play", "delightful", all-caps emphasis, exclamation points, "in today's fast-paced…", promising
transformation in a timeframe, invented jargon ("Source of Truth" is allowed because it is the method's
term). The test: *could this appear in Monocle without being the ad?*

### 9.4 Boundaries (unchanged from v1.0)

- Preserve the verified GearHeart name, mark, and binding brand assets unless the owner separately approves a replacement.
- Demonstrate the method with inspectable evidence, decision, lifecycle, delivery, and history states — not decorative AI imagery or a generic node cloud.
- Make source annotations, status, contradiction, impact, and time legible without requiring graph vocabulary.
- Keep the first viewport specific: one promise, one visible exhibit, and one real action.
- Do not copy Impeccable's assets, composition, palette, typography, command names, or motion.
- Avoid generic AI-site defaults — glowing gradients, arbitrary icon tiles, nested card grids, pill saturation, empty cinematic scroll space.
- Use no factual claim, customer, benchmark, screenshot, or capability that the product record and provenance model do not support.

### 9.5 Motion language (Phase 2 with the proof interaction; Phase 1 uses only the language's three transitions)

Motion should explain state change: evidence enters; a contradiction becomes visible; a proposed change
shows its impact; a human decision changes current state; prior state moves into history without
disappearing. Avoid continuous ambient animation, scroll capture, parallax that delays reading, or motion
that simulates a working runtime. Respect `prefers-reduced-motion`; the reduced-motion version must
preserve meaning and hierarchy.

## 10. Impeccable workflow in the site repository (process, not template)

The visual direction is now selected (§9), so the new-world direction-selection cycle is not needed.

1. Read the site repository's governing instructions, content model, routes, dependencies, components,
   analytics, deployment configuration, and dirty worktree state.
2. Run Impeccable context resolution once for the homepage target. If `PRODUCT.md` is missing or
   materially stale, run `init` and complete its product-truth interview (audience, purpose, evidence,
   constraints, platform, open decisions). It does not choose a visual world.
3. Treat the incumbent interface as evidence of what to replace. Vendor the Editorial Luxury tokens and
   voice; write the new `DESIGN.md` from the finished build (documenter), not from intentions.
4. Implement the approved composition within the existing stack; reproduce the first viewport before
   extending the rest of the page; then the Method, Key Moments, and Essays surfaces.
5. Inspect bounded desktop and mobile renders, fix material gaps, run the deterministic detector once after
   the UI is finished, then the fresh finish reviewer with the request, this brief, screenshots, target, and
   detector findings; close or explicitly disposition material findings; run the documenter.

Human approval is required at these boundaries: accepting the high-fidelity composition; changing the logo
or brand identity; publishing new product names, install commands, availability claims, customer proof,
pricing, or dates; adding a dependency with material bundle, security, or maintenance cost; deploying to
production.

## 11. Sustainable implementation guidance

- Reuse the existing framework and design primitives. Do not rewrite the site or upgrade its framework merely to achieve the redesign.
- Store status-sensitive product copy and destinations in one schema-validated content module. Components render it; they do not each own a copy.
- **Content pipeline**: essays and canon pages are Markdown/MDX files in the site repository with a
  validated frontmatter schema — `title`, `dek`, `date`, `author`, `series`, `truthClass` (A/B/C),
  `sourceDoc` + `sourceCommit` (when drawing on the repository), `linkedinCut`, `canonical`, `ogImage`.
  RSS/Atom and `sitemap.xml` are generated at build from the same files. Canon pages quote the charters from
  `V2_KEY_MOMENTS.md` and record the commit they were taken from.
- Keep the illustrative fixture in a clearly named module; the same fixture feeds the hero exhibit, the
  specimen, and (Phase 2) the proof interaction and its tests.
- Use semantic component boundaries based on user meaning — `ProductAnswer`, `ChangePreview`,
  `CapabilityStatus`, `ProductLifecycle`, `MomentCard`, `EssayCard`, `ProvenanceFooter` — without a generic
  design-system abstraction for one-off sections or speculative products.
- Preserve progressive enhancement. Essential copy and source links exist in server-rendered or static markup.
- Prefer CSS and the language's three transitions. Add a motion or visualization library only after
  demonstrating that the existing stack cannot express an approved interaction accessibly and performantly.
- Generate dynamic counts and compatibility lists from a single manifest. If no canonical manifest exists, omit the number.
- Validate all external links and remove dead navigation rather than shipping placeholders.
- Keep website facts attributable to a repository commit or release identifier.

## 12. Accessibility, performance, and resilience

### Accessibility

- Semantic landmarks and one logical `h1`.
- Full keyboard operation and visible focus for navigation and any interactive element.
- WCAG AA contrast for text and controls in every state.
- Accessible names and state for tabs, toggles, copy buttons, and expandable details.
- Result changes announced without stealing focus.
- No information encoded only by color, animation, or spatial position.
- Reduced-motion behavior tested, not merely declared.
- Screen-reader order matches the visual argument.

### Performance targets

Unless the existing project defines stricter budgets, target:

- LCP at or below 2.5 seconds on a representative mobile production build.
- CLS at or below 0.1.
- INP at or below 200 milliseconds.
- No autoplay video or hero media required to understand the site.
- Responsive images, subset fonts, and no decorative asset that dominates initial transfer size.

Record the test environment with the result. Do not present lab scores as universal field performance.

### Resilience

- Core narrative, essays, and source links remain usable with JavaScript disabled.
- Any interactive preview has a readable static default.
- Failed analytics, newsletter, or third-party scripts do not block content.
- External requests have explicit purpose; avoid sending repository or visitor context to third parties.

## 13. Responsive behavior

Validate at minimum 390 px mobile portrait · 768 px tablet portrait · 1024 px compact desktop/tablet
landscape · 1440 px desktop · a wide display representative of the current site's presentation
environment. The hero exhibit follows the headline on narrow screens rather than shrinking into
illegibility; semantic diffs wrap by field and retain status labels; the loop may become a vertical
sequence on mobile; the M1→M8 rail may become a list. Essay measure ≤ 70 characters per line at every
width. Do not hide critical evidence or availability labels at smaller breakpoints.

## 14. SEO and sharing

Recommended pre-release defaults, subject to final naming approval:

- **Title:** `GearHeart AI | PRD-Led Context Engineering`
- **Description:** `Memory as Infrastructure — the thinking behind PRD-Led Context Engineering, an open, local-first method for building products with AI agents, with the eight Key Moments and an essay series.`
- **Primary phrase:** `AI product memory`
- **Supporting phrases:** `context engineering`, `PRD-Led Context Engineering`, `AI product management`, `product knowledge graph`, `memory as infrastructure`
- **Per-page**: each essay and canon page has its own title, description, canonical URL, and OG image.

Required: a real `og-image.png` (1200×630) that shows the promise — the exhibit or the M1→M8 arc, visibly
labeled as direction where applicable — not generic AI imagery; canonical host chosen (www vs apex) with
the other redirecting; `sitemap.xml`; `robots.txt`; RSS/Atom for essays; `Article` structured data for
essays (real content — allowed); Organization metadata where facts are verified. Do not publish
SoftwareApplication or SoftwareSourceCode structured data for V2 until a public release and canonical
artifact exist.

## 15. Measurement

Use the site's existing analytics abstraction. Do not add a new provider from this brief.

| Event | Meaning |
|---|---|
| `essay_read` | An essay reaches a scroll/time threshold |
| `moment_view` | A canon page is viewed (with the moment id) |
| `github_open` | Visitor opens the canonical repository |
| `template_use` | Visitor opens the "Use this template" / methodology start destination |
| `linkedin_referral` | Arrival with the LinkedIn UTM convention (campaign + content) |
| `rss_subscribe` | RSS/newsletter destination opened |
| `lifecycle_stage_view` | Visitor examines a loop verb or proof section |
| `product_model_explore` / `product_question_select` | Phase 2 — the proof interaction (Appendix B) |

Do not collect the content of arbitrary visitor input. Phase 1 offers no free-form input.

Success signals for the redesign:

- A first-time visitor can explain the core idea after the hero and one essay.
- The visitor can distinguish what is available now from what is proposed.
- The primary CTA reaches a real next step; the LinkedIn → essay → repository funnel is measurable without invasive tracking.
- Every essay and canon page stands alone as a landing page.

## 16. Verification and acceptance criteria

### Content and truth (Phase 1)

- [ ] The approved naming stack is used consistently: PRD-Led (never "driven" in prose); Memory *as* Infrastructure; "The Product Model" only in its labeled appendix note, if at all.
- [ ] Every capability has one explicit status sourced from the central content model; every class-A/C record carries `sourceUrl`, `sourceCommitOrRelease`, `verifiedAt`; the build fails closed when required provenance is missing.
- [ ] Every essay and canon page carries date, author, truth-class chip, and provenance footer; canon pages quote the charters verbatim and use only the public vocabulary.
- [ ] No unverified install command, feature count, integration, customer, metric, testimonial, or release date appears; no screenshot of an unbuilt capability.
- [ ] No adjacent product or future methodology is named, marketed, previewed, or measured.
- [ ] Repository and source links resolve; the repository is linked from the header action or footer and from every method claim.
- [ ] Fixture data is labeled illustrative.

### Product experience (Phase 1)

- [ ] The hero leads with "Your product should remember." (or approved replacement) and a concrete static exhibit.
- [ ] The page explains Explore → Shape → Decide → Build → Learn and cross-cutting Check, labeled as direction.
- [ ] The eight moments are reachable from the homepage; each canon page follows the §8b anatomy.
- [ ] Essays index, article template, RSS, and the first six to eight pieces ship; the first actionable destination is one click away.
- [ ] `/essays`, `/moments`, `/method` resolve (no redirect to `/`); no dead links or placeholder routes.

### Design quality

- [ ] Editorial Luxury applied: palette, type, spacing, radius, motion, voice; the deprecated dark/cyan language is gone.
- [ ] Embedded repository specimens are framed artifacts with their own tokens, not restyled.
- [ ] No copied Impeccable assets, composition, or black/gold identity.
- [ ] The Impeccable process steps in §10 are complete; P0/P1 findings resolved; lower-severity exceptions have written rationale; `DESIGN.md` records what shipped.

### Engineering quality

- [ ] Existing stack, deployment, analytics, and legal surfaces remain functional.
- [ ] Lint, type checks, build, and existing tests pass; the content schema validates every essay/canon file.
- [ ] `og-image.png` (1200×630) resolves; `sitemap.xml`, `robots.txt`, RSS resolve; canonical host enforced.
- [ ] Responsive checks pass at the required widths; keyboard, screen-reader, contrast, reduced-motion, and no-JavaScript checks pass.
- [ ] Performance budgets met or a measured exception documented.
- [ ] Production deployment occurs only after user approval and preview review.

### Phase 2 additions

- [ ] The proof interaction (Appendix B) works by keyboard, exposes selected state, announces result changes, renders a complete static answer without JavaScript, and is driven by the shared fixture and tests.
- [ ] Moment previews are real renders of built templates, labeled `Illustrative preview`.

## 17. Agent execution order (Phase 1)

1. Inspect the site repository and report stack, instructions, routes, content sources, design tokens, test commands, deployment path, analytics, and any dirty worktree state.
2. Verify the capability/content matrix (§4.2) against public and repository evidence at the recorded commit. Return discrepancies before changing public claims.
3. Resolve Impeccable context once; complete `init` only if product truth is missing or stale.
4. Vendor the Editorial Luxury tokens, voice, and component specs into the site repository.
5. Author content: the canon pages (charters verbatim from `V2_KEY_MOMENTS.md`, commit recorded) and the Phase-1 essays (Appendix C), each with frontmatter, truth-class chip, provenance footer, and `linkedinCut`.
6. Build routes: `/`, `/method`, `/moments`, `/moments/<m1…m8>`, `/essays`, `/essays/<slug>`, `/rss.xml`, `/sitemap.xml`, `/robots.txt`; redirect the legacy anchors sensibly.
7. Implement the homepage composition (§8) with the static exhibit and the shared fixture; reproduce the first viewport before the rest.
8. Ship SEO/OG metadata, the real `og-image.png`, canonical host.
9. Run bounded desktop/mobile inspection, the one detector pass, the fresh finish review, accessibility, responsive, performance, and engineering checks. Record `DESIGN.md` from the reviewed build.
10. Provide a preview URL or local review path plus screenshots at the required widths; report changed files, verified claims, proposed-only content, test results, reviewer disposition, and intentional exceptions.
11. Wait for explicit approval before production deployment.

## 18. Owner decisions before public release

Recommended defaults authorize discovery and preparation of a reviewable build. They do not authorize
bypassing the composition approval gate, publishing changed product claims, or deploying to production.

| Decision | Recommended default |
|---|---|
| Public name stack | **PRD-Led Context Engineering** · thesis **Memory as Infrastructure** · label **V2**; "The Product Model" demoted to Appendix A |
| Hero promise | **Your product should remember.** |
| Pre-release primary CTA | **Read the thesis** (or **See the eight moments**) |
| Pre-release secondary CTA | **View PRD-CE on GitHub** |
| V2 availability language | **Proposed and being validated** |
| Canon pages before R0 | Publish, labeled `Design direction — research input`, public vocabulary only |
| LinkedIn handle | Owner's personal profile primary; company page secondary |
| Substack | Excerpt + canonical link to the site (or cross-post with canonical) |
| Dark mode | None — Editorial Luxury is light-first |
| Canonical host | Pick www or apex; redirect the other |
| Plugin / install CTA | Only after a verified end-to-end install |
| Proof interaction | Phase 2 |
| Product scope | Product Management lifecycle only; do not market future products |
| Brand direction | Editorial Luxury; evolve the GearHeart identity, do not imitate Impeccable |
| Production release | Preview and explicit owner approval required |

## 19. Brief completion definition

The update is successful when GearHeartAI.org feels like the home of a body of thought: one promise, one
thesis, eight moments, a living essay series, and one honest next step into the open repository — with
deeper rigor available on demand, and not a single claim ahead of what exists.

---

## Appendix A — "The Product Model" (working name, demoted)

v1.0 of this brief organised the site around **The Product Model** as the working public name for the
Product Management lifecycle experience, with the reference line "The Product Model — the next generation
of PRD-Led Context Engineering." PRD open decision 1 (approve, reject, or replace the name before its v0.3
category and packaging gate or any public use) remains open. Until it is resolved, the site leads with
PRD-Led Context Engineering and the thesis line, and may mention "The Product Model" only in a clearly
labeled note ("working name for the proposed V2 experience; not an approved product name").

## Appendix B — The proof interaction (deferred to Phase 2)

Retained verbatim from v1.0 so the Phase-2 implementation has its contract.

**Hero proof interaction.** Show an inspectable answer rather than an abstract graph. Use the same clearly
illustrative product-decision fixture throughout the hero, adjudication section, motion story, and tests.
Recommended default question:

> Why is the free workspace limit five members?

Recommended answer structure:

- **Current decision:** Free workspaces allow five active members.
- **Why:** The original decision cites a support-cost threshold and a conversion experiment.
- **New evidence:** A later cohort result contradicts the original cost assumption.
- **Impact:** The entitlement API, onboarding copy, pricing page, and tests depend on the decision.
- **Next action:** Review the proposed change from five to seven members.
- **Source:** `Illustrative fixture — not customer or production data.`

Offer two additional deterministic questions if they improve the interaction without obscuring the page:
**What depends on this decision?** · **What changed after the new evidence?**

The interaction must visibly carry both labels: `Illustrative` and `V2 interaction preview`. It must work
by keyboard, expose selected state, announce result changes accessibly, and render a complete static answer
when JavaScript is unavailable. It is a product preview, not a chat box; do not accept free-form input
unless a real system handles it. Build it as deterministic, local presentation state; do not introduce a
backend for a preview. The motion narrative of §9.5 applies (evidence enters; a contradiction becomes
visible; a proposed change shows its impact; a human decision changes current state; prior state moves
into history without disappearing).

Phase-2 navigation may add **Proof / Explorer** once the interaction exists and is maintained.

## Appendix C — Initial content list

Sequence is the owner's call; series 1 and the canon overview are the Phase-1 minimum. Class per §4.1.

| # | Piece | Angle | LinkedIn post type | Class |
|---|---|---|---|---|
| **Series 1 — The thesis** | | | | |
| 1 | Your product should remember | Agent amnesia is a product-management problem, not a tooling problem | Thesis long-form | B |
| 2 | Memory as Infrastructure | The founding essay: two converging experiences, the Golden Rule ("if it isn't in the memory infrastructure, it isn't true") | Thesis long-form | B |
| 3 | Product archaeology | The tax: re-briefing, re-litigated decisions, unexplained code, documentation that cannot say what is current | Story | B |
| 4 | The Cognitive Shift | Sprints → context windows; user stories → prompts; tribal knowledge → Source of Truth; standups → hooks; project management → context governance | Carousel | B |
| 5 | PRD-Led, not PRD-driven | What a PRD is *for* when agents build, and why "led" | Contrarian short | B |
| 6 | Only a decision becomes memory | AI generates options; an attributable decision turns an option into organizational memory | Aphorism + essay | B |
| **Series 2 — The practice (what exists today)** | | | | |
| 7 | One document, many versions | Why there is never a `PRD-v2.md`; progressive documentation | Practice | A |
| 8 | A repo that scores its own readiness | Three-layer readiness, causal blockers, "the highest-leverage fix is rarely the lowest score" | Build-in-public | A |
| 9 | The human review layer | SoT pages a reviewer actually wants to read — with the real screenshots | Build-in-public (visual) | A |
| 10 | Markdown you own | Local-first product memory; no database, no SaaS, no lock-in; how to start | Build-in-public | A |
| **Series 3 — The canon** | | | | |
| 11 | Five verbs and a Check | Why ten stages collapse into a loop — Explore, Shape, Decide, Build, Learn, Check | Carousel / diagram | B (direction) |
| 12 | Eight moments where clarity is the product | The canon overview, thesis to reckoning | List post | B |
| 13 | M1 · The evidence-footnoted sentence | The spark formula; hedge honestly; tier-5 speculation struck through | Spotlight | B |
| 14 | M2 · The negative persona | "We will not chase this buyer"; behaviour over demographics; the five-card cap | Spotlight | B |
| 15 | M3 · Engagement model before price | Frequency, ecosystem, what it replaces and what the switch costs; pricing as a clause | Spotlight | B |
| 16 | M4 · Emotional temperature and the money shot | The journey map as a set of design decisions; delight vs. utilitarian | Spotlight | B |
| 17 | M5 · Why we rejected the 5×5 heat map | The invest-vs-optimize map over a quantified register (Cox 2008, Hubbard) | Departure ("we rejected X") | B |
| 18 | M6 · Order is not a date | The dependency DAG and the beta line; why no Gantt | Departure | B |
| 19 | M7 · The feedback contract | The launch one-pager with the reconciliation table as its spine | Spotlight | B |
| 20 | M8 · The reckoning | Scale, iterate, pivot, or kill — the scorecard, the grade, the verdict recorded so no session re-litigates it (proposed addition) | Spotlight | B |

## Brief changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-08 | Product-marketing brief: "The Product Model" naming stack, hero proof interaction, truth-boundary table, Impeccable new-work flow |
| 2.0 | 2026-08-19 | Re-centred as the home of the thought leadership (hybrid): outcome hero kept; body = Key Moments canon + essay series; three claim classes; PRD-Led Context Engineering leads with "Memory as Infrastructure" as the thesis; Editorial Luxury selected; LinkedIn → essay → repo distribution; proof interaction deferred (Appendix B); "The Product Model" demoted (Appendix A); live-site audit findings recorded; frontmatter branch/commit language updated |
