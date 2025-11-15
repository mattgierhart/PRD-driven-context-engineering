# PRD Instruction Library

This directory organizes workflow instructions that guide each stage of the Product Requirements Document (PRD) lifecycle.

## Structure
- `README.md`: This file. Describes how to navigate the instruction library.
- `vX.Y/`: Versioned subdirectories that capture the instructions required to produce and advance that PRD milestone.
  - `research-agents.md`: Guidance for research agents producing idea sparks and evidence bundles.
  - `aura-intake.md`: Guidance for the AURA drafting agent that converts research bundles into PRD deliverables.
  - Additional files may be added as new roles join the stage (e.g., validation playbooks, engineering intake guides).

## Usage Guidelines
1. Each stage should host **one to three** role-specific instruction files that align with Gear Heart Methodology (GHM) checkpoints.
2. Instruction files must describe how outputs map into the Source-of-Truth (SoT) graph and note any lifecycle hooks for the next PRD version.
3. When introducing a new stage, create a new `vX.Y/` directory, populate the relevant instructions, and cross-link them from the previous stage as needed.
4. Keep filenames consistent across stages (e.g., `research-agents.md`, `aura-intake.md`) so downstream automation can locate role guides predictably.

By centralizing the instructions here, we make it easier for research, drafting, and validation agents to adopt a shared workflow while scaling additional PRD phases.
