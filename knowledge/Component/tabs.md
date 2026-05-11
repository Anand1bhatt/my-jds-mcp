# Tabs — JDS Component Style Guide

## Overview

**Definition:** A tab component that organises related content into switchable views. Users can navigate between content panels using tab triggers arranged horizontally.

**Purpose:** To streamline navigation across related, mutually exclusive content sections without page reloads.

Component: `/src/app/components/ui/tabs.tsx`
CSS Rules: `/src/styles/theme.css` (under `@layer base`)

---

## Architecture

Built on `@radix-ui/react-tabs`. All state-based visual styling (default, hover, active, focus, disabled) is driven entirely by CSS rules in `/src/styles/theme.css` using `[data-variant]` + `[data-state]` attribute selectors. The React component only manages size-dependent spacing/font-size via inline styles using design tokens. This means:

- **No MutationObservers** — pure CSS handles state transitions
- **No imperative DOM manipulation** — no `onMouseEnter`/`onMouseLeave` style hacks
- **Fully CSS-editable** — update styling by editing `/src/styles/theme.css` alone
- **Override-safe** — `!important` on `font-family`/`font-weight` defeats the global `button` base style

### Component Parts

1. **Tabs (Root):** Container managing tab state and keyboard navigation.
2. **TabsList:** Container for triggers. Accepts `variant`, `size`, `fullWidth`, `scrollable`. Provides variant/size context to child triggers.
3. **TabsTrigger:** Individual clickable tab. Renders `data-variant` attribute from context so CSS can target it. Radix sets `data-state="active"|"inactive"` automatically.
4. **TabsContent:** Content panel associated with each tab, controlled by matching `value`.

---

## When to Use

- ✅ **Use When:** You have 2–8 related content sections at the same hierarchy level.
- ✅ **Use When:** Users need to switch between views without leaving the page.
- ✅ **Use When:** Only one content section should be visible at a time.
- ❌ **Do NOT Use When:** The list exceeds 8 items (use sidebar, dropdown, or accordion).
- ❌ **Do NOT Use When:** Users need to compare content side-by-side.
- ❌ **Do NOT Use When:** Content has a sequential flow (use a stepper/wizard).

---

## Variants

The component supports two primary visual variants:

### A. Pill Variant (Default)

Contained pill-shaped tab triggers inside a muted `var(--grey-40)` background container. Active tab appears as an elevated white pill with `var(--shadow-card-light)`.

```tsx
<Tabs defaultValue="overview">
  <TabsList variant="pill" size="medium">
    <TabsTrigger value="overview">Overview</TabsTrigger>
    <TabsTrigger value="features">Features</TabsTrigger>
    <TabsTrigger value="pricing">Pricing</TabsTrigger>
  </TabsList>
  <TabsContent value="overview">...</TabsContent>
  <TabsContent value="features">...</TabsContent>
  <TabsContent value="pricing">...</TabsContent>
</Tabs>
```

### B. Line Variant (Underline)

Flat transparent-background triggers with a coloured `var(--primary-50)` bottom border on the active tab. Used in SubHeaders and navigation bars.

```tsx
<Tabs defaultValue="discover">
  <TabsList variant="line" size="medium">
    <TabsTrigger value="discover">Discover</TabsTrigger>
    <TabsTrigger value="plans">Plans</TabsTrigger>
    <TabsTrigger value="devices">Devices</TabsTrigger>
  </TabsList>
  <TabsContent value="discover">...</TabsContent>
  <TabsContent value="plans">...</TabsContent>
  <TabsContent value="devices">...</TabsContent>
</Tabs>
```

---

## Specifications

### Pill Variant

#### Large Size (40px)

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| **TabsList Height**| 40px                                         |
| TabsList Background| `var(--grey-40)`                             |
| TabsList Radius    | `var(--radius-lg)` (24px)                    |
| TabsList Padding   | 3px                                          |
| Trigger Radius     | `var(--radius-lg)` (24px)                    |
| Trigger Padding    | `var(--space-2)` `var(--space-4)` (8px 16px) |
| Trigger Font       | `var(--text-body-s)` (16px)                  |
| Trigger Weight     | `var(--font-weight-medium)` (500)            |
| Active Background  | `var(--global-white)`                        |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Shadow      | `var(--shadow-card-light)`                   |

