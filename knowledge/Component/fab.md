# FAB (Floating Action Button) — JDS Component Style Guide

## Overview

A **Floating Action Button (FAB)** is a prominent, fixed-position button that represents the primary or most-used action on a screen. It floats above the content layer, always remaining visible and accessible to the user regardless of scroll position.

FABs exist in two structural forms:
- **Standard FAB** — icon-only, circular
- **Extended FAB** — icon + label text, pill shape (can collapse to icon-only on scroll)

The component lives in `/src/app/components/ui/fab.tsx`.

All styling uses JDS design tokens from `/src/styles/theme.css`.
Typography uses JioType exclusively per typography.md.
Icons use `fill="currentColor"` per icon.md.

---

## Typography Rules (MANDATORY)

> **ALL text in FAB components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (FAB)

| Token                  | Value | Usage                                      |
| ---------------------- | ----- | ------------------------------------------ |
| `--font-weight-bold`   | 700   | Extended FAB label text (all sizes)        |

- FAB labels always use `var(--font-weight-bold)` (700), consistent with button.md.
- **Never** use arbitrary `font-weight` values or Tailwind font-weight utilities.

### Permitted Sizes (FAB)

| Token                 | Value | Usage                                         |
| --------------------- | ----- | --------------------------------------------- |
| `--text-button`       | 16px  | Extended FAB label (default and small sizes)  |
| `--text-button-large` | 18px  | Extended FAB label (large size)               |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Anatomy

### Standard FAB (Icon-Only)

```
           ╭──────────╮
           │          │
           │    ✏️    │   ← Icon (24px default / 20px small / 36px large)
           │          │
           ╰──────────╯
           ↑
      Circular container
      Floating with shadow
```

### Extended FAB (Icon + Label)

```
   ╭────────────────────────────╮
   │                            │
   │   ✏️   Label Text          │   ← Icon (24px) + Label
   │                            │
   ╰────────────────────────────╯
   ↑
   Pill container (auto-width)
   Floating with shadow
```

### Elements

1. **Container** (Required)
   - Circular (Standard FAB) or pill (Extended FAB)
   - Elevated above content with drop shadow
   - Fixed positioned (bottom-right by default)

2. **Icon** (Required)
   - Centered inside the container
   - Uses `fill="currentColor"` per icon.md
   - Scales with FAB size

3. **Label** (Extended FAB only)
   - Positioned to the right of the icon
   - Uses `var(--font-family-jiotype)`, `var(--font-weight-bold)`
   - Animates in/out when FAB expands/collapses

4. **Badge** (Optional overlay)
   - Notification count badge on the top-right of the FAB
   - Uses Badge component per badge.md

---

## Variants

### 1. Primary FAB

The default FAB color scheme. Uses the primary brand color.

```
Background:       var(--primary-50)            → #0F3CC9
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
```

**Usage:**
```tsx
<FAB variant="primary" icon={<IcEdit fill="currentColor" />} aria-label="Create new" />
```

---

### 2. Surface FAB

For use on primary-colored or image backgrounds where a white surface is needed for contrast.

```
Background:       var(--primary-background)    → #FFFFFF
Icon Color:       var(--primary-50)            → #0F3CC9
Label Color:      var(--primary-50)            → #0F3CC9
```

**Usage:**
```tsx
<FAB variant="surface" icon={<IcEdit fill="currentColor" />} aria-label="Create new" />
```

---

### 3. Secondary FAB

For secondary actions that require a floating button. Uses secondary brand color.

```
Background:       var(--secondary-50)          → #000093
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
```

**Usage:**
```tsx
<FAB variant="secondary" icon={<IcShare fill="currentColor" />} aria-label="Share" />
```

---

### 4. Tertiary FAB

A low-emphasis floating button for supplementary actions. Uses a subtle background.

```
Background:       var(--grey-20)               → #F5F5F5
Icon Color:       var(--primary-60)            → #0A2885
Label Color:      var(--primary-60)            → #0A2885
```

**Usage:**
```tsx
<FAB variant="tertiary" icon={<IcFilter fill="currentColor" />} aria-label="Filter" />
```

---

### Standard FAB vs. Extended FAB

| Feature              | Standard FAB                     | Extended FAB                         |
| -------------------- | -------------------------------- | ------------------------------------ |
| Shape                | Circle                           | Pill (auto-width)                    |
| Content              | Icon only                        | Icon + Label text                    |
| Radius               | `var(--radius-full)` → 9999px    | `var(--radius-button)` → 250px       |
| Min Width            | Equal to height (square)         | `var(--space-20)` + content → ≥ 80px |
| Collapses on scroll  | No                               | Yes (to icon-only, optional)         |
| Use case             | Simple action (edit, add, share) | Labeled action needing clarity       |

