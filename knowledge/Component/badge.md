# Badge — JDS Component Style Guide

## Overview

Badges are **non-interactive visual indicators** used to communicate status, highlight information, or grab attention. They are divided into five functional categories based on their purpose and behavior.

The component lives in `/src/app/components/ui/badge.tsx` and exports both `Badge` and `badgeVariants`.

All styling uses JDS design tokens from `/src/styles/theme.css`.
Typography uses JioType exclusively per typography.md.
Icons use `fill="currentColor"` per icon.md.

---

## Functional Categories

| Category       | Primary Usage                | Logic Constraints                                                                 |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------- |
| Notification   | Temporary attention          | Use Dot for general activity; Numbers for specific counts (Max 99+)              |
| Status         | State representation         | Mostly uses Semantic Colors (Red, Green, Orange). Can be Dot, Icon, or Text      |
| Informational  | Categorization/USPs          | Clubbed with other elements or independent. Uses text or icon in containers      |
| Brand          | Logo association             | Strictly for Brand/Service identity. Not for general icons                       |
| Promo          | Marketing/CTR                | Variable shapes; more aggressive visual differentiation than Informational badges |

---

## Typography Rules (MANDATORY)

> **ALL text in Badge components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (Badges)

| Token                  | Value | Usage                            |
| ---------------------- | ----- | -------------------------------- |
| `--font-weight-medium` | 500   | All badge text (all sizes)       |

- Badges always use `var(--font-weight-medium)` (500).
- **Never** use arbitrary `font-weight` numbers or Tailwind font-weight utilities.

### Permitted Sizes

**Notification & Status Badges:**

| Token          | Value | Usage                          |
| -------------- | ----- | ------------------------------ |
| `--text-base`  | 16px  | 4XL size badges (body-l-bold)  |
| `--text-small` | 14px  | 3XL size badges (body-s-bold)  |
| `--text-tiny`  | 12px  | 2XL, XL size badges (body-xs-bold) |
| `--text-micro` | 10px  | L, M size badges (body-xxs-bold) |

**Informational Badges:**

| Token          | Value | Usage                          |
| -------------- | ----- | ------------------------------ |
| `--text-base`  | 16px  | **ALL sizes** (body-l-bold)    |

- **Important**: All informational badge labels use `var(--text-base)` (16px) regardless of badge size.
- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Anatomy & Variants

### Shape & Content Priority

- **Circle/Dot**: Used for simple status or notification triggers
- **Rectangle (Variable Radii)**: Used for text-heavy badges (Status/Info/Brand)
- **Irregular**: Reserved for Promo badges
- **Content Priority**: Icon | Text | Number | Image | Dot

### Numeric Logic (Notification)

- **Single/Double**: Shows actual count (e.g., `01`, `15`)
- **Multiple (99+)**: Mandatory "+" symbol for counts over 99
- **Never** use "K" for 100s (e.g., never use "1K" — use "99+")

---

## Placement & Elevation Logic

The system automatically determines elevation based on the badge's relationship with its parent element.

| Placement Type | Position                                                           | Elevation                |
| -------------- | ------------------------------------------------------------------ | ------------------------ |
| **Overlay**    | Top-right / Bottom-right corner of parent (e.g., Avatar, Button)  | +1 from parent           |
| **Inline**     | Inline right / Inline left of parent content (e.g., List item, Tabs) | 0 (Same as parent)    |
| **Independent** | Dependent only on context (e.g., Banner, Card section)            | 0 / Context Dependent    |

---

## Accessibility (A11y)

### Contrast

- **Minimum contrast ratio**: 4.5:1 for label and container colors
- **Semantic colors**: Always use 100% opacity for semantic status colors to ensure visibility
- **Note**: Though not all color accessibility tests pass for error-50, warning-50, and success-50 versions, they present good semantic recognition to end users. Once new color tokens are available, these will be updated.

### Alt-Text Pattern

```tsx
{/* Notification */}
<Badge aria-label="Active notification 5">5</Badge>

{/* Status */}
<Badge aria-label="Status Active">Active</Badge>

{/* Informational */}
<Badge aria-label="Badge Trending">Trending</Badge>
```