#### Medium Size (36px) — Default

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| **TabsList Height**| 36px                                         |
| TabsList Background| `var(--grey-40)`                             |
| TabsList Radius    | `var(--radius-lg)` (24px)                    |
| TabsList Padding   | 3px                                          |
| Trigger Radius     | `var(--radius-lg)` (24px)                    |
| Trigger Padding    | `var(--space-1)` `var(--space-3)` (4px 12px) |
| Trigger Font       | `var(--text-label)` (14px)                   |
| Trigger Weight     | `var(--font-weight-medium)` (500)            |
| Active Background  | `var(--global-white)`                        |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Shadow      | `var(--shadow-card-light)`                   |

#### Small Size (32px)

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| **TabsList Height**| 32px                                         |
| TabsList Background| `var(--grey-40)`                             |
| TabsList Radius    | `var(--radius-lg)` (24px)                    |
| TabsList Padding   | 2px                                          |
| Trigger Radius     | `var(--radius-lg)` (24px)                    |
| Trigger Padding    | `var(--space-1)` `var(--space-2)` (4px 8px)  |
| Trigger Font       | `var(--text-body-xs)` (14px)                 |
| Trigger Weight     | `var(--font-weight-medium)` (500)            |
| Active Background  | `var(--global-white)`                        |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Shadow      | `var(--shadow-card-light)`                   |

---

### Line Variant

#### Large Size (48px)

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| TabsList Background| transparent                                  |
| TabsList Gap       | `var(--space-6)` (24px)                      |
| Trigger Padding    | `var(--space-4)` (16px all sides)            |
| Trigger Font       | `var(--text-body-s)` (16px)                  |
| Inactive Color     | `var(--grey-80)`                             |
| Inactive Weight    | `var(--font-weight-medium)` (500)            |
| Active Color       | `var(--primary-50)`                          |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Indicator   | `var(--border-width-thick)` (2px) bottom border, `var(--primary-50)` |

#### Medium Size (40px) — Default

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| TabsList Background| transparent                                  |
| TabsList Gap       | `var(--space-0)` (0px)                       |
| Trigger Padding    | `var(--space-3)` (12px all sides)            |
| Trigger Font       | `var(--text-label)` (14px)                   |
| Inactive Color     | `var(--grey-80)`                             |
| Inactive Weight    | `var(--font-weight-medium)` (500)            |
| Active Color       | `var(--primary-50)`                          |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Indicator   | `var(--border-width-thick)` (2px) bottom border, `var(--primary-50)` |

#### Small Size (32px)

| Element            | Specification                                |
| ------------------ | -------------------------------------------- |
| TabsList Background| transparent                                  |
| TabsList Gap       | `var(--space-0)` (0px)                       |
| Trigger Padding    | `var(--space-2)` `var(--space-3)` (8px 12px) |
| Trigger Font       | `var(--text-body-xs)` (14px)                 |
| Inactive Color     | `var(--grey-80)`                             |
| Inactive Weight    | `var(--font-weight-medium)` (500)            |
| Active Color       | `var(--primary-50)`                          |
| Active Weight      | `var(--font-weight-bold)` (700)              |
| Active Indicator   | `var(--border-width-thick)` (2px) bottom border, `var(--primary-50)` |

---

## Visual States

### Pill Variant

All state rules live in `/src/styles/theme.css` under `[data-slot="tabs-trigger"][data-variant="pill"]`.

| State     | Text Color        | Background              | Border       | Shadow                     | Font Weight                |
| --------- | ----------------- | ----------------------- | ------------ | -------------------------- | -------------------------- |
| Default   | `var(--grey-100)` | transparent             | transparent  | none                       | `var(--font-weight-medium)`|
| Hover     | `var(--grey-100)` | `var(--grey-20)`        | transparent  | none                       | `var(--font-weight-medium)`|
| Active    | `var(--grey-100)` | `var(--global-white)`   | transparent  | `var(--shadow-card-light)` | `var(--font-weight-bold)`  |
| Focus     | inherit           | inherit                 | `var(--primary-50)` 1px | 3px ring `var(--primary-50)` 50% | inherit |
| Disabled  | inherit (30%)     | inherit (30%)           | inherit (30%)| none                       | inherit (30%)              |

### Line Variant

All state rules live in `/src/styles/theme.css` under `[data-slot="tabs-trigger"][data-variant="line"]`.

