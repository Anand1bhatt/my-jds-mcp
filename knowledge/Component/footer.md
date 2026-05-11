# Footer — JDS Component Style Guide

## Overview

The footer is split into two distinct zones:

1. **Footer Container** (Upper section) — Multi-column link grid + right sidebar (social icons & app download badges)
2. **Bottom Bar** — Jio logo, copyright text, and legal links on a single row

All styling uses JDS design tokens exclusively. No hardcoded hex values.

---

## Footer Architecture

### Footer Container

The Footer Container consists of 5 sections with the following grid structure:

| Section | Columns | Content Type |
|---------|---------|--------------|
| **Section 1-4** | 2 columns each | Links with Headers |
| **Section 5** | 4 columns | Connect with us + Download the app |

**Spacing:**
- Top and bottom spacing: `var(--space-10)` (40px) — `$Spacing-XL`

**Background:**
- Color: `var(--grey-20)`

---

## Section 1-4: Link Columns

### Column Headers

| Property | Token | Value |
|----------|-------|-------|
| Text size | `var(--text-label)` | 14px — `$heading-xxs` |
| Color | `var(--grey-100)` | `#141414` |
| Font-family | `var(--font-family-jiotype)` | JioType |
| Font-weight | `var(--font-weight-bold)` | 700 |
| Line-height | 1.5 | — |
| Margin-bottom | `var(--space-5)` | 20px |

### Link Items

| Property | Token | Value |
|----------|-------|-------|
| Text size | `var(--text-footnote)` | 11px — `$body-xxs` |
| Color | `var(--grey-80)` | `rgba(0, 0, 0, 0.65)` |
| Hover color | `var(--global-black)` | `#141414` |
| Font-family | `var(--font-family-jiotype)` | JioType |
| Font-weight | `var(--font-weight-normal)` | 400 |
| Line-height | 1.5 | — |
| Gap | `var(--space-3)` | 12px between items |
| Text-decoration | none | — |
| Transition | color transition | — |

---

## Section 5: Connect & Download

### Part 1: Connect with Us

**Heading:**

| Property | Token | Value |
|----------|-------|-------|
| Text | "Connect with us" | — |
| Text size | `var(--text-label)` | 14px — `$heading-xxs` |
| Color | `var(--global-black)` | `#141414` |
| Font-family | `var(--font-family-jiotype)` | JioType |
| Font-weight | `var(--font-weight-bold)` | 700 |
| Margin-bottom | `var(--space-4)` | 16px |

**Social Media Icons:**

| Property | Token | Value |
|----------|-------|-------|
| Component | Button | — |
| Kind | Primary | — |
| Variant | Icon Only | — |
| Size | S | 36px × 36px |
| Icon Color | `var(--primary-inverse)` | `#FFFFFF` |
| Background | `var(--global-black)` | `#141414` |
| Border-radius | 50% | Circle |
| Icon size | 16px × 16px | — |
| Hover | opacity: 0.8 | — |

**Note:** User-defined icons for social links (X/Twitter, Instagram, Facebook, YouTube, Camera).

**Layout:**
- Social icons row: `flex gap-3 mb-6`
- Gap between icons: `var(--space-3)` (12px)

---

### Part 2: Download the App

**Heading:**

| Property | Token | Value |
|----------|-------|-------|
| Text | "Download the app" | — |
| Text size | `var(--text-label)` | 14px — `$heading-xxs` |
| Color | `var(--global-black)` | `#141414` |
| Font-family | `var(--font-family-jiotype)` | JioType |
| Font-weight | `var(--font-weight-bold)` | 700 |
| Margin-bottom | `var(--space-4)` | 16px |

**Google Play Store Badge:**

| Property | Value |
|----------|-------|
| Size | 132px × 40px |
| Badge asset | https://play.google.com/intl/en_us/badges/ |
| Border-radius | `var(--radius)` (8px) |
| Background | `var(--global-black)` |
| Hover | opacity: 0.8 |

**App Store Badge:**

| Property | Value |
|----------|-------|
| Size | 120px × 40px |
| Badge asset | https://developer.apple.com/app-store/marketing/guidelines/ |
| Border-radius | `var(--radius)` (8px) |
| Background | `var(--global-black)` |
| Hover | opacity: 0.8 |

**Layout:**
- Badges row: `flex gap-3`
- Gap between badges: `var(--space-3)` (12px)

