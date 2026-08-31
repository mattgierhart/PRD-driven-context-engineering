#!/usr/bin/env python3
"""Backend-neutral conformance oracle for the core + schema-pack hypothesis.

This module is intentionally a test oracle, not a production pack compiler.
It models only the invariants that must remain true regardless of whether a
future projection uses an in-memory index, Kuzu, or another graph engine.
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import hashlib
import json
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


class MetaStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    EXPIRED = "expired"
    VOID = "void"


class AssertionKind(str, Enum):
    DEFINITION = "definition"
    DECISION = "decision"
    POLICY = "policy"
    OBSERVATION = "observation"
    ASSUMPTION = "assumption"


class Severity(str, Enum):
    CLEAR = "clear"
    CAUTION = "caution"
    CONFLICT = "conflict"


class GateVerdict(str, Enum):
    PASS = "PASS"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"


CORE_STATUSES = frozenset(MetaStatus)
CORE_ASSERTION_KINDS = frozenset(AssertionKind)
ALLOWED_TRANSITIONS = {
    MetaStatus.DRAFT: frozenset(
        {MetaStatus.DRAFT, MetaStatus.ACTIVE, MetaStatus.VOID}
    ),
    MetaStatus.ACTIVE: frozenset(
        {
            MetaStatus.ACTIVE,
            MetaStatus.SUPERSEDED,
            MetaStatus.EXPIRED,
            MetaStatus.VOID,
        }
    ),
    MetaStatus.SUPERSEDED: frozenset({MetaStatus.SUPERSEDED}),
    MetaStatus.EXPIRED: frozenset({MetaStatus.EXPIRED}),
    MetaStatus.VOID: frozenset({MetaStatus.VOID}),
}
CORE_FIELD_NAMES = frozenset(
    {
        "pack",
        "local_id",
        "revision",
        "entity_type",
        "truth_key",
        "local_status",
        "valid_from",
        "valid_to",
        "transaction_from",
        "transaction_to",
        "supersedes",
        "invalidated_by",
        "rejected_alternatives",
        "provenance",
    }
)
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)(?:r(\d+))?$")
DETECTOR_NAMES = frozenset(
    {
        "product-change-review",
        "accounting-trial-balance",
        "restaurant-unavailable-dependency",
    }
)


@dataclasses.dataclass(frozen=True, order=True)
class ScopedId:
    pack: str
    local_id: str

    def render(self) -> str:
        return f"{self.pack}:{self.local_id}"


@dataclasses.dataclass(frozen=True)
class Provenance:
    actor: str
    activity: str
    source_ref: str
    source_hash: str


@dataclasses.dataclass(frozen=True)
class AssertionRevision:
    id: ScopedId
    revision: int
    entity_type: str
    truth_key: str
    local_status: str
    valid_from: str | None
    valid_to: str | None
    transaction_from: dt.datetime
    transaction_to: dt.datetime | None
    provenance: Provenance
    supersedes: ScopedId | None = None
    invalidated_by: ScopedId | None = None
    rejected_alternatives: tuple[ScopedId, ...] = ()
    attributes: Mapping[str, Any] = dataclasses.field(default_factory=dict)

    @property
    def revision_key(self) -> str:
        return f"{self.id.render()}@{self.revision}"


@dataclasses.dataclass(frozen=True)
class Relation:
    source: ScopedId
    relation: str
    target: ScopedId
    asserted_by: ScopedId
    asserted_in_revision: int


@dataclasses.dataclass(frozen=True)
class EvidenceEvent:
    event_id: str
    pack: str
    evidence_type: str
    observed_at: dt.datetime
    recorded_at: dt.datetime
    assertion_refs: tuple[ScopedId, ...]
    source_system: str
    source_ref: str
    source_hash: str
    effect: str = "verifies"
    measurements: Mapping[str, Any] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass(frozen=True)
class EntityTypeSpec:
    name: str
    prefix: str
    kind: AssertionKind
    id_pattern: str = ""
    single_current: bool = True
    custom_fields: tuple[str, ...] = ()


@dataclasses.dataclass(frozen=True)
class RelationTypeSpec:
    name: str
    from_types: tuple[str, ...]
    to_types: tuple[str, ...]


@dataclasses.dataclass(frozen=True)
class FieldRequirement:
    prefix: str
    field: str


@dataclasses.dataclass(frozen=True)
class EdgeRequirement:
    from_prefix: str
    relation: str
    to_prefix: str


@dataclasses.dataclass(frozen=True)
class GateSpec:
    target: str
    minimum_prefix_counts: Mapping[str, int]
    prefix_aliases: Mapping[str, tuple[str, ...]] = dataclasses.field(
        default_factory=dict
    )
    required_fields: tuple[FieldRequirement, ...] = ()
    required_edges: tuple[EdgeRequirement, ...] = ()
    manual_checks: tuple[str, ...] = ()


@dataclasses.dataclass(frozen=True)
class SchemaPack:
    pack_id: str
    version: str
    core_version: str
    valid_clock: str
    entity_types: Mapping[str, EntityTypeSpec]
    relation_types: Mapping[str, RelationTypeSpec]
    evidence_types: frozenset[str]
    status_map: Mapping[str, MetaStatus]
    detectors: tuple[str, ...] = ()
    freshness_days: Mapping[str, int] = dataclasses.field(default_factory=dict)
    gates: Mapping[str, GateSpec] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: Mapping[str, Any]) -> "SchemaPack":
        entity_types = {
            name: EntityTypeSpec(
                name=name,
                prefix=spec["prefix"],
                kind=AssertionKind(spec["kind"]),
                id_pattern=spec.get(
                    "id_pattern",
                    rf"{re.escape(spec['prefix'])}-\d{{3}}",
                ),
                single_current=bool(spec.get("single_current", True)),
                custom_fields=tuple(spec.get("custom_fields", ())),
            )
            for name, spec in raw["entity_types"].items()
        }
        relation_types = {
            name: RelationTypeSpec(
                name=name,
                from_types=tuple(spec["from_types"]),
                to_types=tuple(spec["to_types"]),
            )
            for name, spec in raw.get("relation_types", {}).items()
        }
        gates: dict[str, GateSpec] = {}
        for target, spec in raw.get("gates", {}).items():
            gates[target] = GateSpec(
                target=target,
                minimum_prefix_counts={
                    key: int(value)
                    for key, value in spec.get(
                        "minimum_prefix_counts", {}
                    ).items()
                },
                prefix_aliases={
                    key: tuple(value)
                    for key, value in spec.get("prefix_aliases", {}).items()
                },
                required_fields=tuple(
                    FieldRequirement(**item)
                    for item in spec.get("required_fields", ())
                ),
                required_edges=tuple(
                    EdgeRequirement(**item)
                    for item in spec.get("required_edges", ())
                ),
                manual_checks=tuple(spec.get("manual_checks", ())),
            )
        return cls(
            pack_id=raw["pack_id"],
            version=raw["version"],
            core_version=raw["core_version"],
            valid_clock=raw["valid_clock"],
            entity_types=entity_types,
            relation_types=relation_types,
            evidence_types=frozenset(raw.get("evidence_types", ())),
            status_map={
                local: MetaStatus(core)
                for local, core in raw["status_map"].items()
            },
            detectors=tuple(raw.get("detectors", ())),
            freshness_days={
                entity_type: int(days)
                for entity_type, days in raw.get("freshness_days", {}).items()
            },
            gates=gates,
        )


@dataclasses.dataclass(frozen=True)
class GateAttestation:
    gate: str
    check_id: str
    passed: bool
    assertion_refs: tuple[ScopedId, ...]
    provenance: Provenance
    recorded_at: dt.datetime


@dataclasses.dataclass(frozen=True, order=True)
class Finding:
    code: str
    severity: Severity
    refs: tuple[str, ...]
    message: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "severity": self.severity.value,
            "refs": list(self.refs),
            "message": self.message,
        }


@dataclasses.dataclass(frozen=True)
class Snapshot:
    assertions: tuple[AssertionRevision, ...]
    relations: tuple[Relation, ...] = ()
    evidence: tuple[EvidenceEvent, ...] = ()


@dataclasses.dataclass(frozen=True)
class GateReport:
    gate: str
    verdict: GateVerdict
    findings: tuple[Finding, ...]
    counted_ids: Mapping[str, tuple[str, ...]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "gate": self.gate,
            "verdict": self.verdict.value,
            "findings": [finding.to_dict() for finding in self.findings],
            "counted_ids": {
                prefix: list(ids)
                for prefix, ids in sorted(self.counted_ids.items())
            },
        }


class ConformanceError(ValueError):
    """Raised when a truth query cannot produce one defensible answer."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code


