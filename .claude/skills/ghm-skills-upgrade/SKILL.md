---
name: ghm-skills-upgrade
description: >
  Upgrade local skills to the latest methodology standard by fetching changes from the upstream
  PRD-driven-context-engineering repository. Adds Consumes/Produces connective tissue, confidence
  scoring, and MVP-SCOPE references to all domain skills. Triggers on requests to upgrade skills,
  sync with methodology, apply latest changes, or when user asks "upgrade skills", "sync methodology",
  "apply upstream changes", "update skills to latest", "add consumes produces", "add confidence scores".
---

# Skills Upgrade

Upgrade your local PRD-driven skills to the latest methodology standard. This skill reads the upstream public repository, audits your local skills, and applies three key improvements: **Consumes/Produces connective tissue**, **confidence scoring**, and **MVP-SCOPE references**.

## When to Use This

Run this skill when your product's `.claude/skills/` directory was forked or copied from `mattgierhart/PRD-driven-context-engineering` and the upstream has released improvements that your local skills don't yet have. This is a one-time migration per release — once applied, your skills are current.

## What Changed Upstream (2026-02-26)

Three changes were made across all 25 domain skills:

1. **Consumes/Produces Connective Tissue** — Every skill now explicitly documents what SoT IDs it requires as input and what it produces as output. This creates a transparent workflow graph so that distributed AI agents (working in separate context windows) can trace data flow between skills.

2. **Confidence Scoring on SoT IDs** — Every SoT entry now carries a confidence score (1-5), an evidence source, and a forward target. Different SoT types (CFD, FEA, TECH, DEP, RISK, API, ARC) have specific confidence progressions.

3. **MVP is Sacred (P1 Principle)** — MVP-SCOPE is now an explicit artifact produced by v0.3 Feature Value Planning. Skills discourage premature optimization. A new `PRINCIPLES.md` governance document defines 6 core principles.

---

## Workflow

### Phase 1: Fetch Upstream Reference Files

Fetch these three files from the public repository. They contain the standards your local skills must match.

**File 1 — PRINCIPLES.md** (governance document, confidence model, audit checklist):
```
https://raw.githubusercontent.com/mattgierhart/PRD-driven-context-engineering/main/.claude/skills/PRINCIPLES.md
```

**File 2 — IMPROVEMENT_SUMMARY.md** (change summary, pattern for upgrades, verification steps):
```
https://raw.githubusercontent.com/mattgierhart/PRD-driven-context-engineering/main/.claude/skills/IMPROVEMENT_SUMMARY.md
```

**File 3 — Example updated skill** (v0.5 Tech Stack Selection — fully upgraded reference):
```
https://raw.githubusercontent.com/mattgierhart/PRD-driven-context-engineering/main/.claude/skills/prd-v05-technical-stack-selection/SKILL.md
```

Use WebFetch to retrieve each file. Store the content in working memory — you'll reference it throughout the upgrade.

**Checkpoint**: You should now have:
- The 6 Core Principles (P1-P6)
- The Confidence Score Model (general framework + per-SoT-type progressions)
- The Consumes/Produces format standard
- The Audit Checklist (8 criteria)
- A concrete example of a fully upgraded skill

---

### Phase 2: Inventory Local Skills

List all skill directories in `.claude/skills/prd-v*/` and `.claude/skills/ghm-*/`.

For each skill, check:

| Check | How | Status |
|-------|-----|--------|
| Has `## Consumes` section? | Grep for `## Consumes` in SKILL.md | Yes/No |
| Has `## Produces` section? | Grep for `## Produces` in SKILL.md | Yes/No |
| Has confidence examples? | Grep for `confidence:` in SKILL.md | Yes/No |
| References MVP-SCOPE? | Grep for `MVP-SCOPE` or `MVP` in SKILL.md | Yes/No |
| References PRINCIPLES.md? | Grep for `PRINCIPLES` in SKILL.md | Yes/No |

