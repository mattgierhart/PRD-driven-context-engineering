---
name: prd-v05-vibe-gate-interview
tier: core
description: >
  Interview the PM after v0.5 Red Team Review as a qualitative go/no-go gate before
  v0.6 Architecture. Pressure-tests framing, experience, riskiest assumption, cost/complexity
  honesty, and distribution readiness, then captures the decision via an interactive HTML
  decision sheet. Triggers on completing v0.5, or requests like "vibe check", "gut check
  before we build", "reality check", "are we ready for architecture?", "should we actually
  build this?". Complements ghm-gate-check (quantitative readiness) with a Vibe Verdict
  (GO / GO-WITH-CHECKS / PAUSE). Outputs RISK- updates, CFD- validation tasks, a PER-
  watering-hole note, and the verdict in PRD v0.5.
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

# Vibe Gate Interview (v0.5 → v0.6)

Qualitative gate interview run at the END of v0.5, after `prd-v05-risk-discovery-interview`
and `prd-v05-technical-stack-selection`, before advancing to v0.6 Architecture.

**Relationship to `ghm-gate-check`**: complements, never overrides. `readiness.py` answers
*"is the documentation ready?"* (quantitative). The vibe gate answers *"is the **PM** ready —
does this still deserve to be built as framed?"* (qualitative). Run both before the gate
decision; this skill's verdict never contradicts an honest readiness BLOCK.

