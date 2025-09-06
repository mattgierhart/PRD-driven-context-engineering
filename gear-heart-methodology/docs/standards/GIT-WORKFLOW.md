# Standard: Git & GitHub Workflow

Our GitHub workflow is designed for quality, automation, and clarity. It is structured in three distinct layers, from local development to production deployment.

## Layer 1: Local Development & Quality (Your Machine)

This layer is about ensuring code quality *before* it is ever committed.

*   **Tooling**: VS Code's built-in Git UI for staging and commits; Docker, `husky`, and `npm` for testing.
*   **Workflow**:
    1.  Create a feature branch (e.g., `feature/new-login-page`).
    2.  Write code and corresponding tests.
    3.  When you attempt to commit the code, a `pre-commit` hook managed by `husky` automatically triggers.
    4.  This hook runs the `test:docker` script, which executes the entire test suite in a clean, isolated Docker environment.
    5.  **The commit is only created if all tests pass.**

## Layer 2: Collaboration & Review (The GitHub Repository)

This layer is about automated review and verification.

*   **Tooling**: GitHub Pull Requests, Claude Code GitHub App, GitHub Actions.
*   **Workflow**:
    1.  Push your feature branch and open a Pull Request (PR).
    2.  The **Claude Code App** automatically reviews the code for quality, style, and potential bugs, posting comments directly in the PR.
    3.  A **GitHub Actions CI pipeline** (`.github/workflows/ci.yml`) automatically runs the same Dockerized test suite in a neutral cloud environment, reporting a pass/fail status to the PR.

## Layer 3: Deployment & Release (Production)

This layer is about getting approved code to users.

*   **Tooling**: GitHub Actions, Vercel/Supabase deployment integrations.
*   **Workflow**:
    1.  Once the PR has been reviewed and all automated checks are passing, it is merged into the main branch.
    2.  This merge automatically triggers a separate **deployment pipeline** (`.github/workflows/deploy.yml`).
    3.  This pipeline connects to our hosting providers using secure, stored secrets and deploys the new version of the application.

## Branch Protection Rules

To ensure code quality and prevent accidental deployments, configure the following branch protection rules for the `main` branch:

### Required Settings

1. **Require pull request reviews before merging**
   - Dismiss stale pull request approvals when new commits are pushed
   - Require review from CODEOWNERS (when applicable)
   - Required approving reviews: 1 (increase for larger teams)

2. **Require status checks to pass before merging**
   - Require branches to be up to date before merging
   - Required status checks:
     - `test` (from CI workflow)
     - `build` (from CI workflow)
     - `claude-code-review` (when configured)

3. **Require conversation resolution before merging**
   - All PR comments must be resolved

4. **Include administrators**
   - Apply rules even to repository administrators
   - Prevents accidental force pushes

### Recommended Settings

5. **Require signed commits** (for enhanced security)
   - Ensures commit authenticity

6. **Automatically delete head branches**
   - Keeps repository clean after merges

7. **Lock branch** (for critical releases only)
   - Prevents any changes during deployment windows

### GitHub CLI Configuration

```bash
# Configure branch protection via GitHub CLI
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["test","build"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
  --field restrictions=null \
  --field allow_force_pushes=false \
  --field allow_deletions=false
```

### Exceptions and Overrides

For emergency fixes (use sparingly):
1. Create a `hotfix/*` branch
2. Document the emergency in the PR description
3. Get expedited review from senior team member
4. Follow up with proper fix in next sprint
