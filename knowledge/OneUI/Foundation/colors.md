# Colors — OneUI Foundation

## Overview

OneUI uses a semantic color system built on top of primitive palettes. Colors are organized by **colour mode** (Light/Dark), **surface context**, and **appearance role**. Multi-theme support: MyJio, JioHome, JioFinance, JioMart, JioPowerSight.

---

## Semantic Color Roles

| Role | Token | Light Value | Usage |
|------|-------|------------|-------|
| Surface FG Minimal | `grey/surface/fg-minimal` | `#afb1b6` | Subtle foreground elements |
| Surface FG Subtle | `grey/surface/fg-subtle` | `#afb1b6` | Secondary foreground |
| On Default Medium [t] | `grey/on-default/medium-t` | `#0c0d10` | Primary text on default surface |
| On Default Low [t] | `grey/on-default/low-t` | `#0c0d10` | Secondary text on default surface |
| On Default Medium [s] | `grey/on-default/medium-s` | `#afb1b6` | Solid medium on default |
| On Default Low [s] | `grey/on-default/low-s` | `#afb1b6` | Solid low on default |
| On Bold Medium [t] | `grey/on-bold/medium-t` | `#ffffff` | Text on bold/filled surfaces |
| On Bold Low [t] | `grey/on-bold/low-t` | `#ffffff` | Secondary text on bold |
| On Bold Medium [s] | `grey/on-bold/medium-s` | `#696d76` | Solid medium on bold |

---

## Indigo Palette (Primary Brand)

| Token | Light Value | Usage |
|-------|------------|-------|
| `indigo/surface/fg-minimal` | `#a3a7ff` | Primary accent foreground |
| `indigo/surface/fg-subtle` | `#a3a7ff` | Subtle accent |
| `indigo/on-subtle/medium-t` | `#0b0034` | Text on indigo subtle bg |
| `indigo/on-subtle/medium-s` | `#8e90ff` | Solid on indigo subtle |
| `indigo/on-default/medium-s` | `#a3a7ff` | Indigo accent on default |
| `indigo/on-bold/medium-t` | `#ffffff` | Text on filled indigo |
| `indigo/on-bold/medium-s` | `#8584fc` | Solid on filled indigo |

---

## Saffron Palette (Secondary/Accent)

| Token | Light Value | Usage |
|-------|------------|-------|
| `saffron/surface/fg-minimal` | `#ff885a` | Warm accent foreground |
| `saffron/surface/fg-subtle` | `#ff885a` | Subtle warm accent |
| `saffron/on-subtle/medium-s` | `#ff671f` | Solid on saffron subtle |

---

## Theme Colors

OneUI supports 5 product themes. Switch by setting the `09 Theme` variable collection mode:

| Theme | Mode Name |
|-------|-----------|
| MyJio | `MyJio` |
| JioHome | `JioHome` |
| JioFinance | `JioFinance` |
| JioMart | `JioMart` |
| JioPowerSight | `JioPowerSight` |

Theme tokens follow the pattern: `Jio/Colours/[Theme] surface`, `[Theme] high`, `[Theme] tinted`, etc.

---

## Semantic Appearance Roles

| Role | Description |
|------|-------------|
| `surface` | Background fill for containers |
| `high` | Primary/prominent brand color |
| `medium [t]` | Translucent medium emphasis |
| `low [t]` | Translucent low emphasis |
| `medium [s]` | Solid medium emphasis |
| `low [s]` | Solid low emphasis |
| `tinted` | Brand-tinted surface |
| `tinted a11y` | Accessible brand-tinted |
| `state layer` | Hover/press overlay |
| `focus ring` | Keyboard focus indicator |

---

## Colour Mode

All tokens have Light and Dark variants. Always use semantic tokens — never hardcode hex values. The `05 Colour Mode` collection switches all semantic tokens between Light and Dark.

---

## Rules

- Never hardcode hex colors
- Always use semantic tokens from the `05 Colour Mode` or `09 Theme` collections
- Surface colors: `surface`, `tinted`
- Text colors: `on default`, `on subtle`, `on bold`
- Interactive states use `state layer` tokens for hover/press overlays
