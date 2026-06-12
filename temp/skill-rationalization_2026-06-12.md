---
title: "Skill Rationalization — Core/Secondary Tiering + Merge Proposals"
scope: ".claude/skills/ (methodology audit)"
updated: "2026-06-12"
---

# Skill Rationalization

> **Question answered**: with 47 skills (now 48 with the v0.5 vibe gate), are they all needed to
> keep the strength — a data-driven, SoT-generating knowledge graph? **Yes and no**: every skill's
> SoT-creation guidance is needed; not every skill needs to sit on the default path.
>
> **Hard constraint honored**: no skill, and no part of a skill that directs how to create a SoT
> file/ID entry, was deleted. Tiering applied this pass is non-destructive. Merges are PROPOSED
> only, each with an explicit relocation map for its SoT-generation guidance.
>
> **Applied this pass**: `tier: core|secondary` frontmatter on all 48 skills; Tier columns in
> `.claude/skills/README.md` + `skills-inventory.md`; tiered taxonomy in `domain-profile.yaml`;
> count reconciliation (root README said 47, skills README said 44 — true count was 47, now 48).
> **Harvest rule**: when the merge proposals below are triaged, execute approved ones and delete this file.

---

## 1. The rubric

| Tier | Definition | Test |
|---|---|---|
| **core** (33) | Produces a gate-mandatory SoT artifact (per `ghm-gate-check/references/gate-criteria.md`), orchestrates a stage chain, is the build engine, or is an essential operator | Delete it and some gate v0.X→v0.Y can no longer be satisfied |
| **secondary** (15) | Tactical/enrichment playbook: channel-specific, practice technique, optional-subtype producer | Delete it and every gate still passes — but you lose a playbook worth keeping |

Why this is the right line: the gates are already the repo's objective definition of "required."
Every gate's mandatory artifacts (CFD → BR/product-type → BR-pricing/KPI/FEA/moat-CFD → PER/UJ/SCR →
RISK/TECH → ARC/API/DBT → EPIC/TEST → DEP/RUN/MON → GTM/KPI-launch/CFD-feedback) trace to specific
producer skills. Anything else is optional by the system's own definition — no judgment call needed.

## 2. Tier assignments with rationale

### Core — the golden path (33)

| Stage | Skill | Why core |
|---|---|---|
| v0.1 | problem-framing, user-value-articulation | Gate v0.1→v0.2 requires 3+ CFD (pain + value) |
| v0.2 | competitive-landscape-mapping, product-type-classification | Gate requires competitor CFD + product-type BR |
| v0.3 | outcome-definition, pricing-model, moat-definition, features-value-planning | Gate requires KPI, BR-pricing, **Moat Analysis CFD** (gate-criteria.md:132), 3+ FEA; features is sole FEA- producer |
| v0.4 | persona-definition, user-journey-mapping, screen-flow-definition | Gate requires PER, 3+ UJ, 3+ SCR; each is the sole producer |
| v0.5 | risk-discovery-interview, technical-stack-selection, **vibe-gate-interview** (new) | Gate requires 5+ RISK, 3+ TECH; vibe gate is the stage-exit ritual (qualitative half of the gate) |
| v0.6 | architecture-design, technical-specification | Gate requires ARC, 3+ API, 3+ DBT; sole producers |
| v0.7 | epic-scoping, test-planning, implementation-loop | Gate requires 3+ EPIC, 3+ TEST; implementation-loop is the build engine (produces the code + devgraph) |
| v0.8 | release-planning, runbook-creation, monitoring-setup | Gate requires DEP, RUN, MON; sole producers |
| v0.9 | gtm-strategy, positioning-dunford, offer-construction-hormozi, launch-channels-orb, launch-metrics, feedback-loop-setup | Gate requires GTM index + launch KPI + feedback CFD channel; the Dunford→Hormozi→ORB chain is the orchestrated spine producing the GTM index |
| v1.0 | chasm-adoption-moore | The v1.0 spine; sole producer of ADO-STAGE/BEACHHEAD/WHOLE/REF |
| ops | ghm-gate-check, ghm-id-register, ghm-harvest, ghm-sot-builder | Gate verdicts, ID integrity, EPIC Phase E harvest (rule 03), only way to create new SoT types |

### Secondary — the playbooks (15)

