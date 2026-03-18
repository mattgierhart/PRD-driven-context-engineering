# Tool Adaptation Notes

> How to use the Visual Prototype Gate skill with tools other than Google Stitch.

The per-screen prompt structure is tool-agnostic. Only the preamble and formatting change.

## Google Stitch (Primary)

- Paste Prototype Context Brief first, then generate one screen at a time
- Use "Pro Screen" mode for higher-fidelity output (200 generations/month)
- Export to Figma for further refinement if needed
- Stitch works best with plain language, specific UI keywords, and aesthetic adjectives
- Expect ~60-70% accuracy on first generation; refine with targeted follow-ups
- One change per refinement prompt — do not combine multiple changes

## v0 (Vercel)

- Replace "Layout" field with component description: "a Next.js sidebar panel with..."
- v0 prefers code-aware descriptions — reference component libraries if relevant
- v0 outputs working code, so technical constraints matter more here
- Best for: developer-facing products where prototype should be functional

## Figma AI

- Use SCR- screen names as Figma frame labels
- Paste Key Elements list into frame description
- Emotional beat translates to Figma's auto-layout and visual hierarchy emphasis
- Best for: teams already in Figma who want to iterate within their design system

## Lovable / Bolt

- These generate full working apps, not just screens
- Use for: products where a clickable prototype is more valuable than static screens
- Map the full UJ- journey (not just individual SCR-) as the prompt
- Overkill for v0.4 validation — better suited for v0.7 rapid prototyping

## Midjourney / Image Generators

- Use only for the Money Shot screen (single hero frame)
- Prepend prompt with: "UI screenshot of a [platform] application showing..."
- Append: "--ar 16:9 --style raw" for Midjourney
- Not suitable for multi-screen prototyping — use for pitch decks and landing pages only
