---
title: "V2 Runtime-Surface Consolidation Audit — Skills, Hooks, Rules, Agents"
version: 1
status: "Research input — not accepted product truth (PRD.md authority order, item 7); execution gated on R0 and the v0.6/v0.7 gates"
purpose: "Full audit of the 50 skill directories, 9 hook components, 8 rules, and 4 agent personas against the v2 two-axis model (loop verbs public, planes internal). Every asset gets a named destination; nothing is deleted before its destination exists."
date: 2026-08-12
method: "13 parallel deep-readers over ~43,000 lines (every SKILL.md, reference, asset, hook implementation, rule, and persona file), each producing a per-skill richness ledger. Raw ledgers: temp/v2-audit/inventory/. Companion: docs/ECOSYSTEM_ONTOLOGY.md (the plane/verb model this audit executes against)."
scope_guard: "Product Management ecosystem only. No skill is modified or deleted by this document. Every disposition requires PRD acceptance at the stated gate."
---

# V2 Runtime-Surface Consolidation Audit

> **Thesis**: The 50 skill directories are two different things wearing one costume. About a third
> is **kernel** — invariants every loop pass needs (gate checking, ID registration, harvest, the
> build discipline) that were packaged as "skills" because skills were the only container. The
> rest is **method** — 20 years of operator judgment (numeric tripwires, anti-pattern tables,
> interview craft, named failure modes) wrapped in ~40% small-context-model scaffolding. The
> proposed v2 move — contingent on R0 and the v0.6/v0.7 gates — gives each its right container:
> **7 verbs** absorb the kernel, **~30 playbooks** carry the methods, **~15 policy packs** make
> the quality gates machine-checkable, and the operator knowledge survives verbatim in dedicated
> reference libraries — while the user-visible surface would shrink from 50 skills to one root
> command.

---

## 0. Standing and method

Research input (PRD authority order item 7), contingent on the ontology doc's R0 (record the
plane-first direction). This audit *maps*; it does not *move*. The prime directive throughout:

> **Harvest before retire.** No file is deleted until every asset flagged MUST-NOT-LOSE in its
> inventory ledger has a live destination. The ledgers live at
> [`temp/v2-audit/inventory/`](../temp/v2-audit/inventory/) — one per skill group plus
> hooks-rules and agents — committed in the same change as this document so they are versioned.
> Per rule 03 they sit in the scratchpad tier: pre-harvest working records that inform this
> audit, to be harvested into the durable migration spec before any execution (v0.6/v0.7).
> Whether they graduate to accepted evidence is the owner's Q5 call (§8).

Inventory base: 50 skill directories (41 `prd-vXX-*` stage skills, 7 `ghm-*` operators, `init`,
`SKILL_TEMPLATE`) totaling ~40,000 lines; 6 wired hooks + 2 libraries + 1 doc-spec; 8 rule files;
4 agent personas with their memory files (~43,000 lines read in total).

---

## 1. Headline findings

1. **The kernel/playbook seam follows one test: is it optional?** Everything a PM could *choose*
   (a positioning method, an interview technique) is playbook material. Everything every loop pass
   *relies on* (gate checking, ID registration, harvest, build discipline, drift baselines) is
   kernel. All 7 `ghm-*` operators, `init`, the entire v0.7 build trio, environment setup, drift
   baselining, and the feedback→ID circulation map to **kernel verb behavior** — none should
   survive as separately invocable skills.
2. **The scaffolding tax is ~40% and uniform.** Every older skill carries the same chassis:
   Consumes/Produces ceremony, workflow-position breadcrumbs, execution-mode tables, templates
   duplicated 2–3× (SKILL.md inline + assets/ + references/), and examples restated defensively —
   small-context insurance that is pure token cost now. Stripping it loses zero knowledge.