| Stage | Skill | Why secondary (NOT why it's expendable) |
|---|---|---|
| v0.4 | visual-prototype-gate | Routes feedback to existing SCR-; no gate artifact. Reach for it when you need a visual demo |
| v0.6 | environment-setup | ENV- is not gate-mandatory; valuable for teams/CI, optional for a solo founder pre-build |
| v0.8 | changelog-as-marketing, drift-baseline-compare, marketing-ops-handoff | MON-CHG-/MON-DRIFT-/BR-MOPS- are optional subtypes; tactical ops plays |
| v0.9 | aeo-audit, alternatives-pages, cold-outreach-tiered, hn-reddit-launch | Channel-specific tactical plays attached to ORB channels; product-dependent |
| v1.0 | continuous-discovery-torres, mom-test-interview, case-study-builder, testimonial-collector | Practice techniques + social-proof harvesting; enrich CFD-/GTM- but gate-optional |
| ops | ghm-status-sync, ghm-template-sync | Display/maintenance helpers; merge proposals below |

**Sole-producer audit (constraint check)**: of the 15 secondary skills, the only sole producers of
ID subtypes are aeo-audit (GTM-AEO-), alternatives-pages (SCR-ALT-), cold-outreach-tiered (GTM-OUT-),
changelog (MON-CHG-), drift (MON-DRIFT-), mops (BR-MOPS-/GTM-MOPS-), case-study (CFD-CASE-/GTM-CASE-),
testimonial (CFD-TST-/GTM-TST-). All are **optional enrichment subtypes** — not required by any gate —
and all 15 skills remain in the library with their SoT-creation guidance intact. ✅ Nothing deleted.

## 3. Why "not all skills get used" — and why that's now by design

The lived problem: 47 flat skills means the agent (and the human) can't see which 60% matter today.
The fix is not deletion — it's **the golden path**. With tiers:

- A new fork runs 33 core skills v0.1→v1.0 and every gate can pass.
- Secondary skills stop creating "am I behind?" pressure — they're a menu, not a checklist.
- The knowledge graph keeps every producer: optional subtypes still have exactly one home each.

## 4. Merge proposals (Triage: Pending — none executed)

| # | Proposal | Rationale | SoT-guidance relocation map | Effort | Triage |
|---|---|---|---|---|---|
| 1 | `prd-v01-problem-framing` + `prd-v01-user-value-articulation` → single `prd-v01-spark` | Sequential halves of one stage; both produce CFD with the same evidence-tier/confidence protocol; always run back-to-back | Problem framing's 5 steps become Phase A; value articulation's steps become Phase B; both `references/` + `assets/` sets carried into the merged folder; CFD- creation protocol stated once (it's currently duplicated) | M | Pending |
| 2 | `ghm-status-sync` → final step of `ghm-gate-check` | Both read project state; status sync is 3.7KB and naturally runs after every gate verdict | Status-sync's README section-update protocol (Squad Status tables, metrics) becomes `ghm-gate-check/references/status-sync.md` + a "Step 4: Sync the dashboard" | S | Pending |
| 3 | `ghm-template-sync` → reference of `ghm-sot-builder` | Template maintenance is a rare sub-task of SoT-file ownership | Sync procedure becomes `ghm-sot-builder/references/template-sync.md`; trigger phrases merged into sot-builder's description | S | Pending |

**Considered and rejected** (do not re-propose): v0.2 pair merge (landscape vs. classification are
distinct frameworks with different outputs); v0.3 BR-producer consolidation (pricing/moat/features
encode different gate-mandatory frameworks — merging loses depth for no context win); splitting
large skills like implementation-loop (opposite of rationalization; size is in references, loaded
on demand).

## 5. Count reconciliation (fixed this pass)

| Surface | Said | Now |
|---|---|---|
| root README (×4 spots) | 47 skills / 41 stage | 48 skills / 42 stage + golden-path copy |
| .claude/skills/README.md | 44 skills total; tree missing ghm-template-sync | 48; tree complete; stage table split Core/Secondary |
| skills-inventory.md | nav table missing 4 ghm operators | all 48 rows + Tier column |
| domain-profile.yaml | missing ghm-template-sync, flat domain list | tiered core/secondary lists, complete |

## 6. If merges are approved (follow-up pass)

1. Execute relocation maps above (create merged folders, move references/assets, redirect triggers).
2. Re-run count reconciliation (48 → 45 if all three approved).
3. Update tier tables + domain-profile + this doc's harvest (delete it).