def load_packs(path: Path) -> dict[str, SchemaPack]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    packs = {
        item["pack_id"]: SchemaPack.from_dict(item)
        for item in raw["packs"]
    }
    if len(packs) != len(raw["packs"]):
        raise ValueError("pack IDs must be unique")
    findings = validate_packs(packs.values())
    if findings:
        rendered = "\n".join(
            f"{finding.code}: {finding.message}" for finding in findings
        )
        raise ValueError(rendered)
    return packs


def validate_packs(packs: Iterable[SchemaPack]) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    seen: set[str] = set()
    for pack in packs:
        if pack.pack_id in seen:
            findings.append(
                Finding(
                    "CORE_PACK_DUPLICATE",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    "Pack IDs must be unique.",
                )
            )
        seen.add(pack.pack_id)
        if pack.valid_clock not in {"prd_version", "date"}:
            findings.append(
                Finding(
                    "CORE_VALID_CLOCK_UNKNOWN",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    f"Unsupported valid clock {pack.valid_clock!r}.",
                )
            )
        missing_statuses = CORE_STATUSES - set(pack.status_map.values())
        if missing_statuses:
            findings.append(
                Finding(
                    "CORE_STATUS_MAP_INCOMPLETE",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    "Status map does not reach: "
                    + ", ".join(sorted(item.value for item in missing_statuses)),
                )
            )
        patterns: dict[str, str] = {}
        for entity in pack.entity_types.values():
            try:
                re.compile(entity.id_pattern)
            except re.error:
                findings.append(
                    Finding(
                        "CORE_ID_PATTERN_INVALID",
                        Severity.CONFLICT,
                        (pack.pack_id, entity.name),
                        f"{entity.id_pattern!r} is not a valid regular expression.",
                    )
                )
            if entity.id_pattern in patterns:
                findings.append(
                    Finding(
                        "CORE_ID_PATTERN_DUPLICATE",
                        Severity.CONFLICT,
                        (pack.pack_id, entity.name),
                        f"{entity.name} and {patterns[entity.id_pattern]} "
                        "share an ID pattern.",
                    )
                )
            patterns[entity.id_pattern] = entity.name
            collisions = CORE_FIELD_NAMES & set(entity.custom_fields)
            if collisions:
                findings.append(
                    Finding(
                        "CORE_FIELD_SHADOWED",
                        Severity.CONFLICT,
                        (pack.pack_id, entity.name),
                        "Pack field shadows core field(s): "
                        + ", ".join(sorted(collisions)),
                    )
                )
        overlap = set(pack.entity_types) & set(pack.evidence_types)
        if overlap:
            findings.append(
                Finding(
                    "CORE_BOUNDARY_TYPE_OVERLAP",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    "Types cannot be both assertions and evidence: "
                    + ", ".join(sorted(overlap)),
                )
            )
        for relation in pack.relation_types.values():
            unknown_from = set(relation.from_types) - set(pack.entity_types)
            unknown_to = set(relation.to_types) - set(pack.entity_types)
            if (
                not relation.from_types
                or not relation.to_types
                or unknown_from
                or unknown_to
            ):
                findings.append(
                    Finding(
                        "CORE_RELATION_SCHEMA_TYPE_UNKNOWN",
                        Severity.CONFLICT,
                        (pack.pack_id, relation.name),
                        "Relation schema references unknown entity type(s): "
                        + ", ".join(sorted(unknown_from | unknown_to)),
                    )
                )
        if len(set(pack.detectors)) != len(pack.detectors):
            findings.append(
                Finding(
                    "CORE_DETECTOR_DUPLICATE",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    "Detector registrations must be unique.",
                )
            )
        unknown_detectors = set(pack.detectors) - DETECTOR_NAMES
        if unknown_detectors:
            findings.append(
                Finding(
                    "CORE_DETECTOR_UNKNOWN",
                    Severity.CONFLICT,
                    (pack.pack_id,),
                    "Unknown detector(s): "
                    + ", ".join(sorted(unknown_detectors)),
                )
            )
        for entity_type, days in pack.freshness_days.items():
            if entity_type not in pack.entity_types or days <= 0:
                findings.append(
                    Finding(
                        "CORE_FRESHNESS_POLICY_INVALID",
                        Severity.CONFLICT,
                        (pack.pack_id, entity_type),
                        "Freshness policy requires a known entity type and "
                        "a positive day count.",
                    )
                )
        declared_prefixes = {
            entity.prefix for entity in pack.entity_types.values()
        }
        for target, gate in pack.gates.items():
            if gate.target != target:
                findings.append(
                    Finding(
                        "CORE_GATE_TARGET_MISMATCH",
                        Severity.CONFLICT,
                        (pack.pack_id, target),
                        "Gate mapping key and declared target must match.",
                    )
                )
            if pack.valid_clock == "prd_version":
                try:
                    parse_valid_point(pack, target)
                except ConformanceError:
                    findings.append(
                        Finding(
                            "CORE_GATE_TARGET_INVALID",
                            Severity.CONFLICT,
                            (pack.pack_id, target),
                            "Gate target is not a valid PRD lifecycle version.",
                        )
                    )
            for required_prefix, minimum in (
                gate.minimum_prefix_counts.items()
            ):
                if required_prefix not in declared_prefixes or minimum <= 0:
                    findings.append(
                        Finding(
                            "CORE_GATE_COUNT_SPEC_INVALID",
                            Severity.CONFLICT,
                            (pack.pack_id, target, required_prefix),
                            "Gate counts require a declared prefix and a "
                            "positive minimum.",
                        )
                    )
                aliases = gate.prefix_aliases.get(
                    required_prefix, (required_prefix,)
                )
                if (
                    not aliases
                    or set(aliases) - declared_prefixes
                ):
                    findings.append(
                        Finding(
                            "CORE_GATE_PREFIX_ALIAS_INVALID",
                            Severity.CONFLICT,
                            (pack.pack_id, target, required_prefix),
                            "Gate aliases must be non-empty declared prefixes.",
                        )
                    )
            for requirement in gate.required_fields:
                matching_entities = [
                    entity
                    for entity in pack.entity_types.values()
                    if entity.prefix == requirement.prefix
                ]
                if not matching_entities or any(
                    requirement.field not in CORE_FIELD_NAMES
                    and requirement.field not in entity.custom_fields
                    for entity in matching_entities
                ):
                    findings.append(
                        Finding(
                            "CORE_GATE_FIELD_SPEC_INVALID",
                            Severity.CONFLICT,
                            (
                                pack.pack_id,
                                target,
                                requirement.prefix,
                                requirement.field,
                            ),
                            "A required gate field must exist on every entity "
                            "type counted under that prefix.",
                        )
                    )
            for requirement in gate.required_edges:
                relation = pack.relation_types.get(requirement.relation)
                source_types = {
                    name
                    for name, entity in pack.entity_types.items()
                    if entity.prefix == requirement.from_prefix
                }
                target_types = {
                    name
                    for name, entity in pack.entity_types.items()
                    if entity.prefix == requirement.to_prefix
                }
                if (
                    relation is None
                    or not source_types
                    or not target_types
                    or not source_types <= set(relation.from_types)
                    or not (target_types & set(relation.to_types))
                ):
                    findings.append(
                        Finding(
                            "CORE_GATE_EDGE_SPEC_INVALID",
                            Severity.CONFLICT,
                            (
                                pack.pack_id,
                                target,
                                requirement.from_prefix,
                                requirement.relation,
                                requirement.to_prefix,
                            ),
                            "Gate edge requirements must be satisfiable by "
                            "the declared relationship schema.",
                        )
                    )
            if (
                any(not check_id for check_id in gate.manual_checks)
                or len(set(gate.manual_checks)) != len(gate.manual_checks)
            ):
                findings.append(
                    Finding(
                        "CORE_GATE_MANUAL_CHECK_INVALID",
                        Severity.CONFLICT,
                        (pack.pack_id, target),
                        "Manual gate check IDs must be non-empty and unique.",
                    )
                )
    return tuple(sorted(findings))


