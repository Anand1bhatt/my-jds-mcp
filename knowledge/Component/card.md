# Card — JDS Component Style Guide

## Variants

This document defines the card variants used across the application. Every card must adhere strictly to JDS design tokens from `/src/styles/theme.css`.

---

## Typography Rules (MANDATORY)

> **ALL text in Card components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- This resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif) anywhere.
- Every text element — headings, brand labels, CTA buttons, descriptions — must inherit or explicitly set `font-family: var(--font-family-jiotype)`.

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.
- The team must provide the JioType `.woff2` file at `/public/fonts/JioType-Variable.woff2`.

### Permitted Weights

Only these four JDS weight tokens are allowed:

| Token                       | Value | Usage                                   |
| --------------------------- | ----- | --------------------------------------- |
| `--font-weight-normal`      | 400   | Body text, descriptions                 |
| `--font-weight-medium`      | 500   | Brand labels, paragraph text            |
| `--font-weight-bold`        | 700   | CTA buttons, sub-headings               |
| `--font-weight-black`       | 900   | Card headlines, section titles          |

- **Never** use arbitrary `font-weight` numbers (e.g. `600`, `800`).
- **Never** use Tailwind font-weight utilities (e.g. `font-semibold`).

### Permitted Sizes

| Token                | Value | Usage                          |
| -------------------- | ----- | ------------------------------ |
| `--text-h1`          | 88px  | Hero display                   |
| `--text-h2`          | 64px  | Page-level section headings    |
| `--text-h3`          | 32px  | Card headline max (clamp)      |
| `--text-h4`          | 24px  | Card headline min (clamp)      |
| `--text-body-large`  | 24px  | Large body text                |
| `--text-button-large`| 18px  | Large button text              |
| `--text-base`        | 16px  | Body text                      |
| `--text-button`      | 16px  | Standard button text           |
| `--text-label`       | 14px  | Brand labels, CTA buttons      |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`).
- Use `clamp()` with JDS tokens for responsive sizing.

---

## Image Card Variant (2-Column Promotional Grid — Grid Banner)

The Image Card is a full-bleed image card used in 2-column grid layouts. The background image fills the entire card. Text content sits over a gradient overlay. **No solid color fill is used — the image IS the background.**

### Visual Structure

```
┌───────────────────────────────────────────┐
│  padding: var(--space-16) (64px all)      │
│                                           │
│  Product Name                             │
│  (--text-heading-xs, 24px, bold 700)      │
│                                           │
│  Heading Title                            │
│  (--text-heading-m, 40px, black 900,      │
│   whitespace pre-line)                    │
│                                           │
│  [ Primary CTA ]  [ Secondary CTA ]      │
│   (product color)  (white outline)        │
│                                           │
│  ┄┄┄┄┄┄┄ gradient overlay ┄┄┄┄┄┄┄┄┄┄┄   │
│                                           │
│        Full-bleed background image        │
│        (object-cover, fills entire        │
│         card, subtle zoom on hover)       │
│                                           │
│  W: 580px  H: 720px  R: 24px (--radius-lg)│
└───────────────────────────────────────────┘
```

### Key Principles

1. **Image fills the entire card** — no solid color background, no split layout
2. **Gradient overlay** provides text contrast without obscuring the image (direction flips based on `contentPosition`)
3. **All text is white** (`--global-white`) — sits on the dark gradient
4. **Primary CTA comes first** (uses per-card/product accent color); **Secondary CTA** comes second (always white outline)
5. **Subtle hover zoom** (scale 1.05) on the background image for interactivity

### Layout Rules (MANDATORY)

| Property              | Value                                          |
| --------------------- | ---------------------------------------------- |
| Grid                  | `grid-cols-1 md:grid-cols-2`                   |
| Grid gap              | `var(--space-6)` (24px)                        |
| Grid max-width        | `calc(580px * 2 + var(--space-6))` — 1184px    |
| Card width            | `580px` max per card (fluid within grid)       |
| Card height           | `720px` fixed                                  |
| Card border-radius    | `var(--radius-lg)` → 24px                      |
| Card border           | None                                           |
| Card shadow           | None                                           |
| Card overflow         | `hidden`                                       |
| Card position         | `relative`                                     |
| Content padding       | `var(--space-16)` (64px) — all sides           |
| Image                 | `absolute inset-0`, `object-cover`, fills card |
| Gradient overlay      | `absolute inset-0`, direction based on content |
| Hover effect          | Image `scale-105` over 500ms transition        |

### Gradient Overlay

Direction flips based on `contentPosition`:

**Bottom (default)** — gradient goes from bottom to top:
```css
background: linear-gradient(
  to top,
  rgba(0, 0, 0, 0.75) 0%,     /* strong at bottom for text */
  rgba(0, 0, 0, 0.45) 40%,    /* medium in middle */
  rgba(0, 0, 0, 0.08) 100%    /* nearly transparent at top */
);
```

**Top** (`contentPosition: 'top'`) — gradient goes from top to bottom:
```css
background: linear-gradient(
  to bottom,
  rgba(0, 0, 0, 0.75) 0%,     /* strong at top for text */
  rgba(0, 0, 0, 0.45) 40%,    /* medium in middle */
  rgba(0, 0, 0, 0.08) 100%    /* nearly transparent at bottom */
);
```

The overlay is `pointer-events: none` so clicks pass through to buttons.

### Typography (MANDATORY)

| Element            | Desktop/Tablet                       | Mobile (<768px)                      |
| ------------------ | ------------------------------------ | ------------------------------------ |
| Product name       | `--text-heading-xs` (24px)           | `--text-body-m` (18px)               |
| Product name weight| `--font-weight-bold` (700)           | `--font-weight-bold` (700)           |
| Heading title      | `--text-heading-m` (40px)            | `--text-heading-xs` (24px)           |
| Heading weight     | `--font-weight-black` (900)          | `--font-weight-black` (900)          |
| CTA buttons        | `--text-button` (16px)               | `--text-button` (16px)               |
| CTA button weight  | `--font-weight-bold` (700)           | `--font-weight-bold` (700)           |
| CTA button size    | `default` (48px height)              | `small` (40px height)                |

All text uses `--font-family-jiotype`. All text color is `--global-white`.

Title supports multi-line via `whitespace-pre-line` with `\\n` in data.

Product name has `opacity: 0.85` for subtle hierarchy.

### CTA Buttons (MANDATORY — Primary First)

Two buttons per card, always side by side. **Primary CTA must come first (left), Secondary CTA second (right).** The Primary CTA color should match the product/brand identity.

#### Primary CTA (filled pill — product-wise color)

```
border-radius: var(--radius-button)     → 250px (full pill)
background:    [card.ctaBgToken]        → e.g. var(--error-60) for JioMart
color:         [card.ctaTextToken]      → e.g. var(--global-white)
hover bg:      [card.ctaHoverToken]     → e.g. var(--error-70)
padding:       px-6 (var(--space-6))
font-size:     var(--text-button)       → 16px
font-weight:   var(--font-weight-bold)  → 700
border:        none
size:          default (48px height)
```

#### Secondary CTA (white outline pill)

Since the image fills the card and all text is white, the outline button is always white:

```
border-radius: var(--radius-button)     → 250px (full pill)
background:    transparent
color:         var(--global-white)
border:        1.5px solid var(--global-white)
hover bg:      rgba(255, 255, 255, 0.15)
padding:       px-6 (var(--space-6))
font-size:     var(--text-button)       → 16px
font-weight:   var(--font-weight-bold)  → 700
size:          default (48px height)
```

### Recommended CTA Color Pairings

| Use case          | Primary CTA bg Token | Primary CTA text Token | Primary CTA hover Token |
| ----------------- | -------------------- | ---------------------- | ----------------------- |
| Commerce/Shopping | `--error-60`         | `--global-white`       | `--error-70`            |
| Cloud/Storage     | `--primary-50`       | `--primary-inverse`    | `--primary-60`          |
| Entertainment/TV  | `--secondary-50`     | `--secondary-inverse`  | `--secondary-60`        |
| Payments/Finance  | `--sparkle-60`       | `--sparkle-inverse`    | `--sparkle-70`          |
| General promo     | `--primary-50`       | `--primary-inverse`    | `--primary-60`          |
| Dark accent       | `--global-black`     | `--global-white`       | `--grey-100`            |

### Data Structure

```ts
interface ImageCardData {
  id: number;
  brand: string;         // Product name (e.g. "JioMart") — 24px Heading/xs
  title: string;         // Heading — 40px Heading/m, supports \n for line breaks
  primaryCta: string;    // Primary button label (comes FIRST)
  secondaryCta: string;  // Outline button label (comes SECOND)
  image: string;         // Image URL (Unsplash or figma:asset)
  alt: string;           // Accessibility alt text
  ctaBgToken: string;    // Primary CTA background token (product-specific)
  ctaTextToken: string;  // Primary CTA text color token
  ctaHoverToken: string; // Primary CTA hover background token
  contentPosition?: 'top' | 'bottom';  // Where to pin text — default 'bottom'
}
```

> **Note:** No `bgToken` or `theme` property — the image fills the card and all text is always white on the dark gradient.

### Spacing (MANDATORY)

| Area                      | Desktop/Tablet                | Mobile (<768px)               |
| ------------------------- | ----------------------------- | ----------------------------- |
| Grid gap                  | `var(--space-6)` (24px)       | `var(--space-6)` (24px)       |
| Card inner padding        | `var(--space-16)` (64px) — all sides | Top/Bottom: `var(--space-8)` (32px), Left/Right: `var(--space-6)` (24px) |
| Product name → Heading    | `var(--space-4)` (16px)       | `var(--space-4)` (16px)       |
| Heading → CTA buttons     | `var(--space-6)` (24px)       | `var(--space-4)` (16px)       |
| CTA button gap            | `var(--space-3)` (12px)       | `var(--space-3)` (12px)       |

### Dimensions (MANDATORY)

| Property             | Desktop/Tablet (≥768px)  | Mobile (<768px)          |
| -------------------- | ------------------------ | ------------------------ |
| Card width           | `580px` (max per card)   | Full-width (100%)        |
| Card height          | `720px` (fixed)          | `520px` (fixed)          |
| Border radius        | `var(--radius-lg)` (24px)| `var(--radius-lg)` (24px)|

### Responsive Behavior

| Breakpoint | Columns   | Card width                       | Card height                      |
| ---------- | --------- | -------------------------------- | -------------------------------- |
| Mobile (<768px) | 1 column | Full-width (100%)                | 520px (fixed)                    |
| md+ (≥768px) | 2 columns | Max 580px per card, 24px gap    | 720px (fixed)                    |

### Accessibility

- All images must have descriptive `alt` text
- Buttons must be focusable and keyboard-accessible
- Gradient overlay ensures WCAG AA contrast for white text on images
- Use semantic `<h3>` for card titles
- Hover zoom uses `transition-transform` for smooth animation

---

## Image Card Variant — Top-Left Content

A variant of the Image Card where text content (product name, heading, CTAs) is pinned to the **top-left** instead of the bottom-left. The gradient overlay flips direction accordingly — darkest at the top for text readability, fading to transparent toward the bottom.

This variant is activated via the `contentPosition: 'top'` prop on the shared `ImageCard` component. When omitted or set to `'bottom'`, the card renders the standard bottom-left layout.

### Visual Structure

```
┌───────────────────────────────────────────┐
│  padding: var(--space-16) (64px all)      │
│                                           │
│  Product Name (Heading/xs, 24px, bold)    │
│  ┌─────────────────────────────────┐      │
│  │ Heading Title                   │      │
│  │ (Heading/m, 40px, black 900)    │      │
│  └─────────────────────────────────┘      │
│                                           │
│  [ Primary CTA ]  [ Secondary CTA ]      │
│   (product color)  (white outline)        │
│                                           │
│  ┄┄┄┄┄┄┄ gradient fades out ┄┄┄┄┄┄┄┄┄   │
│                                           │
│        Full-bleed background image        │
│        (object-cover, fills entire        │
│         card, subtle zoom on hover)       │
│                                           │
└───────────────────────────────────────────┘
```

### Key Differences from Bottom-Left Variant

| Property              | Bottom-Left (default)              | Top-Left (`contentPosition: 'top'`)      |
| --------------------- | ---------------------------------- | ---------------------------------------- |
| Text anchor           | `absolute inset-x-0 bottom-0`     | `absolute inset-x-0 top-0`              |
| Gradient direction    | `to top` (dark at bottom)          | `to bottom` (dark at top)                |
| Gradient stops        | Same 3-stop values                 | Same 3-stop values                       |
| Content padding       | `var(--space-16)` (64px all)       | `var(--space-16)` (64px all)             |
| Typography            | Identical                          | Identical                                |
| CTA buttons           | Identical (Primary first)          | Identical (Primary first)                |
| Hover zoom            | Identical                          | Identical                                |
| Card dimensions       | 580×720px, radius 24px             | 580×720px, radius 24px                   |

### When to Use

- Use **bottom-left** (default) when the image focal point is at the top or center — text sits safely below
- Use **top-left** when the image focal point is at the bottom or center-bottom — text sits safely above
- Can mix both variants in the same grid for visual variety

---

## Image Card Variant — 3-Column (Service / Explore Grid)

A **3-column** variant of the Image Card used for "Explore our new services" or similar sections. Identical visual treatment as the 2x2 variant (full-bleed image, gradient overlay, white text, dual CTAs) but laid out in a single-row 3-column grid.

### Differences from the 2x2 Variant

| Property              | 2x2 Grid                         | 3-Column Grid                         |
| --------------------- | -------------------------------- | ------------------------------------- |
| Grid                  | `grid-cols-1 md:grid-cols-2`     | `grid-cols-1 md:grid-cols-3`          |
| Number of cards       | 4 (2x2)                          | 3 (1x3)                               |
| Section heading       | None                             | Section title above the grid           |
| Headline font-size    | `clamp(h4, 2.5vw, h3)`          | `clamp(h4, 2vw, h3)` (slightly smaller for narrower columns) |
| Card height           | `clamp(400px, 38vw, 520px)`     | `clamp(400px, 38vw, 520px)` (same)    |

Everything else — gradient overlay, typography tokens, CTA button spec, spacing, data structure, hover zoom — is **identical** to the 2x2 variant.

### Section Heading

The section has a title rendered as an `<h2>` above the grid:

```
font-family:  var(--font-family-jiotype)
font-size:    clamp(var(--text-h4), 3vw, var(--text-h3))
font-weight:  var(--font-weight-black)
color:        var(--foreground)
line-height:  1.2
text-align:   center
margin-bottom: mb-8 (32px)
```

> **All section titles and subtitles must be center-aligned** — both `text-align: center` on the text element and horizontally centered within the container. See `layout.md` and `typography.md` for the canonical rule.

### Layout

```
┌────────────────────────────────────────────────────┐
│  Explore our new services  (h2, JioType Black)     │
│                                                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │ Card 1   │  │ Card 2   │  │ Card 3   │         │
│  │ (image)  │  │ (image)  │  │ (image)  │         │
│  │          │  │          │  │          │         │
│  │ Brand    │  │ Brand    │  │ Brand    │         │
│  │ Title    │  │ Title    │  │ Title    │         │
│  │ [CTA][…] │  │ [CTA][…] │  │ [CTA][…] │         │
│  └──────────┘  └──────────┘  └──────────┘         │
│  gap-5 between cards                               │
└────────────────────────────────────────────────────┘
```

### Responsive Behavior

| Breakpoint | Columns   | Card height              |
| ---------- | --------- | ------------------------ |
| Mobile     | 1 column  | `400px` (clamp min)      |
| md+        | 3 columns | `~38vw` fluid, max 520px |

### When to Use

- Use the **2x2 variant** for main promotional grids (4 cards)
- Use the **3-column variant** for service/feature exploration sections (3 cards) with a section heading

---

## Icon Card Variant

The Icon Card is a lightweight content card featuring a prominent icon (instead of an image), a title, a body description, and a **tertiary CTA** (text-link style). It is used for feature highlights, service listings, and business solution showcases.

The component lives in `/src/app/components/IconCard.tsx` and exports both `IconCard` and `IconCardData`.

### Visual Structure

```
┌─────────────────────────────────────────┐
│  padding: var(--space-10) (desktop)     │
│  padding: var(--space-6) (mobile)       │
│                                         │
│  ┌──────┐                               │
│  │ Icon │  40x40px (desktop/tablet)     │
│  │  *   │  32x32px (mobile)             │
│  └──────┘  Icon: 32px (desktop/tablet)  │
│            Icon: 24px (mobile)          │
│                                         │
│  Card Title                             │
│  (h3, JioType Bold, 18px desktop,       │
│   16px mobile)                          │
│                                         │
│  Body text / description paragraph      │
│  (p, JioType Normal, 16px desktop,      │
│   14px mobile, --grey-80)               │
│                                         │
│  Know more ->                            │
│  (tertiary CTA, --primary-50,           │
│   --text-label, bold, ArrowRight icon)  │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **No image** — a JDS icon inside a container replaces the image area
2. **White background** (`--global-white`) — no grey, no layered cards
3. **Subtle border** (`1px solid var(--grey-40)`) — no shadow at rest
4. **Tertiary CTA** — text-link style, no background, no border; pushed to the bottom of the card via `mt-auto`
5. **Hover** — the CTA arrow translates right on card hover for interactivity
6. **Left-aligned content** — all content (icon, title, description, CTA) is aligned to the left

