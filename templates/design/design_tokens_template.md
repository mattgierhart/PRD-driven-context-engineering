---
version: 1.1
purpose: To define a consistent set of design tokens for a product, ensuring visual consistency and a streamlined development process.
summary: Added a standardized metadata header and a contextual "Authority, Template Usage, and Standards" section.
last_updated: 2025-07-02
---

# Design Tokens for {Product Name}

## Authority, Template Usage, and Standards

- **Authority**: The definition and application of these design tokens are governed by the guidelines in [WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md).
- **Template Usage**: Refer to the [Template Usage Guide](./README.md) for instructions on how to properly implement and extend these tokens. This file is the single source of truth for all styling properties.
- **Standards**: All components and styles must adhere to the token definitions in this file and the broader standards in [STANDARDS.md](../../STANDARDS.md).

## Brand Colors
```css
:root {
  /* Primary Palette */
  --color-primary: #{hex};
  --color-primary-light: #{hex};
  --color-primary-dark: #{hex};
  --color-primary-contrast: #{hex};
  
  /* Secondary Palette */
  --color-secondary: #{hex};
  --color-secondary-light: #{hex};
  --color-secondary-dark: #{hex};
  --color-secondary-contrast: #{hex};
  
  /* Semantic Colors */
  --color-success: #{hex};
  --color-warning: #{hex};
  --color-error: #{hex};
  --color-info: #{hex};
  
  /* Neutral Palette */
  --color-neutral-50: #{hex};
  --color-neutral-100: #{hex};
  --color-neutral-200: #{hex};
  --color-neutral-300: #{hex};
  --color-neutral-400: #{hex};
  --color-neutral-500: #{hex};
  --color-neutral-600: #{hex};
  --color-neutral-700: #{hex};
  --color-neutral-800: #{hex};
  --color-neutral-900: #{hex};
}
```

## Typography
```css
:root {
  /* Font Families */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
  
  /* Font Sizes */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
  
  /* Font Weights */
  --font-light: 300;
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  
  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.75;
}
```

## Spacing
```css
:root {
  /* Base unit: 4px */
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
}
```

## Component Tokens
```css
:root {
  /* Border Radius */
  --radius-sm: 0.25rem;   /* 4px */
  --radius-md: 0.5rem;    /* 8px */
  --radius-lg: 0.75rem;   /* 12px */
  --radius-xl: 1rem;      /* 16px */
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-normal: 300ms ease;
  --transition-slow: 500ms ease;
}
```

## Breakpoints
```css
/* Mobile First Breakpoints */
--screen-sm: 640px;   /* Small tablets */
--screen-md: 768px;   /* Tablets */
--screen-lg: 1024px;  /* Laptops */
--screen-xl: 1280px;  /* Desktops */
--screen-2xl: 1536px; /* Large screens */
```

## Component Patterns

### Buttons
```css
/* Primary Button */
.btn-primary {
  @apply bg-primary text-primary-contrast px-4 py-2 rounded-lg 
         hover:bg-primary-dark transition-colors;
}

/* Secondary Button */
.btn-secondary {
  @apply border border-primary text-primary px-4 py-2 rounded-lg 
         hover:bg-primary hover:text-primary-contrast transition-colors;
}
```

### Cards
```css
.card {
  @apply bg-white rounded-lg border border-neutral-200 p-4 shadow-sm 
         hover:shadow-md transition-shadow;
}
```

### Form Elements
```css
.input {
  @apply bg-neutral-50 border border-neutral-300 rounded-md px-3 py-2 
         focus:border-primary focus:ring-2 focus:ring-primary/20;
}
```

## Usage in UXPilot
When creating the page context, reference these tokens:
- Use exact hex values for colors
- Reference spacing values for consistency
- Apply component patterns as described

## APOLLO Cost Optimization Notes
- Use system fonts where possible to reduce bundle size
- Implement design tokens via CSS custom properties for runtime efficiency
- Keep color palette minimal to reduce CSS complexity
- Use Tailwind's built-in breakpoints to leverage framework optimizations