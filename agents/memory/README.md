---
title: "Agent Memory Layer"
updated: 2025-01-09
---

# Agent Memory Layer

## Purpose

Project-specific learning that accumulates as agents work. Unlike static agent definitions (methodology-level), memory captures patterns discovered during this product's development.

## Files

| File | Agent | Purpose |
|------|-------|---------|
| AURA.project.md | AURA | Market/product patterns for this product |
| Designer.project.md | Designer | UX patterns for this product |
| APOLLO.project.md | APOLLO | Technical patterns for this product |
| GTM.project.md | GTM | Go-to-market patterns for this product |

## Update Protocol

**When to update**:
- Session-Closer subagent updates relevant agent memory
- Manual updates when significant pattern observed
- After any gate advancement (lessons learned)

**Harvest threshold**:
When a pattern appears 3+ times, consider:
1. Add to static layer anti-patterns section
2. Extract to `skills/` for cross-project reuse
3. Both (skill for reuse, static for agent awareness)

## Memory Lifecycle

- **Active development**: Update per session
- **v1.0 reached**: Archive completed sections, keep open questions
- **New iteration**: Carry forward validated patterns, reset experiments

## Template

Each memory file follows the structure in the individual files below.
