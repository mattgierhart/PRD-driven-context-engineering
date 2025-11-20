# Default Relevant Docs

Always load these before writing code or editing SoT files:
- `README.md`
- `PRD.md`
- `CLAUDE.md`
- `epics/` (active EPIC listed in README)
- `source-of-truth/` IDs referenced in the active EPIC Section 3A
- `.ghm/task-backlog.yaml`
- `.ghm/memory.jsonl`

> For EPIC-specific overrides, copy `templates/epics/EPIC-relevant-docs-template.md` into the EPIC folder and list the SoT IDs + temp files that matter. Hooks/scripts can merge that manifest with this default list.
