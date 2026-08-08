---
title: "GearHeartAI.org · PRD-CE V2 Product Site Brief"
date: "2026-08-07"
status: "Implementation brief — owner review required before public release"
audience: "Coding agent responsible for GearHeartAI.org"
product_generation: 2
source_repository_commit: "30ed1b07c9945fc66a18d03fdf5bb870293bee3f"
research_blueprint_sha256: "afe50856ff70f9dcf00eafe9ecc41df7eaea5310c395c936af16cb8e706e45a5"
research_blueprint_path: "docs/MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md"
---

# GearHeartAI.org · PRD-CE V2 Product Site Brief

## 1. Assignment

Update GearHeartAI.org so it presents PRD-Led Context Engineering as a product people can understand, trust, and begin using—not as an inventory of methodology mechanics.

The site should introduce the proposed second product generation through one memorable promise:

> **Your product should remember.**

The first viewport must make the outcome tangible: a product can answer what is current, why it is true, what conflicts with it, and what should happen next. The deeper architecture—Markdown Source of Truth, typed IDs, relationships, Change Sets, temporal history, generated indexes, skills, hooks, and policies—supports that experience and should be progressively disclosed.

This brief authorizes changes to the GearHeartAI.org codebase only. It does not authorize changes to the PRD-CE repository, production data, external accounts, analytics providers, email systems, or public release settings unless those are separately requested.

## 2. Product and naming architecture

Use this hierarchy so GearHeart can grow beyond product engineering without making the current site vague:

| Level | Working name | Role | Public status |
|---|---|---|---|
| Publisher / umbrella | **GearHeart AI** | Creates AI-native operating methods and products | Existing |
| Flagship product | **The Product Model** | The public product experience proposed by the V2 research | Working name; owner approval required |
| Transition label | **PRD-CE V2** or **PRD-Led Context Engineering V2** | Connects the new experience to the existing repository and community | Use alongside “The Product Model” during transition |
| Current foundation | **PRD-Led Context Engineering** | Existing open methodology and repository | Available now, subject to claim verification |
| Future application | **RFP response** | A future workflow/method pack for professional-services proposals | Planned research; not available now |

Recommended first public reference:

> **The Product Model — the next generation of PRD-Led Context Engineering.**

Do not rename repositories, packages, commands, or the organization from this brief. Naming remains a product decision. In code and metadata, keep `product_generation: 2` distinct from repository, template, plugin, and package versions; the current project already has unrelated `2.x` and `3.x` version numbers.

## 3. Source basis and authority

The coding agent must read the target site's local instructions and source before changing it. Treat the following as the content basis for this redesign:

