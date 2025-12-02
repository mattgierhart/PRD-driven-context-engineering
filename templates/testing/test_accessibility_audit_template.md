---
version: 1.1
purpose: To serve as a standardized template for conducting and documenting a UI/UX & Accessibility Audit.
summary: Added more detailed structure for specific WCAG categories.
last_updated: "{YYYY-MM-DD}"
---

# UI/UX & Accessibility Audit for {Product Name}

## 1. Overview

- **Product:** `{Product Name}`
- **Test Type:** Accessibility & Visual Regression Testing
- **Overall Status:** `Pending | In Progress | Issues Found | Completed`
- **Target WCAG Compliance:** `AA`

## 2. Automated Scan Results

- **Tool Used:** (e.g., Axe, WAVE, Lighthouse)
- **Run Date:** {YYYY-MM-DD}
- **Summary of Findings:** A high-level overview of the automated scan results, including the number of critical, serious, and moderate issues found.

## 3. Manual Test Results

### 3.1. Keyboard Navigation

*   **Summary:** Assessment of the application's usability with only a keyboard.
*   **Issues Found:**
    1.  (e.g., Focus is not visible on certain elements.)
    2.  (e.g., Keyboard trap in the main modal.)

### 3.2. Screen Reader Experience (NVDA, VoiceOver)

*   **Summary:** Assessment of how the application is perceived and navigated by screen reader users.
*   **Issues Found:**
    1.  (e.g., Images missing alternative text.)
    2.  (e.g., Buttons are not labeled correctly.)

### 3.3. Color Contrast & Visual Design

*   **Summary:** Assessment of color ratios and visual clarity.
*   **Issues Found:**
    1.  (e.g., Text on buttons has insufficient contrast.)
    2.  (e.g., Link text is not distinguishable from surrounding text without relying on color.)

### 3.4. Content & Structure (Semantic HTML)

*   **Summary:** Assessment of the proper use of HTML tags for structure and meaning.
*   **Issues Found:**
    1.  (e.g., Improper heading hierarchy.)
    2.  (e.g., Use of `<div>` for elements that should be buttons.)

## 4. Detailed Issue Log

| ID | Page / Component | WCAG Guideline | Description | Status | Priority | Recommendation |
|:---:|:---|:---|:---|:---:|:---:|:---|
| AX1 | `Login Page` | 1.4.3 (Contrast) | `Color contrast on input field borders is too low (2.5:1).` | `Open` | `High` | {Increase border color to meet 3:1 ratio.} |
| AX2 | `Dashboard` | 2.4.7 (Focus Visible) | `Focus indicator is not visible on chart elements.` | `Open` | `Medium` | {Add a clear focus outline to interactive chart elements.} |
| AX3 | `Profile Page` | 1.1.1 (Non-text Content) | `Missing alt text for user profile picture.` | `Resolved` | `Medium` | {Added descriptive alt text.} |

## 5. Action Plan

### High Priority (Must Fix)
1.  {Issue AX1}

### Medium Priority (Should Fix)
1.  {Issue AX2}

## 6. Conclusion

A final summary of the application's accessibility posture and recommendations for improvement.
