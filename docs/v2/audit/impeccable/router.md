# Impeccable Command Surface & Router — Structural Study

All paths relative to the clone root: `<scratchpad clone root>`

---

## 1. ROUTER ANATOMY

The entire router is **85 lines / ~11KB** (`skill/SKILL.src.md`), while the 36 reference files it dispatches to total ~330KB. The root is a dispatcher plus shared laws; all depth is lazy-loaded.

**Section-by-section structure of SKILL.src.md:**

| Lines | Section | Job |
|---|---|---|
| 1–10 | Frontmatter | trigger description, `argument-hint`, `allowed-tools`, license |
| 12 | Persona grant | one paragraph of identity ("award-winning design director") |
| 14–17 | Core principles | 3 bullets, incl. the bounded-verification cost cap |
| 19–23 | `## Setup` | 3 numbered steps: boot script → load one playbook → load quality floor |
| 25–29 | `## How to design` | 3 cross-cutting laws (brief wins; refine vs redesign; evidence over filename) |
| 31–40 | `## Modes` | 4 modes chosen per *surface* (Persuade/Operate/Read/Experience) |
| 42–68 | `## Commands` | the router table: 23 rows |
| 70–77 | Routing rules | the dispatch algorithm as 4 prose bullets |
| 79–85 | Utility commands | pin, hooks, doctor — deliberately outside the table |

**The routing mechanism is a table + four prose rules.** The table (`skill/SKILL.src.md:44-68`) has exactly four columns:

```
| Command | Category | Description | Reference |
| `audit [target]` | Evaluate | Technical quality checks (a11y, perf, responsive) | `reference/audit.md` · native: `reference/audit.native.md` |
```

Each command is declared **one row in the table + one file in `reference/`** — nothing inline. The row is the routing entry; the file is the whole playbook. Native platforms get a variant file routed *instead of* the web file (`audit.native.md`, `adapt.native.md`).

**The dispatch algorithm** (`skill/SKILL.src.md:70-75`, tagged `<!-- rule:skill-routing -->`):

> - **No argument:** read [routing.md] and present its context-aware menu; **never auto-run a command**.
> - **Explicit or clearly implied command:** load its reference (native variant on native platforms) and follow it. **Ask once if two commands fit.**
> - **Otherwise:** treat the request as general design work. Missing PRODUCT.md routes a new surface... through init, then new-work; a narrow refinement... proceeds on the incumbent implementation...
> - `teach` aliases `init`. `craft` is a deprecated alias...

So the root command is **tri-modal**: it *recommends* on bare invocation, *routes* on a named/implied command, and *does the work itself* under the shared laws for free-text requests (it does not force every request through a named command).

**Plain-language intent maps to commands in three layers:**
1. **Harness-level auto-trigger** — the frontmatter description (`skill/SKILL.src.md:3`) is a keyword-packed intent net ("design, redesign, shape, critique, audit, polish, clarify, distill, harden... Not for backend-only or non-UI tasks") so the skill fires without being named.
2. **Per-command "Use when" text** — `skill/scripts/command-metadata.json` is the single source of truth for descriptions, each phrased as intent triggers: `bolder`: *"Use when the user says the design looks bland, generic, too safe..."*. Build and `pin.mjs` both read this file (`CLAUDE.md:9`).
3. **Fallback to general work** — unmatched requests aren't shoehorned; they run under the shared laws with the right playbook (`new-work.md` for new surfaces).

**Bare invocation** loads `skill/reference/routing.md`, a 19-line playbook for generating a *context-aware* menu rather than a static list:

> "Setup has already run `context.mjs`. If that reported `NO_PRODUCT_MD`... lead the menu with `/impeccable init`... Otherwise run `node {{scripts_path}}/context-signals.mjs` once and read its JSON, then lead with the **2-3 highest-value next commands**, each with a one-line reason pulled from the signals, followed by the full menu... **Never auto-run a command; the recommendation is a suggestion the user confirms.**" (`routing.md:5`)

It then gives *heuristics over signals, not a score*: "Reason over the signals; there is no score to obey" (`routing.md:7`) — e.g. `critique.latest` null → recommend critique; low score / open P0s → `polish` "(it reads that snapshot as its backlog)"; `devServer.running` false → don't lead with `live`. It even runs the deterministic detector on changed files and folds real findings into the picks, with an explicit escape: "If detect errors or the tree is large and slow, skip it... never block the suggestion on it" (`routing.md:16`).

