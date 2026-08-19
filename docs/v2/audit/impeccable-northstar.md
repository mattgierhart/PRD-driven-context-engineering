# Impeccable as Packaging Northstar — Structural Analysis for the §8 Decisions

**Status**: research input supporting `docs/v2/V2_SKILL_CONSOLIDATION_AUDIT.md` §8. Analyzed from a
fresh clone of upstream `pbakaus/impeccable` at `bd25359` (2026-08-13 — committed the day before
this analysis; the workspace's pinned copy at `a312da5e`/April is a full quarter behind, and
upstream is now v4.0.4 with substantially more machinery). Four parallel analyses (router,
references, build/quality, shape metrics) are filed alongside this memo in
[`impeccable/`](impeccable). Content domain ignored throughout — structure only.

---

## 1. The headline numbers (what "easy to understand" measures as)

| Metric | Impeccable | The lesson for v2 |
|---|---|---|
| Router size | **85 lines / ~1,500 words** routes 23 commands | The 7-verb root skill should be ≤100 lines |
| Command definition in router | **1 row each** (Command · Category · Description · Reference link) | Playbook registry = one table row per playbook, nothing inline |
| Reference : router ratio | 4,936 : 85 ≈ **58:1** | Depth lives in lazy-loaded files; the router is 1.7% of prose |
| Per-task read path | SKILL (85) + one reference (median 94) + floor (55) ≈ **~3k tokens, O(1) in command count** | Context cost must not grow with playbook count |
| Reference size range | 5–827 lines, median 94 — **size follows load frequency, not subject size** | Don't force uniform playbook length; tombstones cost 5 lines |
| Quickstart | **2 commands after reading 5 lines**; 3 concepts before first value | `init` then bare root; planes never front-loaded |
| Memory model teaching | **Never explained up front** — `init` writes it, commands read it silently | Exactly the "planes invisible" decision (ontology §10 Q2), independently validated |
| Trigger surface | **One dense frontmatter description (≤1024 chars)** for the whole skill | Replaces 50 competing trigger paragraphs — the anti-pattern we currently ship |
| Workers | **4 sub-agents total**, strict I/O contracts, turn ceilings | Calibrates our worker-count question (§8 Q4) |

The shape-metrics report names our current state precisely: the 50-skill flat list is "a live
instance of the anti-pattern: version-prefixed compound nouns, per-skill trigger paragraphs, no
single entry point."

## 2. The seven load-bearing mechanisms (copy these)

1. **Tri-modal root + context-aware menu.** Bare invocation loads a 19-line `routing.md` that
   reasons over *live signals* (git status, critique history, dev-server state) and leads with
   2–3 recommended next commands — "never auto-run; the recommendation is a suggestion the user
   confirms." v2 analog is nearly free: the bare root command reads `status/readiness.json` and
   recommends next verbs. Explicit commands route to exactly one reference; free-text requests
   run under shared laws without being shoehorned into a command.
2. **Deterministic session loader with typed directives.** `context.mjs` runs once, prints the
   memory files and machine directives (`NO_PRODUCT_MD`, `CONTEXT_STALE`, `UPDATE_AVAILABLE`)
   that the skill text branches on. Routing state lives in script output, not model recall —
   PRD-CE's LLM-free-scorer principle applied to session bootstrap. Our `context-validation.sh`
   hook + `readiness.py` are 80% of this already; they need typed directives.
3. **Staged loading protocol, named in Setup.** Context script (always) → *exactly one* playbook
   (per request) → quality floor (just before writing, "not for planning-only work"). The v2
   analog of `craft-floor.md` is an **SoT hygiene floor** (ID rules, confidence tiers, cross-ref
   discipline) loaded by `shape`/`build` immediately before records are written.
4. **Memory contract: one reader, one writer, drift triaged.** `PRODUCT.md`/`DESIGN.md` have
   disjoint owners; every session enters through one loader; drift has a taxonomy
   (tool/schema/truth) and a standing rule — "**never repair drift as a side effect of a design
   task**." The documenter writes memory *from the shipped artifact only* and explicitly refuses
   to canonize defects ("that is how one violation becomes the house style"). This is the
   plane-ownership model, the Change-plane discipline, and `learn`'s evidence direction, arrived
   at independently. Their `PRODUCT.md` "Anti-references" section is our Intent-plane "Not For".
5. **Instruction-level IDs + authoring-contract tests + behavioral trace tests.** 145
   `<!-- rule:id -->` markers pin normative sentences (stripped at build); unit tests
   regex-assert that specific instructions survive refactors; and the behavioral harness runs
   the real skill against cheap real models in sandboxed fixtures, asserting on the **tool-call
   trace** ("the trace is the source of truth, not the model's reply") with
   **baseline-as-regression-floor** ("regression = more failures than baseline, not any
   failures"). This is the highest-value import: v2's core risk is routing (does `explore` load
   the right playbook; does `check` load the right pack), and this proves it's testable for
   cents. It also extends our ID discipline to the methodology's own instructions.
