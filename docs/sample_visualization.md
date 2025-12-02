# Sample GHM ID Knowledge Graph

This is what the visualization looks like when you have IDs with cross-references.

## ASCII Representation

```
┌─────────────────────────────────────────────────────────────────┐
│                    GHM ID Knowledge Graph                       │
│                   (Sample with 9 IDs, 10 edges)                 │
└─────────────────────────────────────────────────────────────────┘

Legend:
  [BR]  = Business Rule (Blue)
  [API] = API Contract (Green)
  [UJ]  = User Journey (Purple)
  [TEST]= Test Case (Yellow)
  [DBT] = Database Table (Orange)
  [CFD] = Customer Feedback (Red)


                    ┌──────────────┐
                    │   BR-001     │ (Blue)
                    │ Free Tier    │
                    │Product Limit │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
       ┌──────────┐  ┌──────────┐ ┌──────────┐
       │ API-045  │  │  UJ-101  │ │ TEST-301 │
       │ Create   │  │ Product  │ │Free Tier │
       │ Product  │  │Onboarding│ │Limit Test│
       └────┬─────┘  └────┬─────┘ └──────────┘
            │             │
            │             ▼
            │        ┌──────────┐
            └───────▶│ DBT-018  │ (Orange)
                     │ products │
                     │  table   │
                     └──────────┘

       ┌──────────────┐
       │   BR-118     │ (Blue)
       │ OCR Retry    │
       │    Limit     │
       └──────┬───────┘
              │
              ▼
       ┌──────────┐     relates to    ┌──────────┐
       │ API-046  │ ─────────────────▶ │ API-045  │
       │  Retry   │                    │          │
       │Failed OCR│                    └──────────┘
       └────┬─────┘
            │
            ▼
       ┌──────────┐
       │ TEST-303 │ (Yellow)
       │  Retry   │
       │Logic Test│
       └──────────┘

       ┌──────────┐
       │ CFD-401  │ (Red, dashed border)
       │ Partial  │ ⚠️ ORPHANED (no connections)
       │GHM Adopt │
       └──────────┘
```

## Actual Graphviz Output

When rendered with Graphviz, this becomes an interactive SVG with:
- **Colored boxes** for each ID type
- **Arrows** showing relationships (with labels like "enforces", "uses", "tests")
- **Tooltips** showing file path and excerpt on hover
- **Force-directed layout** that automatically organizes nodes
- **Clickable nodes** (in future HTML version)

## Example Insights from This Graph

1. **BR-001 is central** - Many IDs reference it (high importance)
2. **CFD-401 is orphaned** - No connections (needs review or archival)
3. **API-045 has multiple test coverage** - TEST-301 validates it
4. **BR-118 is isolated** - Only connected to API-046 and TEST-303
5. **Clear dependency chains** - BR-001 → API-045 → DBT-018

## Color Coding (from config)

```yaml
graph:
  node_colors:
    BR: '#3498db'   # Blue - Business Rules
    API: '#2ecc71'  # Green - API Contracts
    UJ: '#9b59b6'   # Purple - User Journeys
    DBT: '#e67e22'  # Orange - Database Tables
    TEST: '#f1c40f' # Yellow - Test Cases
    CFD: '#e74c3c'  # Red - Customer Feedback
    DES: '#1abc9c'  # Teal - Design Components
    SEC: '#c0392b'  # Dark Red - Security
    PERF: '#16a085' # Dark Teal - Performance
```

---

**To generate this on your repo:**
```bash
python tools/generate-visuals.py --all
open docs/generated/id-graph.svg
```
