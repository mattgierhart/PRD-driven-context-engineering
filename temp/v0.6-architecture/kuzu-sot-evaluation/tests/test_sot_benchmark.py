from __future__ import annotations

import dataclasses
import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))

import sot_benchmark  # noqa: E402
from sot_benchmark import (  # noqa: E402
    BenchmarkCase,
    KuzuEngine,
    MarkdownEngine,
    authority_boundary_experiment,
    evaluate_acceptance,
    evaluate_lifecycle_manifest_coverage,
    evaluate_semantic_check,
    load_case_manifest,
    load_cases,
    parse_corpus,
    validate_cases,
)
from report import render_report  # noqa: E402


FIXTURE = """# Fixture

## ARC-001: Markdown authority

**Status**: Accepted

### Decision

The repository remains authoritative. It is implemented by DBT-004 and
depends on BR-017.

### Related IDs

- DBT-004
- BR-017

## DBT-004: Rebuildable graph cache

The cache references ARC-001 and API-003.

## API-003: Graph snapshot

Returns DBT-004.

## ADO-STAGE-001: Current stage

The compound ID must remain intact and references ARC-001.

| BR-017 | Repo-owned truth | ARC-001 |
"""


class BenchmarkHarnessTests(unittest.TestCase):
    def make_repo(self, root: Path, fixture: str = FIXTURE) -> Path:
        (root / "SoT").mkdir(parents=True)
        (root / "README.md").write_text("# Fixture repo\n", encoding="utf-8")
        (root / "PRD.md").write_text("# PRD\n", encoding="utf-8")
        (root / "SoT" / "SoT.TEST.md").write_text(fixture, encoding="utf-8")
        return root

    def test_parser_preserves_nested_body_and_compound_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = parse_corpus("fixture", self.make_repo(Path(temporary)))

        self.assertIn("ADO-STAGE-001", corpus.defined_entries)
        self.assertNotIn("STAGE-001", corpus.entries)
        self.assertIn("### Decision", corpus.entries["ARC-001"].body)
        targets = {
            edge.target for edge in corpus.edges if edge.source == "ARC-001"
        }
        self.assertEqual(targets, {"DBT-004", "BR-017"})

    def test_duplicate_definitions_are_reported(self) -> None:
        duplicate = FIXTURE + "\n## ARC-001: Accidental duplicate\n"
        with tempfile.TemporaryDirectory() as temporary:
            corpus = parse_corpus(
                "fixture", self.make_repo(Path(temporary), fixture=duplicate)
            )

        self.assertIn("ARC-001", corpus.duplicate_definitions)
        self.assertEqual(len(corpus.duplicate_definitions["ARC-001"]), 2)

    def test_markdown_and_kuzu_return_identical_graph_answers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            corpus = parse_corpus("fixture", self.make_repo(root / "repo"))
            markdown = MarkdownEngine(corpus)
            graph = KuzuEngine(corpus, root / "fixture.kuzu")
            cases = (
                BenchmarkCase(
                    id="lookup",
                    corpus="fixture",
                    question="",
                    kind="lookup",
                    anchor="ARC-001",
                ),
                BenchmarkCase(
                    id="outgoing",
                    corpus="fixture",
                    question="",
                    kind="traverse",
                    anchor="ARC-001",
                    direction="outgoing",
                    depth=1,
                ),
                BenchmarkCase(
                    id="incoming",
                    corpus="fixture",
                    question="",
                    kind="traverse",
                    anchor="ARC-001",
                    direction="incoming",
                    depth=1,
                ),
                BenchmarkCase(
                    id="compound",
                    corpus="fixture",
                    question="",
                    kind="prefix",
                    prefix="ADO",
                ),
            )
            for case in cases:
                with self.subTest(case=case.id):
                    self.assertEqual(markdown.query(case), graph.query(case))

    def test_ids_are_scoped_by_corpus(self) -> None:
        first = FIXTURE.replace("Markdown authority", "First meaning")
        second = FIXTURE.replace("Markdown authority", "Second meaning")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            corpus_a = parse_corpus(
                "product-a", self.make_repo(root / "a", fixture=first)
            )
            corpus_b = parse_corpus(
                "product-b", self.make_repo(root / "b", fixture=second)
            )

        self.assertNotEqual(
            corpus_a.entries["ARC-001"].body_hash,
            corpus_b.entries["ARC-001"].body_hash,
        )
        self.assertEqual(corpus_a.entries["ARC-001"].id, corpus_b.entries["ARC-001"].id)

    def test_kuzu_payload_entries_are_read_from_database(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            corpus = parse_corpus("fixture", self.make_repo(root / "repo"))
            graph = KuzuEngine(corpus, root / "fixture.kuzu")
            stored_body = corpus.entries["ARC-001"].body
            corpus.entries["ARC-001"] = dataclasses.replace(
                corpus.entries["ARC-001"],
                body="mutated only in the in-memory corpus",
            )

            graph_entry = graph.get_entries(["ARC-001"])[0]

        self.assertEqual(graph_entry.body, stored_body)
        self.assertNotEqual(graph_entry.body, corpus.entries["ARC-001"].body)

    def test_authority_experiment_detects_stale_projection_and_recovers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            corpus = parse_corpus("fixture", self.make_repo(root / "repo"))
            graph = KuzuEngine(corpus, root / "original.kuzu")
            result = authority_boundary_experiment(corpus, graph, root)

        self.assertEqual(result["status"], "complete")
        self.assertTrue(result["cached_graph_was_stale"])
        self.assertFalse(result["cached_hash_matched_new_source"])
        self.assertTrue(result["rebuilt_hash_matched_new_source"])
        self.assertGreater(result["binary_database_files_changed"], 0)

    def test_report_is_independent_of_mapping_insertion_order(self) -> None:
        results = json.loads(
            (EXPERIMENT_ROOT / "artifacts" / "results.json").read_text(
                encoding="utf-8"
            )
        )
        reordered = dict(reversed(tuple(results.items())))

        self.assertEqual(render_report(results), render_report(reordered))

    def test_literal_fidelity_and_semantic_truth_are_separate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = parse_corpus(
                "fixture", self.make_repo(Path(temporary))
            )
        case = BenchmarkCase(
            id="semantic-separation",
            corpus="fixture",
            question="",
            kind="lookup",
            anchor="ARC-001",
            expected=("ARC-001",),
            semantic_check={
                "type": "target_title_contains",
                "terms_by_id": {"ARC-001": ["Kuzu is authoritative"]},
                "expected_verdict": "conflict",
                "required_action": "flag",
            },
        )

        self.assertEqual(MarkdownEngine(corpus).query(case), ["ARC-001"])
        semantic = evaluate_semantic_check(case, corpus)
        self.assertEqual(semantic["actual_verdict"], "conflict")
        self.assertTrue(semantic["verdict_exact"])
        self.assertEqual(
            semantic["findings"][0]["code"],
            "SEMANTIC_TARGET_TITLE_MISMATCH",
        )

    def test_gold_manifest_covers_the_full_prd_lifecycle(self) -> None:
        path = EXPERIMENT_ROOT / "benchmark-cases.json"
        cases, manifest = load_case_manifest(path)
        coverage = evaluate_lifecycle_manifest_coverage(cases)

        self.assertTrue(coverage["complete"])
        self.assertEqual(coverage["missing_stages"], [])
        self.assertEqual(coverage["unknown_stage_cases"], [])
        self.assertEqual(coverage["invalid_anchor_cases"], [])
        self.assertEqual(manifest["case_count"], len(cases))
        self.assertEqual(
            manifest["sha256"],
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
        self.assertFalse(manifest["gold_review"]["independence_claim"])
        self.assertFalse(
            manifest["gold_review"]["human_adjudication_claim"]
        )

    def test_lifecycle_manifest_rejects_wrong_anchor_family(self) -> None:
        cases = load_cases(EXPERIMENT_ROOT / "benchmark-cases.json")
        spark_index = next(
            index
            for index, case in enumerate(cases)
            if case.lifecycle_stage.startswith("v0.1 ")
        )
        cases[spark_index] = dataclasses.replace(
            cases[spark_index],
            anchor="BR-001",
        )

        coverage = evaluate_lifecycle_manifest_coverage(cases)

        self.assertFalse(coverage["complete"])
        self.assertEqual(
            coverage["invalid_anchor_cases"],
            [
                {
                    "case_id": cases[spark_index].id,
                    "stage": "v0.1",
                    "anchor": "BR-001",
                    "actual_family": "BR",
                    "allowed_families": ["CFD"],
                }
            ],
        )

    def test_acceptance_requires_all_four_evidence_dimensions(self) -> None:
        stage_anchors = (
            ("v0.1 Spark", "CFD-001"),
            ("v0.2 Market Definition", "BR-001"),
            ("v0.3 Commercial Model", "KPI-001"),
            ("v0.4 User Journeys", "UJ-001"),
            ("v0.5 Red Team Review", "RISK-001"),
            ("v0.6 Architecture", "ARC-001"),
            ("v0.7 Build Execution", "TEST-001"),
            ("v0.8 Release", "DEP-001"),
            ("v0.9 Go-to-Market", "GTM-001"),
            ("v1.0 Market Adoption", "ADO-STAGE-001"),
        )
        cases = [
            BenchmarkCase(
                id=f"acceptance-case-{index}",
                corpus="fixture",
                question="",
                kind="lookup",
                anchor=anchor,
                expected=(anchor,),
                lifecycle_stage=stage,
                semantic_check=(
                    {
                        "type": "target_title_contains",
                        "expected_verdict": "clear",
                    }
                    if index == 1
                    else {}
                ),
            )
            for index, (stage, anchor) in enumerate(
                stage_anchors,
                start=1,
            )
        ]
        case = cases[0]
        rows = [
            {
                "case_id": item.id,
                "engine": engine,
                "exact": True,
                "actual": list(item.expected),
                "expected": list(item.expected),
            }
            for item in cases
            for engine in ("markdown", "kuzu")
        ]
        dimensions = {
            "semantic_truth": {
                "checks": [
                    {
                        "case_id": case.id,
                        "verdict_exact": True,
                        "expected_verdict": "clear",
                        "actual_verdict": "clear",
                    }
                ]
            },
            "lifecycle_manifest_coverage": {
                **evaluate_lifecycle_manifest_coverage(cases),
            },
        }
        authority = {
            "status": "complete",
            "rebuilt_hash_matched_new_source": True,
        }

        accepted = evaluate_acceptance(
            cases,
            rows,
            dimensions,
            authority,
        )

        self.assertTrue(accepted["passed"])
        self.assertTrue(
            all(check["passed"] for check in accepted["checks"].values())
        )

        failures = (
            (
                "missing-engine",
                rows[1:],
                dimensions,
                authority,
                "source_fidelity",
            ),
            (
                "source",
                [{**rows[0], "exact": False}, *rows[1:]],
                dimensions,
                authority,
                "source_fidelity",
            ),
            (
                "semantic",
                rows,
                {
                    **dimensions,
                    "semantic_truth": {
                        "checks": [
                            {
                                "case_id": case.id,
                                "verdict_exact": False,
                                "expected_verdict": "clear",
                                "actual_verdict": "conflict",
                            }
                        ]
                    },
                },
                authority,
                "semantic_truth",
            ),
            (
                "lifecycle",
                rows,
                {
                    **dimensions,
                    "lifecycle_manifest_coverage": {
                        "complete": False,
                        "missing_stages": ["v1.0"],
                    },
                },
                authority,
                "lifecycle_manifest_coverage",
            ),
            (
                "authority",
                rows,
                dimensions,
                {
                    "status": "skipped",
                    "rebuilt_hash_matched_new_source": False,
                },
                "authority_boundary",
            ),
        )
        for label, failed_rows, failed_dimensions, failed_authority, check in failures:
            with self.subTest(label=label):
                rejected = evaluate_acceptance(
                    cases,
                    failed_rows,
                    failed_dimensions,
                    failed_authority,
                )
                self.assertFalse(rejected["passed"])
                self.assertFalse(rejected["checks"][check]["passed"])

        forged_rows = [
            {
                **row,
                "actual": ["DBT-999"],
                "expected": ["DBT-999"],
                "exact": True,
            }
            for row in rows
        ]
        forged_semantic = {
            **dimensions,
            "semantic_truth": {
                "checks": [
                    {
                        "case_id": case.id,
                        "expected_verdict": "conflict",
                        "actual_verdict": "conflict",
                        "verdict_exact": True,
                    }
                ]
            },
        }

        self.assertFalse(
            evaluate_acceptance(
                cases,
                forged_rows,
                dimensions,
                authority,
            )["checks"]["source_fidelity"]["passed"]
        )
        self.assertFalse(
            evaluate_acceptance(
                cases,
                rows,
                forged_semantic,
                authority,
            )["checks"]["semantic_truth"]["passed"]
        )

    def test_main_returns_nonzero_when_acceptance_fails(self) -> None:
        result = {
            "rollup": {},
            "authority_boundary": {"status": "complete"},
            "acceptance": {
                "passed": False,
                "policy": "test",
                "checks": {},
            },
        }
        args = mock.Mock(
            command="run",
            output=Path("artifacts"),
        )
        parser = mock.Mock()
        parser.parse_args.return_value = args

        with (
            mock.patch.object(sot_benchmark, "build_parser", return_value=parser),
            mock.patch.object(
                sot_benchmark,
                "run_benchmark",
                return_value=result,
            ),
            redirect_stdout(io.StringIO()),
        ):
            exit_code = sot_benchmark.main()

        self.assertEqual(exit_code, 1)

    def test_evidence_spans_must_resolve_to_nonblank_source_lines(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = parse_corpus(
                "fixture", self.make_repo(Path(temporary))
            )
            invalid = BenchmarkCase(
                id="bad-evidence",
                corpus="fixture",
                question="",
                kind="lookup",
                anchor="ARC-001",
                expected=("ARC-001",),
                evidence=("SoT/SoT.TEST.md:9999",),
            )

            with self.assertRaisesRegex(
                ValueError, "evidence line outside file"
            ):
                validate_cases([invalid], {"fixture": corpus})


if __name__ == "__main__":
    unittest.main()
