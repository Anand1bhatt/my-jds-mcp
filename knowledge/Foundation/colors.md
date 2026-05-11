# Colors
The color system defines the visual language of the product. It ensures consistency, accessibility, and clarity across all UI components. All colors are token-based and optimized for AI-driven UI generation.

## Principles
* Color communicates hierarchy and meaning
* Fewer colors improve clarity
* Color must support accessibility
* Semantic meaning is more important than aesthetics


## Color Token Structure

### Token Format
{category}/{scale}

### Examples
* primary/50
* secondary/50
* sparkle/50
* success/50
* error/50
* warning/50
* grey/20
* global/white&black



## Color Categories
* Primary
* Secondary
* Sparkle
* Success
* Warning
* Error
* Global
* Grey

### Primary Color
* primary/80 - #070E21
* primary/70 - #061951
* primary/60 - #0A2885
* primary/50 - #0F3CC9
* primary/40 - #6789F4
* primary/30 - #9EB5FA
* primary/20 - #E7EBF8
* primary/inverse - #FFFFFF
* primary/background - #FFFFFF

**Usage**
* Actionable elements
* Primary CTAs
* Key highlights
* Active states
* Top navigation

### Secondary Color
* secondary/80 - #00002C
* secondary/70 - #00004A
* secondary/60 - #000067
* secondary/50 - #000093
* secondary/40 - #3535F3
* secondary/30 - #9999FF
* secondary/20 - #E8E8FC
* secondary/inverse - #401D0C
* secondary/background - #FFFFFF

**Usage**
* Secondary actions
* Supporting highlights

### Sparkle Color
* sparkle/80 - #001E2B
* sparkle/70 - #00364E
* sparkle/60 - #0C5273
* sparkle/50 - #0078AD
* sparkle/40 - #67C3EF
* sparkle/30 - #89DCFF
* sparkle/20 - #E5F1F7
* sparkle/inverse - #FFFFFF
* sparkle/background - #FFFFFF

**Usage**
* Accent highlights
* Attention-grabbing UI moments
* Limited decorative emphasis

### Grey Color
* grey/100 - #141414
* grey/80 - #000000 (opacity 65%)
* grey/60 - #B5B5B5
* grey/40 - #E0E0E0
* grey/20 - #F5F5F5

**Usage**
* Text
* App background
* Page sections
* Cards
* Sheets
* Containers
* Text must meet WCAG AA contrast
* Do not place low-contrast text on surfaces
* Inverse text only on dark or primary backgrounds

### Global Color
* black - #141414
* white - #FFFFFF

**Usage**
* Text
* App background
* Page sections
* Cards
* Sheets
* Containers
* Text must meet WCAG AA contrast
* Do not place low-contrast text on surfaces
* Inverse text only on dark or primary backgrounds

## Semantic Colors

### Success
* success/80 - #0E540C
* success/70 - #136C11
* success/60 - #1A8417
* success/50 - #25AB21
* success/40 - #85CE7F
* success/30 - #C8E7C5
* success/20 - #EFF8EE

### Warning
* warning/80 - #321304
* warning/70 - #582309
* warning/60 - #B04914
* warning/50 - #F06D0F
* warning/40 - #FC9E6D
* warning/30 - #FCD3BF
* warning/20 - #FFF2EC

### Error
* error/80 - #3E0006
* error/70 - #6A000F
* error/60 - #CD0027
* error/50 - #FA2F40
* error/40 - #FE9993
* error/30 - #FFCFCB
* error/20 - #FFF1F0

**Usage**
* Semantic colors convey meaning.
* They must not be used decoratively.


## Accessibility Guidelines (MANDATORY)
* Text contrast must meet WCAG AA
* Color must not be the only indicator of state
* Always combine color with text or icons


## Do & Don't

### ✅ Do
* Use predefined tokens
* Follow semantic meaning
* Validate contrast

### ❌ Don't
* Use hex values directly
* Use brand color everywhere
* Use color without meaning

---

## JDS Color Usage Rules

Canonical specification for background and color usage across all JDS pages and components.

---

## Mandatory Rule: White Background Only

All page sections, containers, and content areas **must** use a single white background. Grey (`--grey-20`, `--grey-10`, `bg-muted`, etc.) or any other tinted color **must not** be used as a section or container background.

### Allowed background token

```css
background-color: var(--global-white);
/* or equivalently */
background-color: var(--background);  /* maps to --global-white */
```

