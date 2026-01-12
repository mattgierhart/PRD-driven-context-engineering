# Design Brief Guidance

> **Purpose**: Reference material for creating comprehensive design briefs during PRD v0.4.
> **Usage**: Load this context when defining screen flows and design requirements.

## Brand Identity & Voice

When defining design direction, consider:

### Brand Personality
- **Primary Traits**: 3-4 adjectives describing the brand
- **Secondary Traits**: 2-3 supporting characteristics
- **Voice Tone**: Professional/Friendly/Technical/Casual

### Visual Identity Direction
- **Color Psychology**: What colors convey the right message
- **Typography Strategy**: Modern/Classic/Technical/Playful
- **Imagery Style**: Photography/Illustrations/Icons approach
- **Overall Aesthetic**: Clean/Bold/Minimal/Rich

---

## User Context Checklist

For each persona, document:

- **Demographics**: Age, location, profession
- **Tech Comfort Level**: High/Medium/Low
- **Usage Context**: When/where/how they'll use the product
- **Device Preferences**: Desktop/Mobile/Tablet priority
- **Accessibility Needs**: Specific requirements

---

## Journey Framework

### Critical Moments to Design For

1. **First Impression** (0-30 seconds)
   - Goal: User understands value proposition
   - Key Elements: Hero section, clear messaging
   - Success Metric: Time to "aha" moment

2. **First Value** (First session)
   - Goal: User experiences core benefit
   - Key Elements: Onboarding, feature discovery
   - Success Metric: Task completion rate

3. **Habit Formation** (Days 2-7)
   - Goal: User returns and engages regularly
   - Key Elements: Notifications, progress tracking
   - Success Metric: Weekly retention rate

---

## Information Architecture Template

### Site Map Structure
```
Landing Page
├── Product Features
├── Pricing
├── About/Company
└── Authentication
    ├── Dashboard/Home
    ├── [Core Feature 1]
    ├── [Core Feature 2]
    ├── Settings/Profile
    └── Help/Support
```

### Navigation Strategy
- **Primary Navigation**: Top bar/Sidebar/Tab approach
- **Secondary Navigation**: Breadcrumbs/Sub-menus/Context menus
- **Mobile Navigation**: Hamburger/Bottom tabs/Drawer

---

## Screen Definition Template

For each screen, define:

### [Screen Name]
**Primary Goal**: {Main user objective}
**Key Elements**:
- {Interface element 1}
- {Interface element 2}
- {Interface element 3}

**User Actions**: {Action 1}, {Action 2}, {Action 3}

---

## Design System Considerations

### Component Library Selection
- **Options**: Tailwind UI, shadcn/ui, Material UI, Custom
- **Selection Criteria**: Speed to market, customization needs, team familiarity
- **Customization Level**: Minimal/Moderate/Extensive

### Design Tokens
- **Colors**: Primary palette approach
- **Typography**: Font selection criteria
- **Spacing**: Grid system approach (4px, 8px base)
- **Elevation**: Shadow/depth strategy

---

## Tool Integration

### UX Design Tool Chain
- **Primary Tool**: UX Pilot/Lovable/Figma
- **Output Format**: Code/Assets/Specifications
- **Hand-off Process**: How design transfers to development

### Design-to-Code Workflow
- **Code Generation**: Level of automation expected
- **Review Cycles**: Number of iterations planned
- **Quality Gates**: What needs approval before development

---

## Success Metrics

### Design Quality Metrics
- **Usability**: Task completion rate >90%
- **Efficiency**: Time to complete core task <2 minutes
- **Satisfaction**: User satisfaction score >4.5/5
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Page load <2 seconds

### Validation Plan
1. Static mockup review with stakeholders
2. Interactive prototype testing with 5-10 users
3. Development integration validation
4. Pre-launch usability testing

---

## Technical Constraints

### Platform Requirements
- **Responsive Breakpoints**: Mobile-first/Desktop-first approach
- **Browser Support**: Minimum browser versions
- **Device Support**: Touch/Mouse/Keyboard considerations

### Performance Budget
- **Bundle Size**: Maximum JS/CSS size
- **Image Optimization**: Format and compression strategy
- **Loading Strategy**: Progressive loading approach

---

*Reference: Use this guidance when creating SCR-XXX entries in SoT.USER_JOURNEYS.md and DES-XXX entries in SoT.DESIGN_COMPONENTS.md*
