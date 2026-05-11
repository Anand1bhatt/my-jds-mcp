# Accordion — JDS Component Specification

## 1. Overview

**Function:** An accordion is a vertically stacked list of headers that reveals or hides additional content when clicked. It helps reduce page length and cognitive load.

**When to use:** Use when users only need to see specific pieces of content within a large information set (e.g., FAQs, Product Details, or Settings).

**Component file:** `/src/app/components/ui/accordion.tsx`

---

## 2. Anatomy

| # | Slot | Description |
|---|------|-------------|
| 1 | **Prefix** (Optional) | **1A.** Avatar (Medium size) **1B.** Icon (`24×24px`, color `var(--secondary-50)`) **1C.** No prefix |
| 2 | **Centre** | **Heading Title** (Mandatory): `$list/list-title` → `var(--text-base)` · `var(--font-weight-medium)` · color `var(--grey-100)`. **SubText** (Optional): `$body/xs` → `var(--text-body-xs)` · `var(--font-weight-normal)` · color `var(--grey-80)`. |
| 3 | **Suffix** (Non-editable) | Button/Tertiary Medium (`40×40px` touch target). **Collapsed:** `IcChevronDown` or `IcAdd`. **Expanded:** `IcChevronUp` or `IcMinus`. Icon size: `24×24px` (`var(--space-6)`), color: `var(--secondary-50)`. |
| 4 | **Item Border** | `border-bottom: 1px solid var(--grey-40)` on each `AccordionItem`. Provides visual separation between items. |

### Spacing

| Element | Token | CSS Variable | Value |
|---------|-------|-------------|-------|
| Prefix ↔ Centre ↔ Suffix gap | `$space/3` | `var(--space-3)` | `12px` |
| Trigger vertical padding | `$space/4` | `var(--space-4)` | `16px` |
| Content bottom padding | `$space/4` | `var(--space-4)` | `16px` |
| SubText top margin | `$space/1` | `var(--space-1)` | `4px` |
| Suffix touch target | `$space/10` | `var(--space-10)` | `40px` |

---

## 3. States

| State | Behavior |
|-------|----------|
| **Collapsed** | Default. Only header row visible. Trailing icon: down chevron / plus. |
| **Expanded** | Content area slides open (200ms ease-in-out). Trailing icon swaps to up chevron / minus. |
| **Hover** | Background: `var(--grey-20)` (Surface-Hover token) on trigger area. |
| **Focused** | `outline: 2px solid var(--primary-50)`, offset `2px`. Keyboard navigation via `Tab`. |
| **Pressed** | Visual feedback on click/tap (hover state + browser default). |
| **Disabled** | `opacity: 0.3`, `pointer-events: none`. |

---

## 4. Variants

| Variant | Prefix | Title | SubText | Suffix |
|---------|--------|-------|---------|--------|
| **Standard** | — | ✅ | — | ✅ Chevron/Plus |
| **Informational** | — | ✅ | ✅ | ✅ Chevron/Plus |
| **Visual** | ✅ Icon/Avatar | ✅ | — | ✅ Chevron/Plus |
| **Full Detail** | ✅ Icon/Avatar | ✅ | ✅ | ✅ Chevron/Plus |

**Auto-detection:** If `variant` prop is omitted, the component infers the variant from the combination of `prefix` and `subText` props provided.

### Suffix Icon Modes

| Mode | Collapsed Icon | Expanded Icon |
|------|---------------|---------------|
| `"chevron"` (default) | `IcChevronDown` | `IcChevronUp` |
| `"plusminus"` | `IcAdd` (+) | `IcMinus` (−) |

---

## 5. Expansion Logic

| Mode | Behavior | Best For |
|------|----------|----------|
| **Single-expand** (`type="single"`) | Opening one item closes any other open item. Use `collapsible={true}` to allow fully closing all. | FAQs |
| **Multi-expand** (`type="multiple"`) | Users can open multiple items simultaneously. | Settings, Filters |

---

## 6. Responsive Behavior

- **Text Wrapping:** Title and SubText wrap naturally when they exceed the container width. The header height expands to accommodate (Hug Contents). Titles must NOT be truncated.
- **Width:** The Accordion should use `w-full` (Fill Container) to adapt to its parent's width — whether full-width or constrained within a column layout.

---

## 7. Animation

- **Duration:** `200ms`
- **Easing:** `ease-in-out`
- **Property:** Content area height (open/close via `animate-accordion-down` / `animate-accordion-up`)
- **Icon swap:** Instant (no rotation animation — discrete icon swap via `data-state` selector)