3. **The richness is concentrated and identifiable.** The distilled-experience material clusters
   in four shapes: **numeric tripwires** (>40% P2/P3 = scope bloat; CAC payback ≤3 months; 5
   personas max; <15 MVP pages; 30-50 tests; 14.4x burn rates; Fit ≥3/5 per channel), **anti-pattern
   tables** (the densest operator knowledge per token, consistently), **named AI-failure-mode
   discipline** (Assumption Drift, Smuggled Assumptions, Drive-By Refactoring — written for model
   babysitting but *not* era-bound; bigger models still do all of these), and **research craft**
   (salary-as-budget-proxy, 1–3-star review mining, the 48-hour findability test).
4. **The tier system is the Evidence plane's native schema, not skill content.** Six deliberate
   variants of one philosophy (pain tiers, desire tiers, WTP hierarchy, moat evidence quality,
   Mom-Test confidence ladder, segment signals) all descend from *"what people spend > build >
   quantify > say > we assume"* with a reject tier and a mandatory "would move to X/5 if…"
   upgrade condition. This graduates to kernel record fields; the per-context variants stay as a
   small rubric library. Do not flatten them — the pain/desire distinction is real.
5. **Three names, one idea.** Risk-closure (v0.5), architecture-closure (v0.6), and
   contract-closure (v0.6) are the same principle — *upstream nodes need downstream responses; no
   orphans* — which the devgraph/readiness machinery already checks. One kernel concept,
   per-stage policy-pack instantiations.
6. **The persona memory system is elaborate and empty.** Four silos, two hooks, seed/archive/
   promotion pipeline — **zero entries ever captured** in this repo. All four MEMORY.md files are
   byte-identical to their seeds. The migration cost of retiring personas here is zero.
7. **Two skills already model the v2 target.** `ghm-self-install` (thin orchestration over a
   deterministic manifest-driven script) is the kernel packaging model; `prd-v09-gtm-strategy`
   (an orchestrator whose references are framework playbooks) is the playbook-registry model. The
   newest single-file skills (drift, changelog, MOPS) are the playbook authoring style to keep.
8. **Duplication is systemic but solvable by pointing at machines.** The prefix→file map exists
   in 4+ places (`domain-profile.yaml` is canonical); verdict bands in 3 (`readiness.py` is
   canonical); never-touch lists in 2 (`install-manifest.yaml` is canonical); Session State in 5.
   v2 skills *read* the machine sources; the prose mirrors retire.

---

## 2. Target architecture (from the ontology doc, applied)

| Container | Count | What lives there |
|---|---|---|
| **Kernel verbs** (`init, explore, shape, decide, build, learn, check`) | 7 | The invariants: plane write-path + ID registration, gate checking, harvest/ingestion, build execution contract, drift baselining, state projection, install/upgrade |
| **Playbooks** (registry, invoked `verb --playbook=name`) | ~30 | The optional methods — each declares plane reads/writes, carries its distilled tables, cites shared references |
| **Policy packs** (named, consumed by `check`) | ~15 | Every "Quality Gates" checklist, converted to deterministic rules; seeded by gate-criteria.md's ~27 named failure patterns |
| **Reference libraries** | ~9 | The craft that multiple playbooks share (research recipes, benchmarks, anti-patterns, build discipline) |
| **Plane record schemas** | 5 + edge vocabulary | Entry templates (CFD/BR/FEA/UJ/SCR/TEST/DEP/EPIC/Session State…) stated once as plane schemas, not per-skill prose |
| **Worker contracts** | ~7 | The personas' ~14 "Subagent Templates," salvaged nearly verbatim |
| **Depth dial** | 1 | `--depth=quick\|standard\|deep` (rule 08 survives as the one mode doc) |

User-visible surface: **one root command + seven verbs**. Everything else is registry content.

---

## 3. Disposition map — all 50 skill directories

Full rationale and MUST-NOT-LOSE lists per skill: the inventory ledgers. Legend:
**K** = kernel verb behavior · **P** = playbook · **PP** = feeds a policy pack · **R** = feeds a
reference library · **S** = feeds a plane schema.

