# Selector — JDS Component Style Guide

## Overview

The Selector is a control that allows users to choose one value from a range of options. It is an alternative to checkboxes, radio buttons, or dropdowns that clearly presents all available options and works well on mobile devices.

Component: `/src/app/components/ui/selector.tsx`

---

## When to Use

- ✅ **Use Selectors** whenever you want the user to choose one option from many (2-4 options work best)
- ✅ **Use to reduce cognitive load** — all options are visible at once
- ✅ **Use on mobile devices** — touch-friendly design with large tap targets
- ❌ **Do NOT use for filtering or navigation** — use Tabs instead
- ❌ **Do NOT use for many options** (>4) — consider a dropdown instead

---

## Anatomy

A basic selector is composed of:

1. **Container** — Tracker background with pill radius (`var(--grey-20)`)
2. **Selector Items** — Individual options that can be selected
3. **Active State** — Selected item with primary background
4. **Icon** (optional) — 24×24px icon
5. **Label** — Text label using `$body-s` typography

---

## Variants

### 1. Selector with Labels Only
```tsx
<Selector value={value} onValueChange={setValue}>
  <SelectorItem value="mobile">Mobile</SelectorItem>
  <SelectorItem value="home">Home</SelectorItem>
</Selector>
```

### 2. Selector with Icons Only
```tsx
<Selector value={value} onValueChange={setValue}>
  <SelectorItem value="grid" icon={<IcGrid />} />
  <SelectorItem value="list" icon={<IcList />} />
</Selector>
```

### 3. Selector with Icons and Labels
```tsx
<Selector value={value} onValueChange={setValue}>
  <SelectorItem value="mobile" icon={<IcMobile />}>Mobile</SelectorItem>
  <SelectorItem value="home" icon={<IcHome />}>Home</SelectorItem>
</Selector>
```

### 4. Vertical Selector
```tsx
<Selector value={value} onValueChange={setValue} orientation="vertical">
  <SelectorItem value="option1">Option 1</SelectorItem>
  <SelectorItem value="option2">Option 2</SelectorItem>
</Selector>
```

---

## Specifications

### Horizontal Selector

#### Item/Active State

