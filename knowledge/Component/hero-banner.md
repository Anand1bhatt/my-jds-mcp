# Hero Banner — Component Specification

## Overview

The Hero Banner is a versatile promotional component that comes in two variants: **Carousel Banner** and **Single Banner**. Both variants feature full-bleed backgrounds (image/vector/color), optional product logos, headings, support text, and call-to-action buttons.

Component: `/src/app/components/HeroBanner.tsx`

---

## Banner Variants

### 1. Carousel Banner
A horizontally-scrolling carousel of hero banners with autoplay, navigation controls, and optional pagination.

### 2. Single Banner
A standalone hero banner without carousel functionality.

---

## Banner Specifications by Device

### Desktop Device

#### Anatomy

**Container:**
| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Banner Size           | 1184px (max-width, centered)             |
| Background            | Image / Vector / Color                   |
| Border radius         | `var(--radius-lg)` (24px)                |
| Padding Top           | `var(--space-6)` (24px)                  |
| Padding Bottom        | `var(--space-6)` (24px)                  |
| Padding Left          | `var(--space-16)` (64px)                 |
| Padding Right         | `var(--space-16)` (64px)                 |
| Overflow              | `hidden`                                 |
| Height                | `clamp(280px, 40vw, 500px)`              |

**Product Logo (Optional):**
| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Size                  | Default (Desktop)                        |
| Font size             | `var(--text-body-m)` (18px)              |
| Font weight           | `var(--font-weight-bold)` (700)          |
| Brand Label           | Optional text or image                   |
| Margin bottom         | `var(--space-4)` (16px)                  |

**Heading (Optional):**
| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Typography            | `$desktop/Heading/M`                     |
| Font family           | `var(--font-family-jiotype)`             |
| Font size             | `var(--text-heading-m)` (40px)           |
| Font weight           | `var(--font-weight-black)` (900)         |
| Line height           | 1.2                                      |
| Color (light bg)      | `var(--grey-100)` (for light background & light image) |
| Color (dark bg)       | `var(--primary-inverse)` (for dark background & dark image) |
| White space           | `pre-line` (supports `\\n` line breaks)   |
| Margin bottom         | `var(--space-2)` (8px)                   |

**Support Text (Optional):**
| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Typography            | `$desktop/Body/M`                        |
| Font family           | `var(--font-family-jiotype)`             |
| Font size             | `var(--text-body-m)` (18px)              |
| Font weight           | `var(--font-weight-medium)` (500)        |
| Line height           | 1.5                                      |
| Color (light bg)      | `var(--grey-100)` (for light background & light image) |
| Color (dark bg)       | `var(--primary-inverse)` (for dark background & dark image) |
| Margin bottom         | `var(--space-6)` (24px)                  |

**Buttons (Optional):**
| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Primary Button        | `variant="default"` (Primary default)    |
| Secondary Button      | `variant="secondary"` (optional)         |
| Spacing (from text)   | `var(--space-6)` (24px) margin bottom from support text |
| Gap between buttons   | `var(--space-3)` (12px)                  |

**Content Alignment:** Top left align of the banner

---

## Carousel Banner Specifications

### Carousel Configuration

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Engine                | Embla Carousel                           |
| Alignment             | `center`                                 |

### Carousel Dimensions

| Property              | Desktop (≥992px)                         | Tablet (620-991px)                     | Mobile (324-619px)                          |
| --------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Individual banner max-width | `1184px` (fixed width, centered)   | `704px` (fixed width, centered)          | `312px` (fixed width, centered)          |
| Slide width           | `1184px` max-width (centered in viewport) | `704px` (centered in viewport)          | `312px` (centered in viewport)           |
| Slide height          | `clamp(280px, 40vw, 500px)`              | `563px` (fixed)                          | `520px` (fixed)                          |
| Border radius         | `var(--radius-lg)` (24px)                | `var(--radius-lg)` (24px)                | `var(--radius-lg)` (24px)                |
| Padding Top           | `var(--space-6)` (24px)                  | `var(--space-6)` (24px)                  | `var(--space-6)` (24px)                  |
| Padding Bottom        | `var(--space-6)` (24px)                  | `var(--space-6)` (24px)                  | `var(--space-6)` (24px)                  |
| Padding Left          | `var(--space-16)` (64px)                 | `var(--space-12)` (48px)                 | `var(--space-4)` (16px)                  |
| Padding Right         | `var(--space-16)` (64px)                 | `var(--space-30)` (120px)                | `var(--space-4)` (16px)                  |
| Content max-width     | 50%                                      | 100%                                     | 100%                                     |
| Gap between slides    | `var(--space-4)` (16px)                  | `var(--space-4)` (16px)                  | `var(--space-2)` (8px)                   |
| Inactive opacity      | 0.65 (65%)                               | 0.65 (65%)                               | 0.65 (65%)                               |
| Active opacity        | 1.0 (100%)                               | 1.0 (100%)                               | 1.0 (100%)                               |

