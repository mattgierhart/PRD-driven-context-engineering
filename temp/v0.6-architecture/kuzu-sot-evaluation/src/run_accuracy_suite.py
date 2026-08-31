#!/usr/bin/env python3
"""Run the deterministic accuracy suite and emit machine-readable evidence."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = EXPERIMENT_ROOT.parents[2]
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT))

from conformance import load_packs, schema_projection  # noqa: E402
from lifecycle_audit import (  # noqa: E402
    _load_gate_requirements,
    audit_repository_lifecycle,
)


LIFECYCLE_INPUTS = (
    "scripts/_readiness/stage.py",
    ".claude/skills/ghm-gate-check/references/gate-criteria.md",
    ".claude/domain-profile.yaml",
    "README.md",
    "PRD.md",
    "SoT/SoT.UNIQUE_ID_SYSTEM.md",
)


def iter_tests(suite: unittest.TestSuite) -> Iterable[unittest.TestCase]:
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from iter_tests(item)
        else:
            yield item


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _manifest_paths(root: Path) -> list[Path]:
    paths = [
        *root.glob("src/*.py"),
        *root.glob("tests/*.py"),
        *root.glob("tests/fixtures/**/*"),
        root / "benchmark-cases.json",
        root / "artifacts" / "results.json",
    ]
    files = sorted(
        {path for path in paths if path.is_file()},
        key=lambda path: path.relative_to(root).as_posix(),
    )
    required = (
        root / "benchmark-cases.json",
        root / "artifacts" / "results.json",
    )
    missing = [
        path.relative_to(root).as_posix()
        for path in required
        if not path.is_file()
    ]
    if missing:
        raise FileNotFoundError(
            "Required accuracy-suite input missing: " + ", ".join(missing)
        )
    return files


def _repository_lifecycle_inputs(repo: Path) -> list[str]:
    stage_relative = "scripts/_readiness/stage.py"
    stage_path = repo / stage_relative
    requirements = _load_gate_requirements(stage_path)
    relative_paths = set(LIFECYCLE_INPUTS)
    relative_paths.update(
        relative
        for config in requirements.values()
        for relative in config.get("relevant_sots", ())
    )
    return sorted(relative_paths)


def build_input_manifest(root: Path = EXPERIMENT_ROOT) -> dict:
    """Hash experiment inputs and the live lifecycle contract it audits."""

    entries = [
        {
            "path": path.relative_to(root).as_posix(),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        }
        for path in _manifest_paths(root)
    ]
    if root.resolve() == EXPERIMENT_ROOT.resolve():
        for relative in _repository_lifecycle_inputs(REPO_ROOT):
            path = REPO_ROOT / relative
            exists = path.is_file()
            entries.append(
                {
                    "path": f"<repository>/{relative}",
                    "exists": exists,
                    "sha256": sha256_file(path) if exists else None,
                    "bytes": path.stat().st_size if exists else 0,
                }
            )
    entries.sort(key=lambda entry: entry["path"])
    canonical = json.dumps(
        entries,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return {
        "hash_algorithm": "sha256",
        "files": entries,
        "aggregate_sha256": sha256_bytes(canonical),
    }


def read_bound_json(
    relative_path: str,
    manifest: dict,
    root: Path = EXPERIMENT_ROOT,
) -> dict:
    """Read JSON only when its consumed bytes match the input manifest."""

    matches = [
        entry
        for entry in manifest.get("files", [])
        if entry.get("path") == relative_path
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Input manifest must contain exactly one {relative_path} entry"
        )
    content = (root / relative_path).read_bytes()
    if sha256_bytes(content) != matches[0].get("sha256"):
        raise RuntimeError(
            f"Input changed after manifest capture: {relative_path}"
        )
    decoded = json.loads(content)
    if not isinstance(decoded, dict):
        raise TypeError(f"Expected a JSON object in {relative_path}")
    return decoded


def verify_input_manifest(
    expected: dict,
    root: Path = EXPERIMENT_ROOT,
) -> None:
    """Fail closed if any declared input changes while tests are running."""

    observed = build_input_manifest(root)
    if observed != expected:
        raise RuntimeError("Accuracy-suite inputs changed during the test run")


def verify_benchmark_manifest_binding(
    results: dict,
    input_manifest: dict,
) -> None:
    """Require benchmark results to name the exact case-manifest bytes."""

    entries = [
        entry
        for entry in input_manifest.get("files", [])
        if entry.get("path") == "benchmark-cases.json"
    ]
    if len(entries) != 1:
        raise RuntimeError(
            "Input manifest must contain exactly one benchmark-cases.json entry"
        )
    recorded = results.get("benchmark_manifest", {}).get("sha256")
    if not recorded or recorded != entries[0].get("sha256"):
        raise RuntimeError(
            "Benchmark results are not bound to the current case manifest"
        )


def repository_commit(repository_root: Path = REPO_ROOT) -> str:
    """Return the containing repository commit without emitting its local path."""

    return subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def suite_identity(tests: Sequence[unittest.TestCase]) -> dict:
    test_ids = sorted(test.id() for test in tests)
    canonical = ("\n".join(test_ids) + "\n").encode("utf-8")
    return {
        "framework": "unittest",
        "discovery": {
            "start_directory": "tests",
            "pattern": "test*.py",
        },
        "test_count": len(test_ids),
        "test_ids": test_ids,
        "test_ids_sha256": sha256_bytes(canonical),
    }


def _relative_frame_path(raw_path: str) -> str:
    path = Path(raw_path)
    for root, label in (
        (EXPERIMENT_ROOT, "<experiment>"),
        (REPO_ROOT, "<repository>"),
    ):
        try:
            relative = path.resolve().relative_to(root.resolve())
        except ValueError:
            continue
        return f"{label}/{relative.as_posix()}"
    return f"<external>/{path.name}"


def sanitize_diagnostic(diagnostic: str) -> str:
    """Preserve actionable failures without leaking machine-specific paths."""

    frame_pattern = re.compile(r'File "([^"]+)"')
    sanitized = frame_pattern.sub(
        lambda match: f'File "{_relative_frame_path(match.group(1))}"',
        diagnostic,
    )
    for root, label in (
        (EXPERIMENT_ROOT, "<experiment>"),
        (REPO_ROOT, "<repository>"),
    ):
        sanitized = sanitized.replace(str(root), label)
    quoted_path_pattern = re.compile(
        r"""(?P<quote>["'])(?P<path>/[^"'\n]+)(?P=quote)"""
    )
    sanitized = quoted_path_pattern.sub(
        lambda match: (
            f"{match.group('quote')}"
            f"{_relative_frame_path(match.group('path'))}"
            f"{match.group('quote')}"
        ),
        sanitized,
    )
    return sanitized


def issue_details(
    issues: Sequence[tuple[unittest.TestCase, str]],
) -> list[dict[str, str]]:
    return [
        {
            "test_id": test.id(),
            "diagnostic": sanitize_diagnostic(diagnostic),
        }
        for test, diagnostic in issues
    ]


def benchmark_binding(results: dict) -> dict:
    """Copy benchmark conclusions needed to interpret this accuracy run."""

    corpus_fingerprints = [
        {
            "alias": corpus.get("alias"),
            "fingerprint_sha256": corpus.get("fingerprint_sha256"),
            "git_commit": corpus.get("git_commit"),
        }
        for corpus in results.get("corpora", [])
    ]
    corpus_fingerprints.sort(key=lambda corpus: str(corpus["alias"]))
    return {
        "schema_version": results.get("schema_version"),
        "generated_at": results.get("generated_at"),
        "benchmark_manifest": results.get("benchmark_manifest"),
        "corpus_fingerprints": corpus_fingerprints,
        "acceptance_present": "acceptance" in results,
        "acceptance": results.get("acceptance"),
    }


def run(output: Path) -> dict:
    input_manifest = build_input_manifest()
    benchmark_results = read_bound_json(
        "artifacts/results.json",
        input_manifest,
    )
    verify_benchmark_manifest_binding(
        benchmark_results,
        input_manifest,
    )
    root_commit = repository_commit()
    loader = unittest.TestLoader()
    suite = loader.discover(str(EXPERIMENT_ROOT / "tests"))
    tests = list(iter_tests(suite))
    by_module = Counter(test.__class__.__module__ for test in tests)
    identity = suite_identity(tests)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    packs = load_packs(
        EXPERIMENT_ROOT
        / "tests"
        / "fixtures"
        / "conformance"
        / "packs.json"
    )
    lifecycle_findings = audit_repository_lifecycle(REPO_ROOT)
    verify_input_manifest(input_manifest)
    if repository_commit() != root_commit:
        raise RuntimeError("Repository commit changed during the test run")
    payload = {
        "schema_version": "0.2",
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "purpose": (
            "Deterministic accuracy evidence kept separate from latency and "
            "storage benchmark scores."
        ),
        "provenance": {
            "repository_commit": root_commit,
            "repository_commit_verified_after_test_run": True,
            "inputs": input_manifest,
            "inputs_verified_after_test_run": True,
            "suite": identity,
            "benchmark_results": benchmark_binding(benchmark_results),
        },
        "test_run": {
            "command": (
                ".venv/bin/python src/run_accuracy_suite.py "
                "--output artifacts/accuracy-results.json"
            ),
            "tests_run": result.testsRun,
            "passed": result.testsRun
            - len(result.failures)
            - len(result.errors)
            - len(result.skipped),
            "failures": len(result.failures),
            "errors": len(result.errors),
            "skipped": len(result.skipped),
            "successful": result.wasSuccessful(),
            "tests_by_module": dict(sorted(by_module.items())),
            "failure_details": issue_details(result.failures),
            "error_details": issue_details(result.errors),
        },
        "dimensions": {
            "source_fidelity": {
                "test_module": "test_sot_benchmark",
                "scope": "parser, retrieval parity, lifecycle manifest, staleness",
            },
            "semantic_truth": {
                "scope": (
                    "Two seeded deterministic detectors in benchmark results; "
                    "broad blind evaluation is not implemented."
                )
            },
            "epistemic_conformance": {
                "test_module": "test_conformance",
                "scope": (
                    "identity, provenance, lifecycle, bitemporality, "
                    "supersession, gates, evidence boundary, pack detectors"
                ),
            },
            "lifecycle_conformance": {
                "test_module": "test_lifecycle_audit",
                "scope": (
                    "gate count baseline, inactive-ID false pass, and "
                    "cross-artifact contract consistency"
                ),
            },
        },
        "pack_fixture_notice": (
            "JSON is test-fixture serialization only, not a product-format decision."
        ),
        "pack_schema_projections": {
            pack_id: {
                "version": pack.version,
                "core_version": pack.core_version,
                "projection_sha256": schema_projection(pack)["projection_sha256"],
                "assertion_types": len(pack.entity_types),
                "evidence_only_types": len(pack.evidence_types),
            }
            for pack_id, pack in sorted(packs.items())
        },
        "repository_lifecycle_contract_findings": [
            finding.to_dict() for finding in lifecycle_findings
        ],
        "interpretation_contract": {
            "no_blended_accuracy_score": True,
            "repo_contract_findings_are_diagnostics_not_silenced": True,
            "draft_core_pack_design_not_promoted_to_canonical_methodology": True,
            "product_repositories_modified": False,
            "blind_llm_evaluation_performed": False,
            "human_adjudication_performed": False,
            "freshness_policy_declaration_and_projection_tested": True,
            "freshness_policy_enforcement_tested": False,
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    payload = run(output)
    try:
        displayed_output = output.relative_to(EXPERIMENT_ROOT).as_posix()
    except ValueError:
        displayed_output = output.name
    print(
        json.dumps(
            {
                "output": displayed_output,
                "test_run": payload["test_run"],
                "lifecycle_contract_findings": len(
                    payload["repository_lifecycle_contract_findings"]
                ),
            },
            indent=2,
        )
    )
    return 0 if payload["test_run"]["successful"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
