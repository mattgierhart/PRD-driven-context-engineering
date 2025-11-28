# PRD Instruction Library

This directory organizes workflow instructions that guide each stage of the Product Requirements Document (PRD) lifecycle.

## Structure

- `README.md`: This file. Describes how to navigate the instruction library.
- `vX.Y/`: Versioned subdirectories that capture the instructions required to produce and advance that PRD milestone.

### Strategy Stages (AURA ownership: v0.1–v0.5)
| Stage | Files | Focus |
|-------|-------|-------|
| v0.1 Spark | `aura-intake.md`, `research-agents.md` | Problem statement, initial users |
| v0.2 Market Definition | `aura-intake.md`, `research-agents.md` | Segments, TAM, "Not for" rules |
| v0.3 Commercial Model | `aura-intake.md`, `research-agents.md` | Pricing, competitors, moat |
| v0.4 User Journeys | `aura-intake.md`, `research-agents.md` | Personas, journey mapping |
| v0.5 Red Team Review | `aura-intake.md`, `research-agents.md` | Risk analysis, Gate 1 decision |

### Build Stages (APOLLO ownership: v0.6–v0.7)
| Stage | Files | Focus |
|-------|-------|-------|
| v0.6 Architecture | `aura-intake.md`, `research-agents.md` | Stack selection, Gate 2 decision |
| v0.7 Build Execution | `apollo-intake.md`, `build-agents.md` | EPIC planning, implementation |

### Ops Stages (JANUS ownership: v0.8+)
| Stage | Files | Focus |
|-------|-------|-------|
| v0.8 Deployment & Ops | `janus-intake.md`, `deployment-agents.md` | CI/CD, monitoring, Gate 4 |

## File Types

- **`*-intake.md`**: Guidance for the lead agent (AURA/APOLLO/JANUS) to produce PRD deliverables.
- **`research-agents.md`**: Guidance for research sub-agents producing evidence bundles.
- **`build-agents.md`**: Guidance for build sub-agents (CODE-SMITH, TEST-FORGE, etc.).
- **`deployment-agents.md`**: Guidance for ops sub-agents (INFRA-SMITH, SENTINEL, etc.).

## Ready-to-Use Prompts

Each instruction file includes a **Ready-to-Use Agent Prompt** section at the end. These prompts can be copied directly into an AI assistant to execute that stage's work.

## Usage Guidelines

1. Each stage should host **one to three** role-specific instruction files that align with Gear Heart Methodology (GHM) checkpoints.
2. Instruction files must describe how outputs map into the Source-of-Truth (SoT) graph and note any lifecycle hooks for the next PRD version.
3. Before editing or creating a stage playbook, review active field learnings in [`source-of-truth/customer-feedback.md`](../../source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build) so updates embed real-world guidance like CFD-401 (prompt precision, real-user loops, mobile validation, distribution visibility).
4. When introducing a new stage, create a new `vX.Y/` directory, populate the relevant instructions, and cross-link them from the previous stage as needed.
5. Keep filenames consistent across stages so downstream automation can locate role guides predictably.

## Agent Ownership Summary

| Agent | Stages | Primary Focus |
|-------|--------|---------------|
| **AURA** | v0.1–v0.5 | Market & Product Strategy |
| **APOLLO** | v0.6–v0.7 | Architecture & Build |
| **JANUS** | v0.8–v0.9 | Deployment & Ops |
| **IRIS** | v0.4–v0.7 (advisory) | Design & UX |

By centralizing the instructions here, we make it easier for research, drafting, and validation agents to adopt a shared workflow while scaling additional PRD phases.
