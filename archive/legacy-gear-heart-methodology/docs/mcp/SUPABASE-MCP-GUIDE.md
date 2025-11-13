# Supabase MCP Server

**Overview**: Provides tools to interact with Supabase projects, enabling direct database manipulation, schema management, and inspection.

## Strategic Use Cases

*   **Rapid Prototyping**: Quickly stand up a backend by creating and modifying database tables directly from the CLI.
*   **Data Seeding & Management**: Insert, update, and query data for testing or initial setup.
*   **Schema Inspection**: Allow the LLM to view the current database schema to write accurate queries or backend code.
*   **Automated Migrations**: (Use with caution) Generate and apply database migrations programmatically.

## Setup

### 1. Get Access Token

1.  Navigate to [app.supabase.com/account/tokens](https://app.supabase.com/account/tokens).
2.  Click "Generate New Token" and give it a descriptive name.
3.  Copy the token immediately.

### 2. Set Environment Variable

Add the token to your shell profile (`~/.zshrc` or `~/.bash_profile`) and reload your shell.
```bash
export SUPABASE_ACCESS_TOKEN="your_supabase_token_here"
```

### 3. Register the Server

Run the following command, replacing `<your-project-ref>` with your actual Supabase Project Ref.

```bash
claude mcp add supabase -s local -e SUPABASE_ACCESS_TOKEN=$SUPABASE_ACCESS_TOKEN -- npx -y @supabase/mcp-server-supabase@latest -- --project-ref <your-project-ref> --read-only
```

**Flags:**
*   `--project-ref <your-project-ref>`: **(Required)** Scopes access to a single project.
*   `--read-only`: **(Recommended)** Prevents the AI from making changes to your database. Remove this flag only when you explicitly need to perform write operations.