---

# Badge: Notification

Temporary indicators for new activity (vanishes after reading).

## Variants

1. **Dot Badge**
2. **Single/Double Number Badge**
3. **Multiple Number + Symbol Badge**

---

## 1. Dot Badge

Simple circular indicator without text.

### Sizes

| Size | Container | Stroke (Optional) |
| ---- | --------- | ----------------- |
| 4XL  | 40px      | 1px (Outside)     |
| 3XL  | 32px      | 1px (Outside)     |
| 2XL  | 28px      | 1px (Outside)     |
| XL   | 24px      | 1px (Outside)     |
| L    | 20px      | 1px (Outside)     |
| M    | 16px      | 1px (Outside)     |
| S    | 12px      | 1px (Outside)     |
| XS   | 8px       | 1px (Outside)     |

### Colors

```
Background:     var(--error-50)           → #FA2F40
Stroke:         var(--primary-background) → #FFFFFF (optional)
```

### Border Radius

```
All sizes:      Pill (rounded-full)       → 9999px
```

### Usage

```tsx
<Badge category="notification" variant="dot" size="m" hasStroke />
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

- Top-right corner of parent element (Avatar, Button, etc.)
- Inline right of parent element (List item, Tabs, etc.)

---

## 2. Single/Double Number Badge

Circular badge showing 1-2 digit counts.

### Sizes

| Size | Container | Radius | Stroke (Optional) | Typography            |
| ---- | --------- | ------ | ----------------- | --------------------- |
| 4XL  | 40px      | Pill   | 1px (Outside)     | body-m-medium (16px)    |
| 3XL  | 32px      | Pill   | 1px (Outside)     | body-s-medium (14px)    |
| 2XL  | 28px      | Pill   | 1px (Outside)     | body-xs-medium (12px)   |
| XL   | 24px      | Pill   | 1px (Outside)     | body-xs-medium (12px)   |
| L    | 20px      | Pill   | 1px (Outside)     | body-xxs-medium (10px)  |
| M    | 16px      | Pill   | 1px (Outside)     | body-xxs-medium (10px)  |

### Colors

```
Background:     var(--error-50)           → #FA2F40
Stroke:         var(--primary-background) → #FFFFFF (optional)
Label:          var(--global-white)       → #FFFFFF
```

### Border Radius

```
All sizes:      Pill (rounded-full)       → 9999px
```

### Usage

```tsx
<Badge category="notification" variant="number" size="l" hasStroke>
  5
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

- Top-right corner of parent element (Avatar, Button, etc.)
- Inline right of parent element (List item, Tabs, etc.)

---

## 3. Multiple Number + Symbol Badge

Rectangle badge for counts over 99 (shows "99+").

### Sizes

| Size | Container | Radius | Stroke (Optional) | Typography            |
| ---- | --------- | ------ | ----------------- | --------------------- |
| 4XL  | 40px      | 8px    | 1px (Outside)     | body-m-bold (16px)    |
| 3XL  | 32px      | 8px    | 1px (Outside)     | body-s-bold (14px)    |
| 2XL  | 28px      | 8px    | 1px (Outside)     | body-xs-bold (12px)   |
| XL   | 24px      | 4px    | 1px (Outside)     | body-xs-bold (12px)   |
| L    | 20px      | 4px    | 1px (Outside)     | body-xxs-bold (10px)  |
| M    | 16px      | 4px    | 1px (Outside)     | body-xxs-bold (10px)  |

### Colors

```
Background:     var(--error-50)           → #FA2F40
Stroke:         var(--primary-background) → #FFFFFF (optional)
Label & "+":    var(--global-white)       → #FFFFFF
```

### Border Radius

```
4XL, 3XL, 2XL:  8px
XL, L, M:       4px
```

### Usage

