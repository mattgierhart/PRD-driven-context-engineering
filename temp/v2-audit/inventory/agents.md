# Agent Persona Audit vs. V2 Direction

Sources read: `.claude/agents/{horizon,studio,devlab,metro}/{AGENT.md,MEMORY.md,MEMORY.seed.md,MEMORY_ARCHIVE.md}`, `.claude/domain-profile.yaml` (agents section, lines 155–173), plus the memory hooks (`.claude/hooks/subagent-memory-load.sh`, `subagent-memory-save.sh`) and the v2 blueprint (`docs/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md` §7.6, lines 1370–1382; deferral list line 2657; directive line 3260) to ground dispositions.

**Headline finding that frames everything below: all four MEMORY.md files are empty scaffolds, byte-identical to their MEMORY.seed.md, and all four MEMORY_ARCHIVE.md tables have zero rows.** The per-persona memory system has never captured a single entry in this repo. There is no distilled experience to migrate — only the AGENT.md prose and the hook mechanism itself.

---

## HORIZON — Strategy, v0.1–v0.5

**Role**: Market & product strategy lead; origin of every cycle and receiver of post-launch feedback ("Identity" section: "both the origin and the iteration engine").

**Durable knowledge held**:
- *Distilled-experience (worth saving)*: the **Anti-patterns** section is real methodology judgment — "Generic ICP definitions ('SMBs who need efficiency')", "Skipping 'not for' segment definition", "Risk register without early warning signals", "Advancing gates without CFD-XXX evidence references". The **Decision Authority** split (autonomous: ICP prioritization, research direction; escalate: pivots, pricing changes, segment abandonment) is a genuine governance boundary. The three **Subagent Templates** (Competitor-Analyst, User-Researcher, Risk-Scout) carry a real scoping discipline: "Do not recommend strategy—surface data only".
- *Boilerplate*: "Skills I Invoke" table (duplicates skill frontmatter/domain-profile), "Outputs Produced" table (duplicates ID-ownership registry in rule 02/domain-profile), collaboration ASCII diagrams, Inputs Required.
- *Memory*: empty template (Feedback/Patterns/Decisions/Handoff Notes headers, no entries).

**Verb/plane mapping**: `explore` + `shape` over **Evidence** (CFD entries) and **Intent** (BR, KPI, RISK). Its escalation list is really a `decide` trigger inventory. v0.5 risk review is an early `check`.

**V2 disposition — retire the persona; re-home three ways**:
1. Anti-patterns and evidence discipline → `explore`/`shape` verb guidance (the "generic ICP" and "not-for segment" rules are shape-quality checks, not agent identity).
2. The three subagent templates → **Research worker** contracts, nearly verbatim — they already are "self-contained contracts" in the blueprint's sense.
3. Escalation boundaries → `decide` verb governance (which things require human adjudication).
Rationale: blueprint §7.6 removes lifecycle ownership from workers; everything HORIZON durably holds is either verb guidance or a worker contract, not a persona.

---

## STUDIO — Design, v0.3–v0.6

**Role**: UX lead bridging validated journeys to implementation; deliberately overlapping span (concurrent with HORIZON v0.3–v0.4, with DEVLAB v0.6).

**Durable knowledge held**:
- *Distilled-experience*: Anti-patterns — "Visual polish before interaction validation", "Creating DES-XXX without DEVLAB feasibility check", "Desktop-first without mobile consideration". The Prototype-Validator template ("Do not redesign—validate and document gaps") and Token-Extractor template are scoped worker contracts. The DEVLAB handoff contract (tokens, breakpoints, interaction states) is a real Delivery-plane record spec.
- *Boilerplate*: same parallel structure as HORIZON; the skills table lists only v0.4 skills despite a claimed v0.3–v0.6 span — the persona's span and its actual skill surface already disagree.
- *Memory*: empty template.

**Verb/plane mapping**: `shape` → `build` over the **Intent → Delivery** boundary (SCR/DES are Delivery-plane artifacts; its CFD validation findings are Evidence). Prototype-Validator is a `check` activity.