---

## 8. Accessibility (A11y)

| Requirement | Implementation |
|-------------|---------------|
| **Keyboard** | Navigate headers with `Tab`. Toggle with `Enter` or `Space`. |
| **Screen Readers** | `aria-expanded="true/false"` communicates state. `aria-controls` links header to content panel. (Handled by Radix UI Accordion primitive.) |
| **Contrast** | Header text meets WCAG 4.5:1 contrast ratio. `var(--grey-100)` on `var(--global-white)` = compliant. |
| **Focus Ring** | `outline: 2px solid var(--primary-50)` with `2px` offset. |
| **Clickable Area** | The entire header row is clickable, not just the chevron icon. |

---

## 9. Designer Guidelines (Do's & Don'ts)

- ✅ **Do:** Group related content logically.
- ✅ **Do:** Use clear, descriptive titles so users can predict what's inside.
- ✅ **Do:** Use the `AccordionGroup` convenience component for standard lists (FAQs, settings).
- ❌ **Don't Nest:** Avoid placing an Accordion inside another Accordion. Creates confusing "Nested Drawer" UX.
- ❌ **Don't use for Critical Info:** If users must read content to complete a task, do not hide it in an accordion.
- ❌ **Don't truncate titles:** Long titles must wrap, never truncate.

---

## 10. Token Reference

### Typography

| Element | Token | CSS Variable | Value |
|---------|-------|-------------|-------|
| Heading Title | `$list/list-title` | `var(--text-base)` | `16px` |
| Title weight | `$font-weight/medium` | `var(--font-weight-medium)` | `500` |
| SubText | `$body/xs` | `var(--text-body-xs)` | `14px` |
| SubText weight | `$font-weight/normal` | `var(--font-weight-normal)` | `400` |
| Content text | `$body/xs` | `var(--text-body-xs)` | `14px` |
| Content weight | `$font-weight/normal` | `var(--font-weight-normal)` | `400` |

### Colors

| Element | Token | CSS Variable | Value |
|---------|-------|-------------|-------|
| Title color | `$theme/primary/grey-100` | `var(--grey-100)` | `#141414` |
| SubText color | `$theme/primary/grey-80` | `var(--grey-80)` | `#000000a6` |
| Content color | `$theme/primary/grey-80` | `var(--grey-80)` | `#000000a6` |
| Suffix icon color | `$theme/secondary/50` | `var(--secondary-50)` | `#000093` |
| Hover background | Surface-Hover | `var(--grey-20)` | `#F5F5F5` |
| Item border | `$theme/grey/40` | `var(--grey-40)` | `#E0E0E0` |
| Focus ring | `$theme/primary/50` | `var(--primary-50)` | `#0F3CC9` |

### Spacing

| Element | Token | CSS Variable | Value |
|---------|-------|-------------|-------|
| Prefix–Centre–Suffix gap | `$space/3` | `var(--space-3)` | `12px` |
| Trigger vertical padding | `$space/4` | `var(--space-4)` | `16px` |
| Content bottom padding | `$space/4` | `var(--space-4)` | `16px` |
| SubText top margin | `$space/1` | `var(--space-1)` | `4px` |
| Suffix touch target | `$space/10` | `var(--space-10)` | `40px` |
| Icon size | `$space/6` | `var(--space-6)` | `24px` |

---

## 11. API Reference

### `<Accordion>` (Root)

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `"single" \| "multiple"` | — | Expansion mode (required). |
| `collapsible` | `boolean` | `true` | (Single only) Allow fully collapsing all items. |
| `suffixIcon` | `"chevron" \| "plusminus"` | `"chevron"` | Trailing icon style — applies to all items. |
| `defaultValue` | `string \| string[]` | — | Initially expanded item(s). |
| `value` | `string \| string[]` | — | Controlled expanded item(s). |
| `onValueChange` | `function` | — | Callback when expanded items change. |
| `disabled` | `boolean` | `false` | Disable all items. |
| `className` | `string` | — | Additional CSS classes. |

### `<AccordionItem>`

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | — | Unique identifier (required). |
| `disabled` | `boolean` | `false` | Disable this specific item. |
| `className` | `string` | — | Additional CSS classes. |

### `<AccordionTrigger>`

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | `string` | — | Heading title (required). |
| `subText` | `string` | — | Helper text below title. |
| `prefix` | `ReactNode` | — | Icon or Avatar component. |
| `variant` | `AccordionVariant` | Auto-detected | Force a specific variant. |
| `className` | `string` | — | Additional CSS classes. |

