# Product Card Compact — Recent Updates

**Last Updated:** February 25, 2026

This document describes the recent updates to the Product Card Compact variant (`/src/app/components/ProductCard.tsx`) used in the "Now do more with your TV" section carousel.

## What Changed

### 1. Content Alignment — Top vs Bottom

**Previous:** Content (logo, description, CTA) was pinned to the bottom of the card using `justify-end`.

**Current:** Content is now pinned to the **top** of the card using `justify-start` for better visual hierarchy.

### 2. Image Positioning

**Previous:** Image used default `object-position: center`.

**Current:** Image now uses `object-position: center bottom` to ensure the main focus area of the image appears at the bottom of the card.

### 3. Gradient Direction

**Previous:** Used bottom-to-top gradient (`var(--gradient-product-btt)`) with dark overlay at bottom.

**Current:** Uses top-to-bottom gradient (`var(--gradient-card-ttb)`) with dark overlay at top to provide contrast for the top-aligned content.

### 4. Carousel Behavior — Responsive Mobile-Optimized

**Previous:** Standard Embla carousel with `containScroll: 'trimSnaps'` and fixed 25% card width.

**Current:** Responsive carousel layout with drag-free behavior and peek effect:
- `dragFree: true` for smooth free-scrolling on mobile
- `containScroll: false` for overflow-right effect
- **Responsive card widths** based on breakpoint (see below)
- Special padding-left calculation for container alignment
- **Navigation arrows hidden on mobile**, visible on desktop (≥992px)

### 5. Card Width — Responsive Layout with Peek Effect

**Previous:** Responsive width using `clamp(280px, 72vw, 300px)`.

**Current:** Responsive breakpoint-based layout with peek effect to encourage scrolling:
- **Mobile (< 768px):** `calc(85% - 10px)` — 1 full card + peek of next card visible
- **Tablet (768px - 991px):** `calc(50% - 10px)` — 2 cards visible
- **Desktop (≥992px):** `calc(30% - 14px)` — 3 full cards + partial 4th card visible
- Gap between cards: `var(--space-5)` (20px)
- Navigation arrows only appear on desktop (≥992px)

## Updated Visual Structure

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

## Updated Layout Rules

| Property              | Value                                         | Notes                           |
| --------------------- | --------------------------------------------- | ------------------------------- |
| Content position      | Flex column, `justify-start` (pinned to top)  | **Changed from justify-end**    |
| Image object-position | `center bottom` (focus area at bottom)        | **New addition**                |
| Gradient overlay      | `var(--gradient-card-ttb)` (top-to-bottom)    | **Changed from gradient-product-btt** |

## Complete Carousel Implementation

Reference: `/src/app/components/JioHomeProducts.tsx`

### Embla Configuration

```tsx
const [emblaRef, emblaApi] = useEmblaCarousel({
  align: 'start',
  loop: false,
  skipSnaps: false,
  containScroll: false,    // Allows overflow for right-scroll effect
  dragFree: true,          // Smooth free-scrolling on mobile
});
```

### Carousel Layout — Responsive Overflow-Right Pattern

```tsx
<style>{`
  /* Responsive card sizing for carousel */
  .product-carousel-card {
    flex: 0 0 calc(85% - 10px); /* Mobile: ~1 card + peek of next */
  }

  @media (min-width: 768px) {
    .product-carousel-card {
      flex: 0 0 calc(50% - 10px); /* Tablet: 2 cards */
    }
  }

  @media (min-width: 992px) {
    .product-carousel-card {
      flex: 0 0 calc(30% - 14px); /* Desktop: ~3 cards + peek of 4th */
    }
  }

  /* Hide navigation arrows on mobile */
  .carousel-navigation {
    display: none;
  }

  @media (min-width: 992px) {
    .carousel-navigation {
      display: flex;
    }
  }