### Layout Rules

| Property              | Desktop/Tablet (≥768px)                   | Mobile (<768px)                          |
| --------------------- | ----------------------------------------- | ---------------------------------------- |
| Card border-radius    | `calc(var(--radius) * 2)` → 16px          | `calc(var(--radius) * 2)` → 16px         |
| Card border           | `1px solid var(--grey-40)`                | `1px solid var(--grey-40)`               |
| Card background       | `var(--global-white)`                     | `var(--global-white)`                    |
| Card shadow           | None                                      | None                                     |
| Card padding          | `var(--space-10)` (40px) all sides        | `var(--space-6)` (24px) all sides        |
| Card min-height       | 180px                                     | 180px                                    |
| Card display          | `flex flex-col h-full`                    | `flex flex-col h-full`                   |
| Icon container size   | `var(--space-10)` (40x40px)               | `var(--space-8)` (32x32px)               |
| Icon container radius | `calc(var(--radius) * 2)` → 16px          | `calc(var(--radius) * 2)` → 16px         |
| Icon size             | `w-8 h-8` (32px), `fill="currentColor"`   | `var(--space-6)` (24px)                  |

### Icon Container

The icon sits inside a container. The background and icon color are configurable per card:

| Property          | Token example           | Description                |
| ----------------- | ----------------------- | -------------------------- |
| Background        | `var(--primary-20)`     | Light tint from the `-20` scale (currently not visible in implementation) |
| Icon color        | `var(--global-black)`   | Standard black color for icons |

#### Recommended Icon Color Pairings

| Use case            | `iconBgToken`          | `iconColorToken`       |
| ------------------- | ---------------------- | ---------------------- |
| Primary / General   | `var(--primary-20)`    | `var(--primary-50)`    |
| Cloud / Green       | `var(--sparkle-20)`    | `var(--sparkle-60)`    |
| Security / Red      | `var(--error-20)`      | `var(--error-60)`      |
| Commerce / Amber    | `var(--secondary-20)`  | `var(--secondary-60)`  |
| Success / Green     | `var(--success-20)`    | `var(--success-60)`    |

### Typography

| Element            | Desktop/Tablet (≥768px)           | Mobile (<768px)                   |
| ------------------ | --------------------------------- | --------------------------------- |
| Title              | `--text-body-m` (18px)            | `--text-base` (16px)              |
| Title weight       | `--font-weight-bold` (700)        | `--font-weight-bold` (700)        |
| Description        | `--text-base` (16px)              | `--text-label` (14px)             |
| Description weight | `--font-weight-normal` (400)      | `--font-weight-normal` (400)      |
| Tertiary CTA label | `--text-label` (14px)             | `--text-label` (14px)             |
| CTA weight         | `--font-weight-bold` (700)        | `--font-weight-bold` (700)        |

All text uses `--font-family-jiotype`. Title color is `--foreground`, description color is `--grey-80`, CTA color is `--primary-50`.

### Tertiary CTA Button (text-link)

The tertiary button is a text-only link — no background, no border, no padding:

```
font-family:   var(--font-family-jiotype)
font-size:     var(--text-label)     -> 14px
font-weight:   var(--font-weight-bold) -> 700
color:         var(--primary-50)
line-height:   1.5
icon:          ArrowRight (w-4 h-4, fill="currentColor")
hover:         Arrow translates right 4px (translate-x-1)
alignment:     mt-auto — pushed to the bottom of the card
```

### Spacing

| Between                       | Token                           |
| ----------------------------- | ------------------------------- |
| Card padding (all sides)      | `var(--space-10)` (40px) desktop, `var(--space-6)` (24px) mobile |
| Icon -> Title                  | `var(--space-6)` (24px)         |
| Title -> Description           | `var(--space-2)` (8px)          |
| Description -> Tertiary CTA    | `var(--space-6)` (24px) + `mt-auto` |
| CTA label -> Arrow icon        | `var(--space-2)` (8px)          |

### Data Structure

```ts
import type { LucideIcon } from 'lucide-react';

interface IconCardData {
  id: number;
  icon: LucideIcon;          // Lucide icon component
  title: string;             // Card headline
  content: string;           // Body / description text
  cta: string;               // Tertiary CTA label (e.g. "Know more")
  iconBgToken: string;       // Icon circle background token
  iconColorToken: string;    // Icon color token
}
```

### Usage

```tsx
import { IconCard, IconCardData } from './IconCard';
import { Wifi } from 'lucide-react';

const card: IconCardData = {
  id: 1,
  icon: Wifi,
  title: 'JioBusiness Fiber',
  content: 'High-speed broadband built for enterprises with 99.9% uptime.',
  cta: 'Know more',
  iconBgToken: 'var(--primary-20)',
  iconColorToken: 'var(--primary-50)',
};

<IconCard card={card} />
```

### When to Use

- Use the **Icon Card** for feature/service listings where a simple icon represents the category
- Use it in horizontally-scrolling carousels or multi-column grids
- **Do not** use it for promotional content that requires product imagery — use the **Image Card** variant instead

### Carousel Layout (overflow-right)

When used in a horizontally-scrolling carousel (e.g. Section 5):

| Property                  | Value                                              |
| ------------------------- | -------------------------------------------------- |
| Carousel engine           | Embla Carousel (`align: 'start'`, `loop: false`)  |
| Card flex basis           | `clamp(260px, 26vw, 320px)`                       |
| Gap between cards         | `var(--space-5)` (20px)                            |
| Navigation arrows         | Bottom-right of section, pill-shaped (40x40px)    |
| Arrow border              | `1.5px solid var(--grey-40)`                       |
| Arrow disabled state      | `opacity: 0.5`, `color: var(--grey-60)`           |

---

## Story Card Variant

The Story Card is a content/editorial card featuring a **top image**, a **category badge**, a **title**, and a **tertiary CTA** (text-link). It is used for news stories, press releases, blog posts, and editorial content — typically displayed in horizontally-scrolling overflow carousels.

The component lives in `/src/app/components/StoryCard.tsx` and exports both `StoryCard` and `StoryCardData`.

### Visual Structure