### Carousel Peek Effect (Adjacent Slides Visibility)

The carousel shows **partial visibility of adjacent slides** (left/right) on Mobile and Tablet to indicate scrollability and improve visual engagement.

| Property              | Desktop (≥992px)       | Tablet (768-991px)     | Mobile (<768px)        |
| --------------------- | ---------------------- | ---------------------- | ---------------------- |
| Viewport padding (left) | `0px` (no peek)      | `var(--space-6)` (24px) | `var(--space-4)` (16px) |
| Viewport padding (right) | `0px` (no peek)     | `var(--space-6)` (24px) | `var(--space-4)` (16px) |
| Adjacent slides visible | No                   | Yes (24px each side)   | Yes (16px each side)   |
| Overflow behavior     | Hidden                 | Visible                | Visible                |

**Implementation:**
```css
/* Mobile: 16px padding both sides for peek effect */
@media (max-width: 767px) {
  .hero-carousel-viewport {
    padding-left: var(--space-4);  /* 16px */
    padding-right: var(--space-4); /* 16px */
    overflow: visible;
  }
}

/* Tablet: 24px padding both sides for peek effect */
@media (min-width: 768px) and (max-width: 991px) {
  .hero-carousel-viewport {
    padding-left: var(--space-6);  /* 24px */
    padding-right: var(--space-6); /* 24px */
    overflow: visible;
  }
}

/* Desktop: No peek effect (full-width carousel) */
@media (min-width: 992px) {
  .hero-carousel-viewport {
    padding-left: 0;
    padding-right: 0;
    overflow: hidden;
  }
}
```

**Key Behaviors:**
- ✅ **Mobile:** 16px spacing on both sides shows adjacent slides partially visible
- ✅ **Tablet:** 24px spacing on both sides shows adjacent slides partially visible
- ✅ **Desktop:** No side spacing, full-width centered carousel (no peek effect)
- ✅ Inactive adjacent slides appear at 65% opacity
- ✅ Active centered slide appears at 100% opacity
- ✅ Follows grid behavior consistent with all page elements

### Navigation Controls

Located at the bottom-right corner of each banner slide, sticky positioned inside the banner.

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Position              | Absolute, bottom-right inside banner     |
| Background            | `var(--primary-background)`              |
| Border radius         | `var(--radius-button)` (250px)           |
| Padding               | `var(--space-1)` (4px)                   |
| Button size           | 36px × 36px                              |
| Button color          | `var(--primary-60)`                      |
| Counter color         | `var(--grey-100)`                        |
| Gap                   | `var(--space-1)` (4px)                   |
| Bottom offset         | `var(--space-6)` (24px) inside banner    |
| Right offset          | `var(--space-6)` (24px) inside banner    |

---

## Single Banner Specifications

### Dimensions

| Property              | Desktop (≥992px)                         | Tablet (620-991px)                     | Mobile (324-619px)                          |
| --------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Width                 | `1184px` max-width (centered)            | `704px` (fixed, centered)                | `312px` (fixed, centered)                |
| Height                | `clamp(280px, 40vw, 500px)`              | `563px` (fixed)                          | `520px` (fixed)                          |
| Border radius         | `var(--radius-lg)` (24px)                | `var(--radius-lg)` (24px)                | `var(--radius-lg)` (24px)                |
| Content padding       | `var(--space-16)` (64px) all sides       | Top/Bottom/Left: `var(--space-12)` (48px), Right: `var(--space-30)` (120px) | Top: `var(--space-6)` (24px), Sides/Bottom: `var(--space-4)` (16px) |
| Content max-width     | 50%                                      | 100%                                     | 100%                                     |

---

## Background Image Handling

### Full-Bleed Image

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Position              | `absolute inset-0`                       |
| Object fit            | `cover`                                  |
| Transition            | `transform 500ms`                        |
| Hover effect          | `scale(1.05)` (optional)                 |

### Gradient Overlay (for text readability)

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Position              | `absolute inset-0`                       |
| Background            | `var(--gradient-hero-ltr)` (left-to-right gradient) |
| Pointer events        | `none`                                   |

---

## Content Positioning

### Text Content

| Property              | Desktop (992px+)                         | Tablet & Mobile (< 992px)                |
| --------------------- | ---------------------------------------- | ---------------------------------------- |
| Position              | `absolute inset-0`                       | `absolute inset-0`                       |
| Display               | Flex column                              | Flex column                              |
| Justify content       | `center` (vertically centered)           | `flex-start` (top-left aligned)          |
| Padding (all sides)   | `var(--space-16)` (64px)                 | Varies by device (see breakpoint tables) |
| Max width             | 50% of banner width (for readability)    | 100% of banner width                     |
| Z-index               | 10                                       | 10                                       |

