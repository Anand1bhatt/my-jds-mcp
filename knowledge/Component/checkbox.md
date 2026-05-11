# Checkbox — JDS Component Style Guide

## Overview

**Definition:** Checkboxes allow users to select one or more items from a list, or toggle a single independent setting that requires a submission step (e.g., "Agree to terms").

**Core Principle:** Each checkbox is independent. Selecting one does not affect the state of others in the same group.

Component: `/src/app/components/ui/checkbox.tsx`

---

## When to Use

### ✅ Use Checkbox When:
- Users can select multiple options
- You need to filter data in a table/list
- A single option needs to be explicitly submitted

### ❌ Do NOT Use Checkbox When:
- Options are mutually exclusive (Use Radio Button)
- Action should be applied immediately (Use Toggle Switch)
- You want to save space and have >6 options (Use Dropdown)

---

## Anatomy

The Checkbox component consists of:

1. **Checkbox (Control):** The square visual indicator
   - **Control Box:** The outer square container
   - **Control Icon:** The checkmark (Active) or minus (Indeterminate) icon
2. **Label Text:** Descriptive text positioned to the right of the control
3. **Helper Text (Optional):** Provides additional context beneath the label
4. **Feedback Block (Optional):** Displays validation messages (Success/Warning/Error)

---

## Kinds & States

### Kinds

| Kind | Description | Icon |
|------|-------------|------|
| **Rest** | The neutral, unselected state | None |
| **Active** | The state when the user has selected the checkbox | `ic_confirm` (checkmark) |
| **Indeterminate** | A visual state for parent checkboxes when only some (but not all) child items are selected | `ic_minus` (dash) |

### States

| State | Description |
|-------|-------------|
| **Normal** | Default interactive view |
| **Hover** | Visual feedback for mouse interaction |
| **Pressed** | Visual feedback for active press/touch |
| **Focused** | Highlighted for keyboard (Tab) navigation |
| **Disabled** | Non-interactive and de-emphasized (30% opacity) |
| **Success** | Validation state with green accent |
| **Warning** | Validation state with orange accent |
| **Error** | Validation state with red accent |

**Total State Combinations:** 18 states (9 Rest states + 9 Active states)

---

## Sizes

### Default (24px)

| Element | Specification |
|---------|---------------|
| **Control box** | 24px × 24px |
| **Control box radius** | 8px (`var(--radius)`) |
| **Control box padding** | 2px (internal padding for icon) |
| **Control icon** | 16px × 16px |
| **Label** | `$body-s` (`var(--text-body-s)` — 16px) |
| **Helper text** | `$body-s` (`var(--text-body-s)` — 16px) |
| **Spacing** | 8px (`var(--space-2)`) between control & label |

### Small (16px)

| Element | Specification |
|---------|---------------|
| **Control box** | 16px × 16px |
| **Control box radius** | 8px (`var(--radius)`) |
| **Control box padding** | 2px (internal padding for icon) |
| **Control icon** | 12px × 12px |
| **Label** | `$body-xs` (`var(--text-body-xs)` — 14px) |
| **Helper text** | `$body-xs` (`var(--text-body-xs)` — 14px) |
| **Spacing** | 8px (`var(--space-2)`) between control & label |

---

## State Specifications

### Rest States (Unselected)

All states apply to both Active (uses `ic_confirm`) and Indeterminate (uses `ic_minus`).