```tsx
<Badge category="notification" variant="numberPlus" size="m" hasStroke>
  99+
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

- Top-right corner of parent element (Avatar, Button, etc.)
- Inline right of parent element (List item, Tabs, etc.)

---

# Badge: Status

Permanent indicators representing a state (e.g., Online, Cancelled).

## Variants

1. **Dot Only Badge**
2. **Icon Only Badge**
3. **Text Only Badge**
4. **Dot + Text Badge**
5. **Icon + Text Badge**
6. **Text in Container Badge**
7. **Dot + Text in Container Badge**
8. **Icon + Text in Container Badge**

---

## 1. Dot Only Badge

Same sizing as Notification Dot Badge (8px–40px).

### Colors (Without Container)

```
Dot:            var(--success-50) | var(--error-50) | var(--warning-50) | var(--grey-40)
Stroke:         var(--primary-background) → #FFFFFF (optional)
```

### Usage

```tsx
<Badge category="status" variant="dotOnly" size="m" colorScheme="success" hasStroke />
```

### Placement

- Top and bottom right corner of parent element (Avatar)

---

## 2. Icon Only Badge

Circular icon badge without text.

### Sizes

| Size | Container | Radius | Stroke (Optional) | Icon Size |
| ---- | --------- | ------ | ----------------- | --------- |
| 4XL  | 40px      | Pill   | 1px (Outline)     | 40px      |
| 3XL  | 32px      | Pill   | 1px (Outline)     | 32px      |
| 2XL  | 28px      | Pill   | 1px (Outline)     | 28px      |
| XL   | 24px      | Pill   | 1px (Outline)     | 24px      |
| L    | 20px      | Pill   | 1px (Outline)     | 20px      |
| M    | 16px      | Pill   | 1px (Outline)     | 16px      |
| S    | 12px      | Pill   | 1px (Outline)     | 12px      |
| XS   | 8px       | Pill   | 1px (Outline)     | 8px       |

### Colors

```
Icon:           var(--success-50) | var(--error-50) | var(--warning-50) | var(--grey-40)
Stroke:         var(--primary-background) → #FFFFFF (optional)
```

### Usage

```tsx
<Badge category="status" variant="iconOnly" size="l" colorScheme="success" hasStroke>
  <IcCheckCircle fill="currentColor" />
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

- Top and bottom right corner of parent element (Avatar)

---

## 3. Text Only Badge

Text without container.

### Sizes

| Size | Container Height | Typography            |
| ---- | ---------------- | --------------------- |
| 4XL  | 40px             | body-l-bold (16px)    |
| 3XL  | 32px             | body-s-bold (14px)    |
| 2XL  | 28px             | body-xs-bold (12px)   |
| XL   | 24px             | body-xs-bold (12px)   |
| L    | 20px             | body-xxs-bold (10px)  |
| M    | 16px             | body-xxs-bold (10px)  |

### Colors

```
Label:          var(--success-50) | var(--error-50) | var(--warning-50) | var(--grey-40)
```

---

## 4. Icon + Text Badge

Icon and text without container.

### Sizes

| Size | Container Height | Icon Size | Typography            |
| ---- | ---------------- | --------- | --------------------- |
| 4XL  | 40px             | 28px      | body-l-bold (16px)    |
| 3XL  | 32px             | 20px      | body-s-bold (14px)    |
| 2XL  | 28px             | 16px      | body-xs-bold (12px)   |
| XL   | 24px             | 16px      | body-xs-bold (12px)   |
| L    | 20px             | 16px      | body-xxs-bold (10px)  |
| M    | 16px             | 12px      | body-xxs-bold (10px)  |

---

## 5. Text in Container Badge

Text-only badge with background container.

### Sizes

| Size | Container Height | Radius | Stroke (Optional) | Padding (L/R × T/B) | Typography            |
| ---- | ---------------- | ------ | ----------------- | ------------------- | --------------------- |
| 4XL  | 40px             | 8px    | 4px (Outside)     | 8px × 4px           | body-l-bold (16px)    |
| 3XL  | 32px             | 8px    | 3px (Outside)     | 8px × 4px           | body-s-bold (14px)    |
| 2XL  | 28px             | 4px    | 3px (Outside)     | 8px × 4px           | body-xs-bold (12px)   |
| XL   | 24px             | 4px    | 3px (Outside)     | 4px × 2px           | body-xs-bold (12px)   |
| L    | 20px             | 4px    | 3px (Outside)     | 4px × 2px           | body-xxs-bold (10px)  |
| M    | 16px             | 4px    | 2px (Outside)     | 4px × —             | body-xxs-bold (10px)  |

