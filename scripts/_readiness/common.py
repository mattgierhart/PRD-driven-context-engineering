"""Shared primitives for readiness scoring.

Everything that sot.py, epic.py, and stage.py all need lives here so the
three modules can stay focused on their own scoring logic.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


# ---------- Regex / token constants ---------- #

ID_RE = re.compile(r"\b([A-Z]{2,5})-(\d{2,3})\b")
# Range syntax: "ENT-001 → ENT-014" or "..", "to"
RANGE_RE = re.compile(
    r"\b([A-Z]{2,5})-(\d{2,3})\s*(?:\u2192|->|\.\.|to)\s*(?:[A-Z]{2,5}-)?(\d{2,3})\b"
)
HEADING_DEF_RE = re.compile(r"^#{2,3}\s+([A-Z]{2,5}-\d{2,3})\b")
CONFIDENCE_RE = re.compile(r"Confidence:\s*(\d)\s*/\s*5", re.IGNORECASE)
STATUS_RE = re.compile(r"^\s*-?\s*\*?\*?Status\*?\*?:\s*([A-Za-z][\w-]*)", re.MULTILINE)
SECTION_HEADING_RE = re.compile(r"^#{1,3}\s+", re.MULTILINE)

PLACEHOLDER_MARKERS = (
    "pending prd development", "todo", "placeholder", "to be filled", "tbd",
)

STUB_KEYWORDS = (
    "rationale", "purpose", "description", "alternative", "request",
    "response", "fields", "columns", "step", "given", "when", "then",
    "decision", "constraint", "type", "title",
)


# ---------- Severity / penalty constants ---------- #

SEVERITY_PENALTY = {"high": 10, "medium": 3, "low": 1}
MAX_PENALTY = 25


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

    def outbound_refs(self) -> set[str]:
        """IDs referenced in this entry's body, excluding self."""
        refs = {f"{m.group(1)}-{m.group(2)}" for m in ID_RE.finditer(self.body)}
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
    "ENT":  {"file": "SoT/SoT.DATA_MODEL.md"},
    "TEST": {"file": "SoT/SoT.TESTING.md"},
    "DEP":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "RUN":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "MON":  {"file": "SoT/SoT.DEPLOYMENT.md"},
    "CFD":  {"file": "SoT/SoT.customer_feedback.md"},
    "DES":  {"file": "SoT/SoT.DESIGN_COMPONENTS.md"},
    "TECH": {"file": "SoT/SoT.TECHNICAL_DECISIONS.md"},
    "ARC":  {"file": "SoT/SoT.TECHNICAL_DECISIONS.md"},
    "INT":  {"file": "SoT/SoT.INTEGRATIONS.md"},
    "RISK": {"file": "SoT/SoT.RISKS.md"},
    "FEA":  {"file": "PRD.md"},
}


def load_domain_profile(repo: Path) -> dict:
    """Load `.claude/domain-profile.yaml` merged on top of DEFAULT_ID_PREFIXES."""
    path = repo / ".claude" / "domain-profile.yaml"
    result = dict(DEFAULT_ID_PREFIXES)
    if path.is_file():
        with path.open() as f:
            data = yaml.safe_load(f) or {}
        repo_prefixes = data.get("id_prefixes") or {}
        result.update(repo_prefixes)
    return result


def load_readiness_config(repo: Path) -> dict:
    """Optional repo-level overrides — per-dimension defaults, etc."""
    path = repo / ".claude" / "readiness-config.yaml"
    if not path.is_file():
        return {}
    with path.open() as f:
        return yaml.safe_load(f) or {}


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
        start = int(m.group(2))
        end = int(m.group(3))
        if end < start:
            start, end = end, start
        digits = max(len(m.group(2)), len(m.group(3)))
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
    files: list[Path] = []

    sot_dir = repo / "SoT"
    if sot_dir.is_dir():
        files.extend(p for p in sot_dir.glob("*.md")
                     if p.name not in {"SoT.README.md", "SoT.UNIQUE_ID_SYSTEM.md"})
    for extra in ("PRD.md", "README.md"):
        p = repo / extra
        if p.is_file():
            files.append(p)
    epics_dir = repo / "epics"
    if epics_dir.is_dir():
        files.extend(p for p in epics_dir.glob("*.md") if p.name != "EPIC_TEMPLATE.md")

    for f in files:
        text = f.read_text(errors="replace")
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
    roots: list[Path] = []
    for sub in ("SoT", "epics"):
        p = repo / sub
        if p.is_dir():
            roots.extend(p.glob("*.md"))
    for extra in ("PRD.md", "README.md", "CLAUDE.md"):
        p = repo / extra
        if p.is_file():
            roots.append(p)

    for f in roots:
        rel = str(f.relative_to(repo))
        text = f.read_text(errors="replace")
        seen: set[str] = set()
        for m in ID_RE.finditer(text):
            seen.add(f"{m.group(1)}-{m.group(2)}")
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