```
┌─────────────────────────────────────────┐
│  padding: var(--space-3) (top/left/right│
│                                         │
│  ┌─────────────────────────────────┐    │
│  │                                 │    │
│  │   Image area (object-cover)     │    │
│  │   clamp(160px, 16vw, 200px)     │    │
│  │   border-radius: 24px ALL sides │    │
│  │   hover zoom (scale 1.05)       │    │
│  │                                 │    │
│  └────────────────────────────────┘    │
│                                         │
│  padding: var(--space-5) (content area) │
│                                         │
│  ┌──────────┐                           │
│  │  Badge   │  (JDS Badge component,    │
│  └──────────┘   rounded-md)             │
│                                         │
│  Card Title                             │
│  (--text-base, JioType Bold 700,        │
│   max 3 lines, ellipsis overflow)       │
│                                         │
│  Read more ->                            │
│  (tertiary CTA, --primary-50,           │
│   --text-label, bold, ArrowRight icon)  │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **Top image** — inset within the card with `var(--space-3)` padding (top/left/right), 24px border-radius on **all four corners**, `object-cover`
2. **White background** (`--global-white`) — no grey, no layered cards
3. **No border, no stroke** — the Story Card must never have any `border`, `outline`, or `box-shadow` — neither on the component root element nor on any wrapper/container that holds it (e.g. grid cells, carousel slides). The inset image and white background alone define the card boundary. **Consumers must not add borders around Story Cards.**
4. **Category badge** — uses the JDS `Badge` component from `/src/app/components/ui/badge.tsx` with `rounded-md` shape (not a pill)
5. **Title clamped to 3 lines** — uses `-webkit-line-clamp: 3` with overflow hidden
6. **Tertiary CTA** — text-link style, pushed to card bottom via `mt-auto`
7. **Hover** — image zooms subtly (scale 1.05), CTA arrow translates right

### Layout Rules

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |
| Card background       | `var(--global-white)`                         |
| Card border           | **None** — no `border`, `outline`, or `box-shadow` on the card or any wrapping element |
| Card shadow           | None                                          |
| Card display          | `flex flex-col h-full`                        |
| Image inset padding   | `var(--space-3)` (12px) top, left, right; 0 bottom |
| Image border-radius   | `calc(var(--radius) * 3)` -> 24px **all corners** |
| Image height          | `clamp(160px, 16vw, 200px)`                   |
| Image object-fit      | `object-cover`                                |
| Image overflow        | `hidden` (clips hover zoom)                   |
| Image hover           | `scale-105` over 500ms transition             |
| Content padding       | `var(--space-5)` (20px) all sides             |

### Badge (Category Tag)

**Must use the JDS `Badge` component** from `/src/app/components/ui/badge.tsx`. Do **not** create a custom pill-shaped badge — always import and render the `<Badge>` component directly.

The Badge component follows the JDS Badge specification (see `/guidelines/MD/Component/badge.md`). For Story Cards, use the **Informational** category with **Label Only (Text in Container)** variant, **XL** size, and **Subtle** emphasis. Override colors via `bgColor` and `textColor` props to apply per-card JDS tokens:

```tsx
import { Badge } from './ui/badge';

<Badge
  category="informational"
  variant="textInformational"
  size="xl"
  emphasis="subtle"
  bgColor={card.badgeBgToken}
  textColor={card.badgeTextToken}
>
  {card.badge}
</Badge>
```

| Property          | Value                                    |
| ----------------- | ---------------------------------------- |
| Component         | `Badge` from `/src/app/components/ui/badge.tsx` |
| Category          | `informational` (JDS Badge API)          |
| Variant           | `textInformational` (Label only with container) |
| Size              | `xl` (24px height)                       |
| Emphasis          | `subtle` (light background)              |
| Border radius     | `4px` — auto-applied                     |
| Padding           | `4px L/R × 2px T/B` — auto-applied       |
| Font family       | `var(--font-family-jiotype)` — auto-applied |
| Font size         | `var(--text-base)` (16px / body-l-bold) — auto-applied |
| Font weight       | `var(--font-weight-bold)` (700) — auto-applied |
| Background        | Per-card token (e.g. `var(--primary-20)`) via `bgColor` prop |
| Text color        | Per-card token (e.g. `var(--primary-60)`) via `textColor` prop |

**Important:** All informational badges use `body-l-bold` typography (16px, `--text-base`) regardless of badge size per JDS specifications.

#### Recommended Badge Color Pairings

| Category          | `badgeBgToken`          | `badgeTextToken`        |
| ----------------- | ----------------------- | ----------------------- |
| Network / Tech    | `var(--primary-20)`     | `var(--primary-60)`     |
| Innovation / AI   | `var(--sparkle-20)`     | `var(--sparkle-60)`     |
| Education         | `var(--secondary-20)`   | `var(--secondary-60)`   |
| Entertainment     | `var(--error-20)`       | `var(--error-60)`       |
| Sustainability    | `var(--success-20)`     | `var(--success-60)`     |
| Healthcare        | `var(--sparkle-20)`     | `var(--sparkle-60)`     |

### Typography

| Element            | Token                     | Style                          |
| ------------------ | ------------------------- | ------------------------------ |
| Badge label        | `--text-base` (16px)      | `--font-weight-bold` (700)     |
| Title              | `--text-base` (16px)      | `--font-weight-bold` (700)     |
| Tertiary CTA label | `--text-label` (14px)     | `--font-weight-bold` (700)     |

All text uses `--font-family-jiotype`. Title color is `--foreground`, CTA color is `--primary-50`.

Title uses `-webkit-line-clamp: 3` with `overflow: hidden` and `-webkit-box-orient: vertical` to limit to 3 lines.

### Tertiary CTA Button (text-link)

Identical to the Icon Card tertiary CTA:

```
font-family:   var(--font-family-jiotype)
font-size:     var(--text-label)     -> 14px
font-weight:   var(--font-weight-bold) -> 700
color:         var(--primary-50)
line-height:   1.5
icon:          ArrowRight (w-4 h-4, fill="currentColor")
hover:         Arrow translates right 4px (translate-x-1)
alignment:     mt-auto — pushed to the bottom of the card
```

### Spacing

| Between                       | Token                           |
| ----------------------------- | ------------------------------- |
| Content padding (all sides)   | `var(--space-5)` (20px)         |
| Badge -> Title                 | `var(--space-3)` (12px)         |
| Title -> Tertiary CTA          | `var(--space-5)` (20px) + `mt-auto` |
| CTA label -> Arrow icon        | `var(--space-2)` (8px)          |

### Data Structure

```ts
interface StoryCardData {
  id: number;
  image: string;           // Image URL (Unsplash or figma:asset)
  alt: string;             // Accessibility alt text
  title: string;           // Card headline / title
  cta: string;             // Tertiary CTA label (e.g. "Read more")
  badge: string;           // Category badge label (e.g. "Network")
  badgeBgToken: string;    // Badge background token
  badgeTextToken: string;  // Badge text color token
}
```

### Usage

```tsx
import { StoryCard, StoryCardData } from './StoryCard';

const story: StoryCardData = {
  id: 1,
  image: 'https://images.unsplash.com/...',
  alt: '5G telecom tower in rural India',
  title: 'Jio expands True 5G coverage to 500+ cities across India',
  cta: 'Read more',
  badge: 'Network',
  badgeBgToken: 'var(--primary-20)',
  badgeTextToken: 'var(--primary-60)',
};

<StoryCard card={story} />
```

### When to Use

- Use the **Story Card** for news, press releases, blog posts, and editorial content
- Use it in horizontally-scrolling carousels with overflow on the right
- **Do not** use it for service or product feature highlights — use the **Icon Card** or **Image Card** variant instead

### Carousel Layout (overflow-right)

When used in a horizontally-scrolling carousel (e.g. Section 6):

| Property                  | Value                                              |
| ------------------------- | -------------------------------------------------- |
| Carousel engine           | Embla Carousel (`align: 'start'`, `loop: false`)  |
| Card flex basis           | `clamp(260px, 26vw, 320px)`                       |
| Gap between cards         | `var(--space-5)` (20px)                            |
| Navigation arrows         | Bottom-right of section, pill-shaped (40x40px)    |
| Arrow border              | `1.5px solid var(--grey-40)`                       |
| Arrow disabled state      | `opacity: 0.5`, `color: var(--grey-60)`           |

---

## Base Card Variant (UI Card)

The base card from `/src/app/components/ui/card.tsx` is used for non-promotional content (features, info panels, forms). It uses:

- `bg-card` / `text-card-foreground` tokens
- `border-border` with `--elevation-sm` shadow
- `rounded-lg` (var(--radius))
- Composed of: `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, `CardFooter`

---

## Usage Guidelines

1. **Always use JDS tokens** for all colors — never hardcode hex values
2. **Font-family** must always be `var(--font-family-jiotype)`
3. **Font weights** use token references: `--font-weight-black`, `--font-weight-bold`, `--font-weight-medium`, `--font-weight-normal`
4. **Font sizes** use token references: `--text-h1` through `--text-label`
5. **Border radius** uses `var(--radius)` (8px) or `var(--radius-button)` (250px) for pills
6. **The Image Card variant must be followed exactly on all pages** where 2x2 promotional grid cards are needed — full-bleed image, gradient overlay, white text, dual CTAs

---

## Product Card Variant (Shop Grid)

The Product Card is a commerce-oriented card variant used on the **Shop page** (`/shop`). It features a product image at top, a category badge, product name, description, price, and a primary CTA button. Optional "New" badges overlay the image.

Component: `/src/app/components/ShopProductCard.tsx`

### Visual Structure

```
┌─────────────────────────────────────────┐
│  padding: var(--space-3) (image inset)  │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │   [New]  (optional overlay)     │    │
│  │                                 │    │
│  │   Product Image                 │    │
│  │   (object-cover, hover zoom)    │    │
│  │   border-radius: var(--radius-lg)│   │
│  │                                 │    │
│  └─────────────────────────────────┘    │
│                                         │
│  padding: var(--space-5) (content area) │
│                                         │
│  ┌──────────┐                           │
│  │  Badge   │  (JDS Badge component)    │
│  └──────────┘                           
│                                         │
│  Product Name                           │
│  (--text-body-m, 18px, black 900)       │
│                                         │
│  Description (2-line clamp)             │
│  (--text-label, 14px, normal 400,       │
│   --grey-80)                            │
│                                         │
│  ₹X,XXX / Starting ₹XXX/mo             │
│  (--text-base, 16px, bold 700,          │
│   --primary-60)                         │
│                                         │
│  [ Primary CTA → ]  (full-width)        │
│   (JDS Button, variant="default",       │
│    size="sm", with ArrowRight icon)     │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **White background** (`--global-white`) with subtle border (`--grey-40`)
2. **Inset image** — top area has `var(--space-3)` padding, image has `var(--radius-lg)` border-radius
3. **Hover lift** — card lifts 2px with `var(--shadow-card-md)` shadow on hover
4. **Image zoom** — `scale(1.05)` over 500ms transition on image hover
5. **"New" badge** — sparkle-60 bg, white text, pill shape, positioned top-left over image
6. **Full-width CTA** — primary JDS Button with ArrowRight icon, pushed to bottom via `mt-auto`

### Layout Rules

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |
| Card background       | `var(--global-white)`                         |
| Card border           | `var(--border-width-thin) solid var(--grey-40)` |
| Card border-radius    | `calc(var(--radius) * 2)` → 16px              |
| Card shadow (rest)    | None                                          |
| Card shadow (hover)   | `var(--shadow-card-md)`                       |
| Card hover transform  | `translateY(-2px)`                            |
| Card display          | `flex flex-col h-full`                        |
| Image inset padding   | `var(--space-3)` (12px) top, left, right      |
| Image border-radius   | `var(--radius-lg)` (24px)                     |
| Image height          | `clamp(180px, 20vw, 240px)`                   |
| Image object-fit      | `object-cover`                                |
| Image hover           | `scale-105` over 500ms transition             |
| Content padding       | `var(--space-5)` (20px) all sides             |

### "New" Badge Overlay

| Property          | Value                                    |
| ----------------- | ---------------------------------------- |
| Position          | `absolute top-left` inside image area    |
| Offset            | `var(--space-3)` from top and left       |
| Background        | `var(--sparkle-60)`                      |
| Text color        | `var(--global-white)`                    |
| Font size         | `var(--text-footnote)` (11px)            |
| Font weight       | `var(--font-weight-bold)` (700)          |
| Border radius     | `var(--radius-tag)` (80px)               |
| Padding           | `var(--space-1) var(--space-3)`          |
| Text transform    | `uppercase`                              |

### Typography

| Element            | Token                     | Style                          |
| ------------------ | ------------------------- | ------------------------------ |
| Product name       | `--text-body-m` (18px)    | `--font-weight-black` (900)    |
| Description        | `--text-label` (14px)     | `--font-weight-normal` (400)   |
| Price              | `--text-base` (16px)      | `--font-weight-bold` (700)     |
| CTA button         | JDS Button default        | Inherited from button.tsx      |
| Badge              | JDS Badge outline variant | Inherited from badge.tsx       |

All text uses `--font-family-jiotype`. Product name color is `--foreground`, description is `--grey-80`, price is `--primary-60`.

Description uses `-webkit-line-clamp: 2` with overflow hidden.

### Spacing

| Between                       | Token                           |
| ----------------------------- | ------------------------------- |
| Image inset padding           | `var(--space-3)` (12px)         |
| Content padding               | `var(--space-5)` (20px)         |
| Badge → Product name          | `var(--space-3)` (12px)         |
| Product name → Description    | `var(--space-2)` (8px)          |
| Description → Price           | `var(--space-3)` (12px)         |
| Price → CTA button            | `var(--space-5)` (20px) + `mt-auto` |

### Grid Layout (Shop page)

| Property                  | Value                                    |
| ------------------------- | ---------------------------------------- |
| Grid                      | `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4` |
| Grid gap                  | `var(--space-6)` (24px)                  |
| Container                 | `container mx-auto` (1184px stopper)     |
| Animation                 | Motion `AnimatePresence` with stagger    |

### Data Structure

```ts
interface ProductData {
  id: number;
  name: string;            // Product name (e.g. "JioFiber")
  description: string;     // 1-2 sentence description
  price: string;           // e.g. "Starting ₹399/mo" or "₹1,999"
  category: ShopCategory;  // "Connectivity" | "Entertainment" | "Smart Devices" | "Business Solutions"
  image: string;           // Unsplash URL
  alt: string;             // Accessibility alt text
  badgeLabel: string;      // Category/type badge (e.g. "Broadband", "Streaming")
  badgeVariant?: 'default' | 'secondary' | 'outline';  // JDS Badge variant
  cta: string;             // CTA button label (e.g. "Buy Now", "Get Quote")
  isNew?: boolean;         // Shows "New" overlay badge
}
```

### Usage

```tsx
import { ShopProductCard, ProductData } from './ShopProductCard';

