# Intro Component Specification

## Overview

The **Intro** component is a reusable hero-intro pattern used as the introductory section on landing pages (e.g., JioHome, Mobile, Business). It features a two-column layout with a heading and support text, designed to provide a concise overview of the page's key services or offerings.

Each page supplies its own heading and support text content while sharing the same structure, spacing, typography, colors, and responsive behavior.

---

## Structure

### Layout System

- **Grid:** 12-column responsive grid
- **Alignment:** Top-aligned (`items-start`)
- **Column Distribution:**
  - **Desktop & Tablet:** Heading + 2-column gap + Support Text
  - **Mobile:** Both elements stack to full width (12 columns)

### Column Layout Options

The grid uses a 12-column system with **2 columns of spacing** between heading and support text:

**Option 1: 5-2-5 Layout (Recommended)**
- Heading: 5 columns
- Gap: 2 columns (empty space)
- Support Text: 5 columns
- Total: 12 columns

**Option 2: 4-2-6 Layout**
- Heading: 4 columns
- Gap: 2 columns (empty space)
- Support Text: 6 columns
- Total: 12 columns

**Implementation:** Use `col-start-*` utility to create the 2-column gap.

### Content Elements

1. **Heading**
   - Page-specific intro heading
   - Uses `SectionHeading` component
   - Left-aligned within its column
   - Typography follows responsive section heading scale

2. **Support Text**
   - Page-specific description text
   - Uses `SectionSupportText` component
   - Left-aligned within its column
   - Typography follows responsive section support text scale

---

## Spacing

### Section Padding

**Top Padding:**
- All breakpoints: `32px` (`var(--space-8)`)

**Bottom Padding:**
- All breakpoints: `0px` (none)

### Internal Spacing

**Column Gap:**
- All breakpoints: `32px` (`var(--space-8)`)

**Column Spacing Pattern:**
- **2 columns of empty space** between heading and support text on desktop/tablet
- On mobile, elements stack with the column gap applied vertically

---

## Typography

### Heading

Uses `SectionHeading` component with responsive typography:

- **Mobile (< 620px):** `$heading/S` (24px, font-weight: 900)
- **Tablet (620px - 991px):** `$heading/M` (40px, font-weight: 900)
- **Desktop (992px+):** `$heading/M` (40px, font-weight: 900)

**Font Family:** `var(--font-family-jiotype)` (JioType)

### Support Text

Uses `SectionSupportText` component with responsive typography:

- **Mobile (< 620px):** `$body/S` (16px, font-weight: 500)
- **Tablet (620px - 991px):** `$body/M` (18px, font-weight: 500)
- **Desktop (992px+):** `$body/M` (18px, font-weight: 500)

**Font Family:** `var(--font-family-jiotype)` (JioType)

**Text Alignment:** Left-aligned (overrides default center alignment from SectionHeading/SectionSupportText)

---

## Colors

