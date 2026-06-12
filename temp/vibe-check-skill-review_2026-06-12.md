---
title: "Vibe-Check Skill Review — Comparative Audit + Vibe-Gate Skill Spec"
scope: ".claude/skills/ (methodology audit, not stage work)"
updated: "2026-06-12"
---

# Vibe-Check Skill Review

> **Purpose**: Comparative audit of [TexasBedouin/vibe-check](https://github.com/TexasBedouin/vibe-check)
> against our skill library, with a triage-ready recommendation set. The headline recommendation is a
> **new post-v0.5 qualitative gate skill** (`prd-v05-vibe-gate-interview`), specced in full in §3 so it
> can be lifted into `.claude/skills/` once triaged.
>
> **Status**: All recommendations are `Triage: Pending`. No skill files were modified in this pass.
> **Harvest rule**: When triage completes, extract adopted items to the named target files and delete this doc.

---

## 1. Source Summary

**What it is**: `vibe-check` v1.6.0 — a single Claude Code skill by a 12-year PM (0→1 specialist),
positioned as *"grill-me is for engineers. vibe-check is for everyone else."* It turns a complete
beginner's app idea into a buildable plan, then keeps them oriented while they build.

**Shape of the repo**:

| Artifact | Notes |
|---|---|
| `SKILL.md` | One large skill: 2 modes (Planning default, Checkup for messy codebases), Phase 0–8 workflow |
| `references/` (7 files) | `DISCOVERY-DEEP-DIVE`, `MANAGING-YOUR-AI`, `CODE-CHECKUP`, `GITHUB-AND-DEPLOYMENT`, `KEEPING-CODE-NAVIGABLE`, `HTML-BLUEPRINT`, `WHAT-A-SKILL-ACTUALLY-IS` — loaded just-in-time, "pull in when the moment calls for it" |
| `VERSION` + `CHANGELOG.md` + `bump.sh` + `RELEASING.md` | The skill itself is semantically versioned; skill checks GitHub for a newer version at session start (mention once, never block) |

**Workflow**: Phase 0 Discovery (grill the user, then reality-check against Reddit/competitor evidence)
→ 1 The Dream → 2 The Experience (Crazy-3s, flows, aha moment) → 3 Connections → 4 Decisions →
5 Blueprint → 6 Reality Check → 6.5 Distribution ("The Final Boss") → 7 "Stuff They Don't Know About"
→ 8 Plan Document (markdown plan + self-contained HTML blueprint, build phases with checkpoint blocks).

**Methodology lineage**: Jobs-to-be-Done (Moesta), Outcome-Driven Innovation (Ulwick — simplified:
*"directional, not statistical… a strong hypothesis built from public evidence, not proof"*),
Continuous Discovery (Torres), GV Design Sprints, and Karpathy/FrontierCode-style AI supervision
*"translated for beginners"*.

**Where each library is stronger**:

- **Ours**: evidence discipline — 5-tier evidence hierarchy, 1–5 confidence scoring with sources,
  mandatory Consumes/Produces, measurable quality gates, anti-pattern tables, the ID knowledge graph,
  readiness scoring.
- **Theirs**: conversational mechanics and reality-checking the *human* — pacing rules, offered
  defaults, named gut-checks, checkpoint rituals, and a blunt pre-build honesty pass that our
  lifecycle currently has no home for.

---

## 2. What We Already Do As Well or Better (do not relitigate)

| Vibe-check element | Our equivalent | Verdict |
|---|---|---|
| Differentiator vs. table stakes V1 split | Parity/delta features in `prd-v03-features-value-planning` | Covered |
| Visual HTML blueprint deliverable | `SoT/html/` human review layer (richer: per-ID-type views, hyperlinked graph) | Covered |
| "House Rules for Your AI" template | `CLAUDE.md` + `.claude/rules/01–08` (more granular, hook-enforced) | Covered |
| JTBD job-steps → friction mapping | UJ- step flows with pain points + value moments | Covered |
| Evidence tags "seen it / hunch / guess" | 5-tier evidence hierarchy + 1–5 confidence with sources (finer-grained) | Covered — though the 3-word labels are a nice *quick-mode* shorthand |
| "Honest rigor" caveat on proxy research | P3 (Research Drives Scope) + P4 (SoT is Living Evidence) | Covered |
| Just-in-time reference loading | Our `references/` + `assets/` bundling convention | Covered |
| Build-phase sequencing | `prd-v07-epic-scoping` (context-window sizing is stronger) | Covered |

---

## 3. HEADLINE — Draft Spec: `prd-v05-vibe-gate-interview`

> **Origin insight** (Matt): several vibe-check findings — Reality Check (Phase 6) and Distribution
> (Phase 6.5) — don't belong scattered across existing skills. They cluster into **one skill that
> interviews the PM after v0.5 as a vibe gate**.
>
> **Relationship to `ghm-gate-check`**: complements, never overrides. `readiness.py` answers
> *"is the documentation ready?"* (quantitative). The vibe gate answers *"is the **PM** ready — does
> this still deserve to be built as framed?"* (qualitative). Run both before advancing to v0.6.

Everything below is lift-ready: copy into `.claude/skills/prd-v05-vibe-gate-interview/SKILL.md`,
then register in `skills/README.md`, `skills-inventory.md`, and `domain-profile.yaml` if adopted.

### 3.1 Frontmatter (draft)

```yaml
---
name: prd-v05-vibe-gate-interview
description: >
  Interview the PM after v0.5 Red Team Review as a qualitative go/no-go gate before
  v0.6 Architecture. Pressure-tests framing, experience, riskiest assumption, cost/complexity
  honesty, and distribution readiness. Triggers on completing v0.5, or requests like
  "vibe check", "gut check before we build", "reality check", "are we ready for architecture?",
  "should we actually build this?". Complements ghm-gate-check (quantitative readiness) with a
  Vibe Verdict (GO / GO-WITH-CHECKS / PAUSE). Outputs RISK- updates, CFD- validation tasks,
  and PRD v0.5 Outstanding Work updates.
context: fork
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
execution_modes:
  default: standard
  supports: [quick, standard, deep]
---
```

Mode shape (per rule 08): **quick** = Framing Check + Riskiest-Assumption + verdict (~15 min, the
"before I commit to architecture" gut-check); **standard** = all seven phases; **deep** = standard +
evidence re-audit of every claim the verdict rests on, with downstream impact notes.

### 3.2 Interview Style (vibe-check's conversational protocol, baked in)

These rules are the skill's operating contract — quoted nearly verbatim from vibe-check because the
phrasing is the detail worth stealing:

1. **One question at a time. Never stack.** Ask, wait, move on.
2. **Always offer your own answer.** For every question: *"here's what I'd suggest"* — so the PM can
   take it, tweak it, or argue. (Beginners and busy founders need direction, not fifteen equal options.)
3. **When they say "I don't know," decide for them.** Pick a sensible default, give a one-sentence
   reason, flag it for later revisit (tag the resulting entry confidence 1/5).
4. **Show the map before the walk.** Open with: *"This is a gut-check, not a second red-team. Seven
   short beats: framing, experience, your riskiest bet, honest cost, first ten users, then a verdict."*
5. **Read the confidence dial once.** One light question to gauge how battle-tested the PM's evidence
   is, then match pacing — don't re-derive v0.1–v0.5 with a PM who has Tier-1 evidence.
6. **Tone**: the friend who's shipped a few products, genuinely fired up. Patient, but doesn't waste
   time. Pushes back gently when scope balloons. *"Co-pilot, not a teacher at a whiteboard."*

### 3.3 Consumes

- From v0.1–v0.2: CFD- (evidence + tiers), BR- (positioning/targeting rules)
- From v0.3: FEA- (parity/delta), KPI- (thresholds), BR- (pricing)
- From v0.4: PER-, UJ- (value moments), SCR-
- From v0.5: RISK- register (scores + mitigations), TECH- (stack decisions)

### 3.4 Phases

**Phase 1 — Context Load** *(all modes)*
Read the consumed IDs. Build a one-paragraph restatement of the product as currently framed and get
the PM's "yes, that's it" before proceeding. (Vibe-check rule 6: *"Reframe their idea back to them."*)

**Phase 2 — Framing Check** *(all modes)*
A quick honesty pass over how the product is framed. Name anything off:

- **Solution-first?** *"Did this start from 'I want to build X' instead of a real problem?"* (Check
  against v0.1 CFD- evidence.)
- **Outcome mismatch?** *"Will this actually move the v0.1 goal?"* (Check FEA- ↔ KPI- traceability.)
- **Mostly guesses?** If the majority of load-bearing CFD-/FEA- entries sit at confidence 1–2/5,
  that's a *"validate before building"* sign — feed Phase 4.
- **Solution dressed as need?** *"Did any 'need' actually name a feature?"* (Vibe-check: *"'I can't
  tell which listings sold' is a need. 'Add a sold-badge feature' is a solution pretending to be a need."*)

Vibe-check's closer applies: **"If none apply, say so plainly."** A clean framing check is a finding,
not a formality.

**Phase 3 — Experience Gut-Checks** *(standard+)*
Three named, repeatable tests against UJ-/SCR- entries:

- **The Grandma Test**: *"Who's the least techy person who'd ever use this? Could THEY do everything
  we just described with nobody helping? If not, what has to get simpler?"*
- **The Stress Test**: *"Picture your user at their most stressed, most distracted. Low battery. Bad
  signal. Kid screaming. Running late. Walk me through them trying to use your app in THAT moment.
  Where does it fall apart?"* → failures route to UJ- pain points or new RISK- entries.
- **Aha-Moment Timing**: *"What's the single moment a user first feels this was worth it?"* and
  *"How fast can they get there after signing up? Aim for the first 30 seconds."* Design backward:
  strip every blocker between signup and value. If the relevant UJ- has no value moment inside the
  first session, flag it.

**Phase 4 — Riskiest-Assumption Test** *(all modes)*
- Name **the single belief that sinks the whole thing if wrong** — usually *"people want this enough
  to switch."* Force one; a tie means the PM hasn't decided.
- Find the **cheapest way to check it BEFORE building**: landing page with waitlist, ten DMs to people
  with the problem, fake-door button, rough mock shown to five people.
- The rule, verbatim: *"if the test takes two weeks to set up, it's a project, not a test."*
- Output: one RISK- entry (owner = PM) + one CFD- validation-task entry per cheap check, with a date.

**Phase 5 — Honesty Pass** *(standard+)*
- **Complexity score 1–10 with anchors**: *"This is about a 6. A to-do list is a 2, Instagram's a 9.
  You're building something real, and it's still doable."* (Score against TECH-/ARC- scope.)
- **Cost sanity** including the architecture-cost trap: *"Service prices matter. But HOW your app uses
  them matters just as much. Checking the database every 30 seconds for new messages: $480/month at
  100 users. Getting pinged only when a message lands: basically free."* → flag any TECH- entry with
  an unexamined usage-pattern cost.
- **Honest timeline** in phases, not a single date.
- **Learning or real users?** Changes how much to sweat quality, testing, and legal before v0.6.

**Phase 6 — Distribution Final Boss** *(all modes)*
Force specific answers, not vague ones:

- *"**Who are your first 10 users, specifically?** Not a demographic. Ten real people or one real
  place you could name today. 'The folks in r/[subreddit] who keep ranting about X' counts. 'Small
  business owners' does not."*
- *"**Where do they already gather?** The single place they're hanging out having this problem out loud."*
  (Usually the exact community mined for pain in v0.1.)
- *"**What's your first move to reach them?** One concrete action."*

The blunt gut-check, said out loud: *"If you can't name where the first ten users come from, that
isn't a distribution problem for later. It's the riskiest part of this whole thing, and it deserves
more attention than another feature."* → if unanswered, it becomes a RISK- entry and weighs the verdict.

Output: a watering-hole/first-10 note appended to the primary PER- entry (consumed later by v0.9 ORB
channel allocation — Owned/Rented/Borrowed starts from a named Borrowed community).

**Phase 7 — Verdict & Outputs** *(all modes)*

| Verdict | Meaning | Required attachments |
|---|---|---|
| **GO** | Framing clean, riskiest assumption checked or scheduled, first-10 named | — |
| **GO-WITH-CHECKS** | Build may proceed but named cheap checks run in parallel | CFD- validation tasks with dates |
| **PAUSE** | A framing failure or unchecked sink-the-ship assumption | Concrete unblock condition per blocker |

Record the verdict + one-line rationale in PRD v0.5 **"Outstanding Work → v0.6"**, next to the
`ghm-gate-check` readiness score. The two travel together to the gate decision.

### 3.5 Produces

- RISK- — the riskiest assumption (owner = PM) + any Stress-Test/distribution failures (use existing
  v0.5 template; `Added: v0.5`)
- CFD- — one validation-task entry per cheap check (confidence 1/5 until run)
- PER- update — watering-hole/first-10 note on the primary persona
- PRD v0.5 "Outstanding Work → v0.6" — Vibe Verdict + rationale
- No new ID prefix needed — the verdict lives in PRD prose; everything durable lands in existing prefixes

### 3.6 Quality Gates

- [ ] Riskiest assumption is named (exactly one) and its cheap check is scheduled with a date
- [ ] First-10 list is specific (people or a place), or its absence is logged as a RISK-
- [ ] Every PAUSE has a concrete unblock condition
- [ ] Verdict never contradicts an honest readiness BLOCK from `ghm-gate-check`
- [ ] Framing Check result stated plainly — including when clean

### 3.7 Anti-Patterns

| Pattern | Example | Fix |
|---|---|---|
| Second red-team | Re-deriving the v0.5 risk register question by question | Consume RISK-; this skill gut-checks the PM, not the register |
| Verdict theater | Every run ends GO | A clean run states *why* each phase passed, citing IDs |
| "Distribution is marketing's job" | Deferring first-10 to v0.9 | The final boss runs here; v0.9 inherits the named community |
| Interview becomes lecture | Explaining frameworks instead of asking | One question at a time; offer a default; move on |
| Stacked questions | Three questions in one message | Vibe-check rule 1: never stack |

### 3.8 Bundled Resources (create with the skill)

- `references/question-bank.md` — phase-organized verbatim questions (seed from quotes above)
- `assets/vibe-verdict.md` — verdict block + checks-table template for the PRD

### 3.9 Handoff

GO / GO-WITH-CHECKS → `prd-v06-architecture-design` (checks run in parallel; results update CFD-).
PAUSE → route to the unblock condition (usually back to `prd-v01`/`prd-v02` research or a cheap-check
sprint), then re-run quick mode.

---

## 4. Remaining Per-Skill Recommendations (not absorbed by the vibe gate)

| # | Observation (from vibe-check) | Proposed Action | Target file(s) | Effort | Triage |
|---|---|---|---|---|---|
| 1 | Conversational protocol: "One question at a time. Never stack." / "Always offer your own answer" / "When they say 'I don't know,' decide for them" / "Show the map before the walk" / confidence-dial pacing | Promote to a library-wide principle (P7 "Interview Like a Co-pilot") + audit-checklist item; interview-style skills (risk-discovery, mom-test, continuous-discovery) reference it | `.claude/skills/PRINCIPLES.md` | S | Pending |
| 2 | Checkpoint block ritual: per-phase STOP — 📍 WHERE WE ARE / 🔧 WHAT WE JUST BUILT / 💡 WHY WE BUILT IT THIS WAY / 📋 WHAT'S NEXT / ❓ QUESTIONS, **wait for user response**; "always loop back to WHY (point at the specific thing they said earlier)"; "show it, don't just say it" | Add a checkpoint-block template to the implementation loop, aligned with EPIC Session State updates (rule 01) — the explain-back ritual is what we lack | `prd-v07-implementation-loop/SKILL.md` (+ `assets/checkpoint-block.md`) | M | Pending |
| 3 | Per-change Definition of Done + supervised loop (from `MANAGING-YOUR-AI.md`): fail-first test rule ("a test passing on both broken and fixed code proves nothing"); "change only what I asked"; snapshot → ONE small change → prove ("Don't tell me it's fixed. Show me.") → keep-or-undo; "working is the floor, not the bar"; stall redirect ("Stop. Explain, in plain language, WHY this isn't working… then suggest a different approach before we touch any more code") | Fold the 5-item DoD and the supervised loop into the implementation loop; complements rule 04 traceability | `prd-v07-implementation-loop/SKILL.md`, cross-ref `.claude/rules/04-coding-standards.md` | M | Pending |
| 4 | Opportunity scoring + competitor gap matrix (from `DISCOVERY-DEEP-DIVE.md`, beginner-ODI): needs × solutions matrix (does well / poorly / doesn't — include non-tools like spreadsheets and "I just don't bother"); **`Opportunity = Pain + (Pain − Served)`** with Pain from community signal and Served from reviews; decisive rule: *"significantly better on a need people actually feel, or it's not worth building"*; flat scores across needs = segment too broad | Add the matrix + formula as a scoring option in the landscape skill; output feeds v0.3 parity/delta directly | `prd-v02-competitive-landscape-mapping/` (references) | M | Pending |
| 5 | Failure-path journey flows: alongside the happy path, a **"Rough Day" flow** (login fails, data won't load, payment bounces, AI gives a dumb suggestion) and an **"Edge Cases" flow** (power user with 500 items, person returning after 3 months, two connected apps disagreeing) — as Mermaid diagrams | Extend UJ- output template: each core journey gets happy + rough-day flows; edge-case flow in deep mode; Mermaid encouraged in SoT entries | `prd-v04-user-journey-mapping/SKILL.md` (+ assets template) | M | Pending |
| 6 | Reddit pain-mining playbook: `site:reddit.com` search; struggle phrases (*"[tool] is…", "How do I deal with…", "Tired of…", "Does anyone else…", "I gave up and just…"*); signal weighting (hundreds of upvotes, "me too" piles, same complaint resurfacing monthly = real demand); money gut-check (paid products exist? freelancers hired? ads on these keywords?); "future press release" stall-breaker; opening router question (*"real research, talked to people, or still mostly your hunch?"*) | Add a pain-mining section to the research prompts reference; router question as the skill's opener | `prd-v01-problem-framing/references/research-prompts.md` | S | Pending |

---

## 5. Repo-Level Observations (note only — no action proposed this pass)

- **Skill versioning**: vibe-check ships `VERSION` + `CHANGELOG.md` + `bump.sh` + a session-start
  version check (*"mention newer version once if found, never block"*). Irrelevant for fork-native use,
  but directly relevant when our 47 skills ship as a **Claude Code plugin** (README roadmap) — adopters
  will need to know which skill version they run and what changed.
- **Explicit Tone section**: vibe-check ends SKILL.md with a standalone `## Tone` block. Our template
  encodes tone implicitly via design principles. A short optional Tone section in `SKILL_TEMPLATE`
  would standardize voice across interview-style skills.
- **Expectation-setting reference**: `WHAT-A-SKILL-ACTUALLY-IS.md` corrects beginners' mental model of
  AI skills before planning one. Niche, but a good pattern: *correct the user's model of the medium
  before specifying work in it.*

---

## 6. Suggested Next Steps

1. Triage §4 table + §3 spec (mark each row Adopt / Adapt / Reject).
2. If §3 survives triage: lift into `.claude/skills/prd-v05-vibe-gate-interview/` (SKILL.md +
   `references/question-bank.md` + `assets/vibe-verdict.md`); register in `skills/README.md`,
   `skills-inventory.md`, and `.claude/domain-profile.yaml`; add the vibe gate to the v0.5→v0.6 gate
   ritual next to `ghm-gate-check` in README/PRD gate docs.
3. Apply adopted §4 items in order of effort (S first: #1, #6).
4. Harvest: delete this temp file once all rows are resolved (temp/README rule 3).