const product: ProductData = {
  id: 1,
  name: 'JioFiber',
  description: 'Blazing-fast fiber broadband up to 1 Gbps.',
  price: 'Starting ₹399/mo',
  category: 'Connectivity',
  image: 'https://images.unsplash.com/...',
  alt: 'JioFiber broadband router',
  badgeLabel: 'Broadband',
  cta: 'Get JioFiber',
  isNew: false,
};

<ShopProductCard product={product} />
```

### When to Use

- Use the **Product Card** for commerce/shop catalogue listings
- Use it in responsive CSS grids with 1–4 columns
- **Do not** use it for editorial/news content (use Story Card) or promotional banners (use Image Card)

---

## Product Card Variant — Compact (Carousel)

The Product Card Compact variant is a streamlined product card optimized for carousel layouts. It features a full-bleed background image with gradient overlay, logo/brand name, description, and a secondary inverse CTA button. This variant uses a **top-aligned content layout** where the text and CTA are positioned at the top of the card, while the background image's main focus area is positioned at the bottom for optimal visual balance.

**Responsive Heights:**
- **Mobile (< 992px):** 416px
- **Desktop (≥ 992px):** 504px

Component: `/src/app/components/ProductCard.tsx`

### Visual Structure

```
┌─────────────────────────────────────────┐
│  Content (pinned to top)                │
│                                         │
│  Logo / Brand Name                      │
│  (clamp(18px-24px), JioType Black 900,  │
│   white text)                           │
│                                         │
│  Description text (3-line clamp)        │
│  (--text-label, 14px, normal 400,       │
│   white with 0.9 opacity)               │
│                                         │
│  [ Secondary CTA ]                      │
│   (white outline button, size sm)       │
│  ────────────────────────────────────   │
│                                         │
│  Full-bleed background image            │
│  (object-cover, fills entire card)      │
│  Gradient overlay (top-to-bottom)       │
│  Image focus area at bottom             │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **Full-bleed image** — background image fills entire card with `object-cover` and `object-position: center bottom`
2. **Gradient overlay** — top-to-bottom gradient (`var(--gradient-card-ttb)`) provides text contrast for top-aligned content
3. **Top-aligned content** — logo, description, and CTA positioned at top using `justify-start` flex layout
4. **Image focus at bottom** — `object-position: center bottom` ensures main subject/focus area of image appears at bottom
5. **All text is white** — sits on dark gradient overlay for readability
6. **Secondary inverse CTA** — white outline button with transparent background
7. **Hover zoom** — image scales 1.05 over 500ms transition
8. **Responsive height** — 416px on mobile, 504px on desktop using `.product-card-compact` CSS class
9. **3-line description clamp** — description limited to 3 lines with ellipsis overflow

### Layout Rules

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |
| Card border-radius    | `var(--radius-lg)` (24px)                     |
| Card height (mobile)  | `var(--card-product-compact-height-mobile)` (416px) |
| Card height (desktop) | `var(--card-product-compact-height-desktop)` (504px) |
| Card background       | `var(--grey-20)` (fallback)                   |
| Card overflow         | `hidden` (clips hover zoom)                   |
| Image position        | `absolute inset-0` (fills card)               |
| Image object-fit      | `object-cover`                                |
| Image object-position | `center bottom` (focus area at bottom)        |
| Image hover           | `scale-105` over 500ms transition             |
| Gradient overlay      | `var(--gradient-card-ttb)` (top-to-bottom)    |
| Content position      | Flex column, justify-start (pinned to top)    |
| Content padding       | `clamp(var(--space-4), 4vw, var(--space-6))`  |

**CSS Class:** `.product-card-compact` — Apply this class to enable responsive height behavior (defined in `/src/styles/theme.css`).

### Typography

| Element            | Token                                    | Style                          |
| ------------------ | ---------------------------------------- | ------------------------------ |
| Logo / Brand name  | `clamp(var(--text-body-m), 2vw, var(--text-h4))` | `--font-weight-black` (900)    |
| Logo color         | `var(--global-white)`                    | N/A                            |
| Description        | `--text-label` (14px)                    | `--font-weight-normal` (400)   |
| Description color  | `var(--global-white)` with 0.9 opacity   | N/A                            |
| CTA button         | JDS Button secondaryInverse, size sm     | Inherited from button.tsx      |

All text uses `--font-family-jiotype`. Description uses `-webkit-line-clamp: 3` with overflow hidden.

### Secondary Inverse CTA Button

The button uses the `secondaryInverse` variant with `sm` size:

```
variant:       secondaryInverse
size:          sm (40px height)
border-radius: var(--radius-button)     → 250px (full pill)
background:    transparent
color:         var(--global-white)
border:        var(--border-width-medium) solid var(--global-white)
padding:       px-6 (var(--space-6))
font-size:     var(--text-button)       → 16px
font-weight:   var(--font-weight-bold)  → 700
```

### Spacing

| Between                       | Token                           |
| ----------------------------- | ------------------------------- |
| Content padding (all sides)   | `clamp(var(--space-4), 4vw, var(--space-6))` |
| Logo → Description            | `var(--space-2)` (8px)          |
| Description → CTA button      | `var(--space-4)` (16px)         |

### Carousel Layout — Responsive Overflow-Right Pattern

When used in a horizontally-scrolling carousel (e.g., "Now do more with your TV" section):

| Property                  | Value                                              |
| ------------------------- | -------------------------------------------------- |
| Carousel engine           | Embla Carousel with `dragFree: true`, `containScroll: false` |
| Carousel align            | `'start'`, `loop: false`, `skipSnaps: false`      |
| **Mobile Card flex basis** | `calc(85% - 10px)` — 1 full card + peek of next  |
| **Tablet Card flex basis** | `calc(50% - 10px)` — 2 cards visible             |
| **Desktop Card flex basis** | `calc(30% - 14px)` — 3 full cards + peek of 4th |
| Card min-width            | `280px`                                            |
| Gap between cards         | `var(--space-5)` (20px)                            |
| Carousel padding-left     | `max(var(--container-padding-mobile), calc((100% - var(--container-max-width)) / 2 + var(--container-padding-desktop)))` |
| Navigation arrows         | Bottom-right inside container, 44x44px buttons    |
| **Arrow visibility**      | **Hidden on mobile**, visible on desktop (≥992px) |
| Arrow border              | `var(--border-width-medium) solid var(--grey-40)` |
| Arrow disabled state      | `opacity: 0.3`, `color: var(--grey-60)`           |

**Implementation Notes:**
- **Mobile (< 768px)** — Single card visible at ~85% width with peek of next card; navigation arrows hidden (swipe/drag only)
- **Tablet (768px - 991px)** — 2 cards visible at 50% width each
- **Desktop (≥992px)** — 3 full cards visible + partial 4th card (~30% each) with navigation arrows
- **Overflow-right carousel** — Cards overflow to the right with special padding that aligns the first card with the container edge while allowing overflow
- **Drag-free scrolling** — `dragFree: true` enables smooth, continuous scrolling on mobile without snapping
- **Peek effect** — Partial visibility of next card encourages horizontal scrolling on all breakpoints
- **Container alignment** — Navigation arrows sit inside `.container` for proper grid alignment

### CSS Variables & Responsive Heights

The Product Card Compact uses CSS variables defined in `/src/styles/theme.css`:

```css
/* Card Height Tokens */
--card-product-compact-height-desktop: 504px;
--card-product-compact-height-mobile: 416px;

/* Responsive Class */
.product-card-compact {
  height: var(--card-product-compact-height-mobile); /* Mobile: 416px */
}

@media (min-width: 992px) {
  .product-card-compact {
    height: var(--card-product-compact-height-desktop); /* Desktop: 504px */
  }
}
```

This approach allows you to update card heights globally by editing the CSS variables in `theme.css`.

### Data Structure

```ts
interface ProductCardData {
  id: number;
  logo: string;           // Brand/product name (e.g. "JioTV+")
  description: string;    // Product description (max 3 lines)
  cta: string;            // CTA button label (e.g. "Know more")
  image: string;          // Background image URL (Unsplash or figma:asset)
  alt: string;            // Accessibility alt text
}
```

### Usage

```tsx
import { ProductCard, ProductCardData } from './ProductCard';

const product: ProductCardData = {
  id: 1,
  logo: 'JioTV+',
  description: "India's first integrated TV platform with movies, TV shows & videos from OTT apps.",
  cta: 'Know more',
  image: 'https://images.unsplash.com/...',
  alt: 'Family watching smart TV in living room',
};

<ProductCard card={product} />
```

### When to Use

- Use the **Product Card Compact** for product showcases in carousels (e.g. "Now do more with your TV" section)
- Use it in responsive carousel layouts with peek effect (1 card on mobile, 2 on tablet, 3+ on desktop)
- Card height: **416px on mobile**, **504px on desktop** for consistent vertical rhythm
- **Do not** use it for commerce/shop catalogue listings (use standard Product Card instead)
- **Do not** use it for editorial content (use Story Card)

---

## Shopping Card Variant

The Shopping Card is a premium commerce card variant optimized for high-conversion shopping experiences. It features a 1:1 aspect ratio product image with a status badge overlay, bold product title, prominent pricing with strikethrough MRP and savings badge, and a dual-button CTA group.

Component: `/src/app/components/ShoppingCard.tsx`

### Visual Structure

