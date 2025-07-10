---
version: 1.0
purpose: To serve as a standardized template for conducting and documenting a Comprehensive Performance Audit.
summary: Initial template creation based on the HomeFalcon performance audit.
last_updated: "{YYYY-MM-DD}"
---

# Comprehensive Performance Audit for {Product Name}

## 1. Overview

- **Product:** `{Product Name}`
- **Test Type:** Performance Audit & Strategy
- **Overall Status:** `Pending | In Progress | Issues Found | Completed`
- **Description:** This audit provides a holistic assessment of the application's current performance bottlenecks and outlines a strategic plan for optimization.

## 2. Performance Testing Results

### 2.1. Backend API Performance

*   **Tool Used:** (e.g., k6, Artillery)
*   **Summary:** A high-level summary of the API load testing results.
*   **Key Metrics:**
    *   **Avg. Response Time:** {ms}
    *   **p95 Response Time:** {ms}
    *   **Requests per Second (RPS):** {number}
    *   **Error Rate:** {percentage}
*   **Bottlenecks Identified:**
    1.  (e.g., The `/api/documents/search` endpoint is slow under load.)

### 2.2. Frontend Performance (Core Web Vitals)

*   **Tool Used:** (e.g., Lighthouse, PageSpeed Insights)
*   **Summary:** A summary of the frontend performance metrics.
*   **Key Metrics:**
    *   **Largest Contentful Paint (LCP):** {s}
    *   **First Input Delay (FID):** {ms}
    *   **Cumulative Layout Shift (CLS):** {number}
*   **Issues Identified:**
    1.  (e.g., Large, unoptimized images are slowing down the LCP.)

### 2.3. Database Performance

*   **Tool Used:** (e.g., pg_stat_statements, custom query analysis)
*   **Summary:** A summary of database query performance.
*   **Slowest Queries:**
    1.  {Query 1} - {Avg. execution time}
    2.  {Query 2} - {Avg. execution time}
*   **Issues Identified:**
    1.  (e.g., Missing indexes on key tables.)

## 3. Detailed Issue Log

| ID | Area | Description | Status | Priority | Recommendation |
|:---:|:---|:---|:---:|:---:|:---|
| P1 | `Database` | `Missing composite index on the 'queries' table.` | `Open` | `High` | {Add the recommended index.} |
| P2 | `Frontend` | `Large bundle size due to non-lazy loaded dependencies.` | `Open` | `High` | {Implement lazy loading and code splitting.} |
| P3 | `Backend` | `N+1 query pattern in the 'items' service.` | `Resolved` | `Medium` | {Refactored to use a single batched query.} |

## 4. Optimization Strategy

### 4.1. Database Scaling Plan
1.  **Index Optimization:** {Details}
2.  **Query Optimization:** {Details}

### 4.2. Frontend Optimization Roadmap
1.  **Lazy Loading & Code Splitting:** {Details}
2.  **Asset Optimization:** {Details}

### 4.3. Backend Performance Plan
1.  **Caching Strategy:** {Details}
2.  **Scalability Enhancements:** {Details}

## 5. Conclusion

A final summary of the application's performance posture and a prioritized list of recommendations for improvement.
