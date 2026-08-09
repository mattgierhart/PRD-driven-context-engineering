---
title: "GearHeartAI.org · PRD-CE V2 Product Management Site Brief"
date: "2026-08-08"
status: "Planning brief — V2 proposed; owner review required before implementation or release"
audience: "Coding agent responsible for GearHeartAI.org"
product_generation: 2
source_repository_branch: "codex/prd-ce-v2-product-model"
source_review_commit: "REQUIRED_AT_SITE_EXECUTION — use a sanitized immutable commit"
research_blueprint_original_sha256: "afe50856ff70f9dcf00eafe9ecc41df7eaea5310c395c936af16cb8e706e45a5"
research_blueprint_file_sha256: "e32ecaba7db51ffbcabee8f29550a63b7cb828bd781567ba23bd690f146c4f83"
research_blueprint_path: "docs/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md"
build_plan_path: "docs/PRD_CE_V2_BUILD_PLAN.md"
---

# GearHeartAI.org · PRD-CE V2 Product Management Site Brief

## 1. Assignment

Update GearHeartAI.org so it presents PRD-Led Context Engineering as a focused Product Management
lifecycle product people can understand, trust, and begin using—not as an inventory of methodology
mechanics or a catalogue of possible GearHeart products.

The site should introduce the proposed second product generation through one memorable promise:

> **Your product should remember.**

The first viewport must make the Product Management outcome tangible: a team can inspect what is
current, why it is true, what conflicts with it, what delivery or learning depends on it, and what
decision should happen next. The deeper architecture—Markdown Source of Truth, typed IDs,
relationships, provenance, temporal history, generated indexes, skills, hooks, and policies—supports
that experience and should be progressively disclosed.

> **Truth boundary:** This brief defines the eventual scope of an illustrative website experience;
> current approval covers planning and shaping only. Implementation requires separate owner
> approval. The site may not present a working V2 parser, index, Change Set runtime, `/product`
> command, MCP tool, or hosted service. No V2 runtime existed on the source branch when this brief
> was prepared.

When implementation is separately approved, this brief limits changes to the GearHeartAI.org
codebase. It does not authorize changes to the PRD-CE repository, production data, external
accounts, analytics providers, email systems, or public release settings unless those are
separately requested.

## 2. Product and naming architecture

Use this hierarchy to keep the current product specific while preserving GearHeart AI as the
publisher:

| Level | Working name | Role | Public status |
|---|---|---|---|
| Publisher / umbrella | **GearHeart AI** | Creates AI-native operating methods and products | Existing |
| Product Management product | **The Product Model** | Working public name for the Product Management lifecycle experience | Working name; owner approval required |
| Transition label | **PRD-CE V2** or **PRD-Led Context Engineering V2** | Connects the proposed experience to the existing repository and community | Use alongside the approved product name during transition |
| Current foundation | **PRD-Led Context Engineering** | Existing open methodology and repository | Available now, subject to claim verification |

Recommended first public reference:

> **The Product Model — the next generation of PRD-Led Context Engineering.**

Do not name, market, preview, or measure future GearHeart products in this release. Do not rename
repositories, packages, commands, or the organization from this brief. Naming remains a product
decision. In code and metadata, keep `product_generation: 2` distinct from PRD lifecycle gate,
repository, template, plugin, and package versions.

## 3. Source basis and authority

The coding agent must read the target site's local instructions and source before changing it. Treat the following as the content basis for this redesign:

- The canonical root [`PRD.md`](../PRD.md), initialized at v0.1, plus its accepted BR/ARC records.
- The proposed [V2 build plan](PRD_CE_V2_BUILD_PLAN.md), which supplies contingent sequencing
  subordinate to the PRD and accepted SoT.
