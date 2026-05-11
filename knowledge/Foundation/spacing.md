# Spacing

Spacing methods are a set of rules around how to place elements within layouts and components. Our tried and tested methods are more granular than the responsive layout grid. This level of detail allows us to create highly accurate, optimised designs with no awkward spacing issues in sight.

This document is the **single source of truth** for spacing in the Jio Design System.

---

## Spacing Methods

Spacing methods include padding, margins, gutters, alignment and microspacing, all of which can be used to adjust canvas containers and touch target areas to meet your requirements.

### Key Methods

- **Padding** – Internal spacing within elements and containers
- **Margins** – External spacing between elements
- **Gutters** – Spacing between columns in grid systems
- **Alignment** – Placement of content within layouts
- **Microspacing** – Fine-tuned spacing for precision

---

## Spacing Scale

All spacing must use the JDS spacing tokens defined in `theme.css`. The scale uses a **4px base unit**.

### Token Reference

Our spacing tokens and units are set at increments of 4px. This gives you the freedom to manipulate the spacing to meet your user requirements. We also use tokens (XXS-Massive) to clearly label the sizing for things like margins and gutters.

| Descriptive Token | Value | CSS Variable | Tailwind Utility | Common Use |
|-------------------|-------|--------------|------------------|------------|
| XXS | 4px | `--space-1` | `p-1`, `gap-1` | Tight inner padding (toggle track) |
| XS | 8px | `--space-2` | `p-2`, `gap-2` | Icon gaps, small padding |
| S | 12px | `--space-3` | `p-3`, `gap-3` | CTA button gaps, badge padding |
| Base | 16px | `--space-4` | `p-4`, `gap-4` | Card inner padding, carousel gap |
| M | 24px | `--space-6` | `p-6`, `gap-6` | Section inner padding (mobile), nav gap |
| L | 32px | `--space-8` | `p-8`, `gap-8` | Section inner padding (desktop) |
| XL | 40px | `--space-10` | `p-10` | Large inner padding |
| XXL | 48px | `--space-12` | `py-12` | Section vertical padding |
| Huge | 64px | `--space-16` | `py-16` | Section vertical padding (large) |
| Massive | 80px | `--space-20` | `py-20` | Extra large section padding |

**Additional tokens:**

| CSS Variable | Value | Tailwind Utility | Common Use |
|--------------|-------|------------------|------------|
| `--space-0` | 0px | `p-0`, `m-0` | Reset / none |
| `--space-5` | 20px | `p-5`, `gap-5` | Grid card gap, content spacing |

Our spacing tokens and units use 4px increments, giving you the flexibility to adjust spacing to suit user needs.

---

## Padding

Padding is a compositional property used for elements and containers to add space and frame any nested content. When used correctly, padding brings visual clarity and balance to a layout. Padding can be measured both horizontally and vertically and should meet our rule of 4px increments.

Apply 4px increments for padding across all elements and containers to maintain consistent and balanced spacing.

### Padding Examples

- Always provide 4px padding between a button's elements
- Use consistent padding dimensions across each element
- Always precisely align elements within components to the grid

---

## Margins

Margins are a compositional attribute used for external spacing between elements. They can either have a fixed width or adapt to different breakpoints. Margins are responsive and relative to device width in order to ensure there is sufficient distance between the content container and edge of the screen. As a general rule, we use increments of 4px for margins to increase consistency.

Use increments of 4px for margins to increase consistency across breakpoints, ensuring balanced layout spacing.

---

## Gutters

Gutters are the spacing units between each of the columns within a responsive grid system, and should always be consistent in width. Both gutters and margins can scale relative to the breakpoint.

Gutters should remain consistent between columns, adapting to responsive breakpoints for optimal spacing.

---

## Containers

Containers are the unseen ghost-like shapes that surround UI elements such as images or icons. They can be used to limit the size of an element or as a cropping tool for images and elements. Containers can also be fluid and can scale relative to the inner element. The blue outlines are containers, and only appear once the element is hovered over or clicked by the designer.

Invisible containers set boundaries around UI elements, ensuring proper scaling and visual organization.

---

## Touch Targets

