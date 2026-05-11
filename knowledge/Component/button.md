# Button — JDS Component Style Guide

## Overview

This document defines the button variants, sizes, and states used across the application. Every button must adhere strictly to JDS design tokens from `/src/styles/theme.css`.

The component lives in `/src/app/components/ui/button.tsx` and exports both `Button` and `buttonVariants`.

---

## Typography Rules (MANDATORY)

> **ALL text in Button components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (Buttons)

| Token                       | Value | Usage                                   |
| --------------------------- | ----- | --------------------------------------- |
| `--font-weight-bold`        | 700   | Default button text (all sizes)         |

- Buttons always use `var(--font-weight-bold)` (700).
- **Never** use arbitrary `font-weight` numbers or Tailwind font-weight utilities.

### Permitted Sizes (Buttons)

| Token                | Value | Usage                          |
| -------------------- | ----- | ------------------------------ |
| `--text-button`      | 16px  | Default and `sm` sizes         |
| `--text-button-large`| 18px  | `lg` size                      |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Base Styles (All Variants)

All button variants share these base styles:

```
display:        inline-flex
align-items:    center
justify-content: center
gap:            8px (gap-2)
white-space:    nowrap
border-radius:  var(--radius-button)       -> 250px (full pill)
font-family:    var(--font-family-jiotype)
font-size:      var(--text-button)         -> 16px
font-weight:    var(--font-weight-bold)    -> 700
line-height:    1.5
transition:     transition-all
cursor:         pointer
```

### Disabled State (All Variants)

The disabled state preserves the **same visual aspect as the Normal state** (same colors, shape, size) and applies a **general opacity of 30%** over the entire button. No color or layout changes — only reduced opacity.

```
pointer-events: none
opacity:        0.3                        → 30% (MANDATORY)
```

> **MANDATORY:** Disabled buttons must use `opacity: 0.3` (30%). The previous value of `0.5` is deprecated. This applies to:
> - The JDS `<Button>` component (`disabled:opacity-30` in Tailwind)
> - Carousel arrow buttons (inline `opacity: canScroll ? 1 : 0.3`)
> - Any other element using a disabled appearance

### Focus State (All Variants)

```
border-color:   var(--ring)                -> var(--primary-50)
ring:           3px ring in var(--ring) at 50% opacity
outline:        none
```

### SVG Icon Handling

- Nested SVGs auto-size to `size-4` (16px) unless explicitly sized
- SVGs have `pointer-events: none` and `shrink-0`
- All icons must use `fill="currentColor"` per `icon.md`

---

## Variants

### 1. Default (Primary)

The primary action button. Used for the most important CTA on a page or section.

```
Normal State:
  background:     var(--primary-50)          -> #3535F3
  color:          var(--primary-inverse)     -> #FFFFFF
  icon color:     var(--primary-inverse)     -> #FFFFFF
  border:         none

Hover State:
  background:     var(--primary-30)          -> #9999FF
  color:          var(--primary-70)          -> #00004C
  icon color:     var(--primary-70)          -> #00004C
  border:         none

Pressed State:
  background:     var(--primary-60)          -> #000093
  color:          var(--primary-inverse)     -> #FFFFFF
  icon color:     var(--primary-inverse)     -> #FFFFFF
  border:         none

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring color:     var(--primary-60)          -> #000093

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
┌─────────────────────────────┐
│                             │
│   ██ Primary Button Text ██ │  <- white text on blue bg
│                             │
└─────────────────────────────┘
  bg: --primary-50 (#3535F3)
  text: --primary-inverse (#FFFFFF)
  pill shape (250px radius)
```

#### When to Use

- Main CTA in hero sections (on light backgrounds)
- Form submission buttons
- Primary actions in dialogs/modals

---

### 1b. Default Inverse (Primary Inverse)

The inverse variant of the primary button, designed for use on **dark backgrounds** (images, overlays, dark theme) and **primary-colored backgrounds** (e.g. `--primary-50`, `--primary-60`, `--primary-80`). Uses `--primary-background` (white) background with `--grey-100` (dark) text for contrast.

```
Normal State:
  background:     var(--primary-background)  -> #FFFFFF
  color:          var(--grey-100)            -> #141414
  icon color:     var(--grey-100)            -> #141414
  border:         none

Hover State:
  background:     var(--primary-20)          -> #E8E8FC
  color:          var(--grey-100)            -> #141414
  icon color:     var(--grey-100)            -> #141414
  border:         none

Pressed State:
  background:     var(--primary-30)          -> #9999FF
  color:          var(--grey-100)            -> #141414
  icon color:     var(--grey-100)            -> #141414
  border:         none

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring color:     var(--primary-50)          -> #3535F3

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
┌─────────────────────────────┐
│                             │
│   ██ Inverse Primary Btn ██ │  <- dark text on white bg
│                             │  <- sits on dark/primary bg
└─────────────────────────────┘
  bg: --primary-background (#FFFFFF)
  text: --grey-100 (#141414)
  pill shape (250px radius)
```