---

## Sizes

### Small FAB

```
Size (WxH):         40px × 40px
Icon Size:          20px × 20px
Border Radius:      var(--radius-full)          → 9999px
Padding:            var(--space-2)              → 8px
```

### Default / Medium FAB (Standard)

```
Size (WxH):         56px × 56px
Icon Size:          24px × 24px
Border Radius:      var(--radius-full)          → 9999px
Padding:            var(--space-4)              → 16px
```

### Large FAB

```
Size (WxH):         96px × 96px
Icon Size:          36px × 36px
Border Radius:      var(--radius-full)          → 9999px
Padding:            var(--space-8)              → 32px
```

### Extended FAB — Sizes

| Size    | Height | Padding H       | Padding V      | Icon Size | Font Token            |
| ------- | ------ | --------------- | -------------- | --------- | --------------------- |
| Small   | 40px   | `var(--space-4)` → 16px | `var(--space-2)` → 8px  | 20×20px | `--text-button` → 16px |
| Default | 56px   | `var(--space-6)` → 24px | `var(--space-4)` → 16px | 24×24px | `--text-button` → 16px |
| Large   | 72px   | `var(--space-8)` → 32px | `var(--space-5)` → 20px | 28×28px | `--text-button-large` → 18px |

### Extended FAB — Internal Gap (Icon to Label)

```
Gap (Icon to Label):  var(--space-3)            → 12px
```

---

## Size × Variant Matrix

| Size    | Standard Radius       | Extended Radius         | Height  |
| ------- | --------------------- | ----------------------- | ------- |
| Small   | `--radius-full` (9999px) | `--radius-button` (250px) | 40px  |
| Default | `--radius-full` (9999px) | `--radius-button` (250px) | 56px  |
| Large   | `--radius-full` (9999px) | `--radius-button` (250px) | 96px (standard) / 72px (extended) |

---

## States

### Disabled State (All Variants — MANDATORY)

The disabled state preserves the **same visual aspect as the Normal state** and applies a **general opacity of 30%** over the entire FAB. No color or layout changes — only reduced opacity.

```
pointer-events:   none
opacity:          0.3                           → 30% (MANDATORY)
```

> **MANDATORY:** Disabled FABs must use `opacity: 0.3` (30%). This is consistent with button.md. Never change colors for disabled state — only reduce opacity.

---

### Primary FAB States

#### 1. Normal

```
Background:       var(--primary-50)            → #0F3CC9
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
```

#### 2. Hover

```
Background:       var(--primary-40)            → #6789F4
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
Transition:       background-color 0.2s ease
```

#### 3. Pressed / Active

```
Background:       var(--primary-60)            → #0A2885
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-sm)        → 0 4px 12px #0000004d
Transform:        scale(0.97)
Transition:       background-color 0.1s ease, transform 0.1s ease
```

#### 4. Focused (Keyboard)

```
Background:       var(--primary-50)            → #0F3CC9  (same as Normal)
Icon Color:       var(--primary-inverse)       → #FFFFFF
Outline:          var(--border-width-thick) solid var(--primary-60)  → 2px solid #0A2885
Outline Offset:   var(--space-1)              → 4px
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
```

#### 5. Disabled

```
Background:       var(--primary-50)            → #0F3CC9  (same as Normal)
Icon Color:       var(--primary-inverse)       → #FFFFFF
Opacity:          0.3                          → 30% (MANDATORY)
Pointer Events:   none
```

---

### Surface FAB States

#### 1. Normal

```
Background:       var(--primary-background)    → #FFFFFF
Icon Color:       var(--primary-50)            → #0F3CC9
Label Color:      var(--primary-50)            → #0F3CC9
Border:           var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
```

#### 2. Hover

```
Background:       var(--grey-20)               → #F5F5F5
Icon Color:       var(--primary-50)            → #0F3CC9
Label Color:      var(--primary-50)            → #0F3CC9
Border:           var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
Transition:       background-color 0.2s ease
```

#### 3. Pressed / Active

```
Background:       var(--primary-20)            → #E7EBF8
Icon Color:       var(--primary-60)            → #0A2885
Label Color:      var(--primary-60)            → #0A2885
Border:           var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Shadow:           var(--shadow-card-sm)        → 0 4px 12px #0000004d
Transform:        scale(0.97)
```

#### 4. Focused (Keyboard)

