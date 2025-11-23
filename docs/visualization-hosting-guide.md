# GHM Visualization Suite - Hosting & Distribution Guide

## How Visualization Works

The GHM Visualization Suite generates **static files** that can be viewed anywhere. No server required!

## 📦 What Gets Generated

```
docs/generated/
├── id-graph.svg          # Static SVG graph (view in browser or image viewer)
├── id-graph.dot          # Graphviz DOT source (for debugging)
├── id-graph-data.json    # Parsed ID data (for programmatic access)
├── index.md              # Index page with links and instructions
└── .provenance           # Build metadata (git SHA, config hash)
```

## 🌐 Hosting Options

### **Option 1: GitHub-Native (Recommended - FREE!)**

The visualizations are **already hosted** when you push to GitHub:

```bash
# After generating visualizations
git add docs/generated/
git commit -m "Add ID visualizations"
git push

# View on GitHub:
# https://github.com/YOUR_USERNAME/YOUR_REPO/blob/main/docs/generated/id-graph.svg
```

**Pros:**
- ✅ No domain needed
- ✅ No setup required
- ✅ Version controlled (see history)
- ✅ Rendered inline in README

**Cons:**
- ⚠️ GitHub may not render very large SVGs (>1MB)

### **Option 2: GitHub Pages (FREE, with URL)**

Serve as a website at `https://username.github.io/repo-name/`

**Setup (one-time):**
```bash
# 1. Enable GitHub Pages in repo settings:
#    Settings → Pages → Source: main branch → /docs folder

# 2. Add index.html to docs/
cat > docs/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>GHM Visualizations</title></head>
<body>
  <h1>GHM ID Knowledge Graph</h1>
  <img src="generated/id-graph.svg" alt="ID Graph" style="width:100%">
  <hr>
  <a href="generated/index.md">View Index</a>
</body>
</html>
EOF

git add docs/index.html
git commit -m "Add GitHub Pages index"
git push
```

**Access:** `https://yourusername.github.io/yourrepo/`

**Pros:**
- ✅ Free GitHub subdomain
- ✅ Automatic deployment on push
- ✅ Can add custom domain if desired

**Cons:**
- ⚠️ Public only (unless you have GitHub Enterprise)

### **Option 3: Local Viewing (No Internet Needed)**

Just open the files directly:

```bash
# macOS
open docs/generated/id-graph.svg

# Linux
xdg-open docs/generated/id-graph.svg

# Windows
start docs/generated/id-graph.svg
```

**Or use a local HTTP server:**
```bash
cd docs
python -m http.server 8000
# Visit: http://localhost:8000/generated/id-graph.svg
```

**Pros:**
- ✅ Works offline
- ✅ No setup
- ✅ Private

**Cons:**
- ⚠️ Not shareable via URL

### **Option 4: Custom Domain (Optional)**

If you want a custom domain like `viz.yourstartup.com`:

1. **Use GitHub Pages** (free hosting) + custom domain
2. **Use Netlify/Vercel** (deploy from GitHub, free tier)
3. **Use your own server** (copy SVG files to web root)

**You DON'T need this** - GitHub Pages gives you `username.github.io/repo` for free.

## 🎨 Embedding in Documentation

### In README.md (GitHub)
```markdown
## ID Knowledge Graph

![ID Graph](docs/generated/id-graph.svg)

See [full index](docs/generated/index.md) for details.
```

### In Notion/Confluence
1. Export SVG from GitHub
2. Upload as image
3. Link to GitHub for latest version

### In Presentations
1. Export SVG as PNG: `convert id-graph.svg id-graph.png`
2. Insert PNG in slides
3. Regenerate when IDs change

## 🔄 Workflow: Generate → Commit → View

```bash
# Developer workflow
python tools/generate-visuals.py --all   # Generate
git add docs/generated/                  # Stage
git commit -m "Update visualizations"    # Commit
git push                                 # Push

# View options:
# 1. GitHub: https://github.com/user/repo/blob/main/docs/generated/id-graph.svg
# 2. GitHub Pages: https://user.github.io/repo/generated/id-graph.svg
# 3. Local: open docs/generated/id-graph.svg
```

## 📱 Sharing with Non-Technical Stakeholders

### **Best Option: GitHub Pages**

Send them a simple URL: `https://yourusername.github.io/yourrepo/`

They see the graph in their browser. No GitHub account needed.

### **Alternative: Screenshot**

For slide decks or Slack:
```bash
# Convert SVG to PNG (requires ImageMagick)
convert docs/generated/id-graph.svg docs/generated/id-graph.png

# Or use online converter: cloudconvert.com
```

## 💰 Cost Comparison

| Option | Cost | Setup Time | Use Case |
|--------|------|------------|----------|
| GitHub blob view | FREE | 0 min | Quick sharing via GitHub |
| GitHub Pages | FREE | 5 min | Public website |
| Netlify/Vercel | FREE | 10 min | Custom domain + preview deploys |
| Local viewing | FREE | 0 min | Offline/private use |
| Custom hosting | $5-20/mo | 30-60 min | Full control, private repos |

## 🎯 Recommended Setup

**For most users:**
1. Generate locally: `python tools/generate-visuals.py --all`
2. Commit to repo: `git add docs/generated/ && git commit && git push`
3. View on GitHub: Share URL to `docs/generated/id-graph.svg`

**For teams:**
1. Enable GitHub Pages (one-time, 5 minutes)
2. Add visualization generation to CI/CD (auto-update on PR merge)
3. Share permanent URL: `https://company.github.io/product-repo/`

**For presentations:**
1. Export SVG → PNG
2. Insert in slides
3. Regenerate before each demo

## 🚀 Future: Interactive HTML Dashboard (Phase 3)

When we add D3.js interactive graphs (Phase 3), you'll get:
- Clickable nodes → jump to SoT file
- Zoom and pan
- Filter by ID type
- Search functionality

This will be a single `id-graph.html` file you can:
- Open locally (double-click)
- Host on GitHub Pages
- Embed in internal wiki

Still **no server required** - just static HTML + JavaScript.

---

## TL;DR

**Do I need a domain?** NO! ✅

**What's the easiest way to share?**
1. Push SVG to GitHub → share GitHub URL (free)
2. OR enable GitHub Pages → share `username.github.io/repo` (free)

**Can I keep it private?** YES!
- Private repos on GitHub (visualizations only visible to collaborators)
- Local viewing only (don't push to GitHub)
- Self-hosted on internal network

**Cost:** $0 for 99% of use cases 💸
