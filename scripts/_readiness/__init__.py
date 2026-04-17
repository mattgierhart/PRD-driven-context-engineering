"""PRD-CE readiness scoring package.

Three layers compose into `status/readiness.json`:

    SoT files  (primitive)  —  _readiness.sot
    EPICs      (middle)     —  _readiness.epic   (reads SoT scores)
    PRD stage  (composer)   —  _readiness.stage  (reads SoT + EPIC scores)

Shared primitives (SoTEntry, index_all_entries, domain profile loading,
severity constants, build_summary) live in `_readiness.common`.

See docs/READINESS_PROTOCOL.md for the full schema.
"""

VERSION = "0.2.0"
SCHEMA_VERSION = "1.0"