```
Background:       var(--primary-background)    → #FFFFFF  (same as Normal)
Outline:          var(--border-width-thick) solid var(--primary-50)  → 2px solid #0F3CC9
Outline Offset:   var(--space-1)              → 4px
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
```

#### 5. Disabled

```
Background:       var(--primary-background)    → #FFFFFF  (same as Normal)
Opacity:          0.3                          → 30% (MANDATORY)
Pointer Events:   none
```

---

### Secondary FAB States

#### 1. Normal

```
Background:       var(--secondary-50)          → #000093
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
```

#### 2. Hover

```
Background:       var(--secondary-40)          → #3535F3
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-md)        → 0 4px 16px #00000033
Transition:       background-color 0.2s ease
```

#### 3. Pressed / Active

```
Background:       var(--secondary-60)          → #000067
Icon Color:       var(--primary-inverse)       → #FFFFFF
Label Color:      var(--primary-inverse)       → #FFFFFF
Shadow:           var(--shadow-card-sm)        → 0 4px 12px #0000004d
Transform:        scale(0.97)
```

#### 4. Focused (Keyboard)

```
Background:       var(--secondary-50)          → #000093  (same as Normal)
Outline:          var(--border-width-thick) solid var(--secondary-40)  → 2px solid #3535F3
Outline Offset:   var(--space-1)              → 4px
```

#### 5. Disabled

```
Background:       var(--secondary-50)          → #000093  (same as Normal)
Opacity:          0.3                          → 30% (MANDATORY)
Pointer Events:   none
```

---

### Tertiary FAB States

#### 1. Normal

```
Background:       var(--grey-20)               → #F5F5F5
Icon Color:       var(--primary-60)            → #0A2885
Label Color:      var(--primary-60)            → #0A2885
Shadow:           var(--shadow-card)           → 0 4px 16px #0000001a
```

#### 2. Hover

```
Background:       var(--grey-40)               → #E0E0E0
Icon Color:       var(--primary-60)            → #0A2885
Label Color:      var(--primary-60)            → #0A2885
Shadow:           var(--shadow-card)           → 0 4px 16px #0000001a
Transition:       background-color 0.2s ease
```

#### 3. Pressed / Active

```
Background:       var(--grey-60)               → #B5B5B5
Icon Color:       var(--primary-70)            → #061951
Label Color:      var(--primary-70)            → #061951
Shadow:           var(--shadow-card-sm)        → 0 4px 12px #0000004d
Transform:        scale(0.97)
```

#### 4. Focused (Keyboard)

```
Background:       var(--grey-20)               → #F5F5F5  (same as Normal)
Outline:          var(--border-width-thick) solid var(--primary-60)  → 2px solid #0A2885
Outline Offset:   var(--space-1)              → 4px
```

#### 5. Disabled

```
Background:       var(--grey-20)               → #F5F5F5  (same as Normal)
Opacity:          0.3                          → 30% (MANDATORY)
Pointer Events:   none
```

---

## Positioning

### Default Position

```
Position:         fixed
Bottom:           var(--space-6)              → 24px
Right:            var(--space-6)              → 24px
z-index:          Floating layer (above content, below modals/dialogs)
```

### Responsive Positioning

```
Mobile (< 620px):
  Bottom:         var(--space-6)              → 24px
  Right:          var(--space-4)              → 16px

Tablet (≥ 620px):
  Bottom:         var(--space-6)              → 24px
  Right:          var(--space-6)              → 24px

Desktop (≥ 992px):
  Bottom:         var(--space-8)              → 32px
  Right:          var(--space-8)              → 32px
```

### Position Variants

| Variant           | Bottom                | Right / Left                 | Notes                        |
| ----------------- | --------------------- | ---------------------------- | ---------------------------- |
| Bottom-right      | `var(--space-6)`      | Right: `var(--space-6)`      | Default                      |
| Bottom-left       | `var(--space-6)`      | Left: `var(--space-6)`       | For RTL or specific layouts  |
| Bottom-center     | `var(--space-6)`      | Left: 50%, transform: -50%   | For full-width experiences   |
| Above-nav         | `var(--space-20)`     | Right: `var(--space-6)`      | When bottom nav bar present  |

### Offset for Navigation Bar

When a bottom navigation bar or tab bar is present, the FAB must be offset above it:

```
Bottom offset:    var(--space-20)             → 80px
  (accounts for ~56px nav bar + var(--space-6) spacing gap)
```

---

## Elevation / Shadow

FABs are always elevated above content. Shadow communicates this elevation.

