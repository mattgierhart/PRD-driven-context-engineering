---
version: 2.0
last_updated: 2025-08-31
maintainer: Claude Code
description: Comprehensive master guide consolidating all MCP server setup, configuration, usage, and management
consolidates: MCP-GUIDE.md, MCP-CONFIGURATION.md, mcp-setup-guide.md
---

# MCP Master Guide: Complete Model Context Protocol Integration

## Table of Contents

1. [Overview](#1-overview)
2. [Quick Start](#2-quick-start)
3. [Configuration Methods](#3-configuration-methods)
4. [Active MCP Servers](#4-active-mcp-servers)
5. [Environment Management](#5-environment-management)
6. [Health Monitoring & Fallbacks](#6-health-monitoring--fallbacks)
7. [Performance Optimization](#7-performance-optimization)
8. [Troubleshooting](#8-troubleshooting)
9. [Advanced Features](#9-advanced-features)
10. [Contributing New Servers](#10-contributing-new-servers)

---

## 1. Overview

This is the single source of truth for all Model Context Protocol (MCP) server integration in our development workflow. MCP servers provide Claude Code with specialized capabilities for file management, version control, database operations, web automation, and AI collaboration.

### Core Philosophy
- **Strategic Integration**: Each MCP server serves specific development workflow phases
- **Reliability First**: Health monitoring, fallbacks, and graceful degradation
- **Security Conscious**: Environment variable management and access control
- **Performance Optimized**: Caching, resource limits, and priority-based loading

---

## 2. Quick Start

### Check Current Status
```bash
# See all registered and connected MCP servers
claude mcp list

# Check specific server configuration
claude mcp get <server_name>
```

### Verify Environment
```bash
# Check required environment variables
env | grep -E "(TOKEN|KEY|ACCESS)"

# Test server connectivity (if health check script exists)
~/development/tools/scripts/check-mcp-health.sh
```

### Common Commands
```bash
# Add new server (CLI method)
claude mcp add <server_name> [flags] -- <command>

# Remove server
claude mcp remove <server_name> -s local

# Restart all MCP servers (if script exists)
~/development/tools/scripts/restart-mcp-servers.sh
```

---

## 3. Configuration Methods

**VALIDATED TRUTH**: Our setup uses **BOTH** configuration approaches simultaneously and successfully.

### Method 1: JSON Configuration (Primary)
**Location**: `/Users/mattgierhart/Library/CloudStorage/Dropbox/development/mcp.json`  
**Purpose**: Define server configurations with environment variable support  
**Advantages**: Persistent, version-controlled, supports complex configurations

```json
{
  "mcpServers": {
    "server_name": {
      "command": "npx",
      "args": ["-y", "@package/name"],
      "env": {
        "API_TOKEN": "${env:API_TOKEN}"
      },
      "description": "Server description",
      "priority": 2,
      "optional": true
    }
  }
}
```

### Method 2: CLI Registration (Supplementary)
**Purpose**: Dynamic server management and HTTP transport servers  
**Advantages**: Interactive setup, good for HTTP servers like Vercel

```bash
# Command-based server
claude mcp add server_name -s local -- npx -y @package/name

# HTTP transport server
claude mcp add --transport http server_name https://server-url
```

### Environment Variable Syntax
**In mcp.json**: Use `"${env:VARIABLE_NAME}"` format  
**In shell**: Standard `$VARIABLE_NAME` or `${VARIABLE_NAME}`

---

## 4. Active MCP Servers

### 4.1 Filesystem MCP Server
- **Identifier**: `filesystem`
- **Priority**: Critical (1)
- **Purpose**: Direct local file system access for project management
- **Key Commands**:
  - `read_file`: Read specific file content
  - `write_file`: Create/overwrite files
  - `list_directory`: Directory contents
  - `search_files`: Find files by pattern
- **Strategic Use Cases**:
  - **Context Gathering**: Reading `claude.md`, `package.json`, source files
  - **Code Implementation**: Writing generated code after verification
  - **Refactoring**: File modifications and updates
- **Configuration**:
  ```json
  "filesystem": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-filesystem"],
    "args_extra": ["/Users/mattgierhart/Library/CloudStorage/Dropbox/development"],
    "description": "Local file system access for project management."
  }
  ```

### 4.2 GitHub MCP Server
- **Identifier**: `github`
- **Priority**: Important (2)
- **Purpose**: GitHub repository management, issues, PRs, and code search
- **Key Commands**:
  - `get_issue`: Fetch GitHub issue details
  - `create_pull_request`: Create new PR
  - `search_code`: Repository code search
  - `get_file_contents`: Read files from remote repo
- **Strategic Use Cases**:
  - **Task Context**: Reading associated GitHub issues for requirements
  - **Workflow Automation**: Auto-creating PRs after feature completion
  - **Code Discovery**: Finding existing patterns in codebase
- **Environment**: Requires `GITHUB_TOKEN`
- **Fallback**: filesystem + git CLI commands
- **Configuration**:
  ```json
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
    },
    "description": "GitHub repository management, issues, PRs, and code search."
  }
  ```

### 4.3 Supabase MCP Server
- **Identifier**: `supabase`
- **Priority**: Important (2)
- **Purpose**: Direct Supabase backend interaction for data and schema management
- **Key Commands**:
  - `execute_sql`: Run SQL queries
  - `list_tables`: Database schema inspection
  - `get_project`: Project details
  - `apply_migration`: Database migrations
- **Strategic Use Cases**:
  - **Data Validation**: Checking existing records before operations
  - **Schema-Aware Development**: Fetching current schema for code generation
  - **Debugging**: Direct database inspection during development
- **Environment**: Requires `SUPABASE_ACCESS_TOKEN`
- **Configuration**:
  ```json
  "supabase": {
    "command": "npx",
    "args": [
      "-y", "@supabase/mcp-server-supabase@latest",
      "--access-token", "${env:SUPABASE_ACCESS_TOKEN}",
      "--organization", "yxwvwjzltvymxghjbkqn"
    ],
    "description": "Supabase project management and data access."
  }
  ```

### 4.4 Zen MCP Server (AI Sub-Agents)
- **Identifier**: `zen`
- **Priority**: Important (2)
- **Purpose**: "Senior/Junior Developer" workflow via specialized AI sub-agents
- **Key Commands**:
  - `chat`: General conversation with sub-agents
  - `codereview`: Code review delegation
  - `consensus`: Multi-agent opinion gathering
  - `debug`: Systematic debugging workflows
- **Available Models**:
  - **Qwen** (`qwen/qwen-2.5-coder-32b-instruct:free`): Boilerplate generation, unit tests
  - **Kimi** (`moonshotai/kimi-k2:free`): Code analysis, documentation review
- **Strategic Use Cases**:
  - **Boilerplate Generation**: Offload simple component creation
  - **Code Refinement**: Second opinions and error checking
  - **Complex Analysis**: Deep reasoning with fresh context
- **Configuration**: Local Python server with virtual environment
- **Related Documentation**:
  - [SUBAGENT_REGISTRY.md](../workflows/SUBAGENT_REGISTRY.md)
  - [MODEL_USAGE_GUIDE.md](../workflows/MODEL_USAGE_GUIDE.md)

### 4.5 Context7 MCP Server
- **Identifier**: `context7`
- **Priority**: Important (2)
- **Purpose**: Real-time library documentation without context token consumption
- **Key Commands**:
  - `resolve-library-id`: Find correct library identifiers
  - `get-library-docs`: Fetch current documentation
- **Strategic Use Cases**:
  - **API Reference**: Current, accurate library documentation
  - **Sub-Agent Enhancement**: Provide docs to sub-agents without context bloat
  - **Context Preservation**: Access docs without consuming orchestrator context
- **Usage Pattern**: Include "use context7" in prompts
- **Configuration**:
  ```json
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"],
    "description": "Real-time library documentation access"
  }
  ```

### 4.6 Brave Search MCP Server
- **Identifier**: `brave-search`
- **Priority**: Optional (3)
- **Purpose**: Privacy-focused web search for market research
- **Key Commands**:
  - `brave_web_search`: General web search
  - `brave_local_search`: Local business search
- **Strategic Use Cases**:
  - **Market Research**: Competitive analysis and trends
  - **Documentation Lookup**: Finding external resources
  - **Problem Solving**: Search for solutions to development issues
- **Environment**: Requires `BRAVE_API_KEY`
- **Graceful Degradation**: Skip web search if unavailable
- **Configuration**:
  ```json
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "${env:BRAVE_API_KEY}"
    },
    "description": "Privacy-focused web search for market research."
  }
  ```

### 4.7 Vercel MCP Server
- **Identifier**: `vercel`
- **Priority**: Important (2)
- **Purpose**: Official Vercel integration for deployment management and analysis
- **Transport**: HTTP (not command-based)
- **Key Commands**:
  - `search_vercel_documentation`: Deployment guidance
  - `list_deployments`: Project deployment history
  - `get_deployment_build_logs`: Error analysis
  - `deploy_to_vercel`: Direct deployment
- **Strategic Use Cases**:
  - **APOLLO Phase 5**: Deployment automation and validation
  - **Issue Troubleshooting**: AI-powered log analysis
  - **Performance Monitoring**: Deployment health checks
- **Environment**: Requires `VERCEL_TOKEN`
- **Setup**: HTTP transport requires CLI registration
  ```bash
  claude mcp add --transport http vercel https://mcp.vercel.com
  export VERCEL_TOKEN="your_token"
  ```
- **Configuration**:
  ```json
  "vercel": {
    "url": "https://mcp.vercel.com",
    "env": {
      "VERCEL_TOKEN": "your_vercel_token"
    },
    "description": "Official Vercel MCP server for deployment management."
  }
  ```

### 4.8 Puppeteer MCP Server
- **Identifier**: `puppeteer`
- **Priority**: Optional (3)
- **Purpose**: Browser automation for testing, validation, and data extraction
- **Package**: `@hisma/server-puppeteer` (maintained fork)
- **Key Commands**:
  - `puppeteer_navigate`: Browser navigation
  - `puppeteer_screenshot`: Visual capture
  - `puppeteer_click`: Element interaction
  - `puppeteer_fill`: Form filling
  - `puppeteer_evaluate`: JavaScript execution
- **Strategic Use Cases**:
  - **APOLLO Phase 4**: End-to-end testing automation
  - **Phase 5 Deployment**: Production smoke testing
  - **Quality Assurance**: Visual regression and cross-browser testing
  - **Data Extraction**: Dynamic content scraping
- **Security Warning**: ⚠️ Grants access to local files and internal networks
- **APOLLO Integration**:
  - Gate 3.5: E2E testing requirements
  - Gate 4: Browser automation validation
  - Phase 5: Post-deployment verification
- **Configuration**:
  ```json
  "puppeteer": {
    "command": "npx",
    "args": ["-y", "@hisma/server-puppeteer"],
    "description": "Browser automation capabilities using Puppeteer. WARNING: Grants access to local files and internal IP addresses.",
    "priority": 3,
    "optional": true
  }
  ```
- **Related Documentation**:
  - [puppeteer-integration-patterns.md](./puppeteer-integration-patterns.md)
  - [testing_playbook-template.md](../templates/testing_playbook-template.md)

---

## 5. Environment Management

### 5.1 Required Environment Variables
```bash
# GitHub Integration
export GITHUB_TOKEN="ghp_your_github_token"

# Supabase Integration  
export SUPABASE_ACCESS_TOKEN="sbp_your_supabase_token"

# Search Capabilities
export BRAVE_API_KEY="your_brave_api_key"

# Deployment Management
export VERCEL_TOKEN="your_vercel_token"

# Optional: Puppeteer Launch Options
export PUPPETEER_LAUNCH_OPTIONS='{"headless": true}'
```

### 5.2 Shell Profile Setup
1. **Open your shell configuration**:
   ```bash
   open -a "Visual Studio Code" ~/.zshrc
   ```

2. **Add environment variables**:
   ```bash
   # MCP Server Environment Variables
   export GITHUB_TOKEN="your_github_token"
   export SUPABASE_ACCESS_TOKEN="your_supabase_token"
   export BRAVE_API_KEY="your_brave_api_key"
   export VERCEL_TOKEN="your_vercel_token"
   ```

3. **Reload configuration**:
   ```bash
   source ~/.zshrc
   ```

4. **Restart Claude Code session** for changes to take effect

### 5.3 Security Best Practices
- **Never commit tokens**: Use environment variables, not hardcoded values
- **Rotate tokens regularly**: Especially for production access
- **Scope permissions**: Use minimal required permissions for each token
- **Monitor usage**: Watch for unexpected API usage patterns

---

## 6. Health Monitoring & Fallbacks

### 6.1 Priority-Based System
1. **Critical (Priority 1)**: Must work - no fallback
   - `filesystem`: Core file operations
   
2. **Important (Priority 2)**: Fallback available
   - `github`: → filesystem + git CLI
   - `supabase`: → read-only cached data
   - `zen`: → direct Claude usage
   - `context7`: → manual documentation lookup
   - `vercel`: → manual deployment
   
3. **Optional (Priority 3)**: Graceful degradation
   - `brave-search`: → skip web search
   - `puppeteer`: → notify limited functionality

### 6.2 Health Check Script
```bash
#!/bin/bash
# tools/scripts/check-mcp-health.sh

check_mcp_server() {
  local server_name=$1
  local test_command=$2
  
  echo "Checking $server_name..."
  
  if timeout 5s $test_command > /dev/null 2>&1; then
    echo "✓ $server_name is healthy"
    return 0
  else
    echo "✗ $server_name is not responding"
    return 1
  fi
}

# Check filesystem server
check_mcp_server "filesystem" "npx -y @modelcontextprotocol/server-filesystem list /"

# Check GitHub server  
check_mcp_server "github" "npx -y @modelcontextprotocol/server-github --test-connection"

# Add to shell profile for automatic checking
# echo 'bash ~/development/tools/scripts/check-mcp-health.sh' >> ~/.zshrc
```

### 6.3 Automatic Recovery
```bash
# Connection failures - restart server
pkill -f "mcp-server-name"
npx -y @modelcontextprotocol/server-name &

# Authentication failures - refresh tokens  
source ~/.zshrc
echo $GITHUB_TOKEN | gh auth login --with-token

# Performance issues - clear cache
rm -rf ~/.mcp/cache/*
~/development/tools/scripts/restart-mcp-servers.sh
```

---

## 7. Performance Optimization

### 7.1 Resource Limits
```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "@package/name"],
      "resources": {
        "maxMemory": "512M",
        "maxCpu": "1.0", 
        "timeout": 30000
      }
    }
  }
}
```

### 7.2 Caching Strategy
```javascript
// tools/mcp-integrations/cache-config.js
module.exports = {
  filesystem: {
    ttl: 60, // seconds
    maxSize: 100 // MB
  },
  github: {
    ttl: 300,
    maxSize: 50
  },
  context7: {
    ttl: 1800, // 30 minutes
    maxSize: 200
  }
};
```

### 7.3 Debug Mode
```bash
# Enable verbose logging
export MCP_DEBUG=true
export MCP_LOG_LEVEL=verbose

# Or per-session
MCP_DEBUG=true claude-code
```

---

## 8. Troubleshooting

### 8.1 Common Issues & Solutions

#### "MCP server not found"
**Problem**: Server appears unregistered or unreachable  
**Solutions**:
```bash
# Check registration
claude mcp list

# Verify installation
npm list -g | grep mcp

# Reinstall if needed
npm install -g @modelcontextprotocol/server-name
```

#### "Authentication failed" 
**Problem**: Invalid or expired API tokens  
**Solutions**:
```bash
# Verify environment variable
echo $GITHUB_TOKEN

# Check token validity (GitHub example)
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user

# Regenerate token if expired
```

#### "Timeout waiting for server"
**Problem**: Server not responding within timeout  
**Solutions**:
```bash
# Check system resources
top # or htop

# Check for port conflicts
lsof -i :PORT

# Increase timeout in configuration
```

#### "HTTP Transport Server Issues" (Vercel, etc.)
**Problem**: Server shows "Needs authentication" or tools don't appear  
**Root Cause**: HTTP servers require different setup than command-based  
**Solutions**:
```bash
# 1. Add server via CLI (not JSON config)
claude mcp add --transport http servername https://server-url

# 2. Set environment variable persistently  
echo 'export SERVER_TOKEN="your_token"' >> ~/.zshrc
source ~/.zshrc

# 3. Verify environment variable
echo $SERVER_TOKEN

# 4. Check server status
claude mcp list

# 5. Restart Claude session
```

#### "Multiple Configuration Files Conflict"
**Problem**: Confusion between mcp.json and mcp-config.json  
**Solution**: Use single source - project-specific `mcp.json` (validated working approach)

#### "Puppeteer Browser Launch Failures"
**Problem**: Chrome/Chromium not found or permission issues  
**Solutions**:
```bash
# Set launch options
export PUPPETEER_LAUNCH_OPTIONS='{"headless": true, "args": ["--no-sandbox"]}'

# Check Chrome installation
which google-chrome-stable

# Install if missing (Ubuntu)
sudo apt install google-chrome-stable
```

### 8.2 Diagnostic Commands
```bash
# Full system check
claude mcp list
env | grep -E "(TOKEN|KEY|ACCESS)"
node --version
npm --version

# Individual server test
claude mcp get <server_name>

# Network connectivity
curl -I https://api.github.com
ping -c 3 supabase.co
```

---

## 9. Advanced Features

### 9.1 Health Check Automation
```bash
# Add to shell profile for startup health check
if [ -f ~/development/tools/scripts/check-mcp-health.sh ]; then
  ~/development/tools/scripts/check-mcp-health.sh
fi
```

### 9.2 Server Prioritization
Configure fallback chains for important servers:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "priority": 2,
      "fallback": "filesystem"
    }
  }
}
```

### 9.3 Custom Server Integration
For specialized needs:
1. Create server following MCP protocol
2. Add to mcp.json configuration
3. Update this guide with new server documentation
4. Add to health monitoring scripts

---

## 10. Contributing New Servers

### 10.1 Process for Adding New Servers
1. **Research & Validate**: Ensure server provides unique value
2. **Install & Test**: Verify functionality in isolation
3. **Configure**: Add to mcp.json with proper environment setup
4. **Document**: Add complete section to this guide
5. **Test Integration**: Verify works with existing servers
6. **Update Related Docs**: Update APOLLO workflow integration if applicable

### 10.2 Documentation Template
```markdown
### X.X New Server Name
- **Identifier**: `server_name`
- **Priority**: [Critical(1)/Important(2)/Optional(3)]
- **Purpose**: Brief description of server capabilities
- **Key Commands**:
  - `command_name`: Description
- **Strategic Use Cases**:
  - **Use Case**: Detailed explanation
- **Environment**: Required environment variables
- **Configuration**: JSON configuration block
- **Related Documentation**: Links to relevant guides
```

### 10.3 Testing Checklist
- [ ] Server installs without errors
- [ ] Environment variables work correctly
- [ ] Key commands function as expected
- [ ] Integrates with existing workflow
- [ ] Health monitoring works
- [ ] Fallback behavior defined
- [ ] Documentation complete
- [ ] No conflicts with existing servers

---

## Related Standards & Documentation

- **[WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md)**: APOLLO 5-phase workflow integration
- **[STANDARDS.md](../../STANDARDS.md)**: Code quality and development standards
- **[SUBAGENT_REGISTRY.md](../workflows/SUBAGENT_REGISTRY.md)**: Complete sub-agent capabilities
- **[TOOLS-OVERVIEW.md](../TOOLS-OVERVIEW.md)**: Master guide to APOLLO toolchain
- **[Gemini.md](../../Gemini.md)**: Strategic partnership protocols
- **[puppeteer-integration-patterns.md](./puppeteer-integration-patterns.md)**: Comprehensive browser automation guide

---

## Change Log
| Version | Date | Editor | Changes |
|---------|------|--------|---------|
| 2.0 | 2025-08-31 | Claude Code | Consolidated three separate MCP files into single comprehensive guide, validated actual configuration approach, resolved conflicts |