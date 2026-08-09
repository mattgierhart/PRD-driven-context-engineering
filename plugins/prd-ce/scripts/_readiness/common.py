"""Shared primitives for readiness scoring.

Everything that sot.py, epic.py, and stage.py all need lives here so the
three modules can stay focused on their own scoring logic.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


# ---------- Regex / token constants ---------- #

ID_RE = re.compile(
    r"(?<![A-Za-z0-9-])"
    r"(EPIC(?=-\d{2,3}(?![A-Za-z0-9-]))|"
    r"(?!EPIC(?:-|$))[A-Z]+(?=(?:-[A-Z][A-Z0-9]*)?-\d{3}(?![A-Za-z0-9-])))"
    r"(?:-[A-Z][A-Z0-9]*)?-(\d{2,3})(?![A-Za-z0-9-])"
)
# Range syntax: "ENT-001 → ENT-014" or "..", "to"
RANGE_RE = re.compile(
    r"(?<![A-Za-z0-9-])([A-Z]+(?:-[A-Z][A-Z0-9]*)?)-(\d{2,3})\s*"
    r"(?:\u2192|->|\.\.|to)\s*(?:([A-Z]+(?:-[A-Z][A-Z0-9]*)?)-)?"
    r"(\d{2,3})(?![A-Za-z0-9-])"
)
HEADING_DEF_RE = re.compile(
    r"^#{1,3}\s+((?:EPIC-\d{2,3})|(?:(?!EPIC(?:-|$))[A-Z]+(?:-[A-Z][A-Z0-9]*)?-\d{3}))"
    r"(?![A-Za-z0-9-])"
)
EPIC_FILENAME_RE = re.compile(
    r"^(EPIC-\d{2,3})(?:-[A-Za-z0-9][A-Za-z0-9_-]*)?\.md$"
)
CONFIDENCE_RE = re.compile(r"Confidence:\s*(\d)\s*/\s*5", re.IGNORECASE)
STATUS_RE = re.compile(r"^\s*-?\s*\*?\*?Status\*?\*?:\s*([A-Za-z][\w-]*)", re.MULTILINE)
SECTION_HEADING_RE = re.compile(r"^#{1,3}\s+", re.MULTILINE)

PLACEHOLDER_MARKERS = (
    "pending prd development", "todo", "placeholder", "to be filled", "tbd",
)
UNINITIALIZED_TEMPLATE_RE = re.compile(
    r"(?m)^template_state:\s*[\"']?uninitialized[\"']?\s*$"
)

STUB_KEYWORDS = (
    "rationale", "purpose", "description", "alternative", "request",
    "response", "fields", "columns", "step", "given", "when", "then",
    "decision", "constraint", "type", "title",
)


def is_uninitialized_template(text: str) -> bool:
    """Return True when a generic seed has not been replaced with product records."""
    return bool(UNINITIALIZED_TEMPLATE_RE.search(text))


def epic_id_from_filename(path: Path) -> Optional[str]:
    """Return the exact execution ID for a canonical 2/3-digit EPIC filename."""
    match = EPIC_FILENAME_RE.fullmatch(path.name)
    return match.group(1) if match else None


def iter_epic_files(epics_dir: Path) -> list[Path]:
    """Return only canonical numeric EPIC files, excluding templates and malformed lookalikes."""
    if not epics_dir.is_dir():
        return []
    return sorted(
        path for path in epics_dir.glob("EPIC-*.md")
        if epic_id_from_filename(path) is not None
    )


def canonical_graph_markdown_files(
    repo: Path, *, include_claude: bool = False, include_readme: bool = True,
) -> list[Path]:
    """Return authored product graph surfaces, excluding guides/templates/lookalike EPICs."""
    files: list[Path] = []
    sot_dir = repo / "SoT"
    if sot_dir.is_dir():
        files.extend(
            path for path in sot_dir.glob("*.md")
            if path.name not in {"SoT.README.md", "SoT.UNIQUE_ID_SYSTEM.md"}
        )
    extras = ["PRD.md"]
    if include_readme:
        extras.append("README.md")
    for extra in extras:
        path = repo / extra
        if path.is_file():
            files.append(path)
    files.extend(iter_epic_files(repo / "epics"))
    if include_claude and (repo / "CLAUDE.md").is_file():
        files.append(repo / "CLAUDE.md")
    return sorted(set(files))


# ---------- Severity / penalty constants ---------- #

SEVERITY_PENALTY = {"high": 10, "medium": 3, "low": 1}
MAX_PENALTY = 25


# ---------- Development Graph (v0.6→v0.7) constants ---------- #

# Spec prefixes that the codebase is expected to IMPLEMENT — i.e. a code node
# should carry an `@implements` bridge edge back to them. Used by the EPIC
# `implementation_coverage` dimension to compute build-vs-blueprint. Spec types
# that code does not implement (RISK, CFD, KPI, GTM, TECH decisions, LL) are
# excluded so coverage is not diluted by non-buildable specs.
IMPLEMENTABLE_PREFIXES = {"BR", "API", "DBT", "ENT", "FEA", "SCR", "UJ"}


# ---------- SoT entry ---------- #

@dataclass
class SoTEntry:
    """One ID definition found under a `## ID-NNN` or `### ID-NNN` heading."""
    id: str
    prefix: str
    file: str
    line: int
    body: str

    def word_count(self) -> int:
        return len(self.body.split())

    def is_non_stub(self) -> bool:
        if self.word_count() < 15:
            return False
        lower = self.body.lower()
        return any(kw in lower for kw in STUB_KEYWORDS)

    def confidence(self) -> Optional[int]:
        m = CONFIDENCE_RE.search(self.body)
        return int(m.group(1)) if m else None

    def status(self) -> Optional[str]:
        m = STATUS_RE.search(self.body)
        return m.group(1) if m else None

    def has_status(self) -> bool:
        return self.status() is not None

    def has_confidence(self) -> bool:
        return self.confidence() is not None

    def outbound_refs(self, known_prefixes: Optional[set[str]] = None) -> set[str]:
        """IDs referenced in this entry's body, excluding self."""
        refs = {m.group(0) for m in ID_RE.finditer(self.body)}
        if known_prefixes is not None:
            refs = {ref for ref in refs if ref.split("-", 1)[0] in known_prefixes}
        refs.discard(self.id)
        return refs