#### When to Use

- Primary CTAs on dark image backgrounds (e.g. hero carousel slides)
- Primary CTAs on primary-colored backgrounds (e.g. `--primary-50` sections)
- Primary actions on dark theme / dark overlays
- Main CTA on dark hero banners

---

### 2. Destructive

A red button for dangerous or irreversible actions.

```
background:     var(--destructive)         -> var(--error-50) / #FA2F40
color:          var(--global-white)
border:         none

hover:
  background:   var(--destructive) at 90% opacity

focus:
  ring:         var(--destructive) at 20% opacity
```

#### When to Use

- Delete / remove actions
- Account cancellation
- Irreversible operations

---

### 3. Secondary

A bordered button with transparent background and primary-60 text. Used for secondary/complementary actions.

```
Normal State:
  background:     transparent
  color:          var(--primary-60)          -> #000093
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--primary-60)          -> #000093

Hover State:
  background:     var(--primary-20)          -> #E8E8FC
  color:          var(--primary-60)          -> #000093
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--primary-60)          -> #000093

Pressed State:
  background:     var(--primary-30)          -> #9999FF
  color:          var(--primary-70)          -> #00004C
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--primary-70)          -> #00004C

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring color:     var(--grey-60)             -> #B5B5B5

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
┌─────────────────────────────┐
│                             │
│   ○ Secondary Button Text ○ │  <- primary-60 text, grey-60 border
│                             │
└─────────────────────────────┘
  bg: transparent
  text: --primary-60 (#000093)
  border: 1px solid --grey-60 (#B5B5B5)
  pill shape (250px radius)
```

#### When to Use

- Complementary actions alongside primary buttons
- "Explore more", "View all", "Check all" section CTAs
- Secondary CTA on **light backgrounds** only
- Support page action buttons on light sections

---

### 3b. Secondary Inverse

The inverse variant of the secondary button, designed for use on **dark backgrounds** (images, overlays) and **primary-colored backgrounds** (e.g. `--primary-50`). Uses `--primary-background` (white) text in normal state for contrast.

```
Normal State:
  background:     transparent
  color:          var(--primary-background)  -> #FFFFFF
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--primary-background)  -> #FFFFFF

Hover State:
  background:     var(--primary-20)          -> #E8E8FC
  color:          var(--grey-100)            -> #141414
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--grey-100)            -> #141414

Pressed State:
  background:     var(--primary-30)          -> #9999FF
  color:          var(--grey-100)            -> #141414
  border:         1px solid var(--grey-60)   -> #B5B5B5 (inside)
  icon color:     var(--grey-100)            -> #141414

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring color:     var(--primary-50)          -> #3535F3

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
┌─────────────────────────────┐
│                             │
│   ○ Inverse Sec Button   ○  │  <- white text, grey-60 border
│                             │  <- on dark/primary bg
└─────────────────────────────┘
  bg: transparent
  text: --primary-background (#FFFFFF)
  border: 1px solid --grey-60 (#B5B5B5)
  pill shape (250px radius)
```

#### When to Use

- Secondary CTAs on dark image backgrounds (e.g. hero carousel slides)
- Secondary CTAs on primary-colored backgrounds (e.g. `--primary-50` sections)
- Action buttons in dark sections (e.g. SupportContact)

---

### 4. Tertiary

A transparent text-only button with no background or border. Uses `--primary-60` text color and `--radius-xl` (12px) border-radius for the focus ring shape. Used for low-emphasis actions, icon-only buttons, and toolbar actions on **light backgrounds**.

```
Normal State:
  background:     transparent
  color:          var(--primary-60)          -> #000093
  icon color:     var(--primary-60)          -> #000093
  border:         none

Hover State:
  background:     transparent
  color:          var(--primary-50)          -> #3535F3
  icon color:     var(--primary-50)          -> #3535F3
  border:         none

Pressed State:
  background:     transparent
  color:          var(--primary-70)          -> #00004C
  icon color:     var(--primary-70)          -> #00004C
  border:         none

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring radius:    var(--radius-xl)           -> 12px
  ring color:     var(--primary-60)          -> #000093

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
  Tertiary Button Text   <- primary-60 text, no bg/border
  bg: transparent
  text: --primary-60 (#000093)
  border: none
  radius: --radius-xl (12px) for focus ring
```

#### When to Use

- Toolbar actions
- Icon-only buttons in headers/nav (hamburger menu, etc.)
- Low-emphasis actions that shouldn't compete with primary CTAs
- Text-link style CTAs on light backgrounds

