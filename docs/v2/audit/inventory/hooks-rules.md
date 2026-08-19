# Hooks & Rules Audit vs v2 Direction

Scope: 15 files in `.claude/hooks/` (6 wired hooks, 2 libraries, 1 doc-only spec, contract, shared helper), `settings.json`, 8 files in `.claude/rules/`. All paths relative to `<repo root>/.claude/`.

---

## HOOKS

### 1. `hooks/context-validation.sh` + `.md` (SessionStart, wired)
- **Function**: Injects read-order directive (CLAUDE→README→PRD→SoT→active EPIC), parses PRD version from frontmatter, selects exactly one `In Progress` EPIC at v0.7+, warns on session locks and missing core files.
- **V2 disposition**: **Re-key to planes.** The mechanism (inject pointers, not content; detect the single active execution context; warn on contention) survives intact. What changes: read order becomes plane-keyed (Intent goal → Evidence → active Change Set in Delivery); "does an EPIC apply" stops being a version-number comparison and becomes "does an active Change Set exist for the current goal"; the Operating Discipline block re-words to verbs.
- **Stage assumptions**: `context-validation.sh:79` (`minor -ge 7` threshold), `:99` ("pre-v0.7"), `:105-107` ("Lifecycle v${version} requires an approved active EPIC"), `:124-128` (hard-coded lifecycle read order + gate-before-advance directive); `context-validation.md:19-20,27,66` (v0.7+ EPIC detection rationale).
- **Richness ledger**: "Inject pointers, not content — preserves context window" design table (`context-validation.md:63-66`); the 2-hour session-lock staleness window (`context-validation.sh:151`) as a multi-session coordination pattern; the "exactly one In Progress, never a template/planned/completed EPIC" invariant — carries straight to "exactly one active Change Set."

### 2. `hooks/context-density-gate.sh` + `.md` (UserPromptSubmit, wired)
- **Function**: On "start/continue epic N" or "approve gate vX.Y" prompts, checks the EPIC file for sparse (<500 tokens, no SoT refs), dense (>4000 tokens), or broad (>10 SoT refs) conditions; advisory only.
- **V2 disposition**: **Split.** The epic-density branch **re-keys** as a Change Set sizing check fired when the `build` verb engages (thresholds unchanged — they measure context-window fit, which is lifecycle-independent). The gate-approval branch (`:108-109, 177-181`) — which today only emits a generic reminder — **folds into the `check` verb's policy packs** and disappears from the hook.
- **Stage assumptions**: `context-density-gate.sh:109` (gate regex `v?[0-9]+\.[0-9]+`), `:178-180` (gate v${version} message); `.md:33-36,119` (gate trigger examples). The EPIC-numbering resolution (`resolve_epic_path`, `:58-80`) assumes the `epics/EPIC-NN` naming, which becomes Change Set naming.
- **Richness ledger**: The density threshold triple (sparse/dense/broad) is the operationalized "context-window-sized work packages" heuristic — one of the methodology's distinctive claims; chars/4 token estimation ("simple, good enough"); registry-driven ID pattern from `domain-profile.yaml` rather than hard-coded prefixes (`:28-42`, Issue #59) — the correct pattern for plane re-keying too.

### 3. `hooks/subagent-memory-load.sh` (SubagentStart, wired)
- **Function**: Injects the consumer agent's `.claude/agents/<name>/MEMORY.md` at spawn; handles `prd-ce:`-scoped plugin agent names; refuses foreign-plugin scoped agents.
- **V2 disposition**: **Keep as-is.** Agent memory is orthogonal to both the lifecycle and the verb loop; nothing here references stages.
- **Stage assumptions**: None.
- **Richness ledger**: "Never disclose consumer memory to another plugin's scoped agent" (`:47`) — a security-scoping decision worth preserving verbatim.