| State         | Shadow Token           | Value                              |
| ------------- | ---------------------- | ---------------------------------- |
| Normal        | `--shadow-card-md`     | `0 4px 16px var(--overlay-soft)`   |
| Hover         | `--shadow-card-md`     | `0 4px 16px var(--overlay-soft)`   |
| Pressed       | `--shadow-card-sm`     | `0 4px 12px var(--overlay-dim)`    |
| Focused       | `--shadow-card-md`     | `0 4px 16px var(--overlay-soft)`   |
| Disabled      | `--shadow-card`        | `0 4px 16px var(--overlay-faint)`  |

---

## Extended FAB — Expand / Collapse Behaviour

An extended FAB can optionally collapse to a standard (icon-only) FAB when the user scrolls down, and re-expand when the user scrolls back to the top.

### Collapsed State (scroll down)

```
Width:            Same as Standard FAB (56px default)
Label:            Hidden (opacity: 0, width: 0, overflow: hidden)
Icon:             Centered
Border Radius:    var(--radius-full)           → 9999px
Transition:       width 0.3s ease, border-radius 0.3s ease, opacity 0.2s ease
```

### Expanded State (scroll up / default)

```
Width:            Auto (content-driven, min-width enforced)
Label:            Visible (opacity: 1, width: auto)
Icon:             Left-aligned (with padding)
Border Radius:    var(--radius-button)         → 250px
Transition:       width 0.3s ease, border-radius 0.3s ease, opacity 0.2s ease
```

### Minimum Width (Extended FAB)

```
Min Width:        var(--space-20)              → 80px
  (ensures the label has room before collapsing)
```

---

## Container Awareness

### On Light Backgrounds

Use **Primary FAB** or **Secondary FAB** for maximum contrast against white/light surfaces.

```
Recommended variant:  primary
Background context:   var(--primary-background), var(--grey-20)
```

### On Dark / Primary-Colored Backgrounds

Use **Surface FAB** for maximum contrast against dark or brand-colored surfaces.

```
Recommended variant:  surface
Background context:   var(--primary-50), var(--primary-60), image overlays
```

### On Image / Media Backgrounds

Use **Surface FAB** with the border to ensure contrast.

```
Recommended variant:  surface
FAB border:           var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
```

---

## Multiple FABs

When multiple FABs are needed on a single screen:

```
┌─────────────────────────┐
│                         │
│                    [🔔] │  ← Secondary action FAB (smaller, surface variant)
│                    [✏️] │  ← Primary action FAB (default size, primary variant)
└─────────────────────────┘
```

### Stacking Rules

```
Gap between FABs:   var(--space-4)            → 16px
Order:              Primary action at bottom-right, secondary above
Size relationship:  Secondary FAB should be smaller (small size) if different variant
```

### Maximum FABs Per Screen

- **Recommended**: 1 FAB per screen
- **Maximum**: 2 FABs per screen (1 standard + 1 small secondary)
- **Never** show more than 2 FABs simultaneously

---

## FAB + Snackbar / Toast Interaction

When a Snackbar or Toast notification appears at the bottom of the screen, the FAB must animate upward to avoid overlap.

```
Normal bottom:      var(--space-6)             → 24px
Offset (snackbar):  var(--space-6) + snackbar-height + var(--space-3)
  → approx. 24px + 48px + 12px = 84px
Transition:         bottom 0.3s ease-out
```

---

## Badge Integration

An optional notification badge can be overlaid on the FAB's top-right corner.

```
Badge Position:     Top-right (overlay placement per badge.md)
Badge Elevation:    +1 from FAB (above FAB surface)
Badge Variant:      Notification / dot or numeric (per badge.md)
Badge Offset:       Slightly outside the FAB container edge
```

```tsx
<FAB variant="primary" aria-label="Notifications">
  <IcNotification fill="currentColor" />
  <Badge
    badgeColorScheme="error"
    badgeEmphasis="high"
    placement="overlay"
  >
    5
  </Badge>
</FAB>
```

---

## Colors — Full Reference

### Primary FAB

| State    | Background Token      | Icon / Label Token      |
| -------- | --------------------- | ----------------------- |
| Normal   | `--primary-50`        | `--primary-inverse`     |
| Hover    | `--primary-40`        | `--primary-inverse`     |
| Pressed  | `--primary-60`        | `--primary-inverse`     |
| Focused  | `--primary-50`        | `--primary-inverse`     |
| Disabled | `--primary-50`        | `--primary-inverse`     |

### Surface FAB

