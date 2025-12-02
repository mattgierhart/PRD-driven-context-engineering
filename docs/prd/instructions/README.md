# PRD Instruction Library

This directory organizes workflow instructions that guide each stage of the Product Requirements Document (PRD) lifecycle.

## Structure
- `README.md`: This file. Describes how to navigate the instruction library.
- `vX.Y/`: Versioned subdirectories that capture the instructions required to produce and advance that PRD milestone.
  - `research_agents.md`: Guidance for research agents producing idea sparks and evidence bundles.
  - `aura_intake.md`: Guidance for the AURA drafting agent that converts research bundles into PRD deliverables.
  - Additional files may be added as new roles join the stage (e.g., validation playbooks, engineering intake guides).

## Usage Guidelines
1. Each stage should host **one to three** role-specific instruction files that align with Gear Heart Methodology (GHM) checkpoints.
2. Instruction files must describe how outputs map into the Source-of-Truth (SoT) graph and note any lifecycle hooks for the next PRD version.
3. Before editing or creating a stage playbook, review active field learnings in [`source_of_truth/customer_feedback.md`](../../source_of_truth/customer_feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build) so updates embed real-world guidance like CFD-401 (prompt precision, real-user loops, mobile validation, distribution visibility).
4. Use the [SoT kickoff map by PRD stage](../sot_start_map.md) to ensure each ID-backed file starts on time.
5. When introducing a new stage, create a new `vX.Y/` directory, populate the relevant instructions, and cross-link them from the previous stage as needed.
6. Keep filenames consistent across stages (e.g., `research_agents.md`, `aura_intake.md`) so downstream automation can locate role guides predictably.

By centralizing the instructions here, we make it easier for research, drafting, and validation agents to adopt a shared workflow while scaling additional PRD phases.
