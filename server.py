"""
DesignXMCP — 6 tools for Jio Design System prototyping.
Two variants in one MCP:
  - DesignXMCP 2.0  → variant="jds2"   (JDS 2.0, 34 components)
  - DesignXMCP OneUI → variant="oneui"  (OneUI DS, 25 components)

Tools:
  1. find_icon          — search 71 JDS icons, returns svg_path
  2. get_assets         — CDN URLs for fonts, animations, icons, states
  3. get_figma_reference— Figma node IDs + URLs (jds2 or oneui refs)
  4. lookup_component   — component specs (jds2 or oneui)
  5. resolve_token      — design tokens (jds2 or oneui)
  6. validate_prototype — lint HTML for JDS/OneUI compliance
"""

import json
import os
import re
import sys
from typing import Any

# MCP SDK — install: pip install mcp
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from knowledge_base import (
    ASSETS, CDN_BASE, FIGMA_REFS, ICONS, JDS_RULES, TOKENS,
    ONEUI_TOKENS, ONEUI_FIGMA_REFS,
)

# ── Load JDS 2.0 component docs from knowledge/ folder ───────────────────────

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "knowledge")
ONEUI_KNOWLEDGE_DIR = os.path.join(KNOWLEDGE_DIR, "OneUI")


def _comp_dir(variant: str) -> str:
    if variant == "oneui":
        return os.path.join(ONEUI_KNOWLEDGE_DIR, "Component")
    return os.path.join(KNOWLEDGE_DIR, "Component")


def _load_component(name: str, variant: str = "jds2") -> str | None:
    """Load a component's markdown spec. variant: 'jds2' or 'oneui'."""
    comp_dir = _comp_dir(variant)
    for fname in os.listdir(comp_dir):
        if fname.lower() == f"{name.lower()}.md":
            with open(os.path.join(comp_dir, fname)) as f:
                return f.read()
    return None


def _list_components(variant: str = "jds2") -> list[str]:
    comp_dir = _comp_dir(variant)
    return sorted(f.replace(".md", "") for f in os.listdir(comp_dir) if f.endswith(".md"))


# ── MCP Server setup ──────────────────────────────────────────────────────────

app = Server("DesignXMCP")

VERSION = "2.0.0"
VARIANT_PARAM = {
    "variant": {
        "type": "string",
        "description": "Design system variant: 'jds2' (DesignXMCP 2.0, default) or 'oneui' (DesignXMCP OneUI)",
        "default": "jds2",
        "enum": ["jds2", "oneui"],
    }
}


