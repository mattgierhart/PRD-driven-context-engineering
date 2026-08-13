All reading complete. Here is the analysis report.

# Impeccable Reference System Analysis (for PRD-CE v2)

Analyzed clone: `.../scratchpad/impeccable` (upstream pbakaus/impeccable, v3-consolidated). Source of truth is `skill/` (SKILL.src.md + reference/ + agents/ + scripts/); `scripts/build.js` compiles it into 12+ harness-specific copies (`.claude/`, `.agents/`, `.cursor/`, `.gemini/`, …).

## 1. Reference Taxonomy

**35 files in `skill/reference/`, ~339KB total. min 555B, median ~5.2KB, max 42.7KB.** Four heavyweights (critique.md 42.7K, new-work.md 41.6K, live.md 35.6K, document.md 27.4K); everything else is 3–10K.

Naming: **file name == command name**, exactly as it appears in the router table (`polish` → `reference/polish.md`). Variants are dot-suffixed (`adapt.native.md`, `audit.native.md`). Six distinct types:

1. **Per-command playbooks** (23): one per row of the Commands table — including a 555-byte tombstone, `craft.md`: "`craft` is a deprecated alias… It adds no setup, interview, checkpoint, tool, or quality behavior" (craft.md:324). Deprecation costs one stub file, not a table footnote.
2. **Platform craft libraries** (`ios.md`, `android.md`): shared rule sets loaded by Setup on native projects, cross-referenced from command files.
3. **Shared quality floor** (`craft-floor.md`): loaded by *every* editing path immediately before writing UI.
4. **Mode depth** (`operate.md`): "The essentials live in SKILL.md's modes and [craft-floor.md]; this file is extended depth" (operate.md:811).
5. **Flow guides that are not commands**: `new-work.md` (the core build flow), `visualize.md` (a sub-flow of new-work), `routing.md` (the no-arg menu), `live-setup.md` (one-time config split out of live.md — "Not part of the per-session hot path", live-setup.md:681).
6. **Generated degraded fallbacks** (`reference/degraded/*.md`, build output only): "Generated from skill/agents/ at build time. Do not edit; edit the agent definition."

