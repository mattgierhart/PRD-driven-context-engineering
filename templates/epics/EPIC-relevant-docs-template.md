# Relevant Docs for EPIC-XX-short-slug

Always load in this order before resuming work:
1. `README.md` → verify lifecycle gate + alerts.
2. `PRD.md` → read sections v0.x to v0.y.
3. `epics/EPIC-XX-short-slug.md` → confirm Section 3A entries.
4. SoT IDs
   - `source-of-truth/BUSINESS_RULES.md` → BR-###, BR-###
   - `source-of-truth/USER-JOURNEYS.md` → UJ-###
   - `source-of-truth/API_CONTRACTS.md` → API-###
5. Temp / tooling references
   - `temp/{epic}/notes.md`
   - `tools/{script}.sh`

Update this manifest whenever the EPIC scope changes so hooks can pre-load deterministic context.
