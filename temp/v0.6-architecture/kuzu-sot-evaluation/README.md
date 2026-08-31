# Kuzu vs Markdown SoT evaluation

This is a read-only architecture spike for the PRD-Led Context Engineering
Source-of-Truth (SoT) knowledge graph.

It compares the same ID corpus through two retrieval surfaces:

1. canonical Markdown files parsed into an ephemeral in-memory graph; and
2. the same nodes and edges materialized in a local Kuzu `v0.11.3` property graph.

The experiment does **not** edit the GearHeart product repositories. Their Markdown
files are read in place. Committed evidence includes product aliases, IDs,
questions, relative evidence paths and line numbers, selected semantic-check
titles, repository commits, and content fingerprints. It excludes absolute source
paths, source bodies, and PII. Publication still requires a human review of this
metadata.

## Artifacts

- `artifacts/report.html` — self-contained visual findings report
- `artifacts/results.json` — machine-readable run evidence
- `artifacts/accuracy-results.json` — deterministic conformance-test evidence
- `artifacts/run-manifest.json` — versions, corpus fingerprints, and safeguards
- `benchmark-cases.json` — manifest-authored, separately reviewed expected answers
- `src/sot_benchmark.py` — parser, Markdown engine, Kuzu engine, and runner
- `src/conformance.py` — backend-neutral core/pack accuracy oracle
- `src/lifecycle_audit.py` — read-only cross-artifact lifecycle consistency audit
- `src/run_accuracy_suite.py` — test runner and accuracy-evidence emitter
- `src/report.py` — self-contained visual report renderer
- `tests/fixtures/conformance/packs.json` — test-only Product, Accounting, and
  Restaurant pack serialization
- `tests/test_sot_benchmark.py` — parser/query/authority-boundary tests
- `tests/test_conformance.py` — identity, temporal, lifecycle, pack, and evidence tests
- `tests/test_lifecycle_audit.py` — executable/prose lifecycle-contract differential tests

## Reproduce

```bash
./bootstrap.sh

.venv/bin/python src/sot_benchmark.py run \
  --source heartbeat=/path/to/GearHeart/HeartBeat \
  --source agenthunt=/path/to/GearHeart/AgentHunt \
  --source homefalcon=/path/to/GearHeart/HomeFalcon \
  --cases benchmark-cases.json \
  --output artifacts \
  --repeats 50 \
  --authority-corpus heartbeat

.venv/bin/python src/run_accuracy_suite.py \
  --output artifacts/accuracy-results.json
```

The three aliases above are the stable namespaces used by the committed gold cases.
The report records only those aliases, repository commits, and content
fingerprints—not machine-specific source paths. The runner can evaluate another
PRD-CE corpus without code changes when supplied with a matching gold-case file.
The current prototype creates one Kuzu database per corpus; it does not yet prove
a combined portfolio database or composite-key namespace.

## Accuracy dimensions

The results deliberately do not publish one blended “accuracy” number:

1. **Source fidelity** — 25 checked ID-set cases across HeartBeat, AgentHunt, and
   HomeFalcon. Both retrieval engines reproduce all 25 authored sets. This is
   parser/storage parity, not semantic truth.
2. **Semantic truth** — two seeded deterministic checks correctly produce
   `conflict`: HomeFalcon's authored `TECH-007 → UJ-007/UJ-008` meanings do not
   match the canonical journey titles, and HeartBeat's v1.0 adoption examples
   contain placeholder evidence.
3. **Epistemic conformance** — immutable assertion revisions cover scoped
   identity, provenance, the five-state core lifecycle, half-open valid and
   transaction time, supersession reciprocity/cycles, ambiguous-current
   fail-closed behavior, and rejected alternatives/evidence boundaries.
4. **Lifecycle manifest coverage** — real source-fidelity cases label every PRD
   stage from v0.1 through v1.0, and each anchor family is checked against the
   artifact families appropriate to that stage. This is coverage of the benchmark
   manifest, not proof that a product completed the lifecycle. A strict synthetic
   gate matrix separately tests required counts, semantic fields, graph edges, and
   provenance-bearing qualitative attestations.

The deterministic suite currently runs 75 tests: 45 core/pack conformance,
four lifecycle-contract audits, 13 benchmark-harness tests, eleven
accuracy-artifact integrity tests, and two report acceptance tests. Product pack
gates return `BLOCK` for deterministic failures, `REVIEW` when mandatory
qualitative attestations are absent, and `PASS` only when both are present. A
numeric readiness score cannot override a blocker.

The pack fixture uses JSON only to make tests repeatable. It does not decide the
future pack-authoring format or promote the draft core/pack analysis into the
canonical PRD-CE methodology.

## Lifecycle contract findings

The audit preserves six current inconsistencies as explicit findings instead of
silently choosing one source:

- v0.5 gate prose requires `SCR`, while executable counts require only `PER` and `UJ`;
- v0.6 readiness references absent `SoT/SoT.RISKS.md`, while `RISK` is PRD-owned;
- README says `BR` entries are created at v0.2, while the ID registry assigns
  `BR` to v0.6;
- README/PRD call v1.0 Market Adoption, while executable readiness calls the
  target Launch;
- v1.0 describes `ADO` evidence but has no executable adoption-artifact
  requirement; and
- the current count implementation can pass superseded, void, and draft headings
  because it does not evaluate assertion state.

These are observations from read-only tests. This experiment does not change the
canonical lifecycle documents.

## What the tests can and cannot prove

The benchmark directly measures parsing/index build cost, query correctness,
warm-query latency, retrieval payload size, disk footprint, graph traversal,
staleness after a Markdown edit, and rebuild recovery. It also records observable
workflow properties such as text diffs versus binary database changes.

The accuracy suite proves deterministic behavior for its synthetic histories and
seeded conflicts. It does not yet provide a blind raw-Markdown/JIT arm, independent
parser gold extraction, free-form agent answers, human adjudication, broad semantic
precision/recall, graph algorithms, incremental indexing, or a combined
multi-product database. The two retrieval arms still share one parser and neutral
snapshot. Freshness policy declarations and their schema projection are tested,
as are latest-visible-observation precedence and explicit verification resolution.
Automatic TTL expiry and scheduled re-review are not implemented or tested, so
state never ages out merely because time passes. Those limits are explicit in the
report and machine-readable artifacts.