6. **Derived counts, enforced.** The build parses the router table, counts commands and detector
   rules, then fails on any doc/manifest claiming a different number — hardened after "five
   stale counts shipped while the validator reported clean." Our "7 verbs, ~30 playbooks, ~15
   packs" claims should be derived from the registry and build-enforced. (We have three
   hand-synced gate-criteria copies today; this is the cure, generalized.)
7. **One-source build with drift-proofing.** `SKILL.src.md` (the `.src` suffix deliberately hides
   uncompiled source from skill-discovery CLIs) + transformer factory → committed provider
   output + PR `git diff --exit-code` gate + an auto-sync bot on main. Adopt the *factory shape*
   and the drift gates at 1-provider scale; reject the 17-provider matrix for now (plugin-first
   decision stands).

## 3. What this settles for §8

**Q1 (merge appetite): the count that matters is router rows, not playbook count.** Impeccable is
legible at 23 commands because each costs one table row, names are single words, six categories
make the table read as a journey, and per-task context is O(1). Verdict: **keep ~30 playbooks;
don't merge for count's sake** — merge only where content genuinely duplicates (the audit's
stated merges). Legibility comes from the registry table + naming voice, not from a smaller
number. Deprecations cost a 5-line tombstone, so consolidation is also cheap to walk back.

**Q2 (framework names): names encode the outcome; attribution moves inside.** Impeccable's voice
is single lowercase outcome words (`audit`, `polish`, `bolder`). Applied: `--playbook=positioning`
(Dunford credited in the file's first lines), `offer` (Hormozi), `moat`, `pricing`, `personas`,
`chasm` (Moore), `mom-test` (already a name in this voice), `discovery` (Torres). Drop version
prefixes from every user-facing name — lifecycle position is metadata. Recommendation: descriptive
single-word addresses, framework credit inside; `mom-test` keeps its name (it *is* the outcome
vocabulary).

**Q3 (volatile content): pin-with-evidence, then police.** Their pattern: empirically verified
values carry a verification note ("verified against a live Claude Code install, 2026-08") and
unknown values *fail the build* until verified. Applied: benchmark/reference files carry
`verified: YYYY-MM` frontmatter (our SoT staleness convention extended to the reference library),
and the counts validator flags stale stamps.

**Q4 (worker count): four, not seven.** Impeccable ships exactly 4 workers with strict input/
output contracts, turn ceilings, and dispositions "derived, never felt" that the parent "has no
authority to soften" — plus build-generated `degraded/` inline fallbacks for harnesses without
sub-agents. Recommendation: start v2 at **4 workers** (researcher, red-team/reviewer,
documenter-harvester, implementation), hold the remaining salvaged persona templates in the
reference library as dormant contracts. The degraded-fallback trick and the unsoftenable-verdict
rule both transfer (the latter is P7's "score is a floor" applied to worker output).

**Q5 (evidence standing)** — unchanged; this memo strengthens the audit as decision-support but
acceptance remains the owner's call.

## 4. Bonus convergences worth naming

- **They built our planes without naming them**: PRODUCT.md (Intent) + DESIGN.md (Delivery
  decisions) + critique snapshots (Evidence about the artifact) + drift detection (Reality vs
  memory) + doctor/adjudication rules (Change). Markdown canonical, machine frontmatter
  normative, prose carries named rules with rationale — ARC-001 validated by an unrelated
  project.
- **Two prose registers, two validators**: user-facing docs get the strict AI-tell denylist;
  LLM-facing instructions get a narrower one because "hardening repetition exists on purpose."
  Directly applicable to playbook authoring.
- **Reference file anatomy**: line 1 is the thesis plus the trap; a declared input gap; a routing
  guard; Assess→Plan→Execute→Verify skeleton; failure modes cited from observed sessions;
  mandated honesty banners (`⚠️ DEGRADED:`). This is the playbook authoring template §3's
  SKILL_TEMPLATE replacement should encode.

## 5. Explicitly rejected

The 17-provider fan-out and 1.08M generated lines (scale mismatch; keep the factory shape only) ·
committing all provider trees (plugin channel makes it unnecessary) · the persona grant
("award-winning design director" — our authority is the truth-precedence chain, not a persona) ·
all design-domain content (visitor modes, craft floor content, worlds/comps) · vendoring the
validator engine per-copy (ours is shared by design).

## Housekeeping flag (workspace, not this repo)

The MLG workspace's impeccable install is pinned to `a312da5e` (2026-04-30). Upstream is at
v4.0.4 with a materially evolved architecture (behavioral tests, degraded fallbacks, live mode).
The quarterly sync is due; worth a separate session.