### 4. `hooks/subagent-memory-save.sh` (SubagentStop, wired)
- **Function**: Two-pass stop protocol — first stop injects a MANDATORY memory-extraction directive (Feedback/Patterns/Decisions/Handoff Notes); the `stop_hook_active` follow-up stages MEMORY.md via `git add`; also runs `metrics_drift_check.py` and appends a drift warning.
- **V2 disposition**: **Keep, with one re-key.** The memory half is lifecycle-agnostic. The drift-check half re-keys to the **Reality plane** (metrics.json = Reality; README = presentation) and its message ("README Truth Table", `:114-119`) re-words accordingly.
- **Stage assumptions**: None directly (the called library has one, below).
- **Richness ledger**: The four-category memory taxonomy with per-category formats (`:88-93`); "explicitly state 'No new memories to extract' rather than silently skipping" (`:101`) — anti-silent-failure discipline; the `stop_hook_active` two-pass pattern itself (documented `HOOK_CONTRACT.md:143-146`).

### 5. `hooks/traceability-gate.sh` (PreToolUse Write|Edit, wired)
- **Function**: Before source-code writes (methodology paths `SoT/`, `epics/`, `temp/`, `.claude/`, `*.md` exempt), escalates to `permissionDecision: "ask"` unless exactly one EPIC is `In Progress`.
- **V2 disposition**: **Keep — this is the blueprint's literal "runtime policy enforcement around SoT and Change Sets."** Re-key only: "active EPIC" → "active Change Set"; the path allowlist becomes a plane-keyed path map (which paths belong to which plane); message text updates.
- **Stage assumptions**: `traceability-gate.sh:54` ("owner-approved v0.7+ execution context" in the escalation reason).
- **Richness ledger**: `ask`, not `deny` — escalate to the human instead of hard-blocking (false positives don't strand the agent); "Product JSON/YAML remains governed like source code" (`:7`) — a subtle classification decision that took a failure to learn.

### 6. `hooks/sot-sync-reminder.sh` (PostToolUse Write|Edit, wired)
- **Function**: After source-code writes, reminds that SoT updates happen *during* the change, naming BR-/API-/DBT-/TEST- prefixes.
- **V2 disposition**: **Fold into a policy pack + upgrade.** Its generic reminder is exactly what `cascade_checklist.py` was built to replace (its own doc says generic reminders fail). V2 move: wire cascade_checklist's category map behind this event, keyed by plane (which plane's records does this file class obligate you to touch). The hook shell stays; the message body becomes pack-driven.
- **Stage assumptions**: None (hard-coded ID prefixes at `:34` should come from the registry, like context-density-gate does).
- **Richness ledger**: The "during, not after" phrasing — the enforcement voice of rule 03.

### 7. `hooks/cascade_checklist.py` + `.md` (standalone library, NOT wired)
- **Function**: Classifies changed file paths into 8 categories (test/epic/api/schema/business-rule/sot/readme/config changes) and emits the specific cascade checklist per category, using section anchors not line numbers.
- **V2 disposition**: **This is a policy pack in embryo — promote it.** A data-driven map from change-category → obligations is structurally identical to what "gates become policy packs consumed by `check`" needs. Re-key categories to planes (test_changes → Reality obligations; api/schema/business_rule → Evidence/Intent records; epic_phase_change → Delivery/Change). Externalize `CHECKLISTS` from Python source into pack data.
- **Stage assumptions**: `cascade_checklist.py:48-55` (`epic_phase_change` category: `epics/EPIC-*.md` trigger, "Active EPICs table", PRD milestone step); hard-coded SoT filenames throughout `:40-130`.
- **Richness ledger (high value)**: The entire `CHECKLISTS` category map (`:30-131`) plus its origin story — "abstract cascade rules ('update README') don't work for subagents; specific checklists with section anchors are durable" (`:9-13`, `.md:24-27`); design decisions table (`.md:73-80`): data-driven, section anchors over line numbers, multi-category matching, non-blocking.

### 8. `hooks/metrics_drift_check.py` + `.md` (library, called by subagent-memory-save; runnable manually/pre-commit)
- **Function**: Compares `status/metrics.json` against README `<!-- SECTION: truth-table -->` values (normalized); exits 1 on drift; silently skips when metrics.json is absent.
- **V2 disposition**: **Keep, re-key to the Reality plane.** This is a deterministic Reality-vs-presentation consistency validator — precisely the shape v2's plane-keyed scorer wants as a sub-check. Only naming changes ("pre-v0.7 projects" → "pre-build goals").
- **Stage assumptions**: `metrics_drift_check.py:27` ("pre-v0.7 projects"), `.md:7,17,94`.
- **Richness ledger**: "README is the human-authored view; metrics.json is the machine-writable source; validation ensures agreement — never auto-generate README from JSON" (`:10-12`) — a load-bearing stance against doc generation; normalize-before-compare (`1,552` vs `1552`, trailing `%`); section markers over line numbers.