| State     | Text Color          | Border Bottom              | Font Weight                |
| --------- | ------------------- | -------------------------- | -------------------------- |
| Default   | `var(--grey-80)`    | transparent (2px)          | `var(--font-weight-medium)`|
| Hover     | `var(--primary-50)` | `var(--primary-30)` (2px)  | `var(--font-weight-medium)`|
| Active    | `var(--primary-50)` | `var(--primary-50)` (2px)  | `var(--font-weight-bold)`  |
| Focus     | inherit             | 1px outline `var(--primary-50)` | inherit              |
| Disabled  | inherit (30%)       | inherit (30%)              | inherit (30%)              |

---

## Behavioral Logic

### Scrollable Tabs

- Set `scrollable` prop on `TabsList` to enable horizontal overflow scrolling with hidden scrollbars.
- Scrollbar hiding: `scrollbar-width: none` (Firefox), `::-webkit-scrollbar { display: none }` (Chrome/Safari via CSS in theme.css).
- Recommended for SubHeader navigation with many tabs.

### Full Width

- Set `fullWidth` prop on `TabsList` to apply `w-full`.
- In pill variant, each trigger automatically gets `flex: 1` to fill available space.

### Controlled vs Uncontrolled

- **Uncontrolled:** Use `defaultValue` on `Tabs` — component manages its own state.
- **Controlled:** Use `value` + `onValueChange` on `Tabs` — parent manages state.

### With Icons

- Icons can be placed before text inside `TabsTrigger`.
- Icons auto-size to 16px (`size-4`) and use `fill="currentColor"`.
- Icons inherit the trigger's text colour in all states.
- `var(--space-1)` (4px) gap between icon and text.

---

## Spacing

### Pill Variant
- TabsList → TabsContent: controlled by parent `gap` (default: `gap-2` on Tabs root = 8px)
- Triggers are adjacent inside the TabsList (no gap)

### Line Variant
- TabsList → TabsContent: typically `gap-0` on Tabs root
- Between triggers: `var(--space-0)` default for small/medium; `var(--space-6)` for large

---

## Alignment

- Triggers are **center-aligned** vertically within TabsList
- Text and icons are center-aligned horizontally within each trigger
- Line variant indicators are flush with the trigger bottom edge
- Pill variant uses `flex: 1` to distribute triggers equally within the pill container

---

## Accessibility (A11y)

- Follows [WAI-ARIA Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)
- `role="tablist"` on TabsList, `role="tab"` on triggers, `role="tabpanel"` on content
- `aria-selected` on active trigger
- `aria-labelledby` linking content panels to triggers
- **Keyboard Navigation:**
  - `Tab` — Focus tab list, then next focusable element
  - `ArrowLeft` / `ArrowRight` — Navigate between tabs (horizontal)
  - `Home` — Focus first tab
  - `End` — Focus last tab
  - `Space` / `Enter` — Activate tab (manual activation mode)
- Disabled tabs: `opacity: 0.3`, `pointer-events: none`, skipped in tab order
- Focus ring: `1px solid var(--primary-50)` outline + `3px` ring at 50% opacity

---

## Props

### Tabs (Root)

| Prop            | Type                        | Default        | Description                    |
| --------------- | --------------------------- | -------------- | ------------------------------ |
| `defaultValue`  | `string`                    | —              | Default active tab (uncontrolled) |
| `value`         | `string`                    | —              | Active tab (controlled)        |
| `onValueChange` | `(value: string) => void`   | —              | Change callback                |
| `orientation`   | `'horizontal' \| 'vertical'`| `'horizontal'` | Tab orientation                |
| `activationMode`| `'automatic' \| 'manual'`   | `'automatic'`  | Activation mode                |
| `className`     | `string`                    | —              | Additional CSS classes         |

### TabsList

| Prop         | Type                            | Default    | Description                           |
| ------------ | ------------------------------- | ---------- | ------------------------------------- |
| `variant`    | `'pill' \| 'line'`              | `'pill'`   | Visual variant                        |
| `size`       | `'small' \| 'medium' \| 'large'`| `'medium'` | Size variant                          |
| `fullWidth`  | `boolean`                       | `false`    | Distribute triggers equally           |
| `scrollable` | `boolean`                       | `false`    | Enable horizontal scroll              |
| `className`  | `string`                        | —          | Additional CSS classes                |

