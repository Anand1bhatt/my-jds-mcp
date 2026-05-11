# Section Component Specification

## Overview

All `...Section` components follow a consistent 3-slot structure that provides flexibility for various content layouts while maintaining design system compliance.

## Structure

### Three-Slot System

All sections are composed of three optional slots:

1. **Top Slot** — Header content (logo, heading, support text, CTAs)
2. **Middle Slot** — Main content area (flexible grid layouts)
3. **Bottom Slot** — Footer content (support text, CTAs)

**Important:** All slots are optional and should be included based on requirements.

---

## Top Slot Specification

The top slot contains header content and is typically used for section titles, descriptions, and primary actions.

### Elements (All Optional)

1. **Product Logo with Brand Label**
   - Label Typography: `$body/L-Bold`
   - Label Color: `var(--primary-60)`

2. **Heading**
   - Desktop + Tablet: `$heading/M`
   - Mobile: `$heading/S`

3. **Support Text**
   - Desktop + Tablet: `$body/M`
   - Mobile: `$body/S`

4. **Button Group**
   - Primary Button + Secondary Button (optional)

5. **Tertiary Button**
   - Standalone tertiary action (optional)

### Top Slot Spacing

**Desktop:**
- 24px spacing between all elements (product logo, label, heading, button group, tertiary button)
- **Exception:** Heading & Support Text spacing = 12px

**Tablet:**
- 24px spacing between all elements (product logo, label, heading, button group, tertiary button)
- **Exception:** Heading & Support Text spacing = 12px

**Mobile:**
- 16px spacing between all elements (product logo, label, heading, button group, tertiary button)
- **Exception:** Heading & Support Text spacing = 8px

---

## Middle Slot Specification

The middle slot contains the main content area with responsive grid layouts.

### Grid Column Layouts

| Layout Type | Desktop | Tablet | Mobile |
|------------|---------|--------|--------|
| **Full Width** | 12 Column | 6 Column | 4 Column |
| **Half Width** | 6 Column | 6 Column | 4 Column |
| **Third Width** | 4 Column | 3 Column | 3 Column with carousel |
| **Quarter Width** | 3 Column | 3 Column | 3 Column with carousel |
| **Sixth Width** | 2 Column | 3 Column | 3 Column with carousel |

**Note:** On mobile, layouts with 3+ columns should use a carousel pattern to maintain usability.

### Implementation

- Middle slot is a **placeholder** that accepts any content component
- Grid layouts must use CSS variables for column definitions
- Ensure proper responsive behavior across all breakpoints

---

## Bottom Slot Specification

The bottom slot contains footer content and is typically used for additional context or secondary actions.

### Elements (All Optional)

1. **Support Text**
   - Desktop + Tablet: `$body/M`
   - Mobile: `$body/S`

2. **Button Group**
   - Primary Button + Secondary Button (optional)

3. **Tertiary Button**
   - Standalone tertiary action (optional)

### Bottom Slot Spacing

- Same spacing rules as Top Slot apply

---

## Section-Level Spacing

### Desktop (992px+)

**Top Spacing (entire section):**
- Default: `80px` (`var(--space-20)`)
- After Carousel Section: `40px` (`var(--space-10)`)

**Bottom Spacing (entire section):**
- `40px` (`var(--space-10)`)

**Slot Spacing:**
- `40px` between all 3 slots (top, middle, bottom) (`var(--space-10)`)

### Tablet (620px - 991px)

**Top Spacing (entire section):**
- Default: `48px` (`var(--space-12)`)
- After Carousel Section: `24px` (`var(--space-6)`)

**Bottom Spacing (entire section):**
- `24px` (`var(--space-6)`)

**Slot Spacing:**
- `24px` between all 3 slots (top, middle, bottom) (`var(--space-6)`)

### Mobile (< 620px)

**Top Spacing (entire section):**
- Default: `24px` (`var(--space-6)`)
- After Carousel Section: `12px` (`var(--space-3)`)

**Bottom Spacing (entire section):**
- `24px` (`var(--space-6)`)

**Slot Spacing:**
- `24px` between all 3 slots (top, middle, bottom) (`var(--space-6)`)

---

## Section Variants

### Standard Section

The default section variant uses the three-slot system above with a white or alternating background (`var(--global-white)` / `var(--primary-20)`).

---

### Guidance Section (Master Component Variant)

The **Guidance** section is a specialized master component variant designed to provide users with quick access to support and assistance. It features a prominent call-to-action area with multiple contact methods, placed **above the Footer** on all pages.

#### Component Location

- **File**: `/src/app/components/Guidance.tsx`
- **Type**: Master/Reusable Component
- **Placement**: Above Footer on all pages

#### Usage

Currently implemented on:
- Desktop Page (`/`)
- Mobile Page (`/mobile`)

Can be added to other pages as needed.

```tsx
import { Guidance } from '../components/Guidance';

// In your page component
<main>
  {/* Other sections */}
  <Guidance />
</main>
<Footer />
```