### Colors

**Emphasis: Bold**

```
Success:
  Background:   var(--success-50)         → #0FA654
  Label:        var(--global-white)       → #FFFFFF
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Error:
  Background:   var(--error-50)           → #FA2F40
  Label:        var(--global-white)       → #FFFFFF
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Warning:
  Background:   var(--warning-50)         → #FF9500
  Label:        var(--global-white)       → #FFFFFF
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Neutral:
  Background:   var(--grey-40)            → #E5E5E5
  Label:        var(--grey-60)            → #B5B5B5
  Stroke:       var(--primary-background) → #FFFFFF (optional)
```

**Emphasis: Subtle**

```
Success:
  Background:   var(--success-20)         → #E8F9F0
  Label:        var(--success-50)         → #0FA654
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Error:
  Background:   var(--error-20)           → #FFEBEE
  Label:        var(--error-50)           → #FA2F40
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Warning:
  Background:   var(--warning-20)         → #FFF4E5
  Label:        var(--warning-50)         → #FF9500
  Stroke:       var(--primary-background) → #FFFFFF (optional)

Neutral:
  Background:   var(--grey-20)            → #F5F5F5
  Label:        var(--grey-60)            → #B5B5B5
  Stroke:       var(--primary-background) → #FFFFFF (optional)
```

### Usage

```tsx
{/* Bold emphasis */}
<Badge category="status" variant="textContainer" size="m" colorScheme="success" emphasis="bold" hasStroke>
  Active
</Badge>

{/* Subtle emphasis */}
<Badge category="status" variant="textContainer" size="m" colorScheme="error" emphasis="subtle">
  Cancelled
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

- Top and bottom right corner of parent element
- Inline right and left of parent element (List item, Tabs, etc.)

---

## 6. Icon + Text in Container Badge

Icon and text badge with background container.

### Sizes

| Size | Container Height | Radius | Icon Size | Padding (L/R × T/B) | Typography            |
| ---- | ---------------- | ------ | --------- | ------------------- | --------------------- |
| 4XL  | 40px             | 8px    | 28px      | 8px × 4px           | body-l-bold (16px)    |
| 3XL  | 32px             | 8px    | 20px      | 8px × 4px           | body-s-bold (14px)    |
| 2XL  | 28px             | 4px    | 16px      | 8px × 4px           | body-xs-bold (12px)   |
| XL   | 24px             | 4px    | 16px      | 4px × 2px           | body-xs-bold (12px)   |
| L    | 20px             | 4px    | 16px      | 4px × 2px           | body-xxs-bold (10px)  |
| M    | 16px             | 4px    | 12px      | 4px × —             | body-xxs-bold (10px)  |

### Colors

Same as Text in Container Badge (Bold/Subtle emphasis).

### Usage

```tsx
<Badge category="status" variant="iconTextContainer" size="l" colorScheme="success" emphasis="bold">
  <IcCheckCircle fill="currentColor" />
  Online