### TabsTrigger

| Prop       | Type      | Default | Description                     |
| ---------- | --------- | ------- | ------------------------------- |
| `value`    | `string`  | —       | Tab value (required)            |
| `disabled` | `boolean` | `false` | Disabled state                  |
| `className`| `string`  | —       | Additional CSS classes          |

### TabsContent

| Prop         | Type      | Default | Description                     |
| ------------ | --------- | ------- | ------------------------------- |
| `value`      | `string`  | —       | Tab value (required)            |
| `forceMount` | `boolean` | `false` | Force mount when inactive       |
| `className`  | `string`  | —       | Additional CSS classes          |

---

## CSS Rules Reference

All tab visual state rules live in `/src/styles/theme.css` under `@layer base`. This means you can update any colour, weight, radius, or shadow by editing CSS alone — no React code changes needed.

### Pill Variant CSS Selectors

```css
/* Default state */
[data-slot="tabs-trigger"][data-variant="pill"] { ... }

/* Hover (inactive only) */
[data-slot="tabs-trigger"][data-variant="pill"]:hover:not([data-state="active"]):not(:disabled) { ... }

/* Active state */
[data-slot="tabs-trigger"][data-variant="pill"][data-state="active"] { ... }

/* Disabled state */
[data-slot="tabs-trigger"][data-variant="pill"]:disabled { ... }
```

### Line Variant CSS Selectors

```css
/* Default state */
[data-slot="tabs-trigger"][data-variant="line"] { ... }

/* Hover (inactive only) */
[data-slot="tabs-trigger"][data-variant="line"]:hover:not([data-state="active"]):not(:disabled) { ... }

/* Active state */
[data-slot="tabs-trigger"][data-variant="line"][data-state="active"] { ... }

/* Disabled state */
[data-slot="tabs-trigger"][data-variant="line"]:disabled { ... }
```

### Focus Visible (both variants)

```css
[data-slot="tabs-trigger"]:focus-visible { ... }
```

---

## Code Examples

### Pill Tabs (Default)

```tsx
import { Tabs, TabsList, TabsTrigger, TabsContent } from './ui/tabs';

<Tabs defaultValue="overview">
  <TabsList variant="pill" size="medium">
    <TabsTrigger value="overview">Overview</TabsTrigger>
    <TabsTrigger value="features">Features</TabsTrigger>
    <TabsTrigger value="pricing">Pricing</TabsTrigger>
  </TabsList>
  <TabsContent value="overview">Overview content</TabsContent>
  <TabsContent value="features">Features content</TabsContent>
  <TabsContent value="pricing">Pricing content</TabsContent>
</Tabs>
```

### Line Tabs (SubHeader Navigation)

```tsx
<Tabs value={activeTab} onValueChange={setActiveTab} className="gap-0">
  <TabsList variant="line" size="medium" scrollable>
    <TabsTrigger value="discover">Discover</TabsTrigger>
    <TabsTrigger value="prepaid">Prepaid</TabsTrigger>
    <TabsTrigger value="postpaid">Postpaid</TabsTrigger>
    <TabsTrigger value="devices">Devices</TabsTrigger>
  </TabsList>
</Tabs>
```

### Full Width Pill Tabs

```tsx
<Tabs defaultValue="all">
  <TabsList variant="pill" size="large" fullWidth>
    <TabsTrigger value="all">All</TabsTrigger>
    <TabsTrigger value="active">Active</TabsTrigger>
    <TabsTrigger value="completed">Completed</TabsTrigger>
  </TabsList>
  <TabsContent value="all">All items</TabsContent>
</Tabs>
```

### Tabs with Icons

```tsx
import { IcHome, IcSettings } from '@jds/core-icons';

<Tabs defaultValue="home">
  <TabsList variant="pill" size="medium">
    <TabsTrigger value="home">
      <IcHome fill="currentColor" style={{ width: '16px', height: '16px' }} />
      Home
    </TabsTrigger>
    <TabsTrigger value="settings">
      <IcSettings fill="currentColor" style={{ width: '16px', height: '16px' }} />
      Settings
    </TabsTrigger>
  </TabsList>
</Tabs>
```

### Disabled Tab

