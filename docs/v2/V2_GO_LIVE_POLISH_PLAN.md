---
title: "PRD-CE V2 · Go-Live Polish Plan (gap analysis)"
version: 1.2
date: 2026-08-19
status: "Maintainer planning record + living tracker — gap analysis; authorizes nothing (PRD.md authority order, item 7). §7 is the status table: update it as items close."
purpose: "Define what a polished go-live means for this repository and its companion site, inventory the gaps against that bar, and sequence the missing steps — across three lenses: Key Moments visual polish, repository organization, and repo polish for promotion."
origin: "Owner-requested go-live polish review, 2026-08-19 (three read-only repo/GitHub/site sweeps + one structural design pass)."
companions:
  - "docs/v2/audit/v2-todo.md — the gate-sequenced v2 repo to-do (21 items). It owns the v2 update list; this plan cites its item numbers and never restates them."
  - "docs/v2/V2_KEY_MOMENTS.md v1.2 — the canon and design briefing this plan sets the polish bar for."
  - "docs/v2/GEARHEARTAI_PRD_CE_V2_SITE_BRIEF.md v2.0 — the companion-site brief (thought-leadership home)."
  - "docs/v2/PRD_CE_V2_BUILD_PLAN.md §11 — the merge bar for the v2 runtime (Tier 3); not restated here."
  - "PRD.md — product authority; this plan changes no product truth."
scope_guard: "No SoT IDs minted. No file is moved, deleted, or renamed by this document. Every action below is a proposal sized for a follow-up session; the owner decisions in §9 gate the ones that touch public surfaces."
---

# PRD-CE V2 · Go-Live Polish Plan

> **Verdict in one line**: the repository is **under-marketed, not under-built**. The installer is real and
> manifest-driven, the readiness scorer is real and tested, the skills are real, and the SoT HTML review
> layer is the best-looking artifact in its competitive set — but the packaging (first-run experience,
> discoverability, release hygiene, community files), the hygiene (scratch and client-flavored material in
> a public template), and the narrative surfaces (README, site) are where a stranger decides not to star.
> Almost every gap below is a packaging gap, and most are S–M effort.

---

## 0. How to read this — "go live" is three tiers

"Go live" is not one event. It decomposes into three tiers with different gates, and this plan keeps them
apart so that Tier 1 can ship now without borrowing any v2 claim.

| Tier | What goes live | Audience | Entry gate | Exit bar | Approvals |
|---|---|---|---|---|---|
| **T1 · Template-repo go-live** (`main`, now) | The existing methodology as a tight, promotable template: hygiene, cleanup, README polish, community files, GitHub settings, tagged releases | People arriving from LinkedIn / GitHub search; forkers; plugin installers | None — pre-R0, no v2 vocabulary, no v2 claims | §8 T1 checklist; ≥ 25/30 of the §2 polish checklist PASS; community profile 100 %; one GitHub Release published; social preview live | Owner: public settings, releases, removals (§9 D1, D5, D8–D13) |
| **T2 · V2 concept public** | The v2 *story* as thought leadership: the Key Moments canon, the PM loop, the walkthrough, the moment templates as labeled illustrative previews; README "where v2 is going"; site canon pages + essays | Product/engineering leaders; the LinkedIn audience | **R0** for anything stated as methodology truth in the repo; pre-R0 only as dated, labeled owner direction (brief v2.0 claim class B) | §8 T2 checklist; every public artifact carries its truth label | Owner: canon-page publication pre-R0 (§9 D4), site publication (PRD open decision 4) |
| **T3 · V2 runtime alpha** | Read-only Compatibility Inspector (`index / check / query / trace`), the moment pull scripts | Early adopters | Build plan Waves 1–3; v0.7 EPIC | Build plan §11 minimum merge bar (13 items) — not restated here | Owner: merge and release as separate decisions (BR-003) |

**Branch strategy for T1 — decided 2026-08-19 (D1): everything lands on `prd-ce-v2`; `main` waits for the v2 merge.** (The original recommendation, kept for the record:) `main` today is v3.2.0: `PRD.md` is
the *generic template PRD* (no `PRD_template.md` / `SoT_template/` exist there), the README is 389 lines,
and `main` is 14 commits behind `prd-ce-v2`. The Wave 0B split (root authority vs. downstream seeds,
`.claude/VERSION` 3.3.0, plugin payload refresh, distribution tests) lives only on the v2 branch, which
BR-003 keeps isolated until an explicit merge decision. Recommendation: **execute T1 on a branch cut from
`main`** (vocabulary-neutral polish only), merge by PR under the existing CI (tests · plugin-sync · link
check), then reconcile `main → prd-ce-v2` per build plan §11. Whether Wave 0B itself lands on `main` ahead
of the v2 runtime — as a "v3.3.0 template release" — is a separate owner decision (D2); it is template
hygiene, not a V2 runtime release, but it changes what a forker sees at root.

What this plan is not: not a build plan (Waves live in `PRD_CE_V2_BUILD_PLAN.md`), not a PRD change, not the
v2 repo to-do (`docs/v2/audit/v2-todo.md` owns that; crosswalk in §4.6).

**How to use this document as the tracker (v1.1).** §7 holds every actionable item with an owner
(*Claude* executes · *Matt* creates · *Matt-approve* decides) and a status (`☐` open · `◐` in progress ·
`☑` done · `⊘` dropped). §9 is the decision packet — each decision with options, recommendation, and a
slot for the call; the decision log at its end records outcomes. §10 holds the starting points for the
creative items Matt owns. Close an item by flipping its status and adding the date; nothing else in the
document needs to change.

---

## 1. Executive summary

**The three P0 hygiene items (do first, no gate; §4.2):**

1. Client-flavored material tracked in a public template: `temp/v0.5-requirements/prd-v05-technical-stack-selection/` — eight files: a forked copy of a shipped skill with a vendor catalog, plus `LEARNINGS-LIGHTSTACK.md` (addressed to a named individual about a named client ecosystem). Present on `main`.
2. A committed directory named after the owner's local filesystem path: `.claude/projects/-Users-<owner>-…/memory/` (3 files, Feb 2026 retro). Manifest class `never_touch` protects the *runtime dir*, not this content.
3. Absolute `/Users/…` paths inside `temp/v2-audit/impeccable/{router,shape,build}.md`. The distribution leak test covers distributable surfaces only; `temp/` is unscanned.

**The twelve highest-leverage polish gaps, ranked by star-impact (§5 has the work):**

| # | Gap | Fix (one line) | Size |
|---|---|---|---|
| 1 | No custom social preview — every LinkedIn share renders GitHub's default grey card | Upload a 1280×640 preview cropped from `atlas.png` on the cream/ink/gold ground | S |
| 2 | The hero has no line that says what you *get*; the real hook (the amnesia line) is buried in italics under four badges | **Tagline stays** — "Memory as Infrastructure" has performed well (owner, 2026-08-19). Add a **subtitle** that does the verb + outcome + audience work (candidates in §10.1) and promote the amnesia lede | S |
| 3 | No motion proof — six stills, zero demo | 20–30 s GIF of `readiness.py run` blocking a gate then passing, or the loop SVG | M |
| 4 | No one-command start; "Use this template" is live (`isTemplate: true`) but never mentioned | One copy-paste line leads Quick Start; a **Use this template** link in the hero | S |
| 5 | Repo description/topics stale and off-brand (`nextjs`, `supabase`; "PRD-driven") | Description = the tagline; topics `claude-code context-engineering spec-driven-development ai-agents agentic-coding prd agent-skills templates` | S |
| 6 | Zero tags and zero releases for five shipped CHANGELOG versions | Backfill `v1.0.0`–`v3.2.0`; publish a release with the existing notes; every release becomes a LinkedIn post | S |
| 7 | Community profile at 42 % (no CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, issue/PR templates) | Extract README §Contributing into `CONTRIBUTING.md`; add the other four files | S |
| 8 | `main`'s Quick Start runs `python scripts/readiness.py run` with no dependency install and a bare `python` | `python3 -m pip install -r scripts/requirements.txt` then `python3 …` (already fixed on the v2 branch) | S |
| 9 | `homepageUrl` empty; Discussions off; Wiki on; the site never links back | Set homepage; enable Discussions; disable the empty Wiki; add the repo CTA to the site | S |
| 10 | gearheartai.org: `og-image.png` 404s; deprecated cyan/dark palette; no repo link; no writing surface; no sitemap/robots | Brief v2.0 Phase 1 | M–L |
| 11 | README marketing assets live in `temp/` — the directory the method tells forkers to clear | Move the six PNGs to `docs/assets/`; update seven README refs + `SoT/html/README.md` + `screenshot.py` (both trees) | S |
| 12 | README is 432 lines with a wrong skill count in four places + an anchor, and an empty Squad Status table | Generate or drop the count; delete Squad Status from the public README; move Contributing/tree/install into `docs/` behind an index | M |

---

## 2. What "polished" means for a methodology/template repo

The bar is empirical. The repos that win in this category share five patterns: **(1)** every repo above
~5k stars leads with exactly one command (`uvx` / `npx` / `/plugin install` / "Use this template"); **(2)**
the tagline is verb + outcome + audience in ≤ 14 words; **(3)** motion beats stills — a GIF, an SVG loop
diagram, or an embedded video sits under the tagline; **(4)** every repo above ~25k has a docs front door
(a docs site, or at least `docs/index.md`); **(5)** the counter-example that matters most —
`coleam00/context-engineering-intro` (~14k stars) has no docs site, no releases and near-zero community
files; it has one memorable claim, a "Use this template" button, and five numbered steps. That is the
minimum viable star engine, and it is PRD-CE's closest structural twin at roughly 70× the stars on a
fraction of the substance.

### 2.1 Peer calibration (GitHub-reported counts at review time; approximate)

