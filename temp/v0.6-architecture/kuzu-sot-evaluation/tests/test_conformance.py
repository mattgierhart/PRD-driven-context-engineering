from __future__ import annotations

import dataclasses
import datetime as dt
import sys
import unittest
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

EXPERIMENT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXPERIMENT_ROOT / "src"))

from conformance import (  # noqa: E402
    ALLOWED_TRANSITIONS,
    CORE_FIELD_NAMES,
    AssertionKind,
    AssertionRevision,
    ConformanceError,
    EdgeRequirement,
    EntityTypeSpec,
    EvidenceEvent,
    FieldRequirement,
    GateAttestation,
    GateVerdict,
    MetaStatus,
    Provenance,
    Relation,
    SchemaPack,
    ScopedId,
    Snapshot,
    current_truth,
    evaluate_gate,
    load_packs,
    resolve_prefix,
    run_conformance,
    run_pack_detectors,
    schema_projection,
    validate_evidence,
    validate_ids,
    validate_lifecycle,
    validate_packs,
    validate_provenance,
    validate_rejected_alternatives,
    validate_relations,
    validate_revision_intervals,
    validate_supersession,
    validate_truth_uniqueness,
)


UTC = dt.timezone.utc
T0 = dt.datetime(2026, 1, 1, tzinfo=UTC)
T1 = dt.datetime(2026, 2, 1, tzinfo=UTC)
T2 = dt.datetime(2026, 3, 1, tzinfo=UTC)
T3 = dt.datetime(2026, 4, 1, tzinfo=UTC)
PACK_FIXTURE = (
    EXPERIMENT_ROOT / "tests" / "fixtures" / "conformance" / "packs.json"
)


class ConformanceOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.packs = load_packs(PACK_FIXTURE)
        cls.product = cls.packs["product"]
        cls.accounting = cls.packs["accounting"]
        cls.restaurant = cls.packs["restaurant"]

    def provenance(self, suffix: str = "fixture") -> Provenance:
        return Provenance(
            actor="test-author",
            activity="accuracy-suite",
            source_ref=f"tests/{suffix}.json#assertion",
            source_hash="a" * 64,
        )

    def revision(
        self,
        pack: SchemaPack,
        local_id: str,
        entity_type: str,
        *,
        revision: int = 1,
        truth_key: str | None = None,
        status: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        transaction_from: dt.datetime = T0,
        transaction_to: dt.datetime | None = None,
        supersedes: ScopedId | None = None,
        invalidated_by: ScopedId | None = None,
        rejected_alternatives: tuple[ScopedId, ...] = (),
        attributes: Mapping[str, Any] | None = None,
        provenance: Provenance | None = None,
    ) -> AssertionRevision:
        default_status = {
            "product": "accepted",
            "accounting": "effective",
            "restaurant": "approved",
        }.get(pack.pack_id, next(iter(pack.status_map)))
        if valid_from is None:
            valid_from = (
                "v0.1"
                if pack.valid_clock == "prd_version"
                else "2026-01-01T00:00:00Z"
            )
        return AssertionRevision(
            id=ScopedId(pack.pack_id, local_id),
            revision=revision,
            entity_type=entity_type,
            truth_key=truth_key or local_id,
            local_status=status or default_status,
            valid_from=valid_from,
            valid_to=valid_to,
            transaction_from=transaction_from,
            transaction_to=transaction_to,
            supersedes=supersedes,
            invalidated_by=invalidated_by,
            rejected_alternatives=rejected_alternatives,
            provenance=provenance or self.provenance(),
            attributes=attributes or {},
        )

    def test_fixture_packs_are_valid_and_cover_three_verticals(self) -> None:
        self.assertEqual(set(self.packs), {"product", "accounting", "restaurant"})
        self.assertEqual(validate_packs(self.packs.values()), ())
        self.assertIn("JournalEntry", self.accounting.evidence_types)
        self.assertIn("POSSale", self.restaurant.evidence_types)
        self.assertIn("GitCommit", self.product.evidence_types)

    def test_schema_projection_injects_core_fields_deterministically(self) -> None:
        first = schema_projection(self.product)
        second = schema_projection(self.product)

        self.assertEqual(first, second)
        for table in first["assertion_tables"]:
            self.assertTrue(CORE_FIELD_NAMES.issubset(table["fields"]))
        journal_tables = {
            table["name"] for table in schema_projection(self.accounting)["evidence_tables"]
        }
        product_projection = schema_projection(self.product)
        self.assertIn("JournalEntry", journal_tables)
        self.assertNotIn(
            "JournalEntry",
            {table["name"] for table in schema_projection(self.accounting)["assertion_tables"]},
        )
        self.assertEqual(
            {
                "uses-screen",
                "uses-api",
                "verifies",
            },
            {
                table["name"]
                for table in product_projection["relation_tables"]
            },
        )
        for table in product_projection["evidence_tables"]:
            self.assertTrue(
                {"evidence_type", "effect", "measurements"}
                <= set(table["fields"])
            )
        self.assertEqual(
            product_projection["detectors"], ["product-change-review"]
        )
        self.assertEqual(product_projection["freshness_days"]["Risk"], 90)

    def test_pack_cannot_shadow_core_fields_or_weaken_status_map(self) -> None:
        shadowed_entity = dataclasses.replace(
            self.product.entity_types["BusinessRule"],
            custom_fields=("transaction_from",),
        )
        shadowed = dataclasses.replace(
            self.product,
            entity_types={**self.product.entity_types, "BusinessRule": shadowed_entity},
        )
        incomplete = dataclasses.replace(
            self.accounting,
            status_map={
                key: value
                for key, value in self.accounting.status_map.items()
                if value is not MetaStatus.VOID
            },
        )

        codes = {
            finding.code for finding in validate_packs((shadowed, incomplete))
        }
        self.assertIn("CORE_FIELD_SHADOWED", codes)
        self.assertIn("CORE_STATUS_MAP_INCOMPLETE", codes)

    def test_pack_gate_and_detector_declarations_fail_closed(self) -> None:
        invalid_gate = dataclasses.replace(
            self.product.gates["v0.2"],
            target="not-a-version",
            minimum_prefix_counts={"UNKNOWN": 0},
            prefix_aliases={"UNKNOWN": ()},
            required_fields=(FieldRequirement("CFD", "not_a_field"),),
            required_edges=(
                EdgeRequirement("CFD", "not-a-relation", "BR"),
            ),
            manual_checks=("", ""),
        )
        invalid = dataclasses.replace(
            self.product,
            detectors=(
                "product-change-review",
                "product-change-review",
                "not-registered",
            ),
            gates={"v0.2": invalid_gate},
        )

        codes = {finding.code for finding in validate_packs((invalid,))}

        self.assertTrue(
            {
                "CORE_DETECTOR_DUPLICATE",
                "CORE_DETECTOR_UNKNOWN",
                "CORE_GATE_TARGET_MISMATCH",
                "CORE_GATE_COUNT_SPEC_INVALID",
                "CORE_GATE_PREFIX_ALIAS_INVALID",
                "CORE_GATE_FIELD_SPEC_INVALID",
                "CORE_GATE_EDGE_SPEC_INVALID",
                "CORE_GATE_MANUAL_CHECK_INVALID",
            }
            <= codes
        )

    def test_scoped_identity_and_longest_compound_prefix(self) -> None:
        self.assertEqual(
            resolve_prefix(self.product, "ADO-STAGE-001"), "ADO"
        )
        product_id = ScopedId("product", "BR-001")
        alternate_pack = dataclasses.replace(
            self.accounting,
            pack_id="policy-lab",
            entity_types={
                "BusinessRule": EntityTypeSpec(
                    "BusinessRule",
                    "BR",
                    AssertionKind.POLICY,
                    r"BR-\d{3}",
                )
            },
        )
        policy_id = ScopedId(alternate_pack.pack_id, "BR-001")
        snapshot = Snapshot(
            (
                self.revision(self.product, "BR-001", "BusinessRule"),
                self.revision(alternate_pack, "BR-001", "BusinessRule"),
            )
        )

        self.assertNotEqual(product_id, policy_id)
        self.assertEqual(
            validate_ids(
                snapshot,
                {self.product.pack_id: self.product, alternate_pack.pack_id: alternate_pack},
            ),
            (),
        )
        with self.assertRaisesRegex(ConformanceError, "CORE_ID_PREFIX_UNKNOWN"):
            resolve_prefix(self.product, "UNKNOWN-001")
        with self.assertRaisesRegex(ConformanceError, "CORE_ID_FORMAT_INVALID"):
            resolve_prefix(self.product, "BR-garbage")

    def test_lifecycle_transition_matrix(self) -> None:
        inverse = {
            MetaStatus.DRAFT: "proposed",
            MetaStatus.ACTIVE: "accepted",
            MetaStatus.SUPERSEDED: "retired",
            MetaStatus.EXPIRED: "expired",
            MetaStatus.VOID: "rejected",
        }
        all_statuses = tuple(MetaStatus)
        for before in all_statuses:
            for after in all_statuses:
                first = self.revision(
                    self.product,
                    "BR-001",
                    "BusinessRule",
                    revision=1,
                    status=inverse[before],
                    valid_to=(
                        "v0.9"
                        if before in {MetaStatus.SUPERSEDED, MetaStatus.EXPIRED}
                        else None
                    ),
                    transaction_from=T0,
                    transaction_to=T1,
                )
                second = self.revision(
                    self.product,
                    "BR-001",
                    "BusinessRule",
                    revision=2,
                    status=inverse[after],
                    valid_to=(
                        "v0.9"
                        if after in {MetaStatus.SUPERSEDED, MetaStatus.EXPIRED}
                        else None
                    ),
                    transaction_from=T1,
                )
                findings = validate_lifecycle(
                    Snapshot((first, second)), {"product": self.product}
                )
                expected_valid = after in ALLOWED_TRANSITIONS[before]
                with self.subTest(before=before.value, after=after.value):
                    self.assertEqual(findings == (), expected_valid)

    def supersession_snapshot(self) -> Snapshot:
        old_id = ScopedId("product", "ARC-001")
        new_id = ScopedId("product", "ARC-002")
        return Snapshot(
            (
                self.revision(
                    self.product,
                    "ARC-001",
                    "ArchitectureDecision",
                    revision=1,
                    truth_key="request-handling",
                    status="accepted",
                    valid_from="v0.6",
                    transaction_from=T0,
                    transaction_to=T2,
                ),
                self.revision(
                    self.product,
                    "ARC-001",
                    "ArchitectureDecision",
                    revision=2,
                    truth_key="request-handling",
                    status="retired",
                    valid_from="v0.6",
                    valid_to="v0.7",
                    transaction_from=T2,
                    invalidated_by=new_id,
                ),
                self.revision(
                    self.product,
                    "ARC-002",
                    "ArchitectureDecision",
                    truth_key="request-handling",
                    status="accepted",
                    valid_from="v0.7",
                    transaction_from=T2,
                    supersedes=old_id,
                ),
            )
        )

    def test_bitemporal_current_truth_and_half_open_boundaries(self) -> None:
        snapshot = self.supersession_snapshot()

        believed_then = current_truth(
            snapshot, self.product, "request-handling", "v0.7", T1
        )
        known_later = current_truth(
            snapshot, self.product, "request-handling", "v0.7", T3
        )
        exact_transaction_boundary = current_truth(
            snapshot, self.product, "request-handling", "v0.7", T2
        )
        old_side_of_valid_boundary = current_truth(
            snapshot, self.product, "request-handling", "v0.6", T3
        )

        self.assertEqual(believed_then.id.local_id, "ARC-001")
        self.assertEqual(known_later.id.local_id, "ARC-002")
        self.assertEqual(exact_transaction_boundary.id.local_id, "ARC-002")
        self.assertEqual(old_side_of_valid_boundary.id.local_id, "ARC-001")
        self.assertEqual(
            validate_revision_intervals(snapshot, {"product": self.product}), ()
        )
        self.assertEqual(
            validate_supersession(snapshot, {"product": self.product}), ()
        )

    def test_current_truth_fails_closed_on_overlap(self) -> None:
        snapshot = Snapshot(
            (
                self.revision(
                    self.product,
                    "ARC-001",
                    "ArchitectureDecision",
                    truth_key="runtime",
                    valid_from="v0.6",
                ),
                self.revision(
                    self.product,
                    "ARC-002",
                    "ArchitectureDecision",
                    truth_key="runtime",
                    valid_from="v0.6",
                ),
            )
        )

        with self.assertRaisesRegex(ConformanceError, "CORE_TRUTH_AMBIGUOUS"):
            current_truth(snapshot, self.product, "runtime", "v0.7", T1)

    def test_gate_blocks_overlapping_single_current_truths(self) -> None:
        assertions = tuple(
            self.revision(
                self.product,
                f"CFD-{number:03d}",
                "CustomerEvidence",
                truth_key="same-market-signal",
                attributes={"evidence_tier": "Tier 1"},
            )
            for number in range(1, 4)
        )
        snapshot = Snapshot(assertions)
        attestations = tuple(
            GateAttestation(
                gate="v0.2",
                check_id=check_id,
                passed=True,
                assertion_refs=(assertions[0].id,),
                provenance=self.provenance(check_id),
                recorded_at=T0,
            )
            for check_id in self.product.gates["v0.2"].manual_checks
        )

        with self.assertRaisesRegex(
            ConformanceError, "CORE_TRUTH_AMBIGUOUS"
        ):
            current_truth(
                snapshot,
                self.product,
                "same-market-signal",
                "v0.2",
                T1,
            )
        uniqueness = validate_truth_uniqueness(
            snapshot,
            {"product": self.product},
        )
        report = evaluate_gate(
            snapshot,
            self.product,
            "v0.2",
            "v0.2",
            T1,
            attestations,
        )

        self.assertEqual(
            {finding.code for finding in uniqueness},
            {"CORE_TRUTH_INTERVAL_OVERLAP"},
        )
        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertEqual(report.counted_ids, {})
        self.assertIn(
            "CORE_TRUTH_INTERVAL_OVERLAP",
            {finding.code for finding in report.findings},
        )

    def test_singular_truth_query_rejects_multi_current_cardinality(
        self,
    ) -> None:
        multi_rule = dataclasses.replace(
            self.product.entity_types["BusinessRule"],
            single_current=False,
        )
        multi_pack = dataclasses.replace(
            self.product,
            entity_types={
                **self.product.entity_types,
                "BusinessRule": multi_rule,
            },
        )
        snapshot = Snapshot(
            (
                self.revision(
                    multi_pack,
                    "BR-001",
                    "BusinessRule",
                    truth_key="compatible-policies",
                ),
                self.revision(
                    multi_pack,
                    "BR-002",
                    "BusinessRule",
                    truth_key="compatible-policies",
                ),
            )
        )

        self.assertEqual(
            validate_truth_uniqueness(
                snapshot,
                {"product": multi_pack},
            ),
            (),
        )
        with self.assertRaisesRegex(
            ConformanceError,
            "CORE_TRUTH_QUERY_CARDINALITY_UNSUPPORTED",
        ):
            current_truth(
                snapshot,
                multi_pack,
                "compatible-policies",
                "v0.3",
                T1,
            )

    def test_invalid_temporal_intervals_and_revision_overlap_are_rejected(
        self,
    ) -> None:
        first = self.revision(
            self.product,
            "ARC-001",
            "ArchitectureDecision",
            revision=1,
            valid_from="v0.8",
            valid_to="v0.7",
            transaction_from=T0,
            transaction_to=T2,
        )
        second = self.revision(
            self.product,
            "ARC-001",
            "ArchitectureDecision",
            revision=2,
            transaction_from=T1,
        )
        empty_transaction = self.revision(
            self.product,
            "ARC-002",
            "ArchitectureDecision",
            transaction_from=T2,
            transaction_to=T1,
        )
        malformed_one_sided = self.revision(
            self.product,
            "ARC-003",
            "ArchitectureDecision",
            valid_from="not-a-version",
            valid_to=None,
        )
        naive_transaction = self.revision(
            self.product,
            "ARC-004",
            "ArchitectureDecision",
            transaction_from=dt.datetime(2026, 1, 1),
        )
        codes = {
            finding.code
            for finding in validate_revision_intervals(
                Snapshot(
                    (
                        first,
                        second,
                        empty_transaction,
                        malformed_one_sided,
                        naive_transaction,
                    )
                ),
                {"product": self.product},
            )
        }

        self.assertIn("CORE_VALID_INTERVAL_INVALID", codes)
        self.assertIn("CORE_TRANSACTION_INTERVAL_INVALID", codes)
        self.assertIn("CORE_TRANSACTION_HISTORY_GAP_OR_OVERLAP", codes)
        self.assertIn("CORE_VALID_POINT_INVALID", codes)
        self.assertIn("CORE_TRANSACTION_TIMEZONE_MISSING", codes)

    def test_revision_identity_cannot_change_entity_type_or_truth_key(
        self,
    ) -> None:
        first = self.revision(
            self.product,
            "BR-001",
            "BusinessRule",
            revision=1,
            truth_key="pricing",
            transaction_from=T0,
            transaction_to=T1,
        )
        drifted = self.revision(
            self.product,
            "BR-001",
            "Metric",
            revision=2,
            truth_key="activation",
            transaction_from=T1,
        )

        codes = {
            finding.code
            for finding in validate_revision_intervals(
                Snapshot((first, drifted)),
                {"product": self.product},
            )
        }

        self.assertIn("CORE_REVISION_IDENTITY_DRIFT", codes)

    def test_expired_truth_is_historical_and_void_truth_is_never_current(
        self,
    ) -> None:
        expired = self.revision(
            self.product,
            "BR-001",
            "BusinessRule",
            truth_key="pricing-rule",
            status="expired",
            valid_from="v0.2",
            valid_to="v0.5",
        )
        void = self.revision(
            self.product,
            "BR-002",
            "BusinessRule",
            truth_key="rejected-pricing-rule",
            status="rejected",
        )
        snapshot = Snapshot((expired, void))

        self.assertEqual(
            current_truth(
                snapshot, self.product, "pricing-rule", "v0.4", T1
            ),
            expired,
        )
        self.assertIsNone(
            current_truth(
                snapshot, self.product, "pricing-rule", "v0.5", T1
            )
        )
        self.assertIsNone(
            current_truth(
                snapshot,
                self.product,
                "rejected-pricing-rule",
                "v0.4",
                T1,
            )
        )

    def test_supersession_mutations_are_detected(self) -> None:
        valid = self.supersession_snapshot()
        old_first, old_latest, new = valid.assertions
        broken = Snapshot(
            (
                old_first,
                dataclasses.replace(old_latest, invalidated_by=None),
                dataclasses.replace(
                    new,
                    truth_key="different-truth",
                    local_status="proposed",
                ),
            )
        )
        codes = {
            finding.code
            for finding in validate_supersession(
                broken, {"product": self.product}
            )
        }

        self.assertIn("CORE_SUPERSESSION_RECIPROCAL_MISSING", codes)
        self.assertIn("CORE_SUPERSESSION_TRUTH_KEY_MISMATCH", codes)
        self.assertIn("CORE_SUPERSESSION_NEW_STATUS_INVALID", codes)

    def test_supersession_cycle_is_rejected(self) -> None:
        first_id = ScopedId("product", "ARC-001")
        second_id = ScopedId("product", "ARC-002")
        snapshot = Snapshot(
            (
                self.revision(
                    self.product,
                    "ARC-001",
                    "ArchitectureDecision",
                    status="retired",
                    truth_key="runtime",
                    valid_to="v0.7",
                    supersedes=second_id,
                    invalidated_by=second_id,
                ),
                self.revision(
                    self.product,
                    "ARC-002",
                    "ArchitectureDecision",
                    status="retired",
                    truth_key="runtime",
                    valid_from="v0.7",
                    valid_to="v0.8",
                    supersedes=first_id,
                    invalidated_by=first_id,
                ),
            )
        )

        codes = {
            finding.code
            for finding in validate_supersession(
                snapshot, {"product": self.product}
            )
        }
        self.assertIn("CORE_SUPERSESSION_CYCLE", codes)

    def test_provenance_is_required_on_every_revision(self) -> None:
        missing = self.revision(
            self.product,
            "BR-001",
            "BusinessRule",
            provenance=Provenance("", "session", "", ""),
        )
        findings = validate_provenance(Snapshot((missing,)))

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].code, "CORE_PROVENANCE_MISSING")
        self.assertIn("actor", findings[0].message)
        self.assertIn("source_hash", findings[0].message)

    def test_rejected_alternatives_remain_first_class_but_never_current(self) -> None:
        rejected_id = ScopedId("product", "ARC-003")
        accepted = self.revision(
            self.product,
            "ARC-002",
            "ArchitectureDecision",
            truth_key="runtime",
            rejected_alternatives=(rejected_id,),
        )
        rejected = self.revision(
            self.product,
            "ARC-003",
            "ArchitectureDecision",
            truth_key="runtime-alternative",
            status="rejected",
        )
        snapshot = Snapshot((accepted, rejected))

        self.assertEqual(
            validate_rejected_alternatives(snapshot, self.packs), ()
        )
        self.assertEqual(
            current_truth(snapshot, self.product, "runtime", "v0.6", T1),
            accepted,
        )
        self.assertIsNone(
            current_truth(
                snapshot,
                self.product,
                "runtime-alternative",
                "v0.6",
                T1,
            )
        )
        invalid = Snapshot(
            (
                dataclasses.replace(
                    accepted,
                    rejected_alternatives=(
                        ScopedId("product", "ARC-999"),
                    ),
                ),
                rejected,
            )
        )
        self.assertEqual(
            validate_rejected_alternatives(invalid, self.packs)[0].code,
            "CORE_REJECTED_ALTERNATIVE_MISSING",
        )

    def test_evidence_only_types_are_rejected_as_assertions(self) -> None:
        bad_assertions = Snapshot(
            (
                self.revision(
                    self.product, "BR-001", "GitCommit"
                ),
                self.revision(
                    self.accounting, "ACCT-001", "JournalEntry"
                ),
                self.revision(
                    self.restaurant, "MENU-001", "POSSale"
                ),
            )
        )
        codes = [
            finding.code
            for finding in validate_ids(bad_assertions, self.packs)
        ]

        self.assertEqual(
            codes.count("CORE_BOUNDARY_EVIDENCE_AS_ASSERTION"), 3
        )

    def test_relation_schema_and_referential_integrity_fail_closed(self) -> None:
        journey = self.revision(self.product, "UJ-001", "Journey")
        screen = self.revision(self.product, "SCR-001", "Screen")
        valid = Relation(
            journey.id,
            "uses-screen",
            screen.id,
            journey.id,
            1,
        )
        self.assertEqual(
            validate_relations(
                Snapshot((journey, screen), (valid,)), self.packs
            ),
            (),
        )

        malformed = Snapshot(
            (journey, screen),
            (
                valid,
                valid,
                Relation(
                    journey.id,
                    "undeclared-relation",
                    ScopedId("product", "SCR-999"),
                    ScopedId("accounting", "POL-001"),
                    99,
                ),
            ),
        )
        codes = {
            finding.code
            for finding in validate_relations(malformed, self.packs)
        }
        self.assertIn("CORE_RELATION_DUPLICATE", codes)
        self.assertIn("CORE_RELATION_ENDPOINT_MISSING", codes)
        self.assertIn("CORE_RELATION_CROSS_PACK", codes)
        self.assertIn("CORE_RELATION_ASSERTING_REVISION_MISSING", codes)
        self.assertIn("CORE_RELATION_TYPE_UNKNOWN", codes)

    def test_evidence_is_accepted_by_reference_and_orphans_fail(self) -> None:
        assertion = self.revision(
            self.accounting, "POL-001", "RevenuePolicy"
        )
        valid_event = EvidenceEvent(
            event_id="ledger:JE-100",
            pack="accounting",
            evidence_type="JournalEntry",
            observed_at=T1,
            recorded_at=T2,
            assertion_refs=(assertion.id,),
            source_system="ledger",
            source_ref="journal/JE-100",
            source_hash="b" * 64,
        )
        orphan = dataclasses.replace(
            valid_event,
            event_id="ledger:JE-101",
            assertion_refs=(ScopedId("accounting", "POL-999"),),
        )

        self.assertEqual(
            validate_evidence(
                Snapshot((assertion,), evidence=(valid_event,)), self.packs
            ),
            (),
        )
        codes = {
            finding.code
            for finding in validate_evidence(
                Snapshot((assertion,), evidence=(orphan,)), self.packs
            )
        }
        self.assertIn("CORE_EVIDENCE_ASSERTION_MISSING", codes)

    def test_evidence_rejects_empty_duplicate_and_cross_pack_references(
        self,
    ) -> None:
        product_assertion = self.revision(
            self.product, "BR-001", "BusinessRule"
        )
        accounting_assertion = self.revision(
            self.accounting, "POL-001", "RevenuePolicy"
        )
        base = EvidenceEvent(
            event_id="ledger:JE-100",
            pack="accounting",
            evidence_type="JournalEntry",
            observed_at=T1,
            recorded_at=T2,
            assertion_refs=(accounting_assertion.id,),
            source_system="ledger",
            source_ref="journal/JE-100",
            source_hash="b" * 64,
        )
        snapshot = Snapshot(
            (product_assertion, accounting_assertion),
            evidence=(
                base,
                dataclasses.replace(base, assertion_refs=()),
                dataclasses.replace(
                    base,
                    event_id="ledger:JE-101",
                    assertion_refs=(product_assertion.id,),
                ),
            ),
        )
        codes = {
            finding.code
            for finding in validate_evidence(snapshot, self.packs)
        }

        self.assertIn("CORE_EVIDENCE_ID_DUPLICATE_OR_EMPTY", codes)
        self.assertIn("CORE_EVIDENCE_ASSERTION_REFS_EMPTY", codes)
        self.assertIn("CORE_EVIDENCE_CROSS_PACK_REFERENCE", codes)

    def test_evidence_cannot_reference_an_assertion_not_yet_recorded(
        self,
    ) -> None:
        future_policy = self.revision(
            self.accounting,
            "POL-001",
            "RevenuePolicy",
            transaction_from=T2,
        )
        premature = EvidenceEvent(
            event_id="ledger:premature",
            pack="accounting",
            evidence_type="JournalEntry",
            observed_at=T0,
            recorded_at=T1,
            assertion_refs=(future_policy.id,),
            source_system="ledger",
            source_ref="journal/premature",
            source_hash="b" * 64,
        )

        codes = {
            finding.code
            for finding in validate_evidence(
                Snapshot((future_policy,), evidence=(premature,)),
                self.packs,
            )
        }

        self.assertIn(
            "CORE_EVIDENCE_ASSERTION_NOT_TRANSACTION_VISIBLE",
            codes,
        )

    def full_lifecycle_fixture(
        self,
    ) -> tuple[Snapshot, tuple[GateAttestation, ...]]:
        counts = {
            "CFD": 5,
            "BR": 3,
            "KPI": 3,
            "FEA": 1,
            "PER": 1,
            "UJ": 3,
            "SCR": 1,
            "RISK": 5,
            "TECH": 3,
            "ARC": 1,
            "API": 1,
            "DBT": 1,
            "EPIC": 1,
            "TEST": 1,
            "DEP": 1,
            "RUN": 1,
            "MON": 1,
            "GTM": 1,
        }
        by_prefix = {
            spec.prefix: (name, spec)
            for name, spec in self.product.entity_types.items()
        }
        assertions: list[AssertionRevision] = []
        ids: dict[str, list[ScopedId]] = defaultdict(list)
        for prefix, count in counts.items():
            entity_name, spec = by_prefix[prefix]
            attributes = {
                field: (
                    ["step"] if field == "steps" else f"verified-{field}"
                )
                for field in spec.custom_fields
            }
            for number in range(1, count + 1):
                revision = self.revision(
                    self.product,
                    f"{prefix}-{number:03d}",
                    entity_name,
                    attributes=attributes,
                )
                assertions.append(revision)
                ids[prefix].append(revision.id)
        relations = [
            *(
                Relation(
                    source=journey,
                    relation="uses-screen",
                    target=ids["SCR"][0],
                    asserted_by=journey,
                    asserted_in_revision=1,
                )
                for journey in ids["UJ"]
            ),
            *(
                Relation(
                    source=journey,
                    relation="uses-api",
                    target=ids["API"][0],
                    asserted_by=journey,
                    asserted_in_revision=1,
                )
                for journey in ids["UJ"]
            ),
            Relation(
                source=ids["TEST"][0],
                relation="verifies",
                target=ids["BR"][0],
                asserted_by=ids["TEST"][0],
                asserted_in_revision=1,
            ),
        ]
        attestations = tuple(
            GateAttestation(
                gate=target,
                check_id=check,
                passed=True,
                assertion_refs=(
                    ids[next(iter(gate.minimum_prefix_counts))][0],
                ),
                provenance=self.provenance(f"gate-{target}"),
                recorded_at=T0,
            )
            for target, gate in self.product.gates.items()
            for check in gate.manual_checks
        )
        return Snapshot(tuple(assertions), tuple(relations)), attestations

    def test_product_lifecycle_gate_matrix_passes_complete_fixture(self) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        for target in self.product.gates:
            with self.subTest(target=target):
                report = evaluate_gate(
                    snapshot,
                    self.product,
                    target,
                    target,
                    T1,
                    attestations,
                )
                self.assertEqual(report.verdict, GateVerdict.PASS)
                self.assertEqual(report.findings, ())

    def test_v07_gate_matches_executable_dbt_or_ent_alias_contract(
        self,
    ) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        assertions = tuple(
            self.revision(
                self.product,
                "ENT-001",
                "DataEntity",
                attributes={"relationships": "API-001"},
            )
            if revision.id.local_id == "DBT-001"
            else revision
            for revision in snapshot.assertions
        )

        report = evaluate_gate(
            Snapshot(assertions, snapshot.relations),
            self.product,
            "v0.7",
            "v0.7",
            T1,
            attestations,
        )

        self.assertEqual(
            self.product.gates["v0.7"].prefix_aliases["DBT"],
            ("DBT", "ENT"),
        )
        self.assertEqual(report.verdict, GateVerdict.PASS)
        self.assertEqual(report.counted_ids["DBT"], ("product:ENT-001",))

    def test_gate_mutation_matrix_blocks_each_missing_artifact_family(self) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        for target, gate in self.product.gates.items():
            removed_prefix = next(iter(gate.minimum_prefix_counts))
            mutated = Snapshot(
                tuple(
                    revision
                    for revision in snapshot.assertions
                    if resolve_prefix(self.product, revision.id.local_id)
                    != removed_prefix
                ),
                tuple(
                    relation
                    for relation in snapshot.relations
                    if resolve_prefix(self.product, relation.source.local_id)
                    != removed_prefix
                    and resolve_prefix(self.product, relation.target.local_id)
                    != removed_prefix
                    and resolve_prefix(
                        self.product, relation.asserted_by.local_id
                    )
                    != removed_prefix
                ),
            )
            report = evaluate_gate(
                mutated,
                self.product,
                target,
                target,
                T1,
                attestations,
                readiness_score=100.0,
            )
            with self.subTest(target=target, prefix=removed_prefix):
                self.assertEqual(report.verdict, GateVerdict.BLOCK)
                self.assertIn(
                    "GATE_REQUIRED_COUNT_MISSING",
                    {finding.code for finding in report.findings},
                )

    def test_lifecycle_gate_cannot_skip_prerequisite_stages(self) -> None:
        architecture_only = Snapshot(
            (
                self.revision(
                    self.product,
                    "ARC-001",
                    "ArchitectureDecision",
                    attributes={"alternatives": "monolith vs services"},
                ),
                self.revision(
                    self.product,
                    "API-001",
                    "APIContract",
                    attributes={
                        "request_schema": "Request",
                        "response_schema": "Response",
                    },
                ),
                self.revision(
                    self.product,
                    "DBT-001",
                    "DataModel",
                    attributes={"relationships": "API-001"},
                ),
            )
        )
        report = evaluate_gate(
            architecture_only,
            self.product,
            "v0.7",
            "v0.7",
            T1,
            readiness_score=100.0,
        )

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        missing_gate_refs = {
            finding.refs[0]
            for finding in report.findings
            if finding.code == "GATE_REQUIRED_COUNT_MISSING"
        }
        self.assertTrue({"v0.2", "v0.3", "v0.4", "v0.5", "v0.6"} <= missing_gate_refs)

    def test_gate_does_not_count_edges_asserted_by_future_revisions(
        self,
    ) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        journey_ids = {
            revision.id
            for revision in snapshot.assertions
            if revision.entity_type == "Journey"
        }
        assertions: list[AssertionRevision] = []
        for revision in snapshot.assertions:
            if revision.id not in journey_ids:
                assertions.append(revision)
                continue
            assertions.append(
                dataclasses.replace(revision, transaction_to=T2)
            )
            assertions.append(
                dataclasses.replace(
                    revision,
                    revision=2,
                    transaction_from=T2,
                    transaction_to=None,
                )
            )
        relations = tuple(
            dataclasses.replace(
                relation,
                asserted_in_revision=2,
            )
            if relation.relation == "uses-screen"
            else relation
            for relation in snapshot.relations
        )

        report = evaluate_gate(
            Snapshot(tuple(assertions), relations),
            self.product,
            "v0.5",
            "v0.5",
            T1,
            attestations,
        )

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertEqual(
            {
                finding.code
                for finding in report.findings
                if finding.code == "GATE_REQUIRED_EDGE_MISSING"
            },
            {"GATE_REQUIRED_EDGE_MISSING"},
        )

    def test_gate_blocks_a_structurally_complete_but_invalid_snapshot(
        self,
    ) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        first, *rest = snapshot.assertions
        invalid = Snapshot(
            (
                dataclasses.replace(
                    first,
                    provenance=Provenance("", "", "", ""),
                ),
                *rest,
            ),
            snapshot.relations,
        )
        report = evaluate_gate(
            invalid,
            self.product,
            "v1.0",
            "v1.0",
            T1,
            attestations,
            readiness_score=100.0,
        )

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertIn(
            "CORE_PROVENANCE_MISSING",
            {finding.code for finding in report.findings},
        )

    def test_gate_counts_only_bitemporally_current_assertions(self) -> None:
        assertions = (
            self.revision(
                self.product,
                "CFD-001",
                "CustomerEvidence",
                status="accepted",
                attributes={"evidence_tier": "Tier 1"},
            ),
            self.revision(
                self.product,
                "CFD-002",
                "CustomerEvidence",
                status="proposed",
                attributes={"evidence_tier": "Tier 1"},
            ),
            self.revision(
                self.product,
                "CFD-003",
                "CustomerEvidence",
                status="rejected",
                attributes={"evidence_tier": "Tier 1"},
            ),
            self.revision(
                self.product,
                "CFD-004",
                "CustomerEvidence",
                status="accepted",
                transaction_from=T2,
                attributes={"evidence_tier": "Tier 1"},
            ),
        )
        report = evaluate_gate(
            Snapshot(assertions),
            self.product,
            "v0.2",
            "v0.2",
            T1,
            readiness_score=100.0,
        )

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertEqual(report.counted_ids["CFD"], ("product:CFD-001",))

    def test_missing_qualitative_attestations_require_review(self) -> None:
        snapshot, _ = self.full_lifecycle_fixture()
        report = evaluate_gate(
            snapshot, self.product, "v0.2", "v0.2", T1
        )

        self.assertEqual(report.verdict, GateVerdict.REVIEW)
        self.assertEqual(
            {finding.code for finding in report.findings},
            {"GATE_ATTESTATION_MISSING"},
        )

    def test_failed_attestation_blocks_even_when_structure_is_complete(self) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        mutated = tuple(
            dataclasses.replace(item, passed=False)
            if item.gate == "v0.2" and item.check_id == "problem-not-solution"
            else item
            for item in attestations
        )
        report = evaluate_gate(
            snapshot,
            self.product,
            "v0.2",
            "v0.2",
            T1,
            mutated,
            readiness_score=100.0,
        )

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertIn(
            "GATE_ATTESTATION_FAILED",
            {finding.code for finding in report.findings},
        )

    def test_passing_attestation_requires_unique_known_same_pack_refs(
        self,
    ) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        target = next(
            item
            for item in attestations
            if item.gate == "v0.2" and item.check_id == "problem-not-solution"
        )
        malformed = tuple(
            dataclasses.replace(
                item,
                assertion_refs=(
                    ScopedId("accounting", "POL-999"),
                    ScopedId("accounting", "POL-999"),
                ),
            )
            if item == target
            else item
            for item in attestations
        )

        report = evaluate_gate(
            snapshot,
            self.product,
            "v0.2",
            "v0.2",
            T1,
            malformed,
        )
        codes = {finding.code for finding in report.findings}

        self.assertEqual(report.verdict, GateVerdict.BLOCK)
        self.assertIn("GATE_ATTESTATION_REFS_DUPLICATE", codes)
        self.assertIn("GATE_ATTESTATION_REF_INVALID", codes)

    def test_future_attestation_cannot_satisfy_historical_gate(self) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        future = tuple(
            dataclasses.replace(item, recorded_at=T2)
            if item.gate == "v0.2"
            else item
            for item in attestations
        )

        report = evaluate_gate(
            snapshot,
            self.product,
            "v0.2",
            "v0.2",
            T1,
            future,
        )

        self.assertEqual(report.verdict, GateVerdict.REVIEW)
        self.assertEqual(
            {
                finding.code
                for finding in report.findings
                if finding.code.startswith("GATE_ATTESTATION_")
            },
            {"GATE_ATTESTATION_NOT_YET_RECORDED"},
        )

    def test_product_change_flags_review_without_mutating_truth(self) -> None:
        assertion = self.revision(
            self.product, "API-001", "APIContract", truth_key="public-api"
        )
        event = EvidenceEvent(
            event_id="git:abc123",
            pack="product",
            evidence_type="GitCommit",
            observed_at=T1,
            recorded_at=T1,
            assertion_refs=(assertion.id,),
            source_system="git",
            source_ref="commit/abc123",
            source_hash="c" * 64,
            effect="cautions",
        )
        before = current_truth(
            Snapshot((assertion,)), self.product, "public-api", "v0.6", T2
        )
        snapshot = Snapshot((assertion,), evidence=(event,))
        findings = run_pack_detectors(
            snapshot, self.product, "v0.6", T2
        )
        after = current_truth(
            snapshot, self.product, "public-api", "v0.6", T2
        )

        self.assertEqual(before, after)
        self.assertEqual(findings[0].code, "PRODUCT_CHANGE_REVIEW_REQUIRED")

    def test_product_change_review_is_resolved_by_later_verification(
        self,
    ) -> None:
        assertion = self.revision(
            self.product, "API-001", "APIContract", truth_key="public-api"
        )
        changed = EvidenceEvent(
            "git:abc123",
            "product",
            "GitCommit",
            T1,
            T1,
            (assertion.id,),
            "git",
            "commit/abc123",
            "c" * 64,
            effect="cautions",
        )
        verified = EvidenceEvent(
            "build:passed",
            "product",
            "BuildResult",
            T2,
            T2,
            (assertion.id,),
            "ci",
            "build/passed",
            "d" * 64,
            effect="verifies",
        )
        snapshot = Snapshot(
            (assertion,), evidence=(changed, verified)
        )

        before_verification = run_pack_detectors(
            snapshot, self.product, "v0.6", T1
        )
        after_verification = run_pack_detectors(
            snapshot, self.product, "v0.6", T3
        )

        self.assertEqual(
            {finding.code for finding in before_verification},
            {"PRODUCT_CHANGE_REVIEW_REQUIRED"},
        )
        self.assertEqual(after_verification, ())

    def test_product_evidence_tie_fails_closed(self) -> None:
        assertion = self.revision(
            self.product, "API-001", "APIContract", truth_key="public-api"
        )
        caution = EvidenceEvent(
            "git:tie",
            "product",
            "GitCommit",
            T1,
            T1,
            (assertion.id,),
            "git",
            "commit/tie",
            "c" * 64,
            effect="cautions",
        )
        verified = EvidenceEvent(
            "build:tie",
            "product",
            "BuildResult",
            T1,
            T1,
            (assertion.id,),
            "ci",
            "build/tie",
            "d" * 64,
            effect="verifies",
        )

        findings = run_pack_detectors(
            Snapshot((assertion,), evidence=(caution, verified)),
            self.product,
            "v0.6",
            T2,
        )

        self.assertEqual(
            {finding.code for finding in findings},
            {"PRODUCT_EVIDENCE_STATE_AMBIGUOUS"},
        )

    def test_registered_detector_caution_prevents_gate_pass(self) -> None:
        snapshot, attestations = self.full_lifecycle_fixture()
        current_cfd = next(
            revision
            for revision in snapshot.assertions
            if revision.entity_type == "CustomerEvidence"
        )
        changed = EvidenceEvent(
            event_id="git:gate-review",
            pack="product",
            evidence_type="GitCommit",
            observed_at=T1,
            recorded_at=T1,
            assertion_refs=(current_cfd.id,),
            source_system="git",
            source_ref="commit/gate-review",
            source_hash="c" * 64,
            effect="cautions",
        )
        report = evaluate_gate(
            dataclasses.replace(snapshot, evidence=(changed,)),
            self.product,
            "v0.2",
            "v0.2",
            T2,
            attestations,
        )

        self.assertEqual(report.verdict, GateVerdict.REVIEW)
        self.assertIn(
            "PRODUCT_CHANGE_REVIEW_REQUIRED",
            {finding.code for finding in report.findings},
        )

    def test_accounting_trial_balance_detector_and_policy_asof(self) -> None:
        old_id = ScopedId("accounting", "POL-001")
        new_id = ScopedId("accounting", "POL-002")
        old_r1 = self.revision(
            self.accounting,
            "POL-001",
            "RevenuePolicy",
            revision=1,
            truth_key="revenue-recognition",
            valid_from="2026-01-01T00:00:00Z",
            transaction_from=T0,
            transaction_to=T2,
        )
        old_r2 = self.revision(
            self.accounting,
            "POL-001",
            "RevenuePolicy",
            revision=2,
            truth_key="revenue-recognition",
            status="superseded",
            valid_from="2026-01-01T00:00:00Z",
            valid_to="2026-02-15T00:00:00Z",
            transaction_from=T2,
            invalidated_by=new_id,
        )
        new = self.revision(
            self.accounting,
            "POL-002",
            "RevenuePolicy",
            truth_key="revenue-recognition",
            valid_from="2026-02-15T00:00:00Z",
            transaction_from=T2,
            supersedes=old_id,
        )
        balanced = EvidenceEvent(
            "ledger:tb-1",
            "accounting",
            "TrialBalanceSnapshot",
            T2,
            T2,
            (new.id,),
            "ledger",
            "trial-balance/2026-02",
            "d" * 64,
            measurements={"debit_total": 1000, "credit_total": 1000},
        )
        unbalanced = dataclasses.replace(
            balanced,
            event_id="ledger:tb-2",
            measurements={"debit_total": 1000, "credit_total": 999},
        )
        snapshot = Snapshot((old_r1, old_r2, new), evidence=(balanced, unbalanced))

        believed_then = current_truth(
            snapshot,
            self.accounting,
            "revenue-recognition",
            "2026-03-20T00:00:00Z",
            T1,
        )
        known_later = current_truth(
            snapshot,
            self.accounting,
            "revenue-recognition",
            "2026-03-20T00:00:00Z",
            T3,
        )
        codes = {
            finding.code
            for finding in run_pack_detectors(
                snapshot,
                self.accounting,
                "2026-03-20T00:00:00Z",
                T3,
            )
        }

        self.assertEqual(believed_then.id.local_id, "POL-001")
        self.assertEqual(known_later.id.local_id, "POL-002")
        self.assertEqual(
            codes,
            {"ACCT_TRIAL_BALANCE_BALANCED", "ACCT_TRIAL_BALANCE_UNBALANCED"},
        )

    def test_accounting_detector_rejects_binary_float_totals(self) -> None:
        policy = self.revision(
            self.accounting,
            "POL-001",
            "RevenuePolicy",
        )
        inexact = EvidenceEvent(
            "ledger:tb-float",
            "accounting",
            "TrialBalanceSnapshot",
            T1,
            T1,
            (policy.id,),
            "ledger",
            "trial-balance/float",
            "d" * 64,
            measurements={"debit_total": 0.1 + 0.2, "credit_total": 0.3},
        )

        findings = run_pack_detectors(
            Snapshot((policy,), evidence=(inexact,)),
            self.accounting,
            "2026-02-20T00:00:00Z",
            T2,
        )

        self.assertEqual(
            {finding.code for finding in findings},
            {"ACCT_TRIAL_BALANCE_INSUFFICIENT_EVIDENCE"},
        )

    def test_restaurant_inventory_evidence_cascades_without_becoming_ledger(self) -> None:
        ingredient = self.revision(
            self.restaurant, "ING-001", "IngredientDefinition"
        )
        recipe = self.revision(self.restaurant, "RECIPE-001", "Recipe")
        menu = self.revision(
            self.restaurant, "MENU-001", "MenuItem", truth_key="seasonal-drink"
        )
        relations = (
            Relation(recipe.id, "composed-of", ingredient.id, recipe.id, 1),
            Relation(menu.id, "uses-recipe", recipe.id, menu.id, 1),
        )
        count = EvidenceEvent(
            "inventory:count-1",
            "restaurant",
            "InventoryCount",
            T1,
            T1,
            (ingredient.id,),
            "inventory-system",
            "cycle-count/1",
            "e" * 64,
            measurements={"available": False},
        )
        snapshot = Snapshot(
            (ingredient, recipe, menu), relations=relations, evidence=(count,)
        )
        before = current_truth(
            snapshot,
            self.restaurant,
            "seasonal-drink",
            "2026-02-01T00:00:00Z",
            T2,
        )
        findings = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-02-01T00:00:00Z",
            T2,
        )
        after = current_truth(
            snapshot,
            self.restaurant,
            "seasonal-drink",
            "2026-02-01T00:00:00Z",
            T2,
        )

        self.assertEqual(before, after)
        self.assertEqual(findings[0].code, "MENU_ACTIVE_DEPENDENCY_UNAVAILABLE")
        self.assertEqual(findings[0].severity.value, "conflict")

    def test_restaurant_detector_does_not_leak_future_observations(self) -> None:
        ingredient = self.revision(
            self.restaurant, "ING-001", "IngredientDefinition"
        )
        recipe = self.revision(self.restaurant, "RECIPE-001", "Recipe")
        menu = self.revision(
            self.restaurant, "MENU-001", "MenuItem", truth_key="seasonal-drink"
        )
        unavailable_in_march = EvidenceEvent(
            "inventory:count-future",
            "restaurant",
            "InventoryCount",
            T2,
            T2,
            (ingredient.id,),
            "inventory-system",
            "cycle-count/future",
            "e" * 64,
            measurements={"available": False},
        )
        snapshot = Snapshot(
            (ingredient, recipe, menu),
            relations=(
                Relation(
                    recipe.id,
                    "composed-of",
                    ingredient.id,
                    recipe.id,
                    1,
                ),
                Relation(
                    menu.id,
                    "uses-recipe",
                    recipe.id,
                    menu.id,
                    1,
                ),
            ),
            evidence=(unavailable_in_march,),
        )

        january = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-01-15T00:00:00Z",
            T3,
        )
        march = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-03-15T00:00:00Z",
            T3,
        )

        self.assertEqual(january, ())
        self.assertEqual(
            {finding.code for finding in march},
            {"MENU_ACTIVE_DEPENDENCY_UNAVAILABLE"},
        )

    def test_restaurant_detector_uses_latest_inventory_state(self) -> None:
        ingredient = self.revision(
            self.restaurant, "ING-001", "IngredientDefinition"
        )
        recipe = self.revision(self.restaurant, "RECIPE-001", "Recipe")
        menu = self.revision(
            self.restaurant, "MENU-001", "MenuItem"
        )
        relations = (
            Relation(recipe.id, "composed-of", ingredient.id, recipe.id, 1),
            Relation(menu.id, "uses-recipe", recipe.id, menu.id, 1),
        )
        unavailable = EvidenceEvent(
            "inventory:unavailable",
            "restaurant",
            "InventoryCount",
            T1,
            T1,
            (ingredient.id,),
            "inventory-system",
            "cycle-count/1",
            "e" * 64,
            measurements={"available": False},
        )
        available = dataclasses.replace(
            unavailable,
            event_id="inventory:available",
            observed_at=T2,
            recorded_at=T2,
            source_ref="cycle-count/2",
            source_hash="f" * 64,
            measurements={"available": True},
        )
        snapshot = Snapshot(
            (ingredient, recipe, menu),
            relations,
            (unavailable, available),
        )

        before = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-02-15T00:00:00Z",
            T1,
        )
        after = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-04-15T00:00:00Z",
            T3,
        )

        self.assertEqual(
            {finding.code for finding in before},
            {"MENU_ACTIVE_DEPENDENCY_UNAVAILABLE"},
        )
        self.assertEqual(after, ())

    def test_restaurant_inventory_tie_and_invalid_state_fail_closed(
        self,
    ) -> None:
        ingredient = self.revision(
            self.restaurant, "ING-001", "IngredientDefinition"
        )
        unavailable = EvidenceEvent(
            "inventory:false",
            "restaurant",
            "InventoryCount",
            T1,
            T1,
            (ingredient.id,),
            "inventory-system",
            "cycle-count/false",
            "e" * 64,
            measurements={"available": False},
        )
        available = dataclasses.replace(
            unavailable,
            event_id="inventory:true",
            source_ref="cycle-count/true",
            source_hash="f" * 64,
            measurements={"available": True},
        )
        malformed = dataclasses.replace(
            unavailable,
            event_id="inventory:invalid",
            source_ref="cycle-count/invalid",
            source_hash="0" * 64,
            measurements={"available": "yes"},
        )

        ambiguous = run_pack_detectors(
            Snapshot((ingredient,), evidence=(unavailable, available)),
            self.restaurant,
            "2026-02-15T00:00:00Z",
            T2,
        )
        invalid = run_pack_detectors(
            Snapshot((ingredient,), evidence=(malformed,)),
            self.restaurant,
            "2026-02-15T00:00:00Z",
            T2,
        )

        self.assertEqual(
            {finding.code for finding in ambiguous},
            {"MENU_INVENTORY_EVIDENCE_AMBIGUOUS"},
        )
        self.assertEqual(
            {finding.code for finding in invalid},
            {"MENU_INVENTORY_EVIDENCE_INVALID"},
        )

    def test_restaurant_detector_projects_relations_as_of_revision(
        self,
    ) -> None:
        ingredient = self.revision(
            self.restaurant, "ING-001", "IngredientDefinition"
        )
        recipe_v1 = self.revision(
            self.restaurant,
            "RECIPE-001",
            "Recipe",
            revision=1,
            transaction_to=T2,
        )
        recipe_v2 = self.revision(
            self.restaurant,
            "RECIPE-001",
            "Recipe",
            revision=2,
            transaction_from=T2,
        )
        menu = self.revision(
            self.restaurant, "MENU-001", "MenuItem"
        )
        unavailable = EvidenceEvent(
            "inventory:false",
            "restaurant",
            "InventoryCount",
            T1,
            T1,
            (ingredient.id,),
            "inventory-system",
            "cycle-count/false",
            "e" * 64,
            measurements={"available": False},
        )
        future_relation = Relation(
            recipe_v2.id,
            "composed-of",
            ingredient.id,
            recipe_v2.id,
            2,
        )
        menu_relation = Relation(
            menu.id,
            "uses-recipe",
            recipe_v1.id,
            menu.id,
            1,
        )
        snapshot = Snapshot(
            (ingredient, recipe_v1, recipe_v2, menu),
            (future_relation, menu_relation),
            (unavailable,),
        )

        before_relation = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-02-15T00:00:00Z",
            T1,
        )
        after_relation = run_pack_detectors(
            snapshot,
            self.restaurant,
            "2026-04-15T00:00:00Z",
            T3,
        )

        self.assertEqual(before_relation, ())
        self.assertEqual(
            {finding.code for finding in after_relation},
            {"MENU_ACTIVE_DEPENDENCY_UNAVAILABLE"},
        )

    def test_conformance_findings_are_input_order_independent(self) -> None:
        missing_provenance = self.revision(
            self.product,
            "BR-001",
            "BusinessRule",
            provenance=Provenance("", "", "", ""),
        )
        unknown_type = self.revision(
            self.product, "BR-002", "UnknownAssertionType"
        )
        forward = Snapshot((missing_provenance, unknown_type))
        reverse = Snapshot(tuple(reversed(forward.assertions)))

        self.assertEqual(
            run_conformance(forward, self.packs),
            run_conformance(reverse, self.packs),
        )


if __name__ == "__main__":
    unittest.main()
