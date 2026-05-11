# ILL Transform — Component Specification

## Overview

The ILL Transform section showcases 4 key benefits of JioBusiness Internet Leased Line using IconCard components in a 3-column grid layout. The section heading is "Tailored to transform".

Component: `/src/app/components/ILLTransform.tsx`

---

## Layout

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Section padding       | `var(--space-12)` (48px) top & bottom    |
| Background            | `var(--global-white)` (#FFFFFF)          |
| Container             | Centered, max-width constrained          |
| Grid                  | `grid-cols-1 md:grid-cols-3`             |
| Gap                   | `var(--space-6)` (24px)                  |

---

## Section Heading

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Tag                   | `<h2>`                                   |
| Text                  | "Tailored to transform"                  |
| Font family           | `var(--font-family-jiotype)`             |
| Font size             | `var(--text-heading-m)` (40px)           |
| Font weight           | `var(--font-weight-black)` (900)         |
| Color                 | `var(--foreground)` (#141414)            |
| Line height           | 1.2                                      |
| Text align            | Center                                   |
| Margin bottom         | `var(--space-10)` (40px)                 |

---

## Grid Structure

- **Columns:** 3 on desktop (`md:grid-cols-3`), 1 on mobile
- **Rows:** 2 (4 cards wrap naturally into 2 rows of 2–1 cards)
- **Gap:** `var(--space-6)` (24px) between cards

---

## Cards

Uses the standard `IconCard` component from `/src/app/components/IconCard.tsx`.

Each card contains:

1. **Icon circle** (56×56px) with theme-specific background and icon color
2. **Title** (H4, 24px, JioType Black)
3. **Body text** (paragraph, 16px, JioType Normal)
4. **Tertiary CTA** ("Learn more" text link with arrow)

### Card Data

| Card | Icon          | Title                       | Icon BG Token         | Icon Color Token      |
| ---- | ------------- | --------------------------- | --------------------- | --------------------- |
| 1    | Zap           | Lightning-fast speeds       | `--secondary-20`      | `--secondary-60`      |
| 2    | Shield        | Enterprise-grade security   | `--error-20`          | `--error-60`          |
| 3    | TrendingUp    | Guaranteed uptime           | `--sparkle-20`        | `--sparkle-60`        |
| 4    | Headphones    | Dedicated support           | `--primary-20`        | `--primary-50`        |

---

## Icon Card Specification

See `/src/app/components/card.md` → "Icon Card Variant" for full IconCard spec.

**Quick Summary:**

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Card border radius    | `calc(var(--radius) * 2)` (16px)         |
| Card border           | `1px solid var(--grey-40)`               |
| Card background       | `var(--global-white)`                    |
| Card padding          | `var(--space-6)` (24px)                  |
| Icon size             | 24px (w-6 h-6)                           |
| Icon circle size      | 56×56px                                  |
| Icon circle radius    | `calc(var(--radius) * 1.5)` (12px)       |
| Title font size       | `var(--text-h4)` (24px)                  |
| Body font size        | `var(--text-base)` (16px)                |
| CTA font size         | `var(--text-label)` (14px)               |

---

## Responsive Behavior

| Breakpoint | Columns   | Card Layout                       |
| ---------- | --------- | --------------------------------- |
| Mobile     | 1 column  | Cards stack vertically            |
| md+        | 3 columns | 4 cards wrap into 2 rows (2+2 or 2+1+1) |

---

## Content

### Card 1: Lightning-fast speeds
"Symmetrical bandwidth up to 10 Gbps ensures your uploads match your downloads for seamless cloud operations."

### Card 2: Enterprise-grade security
"Dedicated line with end-to-end encryption, DDoS protection, and compliance-ready infrastructure."

### Card 3: Guaranteed uptime
"99.99% SLA-backed uptime with automatic failover, redundant paths, and proactive monitoring."

### Card 4: Dedicated support
"24/7 NOC team, priority ticket resolution, and a dedicated account manager for enterprise clients."

---

## Design Tokens Used

| Token                   | Value         | Usage                          |
| ----------------------- | ------------- | ------------------------------ |
| `--space-12`            | `48px`        | Section vertical padding       |
| `--space-10`            | `40px`        | Heading margin bottom          |
| `--space-6`             | `24px`        | Grid gap                       |
| `--global-white`        | `#FFFFFF`     | Section background             |
| `--foreground`          | `#141414`     | Heading color                  |
| `--font-family-jiotype` | JioType stack | Font family                    |
| `--text-heading-m`      | `40px`        | Heading font size              |
| `--font-weight-black`   | `900`         | Heading font weight            |
| `--primary-20`          | `#E8E8FC`     | Icon BG (card 4)               |
| `--primary-50`          | `#3535F3`     | Icon color (card 4)            |
| `--secondary-20`        | `#FEF7E9`     | Icon BG (card 1)               |
| `--secondary-60`        | `#AC660C`     | Icon color (card 1)            |
| `--error-20`            | `#FFF1F0`     | Icon BG (card 2)               |
| `--error-60`            | `#CD0027`     | Icon color (card 2)            |
| `--sparkle-20`          | `#E8FAF7`     | Icon BG (card 3)               |
| `--sparkle-60`          | `#1E7B74`     | Icon color (card 3)            |

---

## Accessibility

- Semantic heading (`<h2>`) for the section title.
- Each IconCard has proper heading hierarchy (`<h4>` for card title).
- Icon cards are keyboard-navigable.
- CTA text links have hover states and focus indicators.

---

## Usage

```tsx
import { ILLTransform } from '../components/ILLTransform';

export function InternetLeasedLinePage() {
  return (
    <>
      <ILLBanner />
      <ILLTransform />
      <ILLDrivingSolutions />
    </>
  );
}
```

---

## Notes

- The 3-column grid naturally wraps the 4 cards into 2 rows on desktop.
- Icons are from the `lucide-react` package.
- IconCard uses the `mt-auto` utility to push the CTA to the bottom of the card for consistent alignment.
- The icon color pairings use different JDS color scales (primary, secondary, sparkle, error) for visual variety.
