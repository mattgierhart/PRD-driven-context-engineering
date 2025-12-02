---
test_type: "User Acceptance Testing (UAT)"
epic_reference: "EPIC-{XXX}"
status: "Not Started"
created_date: "{YYYY-MM-DD}"
last_updated: "{YYYY-MM-DD}"
---

# User Acceptance Testing (UAT) Plan: {Feature/Product Name}

## 1. Overview

- **Product/Feature:** {Product Name}
- **Testing Goal:** To verify that the product meets business requirements and is fit for purpose from an end-user perspective.
- **Environment:** Staging (URL: {link_to_staging_env})

## 2. Test Scenarios

This section outlines the specific user stories and scenarios that will be tested. The tester should follow these steps and record the outcome.

### 2.1. Scenario 1: {User Story Title, e.g., New User Registration}

*   **User Story:** As a new user, I want to be able to register for an account so that I can access the application.
*   **Test Steps:**
    1.  [ ] Navigate to the registration page.
    2.  [ ] Fill out the registration form with valid data.
    3.  [ ] Submit the form.
    4.  [ ] Receive a verification email.
    5.  [ ] Click the verification link.
    6.  [ ] Be successfully logged into the application.
*   **Expected Result:** The user should be able to create an account and log in without errors.
*   **Actual Result:** *(To be filled out by the tester)*
*   **Status:** `Pass | Fail`

### 2.2. Scenario 2: {User Story Title, e.g., Core Feature Workflow}

*   **User Story:** {User story description}
*   **Test Steps:**
    1.  [ ] {Step 1}
    2.  [ ] {Step 2}
    3.  [ ] {Step 3}
*   **Expected Result:** {Expected outcome}
*   **Actual Result:** *(To be filled out by the tester)*
*   **Status:** `Pass | Fail`

## 3. Feedback and Issues Log

Any feedback, bugs, or unexpected behavior discovered during testing should be logged here.

| ID | Page / Feature | Description of Issue | Severity (`High/Medium/Low`) | Screenshot/Link |
|:---:|:---|:---|:---:|:---|
| UAT-1 | `Registration Page` | `The confirmation email was not received.` | `High` | | 
| UAT-2 | `Dashboard` | `The main chart is not displaying any data.` | `High` | | 

## 4. Sign-off

By signing off on this UAT plan, the product owner confirms that the feature/product has been tested and meets the agreed-upon business requirements.

- **Product Owner:** {Your Name}
- **Date:** {YYYY-MM-DD}
- **Decision:** `Approved for Release` | `Requires Changes`