**Setup is a deterministic script, not prose recall** (`skill/SKILL.src.md:21`): `context.mjs` runs once per session, prints PRODUCT.md, DESIGN.md, the surface brief, native-platform guidance, and machine directives (`NO_PRODUCT_MD`, `UPDATE_AVAILABLE`, `CONTEXT_STALE`, `MANUAL_DETECTOR_REQUIRED`) that the skill text keys off (`skill/scripts/context.mjs:1-30`).

---

## 2. COMMAND DESIGN

**Naming: single words that name the user's desired outcome.** Mostly imperative verbs (`audit`, `polish`, `distill`, `harden`, `animate`, `clarify`, `adapt`, `optimize`, `shape`, `extract`, `document`, `onboard`), plus comparatives-as-commands (`bolder`, `quieter` — "make it X") and one mode noun (`live`). No internal jargon, no namespacing — the namespace is the parent skill.

**The Category column is the lifecycle**: Build (craft/shape/init/document/extract) → Evaluate (critique/audit) → Refine (polish/bolder/quieter/distill/harden/onboard) → Enhance (animate/colorize/typeset/layout/delight/overdrive) → Fix (clarify/adapt/optimize) → Iterate (live). Six categories over 23 commands, so the menu reads as a journey, not an alphabet.

**Commands compose through shared artifacts, not call chains.** Evaluate commands explicitly produce for others: `audit.md:1` — "Don't fix issues; **document them for other commands to address**." Critique writes `.impeccable/critique/*.md` snapshots, which polish "reads... as its backlog" (`routing.md:11`). Sequencing is by artifact handoff: `init` writes PRODUCT.md → `new-work`/`document` write DESIGN.md → everything else reads both. `shape` "owns task discovery, then enters new-work only for visual-world and surface-concept decisions" (`skill/SKILL.src.md:75`).

**Pinning** (`skill/SKILL.src.md:79`, `skill/scripts/pin.mjs`): `pin audit` creates a lightweight standalone `/audit` skill that redirects to `/impeccable audit`, written into every detected harness dir (`HARNESS_DIRS` list, `pin.mjs:24-28`). Two safety details: a `VALID_COMMANDS` whitelist (`pin.mjs:33-39`) and a `PIN_MARKER` comment (`<!-- impeccable-pinned-skill -->`, `pin.mjs:42`) so unpin can never delete a user's own skill. This resolves the favorites-vs-menu-pollution tension: one skill in the menu by default, shortcuts opt-in per user.

**Depth/scope control is multi-axis:**
- `[target]` argument scopes any command to a feature/page/component (`argument-hint: "[{{command_hint}}] [target]"`, `skill/SKILL.src.md:4`).
- **Mode** (Persuade/Operate/Read/Experience) is chosen "from the requested surface, not the product, and persist[ed] only in that surface brief" (`skill/SKILL.src.md:40`).
- **Platform** (web/ios/android/adaptive) is orthogonal, stored in PRODUCT.md, defaults to web, and swaps in native reference variants (`CLAUDE.md:35-48`).
- Depth is *capped*, not open: "Verify in bounded passes, not a loop... confirm with at most one more round, and stop polishing. Open-ended self-QA burns the user's money" (`skill/SKILL.src.md:17`).

**Read/write contract is explicit and layered:** PRODUCT.md = durable product truth (init owns it); DESIGN.md = durable visual decisions (document/new-work own it); `.impeccable/surfaces/` briefs = per-surface strategy; `.impeccable/config.json` shared vs `config.local.json` per-dev. Ownership is guarded in prose: "It does not invent a visual world and does not write DESIGN.md; new-work.md creates or expands one, and document.md records an incumbent one" (`init.md:3`). Nine reference files also open with a one-line input declaration: `> **Additional context needed**: quality bar and shipping constraints.` (`polish.md:1`) — a per-command "Consumes" header. Artifacts carry schema stamps (`<!-- impeccable:product-schema N -->`) and retired fields go into a deprecated-sections registry *with reasons*, because "told only that a field is deprecated, models preserve it 'just in case'" (`CLAUDE.md:67-69`).

---

## 3. USER MENTAL MODEL

**README.md teaches the identity in one line, then one action.** Line 3: "1 skill, 23 commands, live browser iteration, and 59 deterministic detector rules." Line 5 (quickstart, above everything else): "run `npx impeccable install`, then run `/impeccable init` inside your AI coding tool." Two commands and you're operating.

