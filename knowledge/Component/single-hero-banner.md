# Single Hero Banner — Component Specification

## Overview

The Single Hero Banner is a reusable promotional component implementing the Single Banner variant from the Hero Banner specification. It features a full-bleed background image, gradient overlay, optional product logo, heading, description, and up to two CTA buttons.

Component: `/src/app/components/SingleHeroBanner.tsx`
Parent Spec: `/guidelines/MD/Component/hero-banner.md`

---

## Usage

```tsx
import { SingleHeroBanner } from '../components/SingleHeroBanner';

<SingleHeroBanner
  image="https://images.unsplash.com/..."
  alt="Descriptive alt text"
  productLogo="JioHome"
  title="Exciting Offer"
  description="Get amazing benefits with our new plans."
  cta="Learn More"
  ctaVariant="default"
  cta2="Shop Now"
  cta2Variant="secondary"
/>
```

---

## Props Interface

```ts
interface SingleHeroBannerProps {
  image: string;                    // Required: Background image URL
  alt: string;                      // Required: Image alt text for accessibility
  productLogo?: string;             // Optional: Product/brand name displayed above title
  title?: string;                   // Optional: Main heading (supports \n for line breaks via whiteSpace: pre-line)
  description?: string;             // Optional: Support text below title
  cta?: string;                     // Optional: Primary CTA button text
  ctaVariant?: 'default' | 'defaultInverse' | 'primary' | 'secondary';  // Default: 'default'
  cta2?: string;                    // Optional: Secondary CTA button text
  cta2Variant?: 'default' | 'defaultInverse' | 'primary' | 'secondary'; // Default: 'secondary'
  backgroundColor?: string;         // Optional: Solid background color (CSS variable or hex)
}
```

---

## Responsive Specifications

### Container Dimensions

| Breakpoint | Width | Height |
| ---------- | ----- | ------ |
| **Desktop** (≥992px) | 1184px max-width | `clamp(280px, 40vw, 500px)` |
| **Tablet** (768px-991px) | 704px fixed | 563px fixed |
| **Mobile** (<768px) | 312px fixed | 520px fixed |

### Content Positioning

| Breakpoint | Justify | Max Width | Padding Left/Right | Padding Top/Bottom |
| ---------- | ------- | --------- | ------------------ | ------------------ |
| **Desktop** (≥992px) | `center` (vertically) | 50% | `var(--space-16)` (64px) | `var(--space-6)` (24px) |
| **Tablet** (768px-991px) | `flex-start` (top) | 100% | Left: `var(--space-12)` (48px), Right: `var(--space-30)` (120px) | `var(--space-6)` (24px) |
| **Mobile** (<768px) | `flex-start` (top) | 100% | `var(--space-4)` (16px) | `var(--space-6)` (24px) |

### Typography

| Element | Desktop/Tablet | Mobile |
| ------- | -------------- | ------ |
| **Product Logo** | `var(--text-body-m)` (18px), Bold | `var(--text-body-m)` (18px), Bold |
| **Title** | `var(--text-heading-m)` (40px), Black | `var(--text-heading-s)` (24px), Black |
| **Description** | `var(--text-body-m)` (18px), Medium | `var(--text-body-s)` (16px), Medium |

---

## Styling Tokens

All styling uses JDS design system tokens from `/src/styles/theme.css`:

### Spacing
- Section padding: `var(--section-padding-top)` / `var(--section-padding-bottom)`
- Border radius: `var(--radius-lg)` (24px)
- Content gaps: `var(--space-2)` through `var(--space-6)`

### Colors
- Background: `var(--global-white)`
- Text color: `var(--primary-inverse)` (white for dark backgrounds)
- Gradient overlay: `var(--gradient-hero-ltr)` (left-to-right)

### Typography
- Font family: `var(--font-family-jiotype)` (JioType exclusively)
- Font weights: `var(--font-weight-bold)`, `var(--font-weight-black)`, `var(--font-weight-medium)`
- Line heights: 1.2 (headings), 1.5 (body text)

---

## Layout Structure

