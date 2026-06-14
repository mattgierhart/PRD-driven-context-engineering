# Lessons from harness-forge — applied to PRD-CE

**Status**: v1.0 · 2026-06-14 · source: [`001TMF/harness-forge`](https://github.com/001TMF/harness-forge)

A study of the `harness-forge` repository and what it teaches us about our own
skills and methodology. This memo records the analysis; the highest-confidence
lessons have already been **landed as edits** (see [§4](#4-what-we-changed)).

---

## 1. What harness-forge is

`harness-forge` ships a single Claude Code skill, **meta-harness**, that
optimizes the *scaffolding* around a **frozen** language model — retrieval,
memory, context assembly, prompts, tool selection — rather than the model
weights. It runs a four-phase loop:

```
PROPOSE   k candidate harnesses (parallel proposer agents write code)
VALIDATE  cheap import/type-check rejection of broken candidates
SCORE     each on a held-out eval set with a $0 deterministic scorer
FRONTIER  Pareto-merge (quality up, cost down), respecting a quality floor
```

Its headline result (from the Meta-Harness paper it implements) is **+7.7
accuracy points at ~4× fewer context tokens** through harness-only
optimization. Its other notable claim is *native execution*: by using Claude
Code's `Agent`/`Workflow`/`parallel`/`/loop` primitives instead of a bespoke
Python driver, it collapses ~1,260 lines of orchestration Python to ~75.

We are **not** running a model search. So the value to us is not the loop — it
is the **evaluation discipline the loop is built to protect**, plus the
native-execution philosophy.

---

## 2. The mapping

| harness-forge concept | What it protects | Our analog | Verdict |
|---|---|---|---|
| **Frozen-replay defect** — *"can this number change for a quality reason if I swap the candidate, or only because cost moved?"* | Fake optimization where the proxy moves but real quality is locked | `readiness.py` score can rise from entry-count / cross-ref / self-rated-confidence padding without evidence rising | **Adopt now** |
| **Anti-Goodhart floor** — *minimize cost s.t. quality ≥ a do-no-harm floor*; never maximize a soft proxy | Optimizers gaming a soft metric | We implicitly treat readiness thresholds as targets to clear | **Adopt now** |
| **Proxy-fidelity gate** — validate the cheap proxy ranks like the true metric before trusting it | Trusting a proxy that doesn't track reality | Readiness is a proxy for "a product users react to," never checked against shipped outcomes | **Adopt now** (as discipline) |
| **Proposer prior + anti-leakage** — candidates may not hardcode eval values; must generalize | Evidence fabrication / overfitting the grader | Skills are *proposers* of SoT entries; nothing explicitly forbade back-filling confidence/evidence to clear a gate (Tier-5 REJECT was the only seed) | **Adopt now** |
| **Deterministic, $0, no-LLM scorer** — cheap enough to run hundreds of times, trustworthy because reproducible | A scorer you can actually loop on | `readiness.py` is *exactly* this already — no model calls | **Already strong — protect** |
| **Quality vs. cost Pareto frontier** — the product is the whole trade-off curve, not one point | Trade-off visibility | We score quality (readiness) but have no first-class **context-cost** axis — ironic for a *context-engineering* repo. EPIC `context_budget` exists but is never reported as a frontier | **Recommend (future)** |
| **Native execution** — platform primitives over a custom runtime; typed handshakes over file I/O; journaled/resumable parallel agents | Reimplementing runtime machinery | Cross-agent comms is deliberately file-based (durable, cross-session); but *within-session* multi-candidate work could use native `parallel` agents | **Recommend (future)** |
| **Runnable example** — `examples/memory-summary/` runs the whole loop at $0 | A demo that proves the method end-to-end | PRINCIPLES.md already *asks* for "trace a mock product through 3 skills" but no fixture exists | **Recommend (future)** |

---

## 3. What we already do well (honest credit)

The study is not just a gap list. Two of harness-forge's hardest-won design
principles are things this repo got right independently:

- **The scorer is already deterministic, $0, and LLM-free.** `readiness.py`
  makes no model calls; it parses SoT/EPIC/PRD structure and computes weighted
  dimensions. That is precisely the property harness-forge spends most of its
  guardrails defending — it's what makes a proxy cheap enough to trust and
  re-run. Our job is to *protect* this, not rebuild it.
- **The SoT-as-graph + confidence model is a strong "candidate interface."**
  IDs as stable nodes, cross-references as edges, and per-entry confidence
  (P4) give us a clean, inspectable boundary — the same role harness-forge's
  "candidate interface" plays. We didn't need to import this; we needed to
  name the discipline that keeps it honest.

---

## 4. What we changed

Landed in this pass (the "adopt now" rows):

- **`.claude/skills/PRINCIPLES.md`** — new **P7: Readiness is a Floor, Not a
  Target**, with the frozen-replay framing, the detection question, and a
  proxy-fidelity note. P4 gains an explicit **anti-leakage (proposer
  discipline)** paragraph forbidding fabricated/back-filled evidence. Quick-
  reference table and audit checklist extended with P7.
- **`.claude/rules/07-readiness-protocol.md`** — new **"Anti-Goodhart & Proxy
  Fidelity"** section operationalizing P7: the detection question; keep the
  scorer LLM-free; *quality floor, then cost* (don't clear a gate by ballooning
  `context_budget`); periodic proxy-checks.
- **`.claude/skills/SKILL_TEMPLATE/SKILL.md`** — every new skill now inherits a
  *"How this is evaluated"* pointer (output is scored by `readiness.py`; gaming
  inputs is a frozen-replay defect) and an **Evidence fabrication** anti-pattern
  row.

---

## 5. Recommended future work

Bigger ideas worth a dedicated EPIC, deliberately *not* built in this pass:

1. **Context-cost as a first-class axis.** We optimize readiness (quality) but
   never report context cost alongside it. Add a companion metric — tokens (or
   chars) of context an EPIC's spec set implies vs. the coverage it achieves —
   and surface the **Pareto frontier** (best readiness per context budget).
   `context_budget` in EPIC frontmatter is the natural input. This is the most
   thematically on-point lesson for a repo literally named *context
   engineering*.
2. **Native parallel-agent optimization.** When we generate or improve skills,
   spawn `k` candidate variants in parallel agents and score them against
   `readiness.py` (and the future cost axis), rather than serially by hand —
   harness-forge's Mode B, applied to our own artifacts.
3. **A runnable end-to-end example.** Build the fixture PRINCIPLES.md already
   calls for: a mock product traced v0.1 → v0.3 → v0.7, with SoT entries and a
   passing readiness report, under `tests/fixtures/`. Proves the methodology
   the way `examples/memory-summary/` proves meta-harness.
4. **Optional `ghm-skill-forge` meta-skill.** The full payoff: a skill that
   runs propose → score → Pareto-merge over our *own* skills/SoT, using
   `readiness.py` as the deterministic scorer and the context-cost axis from
   (1). This is the direct port of harness-forge into our methodology — but it
   only makes sense after (1) gives it a cost axis to optimize against.

---

## 6. See also

- [`.claude/skills/PRINCIPLES.md`](../.claude/skills/PRINCIPLES.md) — P4, **P7**
- [`.claude/rules/07-readiness-protocol.md`](../.claude/rules/07-readiness-protocol.md) — Anti-Goodhart & Proxy Fidelity
- [`docs/READINESS_PROTOCOL.md`](READINESS_PROTOCOL.md) — scorer schema
- [`docs/DEVELOPMENT_GRAPH.md`](DEVELOPMENT_GRAPH.md) — the as-built (code) layer