**The Why section is problem-first, product-second** (`README.md:7-16`): names the failure pattern users already recognize ("Inter for everything, purple-to-blue gradients, cards nested in cards"), then three bullets of what Impeccable adds: one setup flow, 23 commands as "a shared design vocabulary with your AI," and the deterministic detector.

**Learning the surface without reading everything** rests on four mechanisms:
1. One entry point: "All commands are accessed through `/impeccable`" (`README.md:38`), with a one-line table per command (`README.md:40-64`).
2. Self-describing tool: "Type `/impeccable` alone to see the full command list" (`README.md:294`) — and that menu is context-aware and recommends next steps.
3. `init` as tour guide: it "recommends the best commands to run next" (`command-metadata.json`, init entry).
4. Both invocation styles taught side by side: `/impeccable audit blog` and free-text `/impeccable redo this hero section` (`README.md:70-80`) — the surface works even if you never learn a command name.

**Journey framing** is the category axis (Build → Evaluate → Refine → Enhance → Fix → Iterate) rather than an explicit named funnel; the README usage examples walk it implicitly (audit → critique → polish → harden). Counts are load-bearing marketing ("23 commands") and the build **fails if any doc's count disagrees with the router table** (`generateCounts`, `CLAUDE.md:292-300`) — the mental model is kept true mechanically.

---

## 4. GUARDRAILS

- **Negative trigger scope in frontmatter**: "Not for backend-only or non-UI tasks" (`skill/SKILL.src.md:3`); `allowed-tools` restricted to exactly two Bash patterns (`:6-8`).
- **Never auto-run**: bare invocation always presents a menu; "the recommendation is a suggestion the user confirms" (`routing.md:5`).
- **"Which command do I need?" is answered by the tool**, two ways: the context-aware menu (signals + detector evidence → 2-3 picks with reasons), and mid-request disambiguation: "Ask once if two commands fit" (`skill/SKILL.src.md:73`) — one question, not a quiz.
- **Anti-taste-hijack**: "The brief wins... Redirecting a clear brief toward your taste is failure" (`:27`).
- **Scope semantics as law**: "Refinement preserves; redesign replaces... Never split the difference into polish on the discarded look" (`:28`); bolder.md hardens it further: "'Everything else stays' is a literal instruction" (`bolder.md:7`).
- **Cost cap on self-QA**: bounded inspection rounds, "Open-ended self-QA burns the user's money doing worse what the finish handoffs do better" (`:17`).
- **Maintenance quarantined from work**: "Never repair drift as a side effect of a design task" (`:85`); `doctor` is "a utility command, not a design command... deliberately not in `IMPECCABLE_SUB_COMMANDS`... and does not count toward the 23. Keep maintenance tooling out of the design menu" (`CLAUDE.md:71`).
- **Deprecated alias as a stub file**: `craft.md` is 5 lines saying it "adds no setup, interview, checkpoint, tool, or quality behavior" and "Do not tell users they need to invoke `craft`" — backward compatible without teaching the legacy path.
- **Platform guards inside references**: "**Web only.** Native platforms... route to audit.native.md instead; if the project is native, switch to it now" (`audit.md:5`).
- **Deliberate omission as a guardrail**: "a11y lives in `audit.md`, not in SKILL.md or the mode guidance. Models over-cautious themselves into safe, underdesigned output when reminded about accessibility at design time" (`CLAUDE.md:31`) — compliance concerns are quarantined to the evaluation command.
- **Rules are addressable and tested**: behavioral rules carry HTML-comment IDs (`<!-- rule:skill-routing -->`; 15 in SKILL.src.md, 130 across reference/), and `bun run test:skill-behavior` inlines the skill into four real models and **asserts on the tool-call trace** — "The trace is the source of truth" (`CLAUDE.md:193`). The router's promises are regression-tested, not aspirational.
- **Consolidation itself is defended**: "Do not add standalone skills... the `/` menu pollution problem is real" and "Do not reintroduce per-domain reference files" — v4 deleted 12 topic files and folded content into command references "where it is loaded only when it applies" (`CLAUDE.md:12-14`).

---

## Pattern Transfer Table

