---
alwaysApply: true
---

# Document Ecosystem

The methodology uses a layered document structure:

| Layer | Files | Purpose |
|-------|-------|---------|
| **Navigation** | README.md | Entry point, dashboard, current status |
| **Strategy** | PRD.md | Requirements evolving v0.1→v1.0 |
| **Execution** | epics/EPIC-XX.md | Active work, session handoffs |
| **Knowledge** | SoT/*.md | Durable specs with unique IDs |
| **Scratchpad** | temp/*.md | Ephemeral notes, harvested to SoT |

**ID Ownership** (see `.claude/domain-profile.yaml` for full registry):
- SoT files own: BR, UJ, PER, SCR, API, DBT, TEST, DEP, RUN, MON, CFD, DES, TECH, ARC, INT, LL
- PRD.md owns: FEA (v0.3), RISK (v0.5), GTM (v0.9)
- README.md owns: KPI metrics

**Cross-Reference Rule**: Every ID should link to related IDs. This creates a knowledge graph that agents can traverse.
