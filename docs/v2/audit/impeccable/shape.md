SHAPE METRICS AND LEGIBILITY ANALYSIS — impeccable (pbakaus/impeccable, v4.0.4)
Repo root: `<scratchpad clone root>` (paths below are relative to it).

## 1. SKILL.src.md (`skill/SKILL.src.md`)

**85 lines, 1,497 words total.** The headline finding: the router for 23 commands is smaller than most single skills.

Internal breakdown by line range:

| Section | Lines | Share | Role |
|---|---|---|---|
| Frontmatter (name, trigger description, allowed-tools) | 1–10 (10) | 12% | Dispatch metadata; the entire trigger surface is ONE dense description string |
| Persona + 3 core principles | 12–17 (6) | 7% | Shared policy |
| Setup protocol (3 numbered steps) | 19–23 (5) | 6% | Session bootstrap: run `context.mjs` once, load ONE playbook, load `craft-floor.md` before editing |
| "How to design" (3 bolded rules) | 25–29 (5) | 6% | Shared policy |
| Modes (Persuade/Operate/Read/Experience) | 31–40 (10) | 12% | Shared policy |
| **Commands table** | 42–68 (27) | 32% | 23 commands × exactly **1 row each** (Command, Category, Description, Reference link) |
| Routing rules | 70–77 (8) | 9% | No-arg → menu; explicit → load reference; else general work |
| Utility commands (pin/hooks/doctor/drift rule) | 79–85 (7) | 8% | Meta-operations |

**Lines per command "section": min 1, median 1, max 1.** Command definitions do not live in the SKILL file at all — each command's row is a one-line pointer to `reference/<command>.md`. Router+dispatch ≈ 45 lines; shared policy ≈ 27 lines; command definitions ≈ 0 lines (fully externalized).

## 2. skill/reference/ — the playbook layer

**35 files, 4,936 lines, 49,348 words total.**

| Stat | Value | File |
|---|---|---|
| Min | 5 lines | `reference/craft.md` (deprecated-alias stub that redirects to normal routing) |
| Median | 94 lines | `reference/clarify.md` |
| Mean | 141 lines | — |
| Max | 827 lines | `reference/critique.md` |

Distribution: 10 files ≤ 59 lines; 14 files 60–119; 4 files 120–139; 7 files ≥ 200 (`onboard` 234, `optimize` 258, `adapt` 312, `live` 327, `harden` 336, `document` 416, `critique` 827). Depth is spent where the procedure is genuinely procedural (critique's dual-agent protocol, document's DESIGN.md spec), not evenly.

Non-command references carry shared machinery: `routing.md` (18 — the no-arg context-aware menu), `craft-floor.md` (55 — quality floor loaded just-in-time before edits), `new-work.md` (114 — shared entry for anything new), `operate.md` (61 — deep mode guidance), platform packs `ios.md`/`android.md` (51/46, loaded only on native platforms).

## 3. skill/scripts/ and skill/agents/

- `skill/scripts/`: **87 files, 43,115 lines** (37 top-level `.mjs`, 16 in `lib/`, 34 in `live/` incl. framework adapters). Deterministic machinery: context loader, 59-rule detector, live-mode server, critique storage, `pin.mjs`, `doctor.mjs`, plus `command-metadata.json` (per-command description + argument hint as data, not prose).
- `skill/agents/`: **4 files, 290 lines** (`impeccable-asset-producer.md` 104, `impeccable-manual-edit-applier.md` 103, `impeccable-finish-reviewer.md` 48, `impeccable-documenter.md` 35). The build also compiles each agent into a `reference/degraded/*.md` variant ("no subagent capability → run this role inline, disclose the substitution") — graceful degradation is generated, not hand-maintained.

## 4. Ratio analysis