- The preserved [V2 research blueprint](MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md), version 2.1, with original-source and current-file fingerprints in this document's frontmatter.
- The canonical [PRD-CE repository](https://github.com/mattgierhart/PRD-driven-context-engineering).
  Before implementation, replace `source_review_commit` with the sanitized immutable commit the
  site agent actually reviewed; do not expose an earlier unsanitized evaluation package.
- The current [GearHeartAI.org site](https://www.gearheartai.org/).
- The current [Impeccable homepage](https://impeccable.style/), [design workflow](https://impeccable.style/designing/), [documentation](https://impeccable.style/docs/), and [getting-started tutorial](https://impeccable.style/tutorials/getting-started/).

This brief is self-contained for website planning. At execution time, record the exact reviewed
source-branch commit in the site repository's provenance config; do not use a mutable branch name as
public evidence. If the build plan or research blueprint is unavailable, do not invent missing
detail or represent the proposal as implemented. Do not link a public site to a machine-local path.

Authority rules:

1. PRD-CE remains the canonical methodology source. GearHeartAI.org is a presentation and distribution surface, not a competing Source of Truth.
2. The root PRD and accepted SoT govern product truth. The build plan is proposed sequencing and the
   research blueprint is input; none of them proves that a feature ships without executable evidence.
3. Website copy must resolve from a small, explicit capability-status model. Each public capability record must include `status`, `sourceUrl`, `sourceCommitOrRelease`, and `verifiedAt`; validation must reject factual claims whose provenance is missing or stale under the site's policy. Do not duplicate changing counts or release claims across components.
4. Never invent customers, testimonials, adoption metrics, benchmarks, installation commands, working integrations, or product screenshots.
5. Every factual product claim must link to a current artifact, release, demo, or repository source. Clearly labeled illustrative fixture data is exempt because it is not a product claim, but it must never be mixed with real evidence.

For this implementation, missing provenance is a build failure. Reverify time-bound claims—release
status, install commands, counts, compatibility, dates, and “current” availability—in the same
implementation session and whenever `sourceCommitOrRelease` changes. Stable principles may cite an
immutable source without an invented time-to-live. Age review beyond those triggers remains manual
until the site defines a separate owner-approved staleness policy.

## 4. Truth boundary: what the site may say

Before implementation, verify every row against the current PRD-CE checkout and public release surface. Store the result in one typed content/config object so badges, buttons, metadata, and copy cannot drift.

| Capability | Default website status | Copy rule |
|---|---|---|
| Markdown Source of Truth, typed IDs, relationship model, lifecycle methods, and existing skills | **Available in the current methodology** | Link to exact repository documentation; do not publish a skill count until generated from one canonical registry |
| Fork-based adoption and deterministic self-install prototype | **Available / prototype**, after live verification | Use the exact verified command only; identify prototype status where applicable |
| Packaged Claude Code plugin / plugin marketplace install | **Unverified release status** | Do not show as a primary CTA until an end-to-end public install succeeds |
| Human-facing SoT HTML companion | **Available as a review view** | Describe as a derived human-review surface, not the canonical editor |
| Interactive deliverables/input mode | **Concept** | Do not render as shipped functionality |
| Development Graph extraction | **Planned unless an extractor is verified** | Do not imply that an AST extractor currently ships |
| Read-only Compatibility Inspector (`index`, `check`, `query`, `trace`) | **Proposed alpha** | May be explained or illustrated; do not present commands as runnable until a release verifies them |
| V2 `/product` interface, Change Set runtime, accepted-state mutation, MCP, graph JSON, viewer, and context compilation | **Proposed later work** | Keep out of the primary product proof; do not imply availability |
| Hosted graph, continuous sync, cloud, registry/marketplace, enterprise governance, or portfolio analytics | **Outside the current product release** | Do not market, navigate to, price, or collect demand for these from this brief |

Use plain labels such as `Available now`, `Prototype`, `V2 proposed`, and `Illustrative preview`.
Do not use ambiguous labels such as `New`, `Live`, `In development`, or `Coming soon` without a
verified release target.

## 5. Audience and jobs to be done

### Proposed site-shaping audience (pending v0.2 evidence and owner decision)

Product managers, product leaders, and product operations leaders responsible for a long-lived
product that is increasingly shaped with multiple AI agents. They have evidence, decisions,
requirements, delivery state, release learning, and rationale spread across PRDs, tickets, code,
tests, chats, dashboards, and individual memory. They want each human and agent to work from current
context without re-briefing or silent invention.

This is a content-shaping hypothesis, not the accepted v0.2 primary segment. The product owner must
select the primary audience and “not for” boundary from accepted, reviewable evidence before the
PRD advances to v0.2; implementation agents must not infer that decision from this brief.

### Secondary audiences

- Solo product builders who have outgrown one-shot prompting.
- Engineering, design, research, data, and operations collaborators who consume or update product
  context.
- Teams in regulated or dependency-heavy domains that need provenance and change history.
- Framework and agent-tooling contributors evaluating an open, local-first foundation.

### Core jobs

1. Tell me what the product currently believes.
2. Show me why that belief exists and where it came from.
3. Show me what contradicts it or has become stale.
4. Show me which journeys, requirements, delivery artifacts, tests, releases, and learning depend on
   it.
5. Help me propose and review a change without erasing history.
6. Give the next human or agent only the context needed for the work at hand.

The homepage should serve these jobs before teaching ontology or lifecycle stages.

## 6. Release scope for the website

### Required in this implementation

- A redesigned homepage with an outcome-led hero and a visible product proof interaction.
- A short explanation of the Product Management loop: Explore → Shape → Decide → Build → Learn,
  with Check as a cross-cutting action. `Build` remains a working verb pending owner confirmation.
- A clear comparison of current knowledge, proposed change, and observed reality.
- A truthful available/proposed capability presentation. Do not turn the internal roadmap into a
  public feature catalogue.
- One focused Product Management lifecycle story; no adjacent-product cards or teasers.
- Working links to verified documentation, source, and contact surfaces.
- Responsive, accessible, reduced-motion, and no-JavaScript fallbacks for essential content.
- SEO and social metadata aligned to the new promise.
- Automated content, accessibility, performance, and visual checks proportionate to the existing stack.

### Preserve

- The GearHeart AI name and existing logo unless the user separately approves a brand change.
- Working privacy, terms, contact, newsletter, and analytics behavior. If a surface cannot be verified, retain it unchanged or remove the new call-to-action rather than simulate success.
- The current technical stack, routing model, package manager, deployment path, and component conventions unless a change is necessary and justified.

### Do not build in this pass

- A real graph database, V2 query backend, authentication, user accounts, cloud dashboard,
  marketplace, pricing system, or adjacent methodology workflow.
- A general node-link graph canvas.
- Fake terminal output presented as a live system.
- Empty navigation destinations.
- A clone of Impeccable's site, assets, layout, command names, dark/gold identity, or motion choreography.
- A second editable copy of PRD-CE product facts inside arbitrary components.

## 7. Recommended information architecture

Keep the first release intentionally shallow. If the current site is a single-page application, these may be anchored sections rather than new routes.

### Primary navigation

1. **Product Management** — scrolls to or opens the lifecycle explanation.
2. **How it works** — the loop and proof interaction.
3. **Proof** — the illustrative current/evidence/impact/next-decision specimen.
4. **Docs** — verified documentation destination.
5. **GitHub** — canonical repository.

Keep one strong header action. Before V2 installation is verified, use **Explore the methodology** or **View on GitHub**, not **Install V2**.

### Possible later navigation, not required now

- Demo / Explorer
- Failure Modes
- Research
- Changelog

Add these only when each destination contains real, maintained Product Management content. Do not
reserve empty navigation for speculative platform surfaces or future products.

## 8. Homepage narrative and content contract

### Section 1 — Hero: outcome plus proof

**Headline**

> Your product should remember.

**Recommended subhead**

> GearHeart AI is validating a Product Management model that connects what your team learns,
> decides, delivers, and observes—so every human and agent can inspect what is current, why it is
> true, and what decision should happen next.

**Actions**

- Primary: **Explore the Product Model** → scroll to the proof interaction.
- Secondary: **View PRD-CE on GitHub** → verified repository URL.
- Nearby status text, not a decorative hero pill: **V2 is proposed and being validated. The current
  open methodology is available today.**

**Hero proof interaction**

Show an inspectable answer rather than an abstract graph. Use the same clearly illustrative product-decision fixture throughout the hero, adjudication section, motion story, and tests. Recommended default question:

> Why is the free workspace limit five members?

Recommended answer structure:

- **Current decision:** Free workspaces allow five active members.
- **Why:** The original decision cites a support-cost threshold and a conversion experiment.
- **New evidence:** A later cohort result contradicts the original cost assumption.
- **Impact:** The entitlement API, onboarding copy, pricing page, and tests depend on the decision.
- **Next action:** Review the proposed change from five to seven members.
- **Source:** `Illustrative Product Model fixture — not customer or production data.`

Offer two additional deterministic questions if they improve the interaction without obscuring the page:

- **What depends on this decision?**
- **What changed after the new evidence?**

The interaction must visibly carry both labels: `Illustrative Product Model` and `V2 interaction preview`. It must work by keyboard, expose selected state, announce result changes accessibly, and render a complete static answer when JavaScript is unavailable. It is a product preview, not a chat box; do not accept free-form input unless a real system handles it.

### Section 2 — The problem: product archaeology

Lead with the consequence, not a history lesson:

> Every agent session starts smart and forgets the product. Teams pay for that amnesia through repeated briefings, re-litigated decisions, unexplained code, and documentation that cannot say what is current.

Use a compact before/after comparison:

| Without a Product Model | With a Product Model |
|---|---|
| Context scattered across files, tools, and conversations | Accepted knowledge has durable addresses and provenance |
| Proposed changes overwrite or bypass current truth | Current and proposed meaning remain distinct |
| An agent sees prose but not authority or history | Context includes evidence, status, relationships, and supersession |
| Release learning disappears into chat and dashboards | Reality can challenge intent and propose the next change |

Do not repeat the current site's Waterfall → Agile → Context Engineering manifesto before the user has seen this concrete value. That history may remain as a deeper explanation.

### Section 3 — The Product Management loop

Render the loop as five user verbs, with Check visibly crossing the sequence:

1. **Explore** — gather evidence and surface uncertainty.
2. **Shape** — turn evidence into a coherent proposed change.
3. **Decide** — accept, reject, revise, deprecate, or supersede with rationale.
4. **Build** — compile relevant context, implement, trace, and verify.
5. **Learn** — compare intent with customer and operational reality.
6. **Check** — detect conflicts, stale assumptions, missing evidence, and drift at every stage.

Avoid presenting the current ten lifecycle stages or dozens of skills as the primary navigation.
They remain valuable Product Management playbooks behind the simpler surface.

### Section 4 — The decision boundary: proposed adjudication

Continue the hero's illustrative fixture as one small semantic-change specimen. Label this section
`Proposed later workflow`; it explains the intended authority boundary and is not the first alpha
proof:

```text
CURRENT      BR-104 · Free plan member limit · Accepted
EVIDENCE     CFD-140 · New cohort result · Contradicts current assumption
PROPOSED     CHG-142 · Change limit from five to seven
IMPACT       API contract · onboarding copy · pricing page · tests
DECISION     Accept · Reject · Revise
HISTORY      Original decision and rationale remain queryable
```

This is illustrative data. Label it **Illustrative Product Model** and never imply it is GearHeart customer evidence or a live customer system.

Explain the point in one sentence:

> AI can generate options; only an attributable decision turns an option into organizational memory.

### Section 5 — V2 promises being proven

Present these V2 design principles as commitments being proven, not shipped runtime behavior:

- **Markdown you own** — accepted product memory stays inspectable and version-controlled.
- **Local by default** — accepted product memory remains usable in files and Git; the current
  product path does not depend on a hosted service.
- **Durable addresses** — typed IDs keep decisions, journeys, contracts, evidence, code, and tests referable.
- **History without erasure** — rejected and superseded meaning remains available.
- **Derived speed** — query indexes and views can be rebuilt from the canonical files.

Do not lead this section with database brands or a file tree.

### Section 6 — First executable proof: read-only inspection

Center the proposed read-only Compatibility Inspector rather than speculative command chrome. Show
one in-place repository inspection with four outcomes:

| Inspector outcome | Product Management value | Status |
|---|---|---|
| Identity and relationship integrity | Know which durable decisions and requirements are actually connected | Proposed alpha |
| Provenance and lifecycle integrity | See why a claim is authoritative and which lifecycle state it belongs to | Proposed alpha |
| Temporal and process-history integrity | Preserve supersession, work sessions, checkpoints, and release learning | Proposed alpha |
| Local repository divergence | See when meaningful branch state creates more than one current story | Proposed alpha |

The specimen may name the planned internal CLI verbs `index`, `check`, `query`, and `trace` in a
clearly labeled technical detail. Do not style them as runnable commands, add copy buttons, or imply
that a released executable exists.

### Section 7 — One GearHeart product path

**Product Management — current methodology available; V2 proposed**

Connect evidence, product decisions, journeys, requirements, delivery, tests, releases, telemetry,
and feedback so Product Management compounds rather than resets.

GearHeartAI.org presents no additional product or use-case cards in this release. Keep the content
model modular enough for independently governed products later, but do not name, preview, route to,
or collect demand for them here.

### Section 8 — Current foundation and V2 direction

Use an honest transition block:

- **Available today:** the current open PRD-Led Context Engineering methodology. Present its prototype adoption path only after the public commands and links are verified.
- **Being proven next:** a smaller product surface over the same Markdown SoT, IDs, relationships, temporal history, and governance principles.
- **First proof:** useful findings from an existing repository before a user learns the ontology.

Include links to the canonical repository and a maintained roadmap/changelog if one exists. Do not use stale readiness files, old skill counts, or roadmap prose as live telemetry.

### Section 9 — Final action

Until the V2 runtime is released:

**Headline:** Build with memory now. Follow the Product Model as it becomes real.

- Primary: **Explore the current methodology**.
- Secondary: **Follow V2 development** only if there is a public branch, issue, discussion, changelog, or newsletter destination.

After a verified V2 release, replace these actions through the central status/config model rather than editing multiple page sections.

## 9. Visual direction

The homepage's visitor mode is **Persuade**: make the Product Management offer intelligible,
desirable, provable, and actionable in the first viewport. Readability and operational clarity still
govern the supporting explanation and specimen, but nested sections do not become separate visual
worlds or persisted surface modes.

No visual direction is selected by this brief. The downstream Impeccable direction process owns
that decision with the product owner. Treat the following as inputs and boundaries:

- Preserve the verified GearHeart name, mark, and binding brand assets unless the owner separately
  approves a replacement.
- Demonstrate the product with inspectable evidence, decision, lifecycle, delivery, and history
  states—not decorative AI imagery or a generic node cloud.
- Make source annotations, status, contradiction, impact, and time legible without requiring graph
  vocabulary.
- Keep the first viewport specific: one promise, one visible proof, and one real action.
- Do not copy Impeccable's assets, composition, palette, typography, command names, or motion.
- Avoid generic AI-site defaults such as glowing gradients, arbitrary icon tiles, nested card grids,
  pill saturation, or empty cinematic scroll space unless the selected direction proves a
  product-specific reason.
- Use no factual claim, customer, benchmark, screenshot, or capability that the product record and
  provenance model do not support.

### Motion language

Motion should explain state change:

- Evidence enters.
- A contradiction becomes visible.
- A proposed change shows its impact.
- A human decision changes current state.
- Prior state moves into history without disappearing.

These are narrative requirements, not a selected motion language. The chosen direction may express
them differently. Avoid continuous ambient animation, scroll capture, parallax that delays reading,
or motion that simulates a working runtime. Respect `prefers-reduced-motion`; the reduced-motion
version must preserve meaning and hierarchy.

## 10. Required Impeccable workflow in the site repository

Use Impeccable as the design and quality workflow, not as a visual template.

1. Read the site repository's governing instructions, current content model, routes, dependencies,
   components, analytics, deployment configuration, and dirty worktree state.
2. Run Impeccable context resolution once for the homepage target. Check whether `PRODUCT.md`,
   `DESIGN.md`, a surface brief, or an incumbent visual system already exists; never overwrite
   trusted human decisions.
3. If `PRODUCT.md` is missing or materially stale, run `init` and complete its product-truth
   interview before design work. It must record the Product Management audience, purpose, evidence,
   constraints, platform, and open decisions. It does not choose a visual world or write
   `DESIGN.md`.
4. Determine whether the site extends an established visual world or replaces it. Use `document`
   before design only when the incumbent world is intentionally being extended. For a replacement,
   treat the old interface as evidence and write the new `DESIGN.md` from the finished build.
5. Run [`shape`](https://impeccable.style/docs/shape/) for the homepage. Shape conducts discovery,
   enters the current new-work direction process when a new or replacement world is needed, returns
   a confirmed shape/design brief with the selected direction, and stops before persistence or
   implementation. Do not run a redundant second direction-selection cycle.
6. When implementation is separately authorized, resume the current
   [new-work flow](https://impeccable.style/docs/new-work/). If image generation is available,
   present the required compositional options and obtain approval of the selected high-fidelity
   composition before code. Persist a route-specific surface brief only in this resumed flow.
7. Implement the approved composition within the existing stack. Reproduce the approved first
   viewport before extending the rest of the page.
8. Inspect bounded desktop and mobile renders, fix material gaps, and run the deterministic detector
   once after the UI is finished—not during concept selection.
9. Run the fresh finish reviewer with the request, approved direction/comp, screenshots, target, and
   detector findings. Close or explicitly disposition its material findings.
10. Run the documenter after the reviewed build so `DESIGN.md` records the system that actually
    shipped. Record intentional detector exceptions with rationale rather than weakening rules.

Human approval is required at these boundaries:

- Selecting the new visual direction, accepting the high-fidelity composition, and changing the
  logo or brand identity are separate approval decisions.
- Publishing new product names, install commands, availability claims, customer proof, pricing, or dates.
- Adding a new dependency with material bundle, security, or maintenance cost.
- Deploying the redesign to production.

## 11. Sustainable implementation guidance

- Reuse the existing framework and design primitives. Do not rewrite the site or upgrade its framework merely to achieve the redesign.
- Store status-sensitive product copy and destinations in one schema-validated content module or content file. Components should render it; they should not each own a copy.
- Keep illustrative Product Model records in a clearly named fixture. The same fixture should feed the visual demo and tests.
- Build the proof interaction as deterministic, local presentation state for this release. Do not introduce a backend for a preview.
- Use semantic component boundaries based on user meaning, such as `ProductAnswer`,
  `InspectorFinding`, `ChangePreview`, `CapabilityStatus`, and `ProductLifecycle`, without creating a
  generic design-system abstraction for one-off sections or speculative future products.
- Preserve progressive enhancement. Essential copy and source links must exist in server-rendered or static markup.
- Prefer CSS and existing motion utilities. Add a motion or visualization library only after demonstrating that the existing stack cannot express the approved interaction accessibly and performantly.
- Generate dynamic counts and compatibility lists from a single manifest. If no canonical manifest exists, omit the number.
- Validate all external links and remove dead navigation rather than shipping placeholders.
- Keep website facts attributable to a repository commit or release identifier.

## 12. Accessibility, performance, and resilience

### Accessibility

- Semantic landmarks and one logical `h1`.
- Full keyboard operation and visible focus for navigation and the proof interaction.
- WCAG AA contrast for text and controls in every theme/state.
- Accessible names and state for tabs, toggles, copy buttons, and expandable details.
- Result changes announced without stealing focus.
- No information encoded only by color, animation, or spatial position.
- Reduced-motion behavior tested, not merely declared.
- Screen-reader order matches the visual argument.

### Performance targets

Unless the existing project defines stricter budgets, target:

- LCP at or below 2.5 seconds on a representative mobile production build.
- CLS at or below 0.1.
- INP at or below 200 milliseconds.
- No autoplay video or hero media required to understand the product.
- Responsive images, subset fonts, and no decorative asset that dominates initial transfer size.

Record the test environment with the result. Do not present lab scores as universal field performance.

### Resilience

- Core narrative and source links remain usable with JavaScript disabled.
- Interactive preview has a readable static default.
- Failed analytics, newsletter, or third-party scripts do not block content.
- External requests have explicit purpose; avoid sending repository or visitor context to third parties.

## 13. Responsive behavior

Validate at minimum:

- 390px mobile portrait.
- 768px tablet portrait.
- 1024px compact desktop/tablet landscape.
- 1440px desktop.
- A wide display representative of the current site's presentation environment.

The hero proof interaction should follow the headline on narrow screens rather than shrinking into illegibility. Semantic diffs should wrap by field and retain status labels. The product loop may become a vertical sequence on mobile. Do not hide critical evidence or availability labels at smaller breakpoints.

## 14. SEO and sharing

Recommended pre-release defaults, subject to final naming approval:

- **Title:** `GearHeart AI | PRD-Led Context Engineering`
- **Description:** `Explore an open, local-first Product Management methodology for durable product memory—and preview the proposed next experience for humans and AI agents.`
- **Primary phrase:** `AI product memory`
- **Supporting phrases:** `context engineering`, `AI product management`, `PRD-Led Context Engineering`, `product knowledge graph`

Add canonical URL, Open Graph metadata, social image, descriptive alt text, and Organization metadata only where the facts are verified. Do not publish SoftwareApplication or SoftwareSourceCode structured data for the V2 Product Model until a public release and canonical artifact exist. A social image should show the GearHeart Product Model interaction, not generic AI imagery, and must visibly identify it as a V2 preview.

## 15. Measurement

Use the site's existing analytics abstraction. Do not add a new provider from this brief.

Recommended events:

| Event | Meaning |
|---|---|
| `product_model_explore` | Visitor invokes the hero proof interaction |
| `product_question_select` | Visitor selects a preview question |
| `github_open` | Visitor opens the canonical repository |
| `methodology_start` | Visitor opens the verified current methodology or prototype adoption destination |
| `v2_follow` | Visitor opens a real V2 follow destination |
| `lifecycle_stage_view` | Visitor examines a Product Management lifecycle stage or proof |

Do not collect the content of arbitrary visitor questions. The first release should not offer free-form query input.

Success signals for the redesign:

- A first-time visitor can explain the core product outcome after the hero and proof interaction.
- The visitor can distinguish what is available now from the proposed V2 preview.
- The primary CTA reaches a real next step.
- Product Model interaction use and repository/adoption clicks can be measured without invasive tracking.

## 16. Verification and acceptance criteria

### Content and truth

- [ ] The site uses the approved naming stack consistently.
- [ ] Every capability has one explicit status sourced from the central content model.
- [ ] Every factual capability record has `sourceUrl`, `sourceCommitOrRelease`, and `verifiedAt`; the build fails closed when required provenance is missing.
- [ ] No unverified install command, feature count, integration, customer, metric, testimonial, or release date appears.
- [ ] No adjacent product or future methodology is named, marketed, previewed, or measured.
- [ ] PRD-CE repository and source links resolve.
- [ ] Preview data is labeled illustrative or V2 preview.

### Product experience

- [ ] The hero leads with “Your product should remember” or approved replacement and a concrete outcome.
- [ ] A visible “what is current and why?” proof interaction works without a backend.
- [ ] Current, evidence, proposed change, impact, decision, and history are visually distinguishable.
- [ ] The page explains Explore → Shape → Decide → Build → Learn and cross-cutting Check.
- [ ] The first actionable destination is available within one click.
- [ ] No dead links or placeholder routes ship.

### Design quality

- [ ] GearHeart has a distinct visual system; no copied Impeccable assets, composition, or black/gold identity.
- [ ] The design uses real product/state specimens instead of generic AI decoration.
- [ ] Typography, spacing, color, and motion decisions are captured in the site's design context.
- [ ] The owning Impeccable new-work flow, bounded render inspection, one deterministic detector
  pass, fresh finish review, and final design documentation are complete.
- [ ] P0 and P1 findings are resolved; intentional lower-severity exceptions have written rationale.

### Engineering quality

- [ ] Existing stack, deployment, analytics, and legal surfaces remain functional.
- [ ] Lint, type checks, build, and existing tests pass.
- [ ] The proof fixture drives both rendering and tests.
- [ ] Responsive checks pass at the required widths.
- [ ] Keyboard, screen-reader, contrast, reduced-motion, and no-JavaScript checks pass.
- [ ] Performance budgets are met or a measured exception is documented.
- [ ] Production deployment occurs only after user approval and preview review.

## 17. Agent execution order

1. Inspect the site repository and report the current stack, instructions, routes, content sources, design tokens, test commands, deployment path, analytics, and any dirty worktree state.
2. Verify the capability-status matrix against public and repository evidence. Return discrepancies before changing public claims.
3. Resolve Impeccable context once. Complete `init` only if product truth is missing or stale; do not
   overwrite trusted human decisions.
4. Run `shape`; complete its discovery and direction-selection flow, then stop for owner
   confirmation of the resulting brief, working name, and visual direction.
5. When implementation is authorized, produce and obtain separate approval of the required
   high-fidelity composition before code.
6. Implement the approved homepage composition with one deterministic, explicitly illustrative
   Product Management fixture.
7. Run bounded desktop/mobile inspection, the one detector pass, fresh finish review, accessibility,
   responsive, performance, and engineering checks. Record `DESIGN.md` from the reviewed build.
8. Provide a preview URL or local review path plus screenshots at the required widths.
9. Report changed files, verified claims, proposed-only content, test results, reviewer disposition,
   and intentional design-rule exceptions.
10. Wait for explicit approval before production deployment.

## 18. Owner decisions before public release

Recommended defaults authorize discovery and preparation of a reviewable shape brief. They do not authorize bypassing the direction and comp approval gates, publishing changed product claims, or deploying to production.

| Decision | Recommended default |
|---|---|
| Public flagship name | **The Product Model** with transition label **PRD-CE V2** |
| Hero promise | **Your product should remember.** |
| Pre-release primary CTA | **Explore the Product Model** → deterministic preview |
| Pre-release secondary CTA | **View PRD-CE on GitHub** |
| V2 availability language | **Proposed and being validated** |
| Product scope | **Product Management lifecycle only; do not market future products** |
| Brand direction | Evolve the existing GearHeart identity; do not imitate Impeccable's identity |
| Production release | Preview and explicit owner approval required |

## 19. Brief completion definition

The update is successful when GearHeartAI.org feels as productized and demonstrative as Impeccable without resembling it: one clear promise, one visible proof, one coherent vocabulary, one honest next step, and deeper rigor available on demand.

The site should make V2 desirable while remaining precise about what exists today.