```
┌─────────────────────────────────────────┐
│                                         │
│  ┌─────────────────────────────────┐    │
│  │   [TRENDING]  (badge overlay)   │    │
│  │                                 │    │
│  │   Product Image (1:1 ratio)     │    │
│  │   Desktop/Tablet: 24px radius   │    │
│  │   Mobile: 16px radius           │    │
│  │                                 │    │
│  └─────────────────────────────────┘    │
│                                         │
│  padding: var(--space-4) (content area) │
│                                         │
│  Product Name                           │
│  (--text-body-m, 18px, bold 700)        │
│                                         │
│  ₹X,XXX  ₹XX,XXX  [Save XX%]           │
│  (price) (MRP strikethrough) (badge)    │
│  (--text-label, 14px)                   │
│                                         │
│  [ Buy now ]  [ Learn more ]           │
│   (Primary)     (Secondary)             │
│   (responsive button group)             │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **1:1 Image Ratio** — Square product image ensures consistent grid alignment
2. **Top-left Badge Overlay** — Informational badge (e.g., "TRENDING", "NEW LAUNCH") in uppercase, positioned over image, **L size with Bold emphasis**
3. **Responsive Border Radius** — Image uses 24px on desktop/tablet, 16px on mobile
4. **Compact Typography** — Product title uses body-m-bold (18px), pricing uses body-s (14px)
5. **Savings Badge** — Success-variant badge highlights the discount percentage
6. **Dual CTA Group** — Primary and Secondary buttons with responsive layout
7. **No Border or Padding** — Card has clean edge-to-edge appearance

### Layout Rules

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |                                   |
| Image container       | `position: relative`                          |
| Image aspect ratio    | `1:1` (square)                                |
| Image border-radius   | Desktop/Tablet: `calc(var(--radius) * 3)` → 24px<br>Mobile: `calc(var(--radius) * 2)` → 16px |
| Image object-fit      | `object-cover`                                |
| Badge padding         | `var(--space-4)` (16px) from top and left     |
| Content padding       | `var(--space-4)` (16px) top only — no left/right/bottom padding |
| Hover state           | None — card has no hover effects              |

### Status Badge Overlay (Top-Left)

The badge is positioned absolutely over the top-left corner of the product image.

| Property          | Value                                    |
| ----------------- | ---------------------------------------- |
| Position          | `absolute top-left` inside image area    |
| Offset            | `var(--space-3)` from top and left       |
| Badge Category    | `informational`                          |
| Badge Variant     | `textInformational` (sparkle colors)     |
| Badge Size        | `l` (20px height)                        |
| Badge Emphasis    | `bold` (strong background)               |
| Text Transform    | `uppercase`                              |
| Badge Text        | e.g., "TRENDING", "NEW LAUNCH"           |

### Typography

| Element            | Token                       | Weight                       | Color             |
| ------------------ | --------------------------- | ---------------------------- | ----------------- |
| Product title      | `--text-body-m` (18px)      | `--font-weight-bold` (700)   | `--grey-100`      |
| Price (current)    | `--text-label` (14px)       | `--font-weight-bold` (700)   | `--grey-100`      |
| MRP (strikethrough)| `--text-label` (14px)       | `--font-weight-normal` (400) | `--grey-80`       |
| CTA buttons        | JDS Button default          | Inherited from button.tsx    | Per button variant|

All text uses `--font-family-jiotype`.

### Pricing & Savings Badge Layout

The pricing area displays horizontally with three elements:

1. **Current Price** — `₹X,XXX` in `--grey-100`, bold
2. **MRP Price** — `₹XX,XXX` with `text-decoration: line-through` in `--grey-80`, bold
3. **Savings Badge** — JDS Badge component (Informational category, Positive colorScheme, L size, Subtle emphasis)

Layout:
```tsx
<div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-2)', flexWrap: 'wrap' }}>
  <span>₹1,799</span>
  <span style={{ textDecoration: 'line-through' }}>₹2,999</span>
  <Badge category="informational" variant="textInformational" colorScheme="positive" emphasis="subtle" size="l">Save 40%</Badge>
</div>
```

### Button Group — Responsive Behavior

The button group displays responsively based on device size:

**Desktop & Tablet (≥768px):**
- Buttons are displayed side-by-side (horizontally)
- Buttons are **NOT** full-width — they fit content naturally
- Gap between buttons: `var(--space-3)` (12px)
- Container: `flex flex-row` with `gap: var(--space-3)`

**Mobile (<768px):**
- Buttons are displayed stacked (vertically)
- Buttons are **full-width** — each button spans 100% width
- Gap between buttons: `var(--space-3)` (12px)
- Container: `flex flex-col` with `gap: var(--space-3)`

| Property       | Primary CTA              | Secondary CTA            |
| -------------- | ------------------------ | ------------------------ |
| Variant        | `default`                | `secondary`              |
| Size           | `default` (48px)         | `default` (48px)         |
| Desktop Width  | Auto (fits content)      | Auto (fits content)      |
| Mobile Width   | 100% (full-width)        | 100% (full-width)        |
| Label          | "Buy now"                | "Learn more"             |
| Icon           | None (optional)          | None (optional)          |

```tsx
// Desktop/Tablet (≥768px): Horizontal layout
<div className="flex flex-row gap-[var(--space-3)]">
  <Button variant="default" size="default">Buy now</Button>
  <Button variant="secondary" size="default">Learn more</Button>
</div>

// Mobile (<768px): Vertical layout with full-width buttons
<div className="flex flex-col gap-[var(--space-3)]">
  <Button variant="default" size="default" className="w-full">Buy now</Button>
  <Button variant="secondary" size="default" className="w-full">Learn more</Button>
</div>
```

### Spacing

| Between                       | Token                           |
| ----------------------------- | ------------------------------- |
| Card padding                  | None (0px)                      |
| Content padding (top only)    | `var(--space-4)` (16px)         |
| Content padding (left/right)  | None (0px) — aligns flush with image |
| Badge offset from image edge  | `var(--space-4)` (16px)         |
| Image → Product title         | `var(--space-4)` (16px)         |
| Product title → Pricing       | `var(--space-3)` (12px)         |
| Pricing → Button group        | `var(--space-4)` (16px)         |
| Price elements gap            | `var(--space-2)` (8px)          |
| Button gap (desktop/tablet)   | `var(--space-3)` (12px)         |
| Button gap (mobile)           | `var(--space-3)` (12px)         |

### Grid Layout

| Property                  | Value                                    |
| ------------------------- | ---------------------------------------- |
| Grid                      | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4` |
| Grid gap                  | `var(--space-6)` (24px)                  |
| Container                 | `container mx-auto` (1184px stopper)     |

### Data Structure

```ts
interface ShoppingCardData {
  id: number;
  name: string;            // Product name/title
  image: string;           // Product image URL (1:1 ratio recommended)
  alt: string;             // Accessibility alt text
  price: string;           // Current price (e.g., "₹1,799")
  originalPrice: string;   // MRP price (e.g., "₹2,999")
  saveBadge: string;       // Savings text (e.g., "Save 40%")
  statusBadge?: string;    // Optional status badge (e.g., "TRENDING", "NEW LAUNCH")
  primaryCta: string;      // Primary button label (e.g., "Buy now")
  secondaryCta: string;    // Secondary button label (e.g., "Learn more")
}
```

### Usage

```tsx
import { ShoppingCard, ShoppingCardData } from './ShoppingCard';

const product: ShoppingCardData = {
  id: 1,
  name: 'JioBharat',
  image: 'https://images.unsplash.com/...',
  alt: 'JioBharat feature phone',
  price: '₹1,799',
  originalPrice: '₹2,999',
  saveBadge: 'Save 40%',
  statusBadge: 'TRENDING',
  primaryCta: 'Buy now',
  secondaryCta: 'Learn more',
};

<ShoppingCard product={product} />
```

### When to Use

- Use the **Shopping Card** for premium commerce experiences with high-conversion focus
- Use it in promotional shopping sections, featured product grids, or sale campaigns
- Ideal for products with significant discounts where the savings should be prominently displayed
- **Do not** use for basic product catalog listings (use Product Card instead)
- **Do not** use for editorial content (use Story Card)

---

## Plan Card Variant

The Plan Card is a telecom-specific card displaying pricing plans with validity, speed benefits, OTT offerings, and optional CTAs. It supports **4 variants**: View Only, Actionable Default Small, Actionable Default Large, and Actionable Business — each optimized for different use cases and grid layouts.

The component lives in `/src/app/components/JioHomePlanCard.tsx` and exports both `JioHomePlanCard` and `PlanCardData`.

### Key Principles

1. **All variants use JDS design tokens exclusively** — no arbitrary values
2. **Base padding** = `var(--space-6)` (24px) for all card interiors
3. **Rupee symbol (₹) is always part of the price text** — no separate styling
4. **Responsive grid behavior** — cards adapt from 1 column (mobile) to specified column counts (desktop)
5. **All typography uses JioType font family** exclusively

---

## Plan Card — View Only Variant

The **View Only** variant is the current implementation in the project — a simple, non-actionable card showing plan pricing, validity, speed, and OTT benefits. Used for plan comparisons and information display.

### Visual Structure

```
┌─────────────────────────────────────────┐
│  bg: var(--primary-20)                  │
│  padding: var(--space-6) (24px)         │
│                                         │
│  ₹Price          [chevron-right-icon]  │  ← row 1 (top section)
│  (h3, Black 900) (icon-only button)   │
│                                         │  ← 16px margin-top
│  ─────────────────────────────────────  │  ← Divider: var(--grey-40), 1px
│                                         │  ← 16px margin-bottom
│  Bill cycle   Upto speed   +N          │  ← row 2 (bottom section, stacked)
│  28 days      30 Mbps                   │
│  (footnote)   (footnote, bold)          │
│                                         │
└─────────────────────────────────────────┘
```

### Key Principles

1. **Light primary background** (`var(--primary-20)`) — subtle branded tint
2. **Right chevron button** — icon-only tertiary button, no background, no border
3. **Divider** — 1px `var(--grey-40)` between price row and detail columns, with 16px (`var(--space-4)`) margin top and bottom
4. **Stacked detail columns** — header/value pairs at 11px (`--text-footnote`), equal spacing (`flex: 1`), no dividers between columns
5. **No actionable CTA** — this is a view-only card
6. **No external content** — no badges or labels outside the card container
7. **Subtle hover shadow** — `hover:shadow-md` for interactivity cue

### Layout Rules

| Property              | Value                                          |
| --------------------- | ---------------------------------------------- |
| Background            | `var(--primary-20)`                            |
| Border                | `var(--border-width-thin) solid var(--grey-40)`|
| Border radius         | `calc(var(--radius) * 2)` → 16px               |
| Padding               | `var(--space-2) var(--space-4) var(--space-3) var(--space-4)` (8px 16px 12px 16px) |
| Vertical spacing      | Margin-based (no flex gap) — divider controls spacing |
| Divider               | 1px `var(--grey-40)`, margin: `var(--space-4)` top & bottom (16px) |
| Display               | `flex flex-col`                                |
| Hover effect          | `shadow-md` transition                         |

### Typography

| Element            | Font size             | Font weight              | Color                |
| ------------------ | --------------------- | ------------------------ | -------------------- |
| Price              | `var(--text-h3)` (32px) | `var(--font-weight-black)` (900) | `var(--foreground)` |
| Detail header      | `var(--text-footnote)` (11px) | `var(--font-weight-normal)` (400) | `var(--grey-80)` |
| Detail value       | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700) | `var(--foreground)` |
| More count         | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700) | `var(--primary-50)` |

### Chevron Button (Icon-Only, No Background)

```
Component:      Button (from /src/app/components/ui/button.tsx)
Variant:        tertiary
Size:           icon (size-10, 40px square)
Background:     transparent (no background)
Border:         none (no border)
Icon:           IcChevronRight (@jds/core-icons)
Icon size:      w-5 h-5 (20px)
Icon color:     var(--primary-60) (inherits from tertiary variant)
Position:       Right side of price row (flex justify-between)
```

### Spacing

| Between                  | Token                           |
| ------------------------ | ------------------------------- |
| Card padding (T R B L)   | `var(--space-2) var(--space-4) var(--space-3) var(--space-4)` (8px 16px 12px 16px) |
| Divider margin (top)     | `var(--space-4)` (16px)         |
| Divider margin (bottom)  | `var(--space-4)` (16px)         |
| Between detail columns   | `var(--space-4)` (16px)         |
| Detail column sizing     | `flex: 1` (equal width)         |

### Data Structure

```ts
export interface PlanCardData {
  id: number;
  price: string;           // e.g. "₹199" — includes rupee symbol
  billCycle: string;       // e.g. "Bill cycle:"
  validity: string;        // e.g. "28 Days"
  speed: string;           // e.g. "Upto:"
  benefits: string;        // e.g. "30 Mbps"
  avatarColors: string[];  // Array of CSS color tokens for OTT icons
  moreCount: string;       // e.g. "+10 more"
}
```

### Grid Layout

| Breakpoint   | Columns   | Gap                      |
| ------------ | --------- | ------------------------ |
| Mobile (<768px) | 1 column | `var(--space-6)` (24px) |
| md+ (≥768px) | 3 columns | `var(--space-6)` (24px) |

**Grid classes:** `grid grid-cols-1 md:grid-cols-3 gap-[var(--space-6)]`

### Responsive Behavior