Touch targets are components that respond to user input, for example a button. They must have a large enough target area for a user to interact with one finger. Because their container extends beyond the outer visual element, the padding around the component needs to extend to the minimum touch target. Aim for at least 8px padding between each touch target to create good visual balance and aid the user experience.

### Touch Target Requirements

- **Minimum touch target size:** 48x48px
- **Minimum spacing between targets:** 8px (XXS / `--space-2`)
- **Example:** An icon that is 24x24px in size should have a touch target of 48x48px to meet minimum requirements

In this example, the icon is 24x24 px, but its touch target expands to 48x48 px, meeting the minimum size for optimal usability.

---

## The Box Model

The Box Model is a way to describe an object's dimensions and spacing. The CSS box model logic proposes every element on a page is a rectangular invisible box. This is the way all Jio Components have been built in design and code.

Each box is composed of four areas:

1. **Content:** From text and images to a component
2. **Padding:** Creates a gap between the content of a box and its border
3. **Border:** The thickness of the stroke around the edges of an element
4. **Margin:** A buffer area that separates the element itself from other elements on a page

### Box Model Calculation

The element **total width** and **total height** will be the result of:

```
Total Width/Height = Content + Padding + Border
```

**Note:** Margin is reserved for the spacing between elements and is not included in the element's total size.

### The Box Model and Text

By placing all text within a content box, we can easily control the spacing from the box rather than the baseline, therefore improving spacing accuracy. This approach ensures:

- Consistent vertical rhythm
- Predictable spacing behavior
- Easier alignment to the grid

---

## Alignment

Alignment is the placement of content, both horizontally and vertically within a grid layout. We offer our creators 3 different types of alignment depending on their needs:

- **Centered** – Content aligned to the center
- **Right-aligned** – Content aligned to the right edge
- **Left-aligned** – Content aligned to the left edge

### Section Title Alignment (MANDATORY)

All section-level headings (`<h2>`, `<h3>` used as section titles) and their subtitles (`<p>`) must be **center-aligned**:

- `text-align: center` on the text element
- The heading/subtitle must sit inside a horizontally centered container (e.g. `container mx-auto`)
- This applies to every content section on the page — no left-aligned section titles
- **Section heading responsive font-sizes**:
  - Mobile (< 620px): `var(--text-heading-s)` (24px, $heading/S) — MANDATORY
  - Tablet (620px - 991px): `var(--text-heading-m)` (40px, $heading/M) — MANDATORY
  - Desktop (992px+): `var(--text-heading-l)` (64px, $heading/L) — MANDATORY
- **Section support text responsive font-sizes**:
  - Mobile (< 620px): `var(--text-body-s)` (16px, $body/S) — MANDATORY
  - Tablet (620px - 991px): `var(--text-body-m)` (18px, $body/M) — MANDATORY
  - Desktop (992px+): `var(--text-body-l)` (24px, $body/L) — MANDATORY

> **📖 See [typography.md](./typography.md) → \"Section Title & Subtitle Typography (RESPONSIVE)\" for complete implementation details.**

---

## Mandatory Rules

### 1. Use tokens, not arbitrary values

All spacing must reference a `--space-*` CSS variable or its Tailwind equivalent. Hardcoded pixel values are **prohibited** except where a CSS variable is used in an inline `style`.

```tsx
/* CORRECT — using token in inline style */
style={{ padding: 'var(--space-6)' }}
style={{ gap: 'var(--space-4)' }}

/* CORRECT — using Tailwind utility (maps to the same scale) */
className="px-4 py-12 gap-5"

/* PROHIBITED — arbitrary hardcoded pixel values */
style={{ padding: '17px' }}
style={{ gap: '22px' }}
```

### 2. Section padding conventions

> **MANDATORY: Every `<section>` on every page (`/`, `/mobile`, `/support`, `/business`, `/business/internet-leased-line`, `/home`, `/glass`, `/shop`) must use responsive section padding tokens.** This ensures uniform vertical rhythm between all sections across all pages and breakpoints. No exceptions except full-bleed hero banners that size via height instead of padding.

**Section Padding Tokens:**

**Desktop (768px+):**
- `--section-padding-top` → `var(--spacing-massive)` → `--space-20` → **80px**
- `--section-padding-bottom` → `var(--space-10)` → **40px**