| Repo | ~Stars | Leads with | Docs site | Template/distribution story |
|---|---|---|---|---|
| obra/superpowers | 274k | one-line thesis; `/plugin install superpowers@…` across 9 harnesses | — | plugin, multi-harness |
| github/spec-kit | 130k | "Define what to build before building it — with any AI coding agent."; `uv tool install specify-cli`; release badge | yes | CLI installer, tagged releases, SECURITY/SUPPORT |
| bmad-code-org/BMAD-METHOD | 52k | banner + SVG "delivery loop"; `npx bmad-method install` | yes | npx installer, Discussions on |
| davila7/claude-code-templates | 30k | screenshot of the browsable catalog; `npx …` | yes | CLI + web catalog |
| eyaltoledano/claude-task-master | 28k | CI + npm-downloads badges; one-click MCP install | yes | npm, example PRD in `init` |
| coleam00/context-engineering-intro | 14k | one extreme claim; **Use this template**; 5 steps | no | use-this-template |
| Wirasm/PRPs-agentic-eng | 2k | embedded YouTube walkthrough; `/plugin install` | no | plugin + copy fallback |

### 2.2 The checklist (30 items) with PRD-CE's current verdict

Verdicts reflect `main` unless noted; ✅ PASS · ⚠️ PARTIAL · ❌ FAIL.

| # | Item | Verdict · evidence |
|---|---|---|
| **(a) Above the fold** | | |
| 1 | One sentence under the H1 that says what you get: verb + outcome + audience, ≤ 15 words | ⚠️ The tagline "Memory as Infrastructure" **stays by owner decision** (it has performed well); the gap is the missing subtitle that names the outcome and the audience — §10.1 |
| 2 | Hero visual within the first screen | ✅ `atlas.png` — the repo's single best asset |
| 3 | Badge row resolves accurately: license · CI · release · stars | ⚠️ 4 badges; no CI badge (3 workflows exist); no release badge (nothing to point at); "PRs welcome" points at a README heading, not a file |
| 4 | Primary CTA above the fold is *install/try*, not *star* | ❌ only CTA is the star ask |
| 5 | No maintainer-internal status text above the fold | ⚠️ clean on `main`; the v2 branch adds a 95-word V2 blockquote with five unexplained internal terms — do not merge as-is |
| **(b) Onboarding** | | |
| 6 | One copy-pasteable command that works on a clean machine | ❌ fork + `cp` ×1–3 + pip + script; the one-paste bootstrap in `BLUEPRINT.md` is buried ~300 lines down |
| 7 | Quick Start references only files that exist on the default branch | ✅ on `main` (`README_template.md` exists); ✅ on v2 |
| 8 | First command succeeds without hidden prerequisites | ❌ on `main`: bare `python`, no `pip install`; fixed on v2 |
| 9 | Explicit "what you get in 5 minutes" outcome statement | ❌ |
| 10 | Prerequisites stated in one place (Python ≥ 3.x, Claude Code, Playwright for screenshots) | ⚠️ scattered |
| **(c) Proof / demo** | | |
| 11 | Animated demo (GIF / video / asciinema) of the loop running | ❌ no motion anywhere |
| 12 | Static screenshots of real output | ✅ six high-quality PNGs |
| 13 | A worked end-to-end example project | ❌ issue #57 open since Feb 2026 |
| 14 | Live CI/test signal visible from the README | ❌ 3 workflows, 0 badges |
| **(d) Community health** | | |
| 15 | GitHub community profile 100 % | ❌ 42 %: CODE_OF_CONDUCT, CONTRIBUTING, issue templates, PR template missing |
| 16 | Discussions on as the Q&A surface; Wiki off if unused | ❌ Discussions off, Wiki on |
| 17 | External PRs triaged within weeks | ❌ PR #68 (external) open since 2026-04-28; #74/#78 in draft for months |
| **(e) Discoverability** | | |
| 18 | Custom social preview (1280×640) uploaded | ❌ `openGraphImageUrl` is GitHub's generated default |
| 19 | Repo description = the tagline, on-brand, names the ecosystem | ❌ "PRD-driven Context Engineering: A systematic approach…" — no Claude Code, skills, hooks, spec-driven terms |
| 20 | Topics accurate and searched-for | ❌ `nextjs`, `supabase` stale; `claude-code`, `context-engineering`, `spec-driven-development`, `ai-agents` absent |
| 21 | `homepageUrl` set to the docs/marketing site | ❌ empty |
| 22 | Docs front door (`docs/index.md` or a docs site) | ❌ 19 loose files, 74 % maintainer-internal |
| 23 | Listed in the relevant awesome lists | ❌ not in `awesome-claude-code` |
| **(f) Release hygiene** | | |
| 24 | Git tag for every shipped version | ❌ 0 tags for 5 versions |
| 25 | GitHub Releases with notes | ❌ 0 releases |
| 26 | CHANGELOG in sync with the version file | ⚠️ `main` consistent at 3.2.0; v2 branch is 3.3.0 with no entry (v2-todo #1) |
| **(g) Template ergonomics** | | |
| 27 | "Use this template" enabled **and advertised** | ⚠️ enabled, never mentioned |
| 28 | Forking cleanly separates template seed from the repo's own content | ⚠️ `main`: root `PRD.md`/`SoT/` *are* the template (clean for forkers, but the repo has no product authority of its own); v2: split into `*_template` (clean, but Quick Start's `cp -R SoT_template/. SoT/` merge-copies instead of replacing) |
| 29 | Installer for adopting into an existing repo | ✅ `install.sh` + `BLUEPRINT.md` + `ghm-self-install`: manifest-driven, idempotent, merges `settings.json` |
| 30 | Plugin/marketplace distribution | ⚠️ `.claude-plugin/marketplace.json` + `plugins/prd-ce/` exist; README correctly labels marketplace availability unverified; manifests carry no `version` |

**Score today: 4 PASS · 7 PARTIAL · 19 FAIL.** The PASSes are substance (screenshots, installer); the
FAILs are packaging.

---

## 3. Lens A — Key Moments: from briefing to polished templates

### 3.1 Where it stands

`docs/v2/V2_KEY_MOMENTS.md` v1.2 is a complete design *briefing* — eight moments with charters, loop
positions, machine faces, and per-moment visual direction; a one-family system (§2.1); three accepted
genre departures (§2.2); a four-stage build order (§2.3); and a vendored research report with citations.
What does **not** exist: a single moment template, a family shell, a fixture, a pull-script schema, or a
line of JavaScript anywhere in the repo. The 40 HTML files in the repo are the SoT companion library
(×3 trees) plus one private walkthrough. And the single decision that most de-risks the build — *which
existing artifact the templates inherit their design system from* — is recorded nowhere: §2 of the canon
says only that "today's hand-authored companion pages are the templates' ancestors."

"Visual polish" for the Key Moments therefore means three things, in order: record the inheritance
decision, rule on the nine conflicts it exposes, then build to the bar in §3.4 in the staging of §3.6.

### 3.2 The inheritance decision (recommended; owner decision D3 covers the one open sub-point)

| Layer | Inherit from | Why |
|---|---|---|
| **Tokens + restraint doctrine** | `SoT/html/assets/sot.css` governed by `SoT/html/README.md` — warm paper `#f4efe3` / surface `#faf6ec` / ink `#14120e` / ink-soft `#6f6a5e` / hairline `#d8d0bd` / ochre `#a8842c` as the single spot colour, `--u: 8px`, `--radius: 0`, `--shadow: none`, serif headline + letterspaced grotesque label + mono ID, the kicker line, the `a.id` ochre-underline chip, the **ochre budget** | The only artifact with the standing of a design system: shipped in three trees, embedded in the README, named "the authoritative design contract for the HTML layer" by `DELIVERABLES_CONCEPT.md`, and named the *ancestor of the views surface* by the ontology (§2.4). Moments are deliverables that sit beside views; they must not read as a foreign product. `v2-todo.md` #13 already commits to preserving this doctrine through the re-key |
| **Mechanics only** | `docs/v2/audit/v2-walkthrough.html` — the three-tier theme switch (`:root` → `@media (prefers-color-scheme: dark) :root:not([data-theme="light"])` → `:root[data-theme="dark"]`) and hand-authored inline SVG whose strokes/fills are `var(--token)` | The only artifact that solves the two things `sot.css` does not (theming, themed diagrams). Take the *structure*, **not the hexes** — its teal/plane palette is a private note, not house style |
| **Components, states, copy rules** | `docs/v2/V2_KEY_MOMENTS_VISUAL_RESEARCH.md` §"One-Family System" — provenance chip, staleness stamp, M1→M8 rail, sign-off ceremony, comparison component, print, dual-channel encodings | It supplies no tokens (its entire token contribution is "8px grid, ~6-step scale, system font stack, one accent per verb"); it is a component spec, to be built *in* the SoT idiom |
| **Not inherited** | The portfolio "Editorial Luxury" language (cream `#F9F8F6` / ink `#1A1A1A` / antique gold `#C5A065`, Playfair/Inter/JetBrains Mono) | That is the **site's** system (brief v2.0 §9). The two are cousins, not the same; repo specimens embedded on the site keep their own tokens, like screenshots |

Record the decision as one paragraph in `V2_KEY_MOMENTS.md` §2.1 (or as the family-shell file's header
comment) — effort S; it is the first step of Phase 2 (§7).

### 3.3 The nine conflicts, with recommended rulings