- **Source vs generated:** `skill/` source = 48,426 tracked lines (127 files). Compiled provider trees (`.claude`, `.cursor`, `.gemini`, `.grok`, `plugin`, +12 more — 18 providers in `scripts/lib/transformers/providers.js`) = **1,080,612 tracked lines**, ~148–155 files and ~72k lines each. **One source tree fans out 22×** via `scripts/build.js` template substitution (`{{scripts_path}}` ×43, `{{command_prefix}}` ×33, `{{available_commands}}`, `{{ask_instruction}}`), with `<!-- rule:* -->` anchors stripped from shipped output.
- **Reference : router = 4,936 : 85 ≈ 58 : 1.** The router is 1.7% of the authored prose.
- **Per-task agent read path:** SKILL.md (85) + one command reference (median 94) + `craft-floor.md` (55) ≈ **~234 lines (~3k tokens) to execute any command** — 4.4% of the 5,311 authored prose lines. Context cost is O(1) in the number of commands.
- **Human quickstart path:** README.md line 5 is a blockquote with the complete path — `npx impeccable install`, then `/impeccable init`. **Two commands, reachable after reading 5 lines.** Total README = 433 lines, but ~60% is per-tool install matrices you skip.

## 5. Cross-link conventions (counted)

| Pattern | Count | Note |
|---|---|---|
| `reference/x.md`-style links from SKILL.src.md | 32 links → 31 unique files | Every command row carries exactly one; native variants add a second (`audit.native.md`, `adapt.native.md`) |
| reference→reference relative links | 48 | e.g. `craft.md` → `init.md`, `new-work.md` |
| `<!-- rule:kebab-id -->` anchors | 14 in SKILL.src.md, 114 across reference/ | Machine-checkable rule IDs; prose is under test (`tests/skill-reference.test.mjs` asserts section content with regexes — "authoring contracts") |
| `{{scripts_path}}/*.mjs` script pointers | 43 (20 unique scripts) | All resolve |
| **Dead links** | **0** | Checked all 32 SKILL links, all 48 reference→reference links, all 20 script pointers |

4 reference files not linked from SKILL.src.md (`android.md`, `ios.md`, `live-setup.md`, `visualize.md`) are all reachable from other references or loaded by `context.mjs` — no orphans.

## 6. Legibility audit (first-time-user read)

**First thing you're told to do:** line 5 of README.md — two commands in a blockquote, before any concept is explained. Value precedes theory.

**Concepts before first value: 3** (skill, command, `init`). The five-plane equivalent here (PRODUCT.md / DESIGN.md / surface briefs / config / critique snapshots) is *never front-loaded* — `init` writes them for you and later commands read them silently via `context.mjs`. The user learns the memory model by using it, not by reading about it.

**Naming voice:** every command is a **single lowercase word, imperative or comparative** — `audit`, `polish`, `distill`, `harden`, `bolder`, `quieter`. No namespacing, no version prefixes, no compound nouns. The pair `bolder`/`quieter` demonstrates the trick: names encode *direction of change*, so the mental model is "what do I want to happen," not "which module owns this." 23 commands are then grouped into **6 categories** (Build/Evaluate/Refine/Enhance/Fix/Iterate) — the table is scannable in one screen.

**Emoji/formatting:** effectively zero decorative emoji. The only glyphs are semantic status markers: `⚠️ DEGRADED:` banner (mandated first line of a degraded critique, `reference/critique.md:9`), ✅/❌ in before/after checklists (`harden.md`, `optimize.md`). Formatting conventions: tables as router artifacts, bolded rule-sentences as policy ("**The brief wins.**"), HTML-comment rule anchors invisible to renderers, one blockquote for the quickstart.

**What makes it structurally easy:**
1. **One entry point** — `/impeccable <verb>`; discoverability is the no-arg case, which renders a *context-aware* menu (`routing.md` reasons over git status, critique history, dev-server state) rather than a static list.
2. **One-row-per-command router** — total command inventory fits in 27 lines; description column doubles as disambiguation.
3. **Lazy, staged loading** — Setup names exactly what loads when: context script (always) → one playbook (per request) → craft-floor (only before edits). Never "read everything."
4. **Escape valves are commands too** — `pin` (promote a verb to a standalone shortcut), `hooks`, `doctor` (drift repair), with an explicit rule that drift is never fixed as a side effect.
5. **Deprecation as a 5-line stub** — `craft.md` stays in the table, costs 5 lines, and redirects; history doesn't clutter the namespace.

