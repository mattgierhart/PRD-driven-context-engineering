# Standard: File & Directory Structure

This document defines the immutable, standardized file and directory structures for the APOLLO development environment. These structures are critical for maintaining predictability, reducing cognitive overhead, and enabling effective automation. They are not to be altered without a formal review process.

## Hard Truth 1: The Meta-Layer (Root Directory)

The `~/development/` root directory is the foundational meta-layer of our workspace. Its structure is fixed and serves as the primary organizational framework for all products and tools.

**Core Principle**: The root directory contains only three primary subdirectories: `products`, `tools`, and `opensource`. All other files and directories must reside within one of these. No project files, scripts, or documentation should ever be placed in the root.

```
/development/
├─── products/      # Contains all revenue-generating products, organized by product name.
│
├─── tools/         # Contains all shared utilities, scripts, templates, and configurations that support the development workflow.
│
└─── opensource/    # Contains any open-source projects we contribute to or maintain.
```

## Hard Truth 2: The Product-Layer (Standardized Product Directory)

Every new product created within the `products/` directory **must** adhere to the following standardized structure. This ensures that anyone can navigate any product and immediately locate key artifacts.

**Core Principle**: A product's directory is self-contained. All documentation, research, design assets, source code, and scripts related to that specific product live within its designated folder.

```
/products/{product-name}/
│
├─── {product-name}-PRD.md           # The single source of truth for product requirements (living document).
├─── {product-name}-DesignBrief.md   # The single source of truth for design specifications.
├─── CLAUDE.md                       # Product-specific operational directives for the Claude agent.
│
├─── active-projects/                # Contains the active source code and related build/deployment files.
│   └─── mvp/                        # The primary folder for the Minimum Viable Product development.
│
├─── docs/                           # All supporting documentation, organized by function.
│   ├─── research/                   # All market, competitive, and user research.
│   ├─── design/                     # All design assets, wireframes, and UX/UI specifications.
│   └─── epics/                      # All development epics, broken down by phase.
│
├─── scripts/                        # Any scripts specific to this product (e.g., deployment, data migration).
│
└─── archive/                        # Contains all outdated or deprecated files for this product.
```
