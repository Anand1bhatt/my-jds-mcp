# HeroCarousel — JDS Component Style Guide

## Overview

The HeroCarousel is a center-focused carousel with "peek" slides visible on both sides. It is built on top of **Embla Carousel** and adheres strictly to the **JDS (Jio Design System)** design tokens defined in `/src/styles/theme.css`.

**Shared component** — `HeroCarousel` is used on **all pages** (Desktop `/`, Mobile `/mobile`, etc.). There is no separate mobile carousel; the same component adapts responsively via `clamp()` sizing and responsive padding classes. Each page passes its own `slides` array via the optional `slides` prop; when omitted, the desktop default slides are used.

---

## Component API

```tsx
interface HeroCarouselProps {
  slides?: SlideData[];  // Optional — defaults to desktop slides when omitted
}

// Usage:
<HeroCarousel />                      // Desktop — uses default slides
<HeroCarousel slides={mobileSlides} /> // Mobile — custom slide content
```

The `SlideData` type is exported from `HeroCarousel.tsx` for use by consuming pages:

```tsx
import { HeroCarousel } from '../components/HeroCarousel';
import type { SlideData } from '../components/HeroCarousel';
```

---

## Typography Rules (MANDATORY)

> **ALL text in the HeroCarousel — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- This resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif) anywhere.
- Every text element — headings, descriptions, buttons, counters — must inherit or explicitly set `font-family: var(--font-family-jiotype)`.

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.
- The team must provide the JioType `.woff2` file at `/public/fonts/JioType-Variable.woff2`.

### Permitted Weights

Only these four JDS weight tokens are allowed:

| Token                       | Value | Usage                              |
| --------------------------- | ----- | ---------------------------------- |
| `--font-weight-normal`      | 400   | Body text, descriptions            |
| `--font-weight-medium`      | 500   | Slide descriptions                 |
| `--font-weight-bold`        | 700   | CTA buttons, pagination counter    |
| `--font-weight-black`       | 900   | Slide titles, section headings     |

- **Never** use arbitrary `font-weight` numbers (e.g. `600`, `800`).
- **Never** use Tailwind font-weight utilities (e.g. `font-semibold`).

### Permitted Sizes

| Token                | Value | Usage                          |
| -------------------- | ----- | ------------------------------ |
| `--text-h1`          | 88px  | Hero display                   |
| `--text-h2`          | 64px  | Page-level section headings    |
| `--text-h3`          | 32px  | Slide title max (clamp)        |
| `--text-h4`          | 24px  | Slide title min (clamp)        |
| `--text-body-large`  | 24px  | Large body text                |
| `--text-button-large`| 18px  | Large button text              |
| `--text-base`        | 16px  | Body text                      |
| `--text-button`      | 16px  | CTA button text                |
| `--text-label`       | 14px  | Description, pagination        |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`).
- Use `clamp()` with JDS tokens for responsive sizing.

---

## Layout Structure

```
┌──────────────────────────────────────────────────────────────────┐
│  [prev peek]  │         ACTIVE SLIDE (80% width)        │ [next]│
│   opacity:0.65│  ┌──────────────────────────────────────┐│ peek  │
│               │  │  Background Image                    ││       │
│               │  │  ├─ Gradient Overlay (L→R)           ││       │
│               │  │  ├─ Title (h3, JioType Black)        ││       │
│               │  │  ├─ Description (p, JioType Med)     ││       │
│               │  │  └─ CTA Button (pill, JDS token)     ││       │
│               │  └──────────────────────────────────────┘│       │
│               │                                          │       │
│               │          ┌──────────────────┐            │       │
│               │          │ [←]  1/3  [→]    │  ← fixed   │       │
│               │          │ pill container    │  overlay   │       │
│               │          └──────────────────┘            │       │
└──────────────────────────────────────────────────────────────────┘
```

### Key Layout Rules

- **Slide width**: `flex: 0 0 80%` — each slide takes 80% of the viewport width
- **Gap**: `16px` between slides — applied via `paddingLeft` and `paddingRight` of `calc(var(--space-4) / 2)` on each slide (not CSS `gap`) for reliable loop spacing
- **Alignment**: `align: 'center'` — active slide is always centered
- **Loop**: `loop: true` — infinite scrolling
- **Inactive opacity**: `0.65` — non-active slides are dimmed
- **Border radius**: `var(--radius-lg)` (24px) on each slide container
- **Height**: `clamp(280px, 40vw, 500px)` — responsive height
- **Controls wrapper**: A `relative` div wraps both the embla viewport and the controls overlay

---

## Design Tokens Used

### Colors

| Token                        | Usage                                    |
| ---------------------------- | ---------------------------------------- |
| `--global-white`             | Slide text color                         |
| `--global-black`             | Dark CTA button bg                       |
| `--grey-100`                 | Controls counter text color, dark CTA hover |
| `--primary-background`       | Controls container background (#FFFFFF)  |
| `--primary-50`               | Primary CTA button bg                    |
| `--primary-60`               | Controls arrow button icon color, primary CTA hover |
| `--primary-inverse`          | Primary CTA text color                   |
| `--secondary-50`             | Secondary CTA button bg                  |
| `--secondary-60`             | Secondary CTA hover                      |
| `--secondary-inverse`        | Secondary CTA text color                 |
| `--background`               | Section background                       |

### Typography

| Token                        | Usage                                    |
| ---------------------------- | ---------------------------------------- |
| `--font-family-jiotype`      | All text elements                        |
| `--font-weight-black` (900)  | Slide title                              |
| `--font-weight-bold` (700)   | CTA buttons, pagination counter          |
| `--font-weight-medium` (500) | Slide description                        |
| `--text-h3` (32px)           | Title max font size                      |
| `--text-h4` (24px)           | Title min font size (clamp)              |
| `--text-label` (14px)        | Description, pagination counter          |
| `--text-button` (16px)       | CTA button text                          |

### Radius

| Token                        | Usage                                    |
| ---------------------------- | ---------------------------------------- |
| `--radius-lg` (24px)         | Slide container border radius            |
| `--radius-button` (250px)    | CTA button pill shape, nav buttons       |

---

## CTA Button Variants

All slide CTA buttons use the **primary** variant (`--primary-50`) by default:

### `primary` (default for all slides)
```css
background: var(--primary-50);
color: var(--primary-inverse);
hover: var(--primary-60);
```

All buttons use:
- `border-radius: var(--radius-button)` (250px pill)
- `font-family: var(--font-family-jiotype)`
- `font-size: var(--text-button)`
- `font-weight: var(--font-weight-bold)`
- Padding: `px-6 py-2.5`

---

## Pagination Indicator

The carousel controls are positioned as a **fixed overlay** at the bottom-right of the carousel area. They do **NOT** live inside each slide — they are a sibling of the Embla viewport, absolutely positioned within a relative wrapper. This means the controls **stay in place** while slides scroll underneath.

### Position (MANDATORY)

```
Position:    absolute (within the relative carousel wrapper)
Bottom:      var(--space-6) (24px)
Right:       calc(10% + calc(var(--space-4) / 2) + var(--space-6))
             → 10% viewport gap + 8px slide padding + 24px inset
