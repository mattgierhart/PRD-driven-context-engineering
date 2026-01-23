# PRD-Led Context Engineering: Memory as Infrastructure

*Documentation is no longer a record of what was built; it is the infrastructure through which we build.*

---

## Table of Contents

- [Quick Start](#quick-start)
- [The Perspective: The Memory Gap](#the-perspective-the-memory-gap)
- [1. Infrastructure of Thought](#1-infrastructure-of-thought)
- [2. The Cognitive Stack](#2-the-cognitive-stack)
  - [Executive Functions (The Instincts)](#executive-functions-the-instincts)
  - [Long-Term Memory (The Anchors)](#long-term-memory-the-anchors)
  - [Working Memory (The Epic)](#working-memory-the-epic)
  - [Short-Term Memory (The Scratchpad)](#short-term-memory-the-scratchpad)
- [3. Pattern Memory: The Role of Agentic Agents](#3-pattern-memory-the-role-of-agentic-agents)
- [4. Principles of the System](#4-principles-of-the-system)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)

---

## Quick Start

1. **Fork this Repository**: Establish your project's cognitive foundation.
2. **Initialize the Dashboard**: Copy [`README_template.md`](README_template.md) to `README.md` and define your project's "Instincts."
3. **Select Your Agent**: This system was built mostly around Anthropic's capabilities (skills, hooks, etc.) but can be used with Gemini, CODEX or Claude Code. Configure [`.claude/`](.claude/) (or your preferred agent directory) to align the AI with your project's physics.

---

## The Perspective: The Memory Gap

Having led hyper-growth startups, enterprise "squads of squads," and launched five products as a solo developer, I've seen where development breaks. It is rarely a failure of talent; it is a failure of memory.

| Approach | Memory Model | The Problem |
|:---------|:-------------|:------------|
| **Waterfall** | Static Memory | Creates a "requirements trap" where we front-load certainty, making change slow and expensive. |
| **Agile** | Fragmented Memory | Knowledge is scattered across tickets and ceremonies, eventually dying in "Definition of Done" checklists that no one reads. |

**In the AI era, these gaps become fatal.** Without a shared history, AI agents guess. PRD-Led Context Engineering replaces tribal knowledge with a **Shared Knowledge Graph**—a living system of memory that both humans and AI use to navigate the product lifecycle with senior-level precision. In this system, documentation is the **Memory Bus** of the project. This manifests in key principles:

### The Golden Rule

> **If a decision is not part of the memory infrastructure, it does not exist.**

### Relative Context Density

> **We do not optimize for *more* context; we optimize for *density*. Too much context and the AI loses focus, attempting to solve the world; too little, and it drifts into hallucination. We engineer the "Goldilocks zone" of information.**

---

## 1. The Cognitive Stack

We organize the repository to reflect how intelligence functions. This hierarchy ensures that every participant operates with the correct level of focus.

### Executive Functions (The Instincts)

| File | Purpose |
|:-----|:--------|
| [`README.md`](README.md) | **The Dashboard.** Current status, priorities, and project instincts. |
| [`PRD.md`](PRD.md) | **The Progressive Strategy.** A gated document that defines the "Why" and "What." It evolves in place from v0.1 (Spark) to v1.0 (Growth). v0.7 (Build) includes deployment configuration — environment setup, CI/CD pipelines, and secrets management. For this lifecycle I've built my 20 years as a product manager into [25 skills](.claude/skills/skills-inventory.md) that guide the PRD progress into building market-ready products. |
| [`CLAUDE.md`](CLAUDE.md) | **The Physics.** The non-negotiable rules of behavior and technical standards. |

### Long-Term Memory (The Anchors)

| Directory | Purpose |
|:----------|:--------|
| [`SoT/`](SoT/) | **The Source of Truth.** This holds immutable facts: [Business Rules (`BR-`)](SoT/SoT.BUSINESS_RULES.md), [User Journeys (`UJ-`)](SoT/SoT.USER_JOURNEYS.md), [Data Contracts (`API-`)](SoT/SoT.API_CONTRACTS.md), [Technical Decisions (`TECH-`, `ARC-`, `ENV-`)](SoT/SoT.TECHNICAL_DECISIONS.md), [Deployment (`DEP-`, `SEC-`, `MON-`)](SoT/SoT.DEPLOYMENT.md), and other key decisions as easy-to-reference anchors that prevent model drift. |

See the complete [SoT Index](SoT/SoT.README.md) and [Unique ID System](SoT/SoT.UNIQUE_ID_SYSTEM.md) for details.

### Working Memory (The Epic)

| Directory | Purpose |
|:----------|:--------|
| [`epics/`](epics/) | **Where execution lives.** An Epic is not just a task; it is a **Context Window**. It frames a specific problem, pulling in only the necessary IDs from the SoT to solve a requirement without distracting the AI with the entire codebase. |

See the [Epic Template](epics/EPIC_TEMPLATE.md) and [Epic README](epics/README.md) for guidance.

### Short-Term Memory (The Scratchpad)

| Directory | Purpose |
|:----------|:--------|
| [`temp/`](temp/) | **The workspace** for audits, technical debt analysis, and research. This memory is ephemeral; its reference structure keeps the context window clean. |

---

## 2. Pattern Memory: The Role of Agentic Agents

We often mistake an agent's "role" for its "instructions." In this system, **Identity is Memory**. Agents are better thought of as **Rooms** where work is captured as sticky notes on the wall, artifacts created, and patterns documented. An agent's effectiveness is determined by the **Pattern Memory** it accumulates within its room:

| Component | What It Represents |
|:----------|:-------------------|
| **Agent Responsibilities** | The Unique IDs (`BR-`, `API-`) they are responsible for maintaining. |
| **Status Log** | The active Working Memory (Epic) currently under review and its point of view for how to collaborate with other agents. |
| **Patterns** | The "learned wisdom" of the project—decisions on why we chose one architecture over another, previous friction points, and successful implementation patterns. |

### The Four Agents

| Agent | Room | Description |
|:------|:-------|:------------|
| [`HORIZON`](.claude/agents/HORIZON.md) | Market War Room | Product vision and market alignment |
| [`STUDIO`](.claude/agents/STUDIO.md) | Design Studio | User experience and interface design |
| [`DEVLAB`](.claude/agents/DEVLAB.md) | Development Garage | Code, architecture, and technical execution |
| [`METRO`](.claude/agents/METRO.md) | GTM Command Center | Deployment, monitoring, and reliability |

**Handoffs are no longer task assignments; they are Context Transfers.** You are walking a partner into a room where the memory is already prepared for them on the walls and in the diary.

---

## 3. Principles of the System

| Principle | Description |
|:----------|:------------|
| **Unique IDs as Nodes** | Using `BR-101` or `UJ-202` turns flat files into a queryable **Knowledge Graph**. It allows for deterministic retrieval instead of probabilistic guessing. |
| **Just-in-Time Context** | We use those IDs to pull only the specific nodes of memory required for a task, maintaining optimal **Context Density**. |
| **Progressive Documentation** | We update in place. As the product matures, the documentation matures with it, ensuring there is only ever one version of the truth. |
| **Gated Workflows** | We verify that the memory (the PRD and SoT) is valid before we allow the system to move from strategy to implementation. |

By engineering the context, we can build complex and iterative software that gives teams a way to navigate their own shared cognitive load and gives AI the right context to focus.

---

## Repository Structure

```text
/
├── README.md               # Dashboard, structure, and status
├── PRD.md                  # Product definition (Progressive PRD)
├── CLAUDE.md               # The agent's operating instructions
├── epics/                  # Active Context Windows (Tasks)
│   └── EPIC_TEMPLATE.md    # Template for new epics
├── SoT/                    # Shared Memory Store (SoT.* files)
│   ├── SoT.README.md       # Index of all SoT files
│   ├── SoT.BUSINESS_RULES.md
│   ├── SoT.USER_JOURNEYS.md
│   ├── SoT.API_CONTRACTS.md
│   └── ...
├── temp/                   # Scratch Pad for explorations and audits
└── .claude/                # Agents, tools, skills, and hooks
    ├── agents/             # Agent definitions (HORIZON, STUDIO, DEVLAB, METRO)
    ├── skills/             # PRD lifecycle skills (24 total)
    └── hooks/              # Automation triggers
```

> **Agent Note**: `.claude/` can be replaced with `.gemini/`, `.codex/`, or any other agent structure, but the skills, hooks, custom commands, and agent model here were built with Anthropic's documentation model in mind.

> **Fork Note**: This `README.md` explains the methodology. When you fork this repo for a product, copy [`README_template.md`](README_template.md) to `README.md` and customize it for that product.

---

## Contributing

Thank you for helping us refine the **PRD-Led Context Engineering** methodology. This repository is not just a codebase; it is a living system of **Memory as Infrastructure**. Look me up on LinkedIn or other social channels if you want to connect. I'm happy to hear ideas or if you need help applying it to your product.