### Kernel absorptions (16)

| Skill | Verb | Notes |
|---|---|---|
| ghm-gate-check | `check` | gate-criteria.md → the policy-pack seed corpus (PP) |
| ghm-id-register | all (write-path) | relationship vocabulary + confidence ladder → edge/plane schema (S, R) |
| ghm-harvest | `learn` | three-way sort + contamination discipline = ingestion policy |
| ghm-sot-builder | schema extension | purity litmus + <20% self-doc cap → authoring policy (R) |
| ghm-status-sync | projection | README computed from planes; four rules → projection policy |
| ghm-self-install | `init` | the kernel packaging model — keep shape |
| ghm-template-sync | `init` (upgrade mode) | merge with self-install; manifest-driven, retire hardcoded lists |
| init | `init` | already v2-shaped |
| prd-v07-epic-scoping | `build` (packaging) | sizing numbers → kernel config; EPIC schema → S |
| prd-v07-implementation-loop | `build` (execution) | behavioral-examples.md preserved **verbatim** as build discipline (R); Assumptions & Ambiguities → Change-plane intake (S) |
| prd-v07-test-planning | `build` + PP | coverage minimums → `test-coverage` pack; process → build kernel; test-types → R |
| prd-v06-environment-setup | `build`/`init` | CLI-over-MCP doctrine → R; verification → PP |
| prd-v08-drift-baseline-compare | `learn` | baseline/compare/history = Reality-plane primitive; siblings already delegate to it |
| prd-v09-feedback-loop-setup (core) | `learn` | the feedback→ID circulation **is** Reality→Evidence→Change; thin `feedback-channels` playbook remains |
| prd-v04-visual-prototype-gate (feedback flow) | `learn` | typed disposition (Accepted/Deferred/Rejected) generalizes to Change-plane routing |
| prd-v09-gtm-strategy (orchestration) | `shape` | reconciliation table → `gtm-coherence` pack; channel-selection.md → channel-economics playbook; launch-strategies.md → launch-strategy-selection playbook; messaging-frameworks.md → commercial-benchmarks library |

### Playbooks (39 named → ~33 after the stated merges; §8 Q1's deeper merges could reach the mid-20s)

| Verb | Playbooks (source skills) |
|---|---|
| `explore` | problem-framing (v01-pf) · competitive-landscape (v02-clm) · red-team-interview (v05-rdi) · mom-test (v10) · brownfield-assets (v05-tss sub-mode) · moat-and-switching-costs (v03-md analysis half; its targeting/defensibility half lands via `decide` — BR-TGT compete/avoid/wedge rules with re-adjudication triggers) |
| `shape` | pain-to-value (v01-uva; merge candidate with problem-framing as one "spark" pair) · commercial-model family: outcome-metrics, pricing-model, feature-value-mapping (v03) · experience-design family: behavioral-personas, journey-mapping, screen-flows, visual-prototype (v04 — one pipeline, shared worked example) · architecture-adr (v06-ad) · api-contracts (v06-ts) · dunford-positioning (v09) · hormozi-offer (v09) · lead-lifecycle (v08-mops) · launch-metrics (v09-lm, definition half) · channel-economics (v09-gtm reference — CAC formula, CAC-tier→channel map, $500×3 testing cadence) · launch-strategy-selection (v09-gtm reference — strategy framework with rollback triggers and phase-exit criteria) |
| `decide` | product-type (v02-ptc) · build-buy-reuse (v05-tss) · orb-channel-mix (v09) · crossing-the-chasm (v10-moore, commitment half) |
| `build` | release-engineering (v08-rp) · observability-setup (v08-ms) · ops-runbooks (v08-rc) · changelog-marketing (v08) · tiered-outreach (v09) · hn-reddit-launch (v09) · alternatives-pages (v09) · social-proof (v10 case-study + testimonial, merged — ~40% of their text is shared rules) |
| `learn` | continuous-discovery (v10-torres) · adoption-stage (v10-moore, diagnostic half) · aeo-audit (v09 — the most future-proof skill in its group) · slo-error-budget (v08-ms reference — playbook OR shared reference library; owner call, see v08-a ledger) · feedback-channels (v09-fls, thin) |