---

### 4b. Tertiary Inverse

The inverse variant of the tertiary button, designed for use on **dark backgrounds** (images, overlays, dark theme) and **primary-colored backgrounds**. Uses `--primary-background` (white) text for contrast.

```
Normal State:
  background:     transparent
  color:          var(--primary-background)  -> #FFFFFF
  icon color:     var(--primary-background)  -> #FFFFFF
  border:         none

Hover State:
  background:     transparent
  color:          var(--primary-20)          -> #E8E8FC
  icon color:     var(--primary-20)          -> #E8E8FC
  border:         none

Pressed State:
  background:     transparent
  color:          var(--primary-30)          -> #9999FF
  icon color:     var(--primary-30)          -> #9999FF
  border:         none

Focused State:
  Same aspect as Normal
  ring:           4px outside
  ring color:     var(--primary-50)          -> #3535F3

Disabled State:
  Same aspect as Normal
  opacity:        0.3                        -> 30% (MANDATORY)
```

#### Visual

```
  Inverse Tertiary Text  <- white text, no bg/border
                           <- on dark/primary bg
  bg: transparent
  text: --primary-background (#FFFFFF)
  border: none
  radius: --radius-xl (12px) for focus ring
```

#### When to Use

- Icon-only buttons on dark image overlays
- Low-emphasis actions on dark/primary-colored backgrounds
- Text-link style CTAs on dark sections

---

### 5. Link

A text-only button styled as a hyperlink.

```
background:     transparent
color:          var(--primary)             -> var(--primary-50)
border:         none
text-decoration: none (underline on hover)
underline-offset: 4px

hover:
  text-decoration: underline
```

#### When to Use

- Inline text actions
- "Learn more", "View details" within body text
- Navigation-style actions

---

## Sizes

### Default

```
height:         48px (h-12)
padding:        px-6 py-3
font-size:      var(--text-button)         -> 16px
icon padding:   px-4 (when button contains only an SVG child)
```

### Small (`sm`)

```
height:         40px (h-10)
padding:        px-4
gap:            6px (gap-1.5)
font-size:      var(--text-button)         -> 16px
border-radius:  var(--radius-button)       -> 250px
icon padding:   px-2.5 (when button contains only an SVG child)
```

### Large (`lg`)

```
height:         56px (h-14)
padding:        px-8
font-size:      var(--text-button-large)   -> 18px
border-radius:  var(--radius-button)       -> 250px
icon padding:   px-5 (when button contains only an SVG child)
```

### Icon (`icon`)

Icon-only button variant used for carousel navigation arrows and other icon-only actions. The button is a perfect circle/square.

```
width:          40px (w-10)
height:         40px (h-10)
padding:        0
font-size:      var(--text-button)         -> 16px
border-radius:  var(--radius-button)       -> 250px
icon size:      w-5 h-5 (20px)
```

**Usage:**
- Carousel navigation arrows (section carousels)
- Icon-only toolbar buttons
- Compact action buttons

**Example:**
```tsx
<Button variant="secondary" size="icon" aria-label="Previous cards">
  <IcArrowBack className="w-5 h-5" fill="currentColor" />
</Button>
```

**Visual:**
```
┌─────┐
│  ←  │  ← 40×40px circle
└─────┘
  bg: transparent
  border: 1px solid --grey-60
  icon: --primary-60
  pill shape (250px radius)
```

---

## Size + Variant Matrix

| Size      | Height | Padding   | Font Size              | Radius                  |
| --------- | ------ | --------- | ---------------------- | ----------------------- |
| `default` | 48px   | `px-6`    | `--text-button` (16px) | `--radius-button` (250px) |
| `sm`      | 40px   | `px-4`    | `--text-button` (16px) | `--radius-button` (250px) |
| `lg`      | 56px   | `px-8`    | `--text-button-large` (18px) | `--radius-button` (250px) |
| `icon`    | 40px   | centered  | n/a                    | `--radius-button` (250px) |

All variants can be used with any size. The variant controls color/style, the size controls dimensions.

---

## Props

| Prop        | Type                                                        | Default     | Description                              |
| ----------- | ----------------------------------------------------------- | ----------- | ---------------------------------------- |
| `variant`   | `'default' \| 'defaultInverse' \| 'destructive' \| 'secondary' \| 'secondaryInverse' \| 'tertiary' \| 'tertiaryInverse' \| 'link'` | `'default'` | Visual style of the button               |
| `size`      | `'default' \| 'sm' \| 'lg' \| 'icon'`                      | `'default'` | Dimensional size of the button           |
| `asChild`   | `boolean`                                                   | `false`     | Render as child element (Radix Slot)     |
| `className` | `string`                                                    | —           | Additional CSS classes                   |
| `disabled`  | `boolean`                                                   | `false`     | Disables interaction and dims the button |
| ...         | `React.ComponentProps<'button'>`                            | —           | All native button HTML attributes        |