**V2 disposition — retire; convert the core into the UX/architecture worker**. The blueprint's worker list names "UX/architecture worker" explicitly. Feasibility anti-patterns → `shape`/`build` playbook guidance; Prototype-Validator → verification worker contract; the DES/token handoff contract → Delivery-plane record schema, enforced by the Change Set, not by a persona remembering to do it. The v0.3–v0.6 overlap is itself an argument for retirement: lifecycle ownership was never clean for design.

---

## DEVLAB — Build, v0.6–v0.8

**Role**: Technical lead from architecture through deployment; "the builder".

**Durable knowledge held**:
- *Distilled-experience*: Anti-patterns — "Building before v0.5 gate passes", "Implementing without TEST-XXX coverage plan", "Deployment without DEP-XXX runbook". Decision Authority ("architecture decisions affecting cost >20%, security concerns" escalate) is real governance. Four worker templates (Tech-Scout, API-Designer, Test-Planner, Deploy-Planner), each with specify-don't-implement scoping.
- *Boilerplate*: skills table (10 skills, duplicated from registry), outputs table (duplicates ID ownership), collaboration diagram.
- *Memory*: empty template.
- *Notable*: DEVLAB is the **only agent with Edit/Write/Bash** in its frontmatter tools line (horizon/studio are read-only + web; metro is read + bash + web). Capability scoping already exists in this file — it is expressed as tool grants, not as persona prose.

**Verb/plane mapping**: `build` + `check` over the **Delivery** plane (ARC/TECH/API/DBT/TEST/DEP/RUN). Its v0.7 epic-scoping duty ("break work into context windows") is exactly the orchestrator's context-pack compilation job in v2 — not a worker concern at all.

**V2 disposition — retire; split three ways**: implementation worker (build execution + traceability tags), verification worker (Test-Planner template + TEST discipline), and orchestrator (epic scoping / context compilation moves up, per blueprint §7.5–7.6: the orchestrator compiles context and merges outputs). DEVLAB is the closest thing to an existing capability worker, which makes it the cheapest conversion.

---

## METRO — Ops, v0.9–v1.0

**Role**: GTM and adoption; "the closer and the feedback engine".

**Durable knowledge held**:
- *Distilled-experience*: the **Feedback Loop (CRITICAL)** section and lifecycle-circularity diagram are the one piece of genuine architecture in any persona file — CFD entries from post-launch feed HORIZON's next cycle. Anti-patterns: "Vanity metrics without revenue/retention connection", "Treating launch as the end (it's the beginning of iteration)", "Distribution as afterthought". Iteration-Synthesizer template ("validated/invalidated assumptions… do not make strategy decisions") is a clean Evidence-reconciler contract.
- *Boilerplate*: skills table lists only 3 of the ~14 v0.9/v1.0 skills in domain-profile — again the persona's claimed surface has drifted from the registry.
- *Memory*: empty template.

**Verb/plane mapping**: `learn` over the **Reality** plane, feeding **Evidence** — METRO's feedback loop *is* the Reality → Evidence → Change cycle that v2 promotes to first-class structure. Metric tracking against KPI targets is `check`.

**V2 disposition — retire; the persona is vindicated, not just deleted**. Its central idea (closed loop) becomes the `learn` verb and Reality-plane ingestion, so nothing of value depends on the METRO name. Two re-homes: feedback-loop discipline and vanity-metrics anti-patterns → `learn` verb guidance; Iteration-Synthesizer → the blueprint's named **Evidence reconciler** worker. The GTM/channel/launch methodology itself is explicitly deferred from v2 core ("Broad pricing and GTM methodology in core" in the Defer list) → optional registry playbooks, not core.

---

## The MEMORY.md mechanism under v2

