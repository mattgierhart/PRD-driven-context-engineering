# Mobile Development with Expo

## Overview

This document defines the APOLLO standards for mobile application development using Expo and React Native. It covers setup, development workflow, testing, and deployment processes for both iOS and Android platforms.

## When to Use

- Building mobile applications alongside web products
- Rapid prototyping of mobile experiences
- Cross-platform mobile development needs
- When native performance is acceptable (vs. requiring pure native)

## When NOT to Use

- Applications requiring extensive native module integration
- High-performance games or graphics-intensive apps
- Apps requiring background processing beyond Expo's capabilities
- When team has strong native iOS/Android expertise

## Setup and Configuration

### Prerequisites
```bash
# Install Node.js (v16+ recommended)
# Install npm or yarn
# Install Expo CLI globally (optional, npx works too)
npm install -g expo-cli
```

### iOS Development Environment Setup (Xcode Integration)

#### Required for iOS Development
1. **macOS Required**: iOS development requires macOS with Xcode
2. **Install Xcode**: Download from App Store (latest stable version)
3. **Xcode Command Line Tools**: `xcode-select --install`
4. **iOS Simulator Setup**: Configure simulators for target devices

#### Xcode Configuration Checklist
- [ ] Xcode installed and updated to latest stable version
- [ ] Apple Developer account configured (for device testing and distribution)  
- [ ] iOS Simulator installed for target device types (iPhone 14, 15, etc.)
- [ ] Command line tools installed and active
- [ ] Provisioning profiles configured for development

#### Development Environment Verification
```bash
# Verify Xcode installation
xcodebuild -version

# List available simulators
xcrun simctl list devices

# Check iOS Simulator availability
open -a Simulator

# Verify command line tools
xcode-select -p
```

### Initial Setup
1. **Install EAS CLI**: `npm install -g eas-cli`
2. **Login to EAS**: `eas login` (from your mobile project directory)
3. **Configure EAS Project**: `eas build:configure` (links local project to EAS)
4. **Install Dependencies**: `npx expo install expo-dev-client && npm install`
5. **Create `eas.json`**: Configure build profiles (development, preview, production)
6. **Setup iOS Development**: Configure Apple Developer account and provisioning

### Environment Configuration
- Use `.env.local` for `EXPO_PUBLIC_API_URL` and other public variables
- Follow the 4-tier secrets management strategy from [SECRETS_MANAGEMENT.md](./SECRETS_MANAGEMENT.md)
- Never expose Tier 3 or Tier 4 secrets in mobile apps

### Example `eas.json` Structure
```json
{
  "cli": {
    "version": ">= 5.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {}
  },
  "submit": {
    "production": {}
  }
}
```

## Development Workflow

### Local Development with Xcode Integration

#### Standard Development Commands
```bash
# Start development server
npx expo start

# Clear cache and start
npx expo start -c

# Launch directly in iOS Simulator
npx expo start --ios

# Launch directly in Android emulator
npx expo start --android

# Run with specific iOS device
npx expo start --ios --device "iPhone 15 Pro"
```

#### Enhanced Package.json Scripts (Required)
```json
{
  "scripts": {
    "start": "expo start",
    "ios": "expo start --ios",
    "android": "expo start --android",
    "web": "expo start --web",
    
    // Mobile development workflow (NEW REQUIRED)
    "ios:simulator": "expo start --ios",
    "ios:device": "expo start --ios --device",
    "mobile:setup": "expo install && expo prebuild",
    "mobile:doctor": "expo doctor",
    "mobile:clear": "expo start --clear",
    
    // Development with real-time testing
    "dev:mobile": "concurrently \"npm run start\" \"npm run ios\"", 
    "dev:full": "concurrently \"npm run web\" \"npm run ios\"",
    
    // Testing and validation
    "test:mobile": "jest --config=jest.mobile.config.js",
    "validate:mobile": "npm run mobile:doctor && npm run test:mobile"
  }
}
```

### iOS Development Workflow Integration

#### 1. Early Development Phase - Simulator Testing
```bash
# Launch app in iOS Simulator (immediate feedback)
npm run ios

# Test on specific device models
npx expo start --ios --device "iPhone 15 Pro Max"
npx expo start --ios --device "iPad Pro 12.9-inch"

# Monitor performance and memory usage
open -a "Simulator" --args -perfmetrics
```