| State    | Background Token       | Icon / Label Token  | Border Token |
| -------- | ---------------------- | ------------------- | ------------ |
| Normal   | `--primary-background` | `--primary-50`      | `--grey-40`  |
| Hover    | `--grey-20`            | `--primary-50`      | `--grey-40`  |
| Pressed  | `--primary-20`         | `--primary-60`      | `--grey-40`  |
| Focused  | `--primary-background` | `--primary-50`      | `--grey-40`  |
| Disabled | `--primary-background` | `--primary-50`      | `--grey-40`  |

### Secondary FAB

| State    | Background Token   | Icon / Label Token  |
| -------- | ------------------ | ------------------- |
| Normal   | `--secondary-50`   | `--primary-inverse` |
| Hover    | `--secondary-40`   | `--primary-inverse` |
| Pressed  | `--secondary-60`   | `--primary-inverse` |
| Focused  | `--secondary-50`   | `--primary-inverse` |
| Disabled | `--secondary-50`   | `--primary-inverse` |

### Tertiary FAB

| State    | Background Token | Icon / Label Token |
| -------- | ---------------- | ------------------ |
| Normal   | `--grey-20`      | `--primary-60`     |
| Hover    | `--grey-40`      | `--primary-60`     |
| Pressed  | `--grey-60`      | `--primary-70`     |
| Focused  | `--grey-20`      | `--primary-60`     |
| Disabled | `--grey-20`      | `--primary-60`     |

---

## Border Radius Reference

| FAB Type       | Size    | Radius Token           | Value   |
| -------------- | ------- | ---------------------- | ------- |
| Standard FAB   | Small   | `--radius-full`        | 9999px  |
| Standard FAB   | Default | `--radius-full`        | 9999px  |
| Standard FAB   | Large   | `--radius-full`        | 9999px  |
| Extended FAB   | Small   | `--radius-button`      | 250px   |
| Extended FAB   | Default | `--radius-button`      | 250px   |
| Extended FAB   | Large   | `--radius-button`      | 250px   |
| Extended (collapsed) | All | `--radius-full`       | 9999px  |
| Focus outline  | All     | `--radius-full`        | 9999px  |

---

## Spacing Reference

### Standard FAB

| Token        | Value  | Usage                                          |
| ------------ | ------ | ---------------------------------------------- |
| `--space-2`  | 8px    | Padding (small)                                |
| `--space-4`  | 16px   | Padding (default)                              |
| `--space-8`  | 32px   | Padding (large)                                |
| `--space-6`  | 24px   | Position bottom/right (mobile/tablet default)  |
| `--space-8`  | 32px   | Position bottom/right (desktop)                |
| `--space-4`  | 16px   | Position right (mobile)                        |
| `--space-4`  | 16px   | Gap between multiple FABs                      |
| `--space-20` | 80px   | Bottom offset when bottom nav bar is present   |

### Extended FAB

| Token        | Value  | Usage                                        |
| ------------ | ------ | -------------------------------------------- |
| `--space-3`  | 12px   | Gap between icon and label                   |
| `--space-4`  | 16px   | Horizontal padding (small)                   |
| `--space-6`  | 24px   | Horizontal padding (default)                 |
| `--space-8`  | 32px   | Horizontal padding (large)                   |
| `--space-2`  | 8px    | Vertical padding (small)                     |
| `--space-4`  | 16px   | Vertical padding (default)                   |
| `--space-5`  | 20px   | Vertical padding (large)                     |
| `--space-20` | 80px   | Minimum width token                          |
| `--space-1`  | 4px    | Focus outline offset                         |

---

## Typography Reference

| Token                   | Value   | Usage                                    |
| ----------------------- | ------- | ---------------------------------------- |
| `--font-family-jiotype` | JioType | Font family (all FAB text)               |
| `--font-weight-bold`    | 700     | Extended FAB label (all sizes)           |
| `--text-button`         | 16px    | Extended FAB label (small, default)      |
| `--text-button-large`   | 18px    | Extended FAB label (large)               |

---

## Animations

### FAB Appear (Mount / Page Load)

```
Duration:         300ms
Easing:           ease-out
Transform:        scale(0) → scale(1)
Opacity:          0 → 1
```

### FAB Disappear (Unmount)

```
Duration:         200ms
Easing:           ease-in
Transform:        scale(1) → scale(0)
Opacity:          1 → 0
```

### Extended FAB Expand (Collapse → Expanded)

```
Duration:         300ms
Easing:           ease-out
Width:            56px → auto
Border Radius:    var(--radius-full) → var(--radius-button)
Label Opacity:    0 → 1
Label Width:      0 → auto
```

### Extended FAB Collapse (Expanded → Collapsed)

```
Duration:         200ms
Easing:           ease-in
Width:            auto → 56px
Border Radius:    var(--radius-button) → var(--radius-full)
Label Opacity:    1 → 0
Label Width:      auto → 0
```