```tsx
<TabsList variant="pill" size="medium">
  <TabsTrigger value="tab1">Tab 1</TabsTrigger>
  <TabsTrigger value="tab2" disabled>Tab 2 (Disabled)</TabsTrigger>
  <TabsTrigger value="tab3">Tab 3</TabsTrigger>
</TabsList>
```

---

## Design Tokens Used — Summary

### Colors

| Token                | Usage                              |
| -------------------- | ---------------------------------- |
| `--global-white`     | Pill active background             |
| `--grey-20`          | Pill hover background              |
| `--grey-40`          | Pill TabsList background           |
| `--grey-80`          | Line inactive text                 |
| `--grey-100`         | Pill text (foreground)             |
| `--primary-30`       | Line hover indicator               |
| `--primary-50`       | Line active text/indicator, focus ring |

### Typography

| Token                   | Usage                           |
| ----------------------- | ------------------------------- |
| `--font-family-jiotype` | All tab text                    |
| `--font-weight-medium`  | Inactive trigger text (500)     |
| `--font-weight-bold`    | Active trigger text (700)       |
| `--text-body-xs`        | Small trigger text (14px)       |
| `--text-label`          | Medium trigger text (14px)      |
| `--text-body-s`         | Large trigger text (16px)       |

### Spacing

| Token        | Usage                                |
| ------------ | ------------------------------------ |
| `--space-0`  | Line variant gap (small/medium)      |
| `--space-1`  | Pill small/medium trigger padding-y; icon-text gap |
| `--space-2`  | Pill small trigger padding-x; line small trigger padding-y |
| `--space-3`  | Pill/line medium trigger padding     |
| `--space-4`  | Pill/line large trigger padding      |
| `--space-6`  | Line large variant trigger gap       |

### Radius

| Token          | Usage                            |
| -------------- | -------------------------------- |
| `--radius-lg`  | Pill TabsList and trigger (24px) |

### Borders

| Token                  | Usage                          |
| ---------------------- | ------------------------------ |
| `--border-width-thick` | Line active indicator (2px)    |

### Shadows

| Token                  | Usage                          |
| ---------------------- | ------------------------------ |
| `--shadow-card-light`  | Pill active trigger elevation  |

---

## Related Components

- **SubHeader** — Uses Line variant tabs for page-level navigation
- **Accordion** — Use for expandable content sections
- **InputDropdown** — Use when list exceeds 8 items
- **Button** — Use for actions, not navigation

---

## Designer Do's & Don'ts

- ✅ **Do:** Keep labels short (1–2 words)
- ✅ **Do:** Use sentence case for labels
- ✅ **Do:** Use Line variant for SubHeader navigation
- ✅ **Do:** Use Pill variant for in-page content switching
- ✅ **Do:** Use `scrollable` for more than 5 tabs in tight containers
- ❌ **Don't:** Nest tabs inside tabs
- ❌ **Don't:** Use more than 8 tabs
- ❌ **Don't:** Use arbitrary colours or font weights
- ❌ **Don't:** Mix Pill and Line variants in the same view
- ❌ **Don't:** Use tabs for sequential flows (use steppers)
- ❌ **Don't:** Add inline style overrides for state colours — edit the CSS rules in theme.css instead

---

## Validation Checklist

- [ ] Uses `font-family: var(--font-family-jiotype)` exclusively (enforced via CSS `!important`)
- [ ] Font weight uses `var(--font-weight-medium)` / `var(--font-weight-bold)` only (enforced via CSS)
- [ ] Font size uses design tokens (`--text-label`, `--text-body-s`, `--text-body-xs`)
- [ ] Pill: TabsList background `var(--grey-40)`, active `var(--global-white)` + shadow
- [ ] Line: Active text/border `var(--primary-50)`, inactive `var(--grey-80)`
- [ ] Line: Hover shows `var(--primary-30)` underline
- [ ] Disabled: `opacity: 0.3`, `pointer-events: none`
- [ ] Focus ring uses `var(--primary-50)` via `color-mix` for 50% opacity
- [ ] All colours reference CSS variables from `/src/styles/theme.css`
- [ ] No Tailwind text-size or font-weight utilities
- [ ] No MutationObservers or imperative DOM styling in the component
- [ ] No `onMouseEnter`/`onMouseLeave` style handlers — CSS `:hover` only
- [ ] Component is keyboard accessible (ARIA tabs pattern)
- [ ] `data-variant` attribute propagated from TabsList to TabsTrigger
