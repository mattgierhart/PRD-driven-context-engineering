# PRD Led Context Engineering: Memory as Infrastructure

> **Purpose**: PRD Led Context Engineering enables product teams to build with AI by turning **shared memory (humans + AI)** into maintained infrastructure. This ensures teams move fast without losing alignment.
>
> This repository is one expression of that system. The principles apply at any stage because documentation becomes a **Knowledge Graph** that humans and AI can query.

See this philosophy in action at **[GearheartAI.org](https://gearheartai.org)**.

---

## The Evolution

The progression of memory in software teams:

- **Start-up / Waterfall** relied on **Static Memory**. We wrote everything down upfront. It created certainty, but made change slow and expensive.
- **Agile** moved faster but created **Fragmented Memory**. We scattered knowledge across tickets, wikis, and chats and lost shared understanding.
- **PRD Led Context Engineering** builds **Shared Memory**. It treats **AI as a team member**, not just a tool, and keeps documentation synchronized with code so humans and AI can navigate the same truth.

---

## The Cognitive Shift

We are changing how we measure work, not just tools.

| Traditional Agile      | PRD Led Context Engineering        | The Shift (Automation & Infrastructure)                                                                |
| :--------------------- | :--------------------------------- | :----------------------------------------------------------------------------------------------------- |
| **Sprints**            | **Context Windows**                | We don't time-box based on dates; we _scope-box_ based on cognitive capacity.                          |
| **User Stories**       | **Prompts**                        | We don't write descriptions; we engineer _prompts_ that deterministically load context.                |
| **Tribal Knowledge**   | **Source of Truth**                | If it isn't in the Knowledge Graph (`SoT/`), it doesn't exist.                                         |
| **Standups**           | **Documentation Hooks (optional)** | We don't have status meetings. Event-based hooks in `.claude/hooks` can update memory when configured. |
| **Project Management** | **Context Governance**             | We don't task-manage people. The system gates execution until context is verified valid.               |

---

## The Manifesto

We are building complex products together.

As humans, we have limits; our cognitive load is finite. Push it too far, and we start forgetting edge cases or introducing bugs.
Our AI partners have limits, too. Their context windows are vast but finite; flooding them leads to hallucination and drift.

When we collaborate—human to human or human to AI—these limits compound. We miscommunicate. We overwrite assumptions. Shared memory drifts.
So we treat team memory as a shared asset across humans and AI, not an individual burden.

### Memory as Infrastructure

This philosophy comes from two experiences.

**First: Leading Human Teams**
Before AI, I led software teams where alignment followed a clear pattern: rally around a single **Source of Truth Artifact**—a mission document—and the team moved as one. Shared memory anchored there. Without it, even great talent drifted.

**Second: Partnering with AI**
When I began coding with AI, I noticed a similar pattern. Sometimes the AI was brilliant; other times it was dense. I realized the variable wasn't the model's intelligence—it was the **Context Density** I provided. When the context was rich and structured, the AI performed at a senior level. When it was vague, it hallucinated.

**PRD Led Context Engineering is the convergence of these truths.**

Here, documentation is not an afterthought. **Documentation is the infrastructure of our shared memory.** The Source of Truth Artifact anchors both humans and AI.

> **The Golden Rule**: If it isn't part of the memory infrastructure, it isn't true.

So how do we introduce team and AI memory into the repo? We do it with **Source of Truth Artifacts (SoT)**—durable documents that turn decisions into shared, queryable memory.
Each SoT entry gets a **Unique ID**. That ID is referenceable and functions as a memory node with **weight and value** because it points to a validated decision, not a suggestion.

When we define a User Journey and give it an ID (`UJ-101`), we create a node in our shared **Knowledge Graph** and offload that complexity from individual brains into the file system.
When the AI references `BR-004`, it is not guessing; it is retrieving a specific, immutable memory we encoded.

**Key Terms**

- **Source of Truth Artifacts**: The clear, anchoring documents that hold a team's shared memory for a product.
- **Context Density**: How much relevant, structured context we deliver per prompt or handoff.
- **Knowledge Graph**: The linked network of IDs (`BR-xxx`, `UJ-xxx`, `API-xxx`) across files that makes memory retrievable for humans and AI.

We treat the `SoT/` files (`SoT.*.md`) as the long-term memory store of the product.

- The **AI** reads the SoT files to understand constraints without needing infinite context.
- **Humans** read the SoT files to remember what we decided last week.
- **We** meet in the code, confident we are building the same thing.

### The Artifacts of Collaboration

This approach changes how teams work:

1.  **We don't just write code; we design context.** We create the navigation paths (`README`, `PRD`, `CLAUDE.md`) so our AI partners onboard quickly.
2.  **We don't rely on tribal knowledge.** If it's not in the Source of Truth (`SoT/`), it doesn't exist. This frees us. We don't have to remember "that one conversation in Slack." We trust the repo.
3.  **We build complexity through references.** By linking small, testable units (`IDs`) together, we can build massive systems without ever needing to load the entire design into our working memory at once.
4.  **We optimize Context Density.** We select context to deliver the right balance of information. **Too dense**, and the AI over-analyzes. **Too sparse**, and it drifts. We use the hierarchy to read exactly what is needed—no more, no less.

This structure preserves alignment and momentum. By engineering context, we build software no single person could hold in their head at once.

---

## The Documentation Ecosystem: 3+1+SoT+Temp

To make memory infrastructure practical, we use an **intentional architecture** designed to **manage Context Density**. This keeps human cognitive load and AI context windows within limits.

### 1. Executive Functions: Building AI's instincts (L0)

This layer orients attention and sets priorities.

- `README.md`: The Dashboard. The status, TOC, and "instincts" of the project (where am I? what is active?).
- `PRD.md`: The Strategy. The "Why" and "What" of the product.
- `CLAUDE.md`: The Physics. The rules of how the AI must behave.

### 2. Focus Memory: The Execution Layer (Active Memory)

- `epics/`: The work in progress. This is the only "variable" state. An Epic frames a specific problem (Context Window) so we can solve it without distraction.

### 3. Long-Term Memory: Source of Truth Artifacts

- `SoT/SoT.*.md`: The immutable facts.

  - **Business Rules (`BR-xxx`)**: Hard constraints.
  - **User Journeys (`UJ-xxx`)**: Critical paths.
  - **Data Contracts (`API-xxx`)**: Interfaces.

    This is the shared memory store. We duplicate nothing here. We reference everything via **Unique IDs**.

    > **Just-in-Time Context**: Unique IDs allow us to pull _only_ what is needed for an active task. Instead of dumping the entire documentation into the context window, we reference specific IDs (`UJ-101`, `API-002`). This reduces input tokens while maintaining deep, specific understanding.

### 4. Short-Term Memory: Scratch Pad

- `temp/`: The workspace for **Audits, Explorations, Tech Debt Analysis, and Concepting**.
  - **Naming Convention**: Files must be associated with the Active Epic (e.g., `temp/EPIC-05_audit_log.md` or `temp/EPIC-05_tech_debt.md`).
  - **Rule**: We **Archive** these files when the associated Epic is marked complete. This preserves the context and logic that led to the final implementation.

---

## The Progressive PRD

A common mistake in AI-assisted development is the "One-Shot"—asking the AI to build the entire app at once. This leads to generic code, hallucinations, and rapid context drift.

Instead, we use a **Progressive PRD**.

`PRD.md` is a **Gated Workflow**, not just a document. We force the AI to focus on one section at a time (e.g., "Strategy", then "User Journeys", then "Data Model").

1.  **Constrained Focus**: By limiting the context window to a single phase, we prevent the AI from "guessing" the architecture before it understands the user needs.
2.  **ID Rigor**: Deep focus allows us to generate meaningful IDs (`UJ-xxx`, `BR-xxx`) without overwhelming the system. These IDs become the anchors for all future code.
3.  **Outcome Quality**: The result is not just a working product, but a _desirable_ one, built with care and speed.

### The PRD Lifecycle (v0.1 to v1.0)

We do not proceed to the next stage until the **Definition of Done (DoD)** is met.

| Version  | Name                     | Focus                 | Definition of Done (DoD)                                           |
| :------- | :----------------------- | :-------------------- | :----------------------------------------------------------------- |
| **v0.1** | **Spark**                | Problem & Outcomes    | Problem defined, Outcomes measurable, Open Questions list.         |
| **v0.2** | **Market Definition**    | Segments & ICP        | Segments sized, "Not For" defined, Business Rules (`BR-`) created. |
| **v0.3** | **Commercial Model**     | Value & Pricing       | Competitors profiled, Pricing model, Monetization rules.           |
| **v0.4** | **User Journeys**        | Personas & Flows      | Core journeys mapped (`UJ-`), Dependencies (`API-`) noted.         |
| **v0.5** | **Red Team Review**      | Risks & Feasibility   | Risks (Market/Tech) identified, Mitigations linked to tests.       |
| **v0.6** | **Architecture**         | Technical Strategy    | Stack selected, API contracts (`API-`) drafted, Cost guardrails.   |
| **v0.7** | **Build Execution**      | Implementation Loop   | Code tested (`TEST-`), SoT updated, Epic loop execution.           |
| **v0.8** | **Release & Deployment** | Operational Readiness | Runbooks (`RUN-`), Monitoring (`MON-`), Rollback plan.             |
| **v0.9** | **Launch**               | Go-to-Market          | Launch metrics (`KPI-`), Feedback channels (`CFD-`) active.        |
| **v1.0** | **Growth**               | Market Adoption       | Paying customers, Retention analysis, Optimization loop.           |

### The Iterative Ecosystem

While the **PRD Lifecycle** is gated for discipline, the **Documentation Ecosystem** allows flexibility.

> **The Paradox**: Gates provide focus; the ecosystem provides agility.

Because our documentation is modular and interlocked via hooks, we can revisit any section just-in-time. If customer feedback changes the **Strategy** during the **Build** phase, we don't restart the plan. We simply:

1.  Open a context window for `PRD.md` (Strategy Section).
2.  Update the `BR-xxx` rules.
3.  If hooks are configured in `.claude/hooks`, use them to propagate changes to the active `epics/`. Otherwise, update the Epic manually.

This allows the product to evolve without losing the structure that keeps humans and AI aligned.

---

## Repository Structure

```text
/
├── README.md               # Dashboard, structure, and status
├── PRD.md                  # Product definition (Progressive PRD)
├── CLAUDE.md               # The agent's operating instructions
├── epics/                  # Active Context Windows (Tasks)
├── SoT/                     # Shared Memory Store (SoT.* files)
├── temp/                    # Scratch Pad for explorations and audits
└── .claude/                 # Agents, tools, skills, and hooks
```

> **Agent Note**: `.claude/` can be replaced with `.gemini/`, `.codex/`, or any other agent structure, but the skills, hooks, custom commands, and agent model here were built with Anthropic's documentation model in mind.

> **Fork Note**: This `README.md` explains the methodology. When you fork this repo for a product, copy `README_template.md` to `README.md` and customize it for that product.

---

## Contributing

Thank you for helping us refine the **PRD Led Context Engineering** methodology. This repository is not just a codebase; it is a living system of **Memory as Infrastructure**.

### Core Philosophy

Before contributing, please read:

1.  **[`README.md`](README.md)**: The "Executive Functions" layer and Project Dashboard.
2.  **[`CLAUDE.md`](CLAUDE.md)**: The Agent Operating Instructions.

Our goal is to optimize **Context Density**: providing the AI (and humans) with exactly the right information at the right time.

### Ways to Contribute

#### 1. Refine the Methodology

- **Templates**: Improve `SoT/` templates or `epics/EPIC_TEMPLATE.md`.
- **Workflows**: Suggest automation hooks or better ways to manage the "Source of Truth".
- **Documentation**: Clarify the "Rules of the Road" in `README.md`.

#### 2. Report Friction

- If you find a "Gate" in the PRD Lifecycle (`README.md#the-prd-lifecycle`) that slows you down without adding value, let us know.
- If the AI struggles to find context, report it as a "Context Leak."

### Getting Started

1.  **Fork & Branch**: Create a branch for your feature or fix.
2.  **Follow the Lifecycle**: Even for meta-changes, we respect the spirit of the **Gated Workflow**.
3.  **Traceability**: If you add a new concept, give it an ID (e.g., `BR-XXX` or `UJ-XXX`) if it's durable.

### Contribution Standards

- **Terminology**: Use "PRD Led Context Engineering", "Source of Truth", and "Epics" consistent with `README.md`.
- **Links**: Always use relative links to files (e.g., `[Link](README.md)`), not absolute paths.
- **Tone**: Professional, prescriptive, and rigorous.

### Questions?

- Open a GitHub Issue for discussion.
- Check `README.md` for the current status of the methodology.
