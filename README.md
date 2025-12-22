# PRD-Driven Context Engineering (Gear Heart Methodology)

> **Philosophy**: Fix "Context Drift" by treating Documentation as Code.

---

## 1. The Problem: "Context Drift"

In modern AI-assisted development, a critical failure mode exists:

1.  **The Spark**: A founder has a clear vision.
2.  **The Hand-off**: They explain it to an AI (or human dev).
3.  **The Drift**: As complexity grows, the "Context Window" fills up. Old instructions are dropped.
4.  **The Hallucination**: The AI starts inventing logic because it lost the original requirements.
5.  **The Spaghetti**: You end up with code that "works" but doesn't solve the business problem.

## 2. The Solution: "Documentation as Context"

We do not use documentation for humans to read once and forget. We use documentation as **Anchors for AI Agents**.

### The 3+1+Specs Framework

To solve drift, we structure the repo so an AI can _always_ re-ground itself in < 60 seconds.

| Component | Purpose |
|Dist|---|
| **1. Navigation** | `README` (Status) + `ROADMAP` (Time) + `CLAUDE` (Rules). |
| **2. Strategy** | `PRD.md`. The "Why". It evolves from v0.1 (Idea) to v1.0 (Scale). |
| **3. Execution** | `epics/`. The "What". Broken into **Context Windows** (safe token limits). |
| **Specs** | `specs/`. The "Truth". ID-based rules (`BR-001`, `UJ-010`) that never change unless explicitly edited. |

## 3. How to Use This Repo

### A. Fork & Initialize

1.  **Fork** this repository.
2.  **Rename**: `README_template.md` -> `README.md` (This becomes your project dashboard).
3.  **Clean**: Delete this philosophy README if you wish, or keep it as `METHODOLOGY.md`.

### B. The Workflow

1.  **Start a Session**: The Agent reads `README` -> `PRD` -> `CLAUDE`.
2.  **Plan**: The Agent creates an EPIC in `epics/` using `EPIC_TEMPLATE.md`.
3.  **Execute (Context Window)**: The Agent builds _one feature set_ (Sprint), then stops to validate.
4.  **Trace**: The Agent tags code with IDs (`// @implements BR-101`).
5.  **Harvest**: Before closing the Epic, the Agent updates `specs/` with new truths.

### C. The Golden Rule

> **"If it's not in the Specs, it doesn't exist."**
> Code is transient. The PRD and Specs are durable.

---

## Repository Structure

```text
/
├── README.md               # Your Project Dashboard (rename from README_template.md)
├── ROADMAP.md              # Release Phases (Beta -> MVP -> V1)
├── PRD.md                  # The Product Strategy
├── CLAUDE.md               # The AI Instructions
├── epics/                  # Active Work (Context Windows)
├── specs/                  # Source of Truth (BR, UJ, API)
├── agents/                 # AI Roster & Tools
└── archive/                # History
```