```
┌─────────────────────────────────────────┐
│ Section (section-padding)               │
│ ┌─────────────────────────────────────┐ │
│ │ Container (mx-auto)                 │ │
│ │ ┌─────────────────────────────────┐ │ │
│ │ │ Banner (radius-lg, responsive)  │ │ │
│ │ │                                 │ │ │
│ │ │  [Background Image]             │ │ │
│ │ │  [Gradient Overlay]             │ │ │
│ │ │                                 │ │ │
│ │ │  ┌───────────────────┐          │ │ │
│ │ │  │ Content (50% max) │          │ │ │
│ │ │  │                   │          │ │ │
│ │ │  │ [Product Logo]    │          │ │ │
│ │ │  │ [Title]           │          │ │ │
│ │ │  │ [Description]     │          │ │ │
│ │ │  │ [CTA Buttons]     │          │ │ │
│ │ │  └───────────────────┘          │ │ │
│ │ └─────────────────────────────────┘ │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## Accessibility

- **Alt text**: Required `alt` prop for background images
- **Semantic HTML**: Uses `<section>`, `<h2>`, `<p>` elements
- **Color contrast**: White text (`--primary-inverse`) on gradient-overlaid images ensures readability
- **Keyboard navigation**: CTA buttons are fully keyboard accessible

---

## Examples

### Basic Banner (Title + CTA only)

```tsx
<SingleHeroBanner
  image="https://images.unsplash.com/photo-..."
  alt="Join Jio team"
  title="Careers at Jio"
  cta="Apply Now"
  ctaVariant="default"
/>
```

### Full-Featured Banner

```tsx
<SingleHeroBanner
  image="https://images.unsplash.com/photo-..."
  alt="JioHome entertainment streaming"
  productLogo="JioHome"
  title="Unlimited Entertainment\nfor the Whole Family"
  description="Stream 18+ OTT apps with one subscription. Cricket, movies, series & more."
  cta="Get JioHome"
  ctaVariant="default"
  cta2="Learn More"
  cta2Variant="secondary"
/>
```

### With Solid Background Color

```tsx
<SingleHeroBanner
  image="https://images.unsplash.com/photo-..."
  alt="Business solutions"
  backgroundColor="var(--primary-60)"
  title="Enterprise Solutions"
  description="Scale your business with Jio's connectivity."
  cta="Contact Sales"
  ctaVariant="defaultInverse"
/>
```

---

## Design Notes

1. **Line Breaks in Title**: Use `\n` in the title string for multiline headings (handled via `whiteSpace: pre-line`)
2. **Gradient Overlay**: Always applied (`var(--gradient-hero-ltr)`) to ensure text readability
3. **Responsive Behavior**: Content justified center on desktop, top-left on tablet/mobile
4. **CTA Spacing**: Buttons have `var(--space-3)` gap and wrap on smaller screens
5. **Image Handling**: Uses `ImageWithFallback` component for proper image loading

---

## Related Components

- **HeroCarousel** (`/src/app/components/HeroCarousel.tsx`) — Carousel variant with multiple slides
- **BusinessBanner** (`/src/app/components/BusinessBanner.tsx`) — Business-specific banner
- **ILLBanner** (`/src/app/components/ILLBanner.tsx`) — Internet Leased Line banner
- **ShopHeroBanner** (`/src/app/components/ShopHeroBanner.tsx`) — Shop page banner with search

---

## Migration from CareersBanner

The `SingleHeroBanner` component replaces the deprecated `CareersBanner` component with a more flexible, reusable API following the hero-banner.md specification.

**Before:**
```tsx
import { CareersBanner } from '../components/CareersBanner';
<CareersBanner />
```

**After:**
```tsx
import { SingleHeroBanner } from '../components/SingleHeroBanner';
<SingleHeroBanner
  image="https://images.unsplash.com/photo-1627599936744-51d288f89af4?..."
  alt="Careers at Jio - Join our team at Reliance Jio"
  title="Careers at Jio"
  description="Join our team and explore exciting opportunities at Reliance Jio across different roles."
  cta="Explore Opportunities"
  ctaVariant="default"
/>
```