---

## Data Structure

### Carousel Banner

```ts
interface HeroBannerSlide {
  id: number;
  image: string;          // Unsplash URL or figma:asset
  alt: string;
  productLogo?: string;   // Optional product logo text
  title?: string;         // Supports \n for line breaks
  description?: string;   // Support text
  cta?: string;           // Primary button text
  ctaVariant?: 'primary' | 'secondary' | 'defaultInverse';
  cta2?: string;          // Optional secondary button text
  cta2Variant?: 'primary' | 'secondary' | 'defaultInverse';
}

interface CarouselBannerProps {
  variant: 'carousel';
  slides: HeroBannerSlide[];
}
```

### Single Banner

```ts
interface SingleBannerProps {
  variant: 'single';
  image: string;
  alt: string;
  productLogo?: string;
  title?: string;
  description?: string;
  cta?: string;
  ctaVariant?: 'primary' | 'secondary' | 'defaultInverse';
  cta2?: string;
  cta2Variant?: 'primary' | 'secondary' | 'defaultInverse';
  backgroundColor?: string;  // Optional solid color background
}
```

---

## Responsive Behavior

### Summary Table

| Breakpoint | Container Width | Container Height | Padding (Top/Bottom) | Padding (Left/Right) | Title Size | Description Size | Max Width | Navigation Controls |
| ---------- | --------------- | ---------------- | -------------------- | -------------------- | ---------- | ---------------- | --------- | ------------------- |
| Mobile (< 768px) | **312px - 605px (fluid)** | 520px (fixed) | **24px** (`var(--space-6)`) | 16px (`var(--space-4)`) | `var(--text-heading-s)` (24px) | `var(--text-body-s)` (16px) | 100% | Hidden |
| Tablet (768px - 991px) | **704px - 991px (fluid)** | 563px (fixed) | **24px** (`var(--space-6)`) | Left: 48px, Right: 120px | `var(--text-heading-m)` (40px) | `var(--text-body-m)` (18px) | 100% | Hidden |
| Desktop (992px+) | 1184px (max-width) | `clamp(280px, 40vw, 500px)` | **24px** (`var(--space-6)`) | 64px (`var(--space-16)`) | `var(--text-heading-m)` (40px) | `var(--text-body-m)` (18px) | 50% | Visible |

### Breakpoint Details

**Mobile (324-767px):**
- Container width: **312px - 605px (fluid)** — adapts to viewport, min 312px, max 605px
- Container height: 520px (fixed)
- Padding: **`var(--space-6)` top/bottom (24px)**, `var(--space-4)` left/right (16px)
- Title: `var(--text-heading-s)` (24px)
- Description: `var(--text-body-s)` (16px)
- Content max-width: 100% of banner width
- Content alignment: Top left
- Navigation controls: Hidden (carousel functionality active)
- Background image: Adopts fluid dimensions (312px - 605px) × 520px

**Tablet (768-991px):**
- Container width: **704px - 991px (fluid)** — adapts to viewport, min 704px, max 991px
- Container height: 563px (fixed)
- Padding: **`var(--space-6)` top/bottom (24px)**, `var(--space-12)` left (48px), `var(--space-30)` right (120px)
- Title: `var(--text-heading-m)` (40px)
- Description: `var(--text-body-m)` (18px)
- Content max-width: 100% of banner width
- Content alignment: Top left
- Navigation controls: Hidden (carousel functionality active)
- Background image: Adopts fluid dimensions (704px - 991px) × 563px

**Desktop (992px+):**
- Container width: 1184px (max-width, centered)
- Container height: `clamp(280px, 40vw, 500px)` (fluid with min/max)
- Padding: **`var(--space-6)` top/bottom (24px)**, `var(--space-16)` left/right (64px)
- Title: `var(--text-heading-m)` (40px)
- Description: `var(--text-body-m)` (18px)
- Content max-width: 50% of banner width (40% for optimal readability)
- Content alignment: Top left (vertically centered in container)
- Navigation controls: Visible

### Fluid Grid Behavior

The Hero Banner follows a **fluid grid system** where width adapts within breakpoint ranges:

| Breakpoint | Min Width | Max Width | Grid Columns | Behavior |
|-----------|-----------|-----------|--------------|----------|
| Mobile    | 312px     | 605px     | 4 columns    | Width: 100% (constrained by min/max) |
| Tablet    | 704px     | 991px     | 6 columns    | Width: 100% (constrained by min/max) |
| Desktop   | 992px     | 1184px    | 12 columns   | Width: 100% (max-width: 1184px) |