def schema_projection(pack: SchemaPack) -> dict[str, Any]:
    """Return deterministic test DDL metadata with denormalized core fields.

    The output demonstrates the proposed seam; it is not an engine-specific
    compiler or a commitment to JSON as the future pack-authoring format.
    """

    core_fields = tuple(sorted(CORE_FIELD_NAMES))
    tables = []
    for name, spec in sorted(pack.entity_types.items()):
        tables.append(
            {
                "name": name,
                "prefix": spec.prefix,
                "id_pattern": spec.id_pattern,
                "assertion_kind": spec.kind.value,
                "fields": list(core_fields + tuple(sorted(spec.custom_fields))),
            }
        )
    evidence_tables = [
        {
            "name": name,
            "fields": [
                "event_id",
                "pack",
                "observed_at",
                "recorded_at",
                "assertion_refs",
                "evidence_type",
                "effect",
                "measurements",
                "source_system",
                "source_ref",
                "source_hash",
            ],
        }
        for name in sorted(pack.evidence_types)
    ]
    relation_tables = [
        {
            "name": name,
            "from_types": list(spec.from_types),
            "to_types": list(spec.to_types),
            "fields": ["asserted_by", "asserted_in_revision"],
        }
        for name, spec in sorted(pack.relation_types.items())
    ]
    payload = {
        "pack_id": pack.pack_id,
        "pack_version": pack.version,
        "core_version": pack.core_version,
        "assertion_tables": tables,
        "relation_tables": relation_tables,
        "evidence_tables": evidence_tables,
        "detectors": list(pack.detectors),
        "freshness_days": dict(sorted(pack.freshness_days.items())),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["projection_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return payload


def resolve_prefix(pack: SchemaPack, local_id: str) -> str:
    matches = [
        spec
        for spec in pack.entity_types.values()
        if re.fullmatch(spec.id_pattern, local_id)
    ]
    if len(matches) > 1:
        raise ConformanceError(
            "CORE_ID_PATTERN_AMBIGUOUS",
            f"{local_id!r} matches multiple entity ID patterns.",
        )
    if matches:
        return matches[0].prefix
    known_family = any(
        local_id.startswith(f"{spec.prefix}-")
        for spec in pack.entity_types.values()
    )
    if known_family:
        raise ConformanceError(
            "CORE_ID_FORMAT_INVALID",
            f"{local_id!r} does not match a declared entity ID pattern.",
        )
    else:
        raise ConformanceError(
            "CORE_ID_PREFIX_UNKNOWN",
            f"{local_id!r} is not in {pack.pack_id}'s prefix registry.",
        )


def normalize_status(pack: SchemaPack, local_status: str) -> MetaStatus:
    try:
        return pack.status_map[local_status]
    except KeyError as error:
        raise ConformanceError(
            "CORE_STATUS_UNKNOWN",
            f"{local_status!r} is not mapped by {pack.pack_id}.",
        ) from error


def parse_valid_point(pack: SchemaPack, raw: str) -> tuple[int, ...] | dt.datetime:
    if pack.valid_clock == "prd_version":
        match = VERSION_RE.fullmatch(raw)
        if not match:
            raise ConformanceError(
                "CORE_VALID_POINT_INVALID",
                f"{raw!r} is not a PRD lifecycle version.",
            )
        return tuple(int(part or 0) for part in match.groups())
    try:
        value = dt.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError as error:
        raise ConformanceError(
            "CORE_VALID_POINT_INVALID", f"{raw!r} is not an ISO timestamp."
        ) from error
    if value.tzinfo is None:
        raise ConformanceError(
            "CORE_VALID_POINT_INVALID", "Valid-time timestamps must include a zone."
        )
    return value


def _valid_contains(
    revision: AssertionRevision, pack: SchemaPack, valid_at: str
) -> bool:
    point = parse_valid_point(pack, valid_at)
    lower = (
        parse_valid_point(pack, revision.valid_from)
        if revision.valid_from is not None
        else None
    )
    upper = (
        parse_valid_point(pack, revision.valid_to)
        if revision.valid_to is not None
        else None
    )
    return (lower is None or lower <= point) and (upper is None or point < upper)


def _transaction_contains(
    revision: AssertionRevision, known_at: dt.datetime
) -> bool:
    return revision.transaction_from <= known_at and (
        revision.transaction_to is None or known_at < revision.transaction_to
    )


def _is_aware(value: dt.datetime) -> bool:
    return value.tzinfo is not None and value.utcoffset() is not None


def _utc_sort_key(value: dt.datetime) -> dt.datetime:
    if _is_aware(value):
        return value.astimezone(dt.timezone.utc)
    return value.replace(tzinfo=dt.timezone.utc)


def revision_at(
    records: Iterable[AssertionRevision],
    scoped_id: ScopedId,
    known_at: dt.datetime,
) -> AssertionRevision | None:
    if not _is_aware(known_at):
        raise ConformanceError(
            "CORE_KNOWN_AT_TIMEZONE_MISSING",
            "known_at must include a timezone.",
        )
    visible = [
        revision
        for revision in records
        if revision.id == scoped_id and _transaction_contains(revision, known_at)
    ]
    if len(visible) > 1:
        raise ConformanceError(
            "CORE_TRANSACTION_OVERLAP",
            f"{scoped_id.render()} has multiple revisions at {known_at.isoformat()}.",
        )
    return visible[0] if visible else None


def current_truth(
    snapshot: Snapshot,
    pack: SchemaPack,
    truth_key: str,
    valid_at: str,
    known_at: dt.datetime,
) -> AssertionRevision | None:
    ids = sorted(
        {
            revision.id
            for revision in snapshot.assertions
            if revision.id.pack == pack.pack_id
            and revision.truth_key == truth_key
        }
    )
    candidates: list[AssertionRevision] = []
    for scoped_id in ids:
        revision = revision_at(snapshot.assertions, scoped_id, known_at)
        if revision is None:
            continue
        status = normalize_status(pack, revision.local_status)
        if status not in {
            MetaStatus.ACTIVE,
            MetaStatus.SUPERSEDED,
            MetaStatus.EXPIRED,
        }:
            continue
        if _valid_contains(revision, pack, valid_at):
            candidates.append(revision)
    unknown_entity_types = sorted(
        {
            item.entity_type
            for item in candidates
            if item.entity_type not in pack.entity_types
        }
    )
    if unknown_entity_types:
        raise ConformanceError(
            "CORE_ENTITY_TYPE_UNKNOWN",
            "Current truth contains unknown entity type(s): "
            + ", ".join(unknown_entity_types),
        )
    single_current = {
        pack.entity_types[item.entity_type].single_current
        for item in candidates
    }
    if len(candidates) > 1:
        if True in single_current:
            raise ConformanceError(
                "CORE_TRUTH_AMBIGUOUS",
                f"{truth_key!r} has {len(candidates)} current assertions.",
            )
        raise ConformanceError(
            "CORE_TRUTH_QUERY_CARDINALITY_UNSUPPORTED",
            f"{truth_key!r} is multi-current; use a plural query surface.",
        )
    return candidates[0] if candidates else None


def validate_ids(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    seen_revisions: set[tuple[ScopedId, int]] = set()
    for revision in snapshot.assertions:
        ref = revision.revision_key
        pack = packs.get(revision.id.pack)
        if pack is None:
            findings.append(
                Finding(
                    "CORE_PACK_UNKNOWN",
                    Severity.CONFLICT,
                    (ref,),
                    f"Unknown pack {revision.id.pack}.",
                )
            )
            continue
        key = (revision.id, revision.revision)
        if key in seen_revisions:
            findings.append(
                Finding(
                    "CORE_REVISION_DUPLICATE",
                    Severity.CONFLICT,
                    (ref,),
                    "Revision identity is duplicated.",
                )
            )
        seen_revisions.add(key)
        spec = pack.entity_types.get(revision.entity_type)
        if spec is None:
            code = (
                "CORE_BOUNDARY_EVIDENCE_AS_ASSERTION"
                if revision.entity_type in pack.evidence_types
                else "CORE_ENTITY_TYPE_UNKNOWN"
            )
            findings.append(
                Finding(
                    code,
                    Severity.CONFLICT,
                    (ref,),
                    f"{revision.entity_type} is not a curated assertion type.",
                )
            )
            continue
        try:
            actual_prefix = resolve_prefix(pack, revision.id.local_id)
        except ConformanceError as error:
            findings.append(
                Finding(error.code, Severity.CONFLICT, (ref,), str(error))
            )
            continue
        if actual_prefix != spec.prefix:
            findings.append(
                Finding(
                    "CORE_ENTITY_PREFIX_MISMATCH",
                    Severity.CONFLICT,
                    (ref,),
                    f"{revision.entity_type} requires {spec.prefix}-, "
                    f"not {actual_prefix}-.",
                )
            )
        if not re.fullmatch(spec.id_pattern, revision.id.local_id):
            findings.append(
                Finding(
                    "CORE_ENTITY_ID_PATTERN_MISMATCH",
                    Severity.CONFLICT,
                    (ref,),
                    f"{revision.entity_type} requires IDs matching "
                    f"{spec.id_pattern!r}.",
                )
            )
    return tuple(sorted(findings))


def validate_provenance(snapshot: Snapshot) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    for revision in snapshot.assertions:
        values = dataclasses.asdict(revision.provenance)
        missing = sorted(key for key, value in values.items() if not value.strip())
        if missing:
            findings.append(
                Finding(
                    "CORE_PROVENANCE_MISSING",
                    Severity.CONFLICT,
                    (revision.revision_key,),
                    "Missing provenance field(s): " + ", ".join(missing),
                )
            )
    return tuple(sorted(findings))


def validate_revision_intervals(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    grouped: dict[ScopedId, list[AssertionRevision]] = defaultdict(list)
    for revision in snapshot.assertions:
        grouped[revision.id].append(revision)
        transaction_values = [
            value
            for value in (revision.transaction_from, revision.transaction_to)
            if value is not None
        ]
        if not all(_is_aware(value) for value in transaction_values):
            findings.append(
                Finding(
                    "CORE_TRANSACTION_TIMEZONE_MISSING",
                    Severity.CONFLICT,
                    (revision.revision_key,),
                    "Transaction timestamps must include a timezone.",
                )
            )
        elif (
            revision.transaction_to is not None
            and revision.transaction_from >= revision.transaction_to
        ):
            findings.append(
                Finding(
                    "CORE_TRANSACTION_INTERVAL_INVALID",
                    Severity.CONFLICT,
                    (revision.revision_key,),
                    "Transaction interval must be non-empty and half-open.",
                )
            )
        pack = packs.get(revision.id.pack)
        if pack:
            lower = None
            upper = None
            for field, raw in (
                ("valid_from", revision.valid_from),
                ("valid_to", revision.valid_to),
            ):
                if raw is None:
                    continue
                try:
                    parsed = parse_valid_point(pack, raw)
                    if field == "valid_from":
                        lower = parsed
                    else:
                        upper = parsed
                except ConformanceError as error:
                    findings.append(
                        Finding(
                            error.code,
                            Severity.CONFLICT,
                            (revision.revision_key,),
                            str(error),
                        )
                    )
            if lower is not None and upper is not None and lower >= upper:
                findings.append(
                    Finding(
                        "CORE_VALID_INTERVAL_INVALID",
                        Severity.CONFLICT,
                        (revision.revision_key,),
                        "Valid interval must be non-empty and half-open.",
                    )
                )
    for scoped_id, revisions in grouped.items():
        entity_types = {revision.entity_type for revision in revisions}
        truth_keys = {revision.truth_key for revision in revisions}
        if len(entity_types) > 1 or len(truth_keys) > 1:
            findings.append(
                Finding(
                    "CORE_REVISION_IDENTITY_DRIFT",
                    Severity.CONFLICT,
                    (scoped_id.render(),),
                    "Revisions of one assertion ID must preserve entity_type "
                    "and truth_key.",
                )
            )
        ordered = sorted(
            revisions,
            key=lambda item: _utc_sort_key(item.transaction_from),
        )
        for previous, current in zip(ordered, ordered[1:]):
            if previous.transaction_to != current.transaction_from:
                findings.append(
                    Finding(
                        "CORE_TRANSACTION_HISTORY_GAP_OR_OVERLAP",
                        Severity.CONFLICT,
                        (previous.revision_key, current.revision_key),
                        "Adjacent transaction revisions must share a boundary.",
                    )
                )
            if current.revision <= previous.revision:
                findings.append(
                    Finding(
                        "CORE_REVISION_ORDER_INVALID",
                        Severity.CONFLICT,
                        (previous.revision_key, current.revision_key),
                        "Revision numbers must increase with transaction time.",
                    )
                )
        if len({item.revision for item in revisions}) != len(revisions):
            findings.append(
                Finding(
                    "CORE_REVISION_DUPLICATE",
                    Severity.CONFLICT,
                    (scoped_id.render(),),
                    "Revision numbers must be unique per scoped ID.",
                )
            )
    return tuple(sorted(findings))


def validate_lifecycle(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    grouped: dict[ScopedId, list[AssertionRevision]] = defaultdict(list)
    for revision in snapshot.assertions:
        grouped[revision.id].append(revision)
    for scoped_id, revisions in grouped.items():
        pack = packs.get(scoped_id.pack)
        if pack is None:
            continue
        ordered = sorted(
            revisions,
            key=lambda item: _utc_sort_key(item.transaction_from),
        )
        statuses: list[MetaStatus] = []
        for revision in ordered:
            try:
                status = normalize_status(pack, revision.local_status)
                statuses.append(status)
                if status in {MetaStatus.SUPERSEDED, MetaStatus.EXPIRED} and (
                    revision.valid_to is None
                ):
                    findings.append(
                        Finding(
                            "CORE_TERMINAL_VALID_BOUNDARY_MISSING",
                            Severity.CONFLICT,
                            (revision.revision_key,),
                            f"{status.value} assertions require valid_to.",
                        )
                    )
            except ConformanceError as error:
                findings.append(
                    Finding(
                        error.code,
                        Severity.CONFLICT,
                        (revision.revision_key,),
                        str(error),
                    )
                )
        for previous, current, current_revision in zip(
            statuses, statuses[1:], ordered[1:]
        ):
            if current not in ALLOWED_TRANSITIONS[previous]:
                findings.append(
                    Finding(
                        "CORE_LIFECYCLE_TRANSITION_INVALID",
                        Severity.CONFLICT,
                        (current_revision.revision_key,),
                        f"{previous.value} cannot transition to {current.value}.",
                    )
                )
    return tuple(sorted(findings))


def _transaction_intervals_overlap(
    left: AssertionRevision,
    right: AssertionRevision,
) -> bool:
    values = (
        left.transaction_from,
        left.transaction_to,
        right.transaction_from,
        right.transaction_to,
    )
    if not all(
        value is None or _is_aware(value)
        for value in values
    ):
        return False
    return (
        right.transaction_to is None
        or left.transaction_from < right.transaction_to
    ) and (
        left.transaction_to is None
        or right.transaction_from < left.transaction_to
    )


def _valid_intervals_overlap(
    left: AssertionRevision,
    right: AssertionRevision,
    pack: SchemaPack,
) -> bool:
    try:
        left_lower = (
            parse_valid_point(pack, left.valid_from)
            if left.valid_from is not None
            else None
        )
        left_upper = (
            parse_valid_point(pack, left.valid_to)
            if left.valid_to is not None
            else None
        )
        right_lower = (
            parse_valid_point(pack, right.valid_from)
            if right.valid_from is not None
            else None
        )
        right_upper = (
            parse_valid_point(pack, right.valid_to)
            if right.valid_to is not None
            else None
        )
    except ConformanceError:
        return False
    return (
        right_upper is None
        or left_lower is None
        or left_lower < right_upper
    ) and (
        left_upper is None
        or right_lower is None
        or right_lower < left_upper
    )


def validate_truth_uniqueness(
    snapshot: Snapshot,
    packs: Mapping[str, SchemaPack],
) -> tuple[Finding, ...]:
    """Reject overlapping bitemporal claims for single-current truth keys."""

    findings: list[Finding] = []
    grouped: dict[tuple[str, str], list[AssertionRevision]] = defaultdict(list)
    for revision in snapshot.assertions:
        grouped[(revision.id.pack, revision.truth_key)].append(revision)
    truth_bearing = {
        MetaStatus.ACTIVE,
        MetaStatus.SUPERSEDED,
        MetaStatus.EXPIRED,
    }
    for (pack_id, truth_key), revisions in grouped.items():
        pack = packs.get(pack_id)
        if pack is None:
            continue
        for index, left in enumerate(revisions):
            left_spec = pack.entity_types.get(left.entity_type)
            if left_spec is None:
                continue
            try:
                left_status = normalize_status(pack, left.local_status)
            except ConformanceError:
                continue
            if left_status not in truth_bearing:
                continue
            for right in revisions[index + 1 :]:
                if left.id == right.id:
                    continue
                right_spec = pack.entity_types.get(right.entity_type)
                if right_spec is None:
                    continue
                try:
                    right_status = normalize_status(
                        pack, right.local_status
                    )
                except ConformanceError:
                    continue
                if right_status not in truth_bearing:
                    continue
                if not (
                    left_spec.single_current
                    or right_spec.single_current
                ):
                    continue
                if not _transaction_intervals_overlap(left, right):
                    continue
                if not _valid_intervals_overlap(left, right, pack):
                    continue
                findings.append(
                    Finding(
                        "CORE_TRUTH_INTERVAL_OVERLAP",
                        Severity.CONFLICT,
                        tuple(
                            sorted(
                                (
                                    left.revision_key,
                                    right.revision_key,
                                )
                            )
                        ),
                        f"{truth_key!r} has overlapping single-current "
                        "assertions in valid and transaction time.",
                    )
                )
    return tuple(sorted(findings))


def validate_supersession(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    by_id: dict[ScopedId, list[AssertionRevision]] = defaultdict(list)
    for revision in snapshot.assertions:
        by_id[revision.id].append(revision)
    latest = {
        scoped_id: max(
            revisions, key=lambda item: _utc_sort_key(item.transaction_from)
        )
        for scoped_id, revisions in by_id.items()
    }
    graph: dict[ScopedId, ScopedId] = {}
    for new_id, new_revision in latest.items():
        if new_revision.supersedes is None:
            continue
        old = latest.get(new_revision.supersedes)
        refs = (new_id.render(), new_revision.supersedes.render())
        if old is None:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_TARGET_MISSING",
                    Severity.CONFLICT,
                    refs,
                    "Superseded assertion does not exist.",
                )
            )
            continue
        graph[new_id] = old.id
        if new_id.pack != old.id.pack:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_CROSS_PACK",
                    Severity.CONFLICT,
                    refs,
                    "Supersession cannot cross pack namespaces.",
                )
            )
        if new_revision.truth_key != old.truth_key:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_TRUTH_KEY_MISMATCH",
                    Severity.CONFLICT,
                    refs,
                    "Supersession endpoints must share one truth key.",
                )
            )
        pack = packs.get(new_id.pack)
        if pack is None:
            continue
        try:
            old_status = normalize_status(pack, old.local_status)
            new_status = normalize_status(
                pack, new_revision.local_status
            )
        except ConformanceError:
            continue
        if new_status not in {
            MetaStatus.ACTIVE,
            MetaStatus.SUPERSEDED,
            MetaStatus.EXPIRED,
        }:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_NEW_STATUS_INVALID",
                    Severity.CONFLICT,
                    refs,
                    "A superseding assertion must itself be truth-bearing, "
                    "not draft or void.",
                )
            )
        if old_status is not MetaStatus.SUPERSEDED:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_OLD_STATUS_INVALID",
                    Severity.CONFLICT,
                    refs,
                    "Superseded assertion's latest revision must be superseded.",
                )
            )
        if old.invalidated_by != new_id:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_RECIPROCAL_MISSING",
                    Severity.CONFLICT,
                    refs,
                    "Old assertion must point back with invalidated_by.",
                )
            )
        if old.valid_to != new_revision.valid_from:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_BOUNDARY_MISMATCH",
                    Severity.CONFLICT,
                    refs,
                    "Old valid_to must equal new valid_from.",
                )
            )
    for old_id, old_revision in latest.items():
        if old_revision.invalidated_by is None:
            continue
        new_revision = latest.get(old_revision.invalidated_by)
        refs = (old_id.render(), old_revision.invalidated_by.render())
        if new_revision is None:
            findings.append(
                Finding(
                    "CORE_INVALIDATION_TARGET_MISSING",
                    Severity.CONFLICT,
                    refs,
                    "invalidated_by must reference an existing assertion.",
                )
            )
        elif new_revision.supersedes != old_id:
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_RECIPROCAL_MISSING",
                    Severity.CONFLICT,
                    refs,
                    "invalidated_by must be reciprocated by supersedes.",
                )
            )
    visiting: set[ScopedId] = set()
    visited: set[ScopedId] = set()

    def walk(node: ScopedId) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        target = graph.get(node)
        cycle = target is not None and walk(target)
        visiting.remove(node)
        visited.add(node)
        return cycle

    for node in sorted(graph):
        if walk(node):
            findings.append(
                Finding(
                    "CORE_SUPERSESSION_CYCLE",
                    Severity.CONFLICT,
                    (node.render(),),
                    "Supersession chains must be acyclic.",
                )
            )
            break
    return tuple(sorted(findings))