### `asChild` Usage

When `asChild` is `true`, the Button renders as a Radix `Slot`, merging its props (including className) onto the single child element. This is useful for rendering a button-styled `<a>` tag or `<Link>`:

```tsx
<Button asChild variant="secondary">
  <a href="/support">Go to Support</a>
</Button>
```

---

## Design Token Reference

| Token                   | Value         | Usage in Button                    |
| ----------------------- | ------------- | ---------------------------------- |
| `--radius-button`       | `250px`       | Border radius (full pill)          |
| `--text-button`         | `16px`        | Font size (default, sm)            |
| `--text-button-large`   | `18px`        | Font size (lg)                     |
| `--font-weight-bold`    | `700`         | Font weight (all sizes)            |
| `--font-family-jiotype` | JioType stack | Font family (all buttons)          |
| `--primary-50`          | `#3535F3`     | Default variant bg                 |
| `--primary-inverse`     | `#FFFFFF`     | Default variant text               |
| `--primary-30`          | `#9999FF`     | Default variant hover bg           |
| `--primary-70`          | `#00004C`     | Default variant hover text         |
| `--primary-60`          | `#000093`     | Default variant pressed bg / focus ring |
| `--primary-background`  | `#FFFFFF`     | Default Inverse bg / Secondary Inverse text |
| `--grey-100`            | `#141414`     | Default Inverse text / Secondary Inverse hover text |
| `--elevation-sm`        | box-shadow    | (legacy, removed from default)     |
| `--grey-60`             | `#B5B5B5`     | Secondary border                   |
| `--error-50`            | `#FA2F40`     | Destructive variant bg             |
| `--radius-xl`           | `12px`        | Tertiary variant focus ring radius |
| `--foreground`          | `#141414`     | Foreground text                    |

---

## Usage Examples

### Primary CTA

```tsx
<Button variant="default" size="default">
  Recharge Now
</Button>
```

### Primary Inverse CTA (on dark/primary backgrounds)

```tsx
<Button variant="defaultInverse">
  Claim now
</Button>
```

### Secondary CTA

```tsx
<Button variant="secondary">
  Explore More
</Button>
```

### Secondary Inverse CTA (on dark/primary backgrounds)

```tsx
<Button variant="secondaryInverse">
  Chat with us
</Button>
```

### Tertiary CTA (text-only, light background)

```tsx
<Button variant="tertiary">
  Learn more
</Button>
```

### Tertiary Inverse (icon button on dark background)

```tsx
<Button variant="tertiaryInverse" size="icon">
  <Menu className="h-6 w-6" fill="currentColor" />
</Button>
```

### Large CTA

```tsx
<Button variant="default" size="lg">
  Get Started
</Button>
```

### Icon Button (e.g. carousel arrow)

```tsx
<Button variant="secondary" size="icon">
  <ChevronRight className="w-5 h-5" fill="currentColor" />
</Button>
```

### Button as Link

```tsx
<Button asChild variant="link">
  <a href="/plans">View all plans</a>
</Button>
```

### Custom-styled Secondary (dark border override)

Used in sections like the Troubleshoot CTA where the border should be `--foreground` instead of `--grey-60`:

```tsx
<Button
  variant="secondary"
  style={{
    fontFamily: 'var(--font-family-jiotype)',
    fontSize: 'var(--text-button)',
    fontWeight: 'var(--font-weight-bold)',
    borderColor: 'var(--foreground)',
    color: 'var(--foreground)',
    borderRadius: 'var(--radius-button)',
    backgroundColor: 'transparent',
  }}
>
  Any other issues? Explore
</Button>
```

---

## Accessibility

- All buttons must be focusable and keyboard-accessible
- Focus ring uses `var(--ring)` (3px ring at 50% opacity)
- Disabled buttons use `opacity: 0.3` (30%) and `pointer-events: none` — same visual aspect as Normal, only dimmed
- Icon-only buttons should include `aria-label` or `<span className="sr-only">` for screen readers
- `aria-invalid` state switches focus ring to destructive color

---

## Checklist

Before using a Button, verify:

- [ ] Uses `font-family: var(--font-family-jiotype)` (inherited from base styles)
- [ ] Font weight is `var(--font-weight-bold)` (700) — never other weights
- [ ] Font size uses `--text-button` or `--text-button-large` tokens only
- [ ] Border radius is `var(--radius-button)` (250px pill)
- [ ] All icons inside buttons use `fill="currentColor"` per `icon.md`
- [ ] No Tailwind text-size or font-weight utilities are used on buttons
- [ ] No arbitrary font families, weights, or sizes appear
- [ ] Icon-only buttons have accessible labels