Output a summary table:

```markdown
| Skill | Consumes | Produces | Confidence | MVP-SCOPE | Status |
|-------|----------|----------|------------|-----------|--------|
| prd-v01-problem-framing | Yes | Yes | Yes | Yes | Current |
| prd-v02-competitive-landscape | No | No | No | No | Needs upgrade |
| ... | ... | ... | ... | ... | ... |
```

**Checkpoint**: You now know exactly which skills need upgrades and what's missing from each.

---

### Phase 3: Upgrade Skills (Batched by Lifecycle Stage)

Process skills in lifecycle order. For each skill that needs upgrades, apply the changes below. **Preserve all existing product-specific content** — these changes are additive.

#### Batch 1: Discovery Skills (v0.1-v0.2)

Skills: `prd-v01-problem-framing`, `prd-v01-user-value-articulation`, `prd-v02-competitive-landscape-mapping`, `prd-v02-product-type-classification`

**Add Consumes section** (after the skill title/intro, before Workflow Overview):

```markdown
## Consumes

This skill requires:
- **[ID-TYPE]-* entries** (from [prior skill]) — [What these provide and why they're needed]
```

For v0.1 skills, Consumes should state: "This skill assumes zero prior research. It is the starting point."

**Add Produces section** (after Consumes):

```markdown
## Produces

This skill creates/updates:
- **[ID-TYPE]-* entries** ([description]) — [What downstream skills need these for]

All [ID-TYPE]- entries should include:
- `confidence: [range]/5` ([evidence level at this stage])
- Evidence source ([what evidence supports this])
- Forward target: "Would move to [X]/5 if [next evidence milestone]"
```

**Confidence guidance for discovery skills**:
- v0.1 outputs: CFD- entries at confidence 1-3/5 (pre-product, research-based)
- v0.2 outputs: CFD- entries at confidence 2-3/5 (competitive research adds evidence)

**MVP-SCOPE guidance for discovery skills**:
- v0.1: Add "MVP scope signal" to Produces — identifies which problem dimensions drive MVP
- v0.2: Reference that competitive analysis feeds into v0.3 MVP-SCOPE definition
- Use language: "This output feeds into v0.3 MVP-SCOPE definition"

#### Batch 2: Commercial Skills (v0.3)

Skills: `prd-v03-outcome-definition`, `prd-v03-pricing-model`, `prd-v03-moat-definition`, `prd-v03-features-value-planning`

These skills are critical for MVP-SCOPE. Feature Value Planning is the skill that **produces** the MVP-SCOPE artifact.

**Consumes**: Reference CFD-* from v0.1-v0.2, KPI-* from Outcome Definition, BR-* from Pricing/Moat
**Produces**: FEA-* entries with confidence 2-3/5, BR-* governance rules, and MVP-SCOPE artifact

**MVP-SCOPE artifact format** (for Feature Value Planning):
```markdown
- **MVP-SCOPE artifact** — Explicit list: "These X features define our MVP"
  - Example: `MVP-SCOPE: 5 P0 features + 3 P1 features = 8 total`
  - This becomes the boundary for v0.4 user journeys and v0.7 build scope
```

#### Batch 3: Journey Skills (v0.4)

Skills: `prd-v04-persona-definition`, `prd-v04-user-journey-mapping`, `prd-v04-screen-flow-definition`

**Consumes**: CFD-* (v0.1-v0.3), FEA-* with MVP-SCOPE (v0.3), BR-* targeting rules (v0.3 Moat)
**Produces**: PER-* (personas), UJ-* (journeys), SCR-* (screens), DES-* (design elements)

**MVP-SCOPE guidance**: These skills consume MVP-SCOPE as a boundary — journeys and screens should map to MVP features only. Add: "Scope journeys/screens to MVP-SCOPE features. Post-MVP features belong in backlog, not in journey maps."

#### Batch 4: Risk & Tech Skills (v0.5)

