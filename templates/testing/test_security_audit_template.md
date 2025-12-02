---
version: 1.1
purpose: To serve as a standardized template for conducting and documenting a Comprehensive Security Audit.
summary: Refined structure based on HomeFalcon audit to include specific vulnerability categories and actionable recommendations.
last_updated: "{YYYY-MM-DD}"
---

# Comprehensive Security Audit - {Project Name}

**Date:** {YYYY-MM-DD}
**Auditor:** {Your Name/Team Name}

## 1. Executive Summary

*   **Overall Risk Level:** `Critical | High | Medium | Low`
*   **Production Readiness:** `Recommended | Not Recommended`
*   **Key Findings:** A brief, high-level summary of the most critical vulnerabilities and areas requiring immediate attention.

## 2. Authentication & Authorization

*   **Summary:** Assessment of user authentication, session management, and access control mechanisms.
*   **Critical Issues:**
    1.  (e.g., Weak JWT Secret Management)
*   **High Issues:**
    1.  (e.g., Missing Multi-Factor Authentication)
*   **Recommendations:**
    *   Provide actionable code snippets or configuration changes to fix the identified issues.

## 3. Input Validation & Sanitization

*   **Summary:** Assessment of how the application handles user-supplied data.
*   **Critical Issues:**
    1.  (e.g., Incomplete Zod/Joi Schema Implementation, leading to XSS)
*   **High Issues:**
    1.  (e.g., SQL Injection Risks in raw queries)
*   **Recommendations:**
    *   Provide examples of proper validation schemas and sanitization techniques.

## 4. Data Protection & Privacy

*   **Summary:** Assessment of how sensitive user data is stored, handled, and protected.
*   **Critical Issues:**
    1.  (e.g., Sensitive Data Exposure in error messages)
*   **High Issues:**
    1.  (e.g., PII Handled improperly, no encryption at rest)
*   **Recommendations:**
    *   Suggest methods for field-level encryption and proper error handling.

## 5. API Security

*   **Summary:** Assessment of the API endpoints and their protection against common attacks.
*   **Critical Issues:**
    1.  (e.g., Insufficient Rate Limiting on auth endpoints)
*   **High Issues:**
    1.  (e.g., CORS Misconfiguration)
*   **Recommendations:**
    *   Provide secure configuration examples for rate limiting, CORS, and security headers.

## 6. Testing Coverage Analysis

*   **Summary:** Analysis of the existing test suite's coverage of security-critical areas.
*   **Critical Test Gaps:**
    1.  (e.g., No tests for auth middleware)
    2.  (e.g., No tests for payment routes)
*   **Recommendations:**
    *   Provide example test cases that should be implemented.

## 7. Infrastructure & Dependency Security

*   **Summary:** Assessment of the deployment environment, secrets management, and third-party dependencies.
*   **Critical Issues:**
    1.  (e.g., Secrets stored in plain text environment variables)
*   **High Issues:**
    1.  (e.g., Outdated and vulnerable dependencies in `package.json`)
*   **Recommendations:**
    *   Suggest tools and processes for secret management (e.g., Vault, Doppler) and dependency scanning (e.g., `npm audit`, Snyk).

## 8. Immediate Action Plan

### Priority 1 (Critical - Fix within 24-48 hours)
1.  {Vulnerability 1}
2.  {Vulnerability 2}

### Priority 2 (High - Fix within 1 week)
1.  {Vulnerability 3}
2.  {Vulnerability 4}

### Priority 3 (Medium - Fix within 2-4 weeks)
1.  {Vulnerability 5}

## 9. Conclusion

A final summary of the application's security posture and a clear recommendation on whether it is safe for production deployment.