#### Rest / Normal

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-80)` (#000000a6) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--grey-80)` |
| Control box background | transparent (none) |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Hover

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--primary-40)` (#6789F4) |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Pressed

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--primary-60)` (#0A2885) |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Focused

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 4px solid `var(--primary-60)` (outside) |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Disabled

| Element | Specification |
|---------|---------------|
| General appearance | Same as Rest / Normal |
| General opacity | **30%** |

#### Rest / Success

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-80)` (#000000a6) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--grey-80)` |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Warning

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-80)` (#000000a6) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--grey-80)` |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Rest / Error

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-80)` (#000000a6) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 1px solid `var(--grey-80)` |
| Control box background | none |
| Control icon | none |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

---

### Active States (Selected & Indeterminate)

Properties apply to both **Active** (checked, uses `ic_confirm`) and **Indeterminate** (uses `ic_minus`) states.

#### Active / Normal

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-50)` (#0F3CC9) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Hover

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-40)` (#6789F4) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Pressed

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-60)` (#0A2885) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Focused

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | 4px solid `var(--primary-60)` (outside) |
| Control box background | `var(--primary-50)` (#0F3CC9) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Disabled

| Element | Specification |
|---------|---------------|
| General appearance | Same as Active / Normal |
| General opacity | **30%** |

#### Active / Success

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-50)` (#0F3CC9) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Warning

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-50)` (#0F3CC9) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

#### Active / Error

| Element | Specification |
|---------|---------------|
| Label color | `var(--grey-100)` (#141414) |
| Label font | `$body-s` (16px for default, 14px for small) |
| Control box border | none |
| Control box background | `var(--primary-50)` (#0F3CC9) |
| Control icon | `var(--primary-inverse)` (#FFFFFF) |
| Helper text color | `var(--grey-80)` |
| Helper text font | `$body-s` (16px for default, 14px for small) |

---

## Spacing

| Element | Spacing Value |
|---------|---------------|
| Control box ↔ Label | 8px (`var(--space-2)`) |
| Checkbox ↔ Feedback block | 8px (`var(--space-2)`) |
| Feedback block ↔ Helper block | 8px (`var(--space-2)`) |

---

## Behavioral Logic

### Parent-Child Relationship

**Bulk Selection:**
- Checking a parent checkbox automatically selects all children

**Indeterminate Logic:**
- If a subset of children is selected, the parent must display the Indeterminate kind (using `ic_minus` icon)

**Sub-selection Alignment:**
- Child controls should be left-aligned with the parent's label (indented)

### Text Overflow & Wrapping

**No Truncation:**
- Never use an ellipsis (...) for checkbox labels

**Wrapping Rule:**
- Long labels must wrap to a second line

**Alignment:**
- Wrapped text must flow beneath the checkbox control so that the control and the first line of text remain top-aligned

---

## Alignment & Layout

**Orientation:**
- **Vertical stacking** is preferred for scannability

**Vertical Limit:**
- Limit to 5–6 items per column
- If there are more, use multiple columns

**Horizontal:**
- Use only for short, binary choices (max 2 options)

**Mobile:**
- Always use a vertical stack (stacked)

---

## Accessibility (A11y)

### Grouping
- Always wrap checkbox groups in a `<fieldset>` with a `<legend>` as the group label

### Interactive Target
- Both the checkbox control and the label text must be interactive to provide a large touch target

### Screen Readers
- Labels must be announced on focus
- For parent-child sets, the relationship must be defined via ARIA attributes

### ARIA Attributes
- `role="group"` on the checkbox group container (or use `<fieldset>`)
- `aria-checked="true|false|mixed"` for selection state (mixed = indeterminate)
- `aria-disabled="true"` for disabled items
- `aria-describedby` for helper text and feedback message association
- `aria-labelledby` for proper label association

### Keyboard Navigation
- Users navigate between checkboxes using **Tab** and **Shift+Tab**
- **Space** toggles the checkbox on/off
- **Enter** can also toggle (in some contexts)

---

## Usage Guidelines

### ✅ Do
- Use positive phrasing for labels (e.g., "Send me updates" vs. "Don't send me updates")
- Place the most common options first in a group
- Both the checkbox control and the label should be clickable
- Allow labels to wrap if they exceed one line
- Top-align the checkbox control with multi-line labels
- Use fieldset and legend for proper semantic structure
- Use helper text for additional context
- Use feedback states (success/warning/error) for validation

### ❌ Don't
- Center-align the control vertically with multi-line labels (always top-align)
- Use checkboxes for mutually exclusive settings (use radio buttons instead)
- Truncate checkbox labels with ellipsis
- Use more than 5–6 options in a single column without multi-column layout
- Use checkboxes for immediate actions (use toggle switch instead)

---

## Code Examples

### Basic Checkbox

```tsx
import { Checkbox } from './ui/checkbox';
import { Label } from './ui/label';

function NewsletterSubscription() {
  return (
    <div className="flex items-center gap-[var(--space-2)]">
      <Checkbox id="newsletter" />
      <Label htmlFor="newsletter">Subscribe to newsletter</Label>
    </div>
  );
}
```

### Checkbox Group with Fieldset

```tsx
<fieldset>
  <legend className="font-[family-name:var(--font-family-jiotype)] font-[var(--font-weight-medium)] text-[length:var(--text-body-s)] mb-[var(--space-3)]">
    Select your interests
  </legend>
  <div className="flex flex-col gap-[var(--space-2)]">
    <div className="flex items-center gap-[var(--space-2)]">
      <Checkbox id="sports" />
      <Label htmlFor="sports">Sports</Label>
    </div>
    <div className="flex items-center gap-[var(--space-2)]">
      <Checkbox id="entertainment" />
      <Label htmlFor="entertainment">Entertainment</Label>
    </div>
    <div className="flex items-center gap-[var(--space-2)]">
      <Checkbox id="news" />
      <Label htmlFor="news">News</Label>
    </div>
  </div>
</fieldset>
```

### Checkbox with Helper Text

```tsx
<div className="flex flex-col gap-[var(--space-2)]">
  <div className="flex items-start gap-[var(--space-2)]">
    <Checkbox id="terms" className="mt-1" />
    <div className="flex flex-col gap-[var(--space-2)]">
      <Label htmlFor="terms">I agree to the terms and conditions</Label>
      <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--grey-80)]">
        You must accept the terms to continue
      </p>
    </div>
  </div>
</div>
```

### Small Size Checkbox

```tsx
<div className="flex items-center gap-[var(--space-2)]">
  <Checkbox id="compact-option" size="small" />
  <Label htmlFor="compact-option" className="text-[length:var(--text-body-xs)]">
    Compact option
  </Label>
</div>
```

### Disabled Checkbox

```tsx
<div className="flex items-center gap-[var(--space-2)]">
  <Checkbox id="disabled-option" disabled />
  <Label htmlFor="disabled-option" className="opacity-30">
    Unavailable option
  </Label>
</div>
```

### Indeterminate Checkbox (Parent-Child)

```tsx
import { useState } from 'react';
import { Checkbox } from './ui/checkbox';
import { Label } from './ui/label';

function SelectAllExample() {
  const [checkedItems, setCheckedItems] = useState({
    option1: false,
    option2: false,
    option3: false,
  });

  const allChecked = Object.values(checkedItems).every(Boolean);
  const someChecked = Object.values(checkedItems).some(Boolean) && !allChecked;

  const handleSelectAll = () => {
    const newValue = !allChecked;
    setCheckedItems({
      option1: newValue,
      option2: newValue,
      option3: newValue,
    });
  };

  return (
    <div className="flex flex-col gap-[var(--space-2)]">
      <div className="flex items-center gap-[var(--space-2)]">
        <Checkbox
          id="select-all"
          checked={allChecked}
          indeterminate={someChecked}
          onCheckedChange={handleSelectAll}
        />
        <Label htmlFor="select-all">Select All</Label>
      </div>
      
      <div className="flex flex-col gap-[var(--space-2)] ml-[var(--space-6)]">
        <div className="flex items-center gap-[var(--space-2)]">
          <Checkbox
            id="option1"
            checked={checkedItems.option1}
            onCheckedChange={(checked) =>
              setCheckedItems({ ...checkedItems, option1: !!checked })
            }
          />
          <Label htmlFor="option1">Option 1</Label>
        </div>
        <div className="flex items-center gap-[var(--space-2)]">
          <Checkbox
            id="option2"
            checked={checkedItems.option2}
            onCheckedChange={(checked) =>
              setCheckedItems({ ...checkedItems, option2: !!checked })
            }
          />
          <Label htmlFor="option2">Option 2</Label>
        </div>
        <div className="flex items-center gap-[var(--space-2)]">
          <Checkbox
            id="option3"
            checked={checkedItems.option3}
            onCheckedChange={(checked) =>
              setCheckedItems({ ...checkedItems, option3: !!checked })
            }
          />
          <Label htmlFor="option3">Option 3</Label>
        </div>
      </div>
    </div>
  );
}
```

### Feedback State Examples

#### Success State

```tsx
<div className="flex flex-col gap-[var(--space-2)]">
  <div className="flex items-center gap-[var(--space-2)]">
    <Checkbox id="verified" checked feedback="success" />
    <Label htmlFor="verified">Email verified</Label>
  </div>
  <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--success-80)]">
    Your email has been successfully verified
  </p>
</div>
```

#### Warning State

```tsx
<div className="flex flex-col gap-[var(--space-2)]">
  <div className="flex items-center gap-[var(--space-2)]">
    <Checkbox id="storage" feedback="warning" />
    <Label htmlFor="storage">Enable cloud storage</Label>
  </div>
  <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--warning-80)]">
    Limited storage space remaining
  </p>
</div>
```

#### Error State

```tsx
<div className="flex flex-col gap-[var(--space-2)]">
  <div className="flex items-center gap-[var(--space-2)]">
    <Checkbox id="required-terms" feedback="error" />
    <Label htmlFor="required-terms">I agree to terms</Label>
  </div>
  <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--error-80)]">
    You must accept the terms to continue
  </p>
</div>
```

### Label-less Checkbox (Standalone Control)

```tsx
<div className="flex gap-[var(--space-4)]">
  <Checkbox id="standalone1" aria-label="Option 1" />
  <Checkbox id="standalone2" aria-label="Option 2" />
  <Checkbox id="standalone3" aria-label="Option 3" />
</div>
```

---

## Design Tokens Used — Summary

### Colors

| Token | Usage |
|-------|-------|
| `--grey-80` | Rest label, rest border, helper text |
| `--grey-100` | Active/Hover label |
| `--primary-40` | Rest hover border, Active hover background |
| `--primary-50` | Active background |
| `--primary-60` | Rest pressed border, Active pressed background, Focus ring |
| `--primary-inverse` | Active icon color (white) |
| `--success-80` | Success feedback text |
| `--warning-80` | Warning feedback text |
| `--error-80` | Error feedback text |

### Typography

| Token | Usage |
|-------|-------|
| `--font-family-jiotype` | All text (label, helper, feedback) |
| `--font-weight-medium` | Label text (500) |
| `--text-body-s` | Default size label, helper (16px) |
| `--text-body-xs` | Small size label, helper, feedback (14px) |

### Spacing

| Token | Usage |
|-------|-------|
| `--space-2` | Gap between checkbox and label (8px), vertical spacing |
| `--space-6` | Indentation for child checkboxes (24px) |

### Border & Radius

| Token | Usage |
|-------|-------|
| `--border-width-thin` | Rest state border (1px) |
| `--radius` | Control box border radius (8px) |

### Sizes

| Size | Control Box | Icon Size | Label Font |
|------|-------------|-----------|------------|
| Default | 24px × 24px | 16px × 16px | 16px (`$body-s`) |
| Small | 16px × 16px | 12px × 12px | 14px (`$body-xs`) |

---

## Related Components

- **Radio Button** — Use for mutually exclusive single selection
- **Toggle Switch** — Use for on/off settings with immediate effect
- **Select/Dropdown** — Use when options exceed 6
- **Selector** — Use for larger touch targets with visual previews

---

## Migration Guide

If migrating from the old Checkbox component:

**Before:**
```tsx
<Checkbox value={checked} />
<span>Accept terms</span>
```

**After:**
```tsx
<div className="flex items-center gap-[var(--space-2)]">
  <Checkbox id="terms" checked={checked} onCheckedChange={setChecked} />
  <Label htmlFor="terms">Accept terms</Label>
</div>
```

**Key Changes:**
- Always wrap Checkbox + Label in a flex container with `gap-[var(--space-2)]`
- Use `id` and `htmlFor` to properly link checkbox and label
- Use Label component instead of plain text/span
- Add `size` prop for small variant
- Use `feedback` prop for success/warning/error states
- Use `indeterminate` prop for parent checkboxes
- Maintain consistent spacing with design tokens
- All CSS values use `var()` for design system adherence