**Versus the anti-pattern (hypothetical 50-skill flat list):** 50 skills × ~90-line median = the same ~4,900 lines of content, but the *discovery* surface becomes 50 trigger descriptions competing in the harness's skill picker — the user must know the taxonomy before their first action, ~50 frontmatter blocks duplicate policy that impeccable states once in 27 shared-policy lines, cross-skill sequencing lives in nobody's file, and there is no no-arg menu because there is no root. Impeccable's shape moves the entire taxonomy problem into one 27-line table and makes shared policy literally shared (stated once, above the table, inherited by all 23 verbs). Your current PRD-CE skill list (50 `prd-vXX-*` entries visible in this very session) is a live instance of the anti-pattern: version-prefixed compound nouns, per-skill trigger paragraphs, no single entry point.

## Transferable patterns for PRD-CE v2

| Pattern | Copy / adapt / reject | Why |
|---|---|---|
| ≤100-line root router: frontmatter trigger + shared policy + 1-row-per-verb table + routing rules | **Copy** | Proven O(1) context cost: 85 lines route 23 commands; PRD-CE's 7 verbs + playbook column fits even smaller. This IS the Northstar shape. |
| One dense frontmatter `description` as the entire trigger surface | **Copy** | Replaces 50 competing trigger paragraphs with one; the harness matches once, the router disambiguates internally. |
| Per-verb/playbook reference files, median ~90 lines, depth uneven where procedure demands (5–827 range) | **Copy** | Registry of ~30 playbooks maps 1:1 to `reference/` files; don't force uniform length — let `check` policy packs be long and stubs be 5 lines. |
| Staged loading protocol named in Setup (context script → one playbook → quality floor just-in-time) | **Copy** | Directly maps: memory-plane loader → one verb playbook → gate criteria loaded only before advancement. Prevents "read everything" sessions. |
| No-arg → context-aware menu that reasons over live signals (`routing.md` + `context-signals.mjs`) | **Copy** | PRD-CE already has `status/readiness.json`; bare root command should read it and lead with 2–3 recommended next verbs, full verb table as fallback. Never auto-run. |
| Deterministic scripts as data/decision layer (`context.mjs`, detector, `command-metadata.json`), LLM-free | **Copy** | Matches PRD-CE's existing anti-Goodhart rule (deterministic `readiness.py`); command metadata as JSON keeps prose and dispatch data separate. |
| `<!-- rule:id -->` anchors + tests asserting prose content ("authoring contracts"), stripped at build | **Copy** | Makes methodology prose regression-testable — a validator can assert every gate rule still exists after edits; PRD-CE's ID discipline extends naturally to its own docs. |
| Single-word directional verb names (`bolder`/`quieter`), 6-category grouping | **Adapt** | The seven verbs are already right; apply the voice to playbook names (`--playbook=moat`, not `prd-v03-moat-definition`). Drop version prefixes from user-facing names; lifecycle position is metadata, not a name. |
| `pin` (promote a sub-verb to standalone shortcut) | **Adapt** | Nice adoption ramp: power users pin `check`. Low priority; needs harness support per provider. |
| `doctor` + "drift is never a side quest" rule | **Adapt** | PRD-CE equivalent: SoT/HTML-companion and readiness-input drift repair as an explicit verb-adjacent utility, with the same rule that design/build sessions report drift but don't fix it unasked. |
| Generated `degraded/` variants of subagent roles | **Adapt** | Smart portability trick if PRD-CE playbooks spawn subagents (research, red-team); generate the inline-fallback text, don't hand-write it. |
| 18-provider build fan-out (22× generated lines, per-provider transformers, template vars) | **Reject (for now)** | Impeccable pays 1.08M tracked generated lines to be tool-agnostic across 18 harnesses; PRD-CE's May-2026 decision is plugin-first on one harness. Adopt only the *pattern* of source/build separation (`SKILL.src.md` + template vars) so multi-provider is possible later without restructuring. |
| Committing all compiled provider trees into the repo root | **Reject** | Duplication noise (17 near-identical 72k-line trees) exists to make the repo itself installable; PRD-CE's plugin distribution channel makes this unnecessary. |
| Persona framing ("award-winning design director") | **Reject** | Design-domain content, not structure; PRD-CE's authority comes from the PRD/SoT truth-precedence chain, and a persona would blur its evidence-tier discipline. |