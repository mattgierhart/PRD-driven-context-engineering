# PRD-CE → Claude Code Plugin: Conversion Plan (scratchpad)

> Status: planning draft for review. No framework files changed. Harvest to SoT/PRD when approved.
> Grounded in verified Claude Code plugin docs (code.claude.com/docs: plugins, plugins-reference,
> plugin-marketplaces, plugin-dependencies, skills).

## SCOPE DECISION (v1 = Scenario 1 / greenfield only)

The plugin's job decomposes into three layers — confirmed model:

- **Scaffold** — `/prd-ce:init` creates PRD.md, SoT/*.md, EPIC_TEMPLATE (empty, to template). One-time.
- **Process** — the `prd-v*` / `ghm-*` skills populate them with quality content in the right format.
- **Governance** — the 7 hooks enforce; `readiness.py` gates.

Two refinements: (1) `init` seeds *empty* structure; **EPIC instances** are generated later by
`prd-v07-epic-scoping`, not at init. (2) The PRD/SoT/EPIC files are the **consumer's data** — the
plugin versions/serves *templates + skills + hooks*; improving a skill improves *future* content, it
does not rewrite already-authored content. Structure is shared; instances are owned. This is what
makes "improve once, propagate everywhere" hold.

**IN scope (v1):** `/prd-ce:init` greenfield seeder · forward skills v0.1→v1.0 + supporting `ghm-` ·
7 hooks rewired + SessionStart discipline preamble · `readiness.py`+validators · plugin/marketplace manifests.

**OUT / backlogged:** Scenario 2 (mid-build) & Scenario 3 (live/retroactive) and their prerequisites
`ghm-stage-entry` + `ghm-graph-extract`; entry-mode branching in `init` (v1 assumes fresh repo);
MCP server; core/phase plugin split.

**Concrete v1 gap:** the manifest currently seeds `PRD.md` (the *populated example*). v1 needs a real
**`PRD_template.md`** (blank v0.1 skeleton) so new products don't inherit example content. Apply the
same check to any SoT file that isn't already in cleared-template state.

## Decisions locked in discussion

1. **Token cost is a non-issue** — progressive disclosure: ~50 skills ≈ 3–8 KB always-on. Splitting is
   justified by release cadence/modularity only, not cost.
2. **Discipline survives as a plugin** via hooks, not passive file-loading:
   - Directives/spine → **SessionStart hook `additionalContext`** (already done in `context-validation.sh`).
   - Enforcement → **hooks** (`traceability-gate`, `sot-sync-reminder`, `sot-update-trigger`).
   - Depth rules (02, 06, 07) → **on-demand reference skills**.
   - Only **config** (`domain-profile.yaml`) + optional human `CLAUDE.md` stub get **seeded**.
3. **Granularity**: ship a **monolith `prd-ce`** now, structured so a later split into
   `prd-core` + phase plugins (via `dependencies`) is mechanical. `prd-core` is the future MCP host.
4. **Seeder**: `ghm-self-install` (PR #77) becomes a bundled skill `/prd-ce:init` that plants bucket-2/3.

## The single-source question (the crux of "is the repo set up right?")

A plugin must be the **source of truth** for skills/agents/hooks, or we recreate drift between a dev
copy in `.claude/` and a built copy in the plugin. Two strategies:

- **(A) Plugin-is-source + repo dogfoods it [TARGET].** Move skills/agents/hooks OUT of `.claude/`
  into the plugin subtree; this repo consumes its own plugin (local marketplace / `--plugin-dir`).
  One copy. The methodology repo becomes its own first consumer. Cleanest; bigger reshape.
- **(B) Author in `.claude/`, build the plugin via a transform step [INTERIM].** A deterministic
  `package` script (reusing `install-manifest.yaml`) copies + transforms (flatten agents, rewrite
  hook paths) into the plugin subtree. `.claude/` = source, plugin = built artifact. Lower risk,
  but two copies until we cut over to (A).

**Recommendation:** build with (B) to de-risk, cut over to (A) once the plugin is proven. Both keep
the *volatile* layer single-sourced at the end.

## Target repo layout (monolith, multi-plugin-ready)

```
prd-driven-context-engineering/                 # this repo = source + marketplace
├── .claude-plugin/
│   └── marketplace.json                        # lists prd-ce (+ future core/phase plugins)
├── plugins/
│   └── prd-ce/
│       ├── .claude-plugin/plugin.json          # name: prd-ce, OMIT version during dev
│       ├── skills/                             # from .claude/skills/<name>/SKILL.md (shape matches)
│       │   ├── prd-v01-problem-framing/ … (all 41 prd-* )
│       │   ├── ghm-*/ …                         (gate-check, harvest, id-register, sot-builder, status-sync, template-sync)
│       │   ├── init/                            # ← ghm-self-install reworked as the seeder
│       │   └── operating-discipline/            # ← reference skill carrying rules 02/06/07 depth
│       ├── agents/                             # FLATTENED: horizon.md, studio.md, devlab.md, metro.md
│       │   └── (AGENT.md bodies; MEMORY.md does NOT ship — it's seeded)
│       ├── hooks/hooks.json                    # rewired from .claude/settings.json
│       ├── scripts/                            # readiness.py, validators, _merge_settings.py, asof.py …
│       └── docs/                               # methodology docs (DEVELOPMENT_GRAPH, READINESS_PROTOCOL)
├── .claude/                                     # repo dogfoods the plugin (consumer config only)
├── CLAUDE.md / PRD.md / SoT/ / epics/           # the EXAMPLE product instance — stays, never ships
└── README.md
```

## File-by-file move map

| Source (today) | Plugin target | Transform |
|---|---|---|
| `.claude/skills/<name>/SKILL.md` (+assets/refs) | `plugins/prd-ce/skills/<name>/` | copy as-is; strip non-standard frontmatter only if it breaks (`context: fork`, `allowed-tools` — verify honored) |
| `.claude/agents/<name>/AGENT.md` | `plugins/prd-ce/agents/<name>.md` | **flatten** dir → file |
| `.claude/agents/<name>/MEMORY.md` | *(not shipped)* → seeded by `/prd-ce:init` | becomes a starter template |
| `.claude/settings.json` (hooks block) | `plugins/prd-ce/hooks/hooks.json` | rewrite each `bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/x.sh` → `bash "${CLAUDE_PLUGIN_ROOT}"/hooks/x.sh` |
| `.claude/hooks/*.sh` | `plugins/prd-ce/hooks/*.sh` | scripts still read consumer files via cwd/`$CLAUDE_PROJECT_DIR` — only the *invocation path* changes |
| `scripts/*.py`, `validate-*.sh` | `plugins/prd-ce/scripts/` | callers that say `python scripts/readiness.py` → `python "${CLAUDE_PLUGIN_ROOT}"/scripts/readiness.py` (reads consumer SoT/PRD) |
| `.claude/rules/*.md` | split: spine → SessionStart preamble; depth → `skills/operating-discipline/` | rules dir does NOT auto-load in plugins |
| `.claude/domain-profile.yaml` | seeded by `/prd-ce:init` | consumer-local config |
| `.claude/install-manifest.yaml` | `plugins/prd-ce/skills/init/` reference | re-bucket: framework→plugin payload (no longer copied), template_seed→what init plants |
| `CLAUDE.md`, `PRD.md`, `SoT/`, `epics/` | **stay in repo as example** | never ship in plugin |

## Hook rewiring detail (the main mechanical risk)

- 7 hooks currently locate their own scripts via `$CLAUDE_PROJECT_DIR/.claude/hooks/`. → `${CLAUDE_PLUGIN_ROOT}/hooks/`.
- Scripts that **read the consumer's project** (context-validation reads `README.md`/`PRD.md`/`epics/`;
  sot-update reads `SoT/`) already use **relative/cwd paths** → unchanged, they naturally read the
  consumer's working dir. ✅ This is why the split works cleanly.
- `context-validation.sh` SessionStart already emits `additionalContext` → extend it with the condensed
  **operating preamble** (authority order, ID-graph core rule, gate-before-advance). This is the
  always-on discipline, plugin-native, zero-drift.

## plugin.json (draft)

```json
{
  "name": "prd-ce",
  "displayName": "PRD-Driven Context Engineering",
  "description": "PRD lifecycle methodology: skills, agents, hooks, readiness scoring.",
  "author": { "name": "Matt Gierhart" },
  "license": "MIT"
  // version OMITTED during active dev → every commit ships to consumers
}
```

## marketplace.json (draft)

```json
{
  "name": "prd-ce-methodology",
  "owner": { "name": "Matt Gierhart" },
  "plugins": [ { "name": "prd-ce", "source": "./plugins/prd-ce", "description": "PRD-CE methodology core" } ]
}
```
Consumer: `/plugin marketplace add mattgierhart/prd-driven-context-engineering` → `/plugin install prd-ce@prd-ce-methodology`.

## `/prd-ce:init` seeder (from ghm-self-install)

Plants bucket-2/3 the plugin can't: `domain-profile.yaml`, `PRD.md`/`SoT/`/`EPIC` templates, agent
`MEMORY.md` starters, optional human `CLAUDE.md` stub. Reuses `install-manifest.yaml` `template_seed`
list + the `_merge_settings.py` discipline. Non-destructive (never_touch honored).

## Sequencing (each step shippable, reversible)

1. **Scaffold** `plugins/prd-ce/` + `.claude-plugin/` manifests (strategy B build script). No `.claude/` changes yet.
2. **Rewire hooks** into `hooks/hooks.json` with `${CLAUDE_PLUGIN_ROOT}`; verify each emits valid JSON.
3. **Flatten agents**; ship AGENT.md bodies, hold MEMORY.md as seed templates.
4. **Preamble**: extend SessionStart hook with the operating spine; build `operating-discipline` reference skill.
5. **Init skill**: port ghm-self-install → `/prd-ce:init`.
6. **Validate**: `claude --plugin-dir ./plugins/prd-ce`, `claude plugin validate`, install into a scratch repo, run a lifecycle skill, run readiness.
7. **Dogfood (cut to strategy A)**: repo consumes its own plugin; delete the dev duplicates in `.claude/`.
8. **Publish**: marketplace public; README install instructions.

## Open questions / risks

- **Verify**: are skill frontmatter keys `context:`/`allowed-tools` honored (or harmlessly ignored) in plugins? (likely ignored)
- **Verify**: does `claude --plugin-dir` resolve `${CLAUDE_PLUGIN_ROOT}` for local dev identically to installed?
- **Decide**: how much human-readable `CLAUDE.md` narrative to seed vs leave to the live preamble.
- **Relationship to PR #77**: self-install becomes `/prd-ce:init`; may re-scope or supersede #77.
- **Strategy A cutover** removes the dev `.claude/` skills — sequence carefully so the repo never breaks mid-migration.

## Verification (when built)

- `claude plugin validate ./plugins/prd-ce` passes.
- Install into a fresh repo via local marketplace; `/prd-ce:init` seeds scaffold; SessionStart preamble appears.
- A `prd-v0X` skill runs and reads the consumer's `domain-profile.yaml` (not the plugin's).
- `readiness.py` (from plugin) scores the consumer's SoT/PRD.
- Update flow: bump a skill in the plugin, `/plugin marketplace update`, change reflected in consumer.

---

## Stress test (persona: Priya, solo founder, 3 products at 3 stages)

Walked one persona through three entry modes to find where the plugin strains.

| Scenario | Entry mode | Experience | Verdict |
|---|---|---|---|
| **InvoiceFlow** (new idea) | greenfield | `init` → frame problem → flow v0.1→v0.7, graph grows as byproduct; `epic-scoping` emits EPICs | **Shines.** Built for this. Only cost = skill volume (use quick-mode). |
| **MeetingMuse** (2mo, code, no specs) | mid-build | `init` brownfield-safe; but methodology is forward-staged. Enters ~v0.6 to document as-built `API-`/`DBT-`/`FEA-`, then epic-scope next chunk | **Strains.** `epic-scoping` consumes thin upstream IDs; `readiness.py` BLOCKs on empty v0.1–v0.5. No clean mid-lifecycle on-ramp. |
| **LedgerLink** (18mo live, no docs) | retroactive | Reverse-engineer SoTs from a large codebase; forward "decide" skills are a poor fit. `prd-v05` (brownfield discovery) + `prd-v06` (document as-built) + `ghm-id-register` help; `@implements` retro-tagging is huge | **Hardest.** No code→graph extractor → manual backfill. Honest value = "stop bleeding forward + gradual backfill," not instant coverage. |

### Findings → design changes the conversion must account for

1. **[High] Forward-bias / no mid-lifecycle on-ramp.** 2 of 3 real scenarios enter mid/late and hit readiness BLOCKs from empty upstream IDs. → new skill **`ghm-stage-entry`**.
2. **[High] No brownfield extractor.** `code_node_types` + bridge relations are *defined* in `domain-profile.yaml` and `docs/DEVELOPMENT_GRAPH.md`, but no shipped AST pass *populates* `devgraph.json` from existing code. → new skill/script **`ghm-graph-extract`** (also the seed of the future MCP "queryable graph").
3. **[Med] Readiness misleads on partial adoption** — BLOCK reads as "failing" when stages were intentionally skipped. → scorer should distinguish *not-yet-done* from *intentionally-skipped*.
4. **[Med] `init` must branch by entry mode** (greenfield→v0.1 / mid-build→backfill spine / live→extract-first), not just seed files. Reuses the greenfield/brownfield detection from PR #77.
5. **[✓] Always-on discipline via SessionStart hook works in all three entry modes** — confirms the packaging decision holds.

## Proposed new skills (specs)

### `ghm-stage-entry` (methodology operator)
- **Purpose:** Adopt PRD-CE at a non-zero stage without the scorer punishing intentionally-skipped upstream work.
- **Trigger:** "enter at v0.X", "I'm already mid-build", "set current stage", run by `/prd-ce:init` when brownfield detected.
- **Behavior:** records declared current stage; writes `dimension_overrides`/disable for skipped upstream stages into `status/readiness.json` inputs; emits a "backfill checklist" of the minimum upstream IDs worth recovering (the spine: a `CFD-`/`BR-` anchor, `FEA-` catalog) so downstream skills aren't starved.
- **Produces:** readiness config + a backfill checklist. No new ID prefix.

### `ghm-graph-extract` (methodology operator, deterministic/LLM-free)
- **Purpose:** Bootstrap the knowledge-graph foundation for a live product from existing code.
- **Trigger:** "extract graph from code", "onboard existing codebase", run by `/prd-ce:init` when live-product detected.
- **Behavior:** AST pass over the consumer repo → `status/devgraph.json` code nodes (per `code_node_types`); proposes **candidate** `API-`/`DBT-` SoT entries from endpoints/tables for human confirmation via `ghm-id-register`; reads existing `@implements` tags to seed bridge edges.
- **Produces:** `devgraph.json` + candidate SoT entries. Must stay deterministic per rule 07 (no LLM in the scorer path). Natural backend for the future MCP `graph.query` tools.

> Sequencing note: build these **before** the strategy-A cutover, since `/prd-ce:init`'s entry-mode branching depends on both.