`SKILL_TEMPLATE` retires into the **playbook authoring template** (carrying its anti-Goodhart
footnote verbatim). The v0.2→v1.0 stage *ordering* becomes the guided-journey doc, per the
ontology doc §3.2.

### Policy packs (~15, consolidated from every Quality Gates checklist)

spark-exit (evidence tiers + gap gate) · product-type-guardrails (the GTM constraints matrix —
"not suggestions, guardrails") · mvp-scope-integrity · moat-evidence-floor · wtp-before-price-lock
· kpi-gate-linkage (kill thresholds authored at v0.3) · experience-coverage (persona/journey/
screen bidirectional matrices — fully deterministic) · risk-register · tech-decisions ·
contract-closure (the unified three-names-one-idea principle) · test-coverage · build-completion
(devgraph green) · release-ready + monitoring-ready · ops-readiness + lead-lifecycle-readiness ·
launch-readiness (positioning-integrity + offer floors + ORB fit + comparison-page credibility) ·
launch-validation (the go/no-go + pivot/kill adjudicator — "maps almost 1:1 onto check + Change
plane") · chasm-crossing + social-proof + interview-hygiene (small, v1.0 cluster).

### Reference libraries (~9)

research-recipes (keyed by gap type / tier target; the salvage from four research-prompts.md) ·
commercial-benchmarks (dated + versioned; benchmarks.md + WTP calibration + switching-cost
thresholds) · product-type-strategy (the four Product Type × X matrices, stated once) ·
build-discipline (behavioral-examples.md verbatim + smuggled-assumptions + silent-assignment — the
crown jewel) · slo-error-budget + rollback-response (the operational-numbers vault) ·
design-tool-adapters (two tool-era files merged, refreshed) · anti-pattern library (merged,
deduplicated — "design for 10x not 1000x" currently lives in two skills verbatim) ·
interview-guides (mom-test + red-team question bank + case-study interview) · plane/edge schema
doc (relationship vocabulary, confidence ladders, entry formats).

---

## 4. Hooks and rules

Per the hooks-rules ledger — the posture finding first: **enforcement is uniformly advisory
(`ask`, never `deny`), and that is distilled experience, not weakness** — block-at-submit,
escalate-don't-block, false-positives-cost-trust. v2 should state it as an explicit hook
principle.

| Component | Disposition |
|---|---|
| context-validation.sh (SessionStart) | Re-key: read order becomes plane-keyed; "one In Progress EPIC" → "one active Change Set" (same invariant) |
| context-density-gate.sh (UserPromptSubmit) | Split: sizing thresholds (sparse/dense/broad — lifecycle-independent) re-key to Change-Set sizing; gate-approval branch folds into `check` packs |
| subagent-memory-load/save.sh | Keep; drift-check half re-keys to Reality plane |
| traceability-gate.sh (PreToolUse) | **Keep — the blueprint's "runtime policy enforcement" clause describes it almost verbatim**; EPIC → Change Set |
| sot-sync-reminder.sh (PostToolUse) | Upgrade: wire cascade_checklist's category map behind it, plane-keyed |
| cascade_checklist.py (unwired) | **Promote — it is a policy pack in embryo** (data-driven category→obligation map with section anchors) |
| metrics_drift_check.py | Keep; it is a working Reality-plane validator prototype |
| stage-gate-validation.md | Retire into packs (its stage table *is* the guided-journey pack; never wired, so zero runtime enforcement is lost) |
| HOOK_CONTRACT.md, _json.sh, settings.json | Keep as-is |
| Companion hook docs (context-validation.md, context-density-gate.md, cascade_checklist.md, metrics_drift_check.md) | Follow their implementation's disposition; the re-key pass should also close the doc gap for the four wired hooks that lack companions |

Rules: **03, 04, 06, 08 keep** (vocabulary re-keys only — the handoff markers, orphan-as-context-
leak framing, "the ID cross-references ARE the communication", and the depth-mode discipline all
survive). **01 re-keys** (the prompt-cache read-order rationale and four-tier eviction model are
lifecycle-independent context engineering — Evidence/Intent never evicted). **02 re-keys heavily —
it becomes the plane map.** **05 dissolves** into `check` (keep the authority principle: "README
reports status but does not authorize"). **07 re-keys** — it becomes the plane-keyed, goal-scoped
scorer's operating doc (layers, thresholds, overrides, causal chain), with its **Anti-Goodhart
block transferring verbatim**. The recurring "before v0.7 / from v0.7 onward" fork (6 files) re-keys
uniformly to "before / after an active Change Set exists" — one shared predicate, not per-file
edits.

---

## 5. Agents: retire the personas, salvage the contracts

> **Owner decision 2026-08-12**: persona retirement agreed ("they aren't adding value").
> Formal recording rides with R0; the salvage plan below stands.

Per the agents ledger: all four AGENT.md files are ~80% one template instantiated four times
(skills/outputs tables duplicating the registry, already drifted from it). The durable 20%
re-homes three ways:

1. **The ~14 "Subagent Templates" are proto-worker contracts** — every one already uses the
   "Do not X — Y only" scoping the blueprint asks of workers. Salvage nearly verbatim into ~7
   worker contracts (research, competitor-analyst, prototype-validator, implementation,
   verification, deploy-planner, evidence-reconciler).
2. **Anti-patterns and escalation boundaries** → verb guidance (`decide`'s trigger inventory is
   literally the personas' escalation lists — notable that no persona ever owned `decide`, v2's
   defining verb).
3. **METRO's feedback loop is vindicated, not deleted** — it *is* the Reality→Evidence→Change
   cycle, now kernel. DEVLAB's tool-grant asymmetry (only agent with Edit/Write/Bash) shows
   capability scoping already existed in the files — as grants, not prose.

**Memory**: collapse four empty silos into one consumer-owned orchestrator memory; keep the
two-pass hook mechanism re-pointed; Decisions → Change-plane records, Feedback/Patterns → the
existing LL- promotion path, Handoff Notes → orchestrator context-pack input. Consumer repos with
*populated* persona memories get a one-time harvest step; this repo's cost is zero.

---

## 6. The gaps: what does NOT exist yet (new authoring work)

The owner's hypotheses, checked against the corpus:

1. **Per-plane "what good looks like" rubrics — partially exist, scattered.** The tier systems,
   coverage matrices, and gate checklists are fragments of five plane-health rubrics that were
   never written as such. NEW: one rubric per plane (healthy Evidence = tiered, fresh, upgrade-
   conditions declared; healthy Intent = constrained, traced, no orphan decisions; healthy
   Delivery = closed contracts, tagged code; healthy Reality = baselined, drift-watched; healthy
   Change = no silent mutations, dispositioned proposals). Seeds: readiness dimensions +
   gate-criteria.md + the closure principle. These become `check`'s *internal* per-plane health
   rubrics, surfaced to users as goal-scoped views keyed to the PM loop — plane names stay off
   the public surface (ontology doc §10 Q2).
2. **Interview guides — exist, dispersed.** Mom-test, the red-team question bank, the case-study
   interview are real craft; they consolidate into the interview-guides reference library behind
   `explore`. Gap is organization, not content.
3. **Conversation/research → plane translation — GENUINELY ABSENT.** `ghm-harvest` ingests
   `temp/` files at cycle close; `feedback-loop` ingests post-launch channels. Nothing ingests
   *a research document or an AI conversation* into typed plane records with provenance (tier,
   confidence, Asserted-By, upgrade condition). NEW: `explore --playbook=research-intake` (a
   document in, Evidence-plane candidates out, quarantine for ambiguity) and
   `learn --playbook=conversation-harvest` (a session transcript in, proposed records out —
   never silently accepted). This session — deep-research report → ontology doc — is the use
   case, done by hand. These two playbooks are also the practical on-ramp to the Change plane's
   Observe/Propose channels.

---

## 7. Sequencing and governance

- **Now (definition, pre-v0.2)**: this audit + the ledgers are *candidate* inventory evidence,
  held as research input pending the owner's Q5 standing decision (§8). R0 (the direction
  record) remains the gate for everything.
- **v0.6 (contracts)**: plane schemas, policy-pack specs, playbook registry format, worker
  contracts — authored as contracts, consistent with ontology-doc R5–R9.
- **v0.7+ (execution, EPIC-gated)**: the actual migration — kernel absorptions, playbook moves,
  scaffolding strips — executed as Change-plane work with the harvest-before-retire rule enforced
  per skill via its MUST-NOT-LOSE ledger (harvested from `temp/` into the durable migration spec
  before execution).
- **BR-002 note**: consolidation changes the *seed packaging* (fewer, different files); the
  install manifest and distribution tests are the guardrail that consumer repos never lose
  content they own. The same Critical rule governs the §5 memory migration: any harvest of
  populated consumer persona memories must be **consumer-adjudicated and additive** — a proposed
  change the consumer reviews, never an installer-executed overwrite or deletion of
  `MEMORY.md`/`MEMORY_ARCHIVE.md` — and the distribution tests must prove populated memories
  survive upgrade unchanged unless the consumer accepts the migration (gate code
  `DISTRIBUTION_LEAK_OR_OVERWRITE`).

## 8. Open questions for the owner

> **Decision support (2026-08-12)**: a structural analysis of `pbakaus/impeccable` (the owner's
> packaging Northstar) at upstream `bd25359`/v4.0.4 is filed at
> [`temp/v2-audit/impeccable-northstar.md`](../temp/v2-audit/impeccable-northstar.md), with four
> detailed reports alongside. Its §3 proposes concrete answers to Q1 (keep ~30 playbooks; the
> count that matters is router rows — one table row per playbook, single-word names, O(1)
> per-task context), Q2 (outcome-named playbooks, framework attribution inside the file), Q3
> (pin-with-evidence + build-enforced counts), and Q4 (start at 4 workers, not 7).

1. **Merge appetite**: the audit proposes conservative merges (spark pair, experience-design
   family, social-proof pair, commercial-model umbrella). Deeper merges are possible; where is
   the line between "fewer skills" and losing named entry points the audience knows?
2. **Framework attribution**: Dunford/Hormozi/Moore/Torres names stay on playbooks (familiar,
   credible) or move to descriptive names with attribution inside?
3. **The volatile-content policy**: benchmarks, tool comparisons, platform specifics (HN timing,
   subreddit norms) need a dating/refresh convention — per-file `verified:` stamps like SoT
   entries?
4. **Worker count**: ~7 contracts salvaged from personas — right-sized, or fold further into the
   orchestrator?
5. **This audit's standing**: hold as input, or accept (with R0) as v0.2 evidence alongside the
   ontology doc?

---

## Provenance

Produced 2026-08-12 by a 13-agent inventory workflow (every skill/hook/rule/agent file read in
full; ~1.45M tokens of reading) + owner-session synthesis, on branch `prd-ce-v2` at commit
`fe1243c`. Raw per-group ledgers with per-asset verdicts (DISTILLED-EXPERIENCE vs GENERIC) and
MUST-NOT-LOSE lists: [`temp/v2-audit/inventory/`](../temp/v2-audit/inventory/). Companion model:
[`docs/ECOSYSTEM_ONTOLOGY.md`](ECOSYSTEM_ONTOLOGY.md).