### Press / Active Feedback

```
Duration:         100ms
Easing:           ease-in
Transform:        scale(1) → scale(0.97)
```

### Press Release

```
Duration:         150ms
Easing:           ease-out
Transform:        scale(0.97) → scale(1)
```

---

## Accessibility (A11y)

### ARIA Attributes

```tsx
{/* Standard FAB — icon only (requires aria-label) */}
<button
  type="button"
  role="button"
  aria-label="Create new post"
  className="fab fab--primary fab--default"
>
  <IcEdit className="w-6 h-6" fill="currentColor" aria-hidden="true" />
</button>

{/* Extended FAB — icon + label (aria-label optional; visible label suffices) */}
<button
  type="button"
  role="button"
  className="fab fab--primary fab--extended fab--default"
>
  <IcEdit className="w-6 h-6" fill="currentColor" aria-hidden="true" />
  <span>Create post</span>
</button>

{/* Disabled FAB */}
<button
  type="button"
  disabled
  aria-disabled="true"
  aria-label="Create new post"
  className="fab fab--primary fab--default"
>
  <IcEdit className="w-6 h-6" fill="currentColor" aria-hidden="true" />
</button>
```

### Keyboard Support

| Key            | Action                              |
| -------------- | ----------------------------------- |
| `Tab`          | Move focus to FAB                   |
| `Shift + Tab`  | Move focus away from FAB            |
| `Enter`        | Activate FAB action                 |
| `Space`        | Activate FAB action (alternative)   |

### Focus Visible

```
Outline:          var(--border-width-thick) solid [variant focus color]  → 2px solid
Outline Offset:   var(--space-1)             → 4px
Border Radius:    var(--radius-full)         → 9999px  (matches FAB shape)
```

### Screen Reader Requirements

- **Standard FABs (icon-only)**: MUST have `aria-label` describing the action (e.g., `"Create new"`, `"Share"`, `"Edit"`)
- **Extended FABs**: The visible label serves as the accessible name; `aria-label` is still recommended for clarity
- **Icons**: MUST have `aria-hidden="true"` — the icon is decorative when a label is present
- **Disabled FABs**: MUST have `aria-disabled="true"` in addition to the HTML `disabled` attribute
- **Fixed position**: Consider adding a landmark or skip-link so keyboard-only users can reach the FAB efficiently

### Color Contrast

- **Primary FAB** (white on `--primary-50`): 4.6:1 (WCAG AA ✓)
- **Surface FAB** (`--primary-50` on white): 4.6:1 (WCAG AA ✓)
- **Secondary FAB** (white on `--secondary-50`): Ensure sufficient contrast is validated
- **Tertiary FAB** (`--primary-60` on `--grey-20`): Validate in implementation

### Touch Target

- All FAB sizes meet or exceed the 44×44px minimum touch target guideline (WCAG 2.5.5)
- Small FAB (40×40px) is slightly below — compensate with a transparent touch-area padding of `var(--space-1)` (4px) on all sides

---

## Props

| Prop              | Type                                                              | Default         | Description                                                      |
| ----------------- | ----------------------------------------------------------------- | --------------- | ---------------------------------------------------------------- |
| `variant`         | `'primary' \| 'surface' \| 'secondary' \| 'tertiary'`            | `'primary'`     | Color scheme of the FAB                                          |
| `size`            | `'small' \| 'default' \| 'large'`                                 | `'default'`     | Dimensional size of the FAB                                      |
| `extended`        | `boolean`                                                         | `false`         | Renders as Extended FAB (icon + label)                           |
| `label`           | `string`                                                          | —               | Label text for Extended FAB (required when `extended={true}`)    |
| `icon`            | `React.ReactNode`                                                 | —               | Icon element (required)                                          |
| `collapsible`     | `boolean`                                                         | `false`         | Extended FAB collapses to icon-only on scroll down               |
| `position`        | `'bottom-right' \| 'bottom-left' \| 'bottom-center'`             | `'bottom-right'`| Fixed position on screen                                         |
| `offsetBottom`    | `string` (CSS value using design tokens)                          | —               | Override bottom offset (for nav bar offset, snackbar avoidance)  |
| `disabled`        | `boolean`                                                         | `false`         | Disables the FAB (opacity 0.3, pointer-events none)              |
| `aria-label`      | `string`                                                          | —               | Accessible label (required for icon-only FABs)                   |
| `onClick`         | `() => void`                                                      | —               | Click/tap handler                                                |
| `className`       | `string`                                                          | —               | Additional CSS classes for the FAB container                     |
| `badge`           | `React.ReactNode`                                                 | —               | Optional Badge element to overlay on top-right of FAB            |