# ---------- Domain profile ---------- #

# Fallback prefix → owning file mapping when a repo has no domain-profile.yaml.
# Covers the canonical PRD-CE taxonomy. Repo-specific profiles override.
DEFAULT_ID_PREFIXES = {
    "BR":   {"file": "SoT/SoT.BUSINESS_RULES.md"},
    "UJ":   {"file": "SoT/SoT.USER_JOURNEYS.md"},
    "PER":  {"file": "SoT/SoT.USER_JOURNEYS.md"},
    "SCR":  {"file": "SoT/SoT.USER_JOURNEYS.md"},
    "API":  {"file": "SoT/SoT.API_CONTRACTS.md"},
    "DBT":  {"file": "SoT/SoT.DATA_MODEL.md"},
    "TEST": {"file": "SoT/SoT.TESTING.md"},
    "DEP":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "RUN":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "MON":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "SEC":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "CFD":  {"file": "SoT/SoT.customer_feedback.md"},
    "DES":  {"file": "SoT/SoT.DESIGN_COMPONENTS.md"},
    "TECH": {"file": "SoT/SoT.TECHNICAL_DECISIONS.md"},
    "ARC":  {"file": "SoT/SoT.TECHNICAL_DECISIONS.md"},
    "ENV":  {"file": "SoT/SoT.TECHNICAL_DECISIONS.md"},
    "INT":  {"file": "SoT/SoT.INTEGRATIONS.md"},
    "LL":   {"file": "SoT/SoT.LESSONS_LEARNED.md"},
    "ADO":  {"file": "SoT/SoT.ADOPTION.md"},
    "FEA":  {"file": "PRD.md"},
    "RISK": {"file": "PRD.md"},
    "GTM":  {"file": "PRD.md"},
    "KPI":  {"file": "README.md"},
    "EPIC": {"file": "epics/"},
}


def load_domain_profile(repo: Path) -> dict:
    """Load the closed prefix registry, falling back only when no profile exists."""
    path = repo / ".claude" / "domain-profile.yaml"
    if path.is_file():
        with path.open() as f:
            data = yaml.safe_load(f) or {}
        repo_prefixes = data.get("id_prefixes")
        return repo_prefixes if isinstance(repo_prefixes, dict) else {}
    return dict(DEFAULT_ID_PREFIXES)


def load_readiness_config(repo: Path) -> dict:
    """Optional repo-level overrides — per-dimension defaults, etc."""
    path = repo / ".claude" / "readiness-config.yaml"
    if not path.is_file():
        return {}
    with path.open() as f:
        return yaml.safe_load(f) or {}


