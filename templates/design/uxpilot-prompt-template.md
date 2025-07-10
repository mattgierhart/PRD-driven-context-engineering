---
version: 1.1
purpose: To provide a structured prompt for UXPilot.ai, ensuring the generated wireframes are consistent, well-structured, and aligned with project requirements.
summary: Added a standardized metadata header and a contextual "Authority, Template Usage, and Standards" section.
last_updated: 2025-07-02
---

# UX Prompt for {Product Name}

## Authority, Template Usage, and Standards

- **Authority**: The use of UXPilot and this prompt template is part of the design workflow defined in [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md).
- **Template Usage**: This template is the starting point for all new design projects using UXPilot. See the [Template Usage Guide](./README.md).
- **Standards**: The output from UXPilot must be convertible to the standards defined in [STANDARDS.md](../../STANDARDS.md).

## Tool Configuration
- **Mode**: Wireframes (recommended for best results)
- **Design System**: Default / {Figma System Name}
- **Screen Type**: Mobile app / Desktop
- **Pages**: {number} pages
- **Export**: Individual HTML files

## Page Context
{Product description and purpose}

Design Requirements:
- Use light theme with these exact colors:
  Primary: #{hex} ({color-name})
  Secondary: #{hex} ({color-name})
  Success: #{hex} ({color-name})
  Error: #{hex} ({color-name})
  Background: #{hex}
  Text: #{hex}

- Font: {font-family} for all text
- Border radius: {size}px for cards, {size}px for buttons
- Shadows: {shadow-definition}

Asset Placeholders (create gray boxes with labels):
{List all placeholders using [ASSET TYPE: Description dimensions] format}

Component Patterns:
- Primary button: {description}
- Secondary button: {description}
- Cards: {description}
- Navigation: {description}

Layout Requirements:
{Specific layout instructions}

Include placeholder blocks for creative assets - do not attempt to create actual graphics.

## Creative Asset Specifications

### Required Assets
| Asset ID | Type | Dimensions | Purpose | Placeholder Text |
|----------|------|------------|---------|------------------|
| {id} | {type} | {dimensions} | {purpose} | [{TYPE}: {description}] |

### Asset Creation Notes
- **Timing**: Create after wireframe approval
- **Style Guide**: Match {product} brand guidelines
- **Performance**: Optimize for web delivery
- **Formats**: SVG for icons, WebP for photos, MP4 for animations

## Pages & Navigation Map

### Page 1: {Page Name}
**File**: page-1-{name}.html
**Purpose**: {What this page does}

**Prompt**: 
```
{Exact prompt text for UXPilot.ai}
Include:
- {specific elements}
- {layout requirements}
- {placeholder assets}
```

**Navigation**:
- → Page {n} via {element/action}
- ← Back to {page} via {element}

**Key Elements**:
- `#{element-id}`: {purpose}
- `.{class-name}`: {reusable component}

### Page 2: {Page Name}
{Repeat structure for all pages}

## Navigation Implementation

### Route Structure
```javascript
const routes = {
  '/': HomePage,
  '/{path}': {PageComponent},
  '/{path}/:id': {DetailComponent}
}
```

### Navigation Handlers
```javascript
const navigation = {
  '{actionName}': () => navigate('{path}'),
  '{actionName}': (id) => navigate(`{path}/${id}`)
}
```

### State Persistence
- {What needs to persist between pages}
- {Session storage requirements}
- {API state management}

## Component Extraction Guide

### Identified Reusable Components
1. **{ComponentName}**
   - Source: Page {n}, element `#{id}`
   - Props: {list of props}
   - Variations: {if any}

2. **{ComponentName}**
   - Source: Multiple pages
   - Props: {list of props}
   - State: {any local state needs}

## Post-UXPilot Checklist
- [ ] All pages exported as HTML
- [ ] Navigation map documented
- [ ] Asset specifications extracted
- [ ] Component inventory created
- [ ] Design tokens verified
- [ ] Ready for Claude Code conversion