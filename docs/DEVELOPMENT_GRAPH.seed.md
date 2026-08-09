# Development Graph — Schema & Visualization Contract

**Status**: v0.1 (draft) · schema_version `0.1` · last revised 2026-06-06

The **Development Graph** is the "as-built" layer of the PRD-CE knowledge graph. Where the ID graph (`BR-`, `UJ-`, `API-`, `ARC-`…) is **top-down intent** authored before code exists, the Development Graph is **bottom-up structure** extracted from the product codebase during v0.7 build execution. Bridging the two — via the `@implements` / `@verifies` traceability tags required by the installed methodology's coding standard — lets the repo measure *build-vs-blueprint*: which specs have code, which code has no spec, and where the code has drifted from a recorded architecture decision.

This file is the canonical schema for `status/devgraph.json` and the contract for any optional
visualization consumer. A visualizer owns rendering (force-directed layout, community color,
god-node sizing — techniques borrowed from [Graphify](https://github.com/safishamsi/graphify));
the methodology owns the data described here. Anything rendered from the graph must be defined in
this document.

> **Companion docs**: [`READINESS_PROTOCOL.md`](READINESS_PROTOCOL.md) (the scorecard that consumes this graph) and [`.claude/domain-profile.yaml`](../.claude/domain-profile.yaml) (`code_node_types` + `bridge_relations`). The installed methodology supplies its readiness-discipline rule.

---

## 1. The three layers

The graph is one connected structure spanning three node layers. The `layer` field on every node says which it belongs to.

| Layer | `layer` value | Nodes | Source | Authored by | Graphify analog |
|---|---|---|---|---|---|
| **Spec** | `spec` | ID-prefixed specs (`BR-001`, `API-045`, `ARC-004`…) | SoT/PRD ID graph | Humans + agents (v0.1–v0.6) | `document` / `concept` nodes |
| **Code** | `code` | modules, classes, functions, tables, endpoints | AST extraction (tree-sitter), **free, no LLM** | Extractor (v0.7) | `code` nodes |
| **Bridge** | — (edges only) | `implements`, `verifies`, `references`, `violates` edges | `@implements`/`@see`/`@verifies` tags + conformance diff | Code authors via tags | `implements` / `references` edges |

The spec layer already exists as the ID graph. The code layer is a Graphify-style AST pass over the product source. The bridge is the traceability protocol turned into extracted edges — it is the entire reason this is more than "run `/graphify` on the repo."

---

## 2. Top-level shape

`status/devgraph.json` follows the **NetworkX node-link format** (`nx.node_link_data`), the same lineage Graphify uses — so force-graph viz tooling consumes it directly — plus three PRD-CE extensions (`conformance`, `coverage`, and a populated `graph` block).

```json
{
  "directed": true,
  "multigraph": false,
  "schema_version": "0.1",
  "graph": { /* §6 metadata: scope, generators, readiness cross-link, counts */ },
  "nodes": [ /* §3 */ ],
  "links": [ /* §4 — node-link calls edges "links" */ ],
  "conformance": [ /* §5 — ARC- rule verdicts */ ],
  "coverage": { /* §7 — graph-wide build/verify/conformance rollup */ },
  "hyperedges": [ /* §8 — optional, Graphify parity */ ]
}
```

`links` is the NetworkX node-link key for edges; a producer that emits `edges` instead must alias it. The readiness consumer (§9) reads only `nodes[].status` and `conformance[]`, never walks `links` — keeping the scorecard decoupled from edge representation.

---

## 3. Node schema

```json
{
  "id": "engine_parser_parsesotentry",
  "label": "parseSoTEntry",
  "layer": "code",
  "node_kind": "function",
  "file_type": "code",
  "source_file": "packages/extension/engine/parser/parse.ts",
  "source_location": "L42",
  "status": "traced",
  "implements": ["API-002", "BR-001"],
  "community": 3,
  "rationale": null,
  "confidence": "EXTRACTED"
}
```

| Field | Required | Meaning |
|---|---|---|
| `id` | ✓ | Stable identifier. **Spec nodes**: the ID itself (`API-002`). **Code nodes**: Graphify convention `{parent_dir}_{file}_{symbol}`, lowercased, `[a-z0-9_]` only. |
| `label` | ✓ | Human-readable name. |
| `layer` | ✓ | `spec` or `code`. Drives which status enum applies and which readiness dimension reads it. |
| `node_kind` | ✓ | Within `code`: one of `code_node_types` in the domain profile (`module`/`class`/`function`/`table`/`endpoint`). Within `spec`: the ID prefix (`BR`, `API`, `ARC`…). |
| `file_type` | ✓ | Graphify-compat render hint: `code`, `document`, `concept`. |
| `source_file` | ✓ | Repo-relative path the node was extracted from. |
| `source_location` | – | Line anchor (`L42`) for click-through. |
| `status` | ✓ | The **pulse** — see §3.1. Pre-computed by the extractor from edges so consumers don't re-derive it. |
| `implements` | – | Code nodes only: denormalized list of spec IDs this node bridges to (mirrors its outbound `implements`/`verifies` edges). Convenience for viz tooltips and readiness. |
| `community` | – | Leiden community index (Graphify-style clustering). Lets a visualizer color emergent subsystems. |
| `rationale` | – | Graphify pattern: design intent / "why" stored as a node **attribute**, not a separate node. |
| `confidence` | – | For inferred nodes: `EXTRACTED` / `INFERRED` / `AMBIGUOUS` (§10). AST-extracted code nodes are always `EXTRACTED`. |

### 3.1 The `status` enum — the pulse

`status` is the primary visualization state. It is derived by the extractor from the bridge edges, so it is the single field that encodes build-vs-blueprint per node.

**Spec-layer node status:**

| `status` | Means | Bridge condition | Visual treatment |
|---|---|---|---|
| `implemented` | Built and verified | ≥1 `implements` **and** ≥1 `verifies` inbound edge | 🟢 green |
| `implemented_unverified` | Built, no test | ≥1 `implements`, 0 `verifies` | 🟡 amber |
| `unimplemented` | Specified, no code | 0 `implements` inbound | 🔴 red |

**Code-layer node status:**

| `status` | Means | Bridge condition | Visual treatment |
|---|---|---|---|
| `traced` | Implements ≥1 spec | ≥1 outbound `implements`/`verifies`/`references` | 🟢 green |
| `orphan` | Code with no spec ("context leak") | 0 outbound bridge edges | ⚪ grey |
| `drift` | Breaks an architecture rule | ≥1 outbound `violates` edge | 🔴 red |

`unimplemented` specs and `drift` code are the two red states an optional pulse view can surface.

---

## 4. Edge (`links`) schema

```json
{
  "source": "engine_parser_parsesotentry",
  "target": "API-002",
  "relation": "implements",
  "confidence": "EXTRACTED",
  "confidence_score": 1.0,
  "source_location": "packages/extension/engine/parser/parse.ts:40"
}
```

Relations, grouped by which layers they connect:

| `relation` | From → To | Source | Confidence |
|---|---|---|---|
| `calls` | code → code | AST call graph | `EXTRACTED` / `INFERRED` |
| `imports` | code → code | AST import statement | `EXTRACTED` |
| `implements` | code → spec | `// @implements <ID>` tag | `EXTRACTED` (tag) / `INFERRED` (name match) |
| `verifies` | code(test) → spec | `// @verifies <ID>` or a `TEST-` entry referencing the ID | `EXTRACTED` / `INFERRED` |
| `references` | code → spec | `// @see <ID>` tag | `EXTRACTED` |
| `violates` | code → spec(ARC) | conformance diff (§5) | `EXTRACTED` (structural check) |
| `relates_to` | spec → spec | ID cross-reference in SoT body | `EXTRACTED` |

`calls` edges must stay within one language and point caller → callee (Graphify rule). Bridge edges always point **code → spec**, never the reverse.

---

## 5. `conformance` block — architecture rules as checkable claims

`ARC-` decisions often make *structural claims* the code graph can verify (e.g. *"the `engine/` layer must have zero VS Code imports"*). Each such claim becomes a conformance entry with a machine verdict — this is the drift signal that feeds the `architecture_conformance` readiness dimension.

```json
{
  "arc_id": "ARC-004",
  "rule": "engine/ layer must not import the vscode API",
  "check": { "type": "forbidden_import", "scope": "packages/extension/engine/**", "forbidden": "vscode" },
  "verdict": "violate",
  "violations": [
    { "source": "engine_parser_parsesotentry", "target": "vscode", "source_location": "parser.ts:12" }
  ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `arc_id` | ✓ | The `ARC-` (or `BR-`) ID whose claim is being checked. Must match a spec node `id`. |
| `rule` | ✓ | Human-readable statement of the constraint. |
| `check` | – | Machine description of how it was evaluated (advisory; for reproducibility). |
| `verdict` | ✓ | `pass` (holds), `violate` (broken — drift), `unknown` (could not be checked). |
| `violations` | – | When `violate`: the offending edges, for a visualizer to highlight and readiness to cite. |

A `violate` produces a `violates` bridge edge from each offending code node to the ARC spec node, flipping that code node's `status` to `drift`.

---

## 6. `graph` metadata block

```json
{
  "scope": "EPIC-06",
  "scope_ids": ["BR-001", "API-002", "ARC-004", "..."],
  "generated_by": "prd-v07-build-graph@0.1",
  "generated_at": "2026-06-06T18:04:11Z",
  "readiness_ref": "status/readiness.json",
  "source_root": "packages/extension",
  "languages": ["typescript"],
  "layer_counts": { "spec": 40, "code": 214 },
  "edge_counts": { "implements": 31, "verifies": 22, "calls": 180, "violates": 1 }
}
```

`scope` ties the graph to an EPIC (or `"repo"` for a full-repo build). `scope_ids` is the spec set the EPIC claims — the denominator for coverage. `readiness_ref` cross-links to the scorecard so the two outputs are navigable as a pair. Timestamps are stamped by the producer (the scorer never invents them).

---

## 7. `coverage` rollup

A graph-wide summary a visualizer may show as headline gauges and readiness can sanity-check against.

```json
{
  "specs_total": 40,
  "specs_implemented": 31,
  "specs_unverified": 5,
  "specs_unimplemented": 4,
  "code_total": 214,
  "code_orphan": 8,
  "conformance_rules": 6,
  "conformance_passing": 5,
  "by_prefix": {
    "BR":  { "total": 12, "implemented": 11 },
    "API": { "total": 10, "implemented": 9 },
    "DBT": { "total": 6,  "implemented": 6 }
  }
}
```

`by_prefix` is graph-global; the readiness EPIC dimension recomputes coverage scoped to one EPIC's `scope_ids`, so the two can differ — that is expected, not a conflict.

---

## 8. `hyperedges` (optional, Graphify parity)

Group relationships connecting 3+ nodes that pairwise edges miss — e.g. *all* functions in an auth flow, or *all* code implementing one `FEA-`. Use sparingly.

```json
{ "id": "auth_flow", "label": "Authentication flow", "nodes": ["...", "...", "..."], "relation": "participate_in", "confidence": "INFERRED", "confidence_score": 0.85 }
```

---

## 9. How readiness consumes this graph

`scripts/_readiness/epic.py` reads `status/devgraph.json` via `load_devgraph()` and powers two EPIC dimensions (both **auto-disable** when the file is absent, so pre-build repos score unchanged):

| Readiness dimension | Reads | Score |
|---|---|---|
| `implementation_coverage` | `nodes[].status` for `layer:spec` nodes whose `id` is in the EPIC's Section 3 **and** of an implementable prefix (`BR/API/DBT/ENT/FEA/SCR/UJ`) | fraction with status `implemented` or `implemented_unverified` |
| `architecture_conformance` | `conformance[]` entries whose `arc_id` is referenced by the EPIC | fraction with `verdict: pass` |

Plus a critical cap: **`unbuilt_specs`** caps an EPIC at 60 when `implementation_coverage < 50%` — most of what the EPIC claims to build has no implementing code. See [`READINESS_PROTOCOL.md` §4, §7](READINESS_PROTOCOL.md).

The contract that matters for readiness: spec nodes carry an accurate `status`, and conformance entries carry an `arc_id` + `verdict`. Other presentation fields serve optional visualization consumers.

---

## 10. Confidence audit trail (borrowed from Graphify)

Every inferred node and edge carries an honest confidence label, so a visualizer can distinguish *known* structure from *guessed* structure and readiness can discount the latter.

| Label | `confidence_score` | When |
|---|---|---|
| `EXTRACTED` | `1.0` | Explicit in source — an `@implements` tag, an import statement, a structural conformance check. |
| `INFERRED` | discrete `0.55`–`0.95` | A reasonable deduction — a function name matching a `BR-` keyword, a likely call target. Use the Graphify discrete rubric, never `0.5`. |
| `AMBIGUOUS` | `0.1`–`0.3` | Uncertain — surfaced for human review, never silently dropped. |

A bridge edge from a literal `@implements BR-101` tag is `EXTRACTED`. A guess that `validateToken()` implements `BR-101` because the names align is `INFERRED`. This is what keeps the graph trustworthy: the green pulse means *traced*, not *assumed*.

---

## 11. Producing the graph (the pipeline)

Generation is the job of the v0.7 build skill (`prd-v07-build-graph`, forthcoming) and is intentionally **not** part of the readiness scorer — the scorer only reads the output. The pipeline mirrors Graphify's stages, scoped to the active EPIC:

```
detect()  →  extract_ast()  →  harvest_tags()  →  check_conformance()  →  derive_status()  →  build_node_link()  →  write devgraph.json
            (tree-sitter,      (@implements/      (ARC- rules vs         (per §3.1)            (+ Leiden cluster,
             free, no LLM)      @verifies/@see)    code edges)                                  god nodes)
```

- **`extract_ast`** — Graphify Pass 1: classes, functions, imports, call graph, SQL tables/FKs. Deterministic, free, cacheable by content hash for incremental rebuilds.
- **`harvest_tags`** — scan code comments for `@implements`/`@verifies`/`@see <ID>`; emit bridge edges (`EXTRACTED`). Optionally infer additional bridges by name/context match (`INFERRED`).
- **`check_conformance`** — evaluate each `ARC-` rule against the code edges; emit `conformance[]` verdicts and `violates` edges.
- **`derive_status`** — set every node's `status` per §3.1 from its bridge edges.
- **`build_node_link`** — assemble the node-link JSON, run Leiden clustering for `community`, compute god nodes, write `status/devgraph.json`.

Until that skill lands, the schema here is the stable target: a visualization consumer can develop against the §12 example, and the readiness dimensions already read the contract.

---

## 12. Worked example

A minimal but complete `status/devgraph.json` — one implemented spec, one unbuilt spec, one drift, one conformance violation:

```json
{
  "directed": true,
  "multigraph": false,
  "schema_version": "0.1",
  "graph": {
    "scope": "EPIC-01",
    "scope_ids": ["BR-001", "API-002", "ARC-004"],
    "generated_by": "prd-v07-build-graph@0.1",
    "generated_at": "2026-06-06T18:04:11Z",
    "readiness_ref": "status/readiness.json",
    "layer_counts": { "spec": 3, "code": 2 }
  },
  "nodes": [
    { "id": "BR-001",  "label": "Free tier rate limit", "layer": "spec", "node_kind": "BR",  "file_type": "concept", "source_file": "SoT/SoT.BUSINESS_RULES.md", "status": "implemented" },
    { "id": "API-002", "label": "POST /parse",          "layer": "spec", "node_kind": "API", "file_type": "concept", "source_file": "SoT/SoT.API_CONTRACTS.md", "status": "unimplemented" },
    { "id": "ARC-004", "label": "engine has no vscode import", "layer": "spec", "node_kind": "ARC", "file_type": "concept", "source_file": "SoT/SoT.TECHNICAL_DECISIONS.md", "status": "implemented" },
    { "id": "limiter_ratelimiter_check", "label": "RateLimiter.check", "layer": "code", "node_kind": "function", "file_type": "code", "source_file": "src/limiter.ts", "source_location": "L20", "status": "traced", "implements": ["BR-001"], "confidence": "EXTRACTED" },
    { "id": "engine_parser_parse", "label": "parse", "layer": "code", "node_kind": "function", "file_type": "code", "source_file": "engine/parser.ts", "source_location": "L12", "status": "drift", "confidence": "EXTRACTED" }
  ],
  "links": [
    { "source": "limiter_ratelimiter_check", "target": "BR-001", "relation": "implements", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_location": "src/limiter.ts:18" },
    { "source": "engine_parser_parse", "target": "ARC-004", "relation": "violates", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_location": "engine/parser.ts:12" }
  ],
  "conformance": [
    { "arc_id": "ARC-004", "rule": "engine/ must not import vscode",
      "check": { "type": "forbidden_import", "scope": "engine/**", "forbidden": "vscode" },
      "verdict": "violate",
      "violations": [ { "source": "engine_parser_parse", "target": "vscode", "source_location": "engine/parser.ts:12" } ] }
  ],
  "coverage": {
    "specs_total": 3, "specs_implemented": 2, "specs_unimplemented": 1,
    "code_total": 2, "code_orphan": 0,
    "conformance_rules": 1, "conformance_passing": 0
  }
}
```

Reading the pulse: `BR-001` 🟢 (built + verified), `API-002` 🔴 (specified, never built), `ARC-004` flagged by a `violate` so `engine_parser_parse` is 🔴 drift. That is what a visualization consumer may render and what `implementation_coverage` (1 of 2 implementable specs = 50%) and `architecture_conformance` (0 of 1 ARC rule passing = 0%) score.

---

## 13. Versioning

`schema_version` bumps on any breaking shape change. The Development Graph schema versions **independently** of `readiness.json`'s `schema_version` — they are separate contracts that cross-link via `graph.readiness_ref`. A visualization consumer should pin the `schema_version` it supports and warn on mismatch.

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-06-06 | Initial draft: three-layer node-link schema, status pulse, conformance block, readiness consumption, and visualization contract. |

---

## 14. Required cross-reference edges (U2 — schema contract)

The bridge edges in §4 are *extracted* — discovered from code tags. **Required edges** are the inverse: *asserted* constraints on the spec graph that must hold regardless of code. They turn "if it's not in the graph it isn't true" from a slogan into a checked invariant — the enforcement half of treating the ID registry as a validated contract (P12).

Where the installed methodology's `validate-ids.sh` checks **structural** integrity (dangling / orphan / duplicate IDs), `validate-edges.py` checks **semantic** integrity: that each entry of a given prefix carries the cross-reference edges its type requires. Rules are declared in [`.claude/domain-profile.yaml`](../.claude/domain-profile.yaml) under `required_edges:` and are **opt-in** — a repo (or the methodology template) that declares none validates clean.

### Rule schema

```yaml
required_edges:
  - from: UJ            # every UJ- entry...
    requires: SCR       # ...must reference at least one SCR- (string or list)
    direction: outbound # outbound (default) | inbound
    severity: warn      # warn (report, exit 0) | block (report, exit 1)
    description: "A user journey must map to at least one screen"
```

| Field | Required | Meaning |
|---|---|---|
| `from` | ✓ | The prefix every entry of which is checked. |
| `requires` | ✓ | The prefix (or list of prefixes) each `from` entry must be edged to. Each listed prefix is independently required (AND). |
| `direction` | – | `outbound` (default): the `from` entry's body must reference a `requires` ID — e.g. a UJ lists its screens. `inbound`: some `requires` entry must reference the `from` one — the convention for test coverage, where a `TEST-` points back at the `API-`/`BR-` it verifies. |
| `severity` | – | `warn` (default; reported, non-fatal) or `block` (fails the gate — exit 1). |
| `description` | – | Human-readable rationale, printed with each violation. |

### How it composes with the gate

`validate-ids.sh` invokes `validate-edges.py` as its check #4; only `block`-severity violations count toward its issue total, so `warn` rules surface drift without failing CI until a team opts to enforce them. Invalid rule schemas, directions, severities, unregistered prefixes, or a missing `python3` semantic runtime fail closed with exit `2`. The semantic check parses entry bodies and prefixes by reusing the readiness index in `scripts/_readiness/common.py`; the structural checks #1–#3 remain Bash-only.

Recommended starter set (commented in `domain-profile.yaml`): `API→TEST` and `BR→TEST` (inbound, "Tests First"), `UJ→SCR` and `SCR→UJ` (outbound, journey/screen integrity).