### 9. `hooks/stage-gate-validation.md` (doc only — no script here; describes `scripts/check-stage-gate.sh`; never wired as a hook, per its own "Future Enhancements": "Actual Claude Code hook integration… not yet implemented", `:92-93`)
- **Function**: Documents per-stage required-artifact checks (file existence only) and the owner override protocol.
- **V2 disposition**: **Fold into policy packs.** The v0.2→v1.0 artifact table (`:42-50`) is the most stage-baked artifact in the audit — and it is *exactly* what a "guided journey" policy pack for the `check` verb looks like: the numbered table becomes one optional pack among several; goal-scoped packs replace the single ladder. The doc itself retires.
- **Stage assumptions**: The whole file — `:11` (`prd-v07-epic-scoping` at v0.5 example), `:22-23`, `:42-50` (full stage table), `:84` (`.claude/skills/prd-v0*` — the only numbered-skill-naming assumption found in hooks/rules).
- **Richness ledger (high value)**: "Block-at-submit, not block-at-write" (`:5`); the hooks-vs-skills division of labor table ("Did you create the files?" vs "How should you create them?", `:52-58`); the owner-override protocol — no agent-controlled bypass, override recorded as accepted risk, "if overrides recur, the methodology or readiness proxy needs adjustment" (`:71-80`).

### 10. `hooks/HOOK_CONTRACT.md`
- **Function**: Universal hook interface spec (stdin/stdout/exit codes/timeout), inventory, memory commit conventions.
- **V2 disposition**: **Keep as-is** (interface is verb/plane-agnostic); update inventory purpose strings as hooks re-key. Its "don't copy a frozen event list, follow the official reference" stance (`:148-153`) is the right pattern for v2 docs generally.
- **Stage assumptions**: Only indirectly, in inventory purpose text (`:126` "Verify active EPIC before source code writes").
- **Richness ledger**: `memory(agent):` commit convention (`:134-146`); the documented two-pass SubagentStop dance.

### 11. `hooks/_json.sh`
- **Function**: Bash-only JSON string escaper (od+awk, all C0 control bytes) shared by all shell hooks.
- **V2 disposition**: **Keep as-is.** No assumptions.
- **Richness ledger**: Minor — "no Python required" degradation discipline echoed in every hook header.

### `settings.json`
- Wires the 6 event hooks with correct 3-level nesting, `"$CLAUDE_PROJECT_DIR"` paths, 5–10s timeouts. **Keep as-is**; only re-pointed if hook files rename. No stage assumptions.

---

## RULES

### `rules/01-session-protocols.md`
- **Function**: Session start (load order, lifecycle state, git check) and end (state update, commit convention) protocols.
- **V2 disposition**: **Re-key to planes.** Start/end protocol survives; the pre-/post-v0.7 branch (`:10-11, 26-28`) becomes "read the active goal's Intent, then its Delivery state"; commit convention `session: [v0.X]` → goal/Change-Set-keyed.
- **Stage assumptions**: `:10-11`, `:20` (eviction item 3 names "PRD gate state… v0.7 onward"), `:26-28`.
- **Richness ledger (high value)**: The prompt-cache prefix-matching rationale for read order (`:14-15`) and the four-tier **eviction-priority model** (`:17-21`: temp → old tool results → volatile state → SoT never evicted). Both are distilled context-engineering experience independent of the lifecycle; the eviction model re-keys cleanly (Evidence/Intent never evicted; Delivery/Change summarized-then-refreshed; scratch first).