- **Mobile (<768px):** Single column, full-width cards, all typography and spacing maintained
- **Desktop (≥768px):** 3-column grid, cards stretch to fill available space

### Accessibility

- Chevron button is focusable and keyboard-accessible
- Use semantic `<div>` with proper color contrast (WCAG AA compliant)
- Price text uses high-contrast color (`--foreground`)
- Hover states provide visual feedback

---

## Plan Card — Actionable Default Small Variant

The **Actionable Default Small** variant features an **informational badge** (secondary color, subtle emphasis) from the JDS Badge component and a "TRUE 5G" label flush against the card container. The card uses compact padding (`var(--space-2) var(--space-4) var(--space-3) var(--space-4)` = 8px 16px 12px 16px) with a `var(--space-3)` (12px) vertical gap between all elements. Detail columns have **no dividers** between them. The CTA is a **small primary** button. Used for plan selection flows.

### Visual Structure

```
   [Badge: secondary subtle]  [TRUE 5G]
┌─────────────────────────────────────────┐  ← no gap between badges and card
│  bg: var(--primary-20)                  │
│  padding: 8px 16px 12px 16px           │
│  (--space-2 --space-4 --space-3 --space-4) │
│  vertical gap: var(--space-3) (12px)   │
│                                         │
│  ₹Price          [chevron-right-icon]  │  ← row 1
│  (h3, Black 900) (icon-only button)   │
│                                         │  ← 12px gap (flex gap)
│  Bill cycle   Data        +N            │  ← row 2 (no dividers between cols)
│  28 days      2 GB/day                  │
│  (footnote)   (footnote, bold)          │
│                                         │  ← 12px gap
│  ─────────────────────────────────────  │  ← divider
│                                         │  ← 12px gap
│  [   Primary CTA Button (sm, full-w)   ]│  ← row 3
│  (small size, primary filled)          │
│                                         │
└─────────────────────────────────────────┘
```

### Key Differences from View Only

Both variants share the same base layout: compact padding (8px 16px 12px 16px), icon-only tertiary chevron, stacked header/value detail columns with equal spacing, and no dividers between columns.

| Property              | View Only                      | Actionable Default Small           |
| --------------------- | ------------------------------ | ---------------------------------- |
| CTA button            | None                           | Full-width small primary CTA       |
| External badge        | None                           | JDS Badge (informational, secondary, subtle) |
| TRUE 5G label         | None                           | Top-right, flush to card           |
| External content      | None                           | Badge + TRUE 5G flush above card   |
| Vertical spacing      | Divider margin-based (16px)    | `var(--space-3)` (12px) flex gap   |
| Dividers              | 1 (between price & details)    | 1 (above CTA only)                |
| Grid columns (desktop)| 3 columns                      | 3 columns                          |

### Layout Rules

| Property              | Value                                          |
| --------------------- | ---------------------------------------------- |
| Background            | `var(--primary-20)`                            |
| Border                | `var(--border-width-thin) solid var(--grey-40)`|
| Border radius         | `calc(var(--radius) * 2)` → 16px               |
| Padding               | `var(--space-2) var(--space-4) var(--space-3) var(--space-4)` (8px 16px 12px 16px) |
| Vertical gap          | `var(--space-3)` (12px) — applied via `gap` on flex column |
| Grid columns (desktop)| 3 (in 12-column grid)                          |
| Display               | `flex flex-col`                                |

### External Badges

#### Badge-to-Card Spacing

```
Gap between badges and card container: 0px (flush, no margin-bottom)
Badges sit directly on top of the card border with no spacing.
```

#### Top-Left Informational Badge (JDS Badge Component)

```
Component:      Badge (from /src/app/components/ui/badge.tsx)
Category:       informational
Variant:        textInformational
Size:           l
Emphasis:       subtle
Color scheme:   secondary (bg: var(--secondary-20), text: var(--secondary-60))
Position:       flex row, left-aligned, outside card container
Text example:   "BEST SELLER", "POPULAR"
```

#### Top-Right "TRUE 5G" Label

```
Position:       flex row, right-aligned, outside card container
Background:     transparent
Padding:        none
Font size:      var(--text-body-xs) (14px)
Font weight:    var(--font-weight-bold) (700)
Color:          var(--primary-50)
Text:           "TRUE 5G"
Gap to card:    0px (no spacing between TRUE 5G and card)
```

### Chevron Button (Icon-Only, No Background)

```
Component:      Button (from /src/app/components/ui/button.tsx)
Variant:        tertiary
Size:           icon (size-10, 40px square)
Background:     transparent (no background)
Border:         none (no border)
Icon:           IcChevronRight (@jds/core-icons)
Icon size:      w-5 h-5 (20px)
Icon color:     var(--primary-60) (inherits from tertiary variant)
Position:       Right side of price row (flex justify-between)
```

**IMPORTANT:** Unlike the View Only variant (which uses a circular container with white bg and grey border), the Actionable Small variant uses the Button component with `variant="tertiary"` and `size="icon"` — resulting in a transparent, borderless icon button.

### Stacked Detail Rows

Each detail is a stacked header/value column with **no dividers** between columns:

```
┌──────────  ──────────  ─────┐
│ Bill cycle  Data        +5  │
│ 28 days     2 GB/day        │
└──────────  ──────────  ─────┘
 (11px)       (11px, bold)
```

| Element        | Font size                | Font weight                     | Color               |
| -------------- | ------------------------ | ------------------------------- | -------------------- |
| Header text    | `var(--text-footnote)` (11px) | `var(--font-weight-normal)` (400) | `var(--grey-80)` |
| Value text     | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700)   | `var(--foreground)` |
| More count     | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700)   | `var(--primary-50)` |

Gap between columns: `var(--space-4)` (16px)
Column sizing: `flex: 1` (equal width distribution)
No vertical dividers between columns.

### Primary CTA Button (Small Size)

```
Width:          100% (full-width)
Variant:        default (primary filled)
Size:           sm (40px height)
Border radius:  var(--radius-button) → 250px (pill shape)
Background:     var(--primary-50)
Color:          var(--primary-inverse)
Hover bg:       var(--primary-30)
Font size:      var(--text-button) (16px)
Font weight:    var(--font-weight-bold) (700)
Text example:   "Select Plan"
```

### Typography

| Element            | Font size             | Font weight              | Color                |
| ------------------ | --------------------- | ------------------------ | -------------------- |
| Price              | `var(--text-h3)` (32px) | `var(--font-weight-black)` (900) | `var(--foreground)` |
| Detail header      | `var(--text-footnote)` (11px) | `var(--font-weight-normal)` (400) | `var(--grey-80)` |
| Detail value       | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700) | `var(--foreground)` |
| More count         | `var(--text-footnote)` (11px) | `var(--font-weight-bold)` (700) | `var(--primary-50)` |
| CTA button         | `var(--text-button)` (16px) | `var(--font-weight-bold)` (700) | `var(--primary-inverse)` |

### Spacing

| Between                  | Token                           |
| ------------------------ | ------------------------------- |
| Card padding (T R B L)   | `var(--space-2) var(--space-4) var(--space-3) var(--space-4)` (8px 16px 12px 16px) |
| Vertical gap (all items) | `var(--space-3)` (12px) — via CSS `gap` on flex column |
| Badges → Card container  | `0px` (no gap, flush)           |
| Between detail columns   | `var(--space-4)` (16px)         |

### Data Structure

```ts
export interface PlanCardDataActionableSmall extends PlanCardData {
  ctaLabel: string;         // Small primary CTA button text
  promoBadge?: string;      // Optional badge text — uses JDS Badge (informational, secondary, subtle)
  showTrue5G?: boolean;     // Show/hide "TRUE 5G" label
  data: string;             // Data value (e.g. "2 GB/day")
  onCtaClick?: () => void;  // CTA button click handler
}
```

### Grid Layout

| Breakpoint   | Columns   | Gap                      |
| ------------ | --------- | ------------------------ |
| Mobile (<768px) | 1 column | `var(--space-6)` (24px) |
| md+ (≥768px) | 3 columns | `var(--space-6)` (24px) |

**Grid classes:** `grid grid-cols-1 md:grid-cols-3 gap-[var(--space-6)]`

**Column span (in 12-col grid):** Each card = `col-span-3` (3/12 = 25% width)

### Responsive Behavior

- **Mobile (<768px):** Single column, badges stack above card (flush), CTA button full-width
- **Desktop (≥768px):** 3-column grid, external badges positioned in flex row outside card bounds

---

## Plan Card — Actionable Default Large Variant

The **Actionable Default Large** variant features a borderless, larger layout with a `min-height` of `var(--card-plan-large-min-height)` (300px), support text subtitle, 4 bulleted feature points (with tick icons), and a **bottom-aligned** full-width primary CTA. Used for hero plan displays and detailed plan showcases.

### Visual Structure

```
┌─────────────────────────────────────────┐
│  bg: var(--primary-20)                  │
│  padding: var(--space-6) (24px)         │
│  min-height: var(--card-plan-large-min-height) │
│  NO BORDER                              │
│                                         │
│  ₹Price                                 │
│  (h3, Black 900)                        │
│                                         │
│  Support text / subtitle                │
│  (body-m, Medium 500, grey-80)          │
│                                         │
│  ✓ Feature point 1 (max 2 lines)       │
│  ✓ Feature point 2 (max 2 lines)       │
│  ✓ Feature point 3 (max 2 lines)       │
│  ✓ Feature point 4 (max 2 lines)       │
│  (base size, Normal 400, grey-80)      │
│  (tick icon: circle bg, primary color) │
│                                         │
│  ← flex spacer pushes CTA to bottom → │
│                                         │
│  [     Primary CTA Button (full-width) ]│
│  (default size, primary color)         │
│                                         │
└─────────────────────────────────────────┘
```

### Key Differences from Small Variant

| Property              | Actionable Default Small       | Actionable Default Large           |
| --------------------- | ------------------------------ | ---------------------------------- |
| Support text          | None                           | Yes (below price)                  |
| Middle section        | Stacked header/value details   | 4 bulleted feature points          |
| Bullets               | None                           | Tick icons with circle background  |
| Border                | `var(--border-width-thin) solid var(--grey-40)` | None (borderless) |
| Min height            | Auto                           | `var(--card-plan-large-min-height)` (300px) |
| CTA alignment         | Inline                         | Bottom-aligned (flex spacer)       |
| Grid columns (desktop)| 3 columns                      | 3 columns                          |
| External badges       | Yes (promo + TRUE 5G)          | None                               |
| Chevron button        | Yes (top-right)                | None                               |

### Layout Rules

| Property              | Value                                          |
| --------------------- | ---------------------------------------------- |
| Background            | `var(--primary-20)`                            |
| Border                | None (borderless)                              |
| Border radius         | `calc(var(--radius) * 2)` → 16px               |
| Padding               | `var(--space-6)` → 24px (all sides)            |
| Min height            | `var(--card-plan-large-min-height)` (300px)    |
| Grid columns (desktop)| 3 (in 12-column grid)                          |
| Display               | `flex flex-col`                                |
| CTA alignment         | Bottom-aligned via flex spacer (`flex: 1`)     |

### Typography

| Element            | Font size             | Font weight              | Color                |
| ------------------ | --------------------- | ------------------------ | -------------------- |
| Price              | `var(--text-h3)` (32px) | `var(--font-weight-black)` (900) | `var(--foreground)` |
| Support text       | `var(--text-body-m)` (18px) | `var(--font-weight-medium)` (500) | `var(--grey-80)` |
| Feature points     | `var(--text-base)` (16px) | `var(--font-weight-normal)` (400) | `var(--grey-80)` |
| CTA button         | `var(--text-button)` (16px) | `var(--font-weight-bold)` (700) | `var(--primary-inverse)` |

### Tick Icon with Background

```
Container size:     var(--space-5) (20px) width/height
Container shape:    circle
Container bg:       var(--primary-50)
Icon:               IcConfirm (@jds/core-icons)
Icon size:          12px
Icon color:         var(--global-white)
Alignment:          flex items-start (aligns to top of text for multi-line)
```

### Feature Point Layout

Each feature point is a flex row:

```
┌────┬──────────────────────────────────┐
│ ✓  │ Feature text wraps to max 2     │
│    │ lines with ellipsis overflow    │
└────┴──────────────────────────────────┘
    20px    gap: var(--space-3) (12px)
```

