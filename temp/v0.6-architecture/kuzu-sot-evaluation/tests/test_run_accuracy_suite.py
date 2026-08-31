from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))

from run_accuracy_suite import (  # noqa: E402
    benchmark_binding,
    build_input_manifest,
    issue_details,
    read_bound_json,
    repository_commit,
    run,
    suite_identity,
    verify_benchmark_manifest_binding,
    verify_input_manifest,
)


class AccuracyArtifactTests(unittest.TestCase):
    def test_input_manifest_hashes_all_declared_input_classes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "tests" / "fixtures" / "nested").mkdir(parents=True)
            (root / "artifacts").mkdir()
            files = {
                "src/engine.py": "engine = 1\n",
                "tests/test_engine.py": "def test_engine(): pass\n",
                "tests/fixtures/nested/case.json": '{"case": 1}\n',
                "benchmark-cases.json": '{"cases": []}\n',
                "artifacts/results.json": '{"acceptance": {"passed": true}}\n',
            }
            for relative, content in files.items():
                (root / relative).write_text(content, encoding="utf-8")

            manifest = build_input_manifest(root)
            first_aggregate = manifest["aggregate_sha256"]

            self.assertEqual(manifest["hash_algorithm"], "sha256")
            self.assertEqual(
                [entry["path"] for entry in manifest["files"]],
                sorted(files),
            )
            self.assertTrue(
                all(
                    not Path(entry["path"]).is_absolute()
                    and re.fullmatch(r"[0-9a-f]{64}", entry["sha256"])
                    for entry in manifest["files"]
                )
            )

            (root / "src" / "engine.py").write_text(
                "engine = 2\n", encoding="utf-8"
            )
            changed_manifest = build_input_manifest(root)

        self.assertNotEqual(
            first_aggregate,
            changed_manifest["aggregate_sha256"],
        )

    def test_bound_json_rejects_content_changed_after_manifest_capture(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "tests").mkdir()
            (root / "artifacts").mkdir()
            (root / "benchmark-cases.json").write_text(
                '{"cases": []}\n', encoding="utf-8"
            )
            results = root / "artifacts" / "results.json"
            results.write_text('{"acceptance": true}\n', encoding="utf-8")
            manifest = build_input_manifest(root)

            self.assertEqual(
                read_bound_json(
                    "artifacts/results.json",
                    manifest,
                    root,
                ),
                {"acceptance": True},
            )

            results.write_text('{"acceptance": false}\n', encoding="utf-8")

            with self.assertRaisesRegex(
                RuntimeError,
                "Input changed after manifest capture",
            ):
                read_bound_json(
                    "artifacts/results.json",
                    manifest,
                    root,
                )
            with self.assertRaisesRegex(
                RuntimeError,
                "inputs changed during the test run",
            ):
                verify_input_manifest(manifest, root)

    def test_live_manifest_binds_repository_lifecycle_inputs(self) -> None:
        manifest = build_input_manifest()
        entries = {
            entry["path"]: entry for entry in manifest["files"]
        }
        required = {
            "<repository>/scripts/_readiness/stage.py",
            (
                "<repository>/.claude/skills/ghm-gate-check/"
                "references/gate-criteria.md"
            ),
            "<repository>/.claude/domain-profile.yaml",
            "<repository>/README.md",
            "<repository>/PRD.md",
            "<repository>/SoT/SoT.UNIQUE_ID_SYSTEM.md",
        }

        self.assertTrue(required <= set(entries))
        for path in required:
            self.assertTrue(entries[path]["exists"])
            self.assertRegex(entries[path]["sha256"], r"^[0-9a-f]{64}$")
        self.assertTrue(
            all(not Path(path).is_absolute() for path in entries)
        )

    def test_input_manifest_fails_closed_without_required_benchmark_inputs(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "tests").mkdir()

            with self.assertRaisesRegex(
                FileNotFoundError,
                "benchmark-cases.json, artifacts/results.json",
            ):
                build_input_manifest(root)

    def test_benchmark_binding_preserves_acceptance_and_corpus_fingerprints(
        self,
    ) -> None:
        acceptance = {
            "passed": False,
            "checks": [{"name": "literal-fidelity", "passed": False}],
        }
        binding = benchmark_binding(
            {
                "schema_version": "1.2",
                "generated_at": "2026-07-23T00:00:00+00:00",
                "benchmark_manifest": {
                    "sha256": "f" * 64,
                    "case_count": 25,
                },
                "acceptance": acceptance,
                "corpora": [
                    {
                        "alias": "zeta",
                        "fingerprint_sha256": "b" * 64,
                        "git_commit": "2" * 40,
                        "source_bytes": 999,
                    },
                    {
                        "alias": "alpha",
                        "fingerprint_sha256": "a" * 64,
                        "git_commit": "1" * 40,
                        "source_bytes": 100,
                    },
                ],
            }
        )

        self.assertTrue(binding["acceptance_present"])
        self.assertEqual(binding["acceptance"], acceptance)
        self.assertEqual(
            binding["benchmark_manifest"]["sha256"],
            "f" * 64,
        )
        self.assertEqual(
            binding["corpus_fingerprints"],
            [
                {
                    "alias": "alpha",
                    "fingerprint_sha256": "a" * 64,
                    "git_commit": "1" * 40,
                },
                {
                    "alias": "zeta",
                    "fingerprint_sha256": "b" * 64,
                    "git_commit": "2" * 40,
                },
            ],
        )

    def test_benchmark_binding_exposes_absent_acceptance_without_inventing_it(
        self,
    ) -> None:
        binding = benchmark_binding({"corpora": []})

        self.assertFalse(binding["acceptance_present"])
        self.assertIsNone(binding["acceptance"])

    def test_benchmark_results_must_bind_the_current_case_manifest(
        self,
    ) -> None:
        manifest = {
            "files": [
                {
                    "path": "src/conformance.py",
                    "sha256": "c" * 64,
                },
                {
                    "path": "benchmark-cases.json",
                    "sha256": "a" * 64,
                }
            ]
        }
        results = {"benchmark_manifest": {"sha256": "a" * 64}}

        verify_benchmark_manifest_binding(results, manifest)

        with self.assertRaisesRegex(
            RuntimeError,
            "not bound to the current case manifest",
        ):
            verify_benchmark_manifest_binding(
                {"benchmark_manifest": {"sha256": "b" * 64}},
                manifest,
            )

    def test_suite_identity_is_order_independent_and_lists_exact_test_ids(
        self,
    ) -> None:
        class ExampleTest(unittest.TestCase):
            def test_alpha(self) -> None:
                pass

            def test_beta(self) -> None:
                pass

        tests = [
            ExampleTest("test_beta"),
            ExampleTest("test_alpha"),
        ]

        identity = suite_identity(tests)
        reversed_identity = suite_identity(list(reversed(tests)))

        self.assertEqual(identity, reversed_identity)
        self.assertEqual(identity["test_count"], 2)
        self.assertEqual(
            identity["test_ids"],
            sorted(test.id() for test in tests),
        )
        self.assertRegex(identity["test_ids_sha256"], r"^[0-9a-f]{64}$")

    def test_issue_details_keep_diagnostics_but_remove_absolute_paths(
        self,
    ) -> None:
        class FailingTest(unittest.TestCase):
            def test_failure(self) -> None:
                pass

        test = FailingTest("test_failure")
        local_path = EXPERIMENT_ROOT / "tests" / "test_failure.py"
        diagnostic = (
            "Traceback (most recent call last):\n"
            f'  File "{local_path}", line 4, in test_failure\n'
            '  File "/opt/python/assertions.py", line 2, in equal\n'
            "AssertionError: expected 1 but received 2; "
            "missing '/private/var/tmp/private-input.json'\n"
        )

        details = issue_details([(test, diagnostic)])

        self.assertEqual(details[0]["test_id"], test.id())
        self.assertIn(
            'File "<experiment>/tests/test_failure.py"',
            details[0]["diagnostic"],
        )
        self.assertIn(
            'File "<external>/assertions.py"',
            details[0]["diagnostic"],
        )
        self.assertIn("AssertionError: expected 1", details[0]["diagnostic"])
        self.assertIn(
            "'<external>/private-input.json'",
            details[0]["diagnostic"],
        )
        self.assertNotIn(str(EXPERIMENT_ROOT), details[0]["diagnostic"])
        self.assertNotIn("/opt/python", details[0]["diagnostic"])
        self.assertNotIn("/private/var", details[0]["diagnostic"])

    def test_repository_commit_is_a_content_identifier_not_a_path(self) -> None:
        commit = repository_commit()

        self.assertRegex(commit, r"^[0-9a-f]{40}$")
        self.assertNotIn("/", commit)

    def test_run_emits_provenance_bindings_in_the_written_artifact(self) -> None:
        class PassingTest(unittest.TestCase):
            def test_passes(self) -> None:
                self.assertTrue(True)

        suite = unittest.TestSuite([PassingTest("test_passes")])
        manifest = {
            "hash_algorithm": "sha256",
            "files": [
                {
                    "path": "artifacts/results.json",
                    "sha256": "b" * 64,
                    "bytes": 10,
                },
                {
                    "path": "benchmark-cases.json",
                    "sha256": "d" * 64,
                    "bytes": 10,
                }
            ],
            "aggregate_sha256": "c" * 64,
        }
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "accuracy-results.json"
            with (
                patch(
                    "run_accuracy_suite.build_input_manifest",
                    return_value=manifest,
                ),
                patch(
                    "run_accuracy_suite.repository_commit",
                    return_value="a" * 40,
                ),
                patch(
                    "run_accuracy_suite.read_bound_json",
                    return_value={
                        "schema_version": "1.2",
                        "benchmark_manifest": {"sha256": "d" * 64},
                        "acceptance": {"passed": True},
                        "corpora": [
                            {
                                "alias": "fixture",
                                "fingerprint_sha256": "d" * 64,
                                "git_commit": "e" * 40,
                            }
                        ],
                    },
                ),
                patch(
                    "run_accuracy_suite.unittest.TestLoader.discover",
                    return_value=suite,
                ),
                patch("run_accuracy_suite.load_packs", return_value={}),
                patch(
                    "run_accuracy_suite.audit_repository_lifecycle",
                    return_value=[],
                ),
            ):
                payload = run(output)
            written = json.loads(output.read_text(encoding="utf-8"))

        self.assertEqual(written, payload)
        self.assertEqual(payload["provenance"]["repository_commit"], "a" * 40)
        self.assertEqual(payload["provenance"]["inputs"], manifest)
        self.assertEqual(payload["provenance"]["suite"]["test_count"], 1)
        self.assertEqual(
            payload["provenance"]["suite"]["test_ids"],
            [PassingTest("test_passes").id()],
        )
        self.assertIn(
            "corpus_fingerprints",
            payload["provenance"]["benchmark_results"],
        )
        self.assertIn(
            "acceptance",
            payload["provenance"]["benchmark_results"],
        )
        self.assertEqual(payload["test_run"]["failure_details"], [])
        self.assertEqual(payload["test_run"]["error_details"], [])
        self.assertTrue(
            payload["interpretation_contract"][
                "freshness_policy_declaration_and_projection_tested"
            ]
        )
        self.assertFalse(
            payload["interpretation_contract"][
                "freshness_policy_enforcement_tested"
            ]
        )
        self.assertNotIn(str(EXPERIMENT_ROOT), json.dumps(payload))


if __name__ == "__main__":
    unittest.main()