</Badge>
```

---

# Badge: Informational

Categorical labeling or USPs (e.g., "Trending", "Gold Member").

## Variants

1. **Icon Only (No Container)**
2. **Icon Only (Circle Container)**
3. **Icon Only (Square Container)**
4. **Label Only (With Container)**
5. **Icon + Label (With Container)**
6. **Image + Label (With Container)**

---

## 1. Icon Only (No Container / Transparent Container)

Icon without background.

### Sizes

| Size | Container | Radius | Stroke (Optional) | Icon Size |
| ---- | --------- | ------ | ----------------- | --------- |
| 4XL  | 40px      | Pill   | 1px (Outline)     | 40px      |
| 3XL  | 32px      | Pill   | 1px (Outline)     | 32px      |
| 2XL  | 28px      | Pill   | 1px (Outline)     | 28px      |
| XL   | 24px      | Pill   | 1px (Outline)     | 24px      |
| L    | 20px      | Pill   | 1px (Outline)     | 20px      |
| M    | 16px      | Pill   | 1px (Outline)     | 16px      |
| S    | 12px      | Pill   | 1px (Outline)     | 12px      |
| XS   | 8px       | Pill   | 1px (Outline)     | 8px       |

### Colors

```
Icon (only):    var(--sparkle-60) | var(--secondary-60) | var(--success-50) | var(--error-50) | var(--warning-50) | var(--grey-80)
```

### Placement

**Elevation: +1 from parent element**
- Bottom: Right, Left, Centre
- Top: Right, Left, Centre
- Right: Center
- Left: Center

---

## 2. Icon Only (Circle Container)

Icon inside a circular background.

### Sizes

| Size | Container | Radius | Stroke (Optional) | Icon Size |
| ---- | --------- | ------ | ----------------- | --------- |
| 4XL  | 40px      | Pill   | 1px (Outline)     | 24px      |
| 3XL  | 32px      | Pill   | 1px (Outline)     | 20px      |
| 2XL  | 28px      | Pill   | 1px (Outline)     | 16px      |
| XL   | 24px      | Pill   | 1px (Outline)     | 16px      |
| L    | 20px      | Pill   | 1px (Outline)     | 12px      |
| M    | 16px      | Pill   | 1px (Outline)     | 10px      |
| S    | 12px      | Pill   | 1px (Outline)     | 8px       |

### Colors

**Default (Sparkle) — Bold:**

```
Background:     var(--sparkle-60)         → #9932FF
Icon:           var(--primary-background) → #FFFFFF
```

**Default (Sparkle) — Subtle:**

```
Background:     var(--sparkle-20)         → #F3E5FF
Icon:           var(--sparkle-60)         → #9932FF
```

**Other Color Schemes:**

- **Secondary**: Bold `--secondary-60` / Subtle `--secondary-20` + `--secondary-60`
- **Neutral**: Bold `--grey-80` / Subtle `--grey-20` + `--grey-80`
- **Positive**: Bold `--success-50` / Subtle `--success-20` + `--success-50`
- **Negative**: Bold `--error-50` / Subtle `--error-20` + `--error-50`
- **Warning**: Bold `--warning-50` / Subtle `--warning-20` + `--warning-50`

### Usage

```tsx
<Badge category="informational" variant="iconCircle" size="m" colorScheme="sparkle" emphasis="bold">
  <IcStar fill="currentColor" />
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

**Elevation: +1 from parent element**
- Bottom: Right, Left, Centre
- Top: Right, Left, Centre
- Right: Center
- Left: Center

---

## 3. Icon Only (Square Container)

Icon inside a square/rounded rectangle background.

### Sizes

| Size | Container | Radius | Stroke (Optional) | Icon Size |
| ---- | --------- | ------ | ----------------- | --------- |
| 4XL  | 40px      | 8px    | 1px (Outline)     | 24px      |
| 3XL  | 32px      | 8px    | 1px (Outline)     | 20px      |
| 2XL  | 28px      | 4px    | 1px (Outline)     | 16px      |
| XL   | 24px      | 4px    | 1px (Outline)     | 16px      |
| L    | 20px      | 4px    | 1px (Outline)     | 12px      |
| M    | 16px      | 4px    | 1px (Outline)     | 10px      |
| S    | 12px      | 2px    | 1px (Outline)     | 8px       |

### Colors

Same as Icon Circle variant.

### Usage

