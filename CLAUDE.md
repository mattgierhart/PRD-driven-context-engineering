---
title: "CLAUDE Agent Operating Guide"
updated: "2026-02-12"
authority: "PRD Led Context Engineering"
template_version: "3.0.0"
---

# CLAUDE.md — Agent Operating Guide

> **Mission**: Build software in lockstep with the PRD Version Lifecycle.
> **Authority**: Load `README.md` → `PRD.md` → `CLAUDE.md` → Active EPIC.
> **Core Rule**: If it's not in the ID Graph (Specs), it doesn't exist.

---

<!-- SECTION: session-protocols -->
## 1. Session Protocols (MANDATORY)

### Start of Session

1. **Load Context**: `README.md`, `PRD.md`, and the Active EPIC.
2. **Read Session State**: Check the **Session State** section of the Active EPIC for "Where we left off".
3. **Check Git Status**: Confirm you are on the right branch/commit.

### End of Session

1. **Update the EPIC Session State section**:
   - **Progress**: What specifically was done? (Link IDs)
   - **Stop Point**: File/Line where work ceased.
   - **Next**: Exact instructions for the next agent.
2. **Commit**: `session: [EPIC-XX] summary of work`.
<!-- /SECTION: session-protocols -->

---

<!-- SECTION: execution-rules -->
## 2. Execution Rules

### Document Ecosystem

The methodology uses a layered document structure:

