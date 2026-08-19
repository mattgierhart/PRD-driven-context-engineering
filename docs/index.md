# Documentation

The user-facing documents for the methodology. Everything a forker needs is in this directory or linked
from it; the repository's own v2 planning lives under [`v2/`](v2/README.md), and historical maintainer
records under [`maintainer/archive/`](maintainer/archive/README.md).

| Document | What it is | Read it when |
|---|---|---|
| [`INSTALL.md`](INSTALL.md) | The three adoption paths — fork / "Use this template", source-run install into an existing repo, the Claude Code plugin — with prerequisites | Starting a product on the method |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | The repository layout: which files are this repo's own truth, which are downstream seeds, which are the runtime, which are generated | Orienting in the repo; contributing |
| [`READINESS_PROTOCOL.md`](READINESS_PROTOCOL.md) | How the repo scores its own readiness (SoT → EPIC → PRD stage), the `status/readiness.json` schema, thresholds | Before advancing a gate; wiring CI |
| [`DEVELOPMENT_GRAPH.md`](DEVELOPMENT_GRAPH.md) | The code ↔ spec graph (`status/devgraph.json`): `@implements` / `@verifies` bridge edges, coverage and conformance | From v0.7, once code exists |
| [`MODERNIZATION_ASSESSMENT_PROMPT.md`](MODERNIZATION_ASSESSMENT_PROMPT.md) | A reusable prompt for assessing a downstream repo's drift from the current template | Upgrading a product repo |
| [`v2/`](v2/README.md) | The v2 direction: build plan, ontology, the Key Moments canon and design research, the site brief, the go-live polish plan and tracker | Following where the method is going |
| [`maintainer/archive/`](maintainer/archive/README.md) | Historical maintainer records (migration broadcasts, earlier improvement plans, superseded scratchpads) | Archaeology only |

`*.seed.md` files next to `READINESS_PROTOCOL.md` and `DEVELOPMENT_GRAPH.md` are the framework-owned
upstream originals that the installer seeds once into a consumer repo; edit the non-seed copy in a
product, never the seed.

Root-level references: [`README.md`](../README.md) · [`PRD.md`](../PRD.md) · [`CLAUDE.md`](../CLAUDE.md) ·
[`SoT/`](../SoT/SoT.README.md) · [`CHANGELOG.md`](../CHANGELOG.md) · [`MIGRATION.md`](../MIGRATION.md) ·
[`BLUEPRINT.md`](../BLUEPRINT.md).
