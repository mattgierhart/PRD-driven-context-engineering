# Contributing to Gear Heart Methodology (GHM)

Thanks for your interest in improving the Gear Heart Methodology! This project documents a clear, disciplined way to ship software. Contributions that improve clarity, correctness, and usability are welcome.

## Ways to Contribute
- Fix typos, broken links, or ambiguous wording
- Improve explanations, add examples, or diagrams
- Propose template enhancements (PRD, Command Center, EPIC, Testing)
- Add optional modules/guides (e.g., integrations) while staying vendor‑neutral
- File issues for gaps, confusing areas, or inconsistencies

## Ground Rules
- Vendor‑neutral and product‑agnostic: avoid product names, pricing, private infra
- One source of truth: prefer updating existing docs over adding near‑duplicates
- Keep links relative, and prefer docs within this package when possible
- Use inclusive, respectful language; follow the Code of Conduct

## Development Setup
This repository is documentation‑first — there is no build step required.

Recommended locally:
- Markdown preview in your editor
- Optional link check: run a markdown link checker or rely on CI

CI:
- A GitHub Action checks markdown links in `gear-heart-methodology/` on PRs

## Proposing Changes
1. Fork the repository
2. Create a feature branch
   - `docs/ghm-clarify-workflow-gates`
   - `feat/ghm-add-architecture-template`
3. Make changes and commit with a clear message
   - `docs(ghm): clarify Gate 2 acceptance criteria`
   - `feat(ghm): add multi‑product example to EPIC template`
4. Push and open a Pull Request against `main`

## PR Checklist
- Content is vendor‑neutral and product‑agnostic
- Links are relative and valid (CI passes link check)
- No duplicate “near‑same” docs; update canonical files instead
- Templates keep the minimal, reusable core (examples belong under `docs/examples/`)
- If the change is notable, update `CHANGELOG.md`

## License
By contributing, you agree your contributions are licensed under the MIT License included in this repository.

## Code of Conduct
This project adheres to a Code of Conduct. By participating, you agree to uphold it.
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
