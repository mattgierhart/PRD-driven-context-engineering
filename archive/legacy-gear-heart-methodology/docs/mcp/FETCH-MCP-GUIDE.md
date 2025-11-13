# Fetch MCP Server

**Overview**: Provides a tool to retrieve content from any URL.

## Strategic Use Cases

*   **Information Gathering**: Quickly pull in content from web pages, articles, or documentation during research.
*   **API Data Retrieval**: Fetch and analyze responses from REST APIs or other web services.
*   **Content Extraction**: Extract text from websites to be summarized or analyzed by the LLM.

## Setup

No setup is required. The Fetch MCP server is available by default.

## Tool Usage

The tool follows the naming convention: `/mcp__fetch__fetch [arguments]`.

*   **`fetch`**: Fetches a URL and returns its content.
    *   **`url` (string, required)**: The URL to fetch.
    *   **`max_length` (integer, optional)**: Max characters to return (default: 5000).
    *   **`start_index` (integer, optional)**: Start at a specific character index.
    *   **`raw` (boolean, optional)**: Set to `true` to get raw HTML/JSON content without Markdown conversion.

*Example:*
```
/mcp__fetch__fetch "https://example.com/article" max_length=1500
```