#### Layout Structure

```
┌─────────────────────────────────────────────────────┐
│                 Primary-50 Background                │
│                                                       │
│              Need Guidance (Responsive)               │
│              We're here to help you.                  │
│                                                       │
│   [Support] [Chat with us] [Call us] [Find a store]  │
│   (Full-width on mobile, auto-width on desktop)      │
│                                                       │
└─────────────────────────────────────────────────────┘
```

#### Guidance Typography

| Element | Token (Mobile) | Token (Tablet/Desktop) | Mobile Value | Tablet/Desktop Value | Color |
|---------|----------------|------------------------|--------------|----------------------|-------|
| Heading | `--text-heading-m` | `--text-heading-l` | 40px | 64px | `--global-white` |
| Body Text | `--text-body-s` | `--text-body-m` | 16px | 18px | `--global-white` (90% opacity) |
| Font Family | `--font-family-jiotype` | `--font-family-jiotype` | JioType | JioType | - |
| Heading Weight | `--font-weight-black` | `--font-weight-black` | 900 | 900 | - |
| Body Weight | `--font-weight-medium` | `--font-weight-medium` | 500 | 500 | - |

#### Guidance Colors

| Element | Token | Value |
|---------|-------|-------|
| Background | `--primary-50` | #0F3CC9 |
| Text | `--global-white` | #FFFFFF |
| Body Text Opacity | - | 0.9 |

#### Guidance Spacing

| Element | Token | Value |
|---------|-------|-------|
| Section Padding Top | `--section-padding-top` | 80px |
| Section Padding Bottom | `--section-padding-bottom` | 40px |
| Heading to Body | `--space-3` | 12px |
| Body to Buttons | `--space-8` | 32px |
| Button Gap | `--space-4` | 16px |

#### Guidance Buttons

- **Variant**: `secondaryInverse`
- **Count**: 4 CTAs
- **Layout**: 
  - Mobile: Full width, stacked vertically with 16px gap (`--space-4`)
  - Desktop: Auto width, flex wrap, horizontal with 16px gap (`--space-4`)
- **Icons**: 20px x 20px (w-5 h-5)

| Button | Icon | Source | Label |
|--------|------|--------|-------|
| Support | `IcSupport` | `@jds/extended-icons` | Support |
| Chat | `IcChat` | `@jds/extended-icons` | Chat with us |
| Call | `IcCall` | `@jds/extended-icons` | Call us |
| Store | `IcLocation` | `@jds/core-icons` | Find a store |

#### Guidance Responsive Behavior

**Mobile (< 768px):**
- Title: Heading M — `var(--text-heading-m)` = 40px
- Description: Body S — `var(--text-body-s)` = 16px
- Buttons: Full width (100%), stacked vertically
- Button Gap: `var(--space-4)` = 16px
- Container Padding: 16px horizontal (`--container-padding-mobile`)
- Alignment: Centered

**Tablet (768px - 991px):**
- Title: Heading L — `var(--text-heading-l)` = 64px
- Description: Body M — `var(--text-body-m)` = 18px
- Buttons: Auto width, flex wrap, horizontal
- Button Gap: `var(--space-4)` = 16px
- Container Padding: 40px horizontal (`--container-padding-desktop`)
- Alignment: Centered
- Buttons may wrap to multiple rows if needed

**Desktop (992px+):**
- Title: Heading L — `var(--text-heading-l)` = 64px
- Description: Body M — `var(--text-body-m)` = 18px
- Buttons: Auto width, flex wrap, horizontal
- Button Gap: `var(--space-4)` = 16px
- Container Padding: 40px horizontal (`--container-padding-desktop`)
- Alignment: Centered

**L/XL (992px+):**
- Container max-width: 1184px
- Horizontal padding: 0px (relies on container max-width)
- Buttons typically fit in 1-2 rows

#### Guidance Visual Consistency

This component follows the same visual pattern as:
- `ILLGuidance.tsx` (Internet Leased Line page)
- `BusinessGuidance.tsx` (Business page)

Key differences:
- **Heading Size**: Mobile uses Heading M (40px); Desktop uses Heading L (64px) — larger than ILLGuidance
- **Button Count**: 4 CTAs vs 3 CTAs in ILLGuidance
- **Button Layout**: Full-width on mobile, auto-width on desktop
- **Description Size**: Responsive (16px mobile, 18px desktop)
- **Background**: Primary-50 (consistent across all guidance variants)
- **Subtitle Text**: "We're here to help you." (generic, reusable across pages)

#### Guidance Customization

To customize for specific pages, create a page-specific variant component (e.g., `BusinessGuidance.tsx`) that:
- Uses different subtitle text
- Adjusts button labels or actions
- Maintains the same visual structure and design tokens
- Follows the same responsive behavior patterns

#### Adding Guidance to New Pages