**Implementation:**
```css
/* Mobile: Fluid width 312px - 605px */
@media (max-width: 767px) {
  .hero-banner {
    width: 100%;
    min-width: 312px;
    max-width: 605px;
    height: 520px; /* Fixed */
  }
}

/* Tablet: Fluid width 704px - 991px */
@media (min-width: 768px) and (max-width: 991px) {
  .hero-banner {
    width: 100%;
    min-width: 704px;
    max-width: 991px;
    height: 563px; /* Fixed */
  }
}

/* Desktop: Fluid width up to 1184px */
@media (min-width: 992px) {
  .hero-banner {
    width: 100%;
    max-width: 1184px;
    height: clamp(280px, 40vw, 500px);
  }
}
```

**Key Rules:**
- ✅ Width is **fluid** — adapts to viewport size within min/max constraints
- ✅ Height is **fixed** — does not change when width changes
- ✅ Centered horizontally via `margin: 0 auto`
- ✅ Container padding remains constant per breakpoint

---

## Design Tokens Used

| Token                   | Value         | Usage                                      |
| ----------------------- | ------------- | ------------------------------------------ |
| `--radius-lg`           | `24px`        | Container border radius                    |
| `--space-16`            | `64px`        | Content padding (all sides) — Desktop      |
| `--space-12`            | `48px`        | Content padding — Tablet                   |
| `--space-6`             | `24px`        | Support text to button spacing             |
| `--space-5`             | `20px`        | Button margin top                          |
| `--space-4`             | `16px`        | Brand label to heading spacing, Carousel slide gap (Desktop/Tablet) |
| `--space-3`             | `12px`        | Button gap                                 |
| `--space-2`             | `8px`         | Heading to support text spacing, Carousel slide gap (Mobile) |
| `--space-1`             | `4px`         | Control padding, gap                       |
| `--gradient-hero-ltr`   | Custom        | Background gradient overlay                |
| `--primary-background`  | `#FFFFFF`     | Control background                         |
| `--primary-inverse`     | `#FFFFFF`     | Text color (dark bg)                       |
| `--grey-100`            | `#141414`     | Text color (light bg)                      |
| `--primary-60`          | `#004B9D`     | Control button color                       |
| `--font-family-jiotype` | JioType stack | Font family                                |
| `--text-heading-m`      | `40px`        | Heading size — Desktop & Tablet            |
| `--text-heading-s`      | `24px`        | Heading size — Mobile                      |
| `--text-body-m`         | `18px`        | Support text size — Desktop & Tablet, Brand label |
| `--text-body-s`         | `16px`        | Support text size — Mobile                 |
| `--font-weight-black`   | `900`         | Heading font weight                        |
| `--font-weight-bold`    | `700`         | Brand label font weight                    |
| `--font-weight-medium`  | `500`         | Support text font weight                   |
| `--radius-button`       | `250px`       | Control border radius                      |

---

## Content Spacing Specifications

**All Devices (Desktop, Tablet, Mobile):**

| Element Pair                    | Spacing       | CSS Variable      |
| ------------------------------- | ------------- | ----------------- |
| Brand Label → Heading           | 16px          | `var(--space-4)`  |
| Heading → Support Text          | 8px           | `var(--space-2)`  |
| Support Text → Button           | 24px          | `var(--space-6)`  |
| Button → Button (horizontal)    | 12px          | `var(--space-3)`  |

---

## Accessibility

- All images have descriptive `alt` text.
- Navigation controls have `aria-label` attributes.
- Carousel is keyboard-accessible (arrow keys work when focused).
- Text has sufficient contrast against backgrounds (via gradient overlays).
- Autoplay can be paused on hover/focus.

---

## Usage Examples

### Carousel Banner

```tsx
import { HeroBanner } from '../components/HeroBanner';

const slides = [
  {
    id: 1,
    image: 'https://images.unsplash.com/...',
    alt: 'Product showcase',
    productLogo: 'JioBusiness',
    title: 'Enterprise-grade\n5G connectivity',
    description: 'Ultra-low latency and blazing-fast speeds.',
    cta: 'Get started',
    ctaVariant: 'primary',
  },
  // ... more slides
];

export function BusinessPage() {
  return (
    <>
      <HeroBanner variant="carousel" slides={slides} />
    </>
  );
}
```

### Single Banner

```tsx
import { HeroBanner } from '../components/HeroBanner';

export function PromoSection() {
  return (
    <HeroBanner
      variant="single"
      image="https://images.unsplash.com/..."
      alt="Special offer"
      title="Limited time offer"
      description="Get 50% off on all plans"
      cta="Claim now"
      ctaVariant="primary"
    />
  );
}
```

---

## Notes

- The carousel uses Embla Carousel with autoplay plugin for smooth scrolling.
- Hover effect on slides provides visual feedback.
- Gradient overlays ensure text is always readable regardless of image content.
- CTA buttons adapt to background (use `defaultInverse` for dark images).
- All content sections (product logo, heading, description, buttons) are optional for maximum flexibility.