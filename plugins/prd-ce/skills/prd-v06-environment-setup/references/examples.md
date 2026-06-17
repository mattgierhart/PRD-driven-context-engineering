# Environment Setup Examples

Real-world examples of ENV- specifications for different tech stacks.

---

## Example 1: Node.js/TypeScript Web Application

### ENV-001: Development Environment

**ID**: ENV-001
**Category**: Development Setup
**Status**: Approved | Date: 2026-01-15
**Owner**: Engineering Team

#### CLIs (Global)

```bash
# macOS
brew install mise jq gh ripgrep httpie

# Linux
apt install jq gh ripgrep
curl https://mise.run | sh
```

| Tool | Version | Purpose |
|------|---------|---------|
| `mise` | latest | Version manager for Node.js |
| `jq` | 1.7+ | JSON processing |
| `gh` | 2.x | GitHub CLI for PR workflows |
| `rg` | 14.x | Fast code search |

#### Packages (Per-Project)

```bash
npm install --save-dev \
  typescript \
  eslint \
  prettier \
  @typescript-eslint/parser \
  @typescript-eslint/eslint-plugin \
  jest \
  @types/jest
```

| Package | Purpose |
|---------|---------|
| `typescript` | Type checking |
| `eslint` | Linting |
| `prettier` | Code formatting |
| `jest` | Testing framework |

#### Configuration Files

| File | Purpose |
|------|---------|
| `tsconfig.json` | TypeScript compiler options |
| `.eslintrc.js` | ESLint rules |
| `.prettierrc` | Prettier formatting |
| `jest.config.js` | Test configuration |
| `.mise.toml` | Tool versions |

#### Scripts (package.json)

```json
{
  "scripts": {
    "validate": "npm run lint && npm run typecheck && npm run test",
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "eslint . --ext .ts,.tsx --fix",
    "typecheck": "tsc --noEmit",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "fix": "npm run lint:fix && npm run format",
    "test": "jest",
    "test:watch": "jest --watch",
    "build": "tsc"
  }
}
```

#### Environment Manager (.mise.toml)

```toml
[tools]
node = "20"

[tasks.validate]
run = "npm run validate"
description = "Run all quality checks"

[tasks.fix]
run = "npm run fix"
description = "Auto-fix code issues"
```

#### Verification

```bash
# 1. Verify mise and Node
mise --version
node --version  # Should show v20.x

# 2. Verify project setup
npm install
npm list --dev | head -20

# 3. Verify quality checks
npm run validate

# 4. Verify build
npm run build
```

#### Related IDs

- TECH-001: Next.js framework selection
- TECH-002: TypeScript strict mode decision
- ARC-001: Monolith structure

---

## Example 2: Python Data Science Project

### ENV-001: Development Environment

**ID**: ENV-001
**Category**: Development Setup
**Status**: Approved | Date: 2026-01-15
**Owner**: Data Team

#### CLIs (Global)

```bash
# macOS
brew install mise jq httpie

# Linux
curl https://mise.run | sh
apt install jq
```

| Tool | Version | Purpose |
|------|---------|---------|
| `mise` | latest | Manages Python + tools |
| `jq` | 1.7+ | JSON processing |

#### Packages (Per-Project)

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dev dependencies
pip install -e ".[dev]"
```

**pyproject.toml:**
```toml
[project.optional-dependencies]
dev = [
    "ruff",
    "mypy",
    "pytest",
    "pytest-cov",
    "ipykernel",
]
```

| Package | Purpose |
|---------|---------|
| `ruff` | Fast linting + formatting |
| `mypy` | Type checking |
| `pytest` | Testing framework |
| `pytest-cov` | Coverage reporting |

#### Configuration Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Project config, dependencies |
| `ruff.toml` | Linting rules |
| `.python-version` | Python version (mise) |

#### Scripts (Makefile)

```makefile
.PHONY: validate lint format typecheck test fix

validate: lint typecheck test

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src/

test:
	pytest --cov=src

fix:
	ruff check . --fix
	ruff format .