z-index:     10
```

> **MANDATORY:** The controls must NEVER be placed inside the per-slide `map()` loop. They must be a sibling of the `emblaRef` viewport div, positioned absolutely within a shared `relative` parent wrapper.

### Container (Pill Shape)

```
background:     var(--primary-background)    → #FFFFFF
border-radius:  var(--radius-button)         → 250px (pill)
padding:        var(--space-1)               → 4px
gap:            var(--space-1)               → 4px
display:        flex items-center
```

### Arrow Buttons (Tertiary Style)

The left/right arrow buttons use a **tertiary** style — no background, no border, icon-only with `var(--primary-60)` color:

```
width:          36px
height:         36px
border-radius:  var(--radius-button)         → 250px
background:     transparent
border:         none
color:          var(--primary-60)            → #000093
cursor:         pointer
transition:     transition-colors
```

Icons: `ArrowLeft` / `ArrowRight` from lucide-react, `w-4 h-4`, `fill="currentColor"`

### Counter Text

```
font-family:    var(--font-family-jiotype)
font-size:      var(--text-label)            → 14px
font-weight:    var(--font-weight-bold)      → 700
color:          var(--grey-100)              → #141414
padding:        0 var(--space-1)             → 0 4px
user-select:    none
```

Format: `{selectedIndex + 1}/{scrollSnaps.length}` (e.g., "1/3", "2/3")

### Visual

```
┌──────────────────────────┐
│  [←]    1/3    [→]       │  ← pill container
│                          │     bg: --primary-background
│  arrows: --primary-60    │     border-radius: --radius-button
│  text:   --grey-100      │     padding: --space-1
└──────────────────────────┘
```

---

## Gradient Overlay

Each slide uses a left-to-right gradient to ensure text readability:

```css
background: linear-gradient(
  to right,
  rgba(0, 0, 0, 0.65) 0%,
  rgba(0, 0, 0, 0.35) 50%,
  rgba(0, 0, 0, 0.05) 100%
);
```

---

## Text Content Area

- Positioned absolutely within the slide: `inset-0`, left-aligned
- Max width: `60%` of slide to avoid overlapping the image focal point
- Padding: `px-8` (mobile), `px-12` (tablet), `px-16` (desktop)
- Title uses `whitespace-pre-line` for multi-line display via `\n` in data

---

## Autoplay Behavior

- **Delay**: 5000ms between auto-advances
- **Stop on interaction**: Pauses when user clicks navigation
- **Mouse enter**: Pauses autoplay
- **Mouse leave**: Resumes autoplay

---

## Embla Carousel Options

```ts
{
  align: 'center',
  loop: true,
  skipSnaps: false,
  containScroll: false,
}
```

---

## Responsive Behavior

| Breakpoint | Title Size       | Slide Height        | Content Padding |
| ---------- | ---------------- | ------------------- | --------------- |
| Mobile     | `var(--text-h4)` | `280px`             | `px-8`          |
| Tablet     | ~3vw fluid       | ~40vw fluid         | `px-12`         |
| Desktop    | `var(--text-h3)` | `500px`             | `px-16`         |

---

## Slide Data Structure

```ts
interface SlideData {
  id: number;
  image: string;          // Unsplash or figma:asset URL
  alt: string;            // Accessibility alt text
  productLogo?: string;   // Optional product name rendered as text label above title
  title: string;          // Supports \n for line breaks
  description?: string;   // Optional subtitle text
  cta: string;            // Button label
  ctaVariant: 'dark' | 'primary' | 'secondary';
}
```

### Product Logo

When a slide has a `productLogo`, it renders as a **text label** above the heading (not an image):

```
font-family:    var(--font-family-jiotype)
font-size:      var(--text-body-m)           → 18px
font-weight:    var(--font-weight-bold)      → 700
color:          var(--global-white)
line-height:    1.4
letter-spacing: 0.02em
margin-bottom:  var(--space-2)               → 8px (below logo, above title)
```

---

## File Dependencies

- `embla-carousel-react` — Core carousel engine
- `embla-carousel-autoplay` — Autoplay plugin
- `lucide-react` — ArrowLeft, ArrowRight icons
- `./figma/ImageWithFallback` — Image component with fallback
- `./ui/button` — (available but pagination uses custom buttons for tighter control)
- `/src/styles/theme.css` — All JDS design tokens

---

## Carousel Navigation Controls

### Hero Banner Carousel (Inside Banner)

For hero banner carousels (HeroCarousel, ILLHeroCarousel, JioHomeHeroCarousel, JioGlassHero), navigation controls are positioned **inside the banner** at bottom-right using **inline button elements** (not the JDS Button component).

**Position:**
```
Position:    absolute (within the slide container)
Bottom:      var(--space-6) (24px)
Right:       var(--space-6) (24px)
z-index:     10
```

**Container (Pill Shape):**
```
background:     var(--primary-background)    → #FFFFFF
border-radius:  var(--radius-button)         → 250px (pill)
padding:        var(--space-1)               → 4px
gap:            var(--space-1)               → 4px
display:        flex items-center
```

**Arrow Buttons (Inline Tertiary Style):**

Hero banner carousels use **inline `<button>` elements** with tertiary styling (transparent background, no border):

```tsx
<button
  onClick={scrollPrev}
  className="flex items-center justify-center transition-colors cursor-pointer"
  style={{
    width: '36px',
    height: '36px',
    borderRadius: 'var(--radius-button)',
    border: 'none',
    backgroundColor: 'transparent',
    color: 'var(--primary-60)',
  }}
  aria-label="Previous slide"
