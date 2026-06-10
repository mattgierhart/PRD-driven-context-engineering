# Methodology Modernization Assessment — Standard Prompt

Run this prompt with an agent (e.g., Claude Code) **inside a repository that uses the PRD-CE
methodology**, when you want to assess how far it has drifted from the latest version of
PRD-Led Context Engineering and produce a modernization plan.

Prerequisites:

- A local clone of the latest methodology at `~/Documents/MLG.Github/PRD-driven-context-engineering/`
  (adjust the `REFERENCE` path in the prompt if yours lives elsewhere).
- Run from the root of the downstream repo.

The prompt is assessment-only by design: it stops at a written report and a proposed EPIC.
Applying the changes is a separate, human-triaged session — consistent with the lifecycle-gate
discipline.

---

```
You are auditing this repository's implementation of the PRD-Led Context Engineering (PRD-CE)
methodology against the latest reference version, and producing a modernization assessment.

REFERENCE (latest methodology): ~/Documents/MLG.Github/PRD-driven-context-engineering/
TARGET (this repo): the current working directory.

Two rules govern everything below:

1. ASSESSMENT ONLY. You will write a report and propose an EPIC. Do not modify any file other
   than the report itself. Modernization is executed later, through this repo's own gate process.
2. DELIBERATE DIVERGENCE IS LEGITIMATE. Repos consciously depart from the methodology for good
   reasons. Your job is to tell drift (unintentional lag) apart from divergence (a documented or
   reconstructable choice) — and to recommend preserving the latter, not "fixing" it.

## Phase 0 — Build the reference snapshot

Read from REFERENCE (markdown only — ignore SoT/html/*.html, they are human-review renders):
- README.md ("What's in the box", lifecycle table, quick start) — the current feature surface
- CLAUDE.md and .claude/rules/*.md — current operating rules (note each rule file's name)
- .claude/domain-profile.yaml and SoT/SoT.UNIQUE_ID_SYSTEM.md — current ID registry
- .claude/skills/ — list skill names only (don't read bodies): the prd-v* and ghm-* inventory
- .claude/hooks/HOOK_CONTRACT.md — hook surface
- SoT/ — the template file set and each file's frontmatter (version, template_version)
- scripts/readiness.py existence + docs/READINESS_PROTOCOL.md + docs/DEVELOPMENT_GRAPH.md
- SoT/html/README.md — the human-review companion layer contract
- epics/EPIC_TEMPLATE.md and PRD.md template (version headers, section structure)

Produce a concise feature inventory of the CURRENT methodology, derived from these files (do not
rely on memory or training data — the reference clone is the truth). Group it: documents &
templates / rules / skills / hooks & agents / scoring & tooling / human-review layer.

## Phase 1 — Archaeology of this repo

Establish what this repo adopted, when, and what happened since:
- git log --oneline --reverse | head -50 and git log --oneline | head -80 — fork era and recency
- The PRD.md "Lifecycle Change Log" table and current gate; README status sections
- epics/ — completed and active EPICs; their Session State and Agent Observations tables
- Past PRs if available (gh pr list --state merged --limit 50, or merge commits otherwise) —
  scan titles/descriptions for methodology-related changes
- temp/ leftovers, SoT/SoT.LESSONS_LEARNED.md, agent MEMORY.md files — places where
  methodology friction gets recorded
- The same surfaces as Phase 0, but local: which rules exist, which skills exist, which SoT
  files exist, frontmatter versions, whether readiness/devgraph/html-companion are present

Estimate the fork point: which generation of PRD-CE does this repo's scaffolding resemble?

## Phase 2 — Gap matrix

For every feature in the Phase 0 inventory, mark this repo's state:
- PRESENT-CURRENT (matches reference)
- PRESENT-MODIFIED (exists, but altered locally — note how)
- PRESENT-DECAYED (exists but visibly unmaintained: stale timestamps, empty sections,
  references to files that no longer exist)
- ABSENT (never adopted, or removed)

## Phase 3 — Deviation register (the heart of this assessment)

For every PRESENT-MODIFIED, PRESENT-DECAYED, and ABSENT-by-removal item, classify:

a) DRIFT — no evidence of a decision; the repo simply lagged or decayed.
b) DELIBERATE DIVERGENCE — you found rationale. Look for it in: TECH-/ARC- entries, LL- lessons,
   RISK- entries, EPIC Agent Observations, PR descriptions, commit messages, CLAUDE.md edits,
   or comments near the modified scaffolding. Cite the exact source (file + ID or commit hash)
   and quote the rationale in one line.
c) UNEXPLAINED DIVERGENCE — clearly intentional-looking (e.g., a renamed ID prefix used
   consistently) but no recorded rationale. Do NOT classify these as drift; flag them as
   questions for the maintainer.

For each DELIBERATE divergence, state what the modernization plan must do to RESPECT it (e.g.,
"skip rule 08 import; this repo runs single-mode skills by ARC-014"). If the rationale exists
only in a PR or commit, recommend promoting it to a durable LL- or ARC- entry so the next
assessment finds it without archaeology.

## Phase 4 — Modernization plan

A prioritized, sequenced plan to bring the scaffolding current while preserving all product
knowledge and all deliberate divergences:
- Order by leverage: items that unblock other items first (ID registry and rules before skills;
  readiness before gate-check workflows; SoT templates before the html companion layer).
- For each item: concrete file operations (copy from REFERENCE path X to local path Y; merge,
  don't overwrite, where local content exists), effort (S/M/L), and risk notes.
- HARD CONSTRAINTS: never overwrite product content — SoT entries, PRD sections, EPICs, and
  LESSONS are knowledge, not scaffolding. IDs are never renumbered. Where a template gained
  sections, additions are appended; existing entries are not reformatted in this pass.
- Group into 1-3 proposed EPICs sized to context windows, each with objective, scoped IDs,
  and a definition of done.

## Phase 5 — Report

Write the full assessment to temp/methodology-modernization-assessment.md (associate it with
the EPIC if one is active, per the temp/ naming convention), structured as:
1. Maturity snapshot — fork era, current gate, scaffolding generation, three-sentence verdict
2. Gap matrix (table)
3. Deviation register (table: item, classification, rationale + citation, plan's obligation)
4. Modernization plan (sequenced, with the proposed EPIC blocks)
5. Open questions for the maintainer (every UNEXPLAINED divergence goes here)

Then summarize the verdict and the top 5 actions in chat, and STOP. Do not begin modernizing.
```

---

## Notes for the operator

- **Why assessment-only**: downstream repos are at different gates; applying scaffolding changes
  without the repo's own EPIC/gate process would violate the methodology being installed.
- **Why the reference is read fresh** (Phase 0): the feature inventory is derived from the local
  clone, not hardcoded into this prompt — so the prompt stays valid as PRD-CE evolves. Keep the
  reference clone pulled to latest before running.
- **The deviation register is the deliverable that matters.** A repo with ten respected,
  documented divergences is healthier than one with two silent ones.