def load_required_edges(repo: Path) -> list[dict]:
    """Required cross-reference edge rules from `.claude/domain-profile.yaml`.

    Each rule declares that every entry of a `from` prefix must reference at
    least one entry of each `requires` prefix — the schema constraint that turns
    "if it's not in the graph it isn't true" from a slogan into a checked
    invariant (see scripts/validate-edges.py). Returns ``[]`` when none are
    declared, so the check is opt-in and a template repo with no rules validates
    clean. See `docs/DEVELOPMENT_GRAPH.md` §14 for the rule schema.
    """
    path = repo / ".claude" / "domain-profile.yaml"
    if not path.is_file():
        return []
    with path.open() as f:
        data = yaml.safe_load(f) or {}
    rules = data.get("required_edges")
    if rules is None:
        return []
    if not isinstance(rules, list):
        raise ValueError("required_edges must be a list")
    return rules


def load_devgraph(repo: Path) -> Optional[dict]:
    """Load the Development Graph (`status/devgraph.json`) if it exists.

    The dev graph is the "as-built" layer: code nodes extracted from the product
    codebase, bridged to spec IDs via @implements/@verifies edges. It is produced
    during v0.7 build execution (see docs/DEVELOPMENT_GRAPH.md). Returns ``None``
    when absent or unparseable — every dev-graph readiness dimension treats
    ``None`` as "not applicable" and auto-disables, so repos that have not yet
    built anything (or the methodology repo itself) score exactly as before.
    """
    path = repo / "status" / "devgraph.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(errors="replace"))
    except (json.JSONDecodeError, OSError):
        return None
    return data if isinstance(data, dict) else None


def devgraph_spec_status(devgraph: Optional[dict]) -> dict[str, str]:
    """Index spec-layer nodes by ID → coverage status from the dev graph.

    Status values (set by the extractor, see docs/DEVELOPMENT_GRAPH.md):
      ``implemented``            — ≥1 inbound `implements` edge
      ``implemented_unverified`` — implemented but no `verifies` edge
      ``unimplemented``          — spec node with no `implements` edge
    """
    out: dict[str, str] = {}
    if not devgraph:
        return out
    for node in devgraph.get("nodes", []) or []:
        if node.get("layer") == "spec" and node.get("id"):
            out[node["id"]] = node.get("status", "unimplemented")
    return out


def devgraph_conformance(devgraph: Optional[dict]) -> list[dict]:
    """Return the architecture-conformance verdicts carried by the dev graph.

    Each entry: ``{arc_id, rule, verdict: pass|violate|unknown, violations[]}``.
    """
    if not devgraph:
        return []
    return devgraph.get("conformance", []) or []


# ---------- Repo discovery ---------- #

def find_repo_root(start: Path) -> Path:
    """Walk up from `start` until a PRD.md / SoT/ / epics/ is found."""
    p = start.resolve()
    if p.is_file():
        p = p.parent
    while p != p.parent:
        if (p / "PRD.md").is_file() or (p / "SoT").is_dir() or (p / "epics").is_dir():
            return p
        p = p.parent
    raise SystemExit(f"error: could not find repo root above {start}")


# ---------- Frontmatter parsing ---------- #

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter. Returns (dict, body-without-frontmatter)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5:]
    try:
        data = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        data = {}
    return data, body


# ---------- Section extraction / ID ranges ---------- #

