# Typography — OneUI Foundation

## Overview

OneUI typography uses **JioType Var** (variable font) as the primary typeface, with **JetBrains Mono** for code. The type scale is responsive — font sizes adapt per platform breakpoint via the `07 Platform` variable collection.

---

## Font Families

| Role | Family | Token |
|------|--------|-------|
| Default (all UI) | `JioType Var` | `Jio/Font Family/[language] Font Family [Default]` |
| Code / monospace | `JetBrains Mono` | `Jio/Font Family/[language] Font Family [code]` |

---

## Type Scale

### Display
| Style | Weight | Token |
|-------|--------|-------|
| Display L | 900 (Black) | `Typography/Fontsize/Display/[platform] L` |
| Display M | 900 (Black) | `Typography/Fontsize/Display/[platform] M` |
| Display S | 900 (Black) | `Typography/Fontsize/Display/[platform] S` |

### Headline
| Style | Weight | Token |
|-------|--------|-------|
| Headline L | 900 (Black) | `Typography/Fontsize/Headline/[platform] L` |
| Headline M | 850 | `Typography/Fontsize/Headline/[platform] M` |
| Headline S | 850 | `Typography/Fontsize/Headline/[platform] S` |

### Title
| Style | Weight | Token |
|-------|--------|-------|
| Title L | 800 | `Typography/Fontsize/Title/[platform] L` |
| Title M | 750 | `Typography/Fontsize/Title/[platform] M` |
| Title S | 750 | `Typography/Fontsize/Title/[platform] S` |

### System (Label/Body combined)
| Style | Token |
|-------|-------|
| System XL | `Typography/Fontsize/System/[platform] XL` |
| System L | `Typography/Fontsize/System/[platform] L` |
| System M | `Typography/Fontsize/System/[platform] M` |
| System S | `Typography/Fontsize/System/[platform] S` |
| System XS | `Typography/Fontsize/System/[platform] XS` |
| System 2XS | `Typography/Fontsize/System/[platform] 2XS` |
| System 3XS | `Typography/Fontsize/System/[platform] 3XS` |

### Label
| Weight | Token Value |
|--------|-------------|
| Label High (Bold) | 700 |
| Label Medium | 500 |
| Label Low (Regular) | 400 |

### Body
| Weight | Token Value |
|--------|-------------|
| Body High (Bold) | 700 |
| Body Medium | 500 |
| Body Low (Regular) | 400 |

---

## Platform Breakpoints

The `07 Platform` collection applies responsive font sizes:

| Mode | Breakpoint |
|------|-----------|
| S [Mobile 360] | 360px |
| M [Tablet portrait 768] | 768px |
| M [Tablet landscape 1024] | 1024px |
| L [Laptop 1440] | 1440px |
| L [Desktop 1920] | 1920px |

---

## Density Variants

The `06 Density` collection adjusts spacing/sizing:

| Mode | Usage |
|------|-------|
| Default | Standard UI density |
| Compact | Tighter spacing |
| Open | More breathing room |

---

## Line Heights

Line heights are defined per style via the `Jio/Line Height/` token group:
- Display: `Jio/Line Height/Display/[language] Display L/M/S`
- Headline: `Jio/Line Height/Headline/[language] Headline L/M/S`
- Title: `Jio/Line Height/Title/[language] Title L/M/S`
- Label: `Jio/Line Height/Label/[language] Label L/M/S/XS/2XS/3XS`
- Body: `Jio/Line Height/Body/[language] Body L/M/S/XS/2XS`
- Code: `Jio/Line Height/Code/[language] Code M/S/XS/2XS/3XS`

---

## Rules

- **Only** use `JioType Var` for UI text — never system fonts
- Use `JetBrains Mono` for code blocks only
- Always bind font size to the `07 Platform` responsive tokens
- Font weights are numeric (400–900) via variable font axis