### `rules/02-document-ecosystem.md`
- **Function**: Five-layer document table (Navigation/Strategy/Execution/Knowledge/Scratchpad) + ID ownership registry + cross-reference rule.
- **V2 disposition**: **Re-key heavily — this becomes the plane map.** Strategy→Intent, Knowledge→Evidence, Execution→Delivery, plus Reality and Change get first-class rows; ID ownership loses its stage annotations and gains plane keys.
- **Stage assumptions**: `:12` ("Requirements evolving v0.1→v1.0"), `:19` ("FEA (v0.3), RISK (v0.5), GTM (v0.9)").
- **Richness ledger**: The Cross-Reference Rule (`:22`): "Every ID should link to related IDs. This creates a knowledge graph that agents can traverse" — arguably the repo's single most load-bearing sentence; unchanged in v2.

### `rules/03-documentation-discipline.md`
- **Function**: SoT-before-code, ID references in commits, progressive documentation (one document many versions), context-efficiency practices.
- **V2 disposition**: **Keep, rename referents.** Only `:9` ("before closing the EPIC" → Change Set) needs re-keying; everything else is lifecycle-free.
- **Stage assumptions**: `:9` only.
- **Richness ledger**: "One Document, Many Versions > Many Documents" + never-fork-PRD-v2.md; the `<!-- HANDOFF -->` marker convention; the batching/consolidation/pruning context-efficiency trio (Opus-plan-then-Sonnet-execute framing).

### `rules/04-coding-standards.md`
- **Function**: `@implements`/`@verifies`/`@see` traceability tags harvested into `status/devgraph.json`; tests-first; no secrets; small commits.
- **V2 disposition**: **Keep, re-key.** The devgraph is the Evidence↔Reality bridge in plane language; "in v0.7 they are harvested" (`:18`) becomes "once `build` runs."
- **Stage assumptions**: `:18` ("in v0.7").
- **Richness ledger**: "Untagged code shows up as an orphan node — a context leak" — the framing that makes traceability self-motivating; the three-edge taxonomy (implements/verifies/references).

### `rules/05-lifecycle-gates.md`
- **Function**: Do-not-skip gates; PRD authorizes, README only reports; blocker STOP protocol.
- **V2 disposition**: **Fold into `check` verb + policy packs.** The gate mechanics dissolve into packs; what survives is the authority principle and the STOP-and-record blocker discipline, restated per-plane (Intent authorizes; presentation surfaces report).
- **Stage assumptions**: The whole 8-line file is gate-framed; `:8` ("at v0.7+ also update the approved active EPIC").
- **Richness ledger**: The authority/status distinction ("README reports status but does not authorize a gate") — small but foundational; keep it in the `check` verb's definition.

### `rules/06-cross-agent-communication.md`
- **Function**: File-based inter-agent protocol — observations table for work requests, SoT cross-refs for decisions, session-state for blockers.
- **V2 disposition**: **Keep, re-key.** The pre-/post-v0.7 routing (`:9-16, 41`) becomes "route through the active goal's Delivery record"; the mechanism (files + ID links, no mailboxes) is unchanged.
- **Stage assumptions**: `:9-10`, `:15-16`, `:22`, `:41`.
- **Richness ledger**: "The ID cross-references ARE the communication" — pull-based context propagation through the graph instead of messages; the Agent Observations triage-table pattern with a human router.

### `rules/07-readiness-protocol.md`
- **Function**: Deterministic readiness scoring (three layers, thresholds 70/50, dimension overrides, causal traceability) + Anti-Goodhart discipline.
- **V2 disposition**: **Re-key per the blueprint's own terms**: scorer stays deterministic; the SoT→EPIC→PRD-stage layer stack becomes plane-keyed and goal-scoped; the code-layer dimensions (`implementation_coverage`, `architecture_conformance`) become Reality-plane dimensions gated on devgraph existence rather than on "v0.6→v0.7" (`:8`); the gate-advance trigger (`:18`) becomes a `check` behavior.
- **Stage assumptions**: `:8` ("v0.6→v0.7"), `:15` (PRD.md-for-stage-scope inputs), `:18` ("at v0.7+").
- **Richness ledger (highest value in the rules set)**: The full Anti-Goodhart block (`:20-27`) — the detection question ("would this change for a genuine quality reason… or only because I padded the inputs?"), padding-as-**frozen-replay-defect**, "raise evidence tier, not entry volume," the deterministic-LLM-free-scorer mandate (`:25`), quality-floor-then-cost, and periodic proxy-fidelity checks ("if gates pass but products don't ship, fix the scorer"). Also the `caused_by`/`consumed_by_epics` causal chain (`:17`). All of this transfers verbatim to the plane-keyed scorer.