---

## Bottom Bar

### Spacing

| Property | Token | Value |
|----------|-------|-------|
| Top spacing | `var(--space-4)` | 16px — `$Spacing-Base` |
| Bottom spacing | `var(--space-4)` | 16px — `$Spacing-Base` |
| Between content (logo, text, links) | `var(--space-4)` | 16px — `$Spacing-Base` |
| Between link and divider | `var(--space-3)` | 12px — `$spacing-xs` |

### Desktop

1. **Jio Logo**
   - Size: 32px x 32px

2. **Trademark text**
   - Text size: $body-xxs
   - Color: grey-80

3. **Regulatory Link**
   - Link text size: $body-xxs
   - Color: grey-80

4. **Press release Link**
   - Link text size: $body-xxs
   - Color: grey-80

5. **Policies Link**
   - Link text size: $body-xxs
   - Color: grey-80

6. **Term and Condition Link**
   - Link text size: $body-xxs
   - Color: grey-80

7. **Vertical Divider**
   - *Height is to container height

8. **Horizontal Divider**
   - *Width is to container width

### Mobile

1. **Jio Logo**
   - Align to column 1 of grid

2. **Trademark text**
   - Align to column 1-4 of grid

**Mobile Spacing:**
- Spacing above the Jio logo: `var(--space-6)` (24px) — `$Spacing-m`
- Spacing below the Jio logo: `var(--space-4)` (16px) — `$Spacing-base`
- Spacing below the Copyright Text: `var(--space-4)` (16px) — `$Spacing-base`
- Spacing below the links: `var(--space-6)` (24px) — `$Spacing-m`

### Background & Border

| Property   | Value                      |
| ---------- | -------------------------- |
| Background | `var(--grey-20)`           |
| Border-top | `1px solid var(--grey-40)` |
| Padding    | `px-6 md:px-10 py-4`       |

### Layout

```
flex flex-col md:flex-row items-start md:items-center gap-4
```

Three elements in a row on desktop, stacked on mobile:

1. **Jio Logo** — shrink-0, left-aligned
2. **Copyright Text** — flex-1, fills remaining space
3. **Legal Links** — shrink-0, right-aligned

### Jio Logo

| Property     | Value                                                      |
| ------------ | ---------------------------------------------------------- |
| Element      | `<img>` tag                                                |
| Image source | `figma:asset/deb19ac67ee66bf03daf6f16b1fd2ea7fe1422e8.png` |
| Alt text     | `Jio`                                                      |
| Height       | `32px`                                                     |
| Width        | `auto` (maintains aspect ratio)                            |

**Note:** The logo uses the blue Jio brand image (PNG) imported via the `figma:asset` virtual module scheme. This replaces the previous text-based logo with black background.

### Copyright Text

```
font-family:  var(--font-family-jiotype)
font-size:    11px
font-weight:  var(--font-weight-normal)  → 400
color:        var(--grey-80)
line-height:  1.5
```

Text: "Jio" trademark is owned by Reliance Industries Limited and licensed to its affiliates and subsidiaries. All rights to this website, including copyright in content represented thereat, vest in Reliance Industries Limited and/or its respective affiliates and subsidiaries. All rights reserved.

### Legal Links

| Property        | Value                             |
| --------------- | --------------------------------- |
| Layout          | `flex items-center gap-5`         |
| Font-family     | `var(--font-family-jiotype)`      |
| Font-size       | `11px`                            |
| Font-weight     | `var(--font-weight-medium)` (500) |
| Color           | `var(--grey-80)`                  |
| Hover color     | `var(--global-black)`             |
| White-space     | `nowrap`                          |
| Text-decoration | `none`                            |

Links: Press release, Regulatory, Policies, Terms & conditions

#### Vertical Dividers Between Links

Each link (except the last) is followed by a vertical divider:

| Property          | Value                          |
| ----------------- | ------------------------------ |
| Width             | `var(--border-width-thin)` (1px) |
| Height            | `16px`                         |
| Background color  | `var(--grey-40)`               |
| Margin left       | `var(--space-3)` (12px)        |
| Margin right      | `var(--space-3)` (12px)        |

---

## Responsive Behavior