```tsx
<Badge category="informational" variant="iconSquare" size="l" colorScheme="secondary" emphasis="subtle">
  <IcTrending fill="currentColor" />
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

---

## 4. Label Only (With Container)

Text-only informational badge with background.

### Sizes

| Size | Container Height | Radius | Stroke (Optional) | Padding (L/R × T/B) | Typography            |
| ---- | ---------------- | ------ | ----------------- | ------------------- | --------------------- |
| 4XL  | 40px             | 8px    | 4px (Outside)     | 8px × 4px           | body-l-bold (16px)    |
| 3XL  | 32px             | 8px    | 3px (Outside)     | 8px × 4px           | body-s-bold (14px)    |
| 2XL  | 28px             | 4px    | 3px (Outside)     | 8px × 4px           | body-xs-bold (12px)   |
| XL   | 24px             | 4px    | 3px (Outside)     | 4px × 2px           | body-xs-bold (12px)   |
| L    | 20px             | 4px    | 3px (Outside)     | 4px × 2px           | body-xxs-bold (10px)  |
| M    | 16px             | 4px    | 2px (Outside)     | 4px × —             | body-xxs-bold (10px)  |


**Important:** All informational badge labels use `body-l-bold` (16px, `var(--text-base)`) regardless of badge size.

### Colors

**Default (Sparkle) — Bold:**

```
Background:     var(--sparkle-60)         → #9932FF
Label:          var(--primary-background) → #FFFFFF
```

**Default (Sparkle) — Subtle:**

```
Background:     var(--sparkle-20)         → #F3E5FF
Label:          var(--sparkle-60)         → #9932FF
```

**Other Color Schemes:**

- **Secondary**: Bold `--secondary-60` bg + `--secondary-background` text / Subtle `--secondary-20` bg + `--secondary-60` text
- **Neutral**: Bold `--grey-80` bg + `--primary-background` text / Subtle `--grey-20` bg + `--grey-80` text
- **Positive**: Bold `--success-50` bg + `--primary-background` text / Subtle `--success-20` bg + `--success-50` text
- **Negative**: Bold `--error-50` bg + `--primary-background` text / Subtle `--error-20` bg + `--error-50` text
- **Warning**: Bold `--warning-50` bg + `--primary-background` text / Subtle `--warning-20` bg + `--warning-50` text

### Usage

```tsx
<Badge category="informational" variant="textInformational" size="xl" colorScheme="sparkle" emphasis="subtle">
  Trending
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

**Elevation: +1 from parent element**
- Bottom: Centre
- Top: Centre

**Elevation: Page 0 level**
- Inline right
- Inline left
- Inline

---

## 5. Icon + Label (With Container)

Icon and text in a rounded rectangle.


### Sizes

| Size | Container Height | Radius | Stroke (Optional) | Icon Size | Padding (L/R × T/B) | Typography            |
| ---- | ---------------- | ------ | ----------------- | --------- | ------------------- | --------------------- |
| 4XL  | 40px             | 8px    | 4px (Outline)     | 28px      | 8px × 4px           | body-l-bold (16px) |
| 3XL  | 32px             | 8px    | 3px (Outline)     | 20px      | 8px × 4px           | body-s-bold (14px) |
| 2XL  | 28px             | 4px    | 3px (Outline)     | 16px      | 8px × 4px           | body-xs-bold (12px) |
| XL   | 24px             | 4px    | 3px (Outline)     | 16px      | 4px × 2px           | body-xs-bold (12px) |
| L    | 20px             | 4px    | 3px (Outline)     | 16px      | 4px × 2px           | body-xxs-bold (10px) |
| M    | 16px             | 4px    | 2px (Outline)     | 12px      | 4px × —             | body-xxs-bold (10px) |

**Important:** All informational badge labels use `body-l-bold` (16px, `var(--text-base)`) regardless of badge size.

### Colors

Same as Label Only variant.

### Usage

```tsx
<Badge category="informational" variant="iconTextInformational" size="xl" colorScheme="sparkle" emphasis="subtle">
  <IcFire fill="currentColor" />
  Hot Deal
</Badge>
```

**Note:** Stroke is optional — use when badge overlaps other elements.

### Placement

Same as Label Only variant.

---

## 6. Image + Label (With Container)

Image and text in a rounded rectangle.

### Sizes

Same as Icon + Label variant, but with `[&>img]` instead of `[&>svg]`.

### Usage

```tsx
<Badge category="informational" variant="imageText" size="xl" colorScheme="secondary" emphasis="bold">
  <img src="/brand-logo.png" alt="" />
  Premium
</Badge>
```

---

## Color Schemes

### Notification

Always uses `--error-50` (red) background with white text.

### Status