**Mobile (< 768px):**
- Padding Top → `var(--space-16)` → **64px** (Huge token)
- Padding Bottom → `var(--space-6)` → **24px** (M token)

**Implementation:**
All sections should use media queries to apply mobile-specific padding:
```tsx
<section
  style={{
    paddingTop: 'var(--section-padding-top)',
    paddingBottom: 'var(--section-padding-bottom)',
  }}
>
  <style>{`
    @media (max-width: 767px) {
      section {
        padding-top: var(--space-16) !important;
        padding-bottom: var(--space-6) !important;
      }
    }
  `}</style>
  {/* Section content */}
</section>
```

| Area | Horizontal | Vertical (Desktop) | Vertical (Mobile) |
|------|------------|-------------------|-------------------|
| Full-width sections | `px-4` (mobile) / `px-6` – `px-10` (desktop) | `var(--section-padding-top)` (80px) top / `var(--section-padding-bottom)` (40px) bottom | `var(--space-16)` (64px) top / `var(--space-6)` (24px) bottom |
| Container inner content | Handled by `.container` class | — | — |
| Cards (inner) | `var(--space-6)` – `var(--space-8)` | `var(--space-6)` – `var(--space-8)` |
| CTA buttons | `var(--space-5)` horizontal / `var(--space-2)` vertical | — |
| Toggle / tag pills | `var(--space-6)` horizontal / `var(--space-2)` vertical | — |

### 3. Grid & layout gaps

| Layout | Gap token | Notes |
|--------|-----------|-------|
| Card grids (2–4 col) | `var(--space-5)` | 20px between cards |
| Footer link columns | `var(--space-8)` / `var(--space-6)` | Desktop / mobile |
| Icon groups | `var(--space-4)` – `var(--space-6)` | Quick-action rows |
| Inline button groups | `var(--space-3)` | CTA button pairs |
| Carousel slides | `var(--space-4)` | Gap between visible slides |

### 4. Vertical rhythm between elements

| Between | Token |
|---------|-------|
| Section title → subtitle | `var(--space-2)` (8px) |
| Section title (or subtitle) → content | `var(--space-8)` (32px) |
| Sub-heading → body text | `var(--space-2)` – `var(--space-3)` |
| Content block → CTA buttons | `var(--space-5)` (20px) |
| Divider → content | `var(--space-6)` (24px) |
| List items (stacked) | `var(--space-3)` (12px) |

---

## Responsive Adjustments

Spacing scales down on mobile. Use Tailwind responsive prefixes (`md:`, `lg:`) or clamp:

```tsx
/* Mobile-first, increasing on desktop */
className="px-4 md:px-6 lg:px-10"
className="py-12 md:py-16"
className="gap-4 sm:gap-6"
```

Never reduce spacing below `--space-2` (8px) on any breakpoint.

---

## Typography Rules

All text must use:

- **Font family:** `var(--font-family-jiotype)` exclusively
- **Font weights:** Only the four permitted JDS weight tokens:
  - `var(--font-weight-normal)` (400)
  - `var(--font-weight-medium)` (500)
  - `var(--font-weight-bold)` (700)
  - `var(--font-weight-black)` (900)
- **No other fonts or weights** are allowed.

> **📖 See [typography.md](./typography.md) for the full typography specification.**

---

## Best Practices

### Do
✔ Use spacing tokens exclusively  
✔ Apply 4px increment rule consistently  
✔ Ensure minimum 48x48px touch targets  
✔ Maintain consistent vertical rhythm  
✔ Use the box model for accurate spacing  

### Don't
✖ Use arbitrary pixel values  
✖ Create touch targets smaller than 48x48px  
✖ Space touch targets closer than 8px apart  
✖ Break the 4px increment system  
✖ Mix different spacing systems  

---

## Summary

Spacing is fundamental to creating clean, balanced, and accessible Jio interfaces. By following the 4px increment system, using spacing tokens consistently, and respecting touch target requirements, layouts remain **predictable, scalable, and user-friendly** across all devices and platforms.

**If it doesn't follow the spacing system — it doesn't ship.**