| Layer | Files | Purpose |
|-------|-------|---------|
| **Navigation** | README.md | Entry point, dashboard, current status |
| **Strategy** | PRD.md | Requirements evolving v0.1→v1.0 |
| **Execution** | epics/EPIC-XX.md | Active work, session handoffs |
| **Knowledge** | SoT/*.md | Durable specs with unique IDs |
| **Scratchpad** | temp/*.md | Ephemeral notes, harvested to SoT |

**ID Ownership** (see [`.claude/domain-profile.yaml`](.claude/domain-profile.yaml) for full registry):
- SoT files own: BR, UJ, PER, SCR, API, DBT, TEST, DEP, RUN, MON, CFD, DES, TECH, ARC, INT
- PRD.md owns: FEA (v0.3), RISK (v0.5), GTM (v0.9)
- README.md owns: KPI metrics

**Cross-Reference Rule**: Every ID should link to related IDs. This creates a knowledge graph that agents can traverse.

### Documentation Discipline

- **IDs**: Reference `BR-`, `UJ-`, `API-` IDs in code comments and commits.
- **SoT Updates**: Update `SoT/` files _before_ or _during_ code changes, never "later".
- **Temp Files**: Use `temp/` for scratchpad, but harvest to SoT before closing the EPIC.

### Progressive Documentation Protocol

> **Rule**: One Document, Many Versions > Many Documents.

- **No Fragmentation**: Never create `PRD-v2.md`. Update `PRD.md` and increment the version header.
- **Change Tracking**: Use inline diffs for minor changes and append logs for major ones.
- **Handoffs**: If hitting context limits, leave a `<!-- HANDOFF -->` marker with summary of state.

### Context Efficiency

- **Batching**: Ask for comprehensive plans (Opus-style) before executing piecemeal (Sonnet-style).
- **Consolidation**: Validation and Verification steps should happen in bulk to save tokens.
- **Pruning**: if context is full, suggest a `session_handoff` where you summarize state and clear history.

### Coding Standards

#### Traceability Protocol (MANDATORY)

Every major code unit must declare which ID it implements.

```typescript
// @implements BR-101 (Free Limit)
// @see API-045
export class RateLimiter { ... }
```

- **Tests First**: Create/Update tests (`TEST-`) for every feature.
- **No Secrets**: Never commit credentials.
- **Small Commits**: Group changes by ID/Feature.

### Lifecycle Gates

- **Do Not Skip**: Verify the Gate Checklist in `PRD.md` or `README.md` (PRD Lifecycle) before advancing.
- **Blockers**: If a gate cannot be passed, update the EPIC and STOP.
<!-- /SECTION: execution-rules -->

---

<!-- SECTION: quick-reference -->
## 3. Quick Reference

- **Lifecycle Guide**: [`README.md`](README.md)
- **ID System**: [`SoT/SoT.UNIQUE_ID_SYSTEM.md`](SoT/SoT.UNIQUE_ID_SYSTEM.md)
- **SoT Index**: [`SoT/SoT.README.md`](SoT/SoT.README.md)
- **EPIC Template**: [`epics/EPIC_TEMPLATE.md`](epics/EPIC_TEMPLATE.md)
- **Active Work**: [`epics/`](epics/)
- **Domain Profile**: [`.claude/domain-profile.yaml`](.claude/domain-profile.yaml)
- **Hook Contract**: [`.claude/hooks/HOOK_CONTRACT.md`](.claude/hooks/HOOK_CONTRACT.md)

**When in doubt, follow the Source of Truth.**
<!-- /SECTION: quick-reference -->

---

<!-- SECTION: pm-governance -->
## 4. PM Governance Rules

These rules define what a PM can directly commit, what requires engineering escalation, what AI prompt changes require before merge, and what observability gates must be met before any feature review. They apply to all product work done in this repo.

---

### 4A. PM Shipping Zone

Defines what a PM can commit directly vs. what must go through engineering review.

#### ✅ PM Can Commit Directly

| Category | Examples |
|---|---|
| **Copy** | CTAs, tooltips, error messages, onboarding text, empty states, labels |
| **Feature flags** | Toggling existing flags; adjusting flag values within documented ranges |
| **Config values** | Non-secret config values (e.g., rate limits, thresholds already in env) |
| **AI prompts** | System prompts and few-shot examples — **subject to AI Prompt Compliance Gate (4B)** |
| **Design tweaks** | CSS adjustments, spacing, color on pre-approved component library components |
| **Planning docs** | PRD.md updates, EPIC files, SoT entries, README updates |
| **Release notes** | User-facing release notes and stakeholder summaries |

#### ❌ PM Must Escalate to Engineering

| Category | Examples | Why |
|---|---|---|
| **Database schemas** | New tables, column additions/removals, index changes | Risk of data loss, migration complexity |
| **API routes** | New endpoints, changing request/response shapes | Contract changes affect all consumers |
| **Middleware** | Auth logic, rate limiting, request validation | Security blast radius |
| **Infrastructure** | Env vars, secrets, deployment config, CI/CD | Environment stability |
| **Package dependencies** | Adding/removing/upgrading npm/pip packages | Supply chain and compatibility risk |
| **Broad file changes** | Changes touching >3 files outside `/planning/` or `/docs/` | Scope indicates engineering concern |
| **Breaking changes** | Any change requiring a DB migration or API version bump | Requires coordinated rollout |

**Escalation protocol**: Open a discussion in the active EPIC (`epics/EPIC-XX.md`) under a `<!-- PM ESCALATION -->` comment. Tag the engineering owner and do not merge until acknowledged.

---

### 4B. AI Prompt Compliance Gate

Any change to a system prompt, few-shot examples, or AI-facing instruction must satisfy **all** of the following before merging. This applies to prompts used in any API call, UI generation step, or AI feature in this product.

#### Required Before Merge

- [ ] **≥5 Good examples** — Inputs that should produce the desired output, with the actual output documented
- [ ] **≥5 Bad examples** — Inputs that should be rejected or handled gracefully, with expected behavior documented
- [ ] **≥5 Reject examples** — Adversarial or out-of-scope inputs the prompt must refuse or deflect
- [ ] **Eval harness result** — Run the prompt change through the eval set; record pass rate vs. baseline
- [ ] **Cost delta** — Document token count change (input + output) vs. the prior prompt version
- [ ] **Latency delta** — Document p50/p95 latency change vs. prior prompt version
- [ ] **PII rejection example** — At least one test case showing the prompt refuses or redacts PII appropriately
- [ ] **Fallback behavior documented** — What happens if the model returns an unexpected format or refuses to respond?

#### Approval Thresholds

| Change | Approval Required |
|---|---|
| Cost increase ≤ 10% | PM self-approval with documented eval result |
| Cost increase 10–25% | Engineering + PM sign-off |
| Cost increase > 25% | Product leadership sign-off required before merge |
| Latency increase > 20% | Engineering review required |
| Eval pass rate drops > 5% | Block merge; root-cause before proceeding |

#### Compliance Checklist Location

Document the compliance checklist in the active EPIC under the relevant Context Window. Example:

```markdown
### AI Prompt Change: [Short description]

**Prompt file**: [path/to/prompt.ts or inline location]
**Prior version**: [hash or description]
**Change**: [What changed and why]

Compliance:
- [ ] ≥5 Good examples (see: temp/prompt-eval-[date].md)
- [ ] ≥5 Bad examples
- [ ] ≥5 Reject examples
- [ ] Eval pass rate: [X%] vs baseline [Y%] (delta: [+/-Z%])
- [ ] Cost delta: [+/-N tokens] per call
- [ ] Latency delta: p50 [+/-Xms], p95 [+/-Xms]
- [ ] PII rejection: [example input + output documented]
- [ ] Fallback: [what happens on unexpected model response]

Approval: [self | eng | leadership] — [Name, date]
```

---

### 4C. Observability Definition of Done

No feature moves to review (v0.8 Release Planning gate) without satisfying this checklist. "We'll add monitoring later" is a gate blocker.

#### Required Before Feature Review

- [ ] **Primary metric dashboard** — A dashboard panel exists tracking the primary KPI- metric for this feature, scoped to users who've used the feature
- [ ] **Guardrail metric alerts** — Alert thresholds defined for all guardrail metrics (from v0.7 A/B Test Design or v0.8 Monitoring Setup). Alert fires before KPI- regresses past acceptable range.
- [ ] **Error rate monitoring** — Feature-specific error rate tracked and alerted if > [threshold in MON- entry]
- [ ] **AI feature cost/latency alerting** (if feature includes AI) — Cost per call and p95 latency alerted if they exceed 110% of the baseline established in the AI Prompt Compliance Gate (4B)
- [ ] **Daily monitoring plan** — For the first 7 days post-launch, a named owner checks the dashboard daily and logs observations in the active EPIC

#### Alert Severity Levels

| Level | Condition | Response time |
|---|---|---|
| **P0 — Page** | Primary KPI- metric drops >20% in 24h; error rate spikes >5x baseline | Immediate (on-call) |
| **P1 — Urgent** | Guardrail metric outside acceptable range for >2h | Within 2 hours |
| **P2 — Warning** | KPI- trending toward threshold; cost/latency creeping up | Next business day |

#### MON- Entry Requirement

Each feature gate must produce at least one `MON-` entry in `SoT/SoT.DEPLOYMENT.md` documenting:
- The metric being monitored
- The alert threshold
- The response action if the alert fires
- The owner responsible for response

This entry must exist before the v0.8 gate is considered passed.
<!-- /SECTION: pm-governance -->
