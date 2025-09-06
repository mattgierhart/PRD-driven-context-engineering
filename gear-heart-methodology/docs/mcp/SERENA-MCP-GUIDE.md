# Serena MCP Server

**Overview**: An advanced coding agent with semantic understanding, granular editing tools, and shell execution capabilities.

## Strategic Use Cases

*   **Complex Code Refactoring**: Perform large-scale, symbol-aware code modifications that are difficult with simple text replacement.
*   **Automated Debugging**: Create iterative agent loops that can run tests, analyze output, and attempt fixes automatically.
*   **Test-Driven Development**: Write and execute tests, then implement the code to make them pass.
*   **Boilerplate Generation**: Automate the creation of new components, modules, or project scaffolding based on existing patterns.

## Setup

1.  **Installation**: Follow the official Serena documentation to install it as an MCP server.
2.  **Configuration**: Configure Serena's `.yml` file to align with our project structure and coding standards.

## Disabling Overlapping Tools

To leverage Serena's advanced, context-aware tools, it is **highly recommended** to disable our standard file system and shell tools when Serena is active. Serena provides more robust, semantically-aware implementations.

| Our Tool            | Serena Equivalent         | Recommendation         |
| :------------------ | :------------------------ | :--------------------- |
| `read_file`         | `read_file`               | Disable our tool       |
| `write_file`        | `create_text_file`        | Disable our tool       |
| `replace`           | `replace_lines`           | Disable our tool       |
| `list_directory`    | `list_dir`                | Disable our tool       |
| `run_shell_command` | `execute_shell_command`   | Disable our tool       |
| `search_file_content`| `search_for_pattern`      | Disable our tool       |