### Background
- `var(--global-white)` (#FFFFFF)

### Text Colors
- **Heading:** `var(--foreground)` (from SectionHeading component)
- **Support Text:** `var(--grey-80)` (from SectionSupportText component)

---

## Responsive Behavior

### Desktop (992px+)
- Two-column layout with 2-column gap (5-2-5 or 4-2-6)
- Top padding: 32px
- Column gap: 32px

### Tablet (620px - 991px)
- Two-column layout with 2-column gap (5-2-5 or 4-2-6)
- Top padding: 32px
- Column gap: 32px

### Mobile (< 620px)
- Stacked layout: Both elements full width (12 columns)
- Top padding: 32px
- Vertical gap: 32px between heading and support text

---

## Design System Compliance

### Typography
- All typography uses **JioType font family** from `/src/styles/fonts.css`
- Uses predefined `SectionHeading` and `SectionSupportText` components
- No arbitrary font sizes or weights
- Only uses CSS variable typography tokens

### Colors
- All colors use **CSS variables** from `/src/styles/theme.css`
- Background: `var(--global-white)`
- Text colors inherited from section components
- No hardcoded color values

### Spacing
- All spacing uses **CSS variables** from `/src/styles/theme.css`
- Top padding: `var(--space-8)` (32px)
- Bottom padding: `0`
- Column gap: `var(--space-8)` (32px)
- No arbitrary spacing values

### Layout
- Uses `.container` class for responsive container with max-width constraints
- Uses Tailwind grid utilities (`grid`, `grid-cols-12`, `col-span-*`, `col-start-*`)
- Follows JDS grid system specifications

---

## Implementation Pattern

### 5-2-5 Layout (Recommended)

```tsx
export function PageIntro() {
  return (
    <section
      className="w-full"
      style={{
        paddingTop: 'var(--space-8)',
        paddingBottom: 0,
        backgroundColor: 'var(--global-white)',
      }}
    >
      <div className="container mx-auto">
        <div className="grid grid-cols-12 items-start" style={{ gap: 'var(--space-8)' }}>
          {/* Heading — 5 columns */}
          <div className="col-span-12 md:col-span-5">
            <SectionHeading
              style={{
                textAlign: 'left',
              }}
            >
              Your Hero Heading Here
            </SectionHeading>
          </div>

          {/* 2-column gap (empty space) */}

          {/* Support text — 5 columns, starting at column 8 */}
          <div className="col-span-12 md:col-span-5 md:col-start-8">
            <SectionSupportText
              style={{
                textAlign: 'left',
                marginTop: 0,
              }}
            >
              Your support text description here.
            </SectionSupportText>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### 4-2-6 Layout (Alternative)

```tsx
export function PageIntro() {
  return (
    <section
      className="w-full"
      style={{
        paddingTop: 'var(--space-8)',
        paddingBottom: 0,
        backgroundColor: 'var(--global-white)',
      }}
    >
      <div className="container mx-auto">
        <div className="grid grid-cols-12 items-start" style={{ gap: 'var(--space-8)' }}>
          {/* Heading — 4 columns */}
          <div className="col-span-12 md:col-span-4">
            <SectionHeading
              style={{
                textAlign: 'left',
              }}
            >
              Your Hero Heading Here
            </SectionHeading>
          </div>

          {/* 2-column gap (empty space) */}

          {/* Support text — 6 columns, starting at column 7 */}
          <div className="col-span-12 md:col-span-6 md:col-start-7">
            <SectionSupportText
              style={{
                textAlign: 'left',
                marginTop: 0,
              }}
            >
              Your support text description here.
            </SectionSupportText>
          </div>
        </div>
      </div>
    </section>
  );
}
```

---

## Implementations

All implementations use the **5-2-5 layout** and follow this pattern exactly. Only the heading and support text content varies per page.

| Page | Component | File | Heading | Layout |
|---|---|---|---|---|
| JioHome | `HomeIntro` | `/src/app/components/HomeIntro.tsx` | "JioHome, Jio more" | 5-2-5 |
| Mobile | `MobileIntro` | `/src/app/components/MobileIntro.tsx` | "Discover the best of mobile life" | 5-2-5 |
| Business | `BusinessTitle` | `/src/app/components/BusinessTitle.tsx` | "Transform how you work or do business" | 5-2-5 |
| Business | *(inline)* | `/src/app/pages/BusinessPage.tsx` | *(currently HomeIntro content)* | 5-2-5 |

### HomeIntro

**File:** `/src/app/components/HomeIntro.tsx`

- **Heading:** "JioHome, Jio more"
- **Support Text:** "Powered by JioAirFiber and JioFiber, JioHome is India's no.1 home entertainment & Wi-Fi service with 1,000+ TV channels, 12+ OTT apps, JioPC, gaming, and more."

```tsx
import { HomeIntro } from '../components/HomeIntro';
```

```tsx
<HomeIntro />
```

### MobileIntro

**File:** `/src/app/components/MobileIntro.tsx`

- **Heading:** "Discover the best of mobile life"
- **Support Text:** "With your Jio SIM, unlock unlimited mobile experiences on 5G and 4G networks, ensuring uninterrupted connectivity anytime, anywhere in India."

```tsx
import { MobileIntro } from '../components/MobileIntro';
```

```tsx
<MobileIntro />
```

### BusinessTitle

**File:** `/src/app/components/BusinessTitle.tsx`

- **Heading:** "Transform how you work or do business"
- **Support Text:** "From connectivity to cloud, JioBusiness delivers enterprise-grade solutions tailored for India."

```tsx
import { BusinessTitle } from '../components/BusinessTitle';
```

```tsx
<BusinessTitle />
```

---

## Key Principles

### 1. Column Spacing
- **Always maintain 2 columns of empty space** between heading and support text on desktop/tablet
- Use `col-start-*` to position support text correctly
- Examples:
  - 5-2-5: Support text starts at column 8 (`col-start-8`)
  - 4-2-6: Support text starts at column 7 (`col-start-7`)

### 2. Alignment
- Top-aligned grid (`items-start`)
- Left-aligned text within columns (override SectionHeading/SectionSupportText defaults)

### 3. Padding Strategy
- **Top padding only:** 32px (`var(--space-8)`)
- **No bottom padding:** Allows seamless flow to next section (usually a hero carousel)

### 4. Responsive Behavior
- Desktop/Tablet: Two-column layout with gap
- Mobile: Stacked full-width layout

---

## Differences from Standard Section Pattern

### Unique Specifications

1. **Custom Top Padding:** Uses `32px` instead of standard section padding (80px/48px/24px)
2. **No Bottom Padding:** Removes default section bottom padding
3. **2-Column Gap:** Maintains visual breathing room between heading and support text
4. **Top Alignment:** Uses `items-start` instead of standard `items-end` or centered layouts
5. **Left-Aligned Text:** Overrides default center alignment from SectionHeading/SectionSupportText
6. **Fixed Purpose:** Always used as first section after subheader/tabs

---

## Usage Guidelines

### When to Use

- **First section after subheader/tabs** on landing pages
- Provides concise page introduction
- Precedes hero carousel or similar visual content

### When NOT to Use

- Mid-page sections (use standard section pattern)
- Sections requiring center-aligned content
- Sections with complex multi-column layouts

---

## Related Components

- **SectionHeading:** Responsive heading component (`/src/app/components/SectionHeading.tsx`)
- **SectionSupportText:** Responsive support text component (`/src/app/components/SectionHeading.tsx`)

---

## Related Documentation

- **Section Specification:** `/guidelines/MD/Component/section.md`
- **Typography:** `/guidelines/MD/Foundation/typography.md`
- **Layout:** `/guidelines/MD/Foundation/layout.md`
- **Design Tokens:** `/src/styles/theme.css`

---

## Visual Example

```
Desktop/Tablet Grid (12 columns):
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|      Heading (5 cols)        |  Gap (2)  |   Support Text (5 cols)     |
+------------------------------+-----------+-----------------------------+

Mobile Grid (stacked):
+-----------------------------+
|    Heading (12 cols)        |
+-----------------------------+
|         Gap (32px)          |
+-----------------------------+
|  Support Text (12 cols)     |
+-----------------------------+
```

---

## Changelog

- **2026-02-23:** Initial `hero-intro.md` pattern specification created
- **2026-02-23:** `home-intro.md` created for JioHome intro (HomeIntro component)
- **2026-02-23:** `mobile-intro.md` created for Mobile intro (MobileIntro component)
- **2026-02-23:** Defined 5-2-5 and 4-2-6 layout options
- **2026-02-23:** Changed alignment from bottom (`items-end`) to top (`items-start`)
- **2026-02-23:** Updated padding: top 32px, bottom 0px
- **2026-02-23:** Standardized all implementations to 5-2-5 layout
- **2026-03-10:** Merged `hero-intro.md`, `home-intro.md`, and `mobile-intro.md` into unified `intro.md`
- **2026-03-10:** Added BusinessTitle as an implementation entry
