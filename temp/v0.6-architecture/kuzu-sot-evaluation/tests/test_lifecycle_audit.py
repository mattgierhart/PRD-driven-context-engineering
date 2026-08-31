from __future__ import annotations

import ast
import datetime as dt
import re
import sys
import tempfile
import unittest
from pathlib import Path

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = EXPERIMENT_ROOT.parents[2]
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT))

from conformance import (  # noqa: E402
    AssertionRevision,
    GateVerdict,
    Provenance,
    ScopedId,
    Snapshot,
    evaluate_gate,
    load_packs,
)
from lifecycle_audit import (  # noqa: E402
    _load_gate_requirements,
    audit_repository_lifecycle,
)


STAGE_PATH = REPO_ROOT / "scripts" / "_readiness" / "stage.py"
GATE_REQUIREMENTS = _load_gate_requirements(STAGE_PATH)


def load_current_counter_functions():
    """Load two pure functions from stage.py without its optional YAML dependency."""

    tree = ast.parse(STAGE_PATH.read_text(encoding="utf-8"))
    selected = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"index_all_ids", "compute_required_ids_present"}
    ]
    namespace = {
        "Path": Path,
        "re": re,
        "HEADING_DEF_RE": re.compile(r"^#{2,3}\s+([A-Z]{2,5}-\d{2,3})\b"),
    }
    exec(compile(ast.Module(selected, type_ignores=[]), str(STAGE_PATH), "exec"), namespace)
    return namespace["index_all_ids"], namespace["compute_required_ids_present"]