One-file-one-topic discipline holds, with one deliberate exception: `critique.md` packs its command *plus* its whole rubric library (`## Reference Material` at critique.md:297 — cognitive load taxonomy, Nielsen's 10 with 0–4 scoring anchors, 5 named test personas). Rationale is consumption-scoped: only critique ever loads that rubric, so splitting it would add a hop with no reader. The inverse rule also applies: `live-setup.md` was split *out* because the hot path shouldn't pay for one-time setup. **Size follows load frequency, not subject size.**

## 2. Progressive Disclosure

**Always in context: SKILL.md only** (~11KB source). Everything else is on-demand. The mechanism is a three-step Setup contract (SKILL.src.md:19–23):

1. **Deterministic context loader**: "Run `node <skill-base-dir>/scripts/context.mjs` once per session… It loads PRODUCT.md, DESIGN.md, the matching surface brief, and native-platform guidance when applicable; follow its directives and do not rerun it" (SKILL.src.md:21). The script emits typed directives the skill branches on: `NO_PRODUCT_MD`, `UPDATE_AVAILABLE`, `CONTEXT_STALE`, `MANUAL_DETECTOR_REQUIRED` (context.mjs:1018, 1107, 1343). Routing state lives in a *script's output*, not in the model's recall.
2. **Exactly-one-playbook rule**: "load the one playbook that owns the request: the Commands table's reference for an explicit or clearly implied sub-command, or reference/new-work.md for a new surface" (SKILL.src.md:22). The router is a markdown table with a `Reference` column per row (SKILL.src.md:44–68); no-arg invocations route to `routing.md`, which builds a context-aware menu from `context-signals.mjs` JSON — "Never auto-run a command; the recommendation is a suggestion the user confirms" (routing.md:973).
3. **Just-in-time floor load**: "After analysis and direction are resolved, load reference/craft-floor.md immediately before editing UI… Do not load it for planning-only work" (SKILL.src.md:23). Load timing is tied to the *phase of work*, not to session start.

Secondary mechanisms: conditional loads are declared in the *target file's own first line* ("Loaded from live.md only when live.mjs reports config_missing" — live-setup.md:681; "Load this from new-work.md on a comp-led build, when image generation is available" — visualize.md:1055), so a wrongly-loaded file self-ejects. In live mode, tool outputs carry an `_instructions` field that "is the authoritative next step for that exact situation… when it conflicts with your recollection of this document, `_instructions` wins" (live.md:725).

**Duplication control**: SKILL.md holds one table row per command; the reference holds the procedure. Where duplication is unavoidable it is *named*: "The report skeleton mirrors audit.md; keep the two in sync when changing it" (audit.native.md:164); DESIGN.md's frontmatter carries "That file is the source of truth; this frontmatter is the portable export. If a token changes there, update both" (DESIGN.md:5–7). Two further disciplines: **145 unique `<!-- rule:id -->` markers** pin individual instruction lines to stable IDs for external eval tooling, then get stripped from staged provider output (scripts/lib/utils.js:602–615); and **LLM-backed skill-behavior tests** assert the loading contract itself against four providers — "They fail when the agent stops following the loading contract" (tests/skill-behavior/README.md).

## 3. The PRODUCT.md / DESIGN.md Contract

Two files with disjoint ownership plus two scoped satellites:

- **PRODUCT.md** (3.4KB) — durable product truth: Register, Users, Product Purpose, Brand Personality, **Anti-references**, Design Principles, Accessibility. Written by `init` via interview + repo scan; "Treat repository evidence as a hypothesis, not user approval" (init.md:605). The Anti-references section is the sharpest idea: memory of what the product must *not* be ("dark mode with purple gradients… 'boost your productivity' copy", PRODUCT.md:25–26).
- **DESIGN.md** (29KB) — durable visual decisions in two layers. YAML frontmatter = machine-readable tokens, **normative**: "Tokens are normative; prose provides context for how to apply them" (document.md:459). Markdown body = *named rules with rationale* — "The Weight-Inversion Rule… This is deliberate… Do not normalize the two weights" (DESIGN.md:432), "The Texture Budget Rule" (DESIGN.md:406), plus a Do/Do-Not list. It follows an external portable spec (the google-labs design.md format, document.md:459) so other tools can consume it. Written by `document` (auto-extract, then "ask the user for qualitative language") or by the documenter sub-agent post-build.
- Satellites: **surface briefs** (`.impeccable/surfaces/`, per-route strategy), **critique snapshots** (`.impeccable/critique/`, the backlog `polish` reads via `critique-storage.mjs latest`, polish.md:31–36), and `.impeccable/config.json`.

What makes it work as persistent memory — four properties:

1. **One reader**: every session enters through `context.mjs`; no command reads memory ad hoc.
2. **One writer per file**: init owns PRODUCT.md, document/documenter own DESIGN.md, new-work replaces the world wholesale, `doctor` repairs schema only. "Missing DESIGN.md alone does not make a project greenfield" (SKILL.src.md:29) — file absence is evidence, not authority.
3. **Drift is a first-class, triaged concept**: doctor.md separates "Tool version… Schema drift… Truth drift" (doctor.md:433–435), with severities `auto`/`mention`, and the skill-level rule "**Never repair drift as a side effect of a design task**" (SKILL.src.md:85).
4. **Evidence direction is enforced**: the documenter writes memory *from the shipped artifact* — "every token and rule you write must be evidenced by the built code, never by what was planned… a rulebook written before the build gets defended against reality" (impeccable-documenter.md:17), and "Never canonize a craft-floor refusal into the system… A live session shipped five invented kickers and the documenter wrote their style into DESIGN.md; that is how one violation becomes the house style" (impeccable-documenter.md:31).

## 4. Reference File Anatomy

The house pattern for a good command reference:

- **Line 1 is the thesis plus the trap**, no preamble: "The trap is treating adaptation as scaling. The job is rethinking the experience for the new context" (adapt.md:4); "Quiet design is harder than bold design. Subtlety needs precision" (quieter.md:937).
- **A declared input gap** as a blockquote header: "> **Additional context needed**: the brand's emotional range" (delight.md:361) — the file tells you what it cannot infer.
- **A routing guard** up top when a variant exists: "**Web only.** Native platforms route to audit.native.md… switch to it now" (audit.md:134).
- **A visitor-mode split** (Persuade/Operate/Read/Experience) so one file serves both marketing and app surfaces without averaging them.
- **Assess → Plan → Execute → Verify** step skeleton; scoring rubrics get explicit 0–4 anchors (audit.md:151); escalation points are marked with the `{{ask_instruction}}` template var rather than left to judgment (distill.md:416, overdrive.md:889).
- **Hard invariants stated as invariants** with a mandated honesty artifact: "If you degrade for any reason, the report's first line MUST be a banner: `⚠️ DEGRADED: single-context (<reason>)`. A silent degraded critique is a failed critique" (critique.md:337).
- **Failure modes cited from observed sessions**, not hypotheticals: "the last two live sessions shipped five kickers past a reviewer that never looked" (impeccable-finish-reviewer.md:34).
- **Tone is governed by a buildable style guide**: docs/STYLE.md ("for every paragraph, point to the sentence that makes it specifically yours") with a regex denylist the build *fails* on (`validateProse` in scripts/build.js).

## 5. Sub-agents (`skill/agents/`)

Four worker definitions, markdown + frontmatter (`name`, `codex-name`, `tools` whitelist, `model: inherit`, `effort`, `max-turns`, `nickname-candidates`):

| Agent | Turns/effort | Job |
|---|---|---|
| impeccable-finish-reviewer | 30 / high, read-only, "You have no browser" (l.19) | Fresh-eyes review of the built artifact vs direction contract, approved comp, quality bar |
| impeccable-documenter | 30 / medium | Writes DESIGN.md from the shipped artifact |
| impeccable-asset-producer | 24 / medium | "production cleanup, not new art direction" — raster assets from approved mocks |
| impeccable-manual-edit-applier | 12 / medium | Applies live-mode manual copy edits to source |

The scoping pattern is a strict three-part contract: **Input Contract** (the exact packet of paths the parent must pass), **Checks/Workflow**, **Output Contract** ("Return the disposition line first, then exactly five sections… No praise, no summary prose", finish-reviewer:44). Two structural inventions worth noting: (a) **turn-budget survival instructions** — "by roughly the tenth turn stop reading and write. Name whatever went unread" (finish-reviewer:21); (b) **derived, unsoftenable verdicts** — "disposition: rebuild / fix / ship… It is derived, never felt… The parent reports your disposition word verbatim and has no authority to soften it" (finish-reviewer:40). For harnesses without sub-agents, the build generates `reference/degraded/*.md` wrappers: "you are both parties: produce the full output contract first, then act on it yourself" (degraded/finish-reviewer.md:2).

## Pattern Transfer Table

| Pattern | Copy / adapt / reject for PRD-CE v2 | Why |
|---|---|---|
| One always-loaded SKILL.md + router table with per-row reference links; "load the one playbook that owns the request" | **Copy** | This IS the seven-verbs + `--playbook=` registry shape, proven at 23 commands. The registry should be a table whose rows carry the playbook file link, and the exactly-one-playbook rule prevents context flooding. |
| File name == command/playbook name; deprecation = 555-byte tombstone file | **Copy** | Makes the registry self-verifying and lets `verb --playbook=name` resolve mechanically; retired playbooks stay routable without weight. |
| Deterministic context loader script whose *output directives* drive routing (`NO_PRODUCT_MD`, `CONTEXT_STALE`) | **Copy** | Matches PRD-CE's LLM-free-scorer principle exactly; `init`/session-start should print plane state + typed directives rather than have the model re-derive lifecycle state each session. |
| Size-follows-load-frequency (hot path small; one-time setup split out; single-consumer rubric embedded in its command file) | **Copy** | The discipline that keeps 339KB of reference usable. Directly answers how ~30 playbooks + libraries stay navigable. |
| Shared floor file loaded just-before-write, not at session start | **Adapt** | PRD-CE analog: an "SoT hygiene floor" (ID rules, confidence tiers, cross-ref discipline) loaded by `build`/`shape` immediately before writing artifacts. Content is domain-specific; the load-timing pattern transfers. |
| `<!-- rule:id -->` stable IDs on instruction lines, stripped at build, consumed by eval tests | **Copy** | PRD-CE already runs on an ID graph for *product* facts; this extends addressability to the *methodology's own instructions*, enabling `check` policy packs and behavior tests to cite exact rules. |
| Skill-behavior trace tests of the loading contract | **Adapt** | The only mechanism seen that keeps a router honest under refactoring. Start with 4–6 scenarios (verb routing, playbook load, plane load) rather than the full multi-provider matrix. |
| PRODUCT.md/DESIGN.md: one reader, one writer per file, external portable spec, tokens-normative frontmatter + named-rules prose | **Adapt** | Blueprint for the five planes: each plane file needs a declared owner verb, machine-readable frontmatter, and named rules with rationale. Anti-references sections belong in the Intent plane. |
| Drift taxonomy (tool/schema/truth) + `doctor` + "never repair drift as a side effect" | **Copy** | This is the Change plane's operating contract, nearly verbatim: three drift kinds, `auto`/`mention` severities, and a ban on silent memory repair during task work. |
| Documenter: memory written from shipped evidence, never intentions; refuses to canonize defects | **Copy** | The Reality plane in one paragraph — `learn` should harvest from the built artifact/devgraph, with an explicit not-canonized line, or observed defects become house style. |
| Sub-agent input/output contracts, turn ceilings, derived dispositions the parent can't soften | **Adapt** | For `check`: gate verdicts should be derived (PASS/WARN/BLOCK already are, via readiness.py) and reported verbatim; the input/output-contract format transfers to any PRD-CE reviewer agent. |
| Degraded-mode fallbacks generated from agent defs + mandatory `DEGRADED` banner | **Copy** | Cheap portability plus honesty: any PRD-CE step that downgrades (no sub-agent, quick mode skipping validation) should self-declare in output, matching P4 evidence discipline. |
| Multi-harness build system (template vars, `<codex>` blocks, 12 output trees) | **Reject (for now)** | Heavy machinery justified by impeccable's every-harness distribution. PRD-CE's May-2026 decision is plugin-first; adopt only the `{{scripts_path}}`-style indirection so a later port stays possible. |
| STYLE.md denylist enforced by the build (`validateProse`) | **Adapt** | A methodology product's voice drifts exactly like a design system; a small enforced denylist for playbook prose is cheap and compounding. Trim to PM-relevant tells. |
| Visitor modes, craft-floor content, worlds/comps/visualize flow, overdrive banner, nickname-candidates | **Reject** | Design-domain content and flavor. The owner's framing is right: the *structure* is the Northstar, not the material. |

Key repo paths for follow-up: `skill/SKILL.src.md`, `skill/reference/routing.md`, `skill/reference/craft-floor.md`, `skill/reference/doctor.md`, `skill/agents/impeccable-finish-reviewer.md`, `skill/scripts/context.mjs`, `scripts/lib/utils.js` (rule-marker/provider-block compilation), `docs/STYLE.md`, `tests/skill-behavior/README.md`.