---

## Usage Examples

### Primary Standard FAB (Default)

```tsx
import { FAB } from '@/components/ui/fab';
import { IcEdit } from '@jds/core-icons';

function PageWithFAB() {
  return (
    <FAB
      variant="primary"
      size="default"
      aria-label="Create new post"
      onClick={() => setCreateModalOpen(true)}
      icon={<IcEdit fill="currentColor" />}
    />
  );
}
```

---

### Extended FAB with Label

```tsx
<FAB
  variant="primary"
  size="default"
  extended
  label="New Post"
  icon={<IcEdit fill="currentColor" />}
  aria-label="Create new post"
  onClick={() => setCreateModalOpen(true)}
/>
```

---

### Collapsible Extended FAB (Collapses on Scroll)

```tsx
<FAB
  variant="primary"
  size="default"
  extended
  collapsible
  label="Create"
  icon={<IcAdd fill="currentColor" />}
  aria-label="Create new item"
  onClick={handleCreate}
/>
```

---

### Surface FAB (for dark/image backgrounds)

```tsx
<FAB
  variant="surface"
  size="default"
  aria-label="Share"
  icon={<IcShare fill="currentColor" />}
  onClick={handleShare}
/>
```

---

### Small FAB (Secondary Action)

```tsx
<FAB
  variant="surface"
  size="small"
  aria-label="Filter results"
  icon={<IcFilter fill="currentColor" />}
  onClick={toggleFilterPanel}
/>
```

---

### Large FAB

```tsx
<FAB
  variant="primary"
  size="large"
  aria-label="Add item"
  icon={<IcAdd fill="currentColor" />}
  onClick={handleAddItem}
/>
```

---

### FAB Positioned Above Navigation Bar

```tsx
<FAB
  variant="primary"
  size="default"
  aria-label="Compose"
  icon={<IcEdit fill="currentColor" />}
  onClick={handleCompose}
  offsetBottom="var(--space-20)"  // 80px — clears bottom nav
/>
```

---

### FAB with Notification Badge

```tsx
<FAB
  variant="primary"
  size="default"
  aria-label="Notifications (5 unread)"
  icon={<IcNotification fill="currentColor" />}
  onClick={openNotificationsPanel}
  badge={
    <Badge badgeColorScheme="error" badgeEmphasis="high" placement="overlay">
      5
    </Badge>
  }
/>
```

---

### Disabled FAB

```tsx
<FAB
  variant="primary"
  size="default"
  disabled
  aria-label="Create (unavailable)"
  icon={<IcEdit fill="currentColor" />}
  onClick={() => {}}
/>
```

---

### Multiple FABs (Primary + Secondary)

```tsx
<>
  {/* Secondary — smaller, above primary */}
  <FAB
    variant="surface"
    size="small"
    aria-label="Share"
    icon={<IcShare fill="currentColor" />}
    onClick={handleShare}
    style={{ bottom: 'calc(var(--space-6) + 56px + var(--space-4))' }}
  />

  {/* Primary — bottom-right default position */}
  <FAB
    variant="primary"
    size="default"
    aria-label="Create new"
    icon={<IcAdd fill="currentColor" />}
    onClick={handleCreate}
  />
</>
```

---

## Design Considerations

### When to Use FAB

✅ **Use FAB when:**

- The action is the **most important and frequent action** on the screen
- The action creates **new content** (compose, add, create, write)
- The action needs to be **persistently accessible** regardless of scroll position
- You want a **high-visibility trigger** that stands out from the page content

### When NOT to Use FAB

❌ **Don't use FAB when:**

- The action is **destructive** (delete, remove) — use a standard button in context
- There are **multiple equally important actions** — use a toolbar or action bar instead
- The page already has a **prominent primary CTA** at the top (hero button) — avoid competing CTAs
- The action is **rarely used** — a FAB draws high attention, reserve it for frequent actions
- You are in a **form or dialog** — use standard in-context buttons
- The **screen is already crowded** with floating elements (modals, toasts) — avoid z-index conflicts

### Best Practices

1. **One FAB per screen**: Only use multiple FABs when strictly necessary (max 2)
2. **Use clear icons**: The icon must unambiguously communicate the action without text (for standard FABs)
3. **Provide always an accessible label**: `aria-label` is mandatory on icon-only FABs
4. **Prefer Extended FAB for new users**: Text + icon aids discoverability; collapse on scroll for experienced users
5. **Respect safe areas**: On mobile, account for the device's bottom safe area (home indicator) by adding appropriate offset
6. **Avoid covering important content**: Position FABs to minimize overlap with key page content
7. **Animate entrance/exit**: FABs should not appear or disappear abruptly — use scale animation
8. **Offset for navigation**: Always account for bottom navigation bars with the `offsetBottom` prop