### `<AccordionContent>`

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | Content shown when expanded. |
| `className` | `string` | — | Additional CSS classes for inner wrapper. |

### `<AccordionGroup>` (Convenience)

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `items` | `AccordionItemData[]` | — | Array of item configs (required). |
| `type` | `"single" \| "multiple"` | `"single"` | Expansion mode. |
| `suffixIcon` | `"chevron" \| "plusminus"` | `"chevron"` | Trailing icon style. |
| `collapsible` | `boolean` | `true` | Allow fully collapsing (single mode). |
| `defaultValue` | `string \| string[]` | — | Initially expanded item(s). |
| `className` | `string` | — | Additional CSS classes. |

#### `AccordionItemData` shape

```ts
interface AccordionItemData {
  value: string;           // Unique key
  title: string;           // Heading text
  subText?: string;        // Helper text
  prefix?: ReactNode;      // Icon or Avatar
  content: ReactNode;      // Expandable content
  disabled?: boolean;      // Disable this item
}
```

---

## 12. Usage Examples

### Standard (FAQ) — Using AccordionGroup

```tsx
import { AccordionGroup } from './components/ui/accordion';

<AccordionGroup
  type="single"
  collapsible
  suffixIcon="chevron"
  items={[
    { value: 'q1', title: 'What is Jio?', content: 'Jio is India\'s leading digital services platform.' },
    { value: 'q2', title: 'How do I recharge?', content: 'Visit jio.com or use the MyJio app.' },
  ]}
/>
```

### Informational — With SubText

```tsx
<AccordionGroup
  type="single"
  suffixIcon="plusminus"
  items={[
    {
      value: 'plan',
      title: 'Plan Details',
      subText: 'View your current plan benefits',
      content: 'Unlimited data, calls, and SMS for 84 days.',
    },
  ]}
/>
```

### Visual — With Icon Prefix

```tsx
import { Icon } from './components/ui/icon';
import { IcSettings } from '@jds/core-icons';

<AccordionGroup
  type="multiple"
  items={[
    {
      value: 'settings',
      title: 'Account Settings',
      prefix: <Icon ic={IcSettings} size="md" color="var(--secondary-50)" />,
      content: 'Manage your account preferences here.',
    },
  ]}
/>
```

### Full Detail — With Avatar Prefix + SubText

```tsx
import { Avatar, AvatarImage, AvatarFallback } from './components/ui/avatar';

<AccordionGroup
  type="single"
  items={[
    {
      value: 'profile',
      title: 'John Doe',
      subText: 'Premium subscriber since 2023',
      prefix: (
        <Avatar className="size-10">
          <AvatarImage src="/avatar.jpg" alt="John" />
          <AvatarFallback>JD</AvatarFallback>
        </Avatar>
      ),
      content: 'Profile details and subscription information.',
    },
  ]}
/>
```

### Composable API (Low-level)

```tsx
import {
  Accordion,
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from './components/ui/accordion';

<Accordion type="single" collapsible suffixIcon="chevron">
  <AccordionItem value="item-1">
    <AccordionTrigger title="Is it accessible?" />
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA Accordion pattern.
    </AccordionContent>
  </AccordionItem>
  <AccordionItem value="item-2">
    <AccordionTrigger
      title="Is it styled?"
      subText="Uses JDS design tokens"
    />
    <AccordionContent>
      Yes. Styled with CSS variables from the JDS design system.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

### In a Section (BusinessFAQ pattern)

```tsx
import { AccordionGroup } from './components/ui/accordion';
import { SectionHeading, SectionSupportText } from './SectionHeading';

<section className="w-full section-padding" style={{ backgroundColor: 'var(--global-white)' }}>
  <div className="container mx-auto">
    <SectionHeading>Frequently asked questions</SectionHeading>
    <SectionSupportText>Everything you need to know.</SectionSupportText>
    <div className="mx-auto" style={{ maxWidth: '800px', marginTop: 'var(--space-10)' }}>
      <AccordionGroup
        type="single"
        collapsible
        suffixIcon="chevron"
        items={faqItems}
      />
    </div>
  </div>
</section>
```

---

## 13. Changelog

- **2026-02-25 (v2):** Refined component — fixed text wrapping (removed truncation), simplified divider to `border-bottom` on items, removed redundant `AccordionDivider` export, cleaned up content padding, all sizing uses CSS variable tokens (`var(--space-6)` etc.), added `AccordionItemData` shape docs, added section usage example.
- **2026-02-25 (v1):** Initial JDS-compliant specification created with all 4 variants, states, accessibility, and token mapping.