def extract_section(body: str, heading_regex: str) -> Optional[str]:
    """Return the text of a section between heading_regex and the next ## heading."""
    matches = list(re.finditer(heading_regex, body, re.MULTILINE))
    if not matches:
        return None
    start = matches[0].end()
    next_section = re.search(r"^#{1,2}\s+", body[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(body)
    return body[start:end]


def expand_ranges(text: str) -> set[str]:
    """Find 'ENT-001 → ENT-014' style ranges and return the expanded IDs."""
    out: set[str] = set()
    for m in RANGE_RE.finditer(text):
        prefix = m.group(1)
        rhs_prefix = m.group(3)
        if rhs_prefix and rhs_prefix != prefix:
            continue
        if prefix.startswith("EPIC-"):
            continue
        if (len(m.group(2)) != 3 or len(m.group(4)) != 3) and prefix != "EPIC":
            continue
        start = int(m.group(2))
        end = int(m.group(4))
        if end < start:
            start, end = end, start
        digits = max(len(m.group(2)), len(m.group(4)))
        for n in range(start, end + 1):
            out.add(f"{prefix}-{str(n).zfill(digits)}")
    return out


# ---------- Entry indexing ---------- #

def index_all_entries(repo: Path) -> dict[str, SoTEntry]:
    """Scan SoT/, PRD.md, epics/ for `## ID-NNN` / `### ID-NNN` definitions.

    The body for each entry runs from its heading to the next heading at
    depth 1–3. Collects all entries into `{id: SoTEntry}`.
    """
    index: dict[str, SoTEntry] = {}
    known_prefixes = set(load_domain_profile(repo))
    files = canonical_graph_markdown_files(repo)

    for f in files:
        text = f.read_text(errors="replace")
        if is_uninitialized_template(text):
            continue
        lines = text.splitlines()
        current: Optional[SoTEntry] = None
        body_lines: list[str] = []
        for i, line in enumerate(lines, start=1):
            m = HEADING_DEF_RE.match(line)
            if m:
                if current is not None:
                    current.body = "\n".join(body_lines).strip()
                    index.setdefault(current.id, current)
                id_ = m.group(1)
                prefix = id_.split("-")[0]
                if prefix not in known_prefixes:
                    current = None
                    body_lines = []
                    continue
                current = SoTEntry(id=id_, prefix=prefix,
                                   file=str(f.relative_to(repo)), line=i, body="")
                body_lines = []
            elif current is not None:
                if SECTION_HEADING_RE.match(line):
                    current.body = "\n".join(body_lines).strip()
                    index.setdefault(current.id, current)
                    current = None
                    body_lines = []
                else:
                    body_lines.append(line)
        if current is not None:
            current.body = "\n".join(body_lines).strip()
            index.setdefault(current.id, current)
    return index


def collect_all_references(repo: Path) -> dict[str, set[str]]:
    """Return `{id: {files_that_reference_it}}` across SoT/, epics/, PRD, README, CLAUDE.

    Used by orphan-rate scoring — an entry defined in SoT.X but referenced only
    within SoT.X is orphaned.
    """
    refs: dict[str, set[str]] = {}
    roots = canonical_graph_markdown_files(repo, include_claude=True)

    for f in roots:
        rel = str(f.relative_to(repo))
        text = f.read_text(errors="replace")
        if is_uninitialized_template(text):
            continue
        seen: set[str] = set()
        for m in ID_RE.finditer(text):
            seen.add(m.group(0))
        for id_ in seen:
            refs.setdefault(id_, set()).add(rel)
    return refs


# ---------- Summary / blockers ---------- #

def build_summary(output: dict, threshold: int = 70) -> dict:
    """Aggregate view: counts + top blockers ranked by EPIC impact.

    Called by every scorer on write, so the top-level `summary` block
    is always current regardless of which layer ran last.
    """
    sot_files = output.get("sot_files", {}) or {}
    epics = output.get("epics", {}) or {}
    stages = output.get("stages", {}) or {}

    sot_passing = sum(1 for b in sot_files.values() if b.get("score", 0) >= threshold)
    epic_passing = sum(1 for b in epics.values() if b.get("score", 0) >= threshold)

    # Rank SoT files by (100 − score) × #consumers. Higher impact = worse blocker.
    blockers = []
    for path, block in sot_files.items():
        if block.get("score", 0) >= threshold:
            continue
        consumers = block.get("consumed_by_epics", [])
        if not consumers:
            continue
        impact = (100 - block.get("score", 0)) * len(consumers)
        blockers.append({
            "file": path,
            "score": block.get("score", 0),
            "blocks": len(consumers),
            "blocking_epics": consumers,
            "impact": round(impact, 0),
        })
    blockers.sort(key=lambda b: -b["impact"])

    summary = {
        "sot_files_total": len(sot_files),
        "sot_files_passing": sot_passing,
        "epics_total": len(epics),
        "epics_passing": epic_passing,
        "threshold": threshold,
        "top_blockers": blockers[:5],
    }

    # Also surface the current stage if any stages block exists.
    if stages:
        latest_gate = sorted(stages.keys())[-1]
        stage = stages[latest_gate]
        summary["current_stage"] = {
            "target": latest_gate,
            "score": stage.get("score", 0),
            "passing": stage.get("score", 0) >= threshold,
        }

    return summary