| Scheme  | Bold BG           | Bold Text          | Subtle BG         | Subtle Text        |
| ------- | ----------------- | ------------------ | ----------------- | ------------------ |
| Success | `--success-50`    | `--global-white`   | `--success-20`    | `--success-50`     |
| Error   | `--error-50`      | `--global-white`   | `--error-20`      | `--error-50`       |
| Warning | `--warning-50`    | `--global-white`   | `--warning-20`    | `--warning-50`     |
| Neutral | `--grey-40`       | `--grey-60`        | `--grey-20`       | `--grey-60`        |

### Informational

| Scheme      | Bold BG           | Bold Text                  | Subtle BG         | Subtle Text        |
| ----------- | ----------------- | -------------------------- | ----------------- | ------------------ |
| Sparkle     | `--sparkle-60`    | `--primary-background`     | `--sparkle-20`    | `--sparkle-60`     |
| Secondary   | `--secondary-60`  | `--secondary-background`   | `--secondary-20`  | `--secondary-60`   |
| Neutral     | `--grey-80`       | `--primary-background`     | `--grey-20`       | `--grey-80`        |
| Positive    | `--success-50`    | `--primary-background`     | `--success-20`    | `--success-50`     |
| Negative    | `--error-50`      | `--primary-background`     | `--error-20`      | `--error-50`       |
| Warning     | `--warning-50`    | `--primary-background`     | `--warning-20`    | `--warning-50`     |

---

## Design Token Reference

### Colors

| Token                        | Value    | Usage                                     |
| ---------------------------- | -------- | ----------------------------------------- |
| `--error-50`                 | #FA2F40  | Notification badges background            |
| `--success-50`               | #0FA654  | Success status/informational (bold)       |
| `--success-20`               | #E8F9F0  | Success status/informational (subtle)     |
| `--error-20`                 | #FFEBEE  | Error status/informational (subtle)       |
| `--warning-50`               | #FF9500  | Warning status/informational (bold)       |
| `--warning-20`               | #FFF4E5  | Warning status/informational (subtle)     |
| `--sparkle-60`               | #9932FF  | Informational sparkle (bold)              |
| `--sparkle-20`               | #F3E5FF  | Informational sparkle (subtle)            |
| `--secondary-60`             | #FF3F6C  | Informational secondary (bold)            |
| `--secondary-20`             | #FFE5EC  | Informational secondary (subtle)          |
| `--grey-80`                  | #3D3D3D  | Neutral informational (bold)              |
| `--grey-20`                  | #F5F5F5  | Neutral informational (subtle)            |
| `--grey-40`                  | #E5E5E5  | Neutral status (bold)                     |
| `--grey-60`                  | #B5B5B5  | Neutral status text                       |
| `--global-white`             | #FFFFFF  | Text on bold badges                       |
| `--primary-background`       | #FFFFFF  | Stroke color, text on bold badges         |

### Typography

| Token                  | Value | Usage                                      |
| ---------------------- | ----- | ------------------------------------------ |
| `--text-base`          | 16px  | 4XL notification/status, ALL informational |
| `--text-small`         | 14px  | 3XL notification/status                    |
| `--text-tiny`          | 12px  | 2XL, XL notification/status                |
| `--text-micro`         | 10px  | L, M notification/status                   |
| `--font-weight-medium` | 500   | All badge text                             |
| `--font-family-jiotype`| JioType stack | Font family (all badges)           |

### Radius

| Token  | Value  | Usage                                     |
| ------ | ------ | ----------------------------------------- |
| Pill   | 9999px | Dot, number badges, icon circles          |
| 8px    | 8px    | Number+ (large), status/info containers (large), icon square (large) |
| 4px    | 4px    | Number+ (small), status/info containers (small/medium), icon square (medium) |
| 2px    | 2px    | Icon square (S size)                      |

---

## Props

