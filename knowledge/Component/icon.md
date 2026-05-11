# Icon Component

**Component:** Icon  
**Status:** Active  
**Last Updated:** 2026-02-20

---

## 1. Overview

The Icon component is a visual primitive used to provide metaphorical or literal representations of actions, concepts, or objects. It is built to be highly flexible, supporting color inheritance and complex background variants.

---

## 2. Anatomy & Configuration

An icon consists of a vector glyph (SVG) that can be rendered standalone or inside a background container based on the `kind` property.

**Structure:**
- **Icon Glyph:** The SVG vector graphic
- **Background Container (optional):** Circular container when `kind` is set to `background` or `background-bold`

---

## 3. Technical Specifications (Props)

| Prop | Type | Description |
|------|------|-------------|
| `ic`* | `React.ComponentType` | **(Required)** The icon component from `@jds/core-icons` or `@jds/extended-icons` |
| `color` | `string \| 'none' \| 'inherit'` | Uses Design System Color Tokens. `inherit` takes the color of the parent text/container. Default: `'inherit'` |
| `kind` | `'default' \| 'background' \| 'background-bold'` | Defines the container style. Default: `'default'` |
| `size` | `'sm' \| 'md' \| 'lg' \| 'xl' \| 'xxl' \| 'fill' \| 'custom'` | Predefined sizing scale. `fill` forces the icon to 100% of parent. Default: `'custom'` |
| `className` | `string` | Optional additional CSS classes |
| `style` | `React.CSSProperties` | Optional inline styles |

---

## 4. Visual Logic & States

### A. Background Logic (`kind`)

**`default`** — Glyph rendered without a container
- Icon displayed standalone
- Color applied directly to the icon glyph
- No background container

**`background`** — Glyph rendered inside a subtle container
- Icon placed inside a circular background container
- Background uses the 20% tint of the selected color (e.g., `primary-50` → `primary-20` background)
- Icon glyph uses the full color value (e.g., `primary-50`)
- Provides visual separation and emphasis

**`background-bold`** — Selected color applied to background container
- Background uses the full color value (e.g., `primary-50`)
- Icon glyph color is automatically inversed for maximum contrast
- Creates high-impact, bold visual treatment

---

### B. Color Inheritance

By default, the icon is set to `inherit`. This is highly effective for webpage builders where icons inside buttons or list items should automatically match the text color of their parent.

**Example:**
```tsx
// Icon inherits blue color from parent button
<Button color="primary">
  <Icon ic={IcHome} /> Home
</Button>
```

---

### C. The Inverse Variation

"Inverse" is not a separate variant. To achieve an inverse look:

1. Select `primary-inverse` from the `color` prop
2. Set `kind` to `default`
3. Enable bold mode (if applicable in parent container)

**Example:**
```tsx
<Icon ic={IcHome} color="var(--primary-inverse)" kind="default" />
```

---

## 5. Size Specifications

### Size S (`sm`)
**No Background:**
- Icon size: 16×16px

**Background:**
- Not available on this size

---

### Size M (`md`)
**No Background:**
- Icon size: 24×24px

**Background:**
- Container size: 24×24px
- Icon size: 16×16px
- Border radius: 50% (circular)

---

### Size L (`lg`)
**No Background:**
- Icon size: 32×32px

**Background:**
- Container size: 32×32px
- Icon size: 24×24px
- Border radius: 50% (circular)

---

### Size XL (`xl`)
**No Background:**
- Icon size: 40×40px

**Background:**
- Container size: 40×40px
- Icon size: 32×32px
- Border radius: 50% (circular)

---

### Size XXL (`xxl`)
**No Background:**
- Icon size: 48×48px

**Background:**
- Container size: 48×48px
- Icon size: 32×32px
- Border radius: 50% (circular)

---

### Custom (`custom`) — Default Value
**No Background:**
- Icon size: 24×24px

**Background:**
- Container size: 24×24px
- Icon size: 16×16px

**Note:** The icon should have a 2/3 proportion to the background variant for custom sizes. Added custom size option — it will resize based on content.

---

### Fill (`fill`)
- Icon scales to 100% width and height of parent container
- Useful for responsive layouts

---

### Size Constraints

- **Minimum size:** 8px
- **Maximum size:** 1000px

**Note:** Ensure that icon sizes are not smaller than the minimum of 8px and do not exceed the maximum limit of 1000px.

---

## 6. Icon Color Options

All color values reference CSS variables from `/src/styles/theme.css`:

