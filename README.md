# Context Engineering: Memory as Infrastructure

> **Purpose**: "Context Engineering" is a macro-philosophy for the next evolution of software development. It posits that as we move from human-only teams to hybrid AI-Human teams, **Memory must become Infrastructure**.
>
> This repository is one expression of that philosophy: a blueprint for taking SaaS products from **Zero to One** with maximum velocity. But the principles here—treating documentation as a living, automated knowledge graph—apply to any stage of software evolution, from refactoring legacy code to managing mature platforms.

See this philosophy in action at **[GearheartAI.org](https://gearheartai.org)**.

---

## The Evolution

To understand where we are going, we must state where we have been.

- **Start-up / Waterfall** was the era of **Static Memory**. We wrote everything down upfront. It gave us certainty, but it killed our ability to react.
- **Agile** was the era of **Fragmented Memory**. We broke work into sprints to move faster, accepting that truth changes. But we scattered our knowledge across tickets, wikis, and chats. We gained speed but lost the "Big Picture."
- **Context Engineering** is the era of **Shared Memory**. It acknowledges that **AI is now a team member**, not just a tool. This requires a living system where documentation keeps pace with code, acting as the rigorous interface between Human and AI.

---

## The Cognitive Shift

We are not just changing tools; we are changing how we measure our work.

| Traditional Agile      | Context Engineering     | The Shift (Automation & Infrastructure)                                                    |
| :--------------------- | :---------------------- | :----------------------------------------------------------------------------------------- |
| **Sprints**            | **Context Windows**     | We don't time-box based on dates; we _scope-box_ based on cognitive capacity.              |
| **User Stories**       | **Prompts**             | We don't write descriptions; we engineer _prompts_ that deterministically load context.    |
| **Tribal Knowledge**   | **Source of Truth**     | If it isn't in the Knowledge Graph (`specs/`), it doesn't exist.                           |
| **Standups**           | **Documentation Hooks** | We don't have status meetings. Event-based hooks auto-update the memory when work happens. |
| **Project Management** | **Context Governance**  | We don't task-manage people. The system gates execution until context is verified valid.   |

---

## The Manifesto

I am building something complex.

As a human, I have a limit. My "cognitive load" can only hold so much state before I start forgetting edge cases or introducing bugs.
My AI partner has a limit, too. Its "context window" is vast but finite; freely dumping information into it leads to hallucination and logical drift.

When we try to collaborate—Human to Human, or Human to AI—these limits compound. We miscommunicate. We overwrite each other's assumptions. The context drifts.

### Memory as Infrastructure

This philosophy is born from two distinct experiences.

**First, Leading Human Teams:**
Before AI, I led software teams where success always followed a pattern: when we rallied around a single **"Hero Artifact"**—a clear, compelling mission document—alignment was automatic. The team moved as one because the shared memory was cemented in that artifact. Without it, even the best talent drifted into chaos.

**Second, Partnering with AI:**
When I began coding with AI, I noticed a similar pattern. Sometimes the AI amazed me with its brilliance; other times, it was disappointingly dense. I realized the variable wasn't the model's intelligence—it was the **Context Density** I provided. When the context was rich and structured, the AI performed like a senior engineer. When it was vague, the AI hallucinated.

**Context Engineering is the convergence of these truths.**

In this repository, documentation is not a chore I do at the end. **Documentation is the infrastructure of our shared memory.** It is the digital "Hero Artifact" that keeps both Human and AI aligned.

> **The Golden Rule**: If it isn't part of the memory infrastructure, it isn't true.

When I define a User Journey and give it an ID (`UJ-101`), I am creating a node in our shared **Knowledge Graph**. I am offloading that complexity from my brain into the file system.
When the AI references `BR-004`, it is not guessing; it is retrieving a specific, immutable memory that I encoded.

We treat our Specs (`specs/SoT.*.md`) as the **External Brain** of the product.

- The **AI** reads the specs to understand constraints without needing infinite context.
- **I** read the specs to remember what we decided last week.
- **We** meet in the code, confident that we are building the same thing.

### The Artifacts of Collaboration

This approach changes the "First Person" experience of coding:

1.  **I don't just write code; I design context.** I create the navigation paths (`README`, `PRD`, `CLAUDE.md`) that allow my AI partner to onboard itself in seconds.
2.  **We don't rely on tribal knowledge.** If it's not in the Source of Truth (`specs/`), it doesn't exist. This ruthlessness frees us. We don't have to remember "that one conversation in Slack." We only have to trust the repo.
3.  **We build complexity through references.** By linking small, testable units (`IDs`) together, we can build massive systems without ever needing to load the entire blueprint into our working memory at once.
4.  **We optimize Context Density.** We navigate memory to deliver the perfect balance of information. **Too dense**, and the AI over-analyzes. **Too sparse**, and it drifts. We use the hierarchy to read exactly what is needed—no more, no less.

We embrace this structure not because we love bureaucracy, but because we love **flow**. By engineering our context, we transcend our individual limits and build software that is smarter than any one of us.

---

## The Documentation Ecosystem: 3+1+SoT+Temp

To make this memory infrastructure practical, we use a strict hierarchy designed to **manage Context Density**. This structure ensures that neither human cognitive load nor AI context windows are ever overwhelmed.

### 1. The Instincts Layer (L0)

- `README.md`: The Dashboard. The status, TOC, and "instincts" of the project (where am I? what is active?).
- `PRD.md`: The Strategy. The "Why" and "What" of the product.
- `CLAUDE.md`: The Physics. The rules of how the AI must behave.

### 2. The Execution Layer (Active Memory)

- `epics/`: The work in progress. This is the only "variable" state. An Epic frames a specific problem (Context Window) so we can solve it without distraction.

### 3. The Source of Truth (Long-Term Memory)

- `specs/SoT.*.md`: The immutable facts.

  - **Business Rules (`BR-xxx`)**: Hard constraints.
  - **User Journeys (`UJ-xxx`)**: Critical paths.
  - **Data Contracts (`API-xxx`)**: Interfaces.

    This is the "External Brain." We duplicate nothing here. We reference everything via **Unique IDs**.

    > **Just-in-Time Context**: Unique IDs allow us to pull _only_ what is needed for an active task. Instead of dumping the entire documentation into the context window, we reference specific IDs (`UJ-101`, `API-002`). This reduces input tokens while maintaining deep, specific understanding.

### 4. The Temp Layer (Scratchpad)

- `temp/`: The workspace for **Audits, Explorations, Tech Debt Analysis, and Concepting**.
  - **Naming Convention**: Files must be associated with the Active Epic (e.g., `temp/EPIC-05_audit_log.md` or `temp/EPIC-05_tech_debt.md`).
  - **Rule**: We **Archive** these files when the associated Epic is marked complete. This preserves the context and logic that led to the final implementation.

---

## The Progressive PRD

The most critical mistake in AI-assisted development is the "One-Shot"—asking the AI to build the entire app at once. This leads to generic code, hallucinations, and rapid context drift.

Instead, we use a **Progressive PRD**.

The `PRD.md` is not just a document; it is a **Gated Workflow**. We force the AI to focus on one section at a time (e.g., "Strategy", then "User Journeys", then "Data Model").

1.  **Anti-One-Shot**: By constraining the context window to a single phase, we prevent the AI from "guessing" the architecture before it understands the user needs.
2.  **ID Rigor**: Deep focus allows us to generate meaningful IDs (`UJ-xxx`, `BR-xxx`) without overwhelming the system. These IDs become the anchors for all future code.
3.  **Desirability**: The result is not just a working product, but a _desirable_ one, built with the thoughtfulness of a handcrafted system and the speed of an automated one.

### The PRD Lifecycle (v0.1 to v1.0)

We do not proceed to the next stage until the **Definition of Done (DoD)** is met.

| Version  | Name             | Focus               | Definition of Done (DoD)                                           |
| :------- | :--------------- | :------------------ | :----------------------------------------------------------------- |
| **v0.1** | **Spark**        | Problem & Outcomes  | Problem defined, Outcomes measurable, Open Questions list.         |
| **v0.2** | **Market**       | Segments & ICP      | Segments sized, "Not For" defined, Business Rules (`BR-`) created. |
| **v0.3** | **Commercial**   | Value & Pricing     | Competitors profiled, Pricing model, Monetization rules.           |
| **v0.4** | **Journeys**     | Personas & Flows    | Core journeys mapped (`UJ-`), Dependencies (`API-`) noted.         |
| **v0.5** | **Red Team**     | Risks & Feasibility | Risks (Market/Tech) identified, Mitigations linked to tests.       |
| **v0.6** | **Architecture** | Technical Strategy  | Stack selected, API contracts (`API-`) drafted, Cost guardrails.   |
| **v0.7** | **Build**        | Implementation Loop | Code tested (`TEST-`), SoT updated, Epic loop execution.           |
| **v0.8** | **Release**      | Deployment & Ops    | Runbooks (`RUN-`), Monitoring (`MON-`), Rollback plan.             |
| **v0.9** | **Launch**       | Go-to-Market        | Launch metrics (`KPI-`), Feedback channels (`CFD-`) active.        |
| **v1.0** | **Growth**       | Market Adoption     | Paying customers, Retention analysis, Optimization loop.           |

### The Iterative Ecosystem

While the **PRD Lifecycle** is gated to ensure discipline, the **Documentation Ecosystem** allows for constant flexibility.

> **The Paradox**: Gates provide focus; The Ecosystem provides agility.

Because our documentation is modular and interlocked via Hooks, we can revisit any section "Just-in-Time." If customer feedback changes the **Strategy** during the **Build** phase, we don't restart the waterfall. We simply:

1.  Open a context window for `PRD.md` (Strategy Section).
2.  Update the `BR-xxx` rules.
3.  Let the **Automation Hooks** propagate distinct changes to the active `epics/`.

This allows the product to evolve continuously without losing the rigorous structure that keeps the AI on track.

---

## Repository Structure

```text
/
├── README.md               # The Instincts (Dashboard & Status)
├── PRD.md                  # The Strategic Source of Truth
├── CLAUDE.md               # The Agent's Operating Instructions
├── epics/                  # Active Context Windows (Tasks)
├── specs/                  # The External Brain (SoT.* files)
├── agents/                 # AI Team Definitions
└── archive/                # Completed memories
```
