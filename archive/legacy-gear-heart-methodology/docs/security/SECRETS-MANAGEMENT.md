# Standard: Secrets Management Strategy

To ensure a secure and efficient workflow, we follow a tiered approach to secrets management. This strategy is not optional and must be adhered to for all projects.

**The Golden Rule**: Secrets are **NEVER** committed to the Git repository. All files containing secrets (like `.env.local`) must be included in the `.gitignore` file.

## The Tiered Approach

| Tier | Location | Purpose | Example |
| :--- | :--- | :--- | :--- |
| **1** | `.env.local` (in `.gitignore`) | Local Development | `DATABASE_URL=...` (to Docker), Stripe Test Keys |
| **2** | Vercel/Supabase UI | Production/Staging App | Stripe Live Keys, Production DB connection string |
| **3** | GitHub Repo Secrets | CI/CD Automation | `VERCEL_TOKEN`, `SUPABASE_ACCESS_TOKEN` |
| **4** | Your OS Environment | Agent (Gemini/Claude) Actions | Your personal master API keys |

## Agent Communication Protocol for Secrets

To maintain security, AI agents will **never** ask for or handle secret values directly. Instead, they will provide explicit instructions on where and how you should set the necessary secrets.

*   **For Local Dev:** "The application requires a `STRIPE_SECRET_KEY`. Please add this key with its test value to your `products/{product-name}/.env.local` file."
*   **For Production:** "To deploy successfully, the Vercel project needs the `STRIPE_SECRET_KEY` for the live environment. Please go to your Vercel project's settings and add this environment variable."
*   **For Automation:** "To enable automated deployments, please add a GitHub repository secret named `VERCEL_TOKEN` with your Vercel API token."

## Troubleshooting

### Common Issues

1. **"Environment variable undefined" errors**
   - **Cause**: Missing `.env.local` file or variable not loaded
   - **Solution**:
     ```bash
     # Verify .env.local exists
     ls -la .env.local
     
     # Check variable is defined
     grep "VARIABLE_NAME" .env.local
     
     # Ensure Next.js prefix for client-side vars
     NEXT_PUBLIC_API_URL=...  # Accessible in browser
     SECRET_API_KEY=...       # Server-side only
     ```

2. **Secrets exposed in logs or client bundle**
   - **Detection**:
     ```bash
     # Search for exposed secrets in build
     grep -r "sk_live" .next/
     grep -r "secret" .next/static/
     ```
   - **Prevention**:
     - Never use secrets in client components
     - Use NEXT_PUBLIC_ prefix only for public values
     - Review Vercel function logs for accidental logging

3. **CI/CD pipeline failing with "missing secret"**
   - **Cause**: GitHub Actions can't access repository secrets
   - **Solution**:
     ```yaml
     # In .github/workflows/deploy.yml
     env:
       VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
       # Ensure secret name matches exactly (case-sensitive)
     ```
   - **Verify**: Settings → Secrets → Actions → Check secret exists

4. **Different values between environments**
   - **Debug approach**:
     ```javascript
     // Temporary debug (remove before commit!)
     console.log('Environment:', process.env.NODE_ENV);
     console.log('API URL:', process.env.NEXT_PUBLIC_API_URL);
     ```
   - **Solution**: Use Vercel's environment-specific variables

5. **Tier 4 secrets not available to agents**
   - **Cause**: OS environment variables not exported
   - **Solution**:
     ```bash
     # Add to ~/.zshrc or ~/.bashrc
     export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_..."
     export ANTHROPIC_API_KEY="sk-ant-..."
     
     # Reload shell
     source ~/.zshrc
     
     # Verify
     echo $GITHUB_PERSONAL_ACCESS_TOKEN
     ```

### Security Best Practices

1. **Secret Rotation Schedule**
   - Tier 1 (Dev): No rotation needed
   - Tier 2 (Prod): Every 90 days
   - Tier 3 (CI/CD): Every 180 days
   - Tier 4 (Personal): When compromised

2. **Emergency Response for Exposed Secrets**
   ```bash
   # 1. Immediately revoke the exposed secret
   # 2. Generate new secret
   # 3. Update in all tiers where used
   # 4. Check logs for unauthorized usage
   # 5. Run security audit
   
   # Use git-secrets to prevent future exposure
   brew install git-secrets
   git secrets --install
   git secrets --register-aws  # Or other providers
   ```

3. **Audit Commands**
   ```bash
   # Check for secrets in git history
   git grep -i "secret\|key\|token\|password" $(git rev-list --all)
   
   # Scan with dedicated tools
   npx @secretlint/cli "**/*"
   
   # List all environment variables (careful with output!)
   printenv | grep -E "(KEY|TOKEN|SECRET)" | cut -d= -f1
   ```

### Debugging Tools

```bash
# Verify environment variables are loaded
node -e "console.log(process.env.YOUR_VARIABLE)"

# Check Vercel environment
vercel env ls

# Validate GitHub secrets are accessible
gh secret list

# Test secret masking in CI logs
echo "::add-mask::$SECRET_VALUE"
```
