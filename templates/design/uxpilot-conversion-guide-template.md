---
version: 1.1
purpose: To guide the conversion of UXPilot HTML wireframes into a functional React application, ensuring consistency and adherence to standards.
summary: Added a standardized metadata header and a contextual "Authority, Template Usage, and Standards" section.
last_updated: 2025-07-02
---

# UXPilot to React Conversion Guide for {Product Name}

## Authority, Template Usage, and Standards

- **Authority**: The conversion process is a key step in the development workflow detailed in [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md).
- **Template Usage**: This guide is generated for each UXPilot project. See the [Template Usage Guide](./README.md).
- **Standards**: The resulting React application must comply with the coding and architectural standards in [STANDARDS.md](../../STANDARDS.md).

## Overview
Convert the attached HTML wireframes into a React application with:
- React Router v6 for navigation
- Tailwind CSS (preserve all classes)
- Component extraction as specified
- Navigation map implementation
- APOLLO cost optimization standards

## Pre-Conversion Checklist
- [ ] All UXPilot HTML exports available
- [ ] Navigation map documented
- [ ] Component extraction plan defined
- [ ] Asset specifications documented
- [ ] Design tokens verified

## Component Extraction Plan

### Identified Reusable Components
1. **{ComponentName}**
   - Source: {Page and element location}
   - Props: {list of required props}
   - Variations: {if any}
   - Tailwind Classes: {preserve exact classes}

2. **{ComponentName}**
   - Source: {Multiple pages/locations}
   - Props: {list of required props}
   - State: {any local state requirements}
   - Tailwind Classes: {preserve exact classes}

### Component Structure
```
components/
├── shared/
│   ├── Navigation.jsx      # From {source page/element}
│   ├── Button.jsx          # From {source page/element}
│   ├── Card.jsx            # From {source page/element}
│   └── Layout.jsx          # From {source page/element}
└── pages/
    ├── HomePage.jsx        # From page-1-home.html
    ├── {PageName}.jsx      # From page-{n}-{name}.html
    └── {PageName}.jsx      # From page-{n}-{name}.html
```

## Navigation Implementation

### Route Structure
```javascript
// Based on navigation map from UXPilot wireframes
const routes = {
  '/': HomePage,                    // From page-1-home.html
  '/{path}': {PageComponent},       // From page-{n}-{name}.html
  '/{path}/:id': {DetailComponent}  // From page-{n}-{name}.html
}
```

### Navigation Handlers
```javascript
// Extract from UXPilot onclick and href attributes
const navigation = {
  '{actionName}': () => navigate('{path}'),
  '{actionName}': (id) => navigate(`{path}/${id}`)
}
```

## Conversion Process

### Step 1: Project Setup
```bash
# Create React app with TypeScript and Tailwind
npm create next-app@latest {product-name} --typescript --tailwind --app

# Install required dependencies
npm install react-router-dom @types/react-router-dom
```

### Step 2: Extract Base Components
1. **Navigation Component**
   - Extract from: {specify UXPilot export}
   - Preserve: {list exact Tailwind classes}
   - Convert: {HTML structure to JSX}

2. **Layout Component**
   - Extract from: {specify UXPilot export}
   - Preserve: {list exact Tailwind classes}
   - Include: Navigation and common elements

### Step 3: Create Page Components
For each UXPilot HTML export:
1. Create corresponding React component
2. Preserve exact Tailwind classes
3. Extract reusable elements to shared components
4. Maintain placeholder structure for assets
5. Add TODO comments for future enhancements

### Step 4: Implement Routing
```javascript
// App.jsx - Based on navigation map
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/shared/Layout';
import HomePage from './components/pages/HomePage';
// ... other imports

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          {/* Add routes based on navigation map */}
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}
```

## State Management Strategy

### Local State Requirements
- {Component}: {state needs}
- {Component}: {state needs}

### Global State Requirements
- {Context/Provider}: {shared state needs}
- {Context/Provider}: {shared state needs}

### Implementation
```javascript
// Start with React Context - no external libraries initially
const {StateContext} = createContext();

const {StateProvider} = ({ children }) => {
  const [state, setState] = useState({
    // Initial state based on UXPilot wireframes
  });

  return (
    <{StateContext}.Provider value={{ state, setState }}>
      {children}
    </{StateContext}.Provider>
  );
};
```

## Asset Integration Plan

### Placeholder Preservation
Keep all UXPilot placeholders as-is during initial conversion:
```jsx
// Example: Preserve placeholder structure
<div className="w-12 h-12 bg-neutral-400 rounded-lg">
  {/* TODO: Replace with actual asset */}
  {/* Original placeholder: [ICON: User avatar 48x48px] */}
</div>
```

### Loading States
Implement loading states for future asset integration:
```jsx
const [isLoading, setIsLoading] = useState(true);

return (
  <div className="w-12 h-12 rounded-lg">
    {isLoading ? (
      <div className="bg-neutral-400 animate-pulse w-full h-full rounded-lg" />
    ) : (
      <img src={assetUrl} alt={altText} className="w-full h-full rounded-lg" />
    )}
  </div>
);
```

## Performance Considerations

### Bundle Optimization
- Lazy load route components
- Implement code splitting at route level
- Use dynamic imports for large components

### Implementation
```javascript
// Lazy load pages
const HomePage = lazy(() => import('./components/pages/HomePage'));
const {PageName} = lazy(() => import('./components/pages/{PageName}'));

// Wrap in Suspense
<Suspense fallback={<div>Loading...</div>}>
  <Routes>
    <Route path="/" element={<HomePage />} />
  </Routes>
</Suspense>
```

### Error Boundaries
```javascript
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <div className="p-4 text-center">Something went wrong.</div>;
    }

    return this.props.children;
  }
}
```

## Quality Assurance

### Conversion Checklist
- [ ] All UXPilot pages converted to React components
- [ ] Exact Tailwind classes preserved
- [ ] Navigation working between all pages
- [ ] Reusable components extracted
- [ ] Placeholder structure maintained
- [ ] Loading states implemented
- [ ] Error boundaries added
- [ ] Performance optimizations applied

### Testing Strategy
- [ ] Manual navigation testing
- [ ] Component rendering verification
- [ ] Responsive design validation
- [ ] Placeholder structure verification
- [ ] Performance baseline measurement

### Handoff to Enhancement Phase
- [ ] Base MVP functionality complete
- [ ] Asset integration ready
- [ ] State management foundations laid
- [ ] Performance targets met
- [ ] Documentation updated

## Post-Conversion Notes

### Asset Integration Next Steps
1. Replace placeholders with actual assets (use asset specifications)
2. Implement progressive image loading
3. Add proper error states for failed asset loads
4. Optimize asset delivery and caching

### Feature Enhancement Next Steps
1. Add form validation and submission
2. Implement API integration
3. Add authentication flow
4. Enhance user interactions

### Performance Monitoring
- Set up Core Web Vitals tracking
- Monitor bundle size growth
- Track component render performance
- Measure navigation speed