#### 2. Feature Development - Continuous Mobile Validation
```bash
# Start development with automatic mobile refresh
npm run dev:mobile

# Launch full cross-platform testing
npm run dev:full

# Clear cache if experiencing issues
npm run mobile:clear
```

#### 3. Real Device Testing (Physical iPhone/iPad)
```bash
# Connect iOS device via USB or WiFi
expo start --ios --device

# For production-like testing
eas build --platform ios --profile development
# Install development build on device via TestFlight or direct install
```

### Testing Options with Xcode Integration

1. **iOS Simulator (Primary Development)**
   - **Command**: `npm run ios` or `npx expo start --ios`
   - **Best for**: Daily development, UI testing, feature validation
   - **Advantages**: Instant feedback, easy debugging, multiple device sizes
   - **Setup**: Automatic with Xcode installation

2. **Physical iOS Device Testing**
   - **Setup**: Connect iPhone/iPad via USB or configure WiFi debugging
   - **Command**: `expo start --ios --device`
   - **Best for**: Performance testing, camera features, device-specific testing
   - **Requirements**: Apple Developer account, provisioning profiles

3. **Expo Go (Quick Prototyping)**
   - Run: `npx expo start`
   - Scan QR code with Expo Go app
   - Best for: Quick iterations during development
   - Limitations: Limited to Expo SDK APIs

4. **Development Builds (Advanced Features)**
   - **iOS**: `eas build --platform ios --profile development`
   - **Android**: `eas build --platform android --profile development`
   - Best for: Testing native modules and custom configurations
   - Install via TestFlight or direct install link

## Production Deployment

### Build Commands
```bash
# Android production build
eas build --platform android --profile production

# iOS production build (requires Apple Developer Account)
eas build --platform ios --profile production

# Build both platforms
eas build --platform all --profile production
```

### App Store Submission
```bash
# Submit to Apple App Store
eas submit --platform ios --profile production

# Submit to Google Play Store
eas submit --platform android --profile production
```

### Over-the-Air (OTA) Updates
```bash
# Publish OTA update
eas update --branch production --message "Bug fixes and improvements"

# Check update status
eas update:list
```

## Cost Considerations

### Required Accounts
- **Apple Developer Account**: $99/year (required for iOS distribution)
- **Google Play Developer**: $25 one-time fee
- **EAS Build**: Free tier includes 30 builds/month
  - Priority builds available with paid plans
  - Consider local builds for development

### Cost Optimization
- Use Expo Go for development when possible
- Batch builds to stay within free tier
- Use OTA updates for non-native changes
- Consider building locally for development builds

## Monorepo Considerations

When working in a monorepo structure:
```bash
# Navigate to mobile app directory
cd apps/mobile-app

# Run EAS commands from app directory
eas build --platform android --profile development

# Or use --non-interactive flag from root
eas build --platform android --profile development --non-interactive
```

## Performance Standards

### Mobile-Specific Metrics
- App launch time: <3 seconds
- Screen transition: <300ms
- Touch response: <100ms
- Memory usage: <200MB baseline
- Battery efficiency: Monitor with profiler

### Optimization Techniques
- Use React Native's `FlatList` for long lists
- Implement image caching with `expo-image`
- Lazy load screens with React Navigation
- Minimize bundle size with tree shaking
- Use Hermes JavaScript engine for Android

## Security Best Practices

### Mobile-Specific Security
- Implement certificate pinning for API calls
- Use secure storage for sensitive data: `expo-secure-store`
- Implement biometric authentication when appropriate
- Never store Tier 3/4 secrets in the app bundle
- Use environment-specific API endpoints

### Code Obfuscation
```json
// In eas.json for production builds
{
  "production": {
    "android": {
      "buildType": "apk",
      "gradleCommand": ":app:assembleRelease"
    },
    "ios": {
      "buildConfiguration": "Release"
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check `eas build --platform [platform] --profile development --clear-cache`
   - Verify all dependencies are compatible with Expo SDK version
   - Check native module compatibility

2. **Metro Bundler Issues**
   - Clear cache: `npx expo start -c`
   - Reset Metro: `npx react-native start --reset-cache`
   - Delete node_modules and reinstall

3. **iOS Signing Issues**
   - Ensure Apple Developer account is active
   - Check provisioning profiles: `eas credentials`
   - Regenerate certificates if needed

4. **Android Build Issues**
   - Check Android SDK version compatibility
   - Verify gradle configuration
   - Ensure keystore is properly configured

### Debug Commands
```bash
# Check EAS CLI version
eas --version

