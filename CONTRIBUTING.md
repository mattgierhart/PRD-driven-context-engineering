# Contributing to PRD-Led Context Engineering

Thank you for helping refine **PRD-Led Context Engineering**. This repository is not just a codebase; it
is a living system of **Memory as Infrastructure** — and it runs the method on itself.

## Core philosophy

Before contributing, read, in this order:

1. [`CLAUDE.md`](CLAUDE.md) — agent operating instructions and documentation discipline.
2. [`README.md`](README.md) — the methodology, navigation, and current status.
3. [`PRD.md`](PRD.md) — this repository's product authority and lifecycle authorization.
4. Accepted [`SoT/`](SoT/SoT.README.md) records — durable detail referenced by the PRD.

The goal is always **context density**: exactly the right information, at exactly the right time, for
humans and AI alike. If it isn't part of the memory infrastructure, it isn't true.

## Ways to contribute

**Refine the methodology**

- **Templates** — improve `SoT_template/`, its [HTML review layer](SoT_template/html/README.md),
  `PRD_template.md`, `README_template.md`, or the manifest's `*.seed.*` sources — without copying this
  repository's own product decisions into them (the seeds stay generic; see
  [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)).
- **Skills & workflows** — sharpen a stage skill (`.claude/skills/prd-v*`), a methodology operator
  (`ghm-*`), a hook, or the readiness scorer. Every skill emits `Consumes` / `Produces` sections; keep them
  connected.
- **Documentation** — clarify the rules of the road in `README.md`, `docs/`, or the rules under
  `.claude/rules/`.

**Report friction**

- A [lifecycle gate](README.md#-feature-the-progressive-prd) that slows you down without adding value?
  Open an issue.
- The AI struggling to find context? Report it as a **Context Leak** (there is an issue form for it).

## Getting started

1. **Fork & branch** for your feature or fix.
2. **Follow the lifecycle** — even meta-changes respect the spirit of the gated workflow; durable new
   concepts get an ID (`BR-XXX`, `UJ-XXX`, `LL-XXX`) in `SoT/` *before or during* the change, never after.
3. **Run the checks** before opening a PR:

   ```bash
   python3 -m pip install -r scripts/requirements.txt
   python3 -m pytest tests/ -q                 # readiness, graph-contract, and distribution tests
   bash scripts/package-plugin.sh              # if you changed anything under .claude/ or a seeded file…
   bash scripts/check-plugin-sync.sh           # …the generated plugin payload must be regenerated and committed
   ```

   CI runs the same three things (tests + readiness smoke, plugin sync, markdown link check on changed files).
4. **Open the PR** with the template — say which IDs you touched, whether SoT was updated, and whether the
   plugin payload was regenerated.

## Contribution standards

- **Terminology**: "PRD-Led Context Engineering", "Source of Truth", and "EPICs", consistent with the README.
- **Links**: relative links to files (e.g. `[Link](README.md)`), never absolute paths; no machine-local paths anywhere.
- **Tone**: professional, prescriptive, rigorous.
- **Small commits**, grouped by ID or feature; commit messages reference the IDs they touch.
- **Never commit credentials**, client-specific material, or anything from `temp/` that has not been harvested.

## Questions?

Open a [Discussion](https://github.com/mattgierhart/PRD-driven-context-engineering/discussions) — and if the
method earned it, [leave a star](https://github.com/mattgierhart/PRD-driven-context-engineering/stargazers)
on the way out. ⭐
