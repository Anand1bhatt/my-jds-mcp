# Spacing & Dimension Scale — OneUI Foundation

## Overview

OneUI uses a **dimension scale** system — all spacing, sizing, and layout values come from the `06 Density` variable collection, which adapts across Default, Compact, and Open density modes.

---

## Base Dimension Scale (Mobile S/360 — Default density)

| Scale Step | Value (px) | Token |
|-----------|-----------|-------|
| 0 | 0 | `Dimension scale/S (360)/[density] 0` |
| 0.5 | 2 | `Dimension scale/S (360)/[density] 0-5` |
| 1 | 4 | `Dimension scale/S (360)/[density] 1` |
| 1.5 | 6 | `Dimension scale/S (360)/[density] 1-5` |
| 2 | 8 | `Dimension scale/S (360)/[density] 2` |
| 2.5 | 10 | `Dimension scale/S (360)/[density] 2-5` |
| 3 | 12 | `Dimension scale/S (360)/[density] 3` |
| 3.5 | 14 | `Dimension scale/S (360)/[density] 3-5` |
| 4 | 16 | `Dimension scale/S (360)/[density] 4` |
| 4.5 | 18 | `Dimension scale/S (360)/[density] 4-5` |
| 5 | 20 | `Dimension scale/S (360)/[density] 5` |
| 5.5 | 22 | `Dimension scale/S (360)/[density] 5-5` |
| 6 | 24 | `Dimension scale/S (360)/[density] 6` |
| 7 | 28 | `Dimension scale/S (360)/[density] 7` |
| 8 | 32 | `Dimension scale/S (360)/[density] 8` |
| 9 | 36 | `Dimension scale/S (360)/[density] 9` |
| 10 | 40 | `Dimension scale/S (360)/[density] 10` |
| 12 | 48 | `Dimension scale/S (360)/[density] 12` |
| 14 | 56 | `Dimension scale/S (360)/[density] 14` |
| 16 | 64 | `Dimension scale/S (360)/[density] 16` |
| 18 | 72 | `Dimension scale/S (360)/[density] 18` |
| 20 | 80 | `Dimension scale/S (360)/[density] 20` |
| 24 | 96 | `Dimension scale/S (360)/[density] 24` |
| 28 | 112 | `Dimension scale/S (360)/[density] 28` |
| 32 | 128 | `Dimension scale/S (360)/[density] 32` |
| 40 | 160 | `Dimension scale/S (360)/[density] 40` |

---

## Grid System

| Breakpoint | Margin | Gutter |
|-----------|--------|--------|
| S — Mobile 360 | 16px | 8px |
| M — Tablet 768 | 24px | 12px |
| M — Tablet 1024 | 36px | 18px |
| L — Laptop 1440 | 45px | 22.5px |
| XL — Desktop 1920 | 50px | 22.5px |

---

## Elevation Shadows

### Level 1 (Cards, tooltips)
| Property | Mobile S Value |
|----------|---------------|
| Key Light Y offset | 4px |
| Key Light blur | 8px |
| Soft Light Y offset | 2px |
| Soft Light blur | 20px |

### Level 2 (Modals, drawers)
| Property | Mobile S Value |
|----------|---------------|
| Key Light Y offset | 6px |
| Key Light blur | 12px |
| Soft Light Y offset | 3px |
| Soft Light blur | 28px |

### Level 3 (Overlays, popovers)
| Property | Mobile S Value |
|----------|---------------|
| Key Light Y offset | 8px |
| Key Light blur | 16px |
| Soft Light Y offset | 4px |
| Soft Light blur | 36px |

---

## Rules

- Never use raw pixel values — always use dimension scale tokens
- All spacing must reference `06 Density` collection tokens
- Use the `07 Platform` collection for responsive font sizing
- Grid margins and gutters scale per breakpoint — always implement responsively
