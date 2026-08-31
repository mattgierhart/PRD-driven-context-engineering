from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))

from report import render_report  # noqa: E402


class ReportAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = json.loads(
            (EXPERIMENT_ROOT / "artifacts" / "results.json").read_text(
                encoding="utf-8"
            )
        )
        accuracy = cls.result.setdefault("accuracy_dimensions", {})
        legacy = accuracy.pop("lifecycle_source_fidelity", None)
        accuracy.setdefault(
            "lifecycle_manifest_coverage",
            legacy
            or {
                "expected_stages": [],
                "covered_stages": [],
                "complete": False,
            },
        )
        accuracy.setdefault("source_fidelity", {})["description"] = (
            "Literal ID-set fidelity to manifest-authored Markdown spans; "
            "not semantic truth."
        )

    def test_report_uses_lifecycle_manifest_coverage(self) -> None:
        result = copy.deepcopy(self.result)
        result["acceptance"] = {
            "passed": True,
            "checks": {"source_fidelity": {"passed": True}},
        }

        rendered = render_report(result)

        self.assertIn("Lifecycle manifest + gate conformance", rendered)
        self.assertIn("Markdown wins this round.", rendered)
        self.assertIn(
            "Latest-visible evidence precedence", rendered
        )
        self.assertIn(
            "TTL expiry and scheduled re-review are not implemented", rendered
        )
        self.assertNotIn("independently checked", rendered)

    def test_failed_acceptance_withholds_positive_architecture_decision(
        self,
    ) -> None:
        result = copy.deepcopy(self.result)
        result["acceptance"] = {
            "passed": False,
            "checks": {"source_fidelity": {"passed": False}},
        }
        result["decision"]["measured"] = (
            "Benchmark acceptance failed; resolve the evidence gaps."
        )

        rendered = render_report(result)

        self.assertIn("Benchmark acceptance failed.", rendered)
        self.assertIn("Withhold the architecture decision.", rendered)
        self.assertIn("No decision passes the evidence gate.", rendered)
        self.assertNotIn("Markdown wins this round.", rendered)
        self.assertNotIn("<h2>Keep Markdown as the SoT.</h2>", rendered)


if __name__ == "__main__":
    unittest.main()
