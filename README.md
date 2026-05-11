# My JDS MCP Server

A personal MCP server for the **Jio Design System (JDS 2.0)**, giving Claude access to:
- JDS design tokens (colors, typography, spacing, border radius, opacity)
- 34 JDS 2.0 component specs
- 71 JDS icons with SVG paths
- JDS asset CDN URLs (fonts, animations, voice states)
- 9 Figma design references
- HTML prototype validator

## Setup

### Step 1 — Update your GitHub username in 2 files

In `knowledge_base.py`, replace line:
```python
CDN_BASE = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/assets"
```
with your actual GitHub username and repo name, e.g.:
```python
CDN_BASE = "https://raw.githubusercontent.com/anand1bhatt/my-jds-mcp/main/assets"
```

In `mcp-config.json`, replace:
```json
"git+https://github.com/YOUR_USERNAME/my-jds-mcp.git"
```
with your actual GitHub URL.

### Step 2 — Push to GitHub

```bash
cd /Users/anand1.bhatt/Documents/my-jds-mcp
git init
git add .
git commit -m "feat: initial JDS MCP server"
git remote add origin https://github.com/YOUR_USERNAME/my-jds-mcp.git
git push -u origin main
```

### Step 3 — Register with Claude Code

Paste this into `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "MyJDS": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/YOUR_USERNAME/my-jds-mcp.git",
        "my-jds-mcp"
      ]
    }
  }
}
```

Then **restart Claude Code**. Your tools appear as `mcp__MyJDS__*`.

### Step 4 — Test locally (optional)

```bash
cd /Users/anand1.bhatt/Documents/my-jds-mcp
pip install mcp
python server.py
```

## Tools

| Tool | What it does |
|------|-------------|
| `find_icon` | Search 71 JDS icons, get SVG path |
| `get_assets` | CDN URLs for fonts, animations, states |
| `get_figma_reference` | Figma node IDs for 9 JDS designs |
| `lookup_component` | JDS 2.0 component specs (34 components) |
| `resolve_token` | JDS tokens — colors, spacing, typography, radius, opacity |
| `validate_prototype` | Lint HTML for JDS compliance |

## Updating JDS 2.0 docs

Drop new/updated `.md` files into:
- `knowledge/Foundation/` — for token/foundation docs
- `knowledge/Component/` — for component specs

The `lookup_component` tool reads these files live — no code changes needed.

## Upgrading

When you update `knowledge_base.py` or `server.py`, just push to GitHub.
Claude will pick up the latest version automatically on next `uvx` run.