### Primary CTA Button (Bottom-Aligned)

```
Width:          100% (full-width)
Variant:        primary (filled)
Size:           default (48px height on desktop, 40px on mobile)
Border radius:  var(--radius-button) → 250px (pill shape)
Background:     var(--primary-50)
Color:          var(--primary-inverse)
Hover bg:       var(--primary-60)
Font size:      var(--text-button) (16px)
Font weight:    var(--font-weight-bold) (700)
Text example:   "Get Started"
Alignment:      Pushed to bottom of card via flex spacer (div with flex: 1)
```

### Spacing

| Between                  | Token                           |
| ------------------------ | ------------------------------- |
| Card padding (all sides) | `var(--space-6)` (24px)         |
| Price → Support text     | `var(--space-2)` (8px)          |
| Support text → Features  | `var(--space-4)` (16px)         |
| Between feature points   | `var(--space-3)` (12px)         |
| Features → CTA button    | `var(--space-6)` (24px) + flex spacer |
| Tick icon → Text         | `var(--space-3)` (12px)         |

### Data Structure

```ts
export interface PlanCardDataActionableLarge {
  id: number;
  price: string;              // e.g. "₹599" — includes rupee symbol
  supportText: string;        // e.g. "Best for home internet"
  features: string[];         // Array of 4 feature strings (max 2 lines each)
  ctaLabel: string;           // Primary CTA button text
  onCtaClick?: () => void;    // CTA button click handler
}
```

### Grid Layout

| Breakpoint   | Columns   | Gap                      |
| ------------ | --------- | ------------------------ |
| Mobile (<768px) | 1 column | `var(--space-6)` (24px) |
| md+ (≥768px) | 3 columns | `var(--space-6)` (24px) |

**Grid classes:** `grid grid-cols-1 md:grid-cols-3 gap-[var(--space-6)]`

**Column span (in 12-col grid):** Each card = `col-span-4` (4/12 = 33.33% width)

### Responsive Behavior

- **Mobile (<768px):** Single column, feature points stack vertically, CTA button full-width
- **Tablet (768px-1024px):** 2 columns, maintaining all spacing and typography
- **Desktop (≥1024px):** 3 columns, min-height ensures consistent card heights with bottom-aligned CTA

### Accessibility

- Tick icons have proper `aria-hidden="true"` attribute (decorative)
- Feature points maintain WCAG AA contrast
- CTA button is keyboard-focusable with visible focus ring

---

## Plan Card — Actionable Business Variant

The **Actionable Business** variant uses a **default background** (white/neutral) with a **subtle green information badge** as the first element, a **hug-content** primary CTA, grey tick icons (no background), feature text at 14px in `--grey-100`, **inset dividers** (not edge-to-edge), and a **center-aligned** tertiary button (no arrow icon) at the bottom. Displayed in a **4-column grid** (3 cols each in 12-col system).

### Visual Structure

```
┌─────────────────────────────────────────┐
│  bg: var(--global-white)                │
│  padding: var(--space-6) (24px)         │
│                                         │
│  [ Info Badge (subtle green) ]          │
│  (informational, positive, subtle)      │
│                                         │
│  ₹Price                                 │
│  (h3, Black 900)                        │
│                                         │
│  Support text / subtitle                │
│  (body-m, Medium 500, grey-80)          │
│                                         │
���  [ Primary CTA (hug content) ]          │
│  (NOT full-width, auto-width)          │
│                                         │
│  ─────────────────────────────────────  │
│  Inset Divider (respects padding)      │
│  ─────────────────────────────────────  │
│                                         │
│  ✓ Feature point 1 — grey tick, no bg  │
│  ✓ Feature point 2 — 14px, grey-100    │
│  ✓ Feature point 3 — 8px gap           │
│  ✓ Feature point 4                     │
│                                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━���━━━━━  │
│  Inset Divider (NOT edge-to-edge)      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                         │
│       [ View Details ]                  │
│       (tertiary, center, no icon)      │
│                                         │
└─────────────────────────────────────────┘
```

### Key Differences from Default Large

| Property              | Actionable Default Large       | Actionable Business               |
| --------------------- | ------------------------------ | --------------------------------- |
| Background            | `var(--primary-20)` (tinted)   | `var(--global-white)` (neutral)   |
| Information badge     | None                           | Yes (subtle green, first element) |
| CTA position          | Bottom (after features)        | Top (after support text)          |
| CTA width             | Full-width (`w-full`)          | Hug content (auto-width)          |
| Dividers              | None                           | 2 inset dividers (NOT edge-to-edge) |
| Tick icon style       | Circle bg + white icon         | No bg, grey icon `var(--grey-60)` |
| Feature text size     | `var(--text-base)` (16px)      | `var(--text-body-xs)` (14px)      |
| Feature text color    | `var(--grey-80)`               | `var(--grey-100)`                 |
| Feature gap           | `var(--space-3)` (12px)        | `var(--space-2)` (8px)            |
| Tertiary button       | None                           | Yes (center-aligned, no icon)     |
| Grid columns (desktop)| 3 columns                      | 4 columns (3-col span in 12-col) |

### Layout Rules

| Property              | Value                                          |
| --------------------- | ---------------------------------------------- |
| Background            | `var(--global-white)`                          |
| Border                | `var(--border-width-thin) solid var(--grey-40)`|
| Border radius         | `calc(var(--radius) * 2)` → 16px               |
| Padding               | `var(--space-6)` → 24px (all sides)            |
| Grid columns (desktop)| 4 columns (each card = 3 of 12)                |
| Display               | `flex flex-col`                                |

### Information Badge

```
Component:      Badge (from /src/app/components/ui/badge.tsx)
Category:       informational
Variant:        textInformational
Size:           l
Emphasis:       subtle
Color scheme:   positive (subtle green: bg var(--success-20), text var(--success-50))
Position:       First element in card, self-start (left-aligned)
Margin bottom:  var(--space-3) (12px)
Text examples:  "Recommended", "Most Popular", "Best Value", "New"
```

### Typography

| Element            | Font size             | Font weight              | Color                |
| ------------------ | --------------------- | ------------------------ | -------------------- |
| Price              | `var(--text-h3)` (32px) | `var(--font-weight-black)` (900) | `var(--foreground)` |
| Support text       | `var(--text-body-m)` (18px) | `var(--font-weight-medium)` (500) | `var(--grey-80)` |
| Feature points     | `var(--text-body-xs)` (14px) | `var(--font-weight-normal)` (400) | `var(--grey-100)` |
| CTA button         | `var(--text-button)` (16px) | `var(--font-weight-bold)` (700) | `var(--primary-inverse)` |
| Tertiary button    | `var(--text-label)` (14px)  | `var(--font-weight-bold)` (700) | `var(--primary-60)` |

### Tick Icon (Grey, No Background)

```
Icon:               IcConfirm (@jds/core-icons)
Icon size:          var(--space-5) (20px) width/height
Icon color:         var(--grey-60) (grey tick, no background circle)
Background:         None (no circle container)
Alignment:          flex items-start (aligns to top of text for multi-line)
```

### Feature Point Layout

Each feature point is a flex row with `var(--space-2)` (8px) gap between rows:

```
┌──────┬──────────────────────────────────┐
│  ✓   │ Feature text in grey-100, 14px  │
│(grey)│ wraps to max 2 lines            │
└──────┴──────────────────────────────────┘
 20px    gap: var(--space-3) (12px) horizontal
         gap: var(--space-2) (8px) vertical between rows
```

### Divider Styling — Both Dividers Inset (NOT Edge-to-Edge)

```
Height:         1px
Background:     var(--grey-40)
Margin X:       0 (respects card padding — NOT edge-to-edge)
Margin Y:       var(--space-4) (16px top/bottom)
Width:          100% (within padding bounds)
```

**IMPORTANT:** Dividers must NOT extend edge-to-edge. They stay within the card's padding.

### Primary CTA Button (Hug Content)

```
Width:          Auto (hug content — NOT full-width)
Variant:        primary (filled)
Size:           default (48px height)
Border radius:  var(--radius-button) → 250px (pill shape)
Background:     var(--primary-50)
Color:          var(--primary-inverse)
Hover bg:       var(--primary-60)
Font size:      var(--text-button) (16px)
Font weight:    var(--font-weight-bold) (700)
Text example:   "Contact Sales"
```

### Tertiary Button (Center-Aligned, No Icon)

```
Variant:        tertiary (text-link style)
Size:           small (40px height)
Background:     transparent
Border:         none
Color:          var(--primary-60)
Hover color:    var(--primary-50)
Font size:      var(--text-label) (14px)
Font weight:    var(--font-weight-bold) (700)
Icon:           None (no arrow/chevron icon)
Alignment:      Center-aligned (parent: flex justify-center)
Text example:   "View Details"
```

### Spacing

| Between                  | Token                           |
| ------------------------ | ------------------------------- |
| Card padding (all sides) | `var(--space-6)` (24px)         |
| Badge → Price            | `var(--space-3)` (12px)         |
| Price → Support text     | `var(--space-2)` (8px)          |
| Support text → CTA       | `var(--space-4)` (16px)         |
| CTA → Divider 1          | `var(--space-4)` (16px)         |
| Divider 1 → Features     | `var(--space-4)` (16px)         |
| Between feature points   | `var(--space-2)` (8px)          |
| Tick icon → Text         | `var(--space-3)` (12px)         |
| Features → Divider 2     | `var(--space-4)` (16px)         |
| Divider 2 → Tertiary CTA | `var(--space-4)` (16px)         |

### Data Structure

```ts
export interface PlanCardDataActionableBusiness {
  id: number;
  badgeText: string;            // e.g. "Recommended" — information badge text
  price: string;                // e.g. "₹2,999" — includes rupee symbol
  supportText: string;          // e.g. "Enterprise Fiber Solution"
  features: string[];           // Array of 4 feature strings (max 2 lines each)
  primaryCtaLabel: string;      // Primary CTA button text (hug content)
  tertiaryCtaLabel: string;     // Tertiary CTA button text (center-aligned, no icon)
  onPrimaryClick?: () => void;  // Primary CTA handler
  onTertiaryClick?: () => void; // Tertiary CTA handler
}
```

### Grid Layout

| Breakpoint     | Columns   | Gap                      |
| -------------- | --------- | ------------------------ |
| Mobile (<768px)   | 1 column | `var(--space-6)` (24px) |
| md (768-1023px)   | 2 columns| `var(--space-6)` (24px) |
| lg+ (≥1024px)     | 4 columns| `var(--space-6)` (24px) |

**Grid classes:** `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-[var(--space-6)]`

**Column span (in 12-col grid):** Each card = `col-span-3` (3/12 = 25% width) → 4 cards visible

### Responsive Behavior

- **Mobile (<768px):** Single column, all buttons auto-width, dividers remain inset
- **Tablet (768px-1023px):** 2 columns, maintaining all spacing and typography
- **Desktop (≥1024px):** 4-column grid with all 4 cards visible side-by-side

### Accessibility

- All buttons are keyboard-focusable with visible focus rings
- Dividers do not interfere with tab order
- Color contrast meets WCAG AA standards
- Tertiary button maintains sufficient clickable area (min 44x44px touch target)
- Information badge uses semantic green color scheme for positive/recommended status

---

## Plan Card — Variant Comparison Summary

