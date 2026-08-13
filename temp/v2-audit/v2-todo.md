# V2 Repo To-Do — What's Left to Update

**Status**: working list (scratchpad tier), 2026-08-13. Compiled from two repo sweeps (template
layer; packaging/top-docs) plus the session's audits. Effort: S < 1 hr · M ≈ half day · L =
multi-day. Grouped by when each item becomes legal — the groups are the sequence.

## Now (pre-R0 — no gate required)

| # | Item | Effort | What changes |
|---|---|---|---|
| 1 | CHANGELOG.md + MIGRATION.md **3.3.0 backfill** | S | Both stop at 3.2.0 while `.claude/VERSION` = 3.3.0. Fixing now removes a confound from the eventual v4 diff |
| 2 | **PRD-Methodology-Overview.pptx** | S | Feb-2026 deck, referenced nowhere; delete or archive with a dated note. Regenerating against the verb model is a separate content project |
| 3 | **Seed de-dup decision** | S | `docs/*.seed.md` are byte-identical to their canonical twins (md5-verified); `SoT/html/` ≈ `SoT_template/html/`. Decide single-sourcing *before* v2 edits, or every edit is done twice |
| 4 | **R1–R4 definition docs** (vocabulary registry, enforcement ladder, truth-state matrix, kernel/pack memo) | M | Already specified in ECOSYSTEM_ONTOLOGY.md §9; pure definition work |

## With R0 (the direction record — unlocks the vocabulary)

| # | Item | Effort | What changes |
|---|---|---|---|
| 5 | **R0 itself** | M | Owner-confirmed BR/ARC record (plane-first, loop-public, skills→playbooks, readiness re-key, persona retirement); revises PLAN:223 + rules touch list |
| 6 | **README.md full refresh** | **L** | The v2 story: one command + seven verbs; lifecycle table → guided journey; "47 Skills" feature section → registry framing; Squad Status section dies with personas; agent-squad feature rewritten around workers; keep the honest V2-status note |
| 7 | CLAUDE.md (root) re-key | S | Read order → projection-aware; Agent Registry pointer → verb/plane pointer; Core Rule survives verbatim; HTML-companion block untouched |
| 8 | CLAUDE_plugin_stub.md | S | "lifecycle skills, hooks, agents" → root command + verbs; drop persona clause; consumer-ownership paragraph verbatim |
| 9 | README_template.md | S | 10-row gate table → loop table; rewrite 4 "v0.7+" boundary phrasings; keep SECTION/CUSTOMIZABLE markers, ID legend, read order |

## v0.6 (contracts gate)

| # | Item | Effort | What changes |
|---|---|---|---|
| 10 | **Loop-verb machine token** decision | S, **blocking** | What replaces `v0.7` in `--gate`, `target_gate`, "Next Target Gate". Blocks PRD_template, READINESS_PROTOCOL, UNIQUE_ID_SYSTEM, html index — decide once, first |
| 11 | **PRD_template.md re-skeleton** | **L** | The ten stages ARE the document skeleton; 10 sections → 5 loop sections + Check block; strip 10 hard-coded `prd-v0*` skill names; keep the pedagogical prompt blocks, ID-ownership map, revision pattern, DoD block |
| 12 | SoT_template/ + UNIQUE_ID_SYSTEM re-key | M | 24-row registry "introduced at" column → verbs; one boilerplate sentence ("Before v0.7…") edited across ~22 files; **guard: PER- user personas are NOT the retiring agent personas** |
| 13 | SoT html review layer (×2 trees) | M | One column in index.html + ~11 one-line touches per tree; do together with #12; preserve the design doctrine in html/README (pattern provenance, ochre budget) |
| 14 | **install-manifest.yaml** — the hinge | M–L | Personas out (framework ×4, seeds ×4, never_touch glob); new classes for verb registry/playbooks/policy packs; **~50 `obsolete_framework_fingerprints` + an upgrade fixture** proving old consumers shed the retired surface cleanly (BR-002) |
| 15 | Rules + hooks re-key | M | Per audit §4 dispositions; the repeated "before/after v0.7" fork (6 files) becomes one shared "active Change Set exists?" predicate; promote cascade_checklist; BLUEPRINT.md table rides with #14 |
| 15b | **Surface-layer spec** (ontology §2.4) | M | Contract for the three surface kinds (front door / views / deliverables): which verb renders which surface, the deliverable emit format (extends DELIVERABLES_CONCEPT to plane records), as-of + supersede as backtracking; all derived, never canonical |
| 15c | **Key-moments question research** (docs/V2_KEY_MOMENTS.md §3) | L | Dedicated session: per moment — the key questions, the expression format (clarity anchor rendered), the pass/fail line in its pack; decide M8 promotion + the three candidate moments |

## v0.7+ (execution, EPIC-gated)

| # | Item | Effort | What changes |
|---|---|---|---|
| 16 | **The skill consolidation itself** | **XL** | The audit's migration: 16 kernel absorptions, ~30 playbooks, ~15 policy packs, harvest-before-retire per MUST-NOT-LOSE ledger |
| 17 | readiness.py + READINESS_PROTOCOL re-key | L | Plane-keyed, goal-scoped dimensions; docs strictly after scripts (they describe running code); bump schema_version deliberately |
| 18 | Packager + payload | S–M | package-plugin.sh drops the agent-flatten loop + exact-name excludes; check-plugin-sync surface list in lockstep; payload regen lands as a separate payload-only commit (it will be a huge diff) |
| 19 | EPIC_TEMPLATE (+ seed) | S | Persona routing → role-neutral worker slots; keep Session State + Assumptions blocks (best resumability content in the repo); `.seed.md` in lockstep |
| 20 | test_distribution.py fixture rework | M–L | Hard-names ghm skills + pins a v3.2 upgrade tree; needs v4 pins + persona-free assertions |

## v0.8 (release gate)

| # | Item | Effort | What changes |
|---|---|---|---|
| 21 | MIGRATION v3.3→v4.0 section + CHANGELOG 4.0.0 | L | The user-facing breaking contract (persona removal, skill collapse, projection promise); must be verified against a real upgrade fixture, so it cannot be written truthfully earlier |

## Cross-cutting cautions

- **The manifest is the hinge**: BLUEPRINT's table, install.sh's classes, the packager's surface
  list, and check-plugin-sync are all projections of `install-manifest.yaml`. Sequence it first;
  four S-items become mechanical.
- **50→1 skills is cheap at the packaging layer** (one manifest line, one `cp -R`); **persona
  retirement is the expensive part** there (manifest ×3, packager loop, sync list, payload dir).
- **"Personas retire" over-application risk**: PER- user-persona records, cards, and CSS survive
  everywhere. State it in every relevant work item.
- **install.sh needs ~zero logic change** as long as new v2 dirs are plain copies — the
  manifest-driven design pays off.