1. Import the component: `import { Guidance } from '../components/Guidance';`
2. Place above the Footer component in your page layout
3. Ensure it's within the `<main>` tag
4. No props required — works out of the box
5. Responsive behavior is automatic

#### Guidance Related Components

- `/src/app/components/ILLGuidance.tsx` — ILL-specific guidance
- `/src/app/components/BusinessGuidance.tsx` — Business-specific guidance
- `/src/app/components/Footer.tsx` — Footer (placed after Guidance)
- `/src/app/components/ui/button.tsx` — Button component with variants

---

## Design System Compliance

### Typography

- **All typography must use JioType font faces** defined in `/src/styles/fonts.css`
- Typography tokens: `$heading/M`, `$heading/S`, `$body/L-Bold`, `$body/M`, `$body/S`
- Map to CSS variables: `var(--text-heading-m)`, `var(--text-heading-s)`, `var(--text-body-l)`, `var(--text-body-m)`, `var(--text-body-s)`

### Colors

- **All colors must use CSS variables** from `/src/styles/theme.css`
- Primary: `var(--primary-60)`, `var(--primary-50)`, etc.
- Ensure colors can be updated globally via CSS

### Spacing

- **All spacing must use CSS variables** from `/src/styles/theme.css`
- Space scale: `var(--space-3)` (12px), `var(--space-6)` (24px), `var(--space-10)` (40px), etc.
- **No arbitrary values** — only design system tokens

### Borders & Radius

- **All borders and radii must use CSS variables**
- Border: `var(--border-width-medium)`, etc.
- Radius: `var(--radius-button)`, `var(--radius-card)`, etc.

---

## Grid System Compliance

- **Container**: Uses standard `.container` class
- **Max Width**: 1184px (L/XL breakpoints)
- **Padding**:
  - Mobile: 16px (`--container-padding-mobile`)
  - Desktop: 40px (`--container-padding-desktop`)
  - L/XL (992px+): 0px horizontal padding

---

## Accessibility

- Semantic `<section>` element
- Heading hierarchy: Uses `<h2>` for section title
- Button labels clearly describe actions
- Icons use `fill="currentColor"` for proper color inheritance
- High contrast ratios maintained (minimum AA)
- Touch-friendly on mobile: Full-width buttons with adequate spacing

---

## Responsive Breakpoints

Sections must adapt across three breakpoints:

- **Desktop:** 992px and above
- **Tablet:** 620px - 991px
- **Mobile:** Below 620px

Use Tailwind CSS breakpoint utilities or CSS media queries:
- Desktop: `lg:`
- Tablet: `md:` to `lg:`
- Mobile: Default (no prefix) to `md:`

---

## Implementation Guidelines

### Required Patterns

1. **Slot Rendering:** Only render slots that have content
2. **Spacing Variables:** Use CSS custom properties for all spacing
3. **Typography Classes:** Use predefined CSS classes for typography (not inline styles)
4. **Grid System:** Use Tailwind grid utilities with design system constraints
5. **Carousel Detection:** Implement logic to detect if previous section is a carousel (for top spacing adjustment)

### Example Structure

```tsx
<section
  className="w-full"
  style={{
    paddingTop: 'var(--section-padding-top)',
    paddingBottom: 'var(--section-padding-bottom)',
    backgroundColor: 'var(--global-white)',
  }}
>
  <div className="container mx-auto">
    {/* Top Slot */}
    {hasTopContent && (
      <div style={{ marginBottom: 'var(--space-10)' }}>
        {/* Logo, Heading, Support Text, Buttons */}
      </div>
    )}

    {/* Middle Slot */}
    {hasMiddleContent && (
      <div style={{ marginBottom: 'var(--space-10)' }}>
        {/* Grid Content */}
      </div>
    )}

    {/* Bottom Slot */}
    {hasBottomContent && (
      <div>
        {/* Support Text, Buttons */}
      </div>
    )}
  </div>
</section>
```

---

## Design System Compliance Checklist

- [x] Uses JDS design tokens exclusively
- [x] Follows 4px spacing system
- [x] Uses JioType font family
- [x] Implements proper grid system
- [x] Uses official JDS icons (where applicable)
- [x] Follows section padding structure
- [x] Maintains semantic HTML
- [x] Responsive across all breakpoints
- [x] Mobile-first responsive typography
- [x] Accessible markup and contrast
- [x] No arbitrary/hardcoded values — only CSS variable tokens

---

## Related Documentation

- **Typography:** `/guidelines/MD/Foundation/typography.md`
- **Layout:** `/guidelines/MD/Foundation/layout.md`
- **Cards:** `/guidelines/MD/Component/card.md`
- **Buttons:** `/guidelines/MD/Component/button.md`
- **Design Tokens:** `/src/styles/theme.css`

---

## Changelog

- **2026-02-19:** Initial specification created for Section component structure
- **2026-02-27:** Merged Guidance Section variant into Section specification; `guidance-section.md` deprecated and removed

---