| Prop          | Type                                                                 | Default          | Description                                 |
| ------------- | -------------------------------------------------------------------- | ---------------- | ------------------------------------------- |
| `category`    | `'notification' \| 'status' \| 'informational' \| 'brand' \| 'promo'` | `'informational'` | Functional category                        |
| `variant`     | See variants section                                                 | `'textInformational'` | Visual structure/layout                |
| `size`        | `'4xl' \| '3xl' \| '2xl' \| 'xl' \| 'l' \| 'm' \| 's' \| 'xs'`      | `'xl'`           | Dimensional size                            |
| `emphasis`    | `'bold' \| 'subtle'`                                                 | `'subtle'`       | Color intensity (status/informational)      |
| `colorScheme` | See color schemes section                                            | `'sparkle'`      | Color palette                               |
| `hasStroke`   | `boolean`                                                            | `false`          | Show border/stroke (for overlays)           |
| `bgColor`     | `string`                                                             | —                | Custom background color (CSS variable/hex)  |
| `textColor`   | `string`                                                             | —                | Custom text/icon color (CSS variable/hex)   |
| `borderColor` | `string`                                                             | —                | Custom border color (CSS variable/hex)      |
| `asChild`     | `boolean`                                                            | `false`          | Render as child element (Radix Slot)        |
| `className`   | `string`                                                             | —                | Additional CSS classes                      |
| ...           | `React.ComponentProps<'span'>`                                       | —                | All native span HTML attributes             |

---

## Usage Examples

### Notification Badges

```tsx
{/* Dot notification */}
<Badge category="notification" variant="dot" size="m" hasStroke />

{/* Number notification */}
<Badge category="notification" variant="number" size="l" hasStroke>
  5
</Badge>

{/* 99+ notification */}
<Badge category="notification" variant="numberPlus" size="m" hasStroke>
  99+
</Badge>
```

### Status Badges

```tsx
{/* Text container - bold */}
<Badge category="status" variant="textContainer" size="m" colorScheme="success" emphasis="bold">
  Active
</Badge>

{/* Text container - subtle */}
<Badge category="status" variant="textContainer" size="m" colorScheme="error" emphasis="subtle">
  Cancelled
</Badge>

{/* Icon + text container */}
<Badge category="status" variant="iconTextContainer" size="l" colorScheme="success" emphasis="bold">
  <IcCheckCircle fill="currentColor" />
  Online
</Badge>

{/* Dot only */}
<Badge category="status" variant="dotOnly" size="m" colorScheme="warning" />
```

### Informational Badges

```tsx
{/* Icon circle - bold */}
<Badge category="informational" variant="iconCircle" size="m" colorScheme="sparkle" emphasis="bold">
  <IcStar fill="currentColor" />
</Badge>

{/* Text only - subtle (DEFAULT for Story Cards) */}
<Badge category="informational" variant="textInformational" size="xl" colorScheme="sparkle" emphasis="subtle">
  Trending
</Badge>

{/* Icon + text - subtle */}
<Badge category="informational" variant="iconTextInformational" size="xl" colorScheme="secondary" emphasis="subtle">
  <IcFire fill="currentColor" />
  Hot Deal
</Badge>
```

### Custom Colors (Legacy Support)

For compatibility with existing code using custom color tokens:

```tsx
<Badge
  category="informational"
  variant="textInformational"
  size="xl"
  bgColor="var(--sparkle-20)"
  textColor="var(--sparkle-60)"
>
  Innovation
</Badge>
```

---

## Implementation Checklist

When implementing badge components, verify:

- [ ] Uses `category`, `variant`, `size`, `emphasis`, `colorScheme` props correctly
- [ ] Uses `font-family: var(--font-family-jiotype)` (inherited from base styles)
- [ ] Font weight is `var(--font-weight-medium)` (500) — never other weights
- [ ] Font size for informational badges is always `var(--text-base)` (16px)
- [ ] Font size for notification/status badges varies by size (16px / 14px / 12px / 10px)
- [ ] Border radius follows the spec (pill for dots/numbers, 8px/4px for containers)
- [ ] Colors use JDS design tokens from `/src/styles/theme.css`
- [ ] Icons use `fill=\"currentColor\"` for proper color inheritance
- [ ] Stroke/border is only applied when `hasStroke` prop is true
- [ ] Custom colors can be applied via `bgColor`, `textColor`, `borderColor` props