Skills: `prd-v05-risk-discovery-interview`, `prd-v05-technical-stack-selection`

**Consumes**: All prior IDs as interview/decision context
**Produces**: RISK-* entries, TECH-* entries with decision categories

**Confidence for TECH entries**:
- 1/5: PM preference or team comfort
- 2/5: Team experience with the tool
- 3/5: Local development successful
- 4/5: Staging environment proven
- 5/5: Production deployment successful

**MVP-SCOPE guidance**: "Evaluate technology choices against MVP-SCOPE, not hypothetical 10x scale. Cost assessment should include current-stage cost as primary, scale cost as secondary context."

#### Batch 5: Architecture Skills (v0.6)

Skills: `prd-v06-architecture-design`, `prd-v06-environment-setup`, `prd-v06-technical-specification`

**Consumes**: TECH-* (v0.5), RISK-* (v0.5), FEA-* with MVP-SCOPE (v0.3)
**Produces**: ARC-* (architecture decisions), API-* (endpoint contracts), DBT-* (data models), ENV-* (environment specs)

**Confidence for ARC/API/DBT entries**:
- ARC: 1/5 (decision made) → 5/5 (production proven)
- API: 1/5 (designed on paper) → 5/5 (production tested)

#### Batch 6: Build Skills (v0.7)

Skills: `prd-v07-epic-scoping`, `prd-v07-test-planning`, `prd-v07-implementation-loop`

**Consumes**: API-*, DBT-*, ARC-* (v0.6), FEA-* with MVP-SCOPE (v0.3)
**Produces**: EPIC-* (work packages), TEST-* (test cases), working code with @implements tags

**Connective tissue is critical here**: EPICs must reference specific upstream IDs. Each EPIC is a context-window-sized handoff — a fresh AI agent must be able to pick it up and execute without rework.

#### Batch 7: Release Skills (v0.8)

Skills: `prd-v08-release-planning`, `prd-v08-monitoring-setup`, `prd-v08-runbook-creation`

**Consumes**: EPIC-* (v0.7), TEST-* (v0.7), ARC-* (v0.6)
**Produces**: DEP-* (deployment steps), MON-* (monitoring rules), RUN-* (runbook entries)

**Confidence for DEP entries**:
- 1/5: Planned, not executed
- 2/5: Documented
- 3/5: Local/dev deployment successful
- 4/5: Staging deployment successful
- 5/5: Production deployment successful

#### Batch 8: Launch Skills (v0.9)

Skills: `prd-v09-gtm-strategy`, `prd-v09-launch-metrics`, `prd-v09-feedback-loop-setup`

**Consumes**: FEA-* (v0.3), KPI-* (v0.3), DEP-* (v0.8)
**Produces**: GTM-* (launch plan), KPI-* (launch metrics), CFD-* (post-launch feedback)

**Feedback loop note**: Post-launch CFD- entries should start at confidence 4-5/5 — they represent real user behavior, the highest evidence tier.

---

### Phase 4: Update Frontmatter Descriptions

For each upgraded skill, update the YAML frontmatter `description` field to include Consumes/Produces summary. Follow this pattern:

```yaml
description: >
  [Existing description].
  Consumes [ID-TYPES] (from [prior skills]).
  Outputs [ID-TYPES] with [key attributes].
  Feeds [downstream skills].
```

This ensures the skill's connections are visible even in skill listing views without loading the full SKILL.md.

---

### Phase 5: Verify Upgrades

Run these verification checks after all upgrades:

#### 5a. Connective Tissue Chain Test

Trace the Produces→Consumes chain across the full lifecycle. Every Produces output from skill N should appear in the Consumes input of skill N+1.