def validate_relations(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    assertions_by_id: dict[ScopedId, list[AssertionRevision]] = defaultdict(list)
    revision_keys: set[tuple[ScopedId, int]] = set()
    for revision in snapshot.assertions:
        assertions_by_id[revision.id].append(revision)
        revision_keys.add((revision.id, revision.revision))
    entity_type_by_id = {
        scoped_id: max(
            revisions, key=lambda item: _utc_sort_key(item.transaction_from)
        ).entity_type
        for scoped_id, revisions in assertions_by_id.items()
    }
    seen: set[tuple[ScopedId, str, ScopedId, ScopedId, int]] = set()
    for relation in snapshot.relations:
        key = (
            relation.source,
            relation.relation,
            relation.target,
            relation.asserted_by,
            relation.asserted_in_revision,
        )
        refs = (
            relation.source.render(),
            relation.relation,
            relation.target.render(),
        )
        if key in seen:
            findings.append(
                Finding(
                    "CORE_RELATION_DUPLICATE",
                    Severity.CONFLICT,
                    refs,
                    "Relationship assertions must be unique.",
                )
            )
        seen.add(key)
        missing_roles = [
            role
            for role, scoped_id in (
                ("source", relation.source),
                ("target", relation.target),
                ("asserted_by", relation.asserted_by),
            )
            if scoped_id not in assertions_by_id
        ]
        if missing_roles:
            findings.append(
                Finding(
                    "CORE_RELATION_ENDPOINT_MISSING",
                    Severity.CONFLICT,
                    refs,
                    "Missing relation assertion role(s): "
                    + ", ".join(missing_roles),
                )
            )
        if len(
            {
                relation.source.pack,
                relation.target.pack,
                relation.asserted_by.pack,
            }
        ) != 1:
            findings.append(
                Finding(
                    "CORE_RELATION_CROSS_PACK",
                    Severity.CONFLICT,
                    refs,
                    "Cross-pack relationships are deferred and must fail closed.",
                )
            )
        if (
            relation.asserted_by,
            relation.asserted_in_revision,
        ) not in revision_keys:
            findings.append(
                Finding(
                    "CORE_RELATION_ASSERTING_REVISION_MISSING",
                    Severity.CONFLICT,
                    (*refs, relation.asserted_by.render()),
                    "asserted_in_revision must identify an existing revision.",
                )
            )
        pack = packs.get(relation.source.pack)
        if pack is None:
            continue
        spec = pack.relation_types.get(relation.relation)
        if spec is None:
            findings.append(
                Finding(
                    "CORE_RELATION_TYPE_UNKNOWN",
                    Severity.CONFLICT,
                    refs,
                    f"{relation.relation!r} is not declared by {pack.pack_id}.",
                )
            )
            continue
        source_type = entity_type_by_id.get(relation.source)
        target_type = entity_type_by_id.get(relation.target)
        if source_type is not None and source_type not in spec.from_types:
            findings.append(
                Finding(
                    "CORE_RELATION_SOURCE_TYPE_INVALID",
                    Severity.CONFLICT,
                    refs,
                    f"{relation.relation} cannot start at {source_type}.",
                )
            )
        if target_type is not None and target_type not in spec.to_types:
            findings.append(
                Finding(
                    "CORE_RELATION_TARGET_TYPE_INVALID",
                    Severity.CONFLICT,
                    refs,
                    f"{relation.relation} cannot end at {target_type}.",
                )
            )
    return tuple(sorted(findings))


def validate_evidence(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    assertion_ids = {revision.id for revision in snapshot.assertions}
    seen_events: set[tuple[str, str]] = set()
    for event in snapshot.evidence:
        event_key = (event.pack, event.event_id)
        if not event.event_id or event_key in seen_events:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_ID_DUPLICATE_OR_EMPTY",
                    Severity.CONFLICT,
                    (event.pack, event.event_id),
                    "Evidence IDs must be non-empty and unique within a pack.",
                )
            )
        seen_events.add(event_key)
        pack = packs.get(event.pack)
        if pack is None:
            findings.append(
                Finding(
                    "CORE_PACK_UNKNOWN",
                    Severity.CONFLICT,
                    (event.event_id,),
                    f"Unknown evidence pack {event.pack}.",
                )
            )
            continue
        if event.evidence_type not in pack.evidence_types:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_TYPE_UNKNOWN",
                    Severity.CONFLICT,
                    (event.event_id,),
                    f"{event.evidence_type} is not an evidence-only type.",
                )
            )
        if event.effect not in {"verifies", "cautions", "invalidates"}:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_EFFECT_UNKNOWN",
                    Severity.CONFLICT,
                    (event.event_id,),
                    f"Unsupported evidence effect {event.effect!r}.",
                )
            )
        if not event.assertion_refs:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_ASSERTION_REFS_EMPTY",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Evidence must reference at least one curated assertion.",
                )
            )
        if len(set(event.assertion_refs)) != len(event.assertion_refs):
            findings.append(
                Finding(
                    "CORE_EVIDENCE_ASSERTION_REFS_DUPLICATE",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Evidence assertion references must be unique.",
                )
            )
        cross_pack = sorted(
            ref.render()
            for ref in event.assertion_refs
            if ref.pack != event.pack
        )
        if cross_pack:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_CROSS_PACK_REFERENCE",
                    Severity.CONFLICT,
                    (event.event_id, *cross_pack),
                    "Evidence references cannot cross pack namespaces.",
                )
            )
        if not event.source_system or not event.source_ref or not event.source_hash:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_PROVENANCE_MISSING",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Evidence requires source system, reference, and hash.",
                )
            )
        if not _is_aware(event.observed_at) or not _is_aware(event.recorded_at):
            findings.append(
                Finding(
                    "CORE_EVIDENCE_TIMEZONE_MISSING",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Evidence timestamps must include a timezone.",
                )
            )
        elif event.recorded_at < event.observed_at:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_TIME_INVALID",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Evidence cannot be recorded before it was observed.",
                )
            )
        missing = sorted(
            ref.render() for ref in event.assertion_refs if ref not in assertion_ids
        )
        if missing:
            findings.append(
                Finding(
                    "CORE_EVIDENCE_ASSERTION_MISSING",
                    Severity.CONFLICT,
                    (event.event_id, *missing),
                    "Evidence must reference known curated assertions.",
                )
            )
        if _is_aware(event.recorded_at):
            not_visible: list[str] = []
            for reference in event.assertion_refs:
                if reference not in assertion_ids:
                    continue
                try:
                    visible = revision_at(
                        snapshot.assertions,
                        reference,
                        event.recorded_at,
                    )
                except ConformanceError:
                    continue
                if visible is None:
                    not_visible.append(reference.render())
            if not_visible:
                findings.append(
                    Finding(
                        "CORE_EVIDENCE_ASSERTION_NOT_TRANSACTION_VISIBLE",
                        Severity.CONFLICT,
                        (event.event_id, *sorted(not_visible)),
                        "Evidence may reference only assertions known when "
                        "the event was recorded.",
                    )
                )
    return tuple(sorted(findings))