class LifecycleContractAuditTests(unittest.TestCase):
    def test_contradictory_contract_fixture_reports_each_supported_diagnostic(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "scripts" / "_readiness").mkdir(parents=True)
            (
                repo
                / ".claude"
                / "skills"
                / "ghm-gate-check"
                / "references"
            ).mkdir(parents=True)
            (repo / "SoT").mkdir()

            (repo / "scripts" / "_readiness" / "stage.py").write_text(
                """GATE_REQUIREMENTS: dict = {
    "v0.5": {
        "name": "Journey Design",
        "required_prefixes": {"UJ": 1},
        "relevant_sots": ["SoT/SoT.USER_JOURNEYS.md"],
    },
    "v0.6": {
        "name": "Architecture",
        "required_prefixes": {"RISK": 1},
        "relevant_sots": ["SoT/SoT.RISKS.md"],
    },
    "v1.0": {
        "name": "Launch Readiness",
        "required_prefixes": {"GTM": 1},
        "relevant_sots": [],
    },
}
""",
                encoding="utf-8",
            )
            (
                repo
                / ".claude"
                / "skills"
                / "ghm-gate-check"
                / "references"
                / "gate-criteria.md"
            ).write_text(
                """# Gate criteria

## v0.4 → v0.5 Gate

**Screen coverage** (SCR)
""",
                encoding="utf-8",
            )
            (repo / ".claude" / "domain-profile.yaml").write_text(
                """prefixes:
  RISK: { file: "SoT/SoT.BUSINESS_RULES.md" }
  ADO: { file: "SoT/SoT.ADOPTION.md" }
""",
                encoding="utf-8",
            )
            (repo / "README.md").write_text(
                """# Contradictory methodology fixture

| Stage | Description |
|---|---|
| **v0.2** | Business Rules created as BR-001 |
| **v1.0** | Market Adoption evidenced by ADO-001 |
""",
                encoding="utf-8",
            )
            (repo / "PRD.md").write_text(
                "# PRD\n\nThe lifecycle ends at v1.0 Market Adoption.\n",
                encoding="utf-8",
            )
            (repo / "SoT" / "SoT.UNIQUE_ID_SYSTEM.md").write_text(
                """# ID registry

| Prefix | Meaning | Created |
|---|---|---|
| **BR** | Business rule | v0.6 |
""",
                encoding="utf-8",
            )
            (repo / "SoT" / "SoT.USER_JOURNEYS.md").write_text(
                "# Journeys\n", encoding="utf-8"
            )

            findings = audit_repository_lifecycle(repo)

        codes = {finding.code for finding in findings}

        self.assertIn("LIFECYCLE_GATE_REQUIREMENT_GAP", codes)
        self.assertIn("LIFECYCLE_RELEVANT_SOURCE_MISSING", codes)
        self.assertIn("LIFECYCLE_OWNER_CONFLICT", codes)
        self.assertIn("LIFECYCLE_PREFIX_STAGE_CONFLICT", codes)
        self.assertIn("LIFECYCLE_TARGET_NAME_CONFLICT", codes)
        self.assertIn("LIFECYCLE_ADOPTION_UNGATED", codes)
        screen_gap = [
            finding
            for finding in findings
            if finding.code == "LIFECYCLE_GATE_REQUIREMENT_GAP"
            and finding.refs[:2] == ("v0.5", "SCR")
        ]
        self.assertEqual(len(screen_gap), 1)

    def test_current_repository_audit_is_deterministic_sorted_and_structured(
        self,
    ) -> None:
        first = audit_repository_lifecycle(REPO_ROOT)
        second = audit_repository_lifecycle(REPO_ROOT)

        self.assertEqual(first, second)
        self.assertEqual(first, tuple(sorted(first)))
        for finding in first:
            self.assertIsInstance(finding.code, str)
            self.assertTrue(finding.code)
            self.assertIsInstance(finding.refs, tuple)
            self.assertIsInstance(finding.message, str)
            self.assertTrue(finding.message)

    def test_gate_requirements_snapshot_detects_intentional_contract_changes(
        self,
    ) -> None:
        """Fail deliberately when executable lifecycle counts change.

        This is a change-detection snapshot, not a claim that the frozen counts
        are intrinsically correct. Update it only after reviewing a deliberate
        lifecycle-contract change.
        """

        expected = {
            "v0.2": {"CFD": 3},
            "v0.3": {"CFD": 3, "BR": 1},
            "v0.4": {"BR": 3, "KPI": 1, "CFD": 5, "FEA": 1},
            "v0.5": {"PER": 1, "UJ": 3},
            "v0.6": {"RISK": 5, "TECH": 3},
            "v0.7": {"ARC": 1, "API": 1, "DBT": 1},
            "v0.8": {"EPIC": 1, "TEST": 1},
            "v0.9": {"DEP": 1, "RUN": 1, "MON": 1},
            "v1.0": {"GTM": 1, "KPI": 3},
        }

        self.assertEqual(
            {
                target: config["required_prefixes"]
                for target, config in GATE_REQUIREMENTS.items()
            },
            expected,
        )

    def test_current_counter_can_false_pass_on_inactive_ids(self) -> None:
        index_all_ids, compute_required_ids_present = load_current_counter_functions()
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            (repo / "SoT").mkdir()
            (repo / "PRD.md").write_text("# PRD\n", encoding="utf-8")
            (repo / "README.md").write_text("# README\n", encoding="utf-8")
            (repo / "SoT" / "SoT.USER_JOURNEYS.md").write_text(
                """# Journeys

## PER-001: Active persona
**Status**: Active

## UJ-001: Superseded journey
**Status**: Superseded

## UJ-002: Rejected journey
**Status**: Void

## UJ-003: Draft journey
**Status**: Draft
""",
                encoding="utf-8",
            )
            index = index_all_ids(repo)
            score, blockers = compute_required_ids_present(
                GATE_REQUIREMENTS["v0.5"], index
            )

        product = load_packs(
            EXPERIMENT_ROOT
            / "tests"
            / "fixtures"
            / "conformance"
            / "packs.json"
        )["product"]
        instant = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
        provenance = Provenance(
            "tester", "status-counter-differential", "fixture", "f" * 64
        )
        statuses = {
            "PER-001": ("Persona", "accepted"),
            "UJ-001": ("Journey", "retired"),
            "UJ-002": ("Journey", "rejected"),
            "UJ-003": ("Journey", "proposed"),
        }
        strict_snapshot = Snapshot(
            tuple(
                AssertionRevision(
                    id=ScopedId("product", local_id),
                    revision=1,
                    entity_type=entity_type,
                    truth_key=local_id,
                    local_status=status,
                    valid_from="v0.1",
                    valid_to="v0.4" if status == "retired" else None,
                    transaction_from=instant,
                    transaction_to=None,
                    provenance=provenance,
                )
                for local_id, (entity_type, status) in statuses.items()
            )
        )
        strict = evaluate_gate(
            strict_snapshot,
            product,
            "v0.5",
            "v0.5",
            instant,
        )

        self.assertEqual(score, 100.0)
        self.assertEqual(blockers, [])
        self.assertEqual(strict.verdict, GateVerdict.BLOCK)


if __name__ == "__main__":
    unittest.main()