```
v0.1 Produces: CFD-*
  → v0.2 Consumes: CFD-* ✓
v0.2 Produces: CFD-* (competitive)
  → v0.3 Consumes: CFD-* ✓
v0.3 Produces: FEA-*, MVP-SCOPE, BR-*, KPI-*
  → v0.4 Consumes: FEA-*, MVP-SCOPE, BR-* ✓
  → v0.5 Consumes: FEA-*, RISK-* ✓
v0.5 Produces: TECH-*, RISK-*
  → v0.6 Consumes: TECH-*, RISK-* ✓
v0.6 Produces: ARC-*, API-*, DBT-*
  → v0.7 Consumes: ARC-*, API-*, DBT-* ✓
v0.7 Produces: EPIC-*, TEST-*, code
  → v0.8 Consumes: EPIC-*, TEST-* ✓
v0.8 Produces: DEP-*, MON-*, RUN-*
  → v0.9 Consumes: DEP-*, KPI-* ✓
```

Flag any breaks in the chain.

#### 5b. Confidence Coverage Test

For each skill that produces SoT IDs, verify:
- At least one example entry includes `confidence: X/5`
- The confidence range is appropriate for the lifecycle stage (earlier stages = lower confidence)
- Forward targets reference realistic next evidence milestones

#### 5c. MVP-SCOPE Reference Test

Verify that:
- v0.3 Feature Value Planning **produces** MVP-SCOPE
- v0.4, v0.5, v0.6, v0.7 skills **reference** MVP-SCOPE as a scope boundary
- No skill assumes scope beyond MVP without flagging it

#### 5d. Product-Specific Content Preserved

Verify that no product-specific customizations were overwritten:
- Custom steps, checklists, or templates unique to this product are intact
- Product-specific examples and references are preserved
- Any custom anti-patterns or quality gates remain

---

### Phase 6: Report

Output a completion report:

```markdown
## Skills Upgrade Report

**Date**: [today]
**Source**: PRD-driven-context-engineering upstream (2026-02-26 release)

### Summary
- Skills upgraded: X / Y total
- Already current: Z
- Skipped (methodology skills): W

### Changes Applied
| Skill | Consumes | Produces | Confidence | MVP-SCOPE | Notes |
|-------|----------|----------|------------|-----------|-------|
| ... | Added | Added | Added | Added | ... |

### Verification
- [ ] Connective tissue chain: Pass/Fail
- [ ] Confidence coverage: Pass/Fail
- [ ] MVP-SCOPE references: Pass/Fail
- [ ] Product content preserved: Pass/Fail

### Next Steps
- Review PRINCIPLES.md for the 6 core principles (P1-P6)
- On next SoT ID creation, include confidence scoring
- On next feature scoping, produce explicit MVP-SCOPE artifact
```

---

## Safety Rules

1. **NEVER delete existing skill content** — all changes are additive (insert sections, not replace)
2. **NEVER overwrite product-specific customizations** — if a skill has custom steps, examples, or references unique to this product, preserve them
3. **NEVER modify SoT/ files** — this skill only touches `.claude/skills/*/SKILL.md` files
4. **Insert Consumes/Produces after the title block**, before Workflow Overview (or equivalent first major section)
5. **Commit incrementally** — one commit per batch, not one giant commit
6. **If a skill already has Consumes/Produces**, verify it matches the upstream pattern but do not overwrite product-specific additions

## Anti-Patterns

| Pattern | Example | Fix |
|---------|---------|-----|
| Overwriting product content | Replacing a custom v0.3 skill with upstream version | Only add Consumes/Produces/confidence; preserve everything else |
| Skipping verification | "All skills updated" without chain test | Run Phase 5 verification — broken chains cause downstream failures |
| Generic confidence scores | `confidence: 3/5` with no source or target | Always include: score + source + forward target |
| MVP-SCOPE in wrong skill | Adding MVP-SCOPE production to v0.5 | Only v0.3 Feature Value Planning **produces** MVP-SCOPE; others **reference** it |

## Handoff

After this skill completes, your local skills match the upstream methodology standard. Future improvements to the methodology will be communicated through the same upstream repository. Run `ghm-template-sync` periodically to check for structural changes beyond skills.