def validate_rejected_alternatives(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    grouped: dict[ScopedId, list[AssertionRevision]] = defaultdict(list)
    for revision in snapshot.assertions:
        grouped[revision.id].append(revision)
    latest = {
        scoped_id: max(
            revisions, key=lambda item: _utc_sort_key(item.transaction_from)
        )
        for scoped_id, revisions in grouped.items()
    }
    for revision in snapshot.assertions:
        for alternative_id in revision.rejected_alternatives:
            refs = (revision.id.render(), alternative_id.render())
            alternative = latest.get(alternative_id)
            if alternative_id == revision.id:
                findings.append(
                    Finding(
                        "CORE_REJECTED_ALTERNATIVE_SELF",
                        Severity.CONFLICT,
                        refs,
                        "An assertion cannot reject itself as an alternative.",
                    )
                )
            elif alternative is None:
                findings.append(
                    Finding(
                        "CORE_REJECTED_ALTERNATIVE_MISSING",
                        Severity.CONFLICT,
                        refs,
                        "Rejected alternatives must remain first-class assertions.",
                    )
                )
            elif alternative_id.pack != revision.id.pack:
                findings.append(
                    Finding(
                        "CORE_REJECTED_ALTERNATIVE_CROSS_PACK",
                        Severity.CONFLICT,
                        refs,
                        "Rejected alternatives cannot cross pack namespaces.",
                    )
                )
            else:
                pack = packs.get(revision.id.pack)
                if pack is None:
                    continue
                try:
                    status = normalize_status(pack, alternative.local_status)
                except ConformanceError:
                    continue
                if status is not MetaStatus.VOID:
                    findings.append(
                        Finding(
                            "CORE_REJECTED_ALTERNATIVE_STATUS_INVALID",
                            Severity.CONFLICT,
                            refs,
                            "A rejected alternative's latest status must map to void.",
                        )
                    )
    return tuple(sorted(findings))


def evidence_findings(event: EvidenceEvent) -> tuple[Finding, ...]:
    severity_by_effect = {
        "verifies": Severity.CLEAR,
        "cautions": Severity.CAUTION,
        "invalidates": Severity.CONFLICT,
    }
    severity = severity_by_effect.get(event.effect, Severity.CONFLICT)
    return (
        Finding(
            f"CORE_EVIDENCE_{event.effect.upper()}",
            severity,
            tuple(ref.render() for ref in event.assertion_refs),
            f"{event.evidence_type} evidence {event.effect} curated assertion(s).",
        ),
    )


Detector = Callable[
    [set[ScopedId], tuple[Relation, ...], tuple[EvidenceEvent, ...]],
    Iterable[Finding],
]


def _detect_product_change(
    current_ids: set[ScopedId],
    relations: tuple[Relation, ...],
    events: tuple[EvidenceEvent, ...],
) -> Iterable[Finding]:
    del relations
    by_assertion: dict[ScopedId, list[EvidenceEvent]] = defaultdict(list)
    for event in events:
        for reference in event.assertion_refs:
            if reference in current_ids:
                by_assertion[reference].append(event)
    for reference, candidates in sorted(by_assertion.items()):
        latest_observed = max(event.observed_at for event in candidates)
        observed_candidates = [
            event
            for event in candidates
            if event.observed_at == latest_observed
        ]
        latest_recorded = max(
            event.recorded_at for event in observed_candidates
        )
        latest = [
            event
            for event in observed_candidates
            if event.recorded_at == latest_recorded
        ]
        effects = {event.effect for event in latest}
        if len(effects) > 1:
            yield Finding(
                "PRODUCT_EVIDENCE_STATE_AMBIGUOUS",
                Severity.CONFLICT,
                (
                    reference.render(),
                    *(event.event_id for event in sorted(
                        latest, key=lambda item: item.event_id
                    )),
                ),
                "Equally current evidence assigns conflicting states to "
                "a product assertion.",
            )
            continue
        effect = next(iter(effects))
        if effect == "cautions":
            yield Finding(
                "PRODUCT_CHANGE_REVIEW_REQUIRED",
                Severity.CAUTION,
                (reference.render(),),
                "The latest evidence for a current assertion requires review.",
            )
        elif effect == "invalidates":
            yield Finding(
                "PRODUCT_ASSERTION_INVALIDATED",
                Severity.CONFLICT,
                (reference.render(),),
                "The latest evidence invalidates a current assertion.",
            )


def _decimal_total(value: Any) -> Decimal:
    if isinstance(value, bool) or isinstance(value, float):
        raise InvalidOperation
    if not isinstance(value, (int, str, Decimal)):
        raise InvalidOperation
    parsed = Decimal(str(value))
    if not parsed.is_finite():
        raise InvalidOperation
    return parsed


def _detect_trial_balance(
    current_ids: set[ScopedId],
    relations: tuple[Relation, ...],
    events: tuple[EvidenceEvent, ...],
) -> Iterable[Finding]:
    del current_ids, relations
    for event in events:
        if event.evidence_type != "TrialBalanceSnapshot":
            continue
        try:
            debit = _decimal_total(event.measurements.get("debit_total"))
            credit = _decimal_total(event.measurements.get("credit_total"))
        except (InvalidOperation, TypeError, ValueError):
            yield Finding(
                "ACCT_TRIAL_BALANCE_INSUFFICIENT_EVIDENCE",
                Severity.CONFLICT,
                (event.event_id,),
                "Trial balance totals require integers or exact decimal strings.",
            )
        else:
            if debit != credit:
                yield Finding(
                    "ACCT_TRIAL_BALANCE_UNBALANCED",
                    Severity.CONFLICT,
                    (event.event_id,),
                    "Debit and credit totals differ.",
                )
            else:
                yield Finding(
                    "ACCT_TRIAL_BALANCE_BALANCED",
                    Severity.CLEAR,
                    (event.event_id,),
                    "Debit and credit totals balance.",
                )


def _detect_unavailable_dependency(
    current_ids: set[ScopedId],
    relations: tuple[Relation, ...],
    events: tuple[EvidenceEvent, ...],
) -> Iterable[Finding]:
    by_ingredient: dict[ScopedId, list[EvidenceEvent]] = defaultdict(list)
    for event in events:
        if event.evidence_type != "InventoryCount":
            continue
        for reference in event.assertion_refs:
            if reference in current_ids:
                by_ingredient[reference].append(event)
    unavailable: set[ScopedId] = set()
    for ingredient, candidates in sorted(by_ingredient.items()):
        latest_observed = max(event.observed_at for event in candidates)
        observed_candidates = [
            event
            for event in candidates
            if event.observed_at == latest_observed
        ]
        latest_recorded = max(
            event.recorded_at for event in observed_candidates
        )
        latest = [
            event
            for event in observed_candidates
            if event.recorded_at == latest_recorded
        ]
        values = [
            event.measurements.get("available") for event in latest
        ]
        if any(type(value) is not bool for value in values):
            yield Finding(
                "MENU_INVENTORY_EVIDENCE_INVALID",
                Severity.CONFLICT,
                (
                    ingredient.render(),
                    *(event.event_id for event in sorted(
                        latest, key=lambda item: item.event_id
                    )),
                ),
                "Current inventory evidence requires a boolean available state.",
            )
            continue
        states = set(values)
        if len(states) > 1:
            yield Finding(
                "MENU_INVENTORY_EVIDENCE_AMBIGUOUS",
                Severity.CONFLICT,
                (
                    ingredient.render(),
                    *(event.event_id for event in sorted(
                        latest, key=lambda item: item.event_id
                    )),
                ),
                "Equally current inventory observations conflict.",
            )
            continue
        if states == {False}:
            unavailable.add(ingredient)
    if unavailable:
        affected_recipes = {
            relation.source
            for relation in relations
            if relation.relation == "composed-of"
            and relation.target in unavailable
            and relation.source in current_ids
        }
        affected_menu = {
            relation.source
            for relation in relations
            if relation.relation == "uses-recipe"
            and relation.target in affected_recipes
            and relation.source in current_ids
        }
        if affected_menu:
            yield Finding(
                "MENU_ACTIVE_DEPENDENCY_UNAVAILABLE",
                Severity.CONFLICT,
                tuple(
                    sorted(
                        ref.render()
                        for ref in unavailable
                        | affected_recipes
                        | affected_menu
                    )
                ),
                "An active menu item depends on an unavailable ingredient.",
            )


DETECTOR_REGISTRY: Mapping[str, Detector] = {
    "product-change-review": _detect_product_change,
    "accounting-trial-balance": _detect_trial_balance,
    "restaurant-unavailable-dependency": _detect_unavailable_dependency,
}


def run_pack_detectors(
    snapshot: Snapshot,
    pack: SchemaPack,
    valid_at: str,
    known_at: dt.datetime,
) -> tuple[Finding, ...]:
    """Run declaratively registered deterministic detectors without mutation."""

    current_ids = {
        revision.id
        for revision in _current_assertions(snapshot, pack, valid_at, known_at)
    }
    valid_limit = (
        parse_valid_point(pack, valid_at)
        if pack.valid_clock == "date"
        else None
    )
    visible_events = tuple(
        event
        for event in sorted(snapshot.evidence, key=lambda item: item.event_id)
        if event.pack == pack.pack_id
        and _is_aware(event.recorded_at)
        and event.recorded_at <= known_at
        and (
            valid_limit is None
            or (
                _is_aware(event.observed_at)
                and event.observed_at <= valid_limit
            )
        )
    )
    visible_relations = _visible_relations(
        snapshot, pack, valid_at, known_at
    )
    findings: list[Finding] = []
    for detector_name in pack.detectors:
        detector = DETECTOR_REGISTRY.get(detector_name)
        if detector is None:
            findings.append(
                Finding(
                    "CORE_DETECTOR_UNKNOWN",
                    Severity.CONFLICT,
                    (pack.pack_id, detector_name),
                    "Pack detector is not registered.",
                )
            )
            continue
        findings.extend(
            detector(current_ids, visible_relations, visible_events)
        )
    return tuple(sorted(findings))


def _current_assertions(
    snapshot: Snapshot,
    pack: SchemaPack,
    valid_at: str,
    known_at: dt.datetime,
) -> list[AssertionRevision]:
    result: list[AssertionRevision] = []
    ids = sorted(
        {revision.id for revision in snapshot.assertions if revision.id.pack == pack.pack_id}
    )
    for scoped_id in ids:
        revision = revision_at(snapshot.assertions, scoped_id, known_at)
        if revision is None:
            continue
        status = normalize_status(pack, revision.local_status)
        if status not in {
            MetaStatus.ACTIVE,
            MetaStatus.SUPERSEDED,
            MetaStatus.EXPIRED,
        }:
            continue
        if _valid_contains(revision, pack, valid_at):
            result.append(revision)
    return result


def _visible_relations(
    snapshot: Snapshot,
    pack: SchemaPack,
    valid_at: str,
    known_at: dt.datetime,
) -> tuple[Relation, ...]:
    visible: list[Relation] = []
    for relation in snapshot.relations:
        if relation.asserted_by.pack != pack.pack_id:
            continue
        asserting_revision = revision_at(
            snapshot.assertions,
            relation.asserted_by,
            known_at,
        )
        if (
            asserting_revision is None
            or asserting_revision.revision
            != relation.asserted_in_revision
        ):
            continue
        asserting_status = normalize_status(
            pack, asserting_revision.local_status
        )
        if asserting_status not in {
            MetaStatus.ACTIVE,
            MetaStatus.SUPERSEDED,
            MetaStatus.EXPIRED,
        }:
            continue
        if _valid_contains(asserting_revision, pack, valid_at):
            visible.append(relation)
    return tuple(
        sorted(
            visible,
            key=lambda relation: (
                relation.source.render(),
                relation.relation,
                relation.target.render(),
                relation.asserted_by.render(),
                relation.asserted_in_revision,
            ),
        )
    )


def evaluate_gate(
    snapshot: Snapshot,
    pack: SchemaPack,
    target: str,
    valid_at: str,
    known_at: dt.datetime,
    attestations: Sequence[GateAttestation] = (),
    readiness_score: float | None = None,
) -> GateReport:
    del readiness_score  # A score must never mask a hard conformance failure.
    try:
        gate = pack.gates[target]
    except KeyError as error:
        raise ConformanceError(
            "CORE_GATE_UNKNOWN", f"{target} is not defined by {pack.pack_id}."
        ) from error
    if pack.valid_clock == "prd_version":
        target_point = parse_valid_point(pack, target)
        gate_chain = [
            item
            for item in sorted(
                pack.gates.values(),
                key=lambda candidate: parse_valid_point(pack, candidate.target),
            )
            if parse_valid_point(pack, item.target) <= target_point
        ]
    else:
        gate_chain = [gate]
    scoped_snapshot = Snapshot(
        assertions=tuple(
            revision
            for revision in snapshot.assertions
            if revision.id.pack == pack.pack_id
        ),
        relations=tuple(
            relation
            for relation in snapshot.relations
            if pack.pack_id
            in {
                relation.source.pack,
                relation.target.pack,
                relation.asserted_by.pack,
            }
        ),
        evidence=tuple(
            event for event in snapshot.evidence if event.pack == pack.pack_id
        ),
    )
    core_findings = tuple(
        sorted(
            {
                *validate_packs((pack,)),
                *run_conformance(
                    scoped_snapshot, {pack.pack_id: pack}
                ),
            }
        )
    )
    if any(
        finding.severity is Severity.CONFLICT
        for finding in core_findings
    ):
        return GateReport(
            gate=target,
            verdict=GateVerdict.BLOCK,
            findings=core_findings,
            counted_ids={},
        )
    current = _current_assertions(snapshot, pack, valid_at, known_at)
    by_prefix: dict[str, list[AssertionRevision]] = defaultdict(list)
    for revision in current:
        by_prefix[resolve_prefix(pack, revision.id.local_id)].append(revision)
    findings: list[Finding] = list(core_findings)
    findings.extend(
        finding
        for finding in run_pack_detectors(
            scoped_snapshot,
            pack,
            valid_at,
            known_at,
        )
        if finding.severity is not Severity.CLEAR
    )
    counted: dict[str, tuple[str, ...]] = {}
    for scoped_gate in gate_chain:
        for required_prefix, minimum in sorted(
            scoped_gate.minimum_prefix_counts.items()
        ):
            aliases = scoped_gate.prefix_aliases.get(
                required_prefix, (required_prefix,)
            )
            matches = [
                revision
                for alias in aliases
                for revision in by_prefix.get(alias, ())
            ]
            counted[required_prefix] = tuple(
                sorted(revision.id.render() for revision in matches)
            )
            if len(matches) < minimum:
                findings.append(
                    Finding(
                        "GATE_REQUIRED_COUNT_MISSING",
                        Severity.CONFLICT,
                        (scoped_gate.target, required_prefix),
                        f"{required_prefix} requires {minimum}; found "
                        f"{len(matches)} current.",
                    )
                )
        for requirement in scoped_gate.required_fields:
            matches = by_prefix.get(requirement.prefix, ())
            missing = [
                revision.id.render()
                for revision in matches
                if not revision.attributes.get(requirement.field)
            ]
            if missing:
                findings.append(
                    Finding(
                        "GATE_REQUIRED_FIELD_MISSING",
                        Severity.CONFLICT,
                        (
                            scoped_gate.target,
                            requirement.prefix,
                            requirement.field,
                            *sorted(missing),
                        ),
                        f"Current {requirement.prefix} assertions require "
                        f"{requirement.field}.",
                    )
                )
    relation_keys = {
        (
            (relation.source, relation.relation, relation.target)
        )
        for relation in _visible_relations(
            snapshot, pack, valid_at, known_at
        )
    }
    current_ids = {revision.id for revision in current}
    for scoped_gate in gate_chain:
        for requirement in scoped_gate.required_edges:
            sources = by_prefix.get(requirement.from_prefix, ())
            for source in sources:
                matched = False
                for edge_source, relation, target_id in relation_keys:
                    if edge_source != source.id or relation != requirement.relation:
                        continue
                    if target_id not in current_ids:
                        continue
                    if (
                        resolve_prefix(pack, target_id.local_id)
                        == requirement.to_prefix
                    ):
                        matched = True
                        break
                if not matched:
                    findings.append(
                        Finding(
                            "GATE_REQUIRED_EDGE_MISSING",
                            Severity.CONFLICT,
                            (
                                scoped_gate.target,
                                source.id.render(),
                                requirement.relation,
                                requirement.to_prefix,
                            ),
                            "Required lifecycle traceability edge is absent.",
                        )
                    )
    attestation_map: dict[tuple[str, str], GateAttestation] = {}
    duplicate_attestations: set[tuple[str, str]] = set()
    for item in attestations:
        key = (item.gate, item.check_id)
        if key in attestation_map:
            duplicate_attestations.add(key)
        else:
            attestation_map[key] = item
    for attestation_gate, check_id in sorted(duplicate_attestations):
        findings.append(
            Finding(
                "GATE_ATTESTATION_DUPLICATE",
                Severity.CONFLICT,
                (attestation_gate, check_id),
                "Each qualitative gate check may have only one attestation.",
            )
        )
    for scoped_gate in gate_chain:
        for check_id in scoped_gate.manual_checks:
            attestation = attestation_map.get((scoped_gate.target, check_id))
            if attestation is None:
                findings.append(
                    Finding(
                        "GATE_ATTESTATION_MISSING",
                        Severity.CAUTION,
                        (scoped_gate.target, check_id),
                        "Qualitative gate check requires a provenance-bearing "
                        "attestation.",
                    )
                )
            elif not _is_aware(attestation.recorded_at):
                findings.append(
                    Finding(
                        "GATE_ATTESTATION_TIMEZONE_MISSING",
                        Severity.CONFLICT,
                        (scoped_gate.target, check_id),
                        "Gate attestation recorded_at must include a timezone.",
                    )
                )
            elif attestation.recorded_at > known_at:
                findings.append(
                    Finding(
                        "GATE_ATTESTATION_NOT_YET_RECORDED",
                        Severity.CAUTION,
                        (scoped_gate.target, check_id),
                        "A future attestation cannot satisfy a historical gate.",
                    )
                )
            elif not attestation.passed:
                findings.append(
                    Finding(
                        "GATE_ATTESTATION_FAILED",
                        Severity.CONFLICT,
                        (scoped_gate.target, check_id),
                        "Qualitative gate check was explicitly failed.",
                    )
                )
            else:
                if any(
                    not value.strip()
                    for value in dataclasses.asdict(
                        attestation.provenance
                    ).values()
                ):
                    findings.append(
                        Finding(
                            "GATE_ATTESTATION_PROVENANCE_MISSING",
                            Severity.CONFLICT,
                            (scoped_gate.target, check_id),
                            "Gate attestation is not auditable.",
                        )
                    )
                if not attestation.assertion_refs:
                    findings.append(
                        Finding(
                            "GATE_ATTESTATION_REFS_EMPTY",
                            Severity.CONFLICT,
                            (scoped_gate.target, check_id),
                            "A passing attestation must cite at least one "
                            "assertion it reviewed.",
                        )
                    )
                if len(set(attestation.assertion_refs)) != len(
                    attestation.assertion_refs
                ):
                    findings.append(
                        Finding(
                            "GATE_ATTESTATION_REFS_DUPLICATE",
                            Severity.CONFLICT,
                            (scoped_gate.target, check_id),
                            "Attestation assertion references must be unique.",
                        )
                    )
                invalid_refs = tuple(
                    sorted(
                        reference.render()
                        for reference in attestation.assertion_refs
                        if reference.pack != pack.pack_id
                        or revision_at(
                            snapshot.assertions,
                            reference,
                            known_at,
                        )
                        is None
                    )
                )
                if invalid_refs:
                    findings.append(
                        Finding(
                            "GATE_ATTESTATION_REF_INVALID",
                            Severity.CONFLICT,
                            (
                                scoped_gate.target,
                                check_id,
                                *invalid_refs,
                            ),
                            "Attestations may cite only same-pack assertions "
                            "known at evaluation time.",
                        )
                    )
    if any(item.severity is Severity.CONFLICT for item in findings):
        verdict = GateVerdict.BLOCK
    elif findings:
        verdict = GateVerdict.REVIEW
    else:
        verdict = GateVerdict.PASS
    return GateReport(
        gate=target,
        verdict=verdict,
        findings=tuple(sorted(findings)),
        counted_ids=counted,
    )


def run_conformance(
    snapshot: Snapshot, packs: Mapping[str, SchemaPack]
) -> tuple[Finding, ...]:
    validators = (
        validate_ids(snapshot, packs),
        validate_provenance(snapshot),
        validate_revision_intervals(snapshot, packs),
        validate_lifecycle(snapshot, packs),
        validate_truth_uniqueness(snapshot, packs),
        validate_supersession(snapshot, packs),
        validate_relations(snapshot, packs),
        validate_rejected_alternatives(snapshot, packs),
        validate_evidence(snapshot, packs),
    )
    return tuple(sorted({finding for group in validators for finding in group}))