**How it works today**: `subagent-memory-load.sh` (SubagentStart) injects `.claude/agents/<agent_type>/MEMORY.md` as additionalContext; `subagent-memory-save.sh` (SubagentStop) issues a mandatory extraction directive (append to Feedback/Patterns/Decisions/Handoff Notes) and `git add`s the file on the follow-up stop. Plugin-scoped agents (`prd-ce:horizon`) map to the *consumer repo's* unscoped path — the memory is consumer-owned; the plugin ships only `MEMORY.seed.md`. The archive header declares the promotion path: entries graduate to `SoT/SoT.LESSONS_LEARNED.md` at EPIC Phase E harvest.

**Under v2, when personas go away**:
- The hook keying (`agent_type` → persona directory) breaks. Re-keying per capability worker would be wrong: v2 workers are ephemeral, receive self-contained contracts, and "do not carry implicit lifecycle ownership" — persistent per-worker memory rebuilds persona silos under new names.
- The four memory categories map cleanly onto v2 structures, which is where the consumer-owned content should live: **Decisions** (with "Alternatives rejected") are literally Change-plane adjudication records — output of `decide`; **Feedback** and **Patterns** are project lessons → the existing `SoT.LESSONS_LEARNED.md` promotion path, i.e., accepted SoT; **Handoff Notes** (inter-agent friction) become orchestrator knowledge — input to context-pack compilation, since the orchestrator now owns transitions.
- Practical shape: collapse four silos into **one consumer-owned project memory attached to the orchestrator** (single MEMORY.md or `product/` lessons records), with the save hook retained but re-pointed; keep the seed/consumer split from the packaging fix (commit 11297db). For consumer repos that *have* populated persona memories, v2 migration needs a one-time harvest step: promote entries by category (Decisions → Change records, rest → lessons), discard the persona keying.
- In this repo the migration cost is zero — there is nothing in any of the eight memory/archive files.

---

## Group observations

1. **The memory system is elaborate and empty.** Four silos, two hooks, seed/archive/promotion pipeline — zero entries captured. Splitting memory four ways puts each silo below critical mass (any session writes to at most one), which is itself evidence for v2's single-orchestrator memory.
2. **The four AGENT.md files are ~80% one template instantiated four times.** Skills tables, outputs tables, and inputs sections duplicate `domain-profile.yaml` and rule 02, and have already drifted from the registry (STUDIO lists 4 of its skills, METRO 3 of ~14). The non-duplicated 20% — anti-patterns, escalation boundaries, subagent scoping contracts, METRO's loop diagram — is exactly the content v2 needs, re-homed into verbs, playbooks, and worker contracts.
3. **Capability scoping already exists in the frontmatter tool grants** (read-only research vs. write/exec build), not in the persona prose. The v2 capability-worker model is latent in these files.
4. **The "Subagent Templates" sections are proto-worker contracts.** Every one uses the "Do not X — Y only" scope discipline the blueprint asks of self-contained worker contracts. They are the highest-value verbatim salvage: roughly 14 templates map onto the blueprint's seven worker types.
5. **No persona owns `decide` or `init`.** Gates are governed by rules files and escalation lines, not by any agent; the lifecycle spans overlap (STUDIO straddles HORIZON and DEVLAB) and the "collaborates_with" choreography exists to patch that. This supports the blueprint's core claim that lifecycle ownership is the wrong navigation axis — and `decide`, v2's "defining verb", is precisely the thing the persona model left homeless.
6. **Rule 06 (file-based cross-agent communication, "the ID cross-references ARE the communication") already anticipates v2** — it just names personas as its actors. It survives as the Change-plane/Change-Set discipline once persona names are rewritten out.
7. **domain-profile.yaml already marks the agent registry optional** ("Non-product repos may drop these entirely", line 156), so removing/replacing it with a worker or verb registry is a low-friction schema change.
8. **Net disposition: retire all four personas; convert none wholesale; keep the hook mechanism re-keyed to a single consumer-owned memory.** METRO's feedback loop and DEVLAB's tool asymmetry are the two places the old design already discovered pieces of v2 — worth citing in migration notes so the retirement reads as consolidation, not loss.