`}</style>

{/* Carousel container with special padding */}
<div style={{ marginBottom: 'var(--space-8)' }}>
  <div
    ref={emblaRef}
    className="overflow-hidden"
    style={{
      paddingLeft: 'max(var(--container-padding-mobile), calc((100% - var(--container-max-width)) / 2 + var(--container-padding-desktop)))',
    }}
  >
    <div className="flex" style={{ gap: 'var(--space-5)' }}>
      {products.map((product) => (
        <div
          key={product.id}
          className="shrink-0"
          className=\"product-carousel-card\"
        >
          <ProductCard card={product} />
        </div>
      ))}
    </div>
  </div>
</div>

{/* Navigation arrows inside container */}
<div className="container mx-auto">
  <div className="flex items-center justify-end" style={{ gap: 'var(--space-3)' }}>
    <button
      onClick={scrollPrev}
      disabled={!canScrollPrev}
      style={{
        width: '44px',
        height: '44px',
        borderRadius: 'var(--radius-button)',
        border: 'var(--border-width-medium) solid var(--grey-40)',
        backgroundColor: 'var(--global-white)',
        color: canScrollPrev ? 'var(--foreground)' : 'var(--grey-60)',
        opacity: canScrollPrev ? 1 : 0.3,
      }}
    >
      <IcChevronLeft className="w-5 h-5" />
    </button>
    <button
      onClick={scrollNext}
      disabled={!canScrollNext}
      style={{
        width: '44px',
        height: '44px',
        borderRadius: 'var(--radius-button)',
        border: 'var(--border-width-medium) solid var(--grey-40)',
        backgroundColor: 'var(--global-white)',
        color: canScrollNext ? 'var(--foreground)' : 'var(--grey-60)',
        opacity: canScrollNext ? 1 : 0.3,
      }}
    >
      <IcChevronRight className="w-5 h-5" />
    </button>
  </div>
</div>
```

## Key Implementation Details

1. **Top-Aligned Content** — Cards use `justify-start` layout positioning content at the top for better readability
2. **Image Focus at Bottom** — `object-position: center bottom` ensures main subject/focus area appears at bottom
3. **Embla Configuration** — `dragFree: true` and `containScroll: false` enable mobile-optimized scrolling behavior
4. **Overflow Padding** — Special `paddingLeft` calculation aligns first card with container while enabling right overflow
5. **Responsive Card Widths** — CSS media queries define card widths per breakpoint with peek effect:
   - Mobile: `calc(85% - 10px)` — 1 card + peek
   - Tablet: `calc(50% - 10px)` — 2 cards
   - Desktop: `calc(30% - 14px)` — 3 cards + peek of 4th
6. **Conditional Navigation** — Arrows hidden on mobile/tablet via CSS media query, visible only on desktop (≥992px)
7. **Navigation State** — Track `canScrollPrev` and `canScrollNext` for proper button disabled states
8. **Container Alignment** — Heading and navigation arrows use `.container` class for grid consistency

## Responsive Behavior Across Breakpoints

**Mobile (< 768px):**
- Single card visible at ~85% width with peek of next card
- Navigation arrows **hidden** (swipe/drag only)
- Each card takes `calc(85% - 10px)` of the viewport width
- 20px gap between cards (`var(--space-5)`)
- Smooth scrolling enabled with drag-free behavior
- Peek effect encourages horizontal scrolling

**Tablet (768px - 991px):**
- 2 cards visible simultaneously
- Each card takes `calc(50% - 10px)` of the container width
- 20px gap between cards
- Navigation arrows **hidden** (swipe/drag only)

**Desktop (≥992px):**
- 3 full cards visible + partial 4th card (~30% width each)
- Each card takes `calc(30% - 14px)` of the container width
- 20px gap between cards (`var(--space-5)`)
- Navigation arrows **visible** at bottom-right
- Peek of 4th card indicates more content available

## CSS Variables Used

All styling continues to use JDS design tokens:

```css
/* Card Heights */
--card-product-compact-height-desktop: 504px;
--card-product-compact-height-mobile: 416px;

/* Gradients */
--gradient-card-ttb: linear-gradient(to bottom, ...);  /* Top-to-bottom */

/* Spacing */
--space-5: 20px;  /* Card gap */
--space-8: 32px;  /* Section margin */

/* Colors */
--global-white: #FFFFFF;
--grey-40: #E0E0E0;
--grey-60: #B5B5B5;
--foreground: (inherits from theme)
```

## Related Files

- Component: `/src/app/components/ProductCard.tsx`
- Implementation: `/src/app/components/JioHomeProducts.tsx`
- Main Documentation: `/guidelines/MD/Component/card.md` (see Product Card Compact section)
- CSS Variables: `/src/styles/theme.css`