| Pattern | Copy / Adapt / Reject for PRD-CE v2 | Why |
|---|---|---|
| Tiny root router (85 lines) + all depth in lazily-loaded per-command reference files | **Copy** | Exactly the shape for 1 root command + 7 verbs: root holds verbs, laws, and the table; playbooks/policy packs load one-at-a-time ("load the one playbook that owns the request", SKILL.src.md:22) |
| Router table: `Command | Category | Description | Reference` | **Adapt** | PRD-CE's table rows are the 7 verbs; the Category column's job (journey grouping) is already done by the verbs themselves. Playbooks become a second registry table under their owning verb |
| Bare invocation → context-aware menu from a deterministic signals script, never auto-run | **Copy** | Bare `/prd` should read `status/readiness.json` + git signals and recommend 2-3 verb/playbook picks with reasons — "there is no score to obey" heuristics fit readiness dimensions perfectly |
| Trigger-optimized frontmatter description with explicit negative scope | **Copy** | One skill must catch all PM intent phrasing; "Not for backend-only" equivalent: "Not for direct code edits outside the lifecycle" |
| `command-metadata.json` as single source of truth feeding build, docs, and pin | **Copy** | PRD-CE's playbook registry needs exactly this: one JSON, counts and menus generated, build fails on drift |
| Free-text fallback: unmatched requests run under shared laws, not forced into a command | **Copy** | PM requests are messier than design requests; forcing every ask through a verb would make the surface brittle |
| Pin/unpin redirect shims with ownership marker + whitelist | **Adapt** | Useful for `--playbook` favorites (e.g. pin `check --policy=gates` to `/gate-check`); marker-comment safety is worth keeping verbatim |
| Deterministic boot script printing context + machine directives (`NO_PRODUCT_MD`, `CONTEXT_STALE`) | **Copy** | Same role as readiness.py, but the *directive vocabulary* (named flags the skill text branches on) is the transferable part — PRD-CE rules currently branch on prose |
| Two-axis context (mode per surface, platform per project) stored at the correct scope | **Adapt** | Maps to PRD-CE's stage (per product, in PRD.md) vs. depth mode quick/standard/deep (per invocation, never persisted) — the lesson is *store each axis where it lives* |
| Just-in-time quality floor (craft-floor.md loaded only before editing, "not for planning-only work") | **Adapt** | Policy packs should load only when `check` (or a build step) needs them, not sit in every verb's context |
| `> Additional context needed:` header convention on references | **Copy** | Cheap, scannable version of PRD-CE's Consumes/Produces sections; put it at line 1 of every playbook |
| Rule-ID comment markers on every behavioral sentence | **Copy** | Makes the ontology auditable and lets tests/validators cite the exact rule; aligns with PRD-CE's ID-graph ethos ("if it's not in the ID Graph, it doesn't exist") |
| LLM behavior tests asserting on tool-call traces across multiple providers | **Adapt** | The only real test of a router; costly, so reserve for the routing + init/boot paths, opt-in like impeccable does |
| Build validators: count sync, prose denylist, plugin-manifest contract | **Copy** | PRD-CE v2's "50 → 1" consolidation will rot without mechanical count/manifest guards; this is how impeccable keeps "23" true everywhere |
| Utility commands excluded from the command count and menu (doctor/hooks/pin) | **Copy** | Keep repo-maintenance verbs (migrate, doctor, sync) out of the seven-verb PM menu; the menu is the product |
| Artifact schema stamps + deprecated-field registry *with reasons* | **Copy** | Five-plane memory files will be read by future versions; the "models preserve deprecated fields just in case" failure mode applies directly |
| Deprecated alias as 5-line stub reference (craft.md) | **Copy** | The migration path for 50 legacy skill names: each becomes a stub declaring "adds no behavior" and pointing at verb + playbook |
| Compliance guidance quarantined to the evaluate command (a11y only in audit) | **Adapt** | Strong argument for keeping policy-pack content exclusively in `check` rather than sprinkling gate warnings through build/shape guidance |
| Persona-grant preamble ("award-winning design director") | **Adapt** | A short identity paragraph earning permission to be opinionated transfers; the design bravado doesn't. PRD-CE's version is evidence-discipline identity, not taste identity |
| Bounded verification passes as a core principle with cost rationale | **Copy** | Same economics as PRD-CE's batching/consolidation rules, but stated as a hard cap with a *why* — stronger than "prefer batching" |
| Provider compilation via `{{placeholders}}` (SKILL.src.md → per-provider builds) | **Reject (for now)** | PRD-CE distribution is decided as Claude-plugin-first; multi-harness transpilation is impeccable's problem, and adopting it early would tax the build for zero users |
| 59-rule deterministic detector wired to a hook | **Adapt** | Out of router scope but structurally instructive: PRD-CE's readiness.py already embodies "deterministic, LLM-free scorer" — the transferable extra is the hook wiring (auto-run after edits) and per-file inline waivers |