### `rules/08-skill-execution-modes.md`
- **Function**: quick/standard/deep depth modes — time budgets, signal-based mode inference, output-depth matrix, anti-patterns, P3/P4 linkage.
- **V2 disposition**: **Keep nearly as-is; re-key vocabulary.** Verbs need depth dials exactly as lifecycle skills did. Only "PRD-lifecycle skills" (`:3`) and "first real attempt at the stage" (`:8`) re-word; the confidence-floor mechanics reference PRINCIPLES.md, not stages.
- **Stage assumptions**: `:3`, `:8` (phrasing only).
- **Richness ledger**: The signal→mode inference table (`:15-20`); "Quick is appropriate, not degraded… honor the budget by cutting optional steps, not by speed-running every step"; the anti-patterns table (`:56-64`); "Modes are a time/scope dial, not a research bypass" (`:68`); deep mode's "blocked on research" honesty requirement.

---

## Group observations

**Load-bearing for v2 (survive with rename-level changes):**
- `traceability-gate.sh` — the blueprint's kept-hooks clause ("runtime policy enforcement around SoT and Change Sets") describes this hook almost verbatim; EPIC→Change Set is the only real change.
- `subagent-memory-load.sh` / `subagent-memory-save.sh` — fully lifecycle-orthogonal; the memory taxonomy and two-pass stop protocol are mature.
- `metrics_drift_check.py` — a working prototype of a Reality-plane validator; slots under the plane-keyed scorer.
- `cascade_checklist.py` — unwired today, but structurally it *is* a policy pack (data-driven category→obligation map); promoting it both realizes the pack concept and fixes `sot-sync-reminder.sh`'s known generic-reminder weakness.
- `HOOK_CONTRACT.md`, `_json.sh`, `settings.json` — neutral infrastructure.
- Rules 03, 04, 06, 08, and the Anti-Goodhart half of 07 — durable discipline with only vocabulary re-keys.

**Legacy scaffolding (dissolves into packs/verbs or retires):**
- `stage-gate-validation.md` — the per-stage artifact table is the numbered lifecycle in tabular form; it becomes the optional "guided journey" policy pack and the doc retires. Notably, it was never wired as a runtime hook, so moving gates into `check` policy packs loses zero runtime enforcement.
- Rule 05 — dissolves entirely into the `check` verb; keep only the authority principle.
- The gate-approval branch of `context-density-gate.sh` and the v0.7 branching in `context-validation.sh` / rules 01, 02, 06, 07 — the recurring "before v0.7 / from v0.7 onward" fork is the single most repeated stage assumption (6 files) and re-keys uniformly to "before an active Change Set exists / once one exists," which suggests one shared predicate rather than per-file re-edits.

**Cross-cutting notes:**
- **No 47-skill count assumptions** exist in hooks or rules; the only skill-naming coupling is `stage-gate-validation.md:84` (`.claude/skills/prd-v0*`).
- **Registry-driven vs hard-coded IDs is inconsistent**: `context-density-gate.sh` derives prefixes from `domain-profile.yaml` (correct pattern for v2), while `sot-sync-reminder.sh:34` and `cascade_checklist.py` hard-code prefixes/filenames — re-keying should route all three through the registry.
- **Doc gap**: 4 of 6 wired hooks (`traceability-gate`, `sot-sync-reminder`, `subagent-memory-load`, `subagent-memory-save`) have no companion `.md`, only inventory rows in `HOOK_CONTRACT.md` — worth fixing during the re-key pass since hook docs are where the design-decision rationale (the richness) lives.
- **Enforcement posture is uniformly advisory** (`ask`/additionalContext, never `deny`/exit 2). That posture — block-at-submit, escalate-don't-block, false-positives-cost-trust — is itself distilled experience and should be stated as an explicit v2 hook principle rather than remaining implicit.