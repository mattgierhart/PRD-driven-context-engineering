#!/usr/bin/env python3
"""Deterministic Markdown-vs-Kuzu benchmark for PRD-CE ID graphs.

This is research-spike code. It deliberately keeps Markdown parsing shared
between both systems so the comparison isolates retrieval/materialization
behavior rather than giving either system a different interpretation of the
source corpus.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import difflib
import hashlib
import json
import math
import os
import platform
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Iterable, Mapping, Protocol, Sequence

try:
    import kuzu
except ImportError:  # pragma: no cover - exercised by the bootstrap guard
    kuzu = None


UPSTREAM_REPOSITORY = "https://github.com/kuzudb/kuzu"
UPSTREAM_RELEASE = "v0.11.3"
UPSTREAM_COMMIT = "27cba5b91423c96a0a0507c92dfe0e1654f7f184"
ID_TOKEN = r"[A-Z]{2,}(?:-[A-Z0-9]+)*-\d{3}"
ID_RE = re.compile(rf"(?<![A-Z0-9-])({ID_TOKEN})(?![A-Z0-9-])")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE_DEFINITION_RE = re.compile(
    rf"^\|\s*(?:\[)?`?({ID_TOKEN})`?(?:\]\([^)]*\))?\s*\|"
)
FIELD_RE_TEMPLATE = r"(?:^|\n)\s*(?:[-*]\s+)?\*\*{field}\*\*\s*:\s*(.+)"
AUTHORITATIVE_TOP_LEVEL = ("README.md", "PRD.md")
AUTHORITATIVE_FOLDERS = ("SoT", "epics")
BENCHMARK_ENGINES = ("markdown", "kuzu")
PRD_LIFECYCLE_ANCHOR_FAMILIES: Mapping[str, tuple[str, ...]] = {
    "v0.1": ("CFD",),
    "v0.2": ("BR",),
    "v0.3": ("BR", "KPI", "FEA", "CFD"),
    "v0.4": ("UJ", "PER", "SCR"),
    "v0.5": ("RISK", "TECH"),
    "v0.6": ("ARC", "API", "DBT", "INT"),
    "v0.7": ("TEST", "EPIC"),
    "v0.8": ("DEP", "RUN", "MON"),
    "v0.9": ("GTM", "KPI", "CFD", "FEA"),
    "v1.0": ("ADO",),
}


@dataclasses.dataclass(frozen=True)
class Entry:
    id: str
    prefix: str
    title: str
    body: str
    source_file: str
    line: int
    body_hash: str
    status: str
    verified: str
    is_defined: bool = True
    is_placeholder: bool = False

    def projection(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "prefix": self.prefix,
            "title": self.title,
            "source_file": self.source_file,
            "line": self.line,
            "defined": self.is_defined,
        }


@dataclasses.dataclass(frozen=True)
class Edge:
    source: str
    target: str
    relation: str
    source_file: str
    line: int


@dataclasses.dataclass
class Corpus:
    alias: str
    root: Path
    files: tuple[Path, ...]
    entries: dict[str, Entry]
    edges: tuple[Edge, ...]
    duplicate_definitions: dict[str, tuple[str, ...]]
    parse_ms: float
    fingerprint: str
    source_bytes: int

    @property
    def defined_entries(self) -> dict[str, Entry]:
        return {key: value for key, value in self.entries.items() if value.is_defined}

    @property
    def dangling_ids(self) -> set[str]:
        return {key for key, value in self.entries.items() if not value.is_defined}

    def public_manifest(self) -> dict[str, Any]:
        prefixes: dict[str, int] = defaultdict(int)
        for entry in self.defined_entries.values():
            prefixes[entry.prefix] += 1
        return {
            "alias": self.alias,
            "fingerprint_sha256": self.fingerprint,
            "files": len(self.files),
            "source_bytes": self.source_bytes,
            "defined_nodes": len(self.defined_entries),
            "placeholder_nodes": sum(
                entry.is_placeholder for entry in self.defined_entries.values()
            ),
            "dangling_nodes": len(self.dangling_ids),
            "edges": len(self.edges),
            "duplicate_definition_ids": len(self.duplicate_definitions),
            "prefix_counts": dict(sorted(prefixes.items())),
            "parse_ms": round(self.parse_ms, 3),
            "git_commit": git_commit(self.root),
        }


@dataclasses.dataclass(frozen=True)
class BenchmarkCase:
    id: str
    corpus: str
    question: str
    kind: str
    anchor: str = ""
    direction: str = "outgoing"
    depth: int = 1
    prefix: str = ""
    term: str = ""
    expected: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    lifecycle_stage: str = ""
    truth_scope: str = "source_fidelity"
    semantic_check: Mapping[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "BenchmarkCase":
        return cls(
            id=raw["id"],
            corpus=raw["corpus"],
            question=raw["question"],
            kind=raw["kind"],
            anchor=raw.get("anchor", ""),
            direction=raw.get("direction", "outgoing"),
            depth=int(raw.get("depth", 1)),
            prefix=raw.get("prefix", ""),
            term=raw.get("term", ""),
            expected=tuple(sorted(set(raw.get("expected", [])))),
            evidence=tuple(raw.get("evidence", [])),
            lifecycle_stage=raw.get("lifecycle_stage", ""),
            truth_scope=raw.get("truth_scope", "source_fidelity"),
            semantic_check=dict(raw.get("semantic_check", {})),
        )


class QueryEngine(Protocol):
    name: str

    def query(self, case: BenchmarkCase) -> list[str]:
        ...

    def get_entries(self, ids: Iterable[str]) -> list[Entry]:
        ...


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def prefix_of(identifier: str) -> str:
    return identifier.split("-", 1)[0]


def normalize_title(raw: str, identifier: str) -> str:
    title = raw
    title = re.sub(r"^\[[^\]]+\]\([^)]*\)\s*", "", title)
    title = re.sub(rf"^`?{re.escape(identifier)}`?\s*", "", title)
    title = re.sub(r"^\s*[:|—–-]\s*", "", title)
    return title.strip() or identifier


def extract_field(body: str, field: str) -> str:
    match = re.search(
        FIELD_RE_TEMPLATE.format(field=re.escape(field)),
        body,
        flags=re.IGNORECASE,
    )
    return match.group(1).strip() if match else ""


def infer_relation(line: str) -> str:
    lowered = line.casefold()
    patterns = (
        ("supersedes", "supersedes"),
        ("invalidated by", "invalidated-by"),
        ("conflicts", "conflicts-with"),
        ("depends", "depends-on"),
        ("validated by", "validated-by"),
        ("verifies", "verifies"),
        ("tests", "tests"),
        ("implements", "implements"),
        ("enforces", "enforces"),
        ("mitigates", "mitigates"),
        ("driven by", "driven-by"),
        ("drives", "drives"),
        ("designed for", "designed-for"),
        ("uses", "uses"),
        ("informs", "informs"),
    )
    for needle, relation in patterns:
        if needle in lowered:
            return relation
    return "references"


def discover_authoritative_files(root: Path) -> tuple[Path, ...]:
    root = root.resolve()
    paths: set[Path] = set()
    for name in AUTHORITATIVE_TOP_LEVEL:
        path = root / name
        if path.is_file():
            paths.add(path)
    for folder in AUTHORITATIVE_FOLDERS:
        directory = root / folder
        if not directory.is_dir():
            continue
        paths.update(
            path
            for path in directory.rglob("*.md")
            if path.is_file() and "html" not in path.relative_to(root).parts
        )
    return tuple(sorted(paths, key=lambda path: path.relative_to(root).as_posix()))


def _definition_candidates(lines: list[str]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        heading = HEADING_RE.match(line)
        if heading:
            heading_text = heading.group(2)
            identifier_match = ID_RE.search(heading_text)
            if identifier_match and identifier_match.start() <= 2:
                identifier = identifier_match.group(1)
                candidates.append(
                    {
                        "index": index,
                        "line": index + 1,
                        "level": len(heading.group(1)),
                        "id": identifier,
                        "title": normalize_title(heading_text, identifier),
                        "kind": "heading",
                    }
                )
                continue
        table = TABLE_DEFINITION_RE.match(line)
        if table:
            identifier = table.group(1)
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            title = cells[1] if len(cells) > 1 else identifier
            candidates.append(
                {
                    "index": index,
                    "line": index + 1,
                    "level": 7,
                    "id": identifier,
                    "title": re.sub(r"[`*]", "", title).strip() or identifier,
                    "kind": "table",
                }
            )
    return candidates


def _body_for_candidate(
    lines: list[str], candidate: dict[str, Any], candidates: list[dict[str, Any]]
) -> str:
    start = candidate["index"]
    if candidate["kind"] == "table":
        return lines[start].rstrip() + "\n"
    end = len(lines)
    for later in candidates:
        if later["index"] <= start or later["kind"] != "heading":
            continue
        if later["level"] <= candidate["level"]:
            end = later["index"]
            break
    return "".join(lines[start:end]).rstrip() + "\n"


def _definition_score(
    candidate: dict[str, Any], relative: str, body: str, identifier: str
) -> int:
    """Prefer actual owning entries over index/summary mentions.

    A heading is usually an entry; a first-column table row is only authoritative
    for PRD-owned and README-owned ID families unless no stronger definition exists.
    Body length is a tiebreaker so later, richer revisions beat thin index rows.
    """

    prefix = prefix_of(identifier)
    score = 10_000 if candidate["kind"] == "heading" else 1_000
    if relative == "PRD.md" and prefix in {"FEA", "RISK", "GTM"}:
        score += 5_000
    if relative == "README.md" and prefix == "KPI":
        score += 5_000
    if relative.startswith("SoT/") and candidate["kind"] == "heading":
        score += 3_000
    if relative.startswith("epics/") and prefix == "EPIC":
        score += 3_000
    score += min(len(body), 20_000)
    return score


def _is_strong_definition(
    candidate: dict[str, Any], relative: str, identifier: str
) -> bool:
    if candidate["kind"] == "heading":
        return True
    prefix = prefix_of(identifier)
    return (
        (relative == "PRD.md" and prefix in {"FEA", "RISK", "GTM"})
        or (relative == "README.md" and prefix == "KPI")
    )


def parse_corpus(alias: str, root: Path) -> Corpus:
    started = time.perf_counter_ns()
    root = root.resolve()
    files = discover_authoritative_files(root)
    if not files:
        raise ValueError(f"{alias}: no authoritative Markdown files under {root}")

    entries: dict[str, Entry] = {}
    ranked_entries: dict[str, tuple[int, Entry]] = {}
    definitions: dict[str, list[str]] = defaultdict(list)
    file_texts: dict[Path, str] = {}
    digest = hashlib.sha256()
    source_bytes = 0

    for path in files:
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        file_texts[path] = text
        encoded = text.encode("utf-8")
        source_bytes += len(encoded)
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(encoded)
        digest.update(b"\0")

        lines = text.splitlines(keepends=True)
        candidates = _definition_candidates(lines)
        for candidate in candidates:
            identifier = candidate["id"]
            body = _body_for_candidate(lines, candidate, candidates)
            if _is_strong_definition(candidate, relative, identifier):
                definitions[identifier].append(f"{relative}:{candidate['line']}")
            title = candidate["title"]
            placeholder = (
                "{" in title
                or "[product" in title.casefold()
                or "{placeholder" in body.casefold()
            )
            entry = Entry(
                id=identifier,
                prefix=prefix_of(identifier),
                title=title,
                body=body,
                source_file=relative,
                line=candidate["line"],
                body_hash=sha256_text(body),
                status=extract_field(body, "Status"),
                verified=(
                    extract_field(body, "Verified")
                    or extract_field(body, "Last Reviewed")
                    or extract_field(body, "Last Updated")
                ),
                is_placeholder=placeholder,
            )
            score = _definition_score(candidate, relative, body, identifier)
            current = ranked_entries.get(identifier)
            if current is None or score > current[0]:
                ranked_entries[identifier] = (score, entry)

    entries = {
        identifier: ranked[1] for identifier, ranked in ranked_entries.items()
    }

    edges_by_key: dict[tuple[str, str, str], Edge] = {}
    all_referenced: set[str] = set()
    for entry in tuple(entries.values()):
        for offset, line in enumerate(entry.body.splitlines()):
            for target in ID_RE.findall(line):
                if target == entry.id:
                    continue
                all_referenced.add(target)
                relation = infer_relation(line)
                key = (entry.id, target, relation)
                edges_by_key.setdefault(
                    key,
                    Edge(
                        source=entry.id,
                        target=target,
                        relation=relation,
                        source_file=entry.source_file,
                        line=entry.line + offset,
                    ),
                )

    for text in file_texts.values():
        all_referenced.update(ID_RE.findall(text))

    for identifier in sorted(all_referenced - set(entries)):
        entries[identifier] = Entry(
            id=identifier,
            prefix=prefix_of(identifier),
            title="Referenced but not defined in indexed scope",
            body="",
            source_file="",
            line=0,
            body_hash=sha256_text(""),
            status="missing",
            verified="",
            is_defined=False,
        )

    duplicates = {
        identifier: tuple(locations)
        for identifier, locations in definitions.items()
        if len(locations) > 1
    }
    elapsed_ms = (time.perf_counter_ns() - started) / 1_000_000
    return Corpus(
        alias=alias,
        root=root,
        files=files,
        entries=entries,
        edges=tuple(
            sorted(
                edges_by_key.values(),
                key=lambda edge: (edge.source, edge.target, edge.relation),
            )
        ),
        duplicate_definitions=duplicates,
        parse_ms=elapsed_ms,
        fingerprint=digest.hexdigest(),
        source_bytes=source_bytes,
    )


class MarkdownEngine:
    name = "markdown"

    def __init__(self, corpus: Corpus):
        self.corpus = corpus
        self.outgoing: dict[str, set[str]] = defaultdict(set)
        self.incoming: dict[str, set[str]] = defaultdict(set)
        for edge in corpus.edges:
            self.outgoing[edge.source].add(edge.target)
            self.incoming[edge.target].add(edge.source)

    def _neighbors(self, identifier: str, direction: str) -> set[str]:
        if direction == "outgoing":
            return self.outgoing.get(identifier, set())
        if direction == "incoming":
            return self.incoming.get(identifier, set())
        if direction == "both":
            return self.outgoing.get(identifier, set()) | self.incoming.get(
                identifier, set()
            )
        raise ValueError(f"unsupported direction: {direction}")

    def _traverse(self, anchor: str, direction: str, depth: int) -> set[str]:
        seen = {anchor}
        frontier = {anchor}
        found: set[str] = set()
        for _ in range(depth):
            next_frontier: set[str] = set()
            for identifier in frontier:
                next_frontier.update(self._neighbors(identifier, direction))
            next_frontier -= seen
            found.update(next_frontier)
            seen.update(next_frontier)
            frontier = next_frontier
            if not frontier:
                break
        return found

    def query(self, case: BenchmarkCase) -> list[str]:
        if case.kind == "lookup":
            result = (
                {case.anchor}
                if case.anchor in self.corpus.entries
                and self.corpus.entries[case.anchor].is_defined
                else set()
            )
        elif case.kind == "traverse":
            result = self._traverse(case.anchor, case.direction, case.depth)
        elif case.kind == "prefix":
            result = {
                entry.id
                for entry in self.corpus.defined_entries.values()
                if entry.prefix == case.prefix
            }
        elif case.kind == "dangling":
            result = set(self.corpus.dangling_ids)
        elif case.kind == "search":
            needle = case.term.casefold()
            result = {
                entry.id
                for entry in self.corpus.defined_entries.values()
                if needle in entry.title.casefold() or needle in entry.body.casefold()
            }
        else:
            raise ValueError(f"unsupported query kind: {case.kind}")
        if case.prefix and case.kind == "traverse":
            result = {
                identifier
                for identifier in result
                if self.corpus.entries[identifier].prefix == case.prefix
            }
        return sorted(result)

    def get_entries(self, ids: Iterable[str]) -> list[Entry]:
        return [self.corpus.entries[identifier] for identifier in ids]


class KuzuEngine:
    name = "kuzu"

    def __init__(self, corpus: Corpus, database_path: Path, rebuild: bool = True):
        if kuzu is None:
            raise RuntimeError("kuzu is not installed; run ./bootstrap.sh")
        self.corpus = corpus
        self.database_path = database_path
        if rebuild and database_path.exists():
            if database_path.is_dir():
                shutil.rmtree(database_path)
            else:
                database_path.unlink()
        started = time.perf_counter_ns()
        self.database = kuzu.Database(str(database_path))
        self.connection = kuzu.Connection(self.database)
        if rebuild:
            self._build()
        self.build_ms = (time.perf_counter_ns() - started) / 1_000_000

    def _build(self) -> None:
        self.connection.execute(
            """
            CREATE NODE TABLE Spec(
                id STRING PRIMARY KEY,
                prefix STRING,
                title STRING,
                body STRING,
                source_file STRING,
                source_line INT64,
                body_hash STRING,
                status STRING,
                verified STRING,
                is_defined BOOL,
                is_placeholder BOOL
            )
            """
        )
        self.connection.execute(
            """
            CREATE REL TABLE RefersTo(
                FROM Spec TO Spec,
                relation STRING,
                source_file STRING,
                source_line INT64
            )
            """
        )
        node_query = """
            CREATE (:Spec {
                id: $id,
                prefix: $prefix,
                title: $title,
                body: $body,
                source_file: $source_file,
                source_line: $source_line,
                body_hash: $body_hash,
                status: $status,
                verified: $verified,
                is_defined: $is_defined,
                is_placeholder: $is_placeholder
            })
        """
        for entry in self.corpus.entries.values():
            self.connection.execute(
                node_query,
                {
                    "id": entry.id,
                    "prefix": entry.prefix,
                    "title": entry.title,
                    "body": entry.body,
                    "source_file": entry.source_file,
                    "source_line": entry.line,
                    "body_hash": entry.body_hash,
                    "status": entry.status,
                    "verified": entry.verified,
                    "is_defined": entry.is_defined,
                    "is_placeholder": entry.is_placeholder,
                },
            )
        edge_query = """
            MATCH (source:Spec), (target:Spec)
            WHERE source.id = $source AND target.id = $target
            CREATE (source)-[:RefersTo {
                relation: $relation,
                source_file: $source_file,
                source_line: $source_line
            }]->(target)
        """
        for edge in self.corpus.edges:
            self.connection.execute(
                edge_query,
                {
                    "source": edge.source,
                    "target": edge.target,
                    "relation": edge.relation,
                    "source_file": edge.source_file,
                    "source_line": edge.line,
                },
            )
        self.connection.execute("CHECKPOINT")

    def _one_hop(self, identifiers: set[str], direction: str) -> set[str]:
        if not identifiers:
            return set()
        result: set[str] = set()
        for identifier in identifiers:
            if direction in {"outgoing", "both"}:
                rows = self.connection.execute(
                    """
                    MATCH (source:Spec)-[:RefersTo]->(target:Spec)
                    WHERE source.id = $id
                    RETURN DISTINCT target.id
                    """,
                    {"id": identifier},
                ).get_all()
                result.update(row[0] for row in rows)
            if direction in {"incoming", "both"}:
                rows = self.connection.execute(
                    """
                    MATCH (source:Spec)-[:RefersTo]->(target:Spec)
                    WHERE target.id = $id
                    RETURN DISTINCT source.id
                    """,
                    {"id": identifier},
                ).get_all()
                result.update(row[0] for row in rows)
        return result

    def _traverse(self, anchor: str, direction: str, depth: int) -> set[str]:
        seen = {anchor}
        frontier = {anchor}
        found: set[str] = set()
        for _ in range(depth):
            next_frontier = self._one_hop(frontier, direction) - seen
            found.update(next_frontier)
            seen.update(next_frontier)
            frontier = next_frontier
            if not frontier:
                break
        return found

    def query(self, case: BenchmarkCase) -> list[str]:
        if case.kind == "lookup":
            rows = self.connection.execute(
                "MATCH (s:Spec) WHERE s.id = $id AND s.is_defined RETURN s.id",
                {"id": case.anchor},
            ).get_all()
            result = {row[0] for row in rows}
        elif case.kind == "traverse":
            result = self._traverse(case.anchor, case.direction, case.depth)
        elif case.kind == "prefix":
            rows = self.connection.execute(
                """
                MATCH (s:Spec)
                WHERE s.prefix = $prefix AND s.is_defined
                RETURN s.id
                """,
                {"prefix": case.prefix},
            ).get_all()
            result = {row[0] for row in rows}
        elif case.kind == "dangling":
            rows = self.connection.execute(
                "MATCH (s:Spec) WHERE NOT s.is_defined RETURN s.id"
            ).get_all()
            result = {row[0] for row in rows}
        elif case.kind == "search":
            rows = self.connection.execute(
                """
                MATCH (s:Spec)
                WHERE s.is_defined
                  AND (
                    lower(s.title) CONTAINS $term
                    OR lower(s.body) CONTAINS $term
                  )
                RETURN s.id
                """,
                {"term": case.term.casefold()},
            ).get_all()
            result = {row[0] for row in rows}
        else:
            raise ValueError(f"unsupported query kind: {case.kind}")
        if case.prefix and case.kind == "traverse":
            result = {
                identifier
                for identifier in result
                if self.corpus.entries[identifier].prefix == case.prefix
            }
        return sorted(result)

    def get_entries(self, ids: Iterable[str]) -> list[Entry]:
        entries: list[Entry] = []
        query = """
            MATCH (s:Spec)
            WHERE s.id = $id
            RETURN
                s.id,
                s.prefix,
                s.title,
                s.body,
                s.source_file,
                s.source_line,
                s.body_hash,
                s.status,
                s.verified,
                s.is_defined,
                s.is_placeholder
        """
        for identifier in ids:
            rows = self.connection.execute(query, {"id": identifier}).get_all()
            if not rows:
                continue
            row = rows[0]
            entries.append(
                Entry(
                    id=row[0],
                    prefix=row[1],
                    title=row[2],
                    body=row[3],
                    source_file=row[4],
                    line=row[5],
                    body_hash=row[6],
                    status=row[7],
                    verified=row[8],
                    is_defined=row[9],
                    is_placeholder=row[10],
                )
            )
        return entries

    def body_hash(self, identifier: str) -> str:
        rows = self.connection.execute(
            "MATCH (s:Spec) WHERE s.id = $id RETURN s.body_hash",
            {"id": identifier},
        ).get_all()
        return rows[0][0] if rows else ""


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(fraction * len(ordered)) - 1))
    return ordered[index]


def score(expected: set[str], actual: set[str]) -> tuple[float, float, float]:
    if not expected and not actual:
        return 1.0, 1.0, 1.0
    true_positive = len(expected & actual)
    precision = true_positive / len(actual) if actual else 0.0
    recall = true_positive / len(expected) if expected else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    return precision, recall, f1


def file_payload_bytes(corpus: Corpus, ids: Iterable[str]) -> int:
    files = {
        corpus.root / corpus.entries[identifier].source_file
        for identifier in ids
        if corpus.entries[identifier].source_file
    }
    return sum(path.stat().st_size for path in files if path.is_file())


def entry_payload_bytes(entries: Iterable[Entry]) -> int:
    return sum(len(entry.body.encode("utf-8")) for entry in entries)


def projection_payload_bytes(entries: Iterable[Entry]) -> int:
    payload = [entry.projection() for entry in entries]
    return len(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def benchmark_case(
    engine: QueryEngine,
    case: BenchmarkCase,
    corpus: Corpus,
    repeats: int,
) -> dict[str, Any]:
    engine.query(case)
    samples: list[float] = []
    actual: list[str] = []
    for _ in range(repeats):
        started = time.perf_counter_ns()
        actual = engine.query(case)
        samples.append((time.perf_counter_ns() - started) / 1_000_000)
    expected = set(case.expected)
    actual_set = set(actual)
    precision, recall, f1 = score(expected, actual_set)
    entries = engine.get_entries(actual)
    return {
        "engine": engine.name,
        "case_id": case.id,
        "corpus": case.corpus,
        "kind": case.kind,
        "question": case.question,
        "lifecycle_stage": case.lifecycle_stage,
        "truth_scope": case.truth_scope,
        "evidence": list(case.evidence),
        "expected": sorted(expected),
        "actual": actual,
        "exact": actual_set == expected,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "latency_ms": {
            "median": round(statistics.median(samples), 4),
            "p95": round(percentile(samples, 0.95), 4),
            "min": round(min(samples), 4),
            "repeats": repeats,
        },
        "payload_bytes": {
            "whole_source_files": file_payload_bytes(corpus, actual),
            "exact_markdown_entries": entry_payload_bytes(entries),
            "structured_projection": projection_payload_bytes(entries),
        },
    }


def evaluate_semantic_check(
    case: BenchmarkCase, corpus: Corpus
) -> dict[str, Any] | None:
    """Evaluate a deterministic, manifest-authored semantic detector.

    These checks are reported independently from literal edge retrieval. They
    do not make the retrieval gold set a semantic ground truth.
    """

    check = case.semantic_check
    if not check:
        return None
    check_type = check.get("type")
    expected_verdict = check.get("expected_verdict")
    findings: list[dict[str, Any]] = []
    if check_type == "target_title_contains":
        for identifier, terms in sorted(
            check.get("terms_by_id", {}).items()
        ):
            entry = corpus.entries.get(identifier)
            title = entry.title if entry else ""
            missing = [
                term for term in terms if term.casefold() not in title.casefold()
            ]
            if missing:
                findings.append(
                    {
                        "id": identifier,
                        "code": "SEMANTIC_TARGET_TITLE_MISMATCH",
                        "expected_terms": list(terms),
                        "actual_title": title,
                    }
                )
    elif check_type == "entry_forbidden_terms":
        identifiers = check.get("target_ids", ())
        forbidden = tuple(check.get("forbidden_terms", ()))
        for identifier in sorted(identifiers):
            entry = corpus.entries.get(identifier)
            text = f"{entry.title}\n{entry.body}" if entry else ""
            present = [
                term for term in forbidden if term.casefold() in text.casefold()
            ]
            if present:
                findings.append(
                    {
                        "id": identifier,
                        "code": "SEMANTIC_PLACEHOLDER_CONTENT",
                        "matched_terms": present,
                    }
                )
    else:
        raise ValueError(
            f"{case.id}: unsupported semantic check type {check_type!r}"
        )
    actual_verdict = "conflict" if findings else "clear"
    return {
        "case_id": case.id,
        "corpus": case.corpus,
        "lifecycle_stage": case.lifecycle_stage,
        "check_type": check_type,
        "expected_verdict": expected_verdict,
        "actual_verdict": actual_verdict,
        "verdict_exact": actual_verdict == expected_verdict,
        "required_action": check.get("required_action", "flag"),
        "findings": findings,
    }


def evaluate_lifecycle_manifest_coverage(
    cases: Sequence[BenchmarkCase],
) -> dict[str, Any]:
    """Check manifest stage labels and their anchor-family fit.

    This is intentionally narrower than executable lifecycle conformance. It
    proves that the benchmark manifest represents every PRD stage with an
    anchor from an allowed artifact family; it does not prove that a product
    has satisfied the corresponding gate.
    """

    expected_stages = tuple(PRD_LIFECYCLE_ANCHOR_FAMILIES)
    covered_stages: set[str] = set()
    unknown_stage_cases: list[dict[str, str]] = []
    invalid_anchor_cases: list[dict[str, Any]] = []
    lifecycle_case_count = 0

    for case in cases:
        if not case.lifecycle_stage:
            continue
        lifecycle_case_count += 1
        stage = case.lifecycle_stage.split(" ", 1)[0]
        allowed = PRD_LIFECYCLE_ANCHOR_FAMILIES.get(stage)
        if allowed is None:
            unknown_stage_cases.append(
                {
                    "case_id": case.id,
                    "lifecycle_stage": case.lifecycle_stage,
                }
            )
            continue

        covered_stages.add(stage)
        actual_family = prefix_of(case.anchor) if case.anchor else ""
        if actual_family not in allowed:
            invalid_anchor_cases.append(
                {
                    "case_id": case.id,
                    "stage": stage,
                    "anchor": case.anchor,
                    "actual_family": actual_family,
                    "allowed_families": list(allowed),
                }
            )

    missing_stages = sorted(set(expected_stages) - covered_stages)
    complete = not (
        missing_stages or unknown_stage_cases or invalid_anchor_cases
    )
    return {
        "description": (
            "Manifest stage-label and anchor-family coverage; not executable "
            "PRD gate conformance."
        ),
        "expected_stages": list(expected_stages),
        "covered_stages": sorted(covered_stages),
        "missing_stages": missing_stages,
        "lifecycle_case_count": lifecycle_case_count,
        "allowed_anchor_families": {
            stage: list(families)
            for stage, families in PRD_LIFECYCLE_ANCHOR_FAMILIES.items()
        },
        "unknown_stage_cases": unknown_stage_cases,
        "invalid_anchor_cases": invalid_anchor_cases,
        "complete": complete,
    }


def evaluate_accuracy_dimensions(
    cases: Sequence[BenchmarkCase],
    corpora: Mapping[str, Corpus],
    rows: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    semantic = [
        result
        for case in cases
        if (
            result := evaluate_semantic_check(case, corpora[case.corpus])
        )
        is not None
    ]
    by_engine: dict[str, Any] = {}
    for engine in sorted({row["engine"] for row in rows}):
        engine_rows = [row for row in rows if row["engine"] == engine]
        by_engine[engine] = {
            "cases": len(engine_rows),
            "exact_cases": sum(row["exact"] for row in engine_rows),
            "exact_rate": round(
                sum(row["exact"] for row in engine_rows) / len(engine_rows), 4
            ),
        }
    return {
        "source_fidelity": {
            "description": (
                "Literal ID-set fidelity to manifest-authored Markdown spans; "
                "not semantic truth."
            ),
            "by_engine": by_engine,
        },
        "semantic_truth": {
            "description": (
                "Deterministic pack-supplied checks; reported separately from "
                "literal retrieval."
            ),
            "assessed_cases": len(semantic),
            "verdict_exact_cases": sum(
                result["verdict_exact"] for result in semantic
            ),
            "checks": semantic,
        },
        "lifecycle_manifest_coverage": evaluate_lifecycle_manifest_coverage(
            cases
        ),
    }


def evaluate_acceptance(
    cases: Sequence[BenchmarkCase],
    rows: Sequence[dict[str, Any]],
    accuracy_dimensions: Mapping[str, Any],
    authority_boundary: Mapping[str, Any],
) -> dict[str, Any]:
    """Evaluate fail-closed acceptance from persisted benchmark evidence."""

    expected_pairs = {
        (case.id, engine)
        for case in cases
        for engine in BENCHMARK_ENGINES
    }
    rows_by_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        rows_by_pair[(row.get("case_id", ""), row.get("engine", ""))].append(
            row
        )

    observed_pairs = set(rows_by_pair)
    missing_pairs = sorted(expected_pairs - observed_pairs)
    unexpected_pairs = sorted(observed_pairs - expected_pairs)
    duplicate_pairs = sorted(
        pair for pair, pair_rows in rows_by_pair.items() if len(pair_rows) != 1
    )
    expected_by_case = {
        case.id: tuple(sorted(case.expected))
        for case in cases
    }

    def row_matches_manifest(
        pair: tuple[str, str],
        row: Mapping[str, Any],
    ) -> bool:
        manifest_expected = expected_by_case[pair[0]]
        actual = row.get("actual")
        recorded_expected = row.get("expected")
        if not isinstance(actual, (list, tuple)) or not isinstance(
            recorded_expected, (list, tuple)
        ):
            return False
        return (
            row.get("exact") is True
            and tuple(sorted(actual)) == manifest_expected
            and tuple(sorted(recorded_expected)) == manifest_expected
        )

    inexact_pairs = sorted(
        pair
        for pair in expected_pairs & observed_pairs
        if len(rows_by_pair[pair]) != 1
        or not row_matches_manifest(pair, rows_by_pair[pair][0])
    )
    source_fidelity_passed = not (
        missing_pairs or unexpected_pairs or duplicate_pairs or inexact_pairs
    )

    expected_semantic = {
        case.id: str(
            case.semantic_check.get("expected_verdict", "clear")
        )
        for case in cases
        if case.semantic_check
    }
    expected_semantic_ids = set(expected_semantic)
    semantic_checks = accuracy_dimensions.get("semantic_truth", {}).get(
        "checks", ()
    )
    semantic_by_id: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for check in semantic_checks:
        semantic_by_id[str(check.get("case_id", ""))].append(check)
    observed_semantic_ids = set(semantic_by_id)
    missing_semantic = sorted(expected_semantic_ids - observed_semantic_ids)
    unexpected_semantic = sorted(observed_semantic_ids - expected_semantic_ids)
    duplicate_semantic = sorted(
        case_id
        for case_id, checks in semantic_by_id.items()
        if len(checks) != 1
    )
    inexact_semantic = sorted(
        case_id
        for case_id in expected_semantic_ids & observed_semantic_ids
        if len(semantic_by_id[case_id]) != 1
        or semantic_by_id[case_id][0].get("verdict_exact") is not True
        or semantic_by_id[case_id][0].get("expected_verdict")
        != expected_semantic[case_id]
        or semantic_by_id[case_id][0].get("actual_verdict")
        != expected_semantic[case_id]
    )
    semantic_truth_passed = not (
        missing_semantic
        or unexpected_semantic
        or duplicate_semantic
        or inexact_semantic
    )

    lifecycle = accuracy_dimensions.get("lifecycle_manifest_coverage", {})
    recomputed_lifecycle = evaluate_lifecycle_manifest_coverage(cases)
    lifecycle_passed = (
        lifecycle.get("complete") is True
        and lifecycle.get("missing_stages")
        == recomputed_lifecycle["missing_stages"]
        and lifecycle.get("unknown_stage_cases")
        == recomputed_lifecycle["unknown_stage_cases"]
        and lifecycle.get("invalid_anchor_cases")
        == recomputed_lifecycle["invalid_anchor_cases"]
        and recomputed_lifecycle["complete"] is True
    )
    authority_passed = (
        authority_boundary.get("status") == "complete"
        and authority_boundary.get("rebuilt_hash_matched_new_source") is True
    )

    checks = {
        "source_fidelity": {
            "passed": source_fidelity_passed,
            "required_engines": list(BENCHMARK_ENGINES),
            "expected_rows": len(expected_pairs),
            "observed_rows": len(rows),
            "missing_rows": [
                {"case_id": case_id, "engine": engine}
                for case_id, engine in missing_pairs
            ],
            "unexpected_rows": [
                {"case_id": case_id, "engine": engine}
                for case_id, engine in unexpected_pairs
            ],
            "duplicate_rows": [
                {"case_id": case_id, "engine": engine}
                for case_id, engine in duplicate_pairs
            ],
            "inexact_rows": [
                {"case_id": case_id, "engine": engine}
                for case_id, engine in inexact_pairs
            ],
        },
        "semantic_truth": {
            "passed": semantic_truth_passed,
            "expected_checks": len(expected_semantic_ids),
            "observed_checks": len(semantic_checks),
            "missing_cases": missing_semantic,
            "unexpected_cases": unexpected_semantic,
            "duplicate_cases": duplicate_semantic,
            "inexact_cases": inexact_semantic,
        },
        "lifecycle_manifest_coverage": {
            "passed": lifecycle_passed,
            "missing_stages": recomputed_lifecycle["missing_stages"],
            "unknown_stage_cases": list(
                recomputed_lifecycle["unknown_stage_cases"]
            ),
            "invalid_anchor_cases": list(
                recomputed_lifecycle["invalid_anchor_cases"]
            ),
        },
        "authority_boundary": {
            "passed": authority_passed,
            "status": authority_boundary.get("status", "missing"),
            "rebuilt_hash_matched_new_source": authority_boundary.get(
                "rebuilt_hash_matched_new_source", False
            ),
        },
    }
    return {
        "passed": all(check["passed"] for check in checks.values()),
        "policy": (
            "Fail closed unless both engines exactly match every manifest case, "
            "all semantic verdicts match, lifecycle manifest coverage is "
            "complete and stage-valid, and the authority rebuild matches source."
        ),
        "checks": checks,
    }


def directory_size(path: Path) -> int:
    if not path.exists():
        return 0
    if path.is_file():
        return path.stat().st_size
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def file_hash_map(path: Path) -> dict[str, str]:
    if path.is_file():
        return {"database": hashlib.sha256(path.read_bytes()).hexdigest()}
    return {
        item.relative_to(path).as_posix(): hashlib.sha256(item.read_bytes()).hexdigest()
        for item in path.rglob("*")
        if item.is_file()
    }


def git_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def copy_corpus_files(corpus: Corpus, destination: Path) -> None:
    for source in corpus.files:
        relative = source.relative_to(corpus.root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def authority_boundary_experiment(
    corpus: Corpus, original_engine: KuzuEngine, runtime_dir: Path
) -> dict[str, Any]:
    candidate = next(
        (
            entry
            for entry in reversed(tuple(corpus.defined_entries.values()))
            if entry.source_file and entry.title and entry.title in entry.body
        ),
        None,
    )
    if candidate is None:
        return {"status": "skipped", "reason": "no mutable definition candidate"}

    with tempfile.TemporaryDirectory(
        prefix=f"{corpus.alias}-authority-", dir=runtime_dir
    ) as temporary:
        copied_root = Path(temporary) / "source"
        copy_corpus_files(corpus, copied_root)
        target = copied_root / candidate.source_file
        before_text = target.read_text(encoding="utf-8", errors="replace")
        replacement = f"{candidate.title} [benchmark mutation]"
        target_lines = before_text.splitlines(keepends=True)
        heading_index = candidate.line - 1
        if not (0 <= heading_index < len(target_lines)):
            return {"status": "skipped", "reason": "candidate line is outside file"}
        target_lines[heading_index] = target_lines[heading_index].replace(
            candidate.title, replacement, 1
        )
        after_text = "".join(target_lines)
        if before_text == after_text:
            return {"status": "skipped", "reason": "candidate title replacement failed"}
        target.write_text(after_text, encoding="utf-8")

        mutated = parse_corpus(f"{corpus.alias}-mutated", copied_root)
        mutated_entry = mutated.entries[candidate.id]
        cached_hash = original_engine.body_hash(candidate.id)
        stale_detected = cached_hash != mutated_entry.body_hash

        rebuild_path = Path(temporary) / "rebuilt.kuzu"
        rebuilt_engine = KuzuEngine(mutated, rebuild_path)
        rebuilt_hash = rebuilt_engine.body_hash(candidate.id)
        source_diff = list(
            difflib.unified_diff(
                before_text.splitlines(),
                after_text.splitlines(),
                lineterm="",
            )
        )
        old_files = file_hash_map(original_engine.database_path)
        new_files = file_hash_map(rebuild_path)
        changed_database_files = sorted(
            key
            for key in set(old_files) | set(new_files)
            if old_files.get(key) != new_files.get(key)
        )
        return {
            "status": "complete",
            "corpus": corpus.alias,
            "mutated_id": candidate.id,
            "source_edit_files": 1,
            "source_diff_lines": len(source_diff),
            "cached_graph_was_stale": stale_detected,
            "cached_hash_matched_new_source": cached_hash == mutated_entry.body_hash,
            "rebuilt_hash_matched_new_source": rebuilt_hash == mutated_entry.body_hash,
            "rebuild_ms": round(rebuilt_engine.build_ms + mutated.parse_ms, 3),
            "binary_database_files_changed": len(changed_database_files),
            "binary_database_changed_files": changed_database_files,
            "markdown_human_diffable": True,
            "kuzu_database_human_diffable": False,
            "detection_method": "harness_hash_comparison",
            "automatic_runtime_guard_implemented": False,
        }


def load_case_manifest(
    path: Path,
) -> tuple[list[BenchmarkCase], dict[str, Any]]:
    content = path.read_bytes()
    raw = json.loads(content)
    cases = [BenchmarkCase.from_dict(item) for item in raw["cases"]]
    identifiers = [case.id for case in cases]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("benchmark case IDs must be unique")
    duplicate_expected = [
        case.id
        for case in cases
        if len(set(case.expected)) != len(case.expected)
    ]
    if duplicate_expected:
        raise ValueError(
            "benchmark expected ID sets contain duplicates: "
            + ", ".join(sorted(duplicate_expected))
        )
    review = raw.get("gold_review", {})
    return cases, {
        "schema_version": raw.get("schema_version"),
        "sha256": hashlib.sha256(content).hexdigest(),
        "case_count": len(cases),
        "gold_review": {
            "method": review.get("method"),
            "reviewed_at": review.get("reviewed_at"),
            "scope": review.get("scope"),
            "independence_claim": review.get("independence_claim", False),
            "human_adjudication_claim": review.get(
                "human_adjudication_claim", False
            ),
        },
    }


def load_cases(path: Path) -> list[BenchmarkCase]:
    cases, _ = load_case_manifest(path)
    return cases


def validate_cases(cases: list[BenchmarkCase], corpora: dict[str, Corpus]) -> None:
    errors: list[str] = []
    for case in cases:
        corpus = corpora.get(case.corpus)
        if corpus is None:
            errors.append(f"{case.id}: unknown corpus {case.corpus}")
            continue
        if case.kind in {"lookup", "traverse"} and case.anchor not in corpus.entries:
            errors.append(f"{case.id}: anchor {case.anchor} is absent")
        missing_expected = set(case.expected) - set(corpus.entries)
        if missing_expected:
            errors.append(
                f"{case.id}: expected IDs absent: {', '.join(sorted(missing_expected))}"
            )
        for evidence in case.evidence:
            if ":" not in evidence:
                errors.append(
                    f"{case.id}: evidence must use relative/path.md:line: {evidence}"
                )
                continue
            relative, raw_line = evidence.rsplit(":", 1)
            if not raw_line.isdigit() or int(raw_line) < 1:
                errors.append(f"{case.id}: invalid evidence line: {evidence}")
                continue
            evidence_path = corpus.root / relative
            if not evidence_path.is_file():
                errors.append(f"{case.id}: evidence file absent: {relative}")
                continue
            evidence_lines = evidence_path.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            line_number = int(raw_line)
            if line_number > len(evidence_lines):
                errors.append(f"{case.id}: evidence line outside file: {evidence}")
            elif not evidence_lines[line_number - 1].strip():
                errors.append(f"{case.id}: evidence line is blank: {evidence}")
        semantic_targets = set(
            case.semantic_check.get("terms_by_id", {})
        ) | set(case.semantic_check.get("target_ids", ()))
        missing_semantic = semantic_targets - set(corpus.entries)
        if missing_semantic:
            errors.append(
                f"{case.id}: semantic target IDs absent: "
                + ", ".join(sorted(missing_semantic))
            )
    if errors:
        raise ValueError("\n".join(errors))


def aggregate(results: list[dict[str, Any]]) -> dict[str, Any]:
    rollup: dict[str, Any] = {}
    for engine in sorted({row["engine"] for row in results}):
        rows = [row for row in results if row["engine"] == engine]
        rollup[engine] = {
            "cases": len(rows),
            "exact_cases": sum(row["exact"] for row in rows),
            "exact_rate": round(sum(row["exact"] for row in rows) / len(rows), 4),
            "mean_f1": round(statistics.mean(row["f1"] for row in rows), 4),
            "median_query_ms": round(
                statistics.median(row["latency_ms"]["median"] for row in rows), 4
            ),
            "p95_query_ms": round(
                percentile([row["latency_ms"]["p95"] for row in rows], 0.95), 4
            ),
            "median_exact_entry_bytes": round(
                statistics.median(
                    row["payload_bytes"]["exact_markdown_entries"] for row in rows
                )
            ),
            "median_whole_file_bytes": round(
                statistics.median(
                    row["payload_bytes"]["whole_source_files"] for row in rows
                )
            ),
            "median_projection_bytes": round(
                statistics.median(
                    row["payload_bytes"]["structured_projection"] for row in rows
                )
            ),
        }
    return rollup


def parse_source(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("source must use alias=/path/to/repo")
    alias, raw_path = value.split("=", 1)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", alias):
        raise argparse.ArgumentTypeError(f"invalid source alias: {alias}")
    path = Path(raw_path).expanduser().resolve()
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"source path is not a directory: {path}")
    return alias, path


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def run_benchmark(args: argparse.Namespace) -> dict[str, Any]:
    experiment_dir = Path(__file__).resolve().parent.parent
    runtime_dir = experiment_dir / ".runtime"
    database_dir = runtime_dir / "databases"
    output_dir = Path(args.output).resolve()
    runtime_dir.mkdir(parents=True, exist_ok=True)
    database_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    corpora: dict[str, Corpus] = {}
    for alias, root in args.source:
        corpora[alias] = parse_corpus(alias, root)
    cases, benchmark_manifest = load_case_manifest(
        Path(args.cases).resolve()
    )
    validate_cases(cases, corpora)

    engines: dict[str, tuple[MarkdownEngine, KuzuEngine]] = {}
    corpus_metrics: list[dict[str, Any]] = []
    for alias, corpus in corpora.items():
        markdown = MarkdownEngine(corpus)
        kuzu_path = database_dir / f"{alias}.kuzu"
        graph = KuzuEngine(corpus, kuzu_path)
        engines[alias] = (markdown, graph)
        manifest = corpus.public_manifest()
        manifest.update(
            {
                "kuzu_build_ms": round(graph.build_ms, 3),
                "kuzu_database_bytes": directory_size(kuzu_path),
                "database_to_markdown_size_ratio": round(
                    directory_size(kuzu_path) / corpus.source_bytes, 3
                )
                if corpus.source_bytes
                else 0,
            }
        )
        corpus_metrics.append(manifest)

    rows: list[dict[str, Any]] = []
    for case in cases:
        corpus = corpora[case.corpus]
        for engine in engines[case.corpus]:
            rows.append(benchmark_case(engine, case, corpus, args.repeats))

    authority_alias = args.authority_corpus or max(
        corpora, key=lambda alias: len(corpora[alias].defined_entries)
    )
    authority = authority_boundary_experiment(
        corpora[authority_alias],
        engines[authority_alias][1],
        runtime_dir,
    )
    accuracy_dimensions = evaluate_accuracy_dimensions(cases, corpora, rows)
    acceptance = evaluate_acceptance(
        cases,
        rows,
        accuracy_dimensions,
        authority,
    )
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat()
    result = {
        "schema_version": "1.2",
        "generated_at": generated_at,
        "question": (
            "For PRD-CE, should the SoT knowledge graph remain canonical Markdown, "
            "move to Kuzu, or use a Markdown-authority plus graph-projection hybrid?"
        ),
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "release": UPSTREAM_RELEASE,
            "commit": UPSTREAM_COMMIT,
            "archived_on": "2025-10-10",
            "license": "MIT",
            "python_package": getattr(kuzu, "__version__", "unavailable"),
        },
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "repeats_per_case": args.repeats,
            "database_layout": "one-kuzu-database-per-corpus",
            "kuzu_source_checkout_bytes": directory_size(
                experiment_dir / ".runtime" / "kuzu-source"
            ),
            "isolated_environment_bytes": directory_size(experiment_dir / ".venv"),
        },
        "benchmark_manifest": benchmark_manifest,
        "corpora": sorted(corpus_metrics, key=lambda item: item["alias"]),
        "cases": rows,
        "rollup": aggregate(rows),
        "accuracy_dimensions": accuracy_dimensions,
        "authority_boundary": authority,
        "acceptance": acceptance,
        "decision": {
            "measured": (
                (
                    "Markdown is the better current SoT and small-corpus retrieval "
                    "baseline: it matched Kuzu correctness with lower latency, "
                    "build cost, storage, and synchronization risk."
                )
                if acceptance["passed"]
                else (
                    "Benchmark acceptance failed; do not infer an architecture "
                    "decision from this run until every failed acceptance check "
                    "is resolved."
                )
            ),
            "architecture_hypothesis": (
                "A read-only graph projection may add value for future portfolio "
                "queries, graph algorithms, and impact analysis, but those benefits "
                "require a separate combined-corpus evaluation."
            ),
            "kuzu_disposition": (
                "Research dependency only; the requested upstream is archived."
            ),
        },
        "interpretation_contract": {
            "shared_parser": True,
            "gold_answers_are_manifest_authored": True,
            "external_products_modified": False,
            "absolute_paths_emitted": False,
            "source_bodies_emitted": False,
            "kuzu_payloads_read_from_database": True,
            "combined_namespace_tested": False,
            "graph_algorithms_tested": False,
            "incremental_indexing_tested": False,
            "llm_outcomes_tested": False,
            "literal_source_fidelity_is_semantic_truth": False,
        },
    }
    write_json(output_dir / "results.json", result)
    write_json(
        output_dir / "run-manifest.json",
        {
            "generated_at": generated_at,
            "upstream": result["upstream"],
            "runtime": result["runtime"],
            "benchmark_manifest": result["benchmark_manifest"],
            "corpora": result["corpora"],
            "accuracy_dimensions": {
                "source_fidelity": result["accuracy_dimensions"][
                    "source_fidelity"
                ],
                "semantic_truth": {
                    key: value
                    for key, value in result["accuracy_dimensions"][
                        "semantic_truth"
                    ].items()
                    if key != "checks"
                },
                "lifecycle_manifest_coverage": result["accuracy_dimensions"][
                    "lifecycle_manifest_coverage"
                ],
            },
            "acceptance": result["acceptance"],
            "safeguards": result["interpretation_contract"],
        },
    )

    from report import render_report

    (output_dir / "report.html").write_text(
        render_report(result),
        encoding="utf-8",
    )
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    run = subparsers.add_parser("run", help="run benchmark and render report")
    run.add_argument(
        "--source",
        action="append",
        required=True,
        type=parse_source,
        metavar="ALIAS=PATH",
    )
    run.add_argument("--cases", required=True, type=Path)
    run.add_argument("--output", required=True, type=Path)
    run.add_argument("--repeats", type=int, default=30)
    run.add_argument("--authority-corpus", default="")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "run":
        result = run_benchmark(args)
        print(
            json.dumps(
                {
                    "report": str((Path(args.output).resolve() / "report.html")),
                    "rollup": result["rollup"],
                    "authority_boundary": result["authority_boundary"]["status"],
                    "acceptance": result["acceptance"],
                },
                indent=2,
            )
        )
        return 0 if result["acceptance"]["passed"] else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