>
  <IcArrowBack className="w-4 h-4" fill="currentColor" />
</button>
```

Button styling:
- Size: `36px × 36px` (inline width/height)
- Background: `transparent`
- Color: `var(--primary-60)` → #000093
- Border: `none`
- Border radius: `var(--radius-button)` → 250px
- Icons: `IcArrowBack`, `IcArrowNext` from `@jds/core-icons`
- Icon size: `w-4 h-4` (16px)
- No disabled state (hero banners loop infinitely)

### Section Carousel Navigation (Below Carousel)

For section carousels (FeatureCardsSection, BusinessServices, MobileIconCards, etc.), navigation controls are positioned **below the carousel** at bottom-right of the section container using **JDS Button component**.

**Position:**
```
Position:    static (inside container)
Margin top:  var(--space-8) (32px)
Alignment:   right (justify-end)
Gap:         var(--space-3) (12px)
```

**Arrow Buttons (Secondary Button Component):**

Use the JDS Button component with `variant="secondary"` and `size="icon"`:

```tsx
<Button
  onClick={scrollPrev}
  disabled={!canScrollPrev}
  variant="secondary"
  size="icon"
  aria-label="Previous cards"
>
  <IcArrowBack className="w-5 h-5" fill="currentColor" />
</Button>
```

Button styling (from button.md):
- Size: `40px × 40px` (size="icon")
- Background: `transparent`
- Color: `var(--primary-60)` → #000093
- Border: `1px solid var(--grey-60)` → #B5B5B5
- Border radius: `var(--radius-button)` → 250px
- Icons: `IcArrowBack`, `IcArrowNext` from `@jds/core-icons`
- Icon size: `w-5 h-5` (20px)
- Hover: background `var(--primary-20)`, maintains border and text color
- Disabled: opacity `0.3` (30%) on entire button

### Counter Text

```
font-family:    var(--font-family-jiotype)
font-size:      var(--text-label)            → 14px
font-weight:    var(--font-weight-bold)      → 700
color:          var(--grey-100)              → #141414
padding:        0 var(--space-1)             → 0 4px
user-select:    none
```

Format: `{selectedIndex + 1}/{scrollSnaps.length}` (e.g., "1/3", "2/3")

### Visual

```
┌──────────────────────────┐
│  [←]    1/3    [→]       │  ← pill container
│                          │     bg: --primary-background
│  arrows: --primary-60    │     border-radius: --radius-button
│  text:   --grey-100      │     padding: --space-1
└──────────────────────────┘
```