```

#### Environment Manager (.mise.toml)

```toml
[tools]
python = "3.12"

[tasks.validate]
run = "make validate"
description = "Run all quality checks"

[tasks.fix]
run = "make fix"
description = "Auto-fix code issues"
```

#### Verification

```bash
# 1. Verify Python version
python --version  # Should show 3.12.x

# 2. Verify venv and packages
source .venv/bin/activate
pip list | grep -E "ruff|mypy|pytest"

# 3. Verify quality checks
make validate
```

---

## Example 3: Go Microservice

### ENV-001: Development Environment

**ID**: ENV-001
**Category**: Development Setup
**Status**: Approved | Date: 2026-01-15
**Owner**: Platform Team

#### CLIs (Global)

```bash
# macOS
brew install mise jq gh golangci-lint

# Linux
curl https://mise.run | sh
apt install jq
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

| Tool | Version | Purpose |
|------|---------|---------|
| `mise` | latest | Go version manager |
| `golangci-lint` | 1.55+ | Meta-linter for Go |
| `jq` | 1.7+ | JSON processing |

#### Configuration Files

| File | Purpose |
|------|---------|
| `go.mod` | Module dependencies |
| `.golangci.yml` | Linter configuration |
| `Makefile` | Build/test commands |

#### Scripts (Makefile)

```makefile
.PHONY: validate lint test build fix

validate: lint test

lint:
	golangci-lint run

test:
	go test -v -race -coverprofile=coverage.out ./...

build:
	go build -o bin/app ./cmd/app

fix:
	golangci-lint run --fix
	go fmt ./...
```

#### Verification

```bash
# 1. Verify Go version
go version  # Should show 1.22.x

# 2. Verify dependencies
go mod download
go mod verify

# 3. Verify quality checks
make validate

# 4. Verify build
make build
```

---

## CLI vs MCP Decision Examples

### Example: GitHub Operations

| Operation | CLI | MCP | Decision |
|-----------|-----|-----|----------|
| Create PR | `gh pr create` | GitHub MCP | **CLI** - works in CI |
| List issues | `gh issue list` | GitHub MCP | **CLI** - scriptable |
| View PR diff | `gh pr diff` | GitHub MCP | **CLI** - standard output |

### Example: Database Operations

| Operation | CLI | MCP | Decision |
|-----------|-----|-----|----------|
| Run migrations | `prisma migrate` | None | **CLI** - only option |
| Query data | `psql` / db CLI | DB MCP | **CLI** - works everywhere |
| Generate types | `prisma generate` | None | **CLI** - build step |

### Example: When MCP is Appropriate

| Operation | CLI | MCP | Decision |
|-----------|-----|-----|----------|
| Jira ticket creation | None native | Jira MCP | **MCP** - no CLI available |
| Confluence updates | None native | Confluence MCP | **MCP** - no CLI available |
| Figma design access | None | Figma MCP | **MCP** - visual context needed |

---

## Common Verification Patterns

### Node.js Project

```bash
#!/bin/bash
set -e

echo "=== Verifying Node.js Environment ==="

# 1. Check Node version
echo "Node: $(node --version)"
[[ $(node --version) == v20* ]] || echo "Warning: Expected Node 20.x"

# 2. Check npm packages
npm install
npm list --depth=0

# 3. Run validation
npm run validate

echo "=== Environment verified ==="
```

### Python Project

```bash
#!/bin/bash
set -e

echo "=== Verifying Python Environment ==="

# 1. Check Python version
echo "Python: $(python --version)"

# 2. Check venv
[[ -d .venv ]] || python -m venv .venv
source .venv/bin/activate

# 3. Install and verify
pip install -e ".[dev]"
make validate

echo "=== Environment verified ==="
```

### Go Project

```bash
#!/bin/bash
set -e

echo "=== Verifying Go Environment ==="

# 1. Check Go version
echo "Go: $(go version)"

# 2. Verify modules
go mod download
go mod verify

# 3. Run validation
make validate

echo "=== Environment verified ==="
```