| # | Conflict | House rule says | Research / briefing asks | Recommended ruling | Decider |
|---|---|---|---|---|---|
| C1 | Font stack | `"Plantin","Freight Text Pro",Georgia…` name-first; macOS-flavoured | one system stack, no web fonts (`file://`) | Keep the *structure* (serif headline · grotesque label · mono ID); re-spec as name-first **with system fallbacks that degrade identically on Windows/Linux**; verify with zero network | design session |
| C2 | One accent per loop verb vs. one ochre spot | "at most one ochre device competes on a page"; rainbow categorical palettes and a second accent banned | six verb accents so a page signals where in the loop it sits | **Sharpest conflict in the corpus.** Ochre stays the only spot (chip underline, kicker №, sign-off commit). The verb signal becomes a **low-chroma hairline/label band in the chrome**, a muted six-value ramp derived from the existing `--green/--amber/--teal/--purple/--navy/--gray` — never as fills; muted further on M5 (the research's own carve-out) | owner confirms |
| C3 | Dark mode | none in `sot.css` (zero `prefers-color-scheme`) | required; walkthrough implements it | Shell carries the three-tier *mechanics* from day one (cheap). Whether a **warm-dark ramp** ships in the first build or waits is owner decision D3; recommendation: light + print first, dark ramp second — and when it comes, derive it from paper/ink, not a generic `#16191b` | owner (D3) |
| C4 | Severity colour | red/amber/green status **dots** banned (fail greyscale, fight the spot) | dual-channel severity and grade, colour included | Both agree colour is never the only channel. Primary = rank position + label + magnitude; the RAG tier renders as **bar fills and labels** using the existing muted `--green #3d6b35` / `--amber #9c7a2d` / `--red #9e3b2c` — satisfies the doctrine's actual objection (dots), not its letter | design session |
| C5 | JavaScript | "if a device needs JavaScript … it has left the system" | chip expand, drag-rank, sortable register, movable beta line, input mode | Apply the amendment already drafted in `DELIVERABLES_CONCEPT.md` §5 (L114–116) / §9: **one sanctioned `deliverable.js`, enhancement-only; every template renders complete without it** (the no-JS floor in §3.4). Update `SoT/html/README.md` when the amendment lands | design session, then html README |
| C6 | Radius / elevation | `--radius: 0`, `--shadow: none`, gradients banned | "recommended" column gets a badge **and elevation**; walkthrough uses 8px radii | Follow the house: "recommended" = heavy ink rule + ochre tag (the doctrine's own `figure.exhibit` device); drop the walkthrough's radii | design session |
| C7 | Print | a four-declaration print block | full print stylesheet: detail-on-demand expands, chips become footnotes, DAG/journey render full width | Net-new work; build it in the shell stage — it is also the cheapest proof that the provenance chip carries real data | design session |
| C8 | Risk scoring model (M5) | `DELIVERABLES_CONCEPT.md` §6.1 computes Raw = Impact × Likelihood (multiplied ordinals) | Cox 2008 / Hubbard reject multiplied ordinals; status-weighted sort is fine, a 5×5 grid is not | The template renders what the pull computes; the *model* (keep Raw for README scorecard continuity vs. quantified exposure ranges) is decided in v2-todo **15c** — flag it in the M5 template, do not pick silently | 15c session |
| C9 | Which ancestor wins | unstated | unstated | §3.2 above; record it | owner (this plan) |

### 3.4 The bar — what a "polished" moment template is

A template is done when every line below is true (the checklist the design session and its reviewer share):

- [ ] **Single file, `file://`, no build step, no CDN, no web fonts, no external libraries.** Opens from a cold clone.
- [ ] **Renders complete without JavaScript**; `deliverable.js` adds interaction only (C5).
- [ ] **Family shell present**: tokens per §3.2; provenance chip (ID-only by default; tier dot + confidence + source on demand); staleness stamp top-right backed by the embedded data fingerprint; the ordered M1→M8 rail with per-moment freshness dot; the sign-off ceremony (literal-verb button, signer + timestamp, weight proportional to consequence — static in the alpha); the comparison component where the moment uses it (M3, M5, M7).
- [ ] **Every data state designed, not just the happy one**: n=0 · n=1 · n-many · overflow, plus the moment's named flags from the canon (e.g. M1 "needs Explore", M2 "n of 5" cap, M4 >15-screen cap breach / dead-end / absent money shot, M5 high-risk-without-response, M6 dependency cycle, M7 reconciliation contradiction / "launching blind", M8 "not yet measured" never rendered as zero).
- [ ] **Hydrates from `<moment>.json`** with the moment's Renders list, record IDs and provenance tags on every fact; no hand-edited content in the template (the Graphify rule — rebuild, don't fix).
- [ ] **Light theme complete; theme mechanics present**; dark ramp per owner decision D3.
- [ ] **Print/PDF**: detail-on-demand expanded, chips as footnotes, full-width maps.
- [ ] **Keyboard-operable, WCAG AA contrast, dual-channel encodings** (position/label + colour; never colour alone).
- [ ] **Responsive at 390 / 768 / 1024 / 1440** without hiding evidence or status labels.
- [ ] **Genre departures honoured**: no 5×5 heat map anywhere (M5); no date-based Gantt (M6); annotated sentence as M1's hero (table fallback only after the prototype test).
- [ ] **Register matches the canon**: M1 quietly authoritative · M2 warm but disciplined · M3 confident, price demoted · M4 allowed warmth and drama · M5 the most sober page in the system · M6 engineering-calm · M7 energized but accountable · M8 the heaviest ceremony.
- [ ] **Fixture-driven**: one illustrative product ("Signal", the walkthrough's product) exercises every state; fixture labelled illustrative, never mixed with real evidence.
- [ ] **Screenshot captured** (`docs/assets/moments/`) and the §2.3 benchmark for its stage met (e.g. a non-author PM reaches every M1 clause's evidence in one click; the DAG renders with zero hairballs at n=20 and redraws identically from the same JSON; no 5×5 grid anywhere; legible at n=50).

### 3.5 Where the prototypes live

Build them **outside canonical paths** (build plan §11: "keep experiments disposable … until their contract
is approved"): `docs/v2/moments/` — `shell/` (tokens layer over `sot.css`, `deliverable.js`, print sheet),
`M1-problem-framing.html` … `M8-launch-verdict.html`, `fixtures/signal/M1..M8.json`, screenshots in
`docs/assets/moments/`. Promotion to `SoT_template/html/moments/` (and through the packager) happens at the
v0.6 surface-layer spec (v2-todo **15b**). Legality: the pull/render halves are read-only by construction
(ARC-003) and therefore alpha-legal; the emit halves ride Wave 5's Change-plane contract — any go-live that
promises sign-off *capture* is promising a Wave 5 deliverable (label accordingly).

### 3.6 Staging and session plan

| Session | Builds | Benchmark to proceed | Size |
|---|---|---|---|
| S1 | Record §3.2 in the canon; **family shell** (tokens, chip, stamp, rail, sign-off grammar, comparison component, print sheet, theme mechanics); a **style tile spanning the emotional extremes** (M4 warmth ↔ M5 sobriety ↔ M8 gravity); fixture JSON schema | chip renders ID-only and expands on demand; stamp flips on fingerprint mismatch; tile approved by owner | M |
| S2 | **M1, M3, M8** — the sentence moments + the scorecard (no layout engine) | non-author PM reaches every M1 clause's evidence in one click; M3 reads engagement-first with price visibly demoted; M8 verdict is the hero, bullet graphs not gauges | L |
| S3 | **M4, M6** — the map moments (layout coordinates hand-computed into the fixture JSON for now; the pull script computes them later) | zero hairballs at n=20, deterministic redraw; money shot and delight/utilitarian as labelled decisions | L |
| S4 | **M5, M2, M7** — the register/decision moments; M5 is the flagship departure | no 5×5 grid; every high risk has a response or sign-off is blocked; legible at n=50; all-green reconciliation table reads as the "coherent" moment | L |
| S5 | Polish pass, screenshots, embedding (README T2 section, site canon pages), prototype tests the research asks for (M1 sentence vs. table with 3–5 experienced PMs; M4 two-mode seam) | every §3.4 box ticked per template | M |

Decisions the design session must **surface, not resolve** (canon §4): M1 hero vs. table; M4 one template
two modes vs. two pages; sign-off staleness tuning; the style tile's range; human-declaration flags (money
shot, negative persona) made visible by absence.

---

## 4. Lens B — Repository organization: a tight template

### 4.1 The layers, and where they bleed

636 tracked files, ~6.5 MB. Five layers coexist and the *contract* between them is sound
(`.claude/install-manifest.yaml` classes — `framework` / `template_seed` / `never_touch` /
`direct_exclude` / `plugin_review_alias` / obsolete fingerprints — enforced by the 90 tests in
`tests/test_distribution.py`). The failure is **legibility**: nothing in the directory layout tells a
first-time forker which layer a file belongs to.

| Layer | Where | Files | What bleeds |
|---|---|---|---|
| This repo's own product truth | `PRD.md`, `SoT/`, `README.md` (v2 branch) | — | Two PRDs and two READMEs at root with the explanatory Fork Note ~270 lines down; `SoT/` vs `SoT_template/` are visually identical 14-file trees (27 files differ, only two carry real truth: BUSINESS_RULES, TECHNICAL_DECISIONS) |
| Generic downstream seeds | `*_template.md`, `SoT_template/`, nine `*.seed.*` pairs | 30 + 9 | The seed pairs are byte-identical to their destinations (expected at rest; the tests require it) but sit side by side in `docs/` and `epics/` with no local explanation |
| Methodology runtime | `.claude/` (211), `scripts/` (19) | 230 | Dead one-shot script `.claude/rename_templates.py`; a 14 KB interview script `docs/maintainer/archive/workflow-review-interview.md`; the owner-path `.claude/projects/…` dir; `.claude/README.md` tree lists 5 `ghm-*` skills (there are 7) |
| Generated plugin payload | `plugins/prd-ce/` (238, 2.2 MB) + `.claude-plugin/marketplace.json` | 239 | None — CI-enforced (`check-plugin-sync.sh` on every PR/push). **Do not hand-edit; regenerate** |
| Scratch | `temp/` (47, 2.0 MB) | 47 | Ten subdirectories in a folder the method calls "transient": 1.3 MB of README PNGs, 330 KB of v2 audits (incl. 66 KB analysing a third-party repo), client-flavoured skill fork, a "superseded scratchpad", an off-topic portfolio proposal, an empty `skill-progress/`; `temp/README.md` (dated a year wrong) forbids the very README references that exist |
| `docs/` | 19 files, 564 KB | 19 | **74 % maintainer-internal** (14 of 19): a 121 KB research blueprint, a 53 KB research report, evaluation prompt, site brief, build plan, ontology, audits, two dead migration briefs, a historical memo — with no index. The two docs a forker needs (`DEVELOPMENT_GRAPH.md`, `READINESS_PROTOCOL.md`) sit alphabetically between them |
| Root | 13 files | 13 | `PRD-Methodology-Overview.pptx` (50 KB binary, Feb 2026, referenced nowhere); `CLAUDE_plugin_stub.md` (a packager input that reads like a leftover) |

### 4.2 P0 hygiene — do first, no gate, owner confirmation

| # | Item | Action | Note |
|---|---|---|---|
| H1 | `temp/v0.5-requirements/prd-v05-technical-stack-selection/` (8 files incl. `LEARNINGS-LIGHTSTACK.md`) | Review; remove from the public repo (move to private if still needed). Leave the empty stage dir + `.gitkeep` | On `main` since 2026-02-26. A forked copy of a shipped skill with a vendor catalog; the learnings file is addressed to a named person about a named client ecosystem. Nothing references it. Also review `.claude/skills/prd-v05-technical-stack-selection/references/brownfield.md` for the same vendor framing |
| H2 | `.claude/projects/-Users-<owner>-…/memory/*.md` (3 files) | Delete the committed content (keep the manifest's `never_touch` entry for the runtime dir) | Evades the leak test only because the path uses dashes, not slashes |
| H3 | `/Users/…` paths in `temp/v2-audit/impeccable/{router,shape,build}.md` | Replace with relative/opaque references | Extend the leak scan (or a light CI grep) to `temp/` so it cannot recur |

Removal is forward-only: the owner accepted the ancestor-history exposure on 2026-08-12 (PRD open decision
5); do not promise or attempt history rewriting.

### 4.3 Target tree (proposed)

```text
/
├── README.md · PRD.md · CLAUDE.md · LICENSE · CHANGELOG.md · MIGRATION.md · BLUEPRINT.md · install.sh
├── README_template.md · PRD_template.md · SoT_template/        # seeds (v2 branch); banner at top of each
├── SoT/                                                         # this repo's accepted memory; banner at top
├── epics/                                                       # template + README (+ .seed twins, signposted)
├── docs/
│   ├── index.md                                                 # NEW — the docs front door
│   ├── DEVELOPMENT_GRAPH.md (+ .seed) · READINESS_PROTOCOL.md (+ .seed)
│   ├── INSTALL.md · ARCHITECTURE.md                             # NEW — lifted out of README
│   ├── MODERNIZATION_ASSESSMENT_PROMPT.md                       # linked from index (today unlinked)
│   ├── assets/                                                  # README PNGs (from temp/sot-html-mockups) + moments/
│   ├── v2/                                                      # v2 planning + research, with its own README
│   │   ├── PRD_CE_V2_BUILD_PLAN.md · ECOSYSTEM_ONTOLOGY.md · V2_KEY_MOMENTS.md · V2_KEY_MOMENTS_VISUAL_RESEARCH.md
│   │   ├── V2_SKILL_CONSOLIDATION_AUDIT.md · DELIVERABLES_CONCEPT.md · GEARHEARTAI_PRD_CE_V2_SITE_BRIEF.md
│   │   ├── V2_GO_LIVE_POLISH_PLAN.md (this file) · MASTER_…_BLUEPRINT.md · PRD_CE_V2_LIVE_PROJECT_EVALUATION_PROMPT.md
│   │   ├── audit/                                               # harvested from temp/v2-audit (ledgers, digests, northstar, walkthrough)
│   │   └── moments/                                             # §3.5 prototypes + fixtures
│   └── maintainer/archive/                                      # MIGRATION_BRIEF_v3*.md · HARNESS_FORGE_LESSONS.md ·
│                                                                #   IMPROVEMENT_SUMMARY.md · PHASE_2_EXECUTION_PLAN.md · workflow-review-interview.md
├── temp/                                                        # README + the seven stage dirs (.gitkeep) — nothing else
├── scripts/ · tests/ · .github/ · .claude/ · .claude-plugin/ · plugins/   # unchanged
└── (deleted) PRD-Methodology-Overview.pptx · .claude/rename_templates.py · temp/skill-progress/ · temp/*-proposal.md · docs/maintainer/archive/plugin-conversion-plan.md
```

`CLAUDE_plugin_stub.md` may move beside the other packager inputs (optional — needs edits in
`scripts/package-plugin.sh`, `scripts/prd-ce-init.sh`, and the tests).

### 4.4 Cleanup table (ranked by how much each confuses a template user)

| # | Target | Disposition | What breaks / follow-through |
|---|---|---|---|
| 1 | README "Repository structure" tree ≠ real tree (omits `docs/ scripts/ tests/ plugins/ .claude-plugin/ .github/ .claude/rules/ install.sh BLUEPRINT.md CHANGELOG.md MIGRATION.md LICENSE README_template.md CLAUDE_plugin_stub.md`); skill counts wrong in four places + an anchor slug (source: 41 stage + **7** `ghm-*` + `init` + `SKILL_TEMPLATE`; plugin ships 41 + 5 + `init` = 47; README says 41 + 6) | Regenerate the tree from `git ls-files`; state the count once and generate it, or drop it from the H2/anchor | Edit inside the `<!-- SECTION: repo-structure -->` markers (`ghm-status-sync` uses them); update the two internal anchors |
| 2 | Six README PNGs in `docs/assets/sot-html/` (1.32 MB ≈ 20 % of tracked bytes) | Move to `docs/assets/`; update 7 README embeds | Also `SoT/html/README.md` (2 refs) and `SoT/html/screenshot.py:40`; the seeded `SoT_template/html/{README.md,screenshot.py}` may keep writing to consumers' `temp/` (their screenshots are scratch) — decide, then `package-plugin.sh`. `docs/assets` stays outside the install allowlist, so nothing ships |
| 3 | `temp/` with ten dirs | Keep the seven stage dirs; move `v2-audit/` → `docs/v2/audit/`; delete `skill-progress/`; archive/delete the two proposals | `V2_KEY_MOMENTS.md` and `V2_SKILL_CONSOLIDATION_AUDIT.md` cite `temp/v2-audit/inventory/` as provenance; `v2-todo.md` links ~12 files — the link-check CI catches every miss |
| 4 | H1–H3 above | Remove / scrub | — |
| 5 | `docs/` split per §4.3 | Move 10 v2 docs to `docs/v2/`, 5 historical to `docs/maintainer/archive/`; add `docs/index.md` + `docs/v2/README.md` | Breaks: `PRD.md` authority item 6 link, README → `DELIVERABLES_CONCEPT.md`, the site brief's `research_blueprint_path`, ~12 cross-links among the moved docs; `tests/test_distribution.py` is name-based (`EXCLUDED_DOCS`, `ALLOWED_DOCS`) so moves are safe — add the new v2 doc names to `EXCLUDED_DOCS` (or switch to directory-based exclusion) |
| 6 | Two PRDs · two READMEs · `SoT/` vs `SoT_template/` | Keep (the manifest requires both); add a three-line "this file is X; forkers use Y" banner at the top of `PRD.md`, `README.md`, `SoT/SoT.README.md`; fix Quick Start to `rm -rf SoT && cp -R SoT_template SoT` (today's `cp -R SoT_template/. SoT/` merge-copies and never deletes) | Additive |
| 7 | `PRD-Methodology-Overview.pptx` | Delete (or attach to a Release) | v2-todo #2 |
| 8 | `docs/maintainer/archive/MIGRATION_BRIEF_v3.md`, `MIGRATION_BRIEF_v3.2.md`, `HARNESS_FORGE_LESSONS.md`, `docs/maintainer/{IMPROVEMENT_SUMMARY,PHASE_2_EXECUTION_PLAN}.md`, `docs/maintainer/archive/workflow-review-interview.md` | `docs/maintainer/archive/` | Zero inbound links; tests reference two by bare name (move-safe) |
| 9 | `CHANGELOG.md` stops at 3.2.0; `MIGRATION.md` lacks 3.2.0 → 3.3.0 | Backfill on the v2 branch | v2-todo #1; `ghm-template-sync` reads both — never delete them; link them from README (0 hits today) |
| 10 | `.claude/rename_templates.py` (Jan 2026, one-shot, zero refs) | Delete | — |
| 11 | `.claude/README.md` tree drift (5 `ghm-*` listed) | Regenerate | — |
| 12 | Nine identical `*.seed.*` pairs | Keep; add a one-line header to each seed ("framework-owned upstream original for `<dest>`; edit `<dest>`, not this") and a note in `docs/index.md` / `epics/README.md` | The md5s will then differ — fine; verify `test_direct_and_plugin_consumer_scaffolds_are_equivalent` still passes before committing |
| 13 | `temp/README.md` | Rewrite: 7 stage dirs, correct date, and drop or re-scope the "never reference temp from README" rule once the PNGs move | — |
| 14 | Plugin manifests carry no `version` (`.claude-plugin/marketplace.json`, `plugins/prd-ce/.claude-plugin/plugin.json`) | Add `version` = `.claude/VERSION` | Route through the packager (v2-todo #18) |
| 15 | `primaryLanguage: HTML` on GitHub (from `SoT/html/`) | `.gitattributes`: `SoT/html/** linguist-documentation` (and the template/plugin copies) | Cosmetic; S |

**Do not touch**: `plugins/prd-ce/` (regenerate only), the three `scripts/compute-*-readiness.py` shims
(18-line dispatchers that `readiness.py` and `_readiness/stage.py` call).

### 4.5 Follow-through for any move or delete

`bash scripts/package-plugin.sh` → `bash scripts/check-plugin-sync.sh` → `python3 -m pytest tests/ -q`
→ local link check (CI's `markdown-link-check` runs only on PR/push, modified files only, no
`ignorePatterns` — add some to `.github/mlc_config.json` for the flaky external hosts while you are there).

### 4.6 Crosswalk to `docs/v2/audit/v2-todo.md`

| This plan | v2-todo item |
|---|---|
| CHANGELOG + MIGRATION 3.3.0 backfill | #1 |
| pptx | #2 |
| seed single-sourcing decision | #3 (this plan recommends *signpost, don't merge* — the pairs are contractual) |
| README full refresh (v2 narrative) | #6 — **after R0**; the README 1.5 polish in §5.1 is vocabulary-neutral and precedes it |
| CLAUDE.md / stub / README_template re-keys | #7, #8, #9 |
| SoT html review layer doctrine preserved | #13 |
| surface-layer spec (promotion home for the moments) | #15b |
| key-moments question research + template design | #15c (§3 here is the bar that session builds to) |
| packager + payload | #18 |
| MIGRATION v3.3 → v4.0 + CHANGELOG 4.0.0 | #21 |

---

## 5. Lens C — Repo polish for promotion (the work behind §2)

### 5.1 README — two passes, not one

**README 1.5 (T1, on `main`, now; vocabulary-neutral; target ≤ 250 lines).** Structure:

1. H1 + the tagline **"Memory as Infrastructure"** (kept — it has performed well) + a **subtitle** that does the verb + outcome + audience work in ≤ 16 words (owner picks from §10.1) + badges (stars · license · **CI** · **release** · built-for-Claude-Code; fix the PRs-welcome target to `CONTRIBUTING.md`).
2. **One-command start** + **Use this template** link, above the image. Candidates for the one line: the `BLUEPRINT.md` one-paste bootstrap, or `gh repo create my-product --template mattgierhart/PRD-driven-context-engineering`, then the two-line `pip install` + `readiness.py run`. State prerequisites once.
3. Hero image (`docs/assets/atlas.png`) **or the motion proof** (§5.4) directly under the tagline.
4. "What you get in 5 minutes" — three lines.
5. The seven features, one line each + links (keep the table; trim the sections below it to a paragraph each).
6. How it works (the lifecycle table stays — it is the method today).
7. Links: docs index · INSTALL · ARCHITECTURE · CONTRIBUTING · CHANGELOG/Releases · gearheartai.org.
8. Star ask **at the end**, after the value moment.

Move out: Contributing (L388–432 on v2) → `CONTRIBUTING.md`; Squad Status (L365–384) → delete from the
public README (it already ships in `README_template.md`; verify `ghm-status-sync` tolerates a missing
marker); Repository structure → `docs/ARCHITECTURE.md`; How-to-use + source-run install → `docs/INSTALL.md`;
the Problem / Idea / Cognitive-Shift manifesto → six lines + a link to the site essay. Drop the V2 blockquote
from any version that lands on `main`.

**README 2.0 (T2, after R0)** = v2-todo #6: the loop as the public vocabulary, the lifecycle table as a
guided journey, the skills feature re-framed as a registry, the agent squad rewritten around workers, a
"where v2 is going" section that links the canon and the moment previews.

### 5.2 GitHub settings (S, owner performs)

| Setting | Today | Set to |
|---|---|---|
| Social preview | GitHub default | 1280×640 from `atlas.png` on the cream/ink/gold ground; the card *is* the product |
| Description | "PRD-driven Context Engineering: A systematic approach…" | the tagline (names Claude Code) |
| Topics | `ai-assisted claude developer-tools nextjs product-development productivity rapid-development supabase templates workflow` | `claude-code context-engineering spec-driven-development ai-agents agentic-coding prd agent-skills claude-code-skills product-management templates` (drop `nextjs`, `supabase`) |
| Homepage | empty | `https://www.gearheartai.org` |
| Discussions / Wiki | off / on | **on / off** |
| Template | on, unadvertised | on, advertised in the hero |

### 5.3 Community health 42 % → 100 % (S)

`CONTRIBUTING.md` (lift README §Contributing — it is good copy) · `CODE_OF_CONDUCT.md` (Contributor Covenant)
· `SECURITY.md` (report path; supported versions = latest tag) · `.github/ISSUE_TEMPLATE/` (bug report; a
"context leak" report in the method's own vocabulary) · `.github/PULL_REQUEST_TEMPLATE.md` (IDs touched,
SoT updated?, plugin payload regenerated?). Optional: `SUPPORT.md`, `FUNDING.yml`, `CITATION.cff`.

### 5.4 Proof in motion (M; owner decision D6)

Either a 20–30 s terminal GIF (`readiness.py run` blocking a gate → a fix → passing; asciinema → agg, or
VHS) or the loop SVG diagram (BMAD's pattern; the walkthrough's plane/verb SVG is a ready candidate once
re-tokenised). One of the two sits under the tagline; the six stills move below the fold. **Owner: yes to
the GIF (2026-08-19)** — storyboard, fixture, and a ready-to-run VHS tape are in §10.3.

### 5.5 Release hygiene (S)

Backfill annotated tags `v1.0.0`, `v2.0.0`, `v3.0.0`, `v3.1.0`, `v3.2.0` at their CHANGELOG commits; publish
a GitHub Release for the T1 polish (`v3.2.1`, notes from the CHANGELOG entry you add); `3.3.0` is entered and
released when/if Wave 0B lands on `main` (decision D2). Each release is a LinkedIn post (build-in-public type).

### 5.6 Maintainer signals (S)

Reply to / disposition external PR #68 (open since 2026-04-28); close or link issues #53 (README vs
dashboard), #56 (QUICKSTART), #57 (example project) as this plan executes them; prune the ~18 stale
`claude/*` and `feat/*` remote branches; pin a Discussion ("Start here / roadmap").

### 5.7 Discoverability (S)

Submit to `hesreallyhim/awesome-claude-code` (Agent Skills / Workflows); cross-link site ↔ repo both ways;
verify the plugin marketplace install end-to-end before any "install" CTA (README already says unverified).

---

## 6. Cross-surface consistency

**Naming matrix (applies to repo, site, GitHub metadata, LinkedIn):**

| Use | Form |
|---|---|
| The method / product name | **PRD-Led Context Engineering** (PRD-CE) |
| The thesis line | **Memory as Infrastructure** ("as", never "is" — the live site's H1 and the GitHub description both drift) |
| The repo slug / URL | `PRD-driven-context-engineering` — immutable; the only sanctioned "driven" |
| "The Product Model" | working name only, appendix-level, pending PRD open decision 1 |
| Public stage vocabulary (T2, after R0) | the PM loop Explore → Shape → Decide → Build → Learn, Check cross-cutting; planes stay internal |

**Stale statements to fix in follow-ups (not edited by this plan):**

- `docs/v2/PRD_CE_V2_BUILD_PLAN.md` §11 (L519–523), §13 "Public-history leakage", §14 decision 5, §15 actions 1–2 still say *do not push / sanitize history* — resolved by PRD open decision 5 on 2026-08-12 (publish as-is; `prd-ce-v2` is on origin). Also `branch:` in its frontmatter.
- `README.md` (v2 branch) V2 blockquote names the superseded `codex/prd-ce-v2-product-model` branch — and must not reach `main`.
- gearheartai.org: `og-image.png` returns 404; the deprecated cyan/dark palette is live; the only GitHub link is the owner's profile, not the repo; `/blog`, `/essays`, `/docs` redirect to `/`; no `sitemap.xml` / `robots.txt` — all owned by brief v2.0 Phase 1.
- The site brief's own frontmatter (fixed in v2.0).

---

## 7. Tracker (was: sequenced roadmap)

Sizes: S < 1 h · M ≈ half day · L = multi-day · XL = multi-session. Owner: **Claude** executes ·
**Matt** creates · **Matt-approve** decides (then usually Claude executes). Status: `☐` open ·
`◐` in progress · `☑` done · `⊘` dropped. Flip the status and date an item when it closes.

### Phase 0 — P0 hygiene

| ID | Item | Tier | Owner | Size | Depends on | Status | Notes |
|---|---|---|---|---|---|---|---|
| H1 | Remove client-flavoured material `temp/v0.5-requirements/prd-v05-technical-stack-selection/` (8 files) | T1 | Matt-approve → Claude | S | D5 | ☑ 2026-08-19 | copied to the owner's private archive first, then removed (commit 7faccb4) |
| H2 | Delete the committed `.claude/projects/-Users-<owner>-…/memory/` content | T1 | Claude | S | — | ☑ 2026-08-19 | manifest `never_touch` entry kept |
| H3 | Scrub absolute paths in the v2 audit notes (now `docs/v2/audit/`) | T1 | Claude | S | — | ☑ 2026-08-19 | repo-wide grep clean; a CI-side leak grep is tracked as 1.1n |

### Phase 1 — T1 template-repo go-live on `main`

| ID | Item | Tier | Owner | Size | Depends on | Status | Notes |
|---|---|---|---|---|---|---|---|
| 1.0 | Branch strategy decided | T1 | Matt-approve | S | D1 | ☑ 2026-08-19 | **D1 = everything lands on `prd-ce-v2`**; `main` waits for the v2 merge |
| 1.1c | Six README PNGs → `docs/assets/sot-html/`; update README refs, `SoT/html/README.md`, `screenshot.py` (both trees) | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | plugin payload regenerated |
| 1.1d | Delete `PRD-Methodology-Overview.pptx` | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | v2-todo #2 |
| 1.1e | Historical docs → `docs/maintainer/archive/` (migration briefs v3/v3.2, HARNESS_FORGE, IMPROVEMENT_SUMMARY, PHASE_2, workflow-review-interview, plugin-conversion-plan) + archive README | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | |
| 1.1f | Delete `.claude/rename_templates.py`; delete `temp/skill-progress/`; portfolio proposal → private archive; plugin-conversion-plan → `docs/maintainer/archive/` | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | |
| 1.1g | `temp/` split — seven stage dirs + README only; `temp/v2-audit/` → `docs/v2/audit/` | T1/T2 | Claude | M | 1.0 | ☑ 2026-08-19 | repo-wide link check: 0 broken |
| 1.1h | `temp/README.md` — date fixed, pointer to `docs/v2/`; the "never reference temp from README" rule now holds | T1 | Claude | S | 1.1c | ☑ 2026-08-19 | |
| 1.1i | `.claude/README.md` — the tree deliberately shows the installed runtime (41 + 5); the note now states the authoring-source extras explicitly | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | |
| 1.1j | Signpost the nine `*.seed.*` pairs | T1 (v2 branch) | Claude | S | 1.2 | ⊘ 2026-08-19 | seed bytes are copied verbatim into consumer files, so an in-file header would mislead there; the signpost lives in `docs/index.md` instead |
| 1.1k | `.gitattributes` — HTML review layer = documentation; `plugins/prd-ce/**` = generated | T1 | Claude | S | 1.0 | ☑ 2026-08-19 | |
| 1.1l | `version: 3.3.0` in both plugin manifests; plugin displayName → PRD-Led; keywords + `claude-code` | T1 (v2 branch) | Claude | S | — | ☑ 2026-08-19 | manifests are authored, not generated |
| 1.1m | CHANGELOG 3.3.0 entry + MIGRATION 3.2.0 → 3.3.0 section | T1 (v2 branch) | Claude | S | — | ☑ 2026-08-19 | v2-todo #1 — the entry covers the whole April→August span |
| 1.1n | Repo-wide leak grep in CI (absolute home paths anywhere tracked, not only distributable surfaces) | T1 | Claude | S | — | ☐ | small workflow step or a test |
| 1.2 | `docs/index.md`; `docs/v2/` split with README; `docs/maintainer/archive/`; `docs/INSTALL.md`; `docs/ARCHITECTURE.md`; every inbound link fixed | T1 | Claude | M | 1.1e | ☑ 2026-08-19 | 110 tests pass; `EXCLUDED_DOCS` extension still a nice-to-have |
| 1.3 | README 1.5 (tagline kept + working subtitle; Quick Start first with one-command create + Use-this-template; CI badges; sections moved to docs/; counts fixed; Squad Status removed; 432 → 271 lines) | T1 | Claude · Matt confirms subtitle wording | M | 1.2, D7 | ◐ 2026-08-19 | `ghm-status-sync` amended to skip a missing squad-status marker; final subtitle wording = D7 |
| 1.4 | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, two issue forms + config, PR template | T1 | Claude | S | — | ☑ 2026-08-19 | GitHub reads community files from the default branch — the profile % moves when these reach `main` |
| 1.5 | Readiness GIF (storyboard + VHS tape §10.3) | T1 | **Matt** (or Claude if `vhs` is installed) | M | §10.3 | ☐ | D6 = yes |
| 1.6a | `gh repo edit`: description, topics, homepage | T1 | Matt-approve → Claude | S | D8 | ☑ 2026-08-19 | applied; 16 topics; homepage gearheartai.org |
| 1.6b | Discussions on · Wiki off | T1 | Matt-approve → Claude | S | D9 | ☑ 2026-08-19 | |
| 1.6c | Upload the social preview (Settings → Social preview; UI only) | T1 | **Matt** | S | D14 | ☐ | draft card §10.4 |
| 1.7a | Backfill tags `v1.0.0`–`v3.2.0` at the CHANGELOG commits | T1 | Matt-approve → Claude | S | D10 | ☐ | push = public |
| 1.7b | `v3.2.1` polish release (`gh release create`) | T1 | Matt-approve → Claude | S | D10, 1.1–1.6 merged | ☐ | |
| 1.7c | LinkedIn launch post drafted against the release | T1 | Claude drafts · Matt posts | S | 1.7b | ☐ | |
| 1.8a | PR #68 disposition (reply drafted) | T1 | Matt-approve | S | D11 | ☐ | |
| 1.8b | Close/link issues #53, #56, #57 as items land | T1 | Claude | S | 1.2–1.3 | ☐ | |
| 1.8c | Prune stale remote branches | T1 | Matt-approve → Claude | S | D12 | ☐ | list in D12 |
| 1.8d | Pin a "Start here / roadmap" Discussion | T1 | Claude | S | 1.6b | ☐ | |
| 1.8e | Submit to `awesome-claude-code` | T1 | Matt-approve → Claude | S | D13, 1.7b | ☐ | external PR |
| 1.9 | Reconcile `main → prd-ce-v2`; decide Wave 0B → `main` | T1→T2 | Matt-approve | M | D2 | ☐ | build plan §11 |

### Phase 2 — T2 v2 concept public

| ID | Item | Tier | Owner | Size | Depends on | Status | Notes |
|---|---|---|---|---|---|---|---|
| 2.0 | Record the inheritance decision (§3.2) in `V2_KEY_MOMENTS.md` §2.1; rulings C1–C9 | T2 | Claude (Matt confirms C2, C3) | S | D3 | ☐ | |
| 2.1 | Design S1: family shell + style tile + fixture schema | T2 | Claude · Matt approves the tile | M | 2.0 | ☐ | |
| 2.2 | Design S2–S4: M1/M3/M8 → M4/M6 → M5/M2/M7 | T2 | Claude | L ×3 | 2.1 | ☐ | |
| 2.3 | Design S5: polish, screenshots, prototype tests | T2 | Claude · Matt runs the PM tests | M | 2.2 | ☐ | |
| 2.4 | Walkthrough re-tokenised to the house system; promoted to a public "v2 in 30 seconds" page | T2 | Claude | M | 2.1 | ☐ | |
| 2.5 | Site Phase 1 per brief v2.0 | T2 | Claude (site repo) · Matt approves | L | brief §17; D4 | ☐ | PRD open decision 4 |
| 2.6 | R0, then README 2.0 + the v2-todo "With R0" items | T2 | Matt-approve → Claude | L | R0 | ☐ | v2-todo #5–#9 |

### Creative items (Matt owns; starting points in §10)

| ID | Item | Owner | Status | Notes |
|---|---|---|---|---|
| C1 | Pick the subtitle under "Memory as Infrastructure" | Matt | ☐ | candidates §10.1 |
| C2 | Hero visual — run the prompt experiments, pick a direction | Matt (Claude generates on request) | ☐ | prompts §10.2 |
| C3 | Readiness GIF recorded | Matt (or Claude with `vhs`) | ☐ | storyboard §10.3 |
| C4 | Social preview card approved and uploaded | Matt | ☐ | draft §10.4 |

### Done

| ID | Item | Date |
|---|---|---|
| 0.0 | This plan (v1.0) and the site brief v2.0 written and committed | 2026-08-19 |
| 0.1 | Plan v1.1: tracker, decision packet, creative starting points; tagline decision recorded | 2026-08-19 |
| 0.2 | Phase 0 hygiene (H1–H3) · cleanup batch 1.1c–1.1m · docs split + front door (1.2) · README 1.5 draft (1.3) · community files (1.4) · GitHub metadata (1.6a/b) — all on `prd-ce-v2` | 2026-08-19 |

---

## 8. Acceptance checklists

**T1 — template-repo go-live is done when**

- [ ] H1–H3 removed/scrubbed; a `temp/`-inclusive leak grep passes.
- [ ] ≥ 25 of the 30 items in §2.2 PASS; community profile reads 100 %.
- [ ] README ≤ 250 lines, tagline + one-command start + "Use this template" above the fold, no empty tables, counts generated or absent, tree matches `git ls-files`, all images under `docs/assets/`.
- [ ] `docs/index.md` exists; `docs/` root contains only user-facing docs; v2 material under `docs/v2/` with a README; historical material under `docs/maintainer/archive/`; `temp/` holds only the seven stage dirs + README.
- [ ] Tags `v1.0.0`–`v3.2.0` exist; one Release published; CHANGELOG matches the version file on the branch that ships.
- [ ] Social preview, description, topics, homepage, Discussions/Wiki set.
- [ ] CI green: tests · plugin-sync · link check; `plugins/prd-ce` regenerated if anything under `.claude/` or a seeded file changed.
- [ ] One LinkedIn launch post drafted against the release.

**T2 — v2 concept public is done when**

- [ ] The inheritance decision is recorded in the canon; C1–C9 carry rulings.
- [ ] Family shell + eight templates tick every §3.4 box; screenshots in `docs/assets/moments/`; fixture labelled illustrative.
- [ ] Every public v2 artifact carries its truth label (design direction / research input pending R0 / illustrative).
- [ ] README 2.0 (post-R0) and the site canon pages link the same eight moments with the same names.
- [ ] No count, command, or screenshot of an unbuilt capability appears anywhere public.

**T3** — build plan §11 minimum merge bar (13 items), unchanged.

---

## 9. Decision packet (owner) and risks

Each decision below is written so it can be made in under a minute: what it decides, the options, the
recommendation, and what happens the moment it is made. Record the call in the log at the end.

| # | Decision | Options | Recommendation | What happens next |
|---|---|---|---|---|
| **D1** | **Where does T1 polish land?** — *decided 2026-08-19: (b)* | (a) a branch cut from `main` now, merged by PR; (b) on `prd-ce-v2`, reaching `main` only with the v2 merge | Matt chose **(b)**; `main` stays at 3.2.0 until the v2 merge | Phase 1 executes on `prd-ce-v2` (this branch) |
| **D2** | **Does Wave 0B (the `*_template` split, 3.3.0, plugin payload refresh) land on `main` ahead of the v2 runtime?** | (a) yes, as a "v3.3.0 template release" after T1; (b) no, it waits for the v2 merge | **(a)** after T1 is green — it is template hygiene under BR-002, not a V2 runtime claim; caveat: it puts the v2 `PRD.md` at root on `main`, which is visible | If (a): a second PR from `prd-ce-v2` minus the v2 planning docs; CHANGELOG 3.3.0 rides with it |
| **D3** | **Dark mode in the moment shell** | (a) theme mechanics only in S1, warm-dark ramp later; (b) ramp in S1 | **(a)** — light + print first; the research's dark requirement is met by the mechanics; the ramp is a design decision worth its own pass | Recorded in the canon §2.1 with the inheritance decision |
| **D4** | **Publish canon pages / moment previews before R0?** | (a) yes, labelled "Design direction — research input", public vocabulary only; (b) wait for R0 | **(a)** — the essays are owner opinion (brief class B); R0 can still revise | Site Phase 1 may start its canon pages; README keeps its v2 note until R0 |
| **D5** | **Remove the client-flavoured material in `temp/v0.5-requirements/`** | (a) delete from the public repo (forward-only); (b) keep | **(a)** | Claude deletes in the T1 branch (and on v2 by reconciliation) |
| **D6** | **Motion proof** — *decided 2026-08-19: the readiness GIF.* Remaining sub-decision: who renders it | (a) Matt records with VHS from the tape in §10.3; (b) `brew install vhs` on this machine and Claude renders, Matt reviews | **(b)** if you are happy to install VHS — it removes a Matt-action; otherwise (a) | Tape + fixture script land in `docs/assets/readiness-demo/` either way |
| **D7** | **Tagline** — *decided 2026-08-19: keep "Memory as Infrastructure".* Subtitle direction given 2026-08-19: *an ontology layer built for product teams to build products that solve real problems*. Remaining: **confirm the exact wording** | working string now in README + GitHub description: "An ontology layer for product teams building products that solve real problems — with AI agents that remember." Variants in §10.1 (i–k) | keep the working string unless you want the memory clause dropped | Claude propagates the final string to README, description, and the social card (D14) |
| **D8** | **GitHub metadata strings** (applied with `gh repo edit`) | Description: `PRD-Led Context Engineering — Memory as Infrastructure. <subtitle>` · Topics add: `claude-code context-engineering spec-driven-development ai-agents agentic-coding prd agent-skills claude-code-skills product-management` · Topics remove: `nextjs supabase rapid-development` · Homepage: `https://www.gearheartai.org` | approve as written, or edit the strings | Claude runs one `gh repo edit` command |
| **D9** | **Discussions on · Wiki off** | (a) yes both; (b) Discussions only | **(a)** — the Wiki is empty and reads as a dead surface | Claude runs `gh repo edit --enable-discussions --enable-wiki=false`, then pins a "Start here" Discussion |
| **D10** | **Tags and releases** | (a) backfill `v1.0.0`–`v3.2.0` at the CHANGELOG commits + `v3.2.1` release for T1; (b) only `v3.2.1` forward | **(a)** — five Releases entries and an Atom feed for free; each is a post | Claude creates annotated tags and the release with the existing notes; **pushing tags is public** |
| **D11** | **External PR #68** (open since 2026-04-28) | (a) review and merge/adapt; (b) thank and close with a reason; (c) ask the author to rebase on the polished `main` | **(c)** with a warm note — it signals a maintained repo | Claude drafts the reply; Matt posts it (or approves Claude posting) |
| **D12** | **Prune stale remote branches** (≈18 `claude/*` and `feat/*`; list produced at execution) | (a) delete merged ones only; (b) delete all but `main`, `prd-ce-v2`, and live work branches | **(a)** first; (b) after confirming nothing unmerged is wanted | Claude lists, you tick, Claude deletes |
| **D13** | **Submit to `awesome-claude-code`** after the release | (a) yes; (b) later | **(a)** | Claude prepares the PR text; Matt approves the external PR |
| **D14** | **Social preview card** | approve the §10.4 draft composition (atlas crop + title + tagline + subtitle on the warm-paper ground), or ask for a variant | approve the draft after the subtitle (D7) lands in it | Matt uploads (UI only — Settings → Social preview) |
| **D15** | **Hero visual direction** (after the §10.2 experiments) | one of the eight concepts, or the typeset/no-illustration route | decide after seeing 2–3 rounds of outputs; my prior: concept 4 (the city map) or 8 (letterpress) fit the house style best | Claude produces the final asset at 16:9 + the 1280×640 crop |

### Decision log

| Date | Decision | Call | By |
|---|---|---|---|
| 2026-08-19 | D6 motion proof | GIF (readiness blocking → passing) — yes | Matt |
| 2026-08-19 | D7 tagline | Keep "Memory as Infrastructure"; add a subtitle (pending pick) | Matt |
| 2026-08-19 | Community profile | Complete it (not a blocker so far, but do it) | Matt |
| 2026-08-19 | Social card from the Atlas | Yes | Matt |
| 2026-08-19 | Execution mode | Claude acts on everything that needs neither approval nor Matt's creative hand | Matt |
| 2026-08-19 | D1 branch strategy | All T1 polish lands on `prd-ce-v2` only; `main` unchanged until the v2 merge | Matt |
| 2026-08-19 | D5 client material | Copy to the owner's private archive first, then remove from the repo — done | Matt |
| 2026-08-19 | D8 + D9 GitHub | Apply description/topics/homepage, Discussions on, Wiki off — done | Matt |
| 2026-08-19 | D7 subtitle direction | "An ontology layer built for product teams to build products that solve real problems" — working string in README/description: *An ontology layer for product teams building products that solve real problems — with AI agents that remember.* Final wording pending Matt | Matt |

### Risks

| Risk | Mitigation |
|---|---|
| Cleanup moves break links and the brief's `research_blueprint_path` | Do 1.1–1.2 in one PR; run the link check locally; update the brief's frontmatter in the same PR |
| Deleting Squad Status breaks `ghm-status-sync` | Check the skill tolerates missing `SECTION` markers; it targets the downstream `README_template.md` dashboard in consumers |
| "Personas retire" over-application when touching `.claude/` | Out of T1 scope entirely; T1 touches no skill content |
| Publishing v2 vocabulary before R0 freezes it | Claim class B labels + public vocabulary only; R0 can still revise |
| Regenerating the plugin payload produces a huge diff | Separate payload-only commit (v2-todo #18) |
| Claim drift on the site | Brief v2.0 §4 claim classes; capability rows still carry provenance |
| Two worktrees (T1 branch + v2 branch) drift on shared files (README, CHANGELOG, this tracker) | Tracker lives on `prd-ce-v2`; T1 commits are reconciled into v2 after each PR (build plan §11) |

---

## 10. Creative starting points (Matt's items)

### 10.1 The subtitle under "Memory as Infrastructure" (C1 / D7)

The tagline stays. The subtitle does the work the tagline deliberately doesn't: a verb, the outcome, and
the audience, in one breath (≤ 16 words). It sits directly under the H1 and becomes the GitHub description
and the social card's second line. Candidates — the test for each is *can a stranger tell what they get
and whether it is for them?*

| | Candidate | Verb · outcome · audience check |
|---|---|---|
| a | Give your AI coding agents a memory that outlives the session — a gated PRD and a markdown knowledge graph. | ✓ verb · ✓ outcome · audience implied (AI coding agents) |
| b | Build products with AI agents that remember every decision — in plain markdown, in your repo. | ✓ · ✓ · ✓ |
| c | A fork-ready method for teams building with AI agents: documentation that works as shared memory. | noun-led; ✓ audience; outcome softer |
| d | Stop re-briefing your AI every session. Keep product truth in a markdown knowledge graph it can navigate. | ✓ strong verb · ✓ · audience implied |
| **e** | **The open method for building products with AI agents — so the 50th session is smarter than the 1st.** | ✓ · ✓ (the line that already tested well) · ✓ — **recommended** |
| f | Turn documentation into the memory your AI agents and your team navigate together. | ✓ · ✓ · ✓; slightly abstract |
| g | A gated PRD, typed IDs, and a markdown knowledge graph — so humans and AI build from the same truth. | mechanism-first; good for the README, weaker on a social card |
| h | For product teams building with Claude Code: memory that survives the session, in files you own. | ✓ audience-first; names the ecosystem (search value) |

**Owner direction (2026-08-19):** *"something along the lines of an ontology layer built for product teams to build products that solve real problems."* Variants in that direction:

| | Candidate |
|---|---|
| **i** | **An ontology layer for product teams building products that solve real problems — with AI agents that remember.** *(working string now in README + GitHub description)* |
| j | An ontology layer built for product teams, so the products they build solve real problems. |
| k | The ontology layer for product teams: build products that solve real problems, with AI agents that never forget. |

Whatever the final wording, the same string goes into README 1.5, the GitHub description (D8), and the social card (D14).

### 10.2 Hero visual — experiment prompts (C2 / D15)

**What the visual has to do.** Say "memory as infrastructure" without the words; show that the memory is
*documents with addresses* (typed IDs, cross-references) rather than a brain or a glowing graph; and read
at 400 px wide on a phone. It must live beside `atlas.png`, so it inherits the repo's editorial palette:
warm paper `#f4efe3`, ink `#14120e`, a single ochre spot `#a8842c`, hairlines `#d8d0bd`, serif/grotesque
type, no gradients, no glow, no neon, no robots, no brains, no node-clouds.

**Tooling (per the workspace rules):** `/codex-image` is the default for hero illustrations; escalate to
Higgsfield only for a photoreal staged scene (concepts 1 and 6). Generate four variants per concept at
16:9 (README hero, ~1600×900), then crop the winner to 1280×640 (GitHub social) and 1200×630 (site OG).
Keep every prompt's *style block* identical so the comparison is about the idea, not the rendering.

**Shared style block (append to every prompt):**

> Editorial illustration in the manner of a printed briefing magazine: warm paper background #f4efe3,
> near-black ink #14120e linework, one ochre accent #a8842c used sparingly, hairline rules #d8d0bd, flat
> engraving/etching texture, generous negative space, no gradients, no glow, no neon, no 3D render, no
> robots, no brains, no floating node clouds, no text other than short monospace ID labels like BR-001,
> UJ-002, API-003. Composition reads clearly at small sizes. 16:9.

| # | Concept | Prompt (before the style block) | Why it might win |
|---|---|---|---|
| 1 | **The Atlas, printed** | A single printed briefing document titled only with a small kicker line lies on a plain desk in soft morning window light; its page shows a neatly ruled table of sections with ochre hairline rules and small monospace ID tags in the margin; a pencil rests on it. Photoreal, shallow depth of field, nothing else on the desk. | Continuity with the existing hero; credible, human |
| 2 | **Infrastructure, literally** | Architectural cross-section of a building's foundations drawn as an engraving: beneath the floors, neatly labelled conduits and pipes run between rooms; each conduit carries a small monospace tag (BR-001, UJ-002, API-003) and the rooms are labelled with short words; one ochre conduit is highlighted. | Makes "infrastructure" literal without being techie |
| 3 | **The card catalogue** | A wooden library card-catalogue drawer pulled open at an angle; the index cards have small typed tabs with monospace IDs; one card is lifted between two fingers and thin ochre threads run from it to three other drawers. Ink engraving on warm paper. | Memory as an addressable archive; the threads are the cross-references |
| 4 | **The city map** | A hand-drawn town plan on warm paper: a few named districts, streets connecting them, a compass rose, a legend in a corner listing short monospace prefixes; one street is traced in ochre and a small marker reads "Session 50". Cartographic ink style, no modern icons. | The knowledge graph as a map people already know how to read; fits the Atlas |
| 5 | **The title block** | An architectural drawing sheet (warm paper, ink — not cyan blueprint): the drawing is a simple plan of connected rooms labelled with monospace IDs; the lower-right title block carries a revision table with three dated rows; one revision row is marked in ochre. | Uses the methodology's own device (the revision table) |
| 6 | **Fifty briefings** | A stack of identical printed briefings on a desk, each with a tabbed edge carrying a date and a short monospace ID; the top one is open; soft daylight; the stack is tall enough to suggest many sessions. Photoreal, calm, nothing else in frame. | "The 50th session is smarter than the 1st" as a picture |
| 7 | **The switchboard** | A vintage telephone switchboard / patch panel drawn as an engraving: rows of jacks each labelled with a small monospace ID; a handful of patch cords connect them, one cord in ochre; no people, no screens. | Connections as physical infrastructure; strong silhouette |
| 8 | **Letterpress poster** | A typographic poster, no illustration: the sentence "If it isn't in the memory infrastructure, it isn't true." set large in a serif, ink on warm paper, a single ochre rule beneath, and a row of tiny monospace ID chips along the bottom edge; letterpress impression texture. | The house style is typographic; a typeset hero may beat any picture |

**Non-raster routes worth testing alongside:** (i) a *typeset* hero built as HTML/CSS in the house
stylesheet and screenshotted (Playwright — same pipeline as `atlas.png`); (ii) the loop SVG from the
walkthrough re-tokenised — the BMAD pattern of a diagram as the hero. Either can ship as the 16:9 and
crop to the social sizes.

**Judging rubric (score each output 0–2):** reads "memory / infrastructure" without words · shows
documents-with-addresses, not a brain · legible at 400 px · palette fidelity (paper, ink, one ochre) ·
does not look like generic AI art. Anything under 7/10 is out; ties go to the one that sits best beside
the Atlas screenshot.

### 10.3 The readiness GIF — storyboard, fixture, tape (C3 / 1.5)

**The story (25–30 s):** the repo tells you what to fix first. One repo, one fix, before and after.

| Beat | Seconds | On screen |
|---|---|---|
| 1 | 0–3 | Title card in the terminal: `PRD-Led Context Engineering — a repo that scores its own readiness` |
| 2 | 3–10 | `python3 scripts/readiness.py run --repo demo` → stage **v0.7 score=46.3 [BLOCK]** · "Found 0 API- entries; gate requires ≥1" · EPIC-01 WARN · **NEXT ACTIONS 1. Populate SoT.API_CONTRACTS.md — unblocks EPIC-01** |
| 3 | 10–16 | The fix: the API contracts file is populated (show the file appearing / `git checkout` of the real file, or a few typed lines) |
| 4 | 16–23 | Re-run → **v0.7 score=97.1 [PASS]** · EPIC-01 PASS · "No blockers — all SoT files passing." |
| 5 | 23–28 | End card: repo URL + `Memory as Infrastructure` |

**The fixture (verified 2026-08-19):** `tests/fixtures/healthy_repo` scores 97.1 PASS at the v0.6 → v0.7
gate. Replacing `SoT/SoT.API_CONTRACTS.md` with a three-line stub drops the stage to **46.3 BLOCK** with
exactly the two "high" findings and the single next action above; restoring the file returns 97.1 PASS.
(Stubbing `SoT.TESTING.md` instead gives a softer WARN story.) Script it as
`docs/assets/readiness-demo/make-demo.sh`: copy the fixture to a scratch dir, stub the file, run, restore,
run. Never record against the repo's own `SoT/`.

**Recording.** Preferred: [VHS](https://github.com/charmbracelet/vhs) (`brew install vhs`) — deterministic,
re-renderable, the tape is the source. Alternative: asciinema + agg, or a plain screen recording of the
script. Theme: a light terminal that reads next to the warm-paper screenshots (VHS `Theme` with a cream
background and ink text, or the built-in "Catppuccin Latte"); 1200×700, 16px font, `TypingSpeed 40ms`.

**VHS tape (starting point — save as `docs/assets/readiness-demo/readiness.tape`):**

```tape
Output docs/assets/readiness-demo.gif
Set Shell bash
Set FontSize 16
Set Width 1200
Set Height 700
Set Padding 24
Set Theme "Catppuccin Latte"
Set TypingSpeed 40ms

Hide
Type "bash docs/assets/readiness-demo/make-demo.sh prepare"   # copies the fixture to /tmp/prd-ce-demo and stubs API contracts
Enter
Type "clear"
Enter
Show

Type "# PRD-Led Context Engineering — a repo that scores its own readiness"
Enter
Sleep 2s
Type "python3 scripts/readiness.py run --repo /tmp/prd-ce-demo"
Enter
Sleep 6s

Type "# fix: draft the API contracts the gate asked for"
Enter
Type "bash docs/assets/readiness-demo/make-demo.sh fix"        # restores SoT.API_CONTRACTS.md
Enter
Sleep 1.5s

Type "python3 scripts/readiness.py run --repo /tmp/prd-ce-demo"
Enter
Sleep 6s

Type "# github.com/mattgierhart/PRD-driven-context-engineering — Memory as Infrastructure"
Enter
Sleep 3s
```

If the BLOCK screen scrolls, trim the readiness report in the demo to the STAGE + NEXT ACTIONS blocks
(the script can pipe through `sed -n '1,/NEXT ACTIONS/,+3p'`), or raise `Height`.

### 10.4 The social preview card (C4 / D14)

**Spec:** 1280×640 PNG (GitHub) and 1200×630 (site OG) from one composition. Warm-paper ground
`#f4efe3`; left two-thirds: the title "PRD-Led Context Engineering" in the serif, the tagline
"Memory as Infrastructure" beneath it in larger serif, the subtitle (D7) in the grotesque, a single ochre
rule; right third: the Atlas screenshot cropped to its table, bled off the right edge, with a hairline
frame. No badges, no logos other than an optional small GearHeart mark, no gradients. Keep 80 px safe
margins (LinkedIn crops aggressively). The same composition at 1200×630 is the site's `og-image.png`
once the site runs the same palette — or the site uses its own Editorial Luxury variant (brief §14).

**Draft:** a first composition can be generated deterministically from `atlas.png` with Pillow (no design
tool needed) — Claude produces it on request for review; the final is a 30-minute polish in any editor.

---

## 11. Provenance and changelog

Inputs: three read-only sweeps on 2026-08-19 (v2 corpus + design ancestry; repository inventory with md5
and diff verification; README/community/GitHub metadata via `gh`, peer repos via their public pages, live
site headers/markup, portfolio design language) and one structural design pass. Numbers are as observed on
that date; star counts are approximate.

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-19 | First gap analysis: three tiers, polish definition, Key Moments bar, cleanup tree, roadmap, owner decisions |
| 1.2 | 2026-08-19 | Tracker updated after execution (Phase 0 + most of Phase 1 done on `prd-ce-v2`); D1/D5/D7/D8/D9 logged; subtitle variants i–k; doc now lives at `docs/v2/` |
| 1.1 | 2026-08-19 | Owner review applied: tagline kept (subtitle added as the gap); §7 becomes the tracker; §9 becomes the decision packet with a log; new §10 creative starting points (subtitle candidates, hero-visual prompts, readiness-GIF storyboard + tape, social card spec) |
