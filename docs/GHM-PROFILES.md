# GHM Profiles & Enforcement Levels

Profiles live in `.ghm/config.yaml` and tell hooks/scripts how strict to be across the PRD lifecycle. Enforcement levels add a second dial for teams that need relaxed vs strict guardrails within the same profile.

| Profile | Lifecycle Focus | Default Enforcement | Expectations |
|---------|-----------------|---------------------|--------------|
| `definition` | v0.1 → v0.6 (research/strategy) | relaxed | Allow lightweight SoT updates, warn (not block) if TEST-/DEP- IDs missing. Requires CFD-/BR- references for research artifacts and documents open questions for downstream gates. |
| `standard` | v0.1 → v1.0 | standard | Balanced defaults. Plan-exit hooks insist on a TASK-### + GitHub issue pair, stop hooks block until README/PRD/SoT updates are recorded, and validation expects Section 3A + SoT references. |
| `development` | v0.7 execution | strict | Emphasizes TEST-/DEP- IDs, requires `tools/create_task.py` output for every issue, and treats missing test evidence as blocking errors. `.ghm/task-backlog.yaml` becomes mandatory input to pre-stop hooks. |
| `production` | v0.8 → v0.9 (launch) | strict | Adds deployment/security/GTM requirements. Hooks will require RUN-/SEC-/PERF- IDs in tasks touching deployment, and `tools/validate_ghm.py` warns if relevant manifests (`templates/epics/EPIC-relevant-docs-template.md`) are missing. |

### Enforcement Levels

`enforcement_level` (relaxed | standard | strict) can downshift or upshift the defaults above:
- **relaxed**: Hooks log warnings but do not block tool use when required files are missing; validation script emits warnings only.
- **standard**: Hooks enforce plan-exit and stop requirements; validation script fails when state is inconsistent.
- **strict**: Adds blocking checks for README/PRD metrics, SoT backlinks, and memory entries on each completed task. CI should run `tools/validate_ghm.py --strict` to gate merges.

> Hook wiring isn't live yet, but documenting intent up front keeps the profile semantics clear as automation lands.
