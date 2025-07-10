---
version: 1.1
purpose: To provide a template for documenting the specifications of all assets required for a product, ensuring a smooth design and development process.
summary: Added a standardized metadata header and a contextual "Authority, Template Usage, and Standards" section.
last_updated: 2025-07-02
---

# Asset Specifications for {Product Name}

## Authority, Template Usage, and Standards

- **Authority**: Asset creation and management are governed by the workflow defined in [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md).
- **Template Usage**: This template is used to generate a detailed inventory of all assets. See the [Template Usage Guide](./README.md).
- **Standards**: All assets must meet the quality and performance standards outlined in [STANDARDS.md](../../STANDARDS.md).

## Asset Brief Template

### Asset: {Asset Name} ({asset-id})

**Context**
- Page: {Page name and location}
- Container: {Exact dimensions from wireframe}
- Purpose: {What this asset communicates}
- User Impact: {How it enhances UX}

**Technical Specifications**
- Dimensions: {width}x{height}px
- Format: {SVG/PNG/WebP/MP4}
- Max file size: {size}KB
- Responsive behavior: {scaling rules}

**Design Requirements**
- Style: {visual style guidelines}
- Colors: Use tokens from design-tokens.md
- Animation: {if applicable, duration and type}
- Accessibility: {alt text and ARIA labels}

**Integration Notes**
- Component: {Which React component}
- Loading state: {placeholder behavior}
- Error state: {fallback asset}

## Asset Creation Workflow

### Phase 1: Wireframe Completion
- [ ] Lock layout in UXPilot
- [ ] Export all HTML wireframes
- [ ] Verify placeholder positioning
- [ ] Document exact dimensions

### Phase 2: Specification Extraction
- [ ] Extract all placeholder specifications
- [ ] Create detailed asset briefs
- [ ] Plan asset creation timeline
- [ ] Define loading/error states

### Phase 3: Asset Creation
- [ ] Create assets per specifications
- [ ] Optimize for web delivery
- [ ] Test loading states
- [ ] Validate accessibility

### Phase 4: Integration
- [ ] Replace placeholders in code
- [ ] Test responsive behavior
- [ ] Verify performance impact
- [ ] Update documentation

## Asset Inventory

| Asset ID | Type | Status | File Path | Size | Notes |
|----------|------|--------|-----------|------|-------|
| {id} | {type} | {status} | {path} | {size} | {notes} |

## Performance Tracking

### Target Metrics
- **Total Asset Size**: < {target}KB
- **Loading Time**: < {target}ms
- **Core Web Vitals**: All green
- **Accessibility Score**: > 95%

### Actual Metrics
- **Total Asset Size**: {actual}KB
- **Loading Time**: {actual}ms
- **Core Web Vitals**: {scores}
- **Accessibility Score**: {score}%

## Troubleshooting

### Common Issues
- **Asset doesn't fit layout**: Verify exact dimensions from wireframe
- **Loading performance**: Check file size and format optimization
- **Accessibility problems**: Ensure alt text and ARIA labels
- **Responsive issues**: Test on all target breakpoints