# ── Tool 1: find_icon ─────────────────────────────────────────────────────────

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="find_icon",
            description=(
                f"[DesignXMCP v{VERSION}] Search JDS icon library (71 icons). "
                "Returns svg_path for direct inline SVG usage in HTML prototypes. (Icons are shared across both variants.)"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term (e.g. 'calendar', 'mic', 'home')"},
                    "limit": {"type": "number", "description": "Max results (default 10, max 50)", "default": 10},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_assets",
            description=(
                f"[DesignXMCP v{VERSION}] Get JDS asset CDN URLs for prototyping. "
                "Returns GitHub-hosted URLs for fonts (JioType WOFF2), animations (MP4s), "
                "icons (71 JSX), and Voice states (18 MP4s). Call this FIRST in every prototype. (Shared across both variants.)"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "asset_type": {
                        "type": "string",
                        "description": "Asset type: 'all', 'fonts', 'animations', 'icons', 'states'",
                        "default": "all",
                    }
                },
            },
        ),
        Tool(
            name="get_figma_reference",
            description=(
                f"[DesignXMCP v{VERSION}] Get Figma node IDs and URLs. "
                "JDS 2.0: homepage, menu, chat_page, media_page, assistants_page, tools_page, jio_testlab, chat_input. "
                "OneUI: oneui_foundations, oneui_components, oneui_micropatterns."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "design_name": {
                        "type": "string",
                        "description": "Design name (e.g. 'homepage', 'oneui_components')",
                    },
                    **VARIANT_PARAM,
                },
                "required": ["design_name"],
            },
        ),
        Tool(
            name="lookup_component",
            description=(
                f"[DesignXMCP v{VERSION}] Get component specs. "
                "JDS 2.0 (variant='jds2'): 34 components — Button, Card, Input, Tabs, Accordion, Carousel, FAB, Footer, Header, Badge, Toggle, RadioButton, and more. "
                "OneUI (variant='oneui'): 25 components — Button, Avatar, Badge, Input, Checkbox, Chip, Radio, Switch, HeaderNative, BottomNav, TabGroup, ListItem, Pagination, Divider, Spinner, Scrim."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "component_name": {
                        "type": "string",
                        "description": "Component name (e.g. 'Button', 'Avatar', 'bottom-nav')",
                    },
                    **VARIANT_PARAM,
                },
                "required": ["component_name"],
            },
        ),
        Tool(
            name="resolve_token",
            description=(
                f"[DesignXMCP v{VERSION}] Resolve design tokens. "
                "JDS 2.0 categories: colors, typography, spacing, border_radius, opacity. "
                "OneUI categories: colors, typography, spacing, border_radius, opacity, themes, platforms."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "token_category": {
                        "type": "string",
                        "description": "Token category: 'colors', 'typography', 'spacing', 'border_radius', 'opacity'",
                    },
                    "token_name": {
                        "type": "string",
                        "description": "Optional specific token name",
                    },
                    **VARIANT_PARAM,
                },
                "required": ["token_category"],
            },
        ),
        Tool(
            name="validate_prototype",
            description=(
                f"[MyJDS v{VERSION}] Validate an HTML prototype for JDS token compliance. "
                "Scans for hardcoded colors, wrong fonts, raw spacing values, and emoji usage. "
                "Returns violations with JDS token suggestions. Run before dev handoff."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "html_content": {
                        "type": "string",
                        "description": "Complete HTML/CSS content to validate (max 200KB)",
                    },
                    "strict": {
                        "type": "boolean",
                        "description": "If true, also flag warnings for unknown values",
                        "default": False,
                    },
                },
                "required": ["html_content"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:

    # ── find_icon ─────────────────────────────────────────────────────────────
    if name == "find_icon":
        query = arguments["query"].lower()
        limit = min(int(arguments.get("limit", 10)), 50)

        results = []
        for icon_name, icon_data in ICONS.items():
            keywords = icon_data.get("keywords", [])
            name_lower = icon_name.lower()
            score = 0
            if query in name_lower:
                score += 10
            for kw in keywords:
                if query in kw or kw in query:
                    score += 5
            if score > 0:
                results.append((score, icon_name, icon_data))

        results.sort(key=lambda x: -x[0])
        results = results[:limit]

        if not results:
            output = {"found": 0, "query": query, "message": f"No icons found for '{query}'. Try: mic, search, home, calendar, user, menu"}
        else:
            output = {
                "found": len(results),
                "query": query,
                "icons": [
                    {
                        "name": r[1],
                        "keywords": r[2]["keywords"],
                        "viewBox": r[2].get("viewBox", "0 0 24 24"),
                        "svg_path": r[2]["svg_path"],
                        "usage": f'<svg viewBox="{r[2].get("viewBox","0 0 24 24")}" width="24" height="24" fill="currentColor"><path d="{r[2]["svg_path"] if isinstance(r[2]["svg_path"], str) else r[2]["svg_path"][0]}"/></svg>',
                    }
                    for r in results
                ],
            }

        return [TextContent(type="text", text=json.dumps(output, indent=2) + "\n\n---\n" + JDS_RULES)]

    # ── get_assets ────────────────────────────────────────────────────────────
    elif name == "get_assets":
        asset_type = arguments.get("asset_type", "all")

        if asset_type == "all":
            selected = ASSETS
        elif asset_type in ASSETS:
            selected = {asset_type: ASSETS[asset_type]}
        else:
            selected = ASSETS

        # Build full cdn_url for each file
        result = {"cdn_base": CDN_BASE, "types": {}}
        for atype, adata in selected.items():
            entry = dict(adata)
            if "files" in entry and isinstance(entry["files"], list):
                entry["files"] = [
                    {
                        "name": f,
                        "cdn_url": f"{adata['cdn_base']}/{f}",
                    }
                    for f in entry["files"]
                ]
            result["types"][atype] = entry

        result["IMPORTANT"] = (
            "Use cdn_url values DIRECTLY in your HTML src/url() attributes. "
            "No file copying needed."
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2) + "\n\n---\n" + JDS_RULES)]

    # ── get_figma_reference ───────────────────────────────────────────────────
    elif name == "get_figma_reference":
        design_name = arguments["design_name"].lower().strip()
        variant = arguments.get("variant", "jds2").lower()

        if variant == "oneui":
            ref = ONEUI_FIGMA_REFS.get(design_name)
            available = list(ONEUI_FIGMA_REFS.keys())
            source = "DesignXMCP OneUI"
        else:
            ref = FIGMA_REFS.get(design_name)
            available = list(FIGMA_REFS.keys())
            source = "DesignXMCP 2.0"

        if not ref:
            output = {"error": f"Unknown design '{design_name}' in {source}", "available": available}
        else:
            output = {**ref, "variant": variant, "source": source}
        return [TextContent(type="text", text=json.dumps(output, indent=2) + "\n\n---\n" + JDS_RULES)]

    # ── lookup_component ──────────────────────────────────────────────────────
    elif name == "lookup_component":
        component_name = arguments["component_name"].strip()
        variant = arguments.get("variant", "jds2").lower()
        source = "DesignXMCP OneUI" if variant == "oneui" else "DesignXMCP 2.0"

        content = _load_component(component_name, variant)

        if content:
            output = {
                "component": component_name,
                "spec": content,
                "source": source,
                "variant": variant,
            }
        else:
            available = _list_components(variant)
            matches = [c for c in available if component_name.lower() in c.lower()]
            output = {
                "error": f"Component '{component_name}' not found in {source}.",
                "suggestions": matches if matches else available[:10],
                "all_components": available,
                "variant": variant,
            }
        return [TextContent(type="text", text=json.dumps(output, indent=2) + "\n\n---\n" + JDS_RULES)]

    # ── resolve_token ─────────────────────────────────────────────────────────
    elif name == "resolve_token":
        category = arguments["token_category"].lower().strip()
        token_name = arguments.get("token_name", "").strip()
        variant = arguments.get("variant", "jds2").lower()

        token_store = ONEUI_TOKENS if variant == "oneui" else TOKENS
        source = "DesignXMCP OneUI" if variant == "oneui" else "DesignXMCP 2.0"

        if category not in token_store:
            return [TextContent(
                type="text",
                text=json.dumps({"error": f"Unknown category '{category}' in {source}", "available": list(token_store.keys()), "variant": variant})
            )]

        tokens = token_store[category]

        if token_name and isinstance(tokens, dict):
            value = tokens.get(token_name)
            if value:
                output = {"category": category, "token": token_name, "value": value, "source": source, "variant": variant}
            else:
                matches = {k: v for k, v in tokens.items() if token_name.lower() in k.lower()}
                output = {"category": category, "query": token_name, "matches": matches, "all_tokens": tokens, "variant": variant}
        else:
            output = {"category": category, "tokens": tokens, "source": source, "variant": variant}

        return [TextContent(type="text", text=json.dumps(output, indent=2) + "\n\n---\n" + JDS_RULES)]

    # ── validate_prototype ────────────────────────────────────────────────────
    elif name == "validate_prototype":
        html = arguments["html_content"]
        strict = arguments.get("strict", False)

        violations = []

        # 1. Check for non-JioType fonts
        bad_fonts = re.findall(r'font-family\s*:\s*([^;{}\n]+)', html, re.IGNORECASE)
        for font in bad_fonts:
            font_clean = font.strip().strip("'\"")
            if font_clean.lower() not in ("jiotype", "jiotypevars", "jioTypeVar", "jiotype var", "inherit", "initial", "unset"):
                violations.append({
                    "type": "FONT",
                    "severity": "ERROR",
                    "found": font_clean,
                    "fix": "Use font-family: 'JioType' only. Load from CDN via get_assets('fonts').",
                })

        # 2. Check for hardcoded hex colors not in JDS palette
        jds_colors = set(TOKENS["colors"].values())
        found_colors = re.findall(r'#[0-9a-fA-F]{3,8}', html)
        for color in set(found_colors):
            if color.lower() not in {c.lower() for c in jds_colors if isinstance(c, str) and c.startswith("#")}:
                violations.append({
                    "type": "COLOR",
                    "severity": "ERROR",
                    "found": color,
                    "fix": f"Replace with a JDS color token. Common: primary-50=#3535f3, grey-100=#141414, error=#fa2f40, success=#25ab21",
                })

        # 3. Check for emoji used as icons
        emoji_pattern = re.compile(
            "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF"
            "\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF"
            "\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF"
            "☀-⛿✀-➿]+",
            flags=re.UNICODE
        )
        if emoji_pattern.search(html):
            violations.append({
                "type": "EMOJI",
                "severity": "ERROR",
                "found": "Emoji characters detected",
                "fix": "Replace emoji with JDS SVG icons. Use find_icon to get svg_path.",
            })

        # 4. Check for gradient usage
        if "linear-gradient" in html or "radial-gradient" in html:
            violations.append({
                "type": "GRADIENT",
                "severity": "ERROR",
                "found": "CSS gradient detected",
                "fix": "Remove gradients. Use JDS surface tokens for backgrounds.",
            })

        # 5. Check for Material / Heroicons usage
        icon_violations = []
        if "material-icons" in html.lower():
            icon_violations.append("material-icons")
        if "heroicons" in html.lower():
            icon_violations.append("heroicons")
        if "feather" in html.lower() and "icon" in html.lower():
            icon_violations.append("feather-icons")
        if icon_violations:
            violations.append({
                "type": "ICONS",
                "severity": "ERROR",
                "found": f"Non-JDS icon library: {', '.join(icon_violations)}",
                "fix": "Use only JDS SVG icons via find_icon tool.",
            })

        # 6. Strict mode: arbitrary opacity values
        if strict:
            bad_opacity = re.findall(r'opacity\s*:\s*([\d.]+)', html)
            jds_opacities = set(TOKENS["opacity"].values())
            for op in set(bad_opacity):
                if op not in jds_opacities:
                    violations.append({
                        "type": "OPACITY",
                        "severity": "WARNING",
                        "found": f"opacity: {op}",
                        "fix": f"Use JDS opacity tokens: disabled=0.38, text-low=0.65, enabled=1.0",
                    })

        errors = [v for v in violations if v["severity"] == "ERROR"]
        warnings = [v for v in violations if v["severity"] == "WARNING"]
        verdict = "COMPLIANT" if not errors else "NON-COMPLIANT"

        output = {
            "verdict": verdict,
            "errors": len(errors),
            "warnings": len(warnings),
            "violations": violations,
            "summary": (
                f"✅ Prototype is JDS compliant." if verdict == "COMPLIANT"
                else f"❌ {len(errors)} error(s) found. Fix before dev handoff."
            ),
        }
        return [TextContent(type="text", text=json.dumps(output, indent=2))]

    return [TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]


# ── Entry point ───────────────────────────────────────────────────────────────

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
