# PM Governance Rules

These rules define what a PM can directly commit, what requires engineering escalation, what AI prompt changes require before merge, and what observability gates must be met before any feature review. They apply to all product work done in a repo that adopts this methodology.

## 4A. PM Shipping Zone

Defines what a PM can commit directly vs. what must go through engineering review.

### ✅ PM Can Commit Directly

| Category | Examples |
|---|---|
| **Copy** | CTAs, tooltips, error messages, onboarding text, empty states, labels |
| **Feature flags** | Toggling existing flags; adjusting flag values within documented ranges |
| **Config values** | Non-secret config values (e.g., rate limits, thresholds already in env) |
| **AI prompts** | System prompts and few-shot examples — **subject to AI Prompt Compliance Gate (4B)** |
| **Design tweaks** | CSS adjustments, spacing, color on pre-approved component library components |
| **Planning docs** | PRD.md updates, EPIC files, SoT entries, README updates |
| **Release notes** | User-facing release notes and stakeholder summaries |

### ❌ PM Must Escalate to Engineering

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

## 4B. AI Prompt Compliance Gate

Any change to a system prompt, few-shot examples, or AI-facing instruction must satisfy **all** of the following before merging. This applies to prompts used in any API call, UI generation step, or AI feature in the product.

### Required Before Merge

- [ ] **≥5 Good examples** — Inputs that should produce the desired output, with the actual output documented
- [ ] **≥5 Bad examples** — Inputs that should be rejected or handled gracefully, with expected behavior documented
- [ ] **≥5 Reject examples** — Adversarial or out-of-scope inputs the prompt must refuse or deflect
- [ ] **Eval harness result** — Run the prompt change through the eval set; record pass rate vs. baseline
- [ ] **Cost delta** — Document token count change (input + output) vs. the prior prompt version
- [ ] **Latency delta** — Document p50/p95 latency change vs. prior prompt version
- [ ] **PII rejection example** — At least one test case showing the prompt refuses or redacts PII appropriately
- [ ] **Fallback behavior documented** — What happens if the model returns an unexpected format or refuses to respond?

### Approval Thresholds

| Change | Approval Required |
|---|---|
| Cost increase ≤ 10% | PM self-approval with documented eval result |
| Cost increase 10–25% | Engineering + PM sign-off |
| Cost increase > 25% | Product leadership sign-off required before merge |
| Latency increase > 20% | Engineering review required |
| Eval pass rate drops > 5% | Block merge; root-cause before proceeding |

### Compliance Checklist Location

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

## 4C. Observability Definition of Done

No feature moves to review (v0.8 Release Planning gate) without satisfying this checklist. "We'll add monitoring later" is a gate blocker.

### Required Before Feature Review

- [ ] **Primary metric dashboard** — A dashboard panel exists tracking the primary KPI- metric for this feature, scoped to users who've used the feature
- [ ] **Guardrail metric alerts** — Alert thresholds defined for all guardrail metrics (from v0.7 A/B Test Design or v0.8 Monitoring Setup). Alert fires before KPI- regresses past acceptable range.
- [ ] **Error rate monitoring** — Feature-specific error rate tracked and alerted if > [threshold in MON- entry]
- [ ] **AI feature cost/latency alerting** (if feature includes AI) — Cost per call and p95 latency alerted if they exceed 110% of the baseline established in the AI Prompt Compliance Gate (4B)
- [ ] **Daily monitoring plan** — For the first 7 days post-launch, a named owner checks the dashboard daily and logs observations in the active EPIC

### Alert Severity Levels

| Level | Condition | Response time |
|---|---|---|
| **P0 — Page** | Primary KPI- metric drops >20% in 24h; error rate spikes >5x baseline | Immediate (on-call) |
| **P1 — Urgent** | Guardrail metric outside acceptable range for >2h | Within 2 hours |
| **P2 — Warning** | KPI- trending toward threshold; cost/latency creeping up | Next business day |

### MON- Entry Requirement

Each feature gate must produce at least one `MON-` entry in `SoT/SoT.DEPLOYMENT.md` documenting:

- The metric being monitored
- The alert threshold
- The response action if the alert fires
- The owner responsible for response

This entry must exist before the v0.8 gate is considered passed.