---

## Do's and Don'ts

### ✅ Do: Single, clear primary action

```
[✏️ Create]  ← Extended FAB, primary variant, bottom-right
```

Clear label + icon makes the action obvious.

---

### ✅ Do: Collapse on scroll for cleaner reading experience

```
Scrolling down:  [✏️]       ← Collapses to icon
Scrolling up:    [✏️ Create] ← Expands to show label
```

---

### ❌ Don't: Use FAB for destructive actions

```
[🗑️ Delete]  ← Never use FAB for delete/remove
```

Destructive actions should be in context (dialogs, inline buttons).

---

### ❌ Don't: Stack more than 2 FABs

```
[📎]   ← Too many FABs
[🔔]   ← Confusing hierarchy
[📤]
[✏️]   ← Which is the primary action?
```

Limit to 1–2 FABs maximum.

---

### ❌ Don't: Use FAB in forms or dialogs

```
┌──────────────────┐
│  Form Title      │
│                  │
│  [Input]         │
│  [Input]         │
│                  │         ← FAB out of place here
│              [✏️]│
└──────────────────┘
```

Use standard form action buttons (`<Button>`) inside dialogs and forms.

---

## Implementation Checklist

When implementing FAB components, verify:

- [ ] Uses `font-family: var(--font-family-jiotype)` for all text
- [ ] Extended FAB label uses `var(--font-weight-bold)` (700) — never other weights
- [ ] Extended FAB label font size uses `--text-button` (default/small) or `--text-button-large` (large)
- [ ] Standard FAB border radius is `var(--radius-full)` (9999px — full circle)
- [ ] Extended FAB border radius is `var(--radius-button)` (250px — pill)
- [ ] Collapsed extended FAB switches to `var(--radius-full)` (9999px)
- [ ] FAB size is 40px (small), 56px (default), or 96px (large)
- [ ] Icon uses `fill="currentColor"` per icon.md
- [ ] Shadow uses `var(--shadow-card-md)` (normal/hover) and `var(--shadow-card-sm)` (pressed)
- [ ] Disabled state uses `opacity: 0.3` (30%) — MANDATORY — no color changes
- [ ] Disabled state has `pointer-events: none` and `aria-disabled="true"`
- [ ] Primary variant uses `var(--primary-50)` background and `var(--primary-inverse)` icon/text
- [ ] Surface variant uses `var(--primary-background)` bg and `var(--primary-50)` icon/text
- [ ] Hover state uses correct per-variant hover background token
- [ ] Pressed state uses scale(0.97) transform
- [ ] Focus outline uses `var(--border-width-thick)` (2px) with correct variant color
- [ ] Focus outline offset uses `var(--space-1)` (4px)
- [ ] FAB is `position: fixed` with bottom/right using spacing tokens
- [ ] Position offsets for bottom nav bar use `var(--space-20)` (80px)
- [ ] Entrance animation uses scale(0) → scale(1) over 300ms ease-out
- [ ] Icon-only FABs have `aria-label` (MANDATORY for accessibility)
- [ ] Icons have `aria-hidden="true"` when label is present
- [ ] Touch target is at minimum 44×44px (apply transparent padding for small FAB)
- [ ] Gap between icon and label in extended FAB is `var(--space-3)` (12px)
- [ ] No custom/hardcoded colors, spacing, or typography values

---

## Related Components

- **Button** (`/guidelines/MD/Component/button.md`): FAB states and typography rules mirror the Button component
- **Badge** (`/guidelines/MD/Component/badge.md`): Optional badge overlay on FAB
- **Bottomsheet** (`/guidelines/MD/Component/bottomsheet.md`): FAB often triggers a bottom sheet on mobile
- **Icon** (`/guidelines/MD/Component/icon.md`): Icon usage rules (fill="currentColor")
- **Toast / Snackbar**: FAB must offset upward when a toast/snackbar is visible

---

## Browser Compatibility

- `position: fixed` with bottom/right offsets — fully supported in modern browsers
- CSS transforms (`scale`, `translateY`) — fully supported
- CSS transitions — fully supported
- `outline-offset` — fully supported in modern browsers
- Bottom safe area on iOS: use `env(safe-area-inset-bottom)` combined with spacing tokens when targeting PWA / installed apps