| Feature               | View Only | Actionable Small | Actionable Large | Actionable Business |
| --------------------- | --------- | ---------------- | ---------------- | ------------------- |
| **Background**        | Primary-20 | Primary-20       | Primary-20       | White               |
| **Border**            | Yes       | Yes              | No (borderless)  | Yes                 |
| **Padding**           | 8 16 12 16 | 8 16 12 16      | 24px all         | 24px all            |
| **Vertical gap**      | Divider margin (16px) | 12px       | Margin-based     | Margin-based        |
| **Grid columns (12-col)** | 3     | 3                | 3                | 4                   |
| **Min height**        | Auto      | Auto             | 300px token      | Auto                |
| **Info badge**        | No        | No               | No               | Yes (subtle green)  |
| **Chevron button**    | Icon-only | Icon-only        | No               | No                  |
| **Support text**      | No        | No               | Yes              | Yes                 |
| **Middle content**    | Stacked header/value (11px) | Stacked header/value (11px) | 4 bullets | 4 bullets (14px, grey-100) |
| **Detail col spacing**| Equal (flex:1) | Equal (flex:1) | N/A              | N/A                 |
| **Primary CTA**       | No        | Small, full-width | Bottom-aligned   | Top (hug content)   |
| **Tertiary CTA**      | No        | No               | No               | Center, no icon     |
| **External badges**   | No        | Badge (secondary subtle) | No          | No                  |
| **Dividers**          | 1 (between price & details) | 1 (above CTA) | 0          | 2 (inset)           |
| **Tick icons**        | No        | No               | Primary circle   | Grey, no bg         |
| **Detail font**       | 14px      | 11px footnote    | 16px base        | 14px body-xs        |
| **Use case**          | Comparison | Selection       | Hero showcase    | Enterprise B2B      |

---

## Plan Card — When to Use Each Variant

### View Only

- Use for **plan comparison grids** where users need to review multiple options side-by-side
- Use on **informational pages** where plan details are displayed but no immediate action is required
- Ideal for **mobile app onboarding** screens showing available plans
- **Do not** use when conversion is the primary goal — use an actionable variant instead

### Actionable Default Small

- Use for **primary plan selection flows** where users need to choose and activate a plan
- Uses **JDS Badge component** (informational, secondary, subtle) for promotional badges flush to card
- Ideal for **recharge/renewal pages** where "TRUE 5G" label adds marketing value
- Uses **stacked header/value detail rows** at 11px (`--text-footnote`) with bold values and **no dividers between columns**
- Compact padding (`8px 16px 12px 16px`) with `12px` vertical gap for a tight, efficient layout
- Uses **small primary CTA** button for clear conversion action
- Use in **3-column grids** where space efficiency is important
- **Do not** use for enterprise/business plans — use Actionable Business variant

### Actionable Default Large

- Use for **hero plan showcases** where one or two premium plans are highlighted
- Use on **product detail pages** where plan features need detailed explanation
- **Borderless** card with `min-height: var(--card-plan-large-min-height)` (300px) for consistent heights
- **Bottom-aligned CTA** via flex spacer ensures button stays at card bottom regardless of content length
- Ideal for **long-form landing pages** with generous whitespace and larger cards
- Use in **3-column grids** where more space is available
- **Do not** use for dense comparison grids — use Small variant for compactness

### Actionable Business

- Use for **B2B/enterprise plan pages** targeting business customers
- Features a **subtle green information badge** as the first card element for plan categorization
- **Hug-content CTA** (not full-width) creates a professional, less aggressive feel
- **Grey tick icons** (no background circle) for a clean, enterprise aesthetic
- Feature text at **14px** (`--text-body-xs`) in **grey-100** with **8px gap** between points
- **Inset dividers** (not edge-to-edge) maintain clean internal spacing
- **Center-aligned tertiary button** with no arrow icon for "View Details"
- Displayed in a **4-column grid** (3 cols each in 12-col system) for side-by-side comparison
- **Do not** use for consumer plans — the white background and formal layout is less engaging

---

## Plan Card — Responsive Design Guidelines

### Breakpoint Strategy

All plan card variants follow this responsive pattern:

| Breakpoint   | Layout behavior                                      |
| ------------ | ---------------------------------------------------- |
| Mobile (<768px) | Single column, full-width cards, stacked vertically |
| Tablet (768px-1024px) | 2 columns (except View Only = 3 columns)   |
| Desktop (≥1024px) | 3 or 4 columns based on variant specification      |

### Typography Scaling

| Element               | Mobile (<768px)       | Desktop (≥768px)      |
| --------------------- | --------------------- | --------------------- |
| Price (h3)            | `var(--text-h4)` (24px) | `var(--text-h3)` (32px) |
| Support text          | `var(--text-base)` (16px) | `var(--text-body-m)` (18px) |
| Feature points        | `var(--text-label)` (14px) | `var(--text-base)` (16px) |
| Labels (bill cycle)   | `var(--text-label)` (14px) | `var(--text-label)` (14px) |

Use responsive font-size rules:

```css
font-size: clamp(var(--text-h4), 3vw, var(--text-h3));
```

### Button Sizing

| Button type           | Mobile (<768px)       | Desktop (≥768px)      |
| --------------------- | --------------------- | --------------------- |
| Primary CTA           | 40px height           | 48px height           |
| Tertiary CTA          | 32px height           | 32px height           |
| Chevron button        | 40px (square)         | 40px (square)         |

### Spacing Adjustments

| Area                  | Mobile (<768px)       | Desktop (≥768px)      |
| --------------------- | --------------------- | --------------------- |
| Card padding          | `var(--space-5)` (20px) | `var(--space-6)` (24px) |
| Price → Support text  | `var(--space-2)` (8px)  | `var(--space-2)` (8px)  |
| Features gap          | `var(--space-2)` (8px)  | `var(--space-3)` (12px) |

### External Badge Behavior (Actionable Small)

- **Mobile:** Badges render **above the card** in a flex row (left badge, spacer, right badge)
- **Desktop:** Badges render **absolutely positioned** outside the card container

---

## Plan Card — Implementation Notes

### CSS-First Approach

All plan card variants must be implemented using:

1. **Inline style objects** with JDS token references: `style={{ padding: 'var(--space-6)' }}`
2. **NO Tailwind arbitrary values** — only design system tokens
3. **Responsive utilities** via Tailwind breakpoint prefixes: `md:grid-cols-3`
4. **CSS custom properties** for all colors, spacing, typography, and borders

### Component File Structure

```
/src/app/components/
  ├── JioHomePlanCard.tsx           # View Only variant (current)
  ├── JioHomePlanCardActionable.tsx # Small + Large + Business variants
  └── PlanCardTypes.ts              # Shared TypeScript interfaces
```

### Shared JDS Tokens

All plan cards use these foundational tokens:

**Spacing:**
- `--space-2` (8px), `--space-3` (12px), `--space-4` (16px), `--space-5` (20px), `--space-6` (24px)

**Colors:**
- `--primary-20`, `--primary-50`, `--primary-60`, `--primary-inverse`
- `--grey-40`, `--grey-80`, `--foreground`, `--global-white`

**Typography:**
- `--font-family-jiotype`, `--text-h3`, `--text-h4`, `--text-base`, `--text-label`
- `--font-weight-normal` (400), `--font-weight-medium` (500), `--font-weight-bold` (700), `--font-weight-black` (900)

**Borders & Radius:**
- `--border-width-thin`, `--radius`, `--radius-button`, `--radius-circle`

### Icon Usage

- **Chevron:** `lucide-react` → `ChevronRight` (20px)
- **Tick/Check:** `lucide-react` → `Check` (12px inside 20px circle)
- All icons use `fill="currentColor"` for color inheritance

### Accessibility Checklist

- [ ] All interactive elements (buttons, cards) are keyboard-focusable
- [ ] Focus rings are visible and meet WCAG 2.4.7 guidelines
- [ ] Color contrast ratios meet WCAG AA (4.5:1 for text, 3:1 for UI components)
- [ ] Decorative icons have `aria-hidden="true"`
- [ ] CTA buttons have descriptive labels (avoid generic "Click here")
- [ ] Card hover states provide clear visual feedback
- [ ] External badges do not obscure card content on mobile

---

## Plan Card — Usage Examples

### View Only Variant

```tsx
import { JioHomePlanCard, PlanCardData } from './JioHomePlanCard';

const plans: PlanCardData[] = [
  {
    id: 1,
    price: '₹199',
    billCycle: 'Bill cycle:',
    validity: '28 Days',
    speed: 'Upto:',
    benefits: '30 Mbps',
    avatarColors: ['#FF6B6B', '#4ECDC4', '#45B7D1'],
    moreCount: '+10 more',
  },
];

<div className="grid grid-cols-1 md:grid-cols-3" style={{ gap: 'var(--space-6)' }}>
  {plans.map((plan) => (
    <JioHomePlanCard key={plan.id} plan={plan} />
  ))}
</div>
```

### Actionable Default Small Variant

```tsx
import { PlanCardActionableSmall } from './JioHomePlanCardActionable';

const plan = {
  id: 1,
  price: '₹399',
  validity: '56 Days',
  data: '2 GB/day',
  moreCount: '+15',
  ctaLabel: 'Select Plan',
  promoBadge: 'BEST SELLER',
  showTrue5G: true,
  onCtaClick: () => console.log('Plan selected'),
};

// Badge: JDS Badge (informational, secondary, subtle) — flush to card
// Padding: 8px 16px 12px 16px, vertical gap: 12px
// Stacked detail rows (11px) — no dividers between columns
// CTA: small primary button
<div className="grid grid-cols-1 md:grid-cols-3" style={{ gap: 'var(--space-6)' }}>
  <PlanCardActionableSmall plan={plan} />
</div>
```

### Actionable Default Large Variant

```tsx
import { PlanCardActionableLarge } from './JioHomePlanCardActionable';

const plan = {
  id: 1,
  price: '₹599',
  supportText: 'Best for home internet',
  features: [
    'Unlimited data with no FUP limits',
    'Free router and installation',
    '200+ live TV channels and OTT apps',
    '24/7 customer support',
  ],
  ctaLabel: 'Get Started',
  onCtaClick: () => console.log('Large plan CTA clicked'),
};

// No border, min-height: var(--card-plan-large-min-height) (300px)
// CTA bottom-aligned via flex spacer
<div className="grid grid-cols-1 md:grid-cols-3" style={{ gap: 'var(--space-6)' }}>
  <PlanCardActionableLarge plan={plan} />
</div>
```

### Actionable Business Variant

```tsx
import { PlanCardActionableBusiness } from './JioHomePlanCardActionable';
import { Badge } from './components/ui/badge';

const plan = {
  id: 1,
  badgeText: 'Recommended',
  price: '₹2,999',
  supportText: 'Enterprise Fiber Solution',
  features: [
    'Dedicated 1 Gbps symmetric bandwidth',
    'Static IP and DNS management',
    '99.9% uptime SLA guarantee',
    'Priority technical support',
  ],
  primaryCtaLabel: 'Contact Sales',
  tertiaryCtaLabel: 'View Details',
  onPrimaryClick: () => console.log('Contact sales clicked'),
  onTertiaryClick: () => console.log('View details clicked'),
};

// Info badge (subtle green) as first element
// Hug-content primary CTA (not full-width)
// Grey tick icons (no bg), 14px text in grey-100, 8px gap
// Inset dividers (not edge-to-edge)
// Center-aligned tertiary button, no icon
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4" style={{ gap: 'var(--space-6)' }}>
  <PlanCardActionableBusiness plan={plan} />
</div>
```

---

## Plan Card — Design Tokens Reference

### Required CSS Variables

Ensure these tokens are defined in `/src/styles/theme.css`:

```css
:root {
  /* Spacing */
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;

  /* Colors — Primary */
  --primary-20: #e6f0ff;
  --primary-50: #0066ff;
  --primary-60: #0052cc;
  --primary-inverse: #ffffff;

  /* Colors — Neutrals */
  --grey-40: #d9d9d9;
  --grey-60: #999999;
  --grey-80: #666666;
  --foreground: #1a1a1a;
  --global-white: #ffffff;
  --global-black: #000000;

  /* Colors — Secondary (for badges) */
  --secondary-20: #fff4e6;

  /* Typography */
  --font-family-jiotype: 'JioType', system-ui, -apple-system, sans-serif;
  --text-h3: 32px;
  --text-h4: 24px;
  --text-body-m: 18px;
  --text-base: 16px;
  --text-button: 16px;
  --text-label: 14px;
  --text-xs: 12px;

  /* Font Weights */
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --font-weight-black: 900;

  /* Borders & Radius */
  --border-width-thin: 1px;
  --radius: 8px;
  --radius-button: 250px;
  --radius-circle: 50%;
}
```

### Responsive Typography Helper

Use this CSS pattern for responsive font sizing:

```css
.plan-card-price {
  font-size: clamp(var(--text-h4), 3vw, var(--text-h3));
}

.plan-card-support {
  font-size: clamp(var(--text-base), 2vw, var(--text-body-m));
}
```

---

**End of Plan Card Variant Documentation**