| Color Token | Background Pair | Usage |
|-------------|-----------------|-------|
| `var(--primary-50)` | `var(--primary-20)` | Primary brand actions |
| `var(--secondary-50)` | `var(--secondary-20)` | Secondary actions |
| `var(--sparkle-50)` | `var(--sparkle-20)` | Special promotions |
| `var(--success-50)` | `var(--success-20)` | Success states |
| `var(--warning-50)` | `var(--warning-20)` | Warning states |
| `var(--error-50)` | `var(--error-20)` | Error states |
| `var(--grey-60)` | `var(--grey-20)` | Muted/neutral |
| `var(--grey-80)` | `var(--grey-20)` | Text-level neutral |
| `var(--grey-100)` | `var(--grey-20)` | High contrast neutral |
| `var(--primary-inverse)` | — | Inverse on dark backgrounds |
| `var(--secondary-inverse)` | — | Secondary inverse |
| `var(--sparkle-inverse)` | — | Sparkle inverse |
| `var(--global-white)` | — | White icons on dark |
| `var(--global-black)` | — | Black icons on light |

---

## 7. Design Tokens

All styling uses CSS variables from `/src/styles/theme.css`:

### Colors
```css
/* Primary */
--primary-50
--primary-20

/* Secondary */
--secondary-50
--secondary-20

/* Sparkle */
--sparkle-50
--sparkle-20

/* Feedback */
--success-50, --success-20
--warning-50, --warning-20
--error-50, --error-20

/* Neutrals */
--grey-20, --grey-60, --grey-80, --grey-100

/* Inverse */
--primary-inverse
--secondary-inverse
--sparkle-inverse
```

---

## 8. Implementation Requirements

### Mandatory: Filled Icons Only

All icons used in JDS components **must** be rendered in their **filled** style. Outline/stroke-only icons are not permitted.

### Using @jds/core-icons and @jds/extended-icons

JDS icons are designed to work with `fill="currentColor"`:

```tsx
import { IcHome } from '@jds/core-icons';

<IcHome fill="currentColor" />
```

### Using lucide-react (Fallback)

lucide-react icons are stroke-based by default. To convert them to filled style, **always** pass:

```tsx
<IconName fill="currentColor" />
```

For icons where fill + stroke creates visual doubling, also reduce stroke width:

```tsx
<IconName fill="currentColor" strokeWidth={1} />
```

### Custom SVG Icons

When creating inline SVG icons, always use `fill="currentColor"`:

```tsx
<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
  <path d="..." />
</svg>
```

---

## 9. Usage Examples

### Example 1: Simple Icon (No Background)
```tsx
<Icon 
  ic={IcHome} 
  size="md" 
  color="var(--primary-50)" 
/>
```

### Example 2: Icon with Background
```tsx
<Icon 
  ic={IcMobile} 
  size="lg" 
  kind="background"
  color="var(--primary-50)" 
/>
// Result: 32×32 grey background with 24×24 primary icon
```

### Example 3: Bold Background Icon
```tsx
<Icon 
  ic={IcSupport} 
  size="xl" 
  kind="background-bold"
  color="var(--sparkle-50)" 
/>
// Result: 40×40 sparkle background with 32×32 white icon
```

### Example 4: Color Inheritance
```tsx
<div style={{ color: 'var(--primary-50)' }}>
  <Icon ic={IcHome} size="md" />
  {/* Icon automatically inherits primary-50 color */}
</div>
```

### Example 5: Fill Size
```tsx
<div style={{ width: '64px', height: '64px' }}>
  <Icon ic={IcHome} size="fill" color="var(--primary-50)" />
  {/* Icon fills the entire 64×64 parent */}
</div>
```

---

## 10. Typography Rules for Icon Labels

All text labels associated with icons (e.g., quick-action labels, button text) must use:

- **Font family:** `var(--font-family-jiotype)` exclusively
- **Font weights:** Only the four permitted JDS weight tokens:
  - `var(--font-weight-normal)` (400)
  - `var(--font-weight-medium)` (500)
  - `var(--font-weight-bold)` (700)
  - `var(--font-weight-black)` (900)
- **No other fonts or weights** are allowed.

---

## 11. Accessibility

- Always provide `aria-label` or `aria-hidden` when using icons
- Decorative icons should have `aria-hidden="true"`
- Interactive icons must have accessible labels
- Ensure sufficient color contrast (WCAG AA minimum)

---

## 12. Best Practices

✅ **DO:**
- Use `inherit` for icons inside buttons or cards
- Use `background` variant for standalone action items
- Use `background-bold` for CTAs or feature highlights
- Keep icon sizes consistent within the same context
- Use design tokens for all colors

❌ **DON'T:**
- Mix outline and filled icon styles
- Use arbitrary pixel values for sizing
- Use hard-coded hex colors
- Exceed 1000px or go below 8px
- Use icons smaller than 16px for interactive elements

---

## 13. Related Components

- **Button** — Icons commonly used inside buttons
- **Card** — Icons used for card headers or actions
- **Header** — Navigation and action icons
- **Footer** — Social media and utility icons
- **Quick Actions** — Circular icon buttons

---

**End of Icon Component Specification**