**Mode shape** (per rule 08): **quick** = Phases 1, 2, 4, 6, 7 (~15 min "before I commit to
architecture" gut-check); **standard** = all seven phases; **deep** = standard + re-audit of
every CFD-/FEA- confidence score the verdict rests on, with downstream impact notes.

## Workflow Overview

1. Load context (all prior IDs) and reframe the product back to the PM.
2. Run the framing check, experience gut-checks, riskiest-assumption test, honesty pass,
   and distribution final boss — one question at a time.
3. Generate the HTML decision sheet into `temp/`, let the PM click their decisions.
4. Record the pasted decisions into PRD/SoT markdown (markdown stays authoritative).

## Interview Style (operating contract)

1. **One question at a time. Never stack.** Ask, wait, move on.
2. **Always offer your own answer.** For every question: *"here's what I'd suggest"* — so the
   PM can take it, tweak it, or argue.
3. **When they say "I don't know," decide for them.** Pick a sensible default, give a
   one-sentence reason, flag the resulting entry at confidence 1/5 for later revisit.
4. **Show the map before the walk.** Open with: *"This is a gut-check, not a second red-team.
   Seven short beats: framing, experience, your riskiest bet, honest cost, first ten users,
   then a verdict."*
5. **Read the confidence dial once.** One light question to gauge how battle-tested the PM's
   evidence is, then match pacing — don't re-derive v0.1–v0.5 with a PM who has Tier-1 evidence.
6. **Tone**: the friend who's shipped a few products, genuinely fired up. Patient, but doesn't
   waste time. Pushes back gently when scope balloons. Co-pilot, not a teacher at a whiteboard.

## Consumes

- From v0.1–v0.2: CFD- (evidence + tiers), BR- (positioning/targeting rules)
- From v0.3: FEA- (parity/delta), KPI- (thresholds), BR- (pricing)
- From v0.4: PER-, UJ- (value moments), SCR-
- From v0.5: RISK- register (scores + mitigations), TECH- (stack decisions)

## Phases

### Phase 1 — Context Load *(all modes)*

Read the consumed IDs. Build a one-paragraph restatement of the product as currently framed
and get the PM's "yes, that's it" before proceeding. Reframe their idea back to them —
sharper and clearer — and ask if you got it right.

### Phase 2 — Framing Check *(all modes)*

A quick honesty pass over how the product is framed. Name anything off:

- **Solution-first?** "Did this start from 'I want to build X' instead of a real problem?"
  (Check against v0.1 CFD- evidence.)
- **Outcome mismatch?** "Will this actually move the v0.1 goal?" (Check FEA- ↔ KPI- traceability.)
- **Mostly guesses?** If the majority of load-bearing CFD-/FEA- entries sit at confidence
  1–2/5, that's a *"validate before building"* sign — feed Phase 4.
- **Solution dressed as need?** "Did any 'need' actually name a feature?" (*"I can't tell
  which listings sold"* is a need. *"Add a sold-badge feature"* is a solution pretending to be one.)

**If none apply, say so plainly.** A clean framing check is a finding, not a formality.

### Phase 3 — Experience Gut-Checks *(standard+)*

Three named, repeatable tests against UJ-/SCR- entries (questions in
`references/question-bank.md`):

- **The Grandma Test** — could the least techy user do everything unaided? If not, what
  must get simpler?
- **The Stress Test** — walk the most stressed, distracted user through the core journey.
  Where does it fall apart? Failures route to UJ- pain points or new RISK- entries.
- **Aha-Moment Timing** — what's the single moment it first feels worth it, and how fast
  after signup? Aim for the first 30 seconds; design backward, strip blockers. If the
  relevant UJ- has no value moment inside the first session, flag it.

### Phase 4 — Riskiest-Assumption Test *(all modes)*

- Name **the single belief that sinks the whole thing if wrong** — usually *"people want
  this enough to switch."* Force exactly one; a tie means the PM hasn't decided.
- Find the **cheapest way to check it BEFORE building**: landing page with waitlist, ten DMs
  to people with the problem, fake-door button, rough mock shown to five people.
- The rule: **"if the test takes two weeks to set up, it's a project, not a test."**
- Output: one RISK- entry (owner = PM) + one CFD- validation-task entry per cheap check,
  each with a date.

### Phase 5 — Honesty Pass *(standard+)*

- **Complexity score 1–10 with anchors**: "a to-do list is a 2, Instagram's a 9" — score
  against TECH-/ARC- scope and say what the number means.
- **Cost sanity** including the architecture-cost trap: how the stack is *used* matters as
  much as its sticker price (polling a database every 30 s vs. event webhooks can be the
  difference between $480/month and free). Flag any TECH- entry with an unexamined
  usage-pattern cost.
- **Honest timeline** in phases, not a single date.
- **Learning or real users?** The answer changes how much to sweat quality, testing, and
  legal before v0.6.

### Phase 6 — Distribution Final Boss *(all modes)*

Force specific answers, not vague ones:

- **"Who are your first 10 users, specifically?"** Not a demographic — ten real people or
  one real place nameable today. "The folks in r/[subreddit] who keep ranting about X"
  counts. "Small business owners" does not.
- **"Where do they already gather?"** The single place they're having this problem out loud
  (usually the community mined for pain in v0.1).
- **"What's your first move to reach them?"** One concrete action.

Say the blunt gut-check out loud: *"If you can't name where the first ten users come from,
that isn't a distribution problem for later — it's the riskiest part of this whole thing."*
If unanswered, it becomes a RISK- entry and weighs the verdict.

Output: a watering-hole / first-10 note appended to the primary PER- entry (consumed later
by v0.9 ORB channel allocation).

### Phase 7 — Verdict & Outputs *(all modes)*

| Verdict | Meaning | Required attachments |
|---|---|---|
| **GO** | Framing clean, riskiest assumption checked or scheduled, first-10 named | — |
| **GO-WITH-CHECKS** | Build may proceed; named cheap checks run in parallel | CFD- validation tasks with dates |
| **PAUSE** | A framing failure or unchecked sink-the-ship assumption | Concrete unblock condition per blocker |

**7a. Generate the decision sheet.** Copy `assets/decision-sheet-template.html` to
`temp/v05-vibe-gate_<YYYY-MM-DD>.html` and fill every `{PLACEHOLDER}` with this session's
actual candidates: your verdict lean + one-line rationale, the riskiest-assumption statement,
the cheap-check options surfaced in Phase 4, the first-10/watering-hole draft from Phase 6,
the complexity/cost lines from Phase 5, and the evidence ID chips (CFD-/RISK-/UJ-/TECH-).
Tell the PM: *"Open this file in your browser, click your decisions, then hit 'Copy my
decisions' and paste the block back to me."* The sheet is an input device — it lives in
`temp/` and is disposable after harvest (temp/ rule 3).

**7b. Record.** Parse the pasted decision block (it matches `assets/vibe-verdict.md`):
- Write the RISK- entry for the riskiest assumption (use the v0.5 RISK- template,
  `Added: v0.5`, owner = PM) and any Stress-Test/distribution failures.
- Write one CFD- validation-task entry per selected cheap check (confidence 1/5 until run).
- Append the watering-hole / first-10 note to the primary PER- entry.
- Write the **Vibe Verdict + rationale** into PRD v0.5 **"Outstanding Work → v0.6"**, next
  to the `ghm-gate-check` readiness score. The two travel together to the gate decision.

Markdown is authoritative; the HTML sheet is never the system of record.

## Produces

- RISK- — riskiest assumption (owner = PM) + gut-check failures (existing v0.5 template)
- CFD- — one validation-task entry per cheap check (confidence 1/5 until run)
- PER- update — watering-hole / first-10 note on the primary persona
- PRD v0.5 "Outstanding Work → v0.6" — Vibe Verdict + rationale
- No new ID prefix — the verdict lives in PRD prose; everything durable lands in existing prefixes

## Quality Gates

- [ ] Riskiest assumption is named (exactly one) and its cheap check is scheduled with a date
- [ ] First-10 list is specific (people or a place), or its absence is logged as a RISK-
- [ ] Every PAUSE has a concrete unblock condition
- [ ] Verdict never contradicts an honest readiness BLOCK from `ghm-gate-check`
- [ ] Framing Check result stated plainly — including when clean
- [ ] Decision sheet decisions are recorded in markdown before the session ends

## Anti-Patterns

| Pattern | Example | Fix |
|---|---|---|
| Second red-team | Re-deriving the v0.5 risk register question by question | Consume RISK-; this skill gut-checks the PM, not the register |
| Verdict theater | Every run ends GO | A clean run states *why* each phase passed, citing IDs |
| "Distribution is marketing's job" | Deferring first-10 to v0.9 | The final boss runs here; v0.9 inherits the named community |
| Interview becomes lecture | Explaining frameworks instead of asking | One question at a time; offer a default; move on |
| Stacked questions | Three questions in one message | Never stack — ask, wait, move on |
| HTML as system of record | Verdict only exists in the sheet | Phase 7b writes markdown before the session ends |

## Bundled Resources

- `references/question-bank.md` — phase-organized verbatim questions
- `assets/vibe-verdict.md` — verdict block + checks table template (the markdown that lands in PRD)
- `assets/decision-sheet-template.html` — self-contained interactive decision sheet (copied to `temp/`, placeholders filled per session)

## Handoff

- **GO / GO-WITH-CHECKS** → `prd-v06-architecture-design` (checks run in parallel; results update CFD-).
- **PAUSE** → route to the unblock condition (usually back to `prd-v01`/`prd-v02` research or
  a cheap-check sprint), then re-run this skill in quick mode.