### Prohibited patterns

```css
/* DO NOT use grey as section/container backgrounds */
background-color: var(--grey-20);    /* prohibited */
background-color: var(--grey-40);    /* prohibited */
background-color: var(--card);       /* prohibited if it maps to grey */
```

```tsx
/* DO NOT use Tailwind grey/muted backgrounds on sections */
className="bg-muted/20"       // prohibited
className="bg-gray-50"        // prohibited
className="bg-slate-50"       // prohibited
```

---

## Mandatory Rule: No Card-on-Card

Never place a `<Card>` component on top of another card or a tinted container to create a layered "card-on-card" appearance. Content sections must render directly on the single white page background.

### Prohibited

```tsx
{/* Grey section wrapping a white card = card-on-card */}
<section style={{ backgroundColor: 'var(--grey-20)' }}>
  <Card style={{ backgroundColor: 'var(--global-white)' }}>
    ...content...
  </Card>
</section>
```

### Correct

```tsx
{/* Content directly on white background */}
<section style={{ backgroundColor: 'var(--global-white)' }}>
  ...content...
</section>
```

---

## Where Grey Is Permitted

Grey tokens may **only** be used for:

| Use case                    | Token                | Example                          |
|-----------------------------|----------------------|----------------------------------|
| Dividers / separators       | `var(--grey-40)`     | 1px horizontal rule              |
| Borders                     | `var(--grey-40)` / `var(--grey-60)` | Card borders, header border |
| UI control backgrounds      | `var(--grey-20)`     | Toggle-group pill track, input bg |
| Interactive hover states    | `var(--grey-20)`     | Icon button hover                |
| Muted text color            | `var(--grey-80)`     | Secondary / footnote text        |

These are **component-level** uses — never full-section backgrounds.

---

## JDS Color Palette Quick Reference

### Primary

| Token              | Value     | Usage                        |
|--------------------|-----------|------------------------------|
| `--primary-80`     | #070E21   | Darkest primary              |
| `--primary-70`     | #061951   | Darker primary               |
| `--primary-60`     | #0A2885   | Dark primary                 |
| `--primary-50`     | #0F3CC9   | Default primary actions/CTAs |
| `--primary-40`     | #6789F4   | Light primary                |
| `--primary-30`     | #9EB5FA   | Lighter primary              |
| `--primary-20`     | #E7EBF8   | Icon circle backgrounds      |
| `--primary-inverse`| #FFFFFF   | Text on primary bg           |

### Secondary

| Token               | Value     | Usage                     |
|---------------------|-----------|---------------------------|
| `--secondary-80`    | #00002C   | Darkest secondary         |
| `--secondary-70`    | #00004A   | Darker secondary          |
| `--secondary-60`    | #000067   | Dark secondary            |
| `--secondary-50`    | #000093   | Default secondary CTAs    |
| `--secondary-40`    | #3535F3   | Light secondary           |
| `--secondary-30`    | #9999FF   | Lighter secondary         |
| `--secondary-20`    | #E8E8FC   | Lightest secondary        |
| `--secondary-inverse`| #401D0C  | Text on secondary bg      |

### Sparkle (Accent)

| Token              | Value     | Usage                     |
|--------------------|-----------|---------------------------|
| `--sparkle-80`     | #001E2B   | Darkest sparkle           |
| `--sparkle-70`     | #00364E   | Darker sparkle            |
| `--sparkle-60`     | #0C5273   | Accent CTAs               |
| `--sparkle-50`     | #0078AD   | Default sparkle           |
| `--sparkle-40`     | #67C3EF   | Light sparkle             |
| `--sparkle-30`     | #89DCFF   | Lighter sparkle           |
| `--sparkle-20`     | #E5F1F7   | Lightest sparkle          |
| `--sparkle-inverse`| #FFFFFF   | Text on sparkle bg        |

### Semantic

| Token            | Value     | Usage               |
|------------------|-----------|---------------------|
| `--error-50`     | #FA2F40   | Error states        |
| `--success-50`   | #25AB21   | Success states      |
| `--warning-50`   | #F06D0F   | Warning states      |

### Global

| Token            | Value     | Usage                          |
|------------------|-----------|--------------------------------|
| `--global-white` | #FFFFFF   | Page background (the only one) |
| `--global-black` | #141414   | Primary text, dark elements    |

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