| Property       | Value                                   |
| -------------- | --------------------------------------- |
| Icon Size      | 24×24px                                 |
| Icon color     | `var(--primary-inverse)` (#FFFFFF)     |
| Label          | `var(--text-body-s)` (16px)            |
| Label color    | `var(--primary-inverse)` (#FFFFFF)     |
| Font-family    | `var(--font-family-jiotype)`           |
| Font-weight    | `var(--font-weight-medium)` (500)      |
| Radii          | `var(--radius-full)` (9999px/pill)     |
| BG color       | `var(--primary-50)` (#0F3CC9)          |
| Width          | Fill container (flex-1)                 |
| Padding-top    | `var(--space-3)` (12px)                |
| Padding-bottom | `var(--space-3)` (12px)                |
| Padding-left   | `var(--space-6)` (24px)                |
| Padding-right  | `var(--space-6)` (24px)                |
| Min-height     | 48px                                    |
| Gap            | `var(--space-2)` (8px) between icon/label |

#### Item/Inactive State

| Property       | Value                                   |
| -------------- | --------------------------------------- |
| Icon Size      | 24×24px                                 |
| Icon color     | `var(--primary-60)` (#0A2885)          |
| Label          | `var(--text-body-s)` (16px)            |
| Label color    | `var(--primary-60)` (#0A2885)          |
| Font-family    | `var(--font-family-jiotype)`           |
| Font-weight    | `var(--font-weight-medium)` (500)      |
| Radii          | `var(--radius-full)` (9999px/pill)     |
| BG color       | `transparent`                           |
| Width          | Fill container (flex-1)                 |
| Padding-top    | `var(--space-3)` (12px)                |
| Padding-bottom | `var(--space-3)` (12px)                |
| Padding-left   | `var(--space-6)` (24px)                |
| Padding-right  | `var(--space-6)` (24px)                |
| Min-height     | 48px                                    |
| Hover BG       | `rgba(0, 0, 0, 0.02)`                  |

#### Tracker (Container)

| Property       | Value                                   |
| -------------- | --------------------------------------- |
| BG color       | `var(--grey-20)` (#F5F5F5)             |
| Radii          | `var(--radius-full)` (9999px/pill)     |
| Width          | Full width of parent container          |
| Padding        | `var(--space-1)` (4px)                 |
| Gap            | `var(--space-0)` (0px)                 |

#### Focused States

**Focused:Active**
- Same appearance as active state
- Stroke: 4px outline
- Stroke color: `var(--primary-60)` (#0A2885)
- Outline offset: 0px

**Focused:Inactive**
- Same appearance as inactive state
- Stroke: 4px outline
- Stroke color: `var(--primary-60)` (#0A2885)
- Outline offset: 0px

---

### Vertical Selector

#### When to Use Vertical

1. **Automatic (Responsive)** — When horizontal selector shrinks to a viewport where label and icon overflow, it converts to vertical
2. **User Defined** — Users can explicitly select vertical orientation with `orientation="vertical"`

#### Differences from Horizontal

| Property       | Value                                   |
| -------------- | --------------------------------------- |
| Flex direction | `column` (icon stacked above label)    |
| Gap            | `var(--space-2)` (8px) between icon/label |
| Min-height     | 56px (taller to accommodate stacking)   |

---

## Responsive Behavior

### Word Wrapping
- Labels with multiple words wrap to a second line
- **Maximum 2 lines** allowed across all variants
- Labels exceeding 2 lines will be truncated with ellipsis

### Truncation
- Long words that cannot fit in one line will be truncated
- CSS property: `text-overflow: ellipsis`
- CSS property: `-webkit-line-clamp: 2`

---

## Sizing

- The Selector component **always takes the full width** of its parent container
- Individual items use `flex-1` to distribute space evenly
- All elements in a selector should use the **same variant**
  - ❌ **Do NOT** mix label-only with icon+label variants
  - ✅ **Use consistent** icon+label OR label-only across all items

---

## Accessibility

- Uses `@radix-ui/react-radio-group` for proper radio semantics
- All items are keyboard-focusable
- Active item indicated with `data-state="checked"`
- Focus states use 4px outline for visibility
- `role="radiogroup"` provided by Radix (automatically)
- `role="radio"` on each item (automatically)
- `aria-checked` attribute updates on selection (automatically)

---

## Usage Guidelines

### ✅ Do

- Use for 2-4 mutually exclusive options
- Keep labels short and concise (1-2 words ideal)
- Use consistent variant across all items (all with icons, or all without)
- Use vertical orientation when labels are long
- Provide clear, distinct labels for each option

### ❌ Don't

- Don't use for more than 4 options (use dropdown instead)
- Don't mix variants (icon-only with icon+label)
- Don't use for filtering content (use Tabs)
- Don't use for navigation between pages (use Tabs or Navigation)
- Don't use arbitrary values — only CSS design tokens

---

## Code Example

### Basic Implementation

```tsx
import { Selector, SelectorItem } from './ui/selector';

function RechargeSection() {
  const [type, setType] = React.useState('mobile');

  return (
    <div className="max-w-md mx-auto">
      <Selector value={type} onValueChange={setType}>
        <SelectorItem value="mobile">Mobile</SelectorItem>
        <SelectorItem value="home">Home</SelectorItem>
      </Selector>
    </div>
  );
}
```

### With Icons

```tsx
import { Selector, SelectorItem } from './ui/selector';
import { IcMobile } from '@jds/extended-icons';
import { IcHome } from '@jds/core-icons';

function ServiceSelector() {
  const [service, setService] = React.useState('mobile');

  return (
    <Selector value={service} onValueChange={setService}>
      <SelectorItem value="mobile" icon={<IcMobile style={{ width: '24px', height: '24px' }} />}>
        Mobile
      </SelectorItem>
      <SelectorItem value="home" icon={<IcHome style={{ width: '24px', height: '24px' }} />}>
        Home
      </SelectorItem>
    </Selector>
  );
}
```

### Vertical Orientation

```tsx
<Selector value={value} onValueChange={setValue} orientation="vertical">
  <SelectorItem value="prepaid">Prepaid</SelectorItem>
  <SelectorItem value="postpaid">Postpaid</SelectorItem>
  <SelectorItem value="business">Business</SelectorItem>
</Selector>
```

---

## Design Tokens Used — Summary

### Colors

| Token                    | Usage                          |
| ------------------------ | ------------------------------ |
| `--primary-50`           | Active item background         |
| `--primary-60`           | Inactive item text/icon, focus outline |
| `--primary-inverse`      | Active item text/icon          |
| `--grey-20`              | Tracker/container background   |

### Typography

| Token                    | Usage                          |
| ------------------------ | ------------------------------ |
| `--font-family-jiotype`  | All text labels                |
| `--font-weight-medium`   | All labels (active + inactive) |
| `--text-body-s`          | Label font size (16px)         |

### Spacing

| Token       | Usage                                  |
| ----------- | -------------------------------------- |
| `--space-1` | Container padding (4px)                |
| `--space-2` | Gap between icon and label (8px)       |
| `--space-3` | Item padding top/bottom (12px)         |
| `--space-6` | Item padding left/right (24px)         |
| `--space-0` | Gap between items (0px — flush)        |

### Radius

| Token            | Usage                              |
| ---------------- | ---------------------------------- |
| `--radius-full`  | Container and item radius (pill)   |

---

## File Dependencies

- `@radix-ui/react-radio-group` — RadioGroup, RadioGroupItem primitives
- `/src/styles/theme.css` — All JDS design tokens
- `@jds/core-icons` — (optional) for icons
- `@jds/extended-icons` — (optional) for icons

---

## Related Components

- **Tabs** — Use for navigation/filtering content (different styling, different purpose)
- **Toggle** — Use for binary on/off states
- **Radio Group** — Selector is built on top of Radio Group with custom JDS styling
- **Button Group** — Use for actions, not selection

---

## Migration from ToggleGroup

If migrating from `ToggleGroup`, the API is similar:

**Before (ToggleGroup):**
```tsx
<ToggleGroup type="single" value={value} onValueChange={setValue}>
  <ToggleGroupItem value="option1">Option 1</ToggleGroupItem>
  <ToggleGroupItem value="option2">Option 2</ToggleGroupItem>
</ToggleGroup>
```

**After (Selector):**
```tsx
<Selector value={value} onValueChange={setValue}>
  <SelectorItem value="option1">Option 1</SelectorItem>
  <SelectorItem value="option2">Option 2</SelectorItem>
</Selector>
```

**Key Differences:**
- No `type="single"` prop needed (Selector is always single-selection)
- Cleaner styling adhering to JDS specs
- Proper focus states with 4px outline
- Icons are passed as `icon` prop
- Vertical orientation support built-in