# Verify project configuration
eas diagnostics

# Check credentials
eas credentials

# View build logs
eas build:list --platform android
eas build:view [build-id]
```

## Integration with APOLLO Workflow

### Phase 0.5: Technology Selection (Enhanced for Mobile)
- **Mobile Platform Decision**: iOS-first, Android-second, or cross-platform
- **Native vs Expo Evaluation**: Performance requirements vs development speed
- **Device Support Matrix**: Target iOS versions and device types
- **Development Environment**: Xcode setup requirements and team access

### Phase 1: Product Definition (Mobile Considerations)
- **Mobile User Experience**: Touch-first interaction patterns
- **Platform-Specific Features**: iOS/Android native capabilities needed
- **Offline Functionality**: Data sync and offline mode requirements
- **Performance Targets**: Mobile-specific performance benchmarks

### Phase 2: Technical Feasibility (Mobile Architecture)
- **iOS Development Capability**: Team access to macOS and Xcode
- **App Store Requirements**: Apple Developer Program membership
- **Mobile Infrastructure**: Push notifications, deep linking, analytics
- **Testing Strategy**: Simulator vs device testing approach

### Phase 3: Design Integration (Mobile-First)
- Use React Native components that match web design system
- **iOS Design Guidelines**: Follow Apple Human Interface Guidelines
- **Responsive Mobile Design**: Test on iPhone SE to iPhone 15 Pro Max
- **Touch Interface**: Ensure 44pt minimum touch targets
- **Navigation Patterns**: iOS-native navigation with React Navigation

### Phase 4: Development (Mobile Development Integration)
- **Early Mobile Testing**: Set up iOS Simulator from day 1
- **Daily Mobile Validation**: Include `npm run ios` in development workflow
- **Epic Mobile Criteria**: All epics must pass iOS Simulator testing
- **Cross-Platform Testing**: Web and mobile feature parity validation

#### Mobile Development Checkpoints
```markdown
## Mobile Development Checkpoints (Required for all Features)

### Development Phase Validation
- [ ] Feature launches successfully in iOS Simulator
- [ ] Touch interactions work correctly (tap, swipe, scroll)
- [ ] Navigation functions properly on mobile interface
- [ ] Forms and inputs are accessible via touch
- [ ] API calls function from mobile environment
- [ ] Responsive design validates across iPhone sizes

### Pre-Deployment Mobile Testing
- [ ] iOS Simulator testing completed (iPhone 14, 15 Pro)
- [ ] Physical device testing on actual iPhone (recommended)
- [ ] Touch interface validation with real fingers
- [ ] Mobile-specific features verified (camera, location, etc.)
- [ ] Cross-platform compatibility confirmed
- [ ] Performance acceptable on target devices
```

### Phase 5: Deployment & Monitoring (Mobile-Enhanced)
- **iOS App Store Preparation**: Screenshots, metadata, review guidelines
- **TestFlight Beta Testing**: Internal testing before public release
- **Mobile Analytics**: App-specific crash reporting and user behavior
- **Performance Monitoring**: Mobile-specific metrics and optimization

#### Mobile Deployment Checklist
- [ ] Apple Developer account configured and active
- [ ] iOS app icons and splash screens generated
- [ ] App Store metadata and screenshots prepared  
- [ ] TestFlight internal testing completed
- [ ] Production build tested on physical devices
- [ ] App Store review guidelines compliance verified

## Related Standards

- [FILE_STRUCTURE.md](./FILE_STRUCTURE.md) - Directory organization
- [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) - Version control practices
- [SECRETS_MANAGEMENT.md](./SECRETS_MANAGEMENT.md) - Environment variables
- [MONITORING-ALERTING.md](./MONITORING-ALERTING.md) - Mobile app monitoring

## References

- [Expo Documentation](https://docs.expo.dev)
- [EAS Build Documentation](https://docs.expo.dev/build/introduction/)
- [React Native Performance](https://reactnative.dev/docs/performance)
- [App Store Guidelines](https://developer.apple.com/app-store/guidelines/)
- [Google Play Guidelines](https://play.google.com/console/about/)