- The committed [V2 implementation blueprint](MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md), version 2.1, fingerprinted in this document's frontmatter.
- The canonical [PRD-CE repository](https://github.com/mattgierhart/PRD-driven-context-engineering) and its [immutable source commit for this brief](https://github.com/mattgierhart/PRD-driven-context-engineering/tree/30ed1b07c9945fc66a18d03fdf5bb870293bee3f).
- The current [GearHeartAI.org site](https://www.gearheartai.org/).
- The current [Impeccable homepage](https://impeccable.style/), [design workflow](https://impeccable.style/designing/), [documentation](https://impeccable.style/docs/), and [getting-started tutorial](https://impeccable.style/tutorials/getting-started/).

This brief is self-contained for the website scope. If the committed research blueprint is not present in the site repository, do not invent missing detail or block the redesign; use this brief's capability statuses, copy boundaries, and acceptance criteria. Do not link a public site to a machine-local file path. Publish this brief or a later canonical V2 direction artifact at a stable commit URL before using it as public evidence.

Authority rules:

1. PRD-CE remains the canonical methodology source. GearHeartAI.org is a presentation and distribution surface, not a competing Source of Truth.
2. The research blueprint is proposed V2 direction, not proof that its features ship.
3. Website copy must resolve from a small, explicit capability-status model. Each public capability record must include `status`, `sourceUrl`, `sourceCommitOrRelease`, and `verifiedAt`; validation must reject factual claims whose provenance is missing or stale under the site's policy. Do not duplicate changing counts or release claims across components.
4. Never invent customers, testimonials, adoption metrics, benchmarks, installation commands, working integrations, or product screenshots.
5. Every factual product claim must link to a current artifact, release, demo, or repository source. Clearly labeled illustrative fixture data is exempt because it is not a product claim, but it must never be mixed with real evidence.

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
| V2 `/product` interface, generated SQLite index, graph JSON, Change Set runtime, and V2 MCP | **In development / proposed** | Demo may show the intended interaction only if clearly labeled “V2 preview” or “illustrative” |
| Hosted graph, continuous sync, Cloud, method-pack registry/marketplace, enterprise governance, portfolio analytics | **Roadmap** | No “Get started,” pricing, or availability claims |
| RFP response method | **Future use case** | Present as a future application of the kernel, not a waitlist or product unless one actually exists |

Use plain labels such as `Available now`, `Prototype`, `V2 preview`, `Concept`, and `Roadmap`. Do not use ambiguous labels such as `New`, `Live`, or `Coming soon` without a defined release target.

## 5. Audience and jobs to be done

### Primary audience

Product and engineering leaders responsible for a long-lived product that is increasingly built with multiple AI agents. They have durable decisions spread across PRDs, tickets, code, tests, chats, and individual memory. They want agents to work from current context without re-briefing or silent invention.

### Secondary audiences

- Solo builders who have outgrown one-shot prompting.
- Teams in regulated or dependency-heavy domains that need provenance and change history.
- Consultancies that transfer product knowledge across people, clients, and delivery phases.
- Framework and agent-tooling contributors evaluating an open, local-first foundation.

### Core jobs

1. Tell me what the product currently believes.
2. Show me why that belief exists and where it came from.
3. Show me what contradicts it or has become stale.
4. Show me what code, tests, and user experience depend on it.
5. Help me propose and review a change without erasing history.
6. Give the next human or agent only the context needed for the work at hand.

The homepage should serve these jobs before teaching ontology or lifecycle stages.

## 6. Release scope for the website

### Required in this implementation

- A redesigned homepage with an outcome-led hero and a visible product proof interaction.
- A short explanation of the Product Model loop: Explore → Shape → Decide → Build → Learn, with Check as a cross-cutting action.
- A clear comparison of current knowledge, proposed change, and observed reality.
- A truthful current/preview/roadmap capability presentation.
- A product-engineering use case and a clearly marked future RFP use case.
- Working links to verified documentation, source, and contact surfaces.
- Responsive, accessible, reduced-motion, and no-JavaScript fallbacks for essential content.
- SEO and social metadata aligned to the new promise.
- Automated content, accessibility, performance, and visual checks proportionate to the existing stack.

### Preserve

- The GearHeart AI name and existing logo unless the user separately approves a brand change.
- Working privacy, terms, contact, newsletter, and analytics behavior. If a surface cannot be verified, retain it unchanged or remove the new call-to-action rather than simulate success.
- The current technical stack, routing model, package manager, deployment path, and component conventions unless a change is necessary and justified.

### Do not build in this pass

- A real graph database, V2 query backend, authentication, user accounts, cloud dashboard, marketplace, pricing system, or RFP workflow.
- A general node-link graph canvas.
- Fake terminal output presented as a live system.
- Empty navigation destinations.
- A clone of Impeccable's site, assets, layout, command names, dark/gold identity, or motion choreography.
- A second editable copy of PRD-CE product facts inside arbitrary components.

## 7. Recommended information architecture

Keep the first release intentionally shallow. If the current site is a single-page application, these may be anchored sections rather than new routes.

### Primary navigation

1. **Product Model** — scrolls to or opens the product explanation.
2. **How it works** — the loop and proof interaction.
3. **Use cases** — current product-engineering methodology plus its V2 direction; RFP marked future.
4. **Docs** — verified documentation destination.
5. **GitHub** — canonical repository.

Keep one strong header action. Before V2 installation is verified, use **Explore the methodology** or **View on GitHub**, not **Install V2**.

### Future navigation, not required now

- Demo / Explorer
- Failure Modes
- Research
- Changelog
- Registry
- Integrations
- Cloud

Add these only when each destination contains real, maintained content. The first four are natural next expansions. Registry, Integrations, and Cloud are roadmap surfaces.

## 8. Homepage narrative and content contract

### Section 1 — Hero: outcome plus proof

**Headline**

> Your product should remember.

**Recommended subhead**

> GearHeart AI is building a living Product Model that connects what your team learns, decides, builds, and observes—so every human and agent can ask what is current, why it is true, and what should change next.

**Actions**

- Primary: **Explore the Product Model** → scroll to the proof interaction.
- Secondary: **View PRD-CE on GitHub** → verified repository URL.
- Nearby status text, not a decorative hero pill: **V2 is in development. The current open methodology is available today.**

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

### Section 3 — The product loop

Render the loop as five user verbs, with Check visibly crossing the sequence:

1. **Explore** — gather evidence and surface uncertainty.
2. **Shape** — turn evidence into a coherent proposed change.
3. **Decide** — accept, reject, revise, deprecate, or supersede with rationale.
4. **Build** — compile relevant context, implement, trace, and verify.
5. **Learn** — compare intent with customer and operational reality.
6. **Check** — detect conflicts, stale assumptions, missing evidence, and drift at every stage.

Avoid presenting the current ten lifecycle stages or dozens of skills as the primary navigation. They remain valuable playbooks behind the simpler surface.

### Section 4 — The differentiator: adjudication

Continue the hero's illustrative fixture as one small semantic-change specimen:

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
- **Complete without cloud** — local files and history remain usable and exportable offline; hosted services are optional projections and collaboration layers.
- **Durable addresses** — typed IDs keep decisions, journeys, contracts, evidence, code, and tests referable.
- **History without erasure** — rejected and superseded meaning remains available.
- **Derived speed** — query indexes and views can be rebuilt from the canonical files.

Do not lead this section with database brands or a file tree.

### Section 6 — One public surface

Show the proposed interaction model as conceptual cards, not a runnable terminal. Do not provide a shell prompt, copy control, or autocomplete treatment. Every card must carry the visible status `V2 proposed — not yet installable`:

| Conceptual interaction | Intended role | Status |
|---|---|---|
| `/product` | Ask, route, explain | V2 proposed — not yet installable |
| `/product init` | Scan and establish a proposed baseline | V2 proposed — not yet installable |
| `/product check` | Find conflicts, staleness, gaps, and drift | V2 proposed — not yet installable |
| `/product decide` | Review a material change | V2 proposed — not yet installable |

Then show the broader V2 loop (`explore`, `shape`, `build`, `learn`) as the planned command family. Do not provide a copyable install command until a released executable has been verified from a clean environment.

### Section 7 — Use cases and the GearHeart seam

**Product Engineering — current methodology available; Product Model V2 in development**

Connect evidence, product decisions, requirements, architecture, code, tests, telemetry, and feedback so product work compounds rather than resets.

**Professional-services RFP response — future application**

The same underlying ideas could connect RFP requirements, approved claims, source evidence, compliance responses, case studies, reviewers, and answer history. Label this card **Future method under research**. Do not create a route, CTA, waitlist, or availability date unless there is a maintained artifact and owner-approved plan.

The visual architecture should make it easy to add future GearHeart methods without implying that every method uses the public `/product` vocabulary.

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

### Product mode by surface

Use Impeccable's surface-awareness as a working discipline:

- Homepage: **Persuade** — earn attention through a strong argument and visible proof.
- Product explanation and research: **Read** — optimize comprehension, measure, hierarchy, and citations.
- Interactive Product Model specimen: **Operate** — make state, actions, and consequences immediately legible.
- Case studies or artifacts: **Experience** — let the work lead while interface chrome recedes.

These are design modes for the coding process, not public GearHeart terminology.

### GearHeart-specific concept

Create an original visual system around **the living record**: evidence, decisions, and implementation forming a durable, inspectable thread through time.

Recommended characteristics:

- Preserve the GearHeart mark and its mint signal color, but increase contrast and give the brand a more decisive secondary accent derived during design exploration.
- Use off-white and ink surfaces with intentional dark sections rather than a direct black/gold Impeccable imitation.
- Pair a distinctive, readable display face with a disciplined sans-serif and a restrained mono face for IDs, states, and source references.
- Prefer fine keylines, source annotations, semantic diffs, temporal tracks, and connected record specimens over decorative node clouds.
- Use square or modest radii where the existing system permits. Avoid pill saturation, cards nested inside cards, generic gradient glows, oversized empty heroes, and icon tiles above every heading.
- Use real interface/state specimens as the primary imagery. Decorative imagery must support the product thesis and must not masquerade as product UI.
- Keep copy measure tight and contrast strong. The current site becomes visually empty during parts of its long scroll narrative; shorten dead space and let each viewport carry an idea or proof.

### Motion language

Motion should explain state change:

- Evidence enters.
- A contradiction becomes visible.
- A proposed change shows its impact.
- A human decision changes current state.
- Prior state moves into history without disappearing.

Avoid continuous ambient animation, scroll capture, long black transition zones, parallax that delays reading, and motion that makes the page feel like a product demo without providing inspectable information. Respect `prefers-reduced-motion`; the reduced-motion version must preserve meaning and hierarchy.

## 10. Required Impeccable workflow in the site repository

Use Impeccable as the design and quality workflow, not as a visual template.

1. Read the site repository's governing instructions, current content model, routes, dependencies, components, analytics, and deployment configuration.
2. Check whether Impeccable is already installed and whether `PRODUCT.md` or `DESIGN.md` exists. Do not overwrite human-authored context.
3. If installation is absent and external installation is authorized, follow the current [official setup guide](https://impeccable.style/tutorials/getting-started/) rather than copying a possibly stale command from this brief. If installation is not authorized, stop and request approval; do not substitute an improvised design workflow while claiming Impeccable was used.
4. Run `/impeccable init` or its current equivalent. Let it inspect the repository first; correct its product interpretation before design work.
5. Run `document` or its current equivalent to capture or refresh `DESIGN.md` from the existing brand and components. Preserve valid GearHeart decisions; explicitly record anti-references, including “do not clone Impeccable's black/gold visual identity.”
6. Run [`/impeccable shape`](https://impeccable.style/docs/shape/) for the homepage. Shape produces the discovery brief; review and approve that brief before requesting a redesign.
7. Invoke Impeccable's current [plain-language new-work flow](https://impeccable.style/docs/new-work/) for the approved homepage brief. Treat visual-direction approval and high-fidelity comp approval as two separate human gates before code is built.
8. Implement the approved comp within the existing stack and component conventions.
9. Use critique before polish. Resolve the highest-impact hierarchy, clarity, persona, and automated findings first.
10. Run focused polish, audit, and hardening passes on the hero, proof interaction, navigation, capability-status presentation, use cases, and final CTA.
11. Run the deterministic detector in CI or locally using the current documented CLI. Record intentional exceptions with rationale rather than weakening rules globally.

Human approval is required at these boundaries:

- Before selecting the new visual direction, before accepting the high-fidelity comp, and before changing the logo/brand identity.
- Publishing new product names, install commands, availability claims, customer proof, pricing, or dates.
- Adding a new dependency with material bundle, security, or maintenance cost.
- Deploying the redesign to production.

## 11. Sustainable implementation guidance

- Reuse the existing framework and design primitives. Do not rewrite the site or upgrade its framework merely to achieve the redesign.
- Store status-sensitive product copy and destinations in one schema-validated content module or content file. Components should render it; they should not each own a copy.
- Keep illustrative Product Model records in a clearly named fixture. The same fixture should feed the visual demo and tests.
- Build the proof interaction as deterministic, local presentation state for this release. Do not introduce a backend for a preview.
- Use semantic component boundaries based on user meaning, such as `ProductAnswer`, `ChangePreview`, `CapabilityStatus`, `ProductLoop`, and `UseCase`, without creating a generic design-system abstraction for one-off sections.
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

The hero proof interaction should follow the headline on narrow screens rather than shrinking into illegibility. Semantic diffs should wrap by field and retain status labels. The product loop may become a vertical sequence on mobile. Do not hide critical evidence, status, or roadmap labels at smaller breakpoints.

## 14. SEO and sharing

Recommended pre-release defaults, subject to final naming approval:

- **Title:** `GearHeart AI | PRD-Led Context Engineering`
- **Description:** `Explore an open, local-first methodology for durable product memory—and preview the next Product Model experience for humans and AI agents.`
- **Primary phrase:** `AI product memory`
- **Supporting phrases:** `context engineering`, `AI-native product development`, `PRD-Led Context Engineering`, `product knowledge graph`

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
| `use_case_view` | Visitor examines Product Engineering or future RFP context |

Do not collect the content of arbitrary visitor questions. The first release should not offer free-form query input.

Success signals for the redesign:

- A first-time visitor can explain the core product outcome after the hero and proof interaction.
- The visitor can distinguish what is available now from V2 preview and roadmap.
- The primary CTA reaches a real next step.
- Product Model interaction use and repository/adoption clicks can be measured without invasive tracking.

## 16. Verification and acceptance criteria

### Content and truth

- [ ] The site uses the approved naming stack consistently.
- [ ] Every capability has one explicit status sourced from the central content model.
- [ ] Every factual capability record has `sourceUrl`, `sourceCommitOrRelease`, and `verifiedAt`; the build fails closed when required provenance is missing.
- [ ] No unverified install command, feature count, integration, customer, metric, testimonial, or release date appears.
- [ ] RFP response is visibly future scope.
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
- [ ] Impeccable critique, polish, audit, harden, and deterministic detection have been run on the finished scope.
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
3. Initialize or refresh Impeccable context without overwriting trusted human decisions. If Impeccable is absent and installation is not authorized, stop and request approval.
4. Produce a concise homepage shape brief. Stop for owner approval of the brief and naming.
5. Run the approved brief through the current new-work flow. Stop separately for owner approval of the visual direction, then the high-fidelity comp.
6. Implement the approved homepage comp with the deterministic Product Model preview fixture.
7. Run content, design, accessibility, responsive, performance, and engineering checks.
8. Provide a preview URL or local review path plus screenshots at the required widths.
9. Report changed files, verified claims, remaining roadmap-only content, test results, and any intentional design-rule exceptions.
10. Wait for explicit approval before production deployment.

## 18. Owner decisions before public release

Recommended defaults authorize discovery and preparation of a reviewable shape brief. They do not authorize bypassing the direction and comp approval gates, publishing changed product claims, or deploying to production.

| Decision | Recommended default |
|---|---|
| Public flagship name | **The Product Model** with transition label **PRD-CE V2** |
| Hero promise | **Your product should remember.** |
| Pre-release primary CTA | **Explore the Product Model** → deterministic preview |
| Pre-release secondary CTA | **View PRD-CE on GitHub** |
| V2 availability language | **In development** |
| RFP language | **Future method under research** |
| Brand direction | Evolve the existing GearHeart identity; do not imitate Impeccable's identity |
| Production release | Preview and explicit owner approval required |

## 19. Brief completion definition

The update is successful when GearHeartAI.org feels as productized and demonstrative as Impeccable without resembling it: one clear promise, one visible proof, one coherent vocabulary, one honest next step, and deeper rigor available on demand.

The site should make V2 desirable while remaining precise about what exists today.