| Breakpoint | Link Grid       | Sidebar                 | Bottom Bar                    |
| ---------- | --------------- | ----------------------- | ----------------------------- |
| Mobile     | 2 columns       | Below links, full width | Stacked (logo → text → links) |
| md+        | 6 columns (4+2) | Inline right            | Single row                    |

---

## Accessibility

- All links must be focusable and keyboard-accessible
- Social icon links should have `aria-label` for screen readers (currently relies on icon recognition)
- Legal links must have sufficient contrast (grey-80 on grey-20 meets WCAG AA for small text)
- Logo uses semantic text, not an image

---

## Design Token Mapping

For reference, here's how design system tokens map to CSS variables:

| Design Token | CSS Variable | Value | Usage |
|--------------|--------------|-------|-------|
| `$Spacing-XL` | `var(--space-10)` | 40px | Footer container top/bottom spacing |
| `$Spacing-Base` / `$Spacing-base` | `var(--space-4)` | 16px | Bottom bar spacing |
| `$spacing-xs` | `var(--space-3)` | 12px | Link-to-divider spacing |
| `$Spacing-m` | `var(--space-6)` | 24px | Mobile spacing (logo, links) |
| `$heading-xxs` | `var(--text-label)` | 14px | Section headers, headings |
| `$body-xxs` | `var(--text-footnote)` | 11px | Link items, bottom bar text |

**All spacing and typography values use CSS variables from `/src/styles/theme.css` to ensure consistency across the design system.**

---

## Usage Guidelines

1. **All colors** use JDS tokens — never hardcode hex values
2. **Font-family** must always be `var(--font-family-jiotype)`
3. **Font weights** use token references: `--font-weight-black`, `--font-weight-bold`, `--font-weight-medium`, `--font-weight-normal`
4. **Font sizes** use token references where available; use explicit `11px` only for the bottom bar fine print
5. **Border-radius** uses `var(--radius)` for badges/logo or `50%` for circular social icons
6. **Link hover** transitions to `var(--global-black)` from `var(--grey-80)`
7. **No shadows or elevation** on the footer — flat design only
8. **This footer layout must be followed exactly** on all pages

---

## Visual Structure

```
┌──────────────────────────────────────────────────────────────────────┐
│  FOOTER CONTAINER                                                    │
│  bg: var(--grey-20) | Top/Bottom spacing: var(--space-10) (40px)    │
│                                                                      │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐  │
│  │ Section 1   │ │ Section 2   │ │ Section 3   │ │ Section 4   │  │
│  │ (2 cols)    │ │ (2 cols)    │ │ (2 cols)    │ │ (2 cols)    │  │
│  │             │ │             │ │             │ │             │  │
│  │ HEADER      │ │ HEADER      │ │ HEADER      │ │ HEADER      │  │
│  │ (14px,      │ │ (14px,      │ │ (14px,      │ │ (14px,      │  │
│  │ grey-100)   │ │ grey-100)   │ │ grey-100)   │ │ grey-100)   │  │
│  │             │ │             │ │             │ │             │  │
│  │ • Link 1    │ │ • Link 1    │ │ • Link 1    │ │ • Link 1    │  │
│  │ • Link 2    │ │ • Link 2    │ │ • Link 2    │ │ • Link 2    │  │
│  │ • Link 3    │ │ • Link 3    │ │ • Link 3    │ │ • Link 3    │  │
│  │ (11px,      │ │ (11px,      │ │ (11px,      │ │ (11px,      │  │
│  │ grey-80)    │ │ grey-80)    │ │ grey-80)    │ │ grey-80)    │  │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │ Section 5 (4 cols)                                       │      │
│  │                                                          │      │
│  │ CONNECT WITH US (14px, global-black)                    │      │
│  │ [●][●][●][●][●] — Social icons (36×36px circles)        │      │
│  │                                                          │      │
│  │ DOWNLOAD THE APP (14px, global-black)                   │      │
│  │ [▶ Google Play 132×40] [🍎 App Store 120×40]           │      │
│  └──────────────────────────────────────────────────────────┘      │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│  BOTTOM BAR                                                          │
│  border-top: 1px solid var(--grey-40)                                │
│  Top/Bottom spacing: var(--space-4) (16px)                           │
│                                                                      │
│  [Jio Logo]  Copyright text (11px, grey-80)  Links (11px, grey-80)  │
│  32×32px     Spacing: var(--space-4)         With dividers          │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```