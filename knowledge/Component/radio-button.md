# Radio Button — JDS Component Style Guide

## Overview

**Definition:** A radio button allows users to select exactly one option from a set of mutually exclusive choices. Selecting a new item automatically deselects the previously selected one.

**Core Principles:**
- **Mutual Exclusivity:** Only one option in a group can be active
- **Selection Persistence:** Once a selection is made, a radio group usually cannot be returned to an unselected state without a reset or "None" option
- **Default Selection:** It is recommended to have a default option pre-selected to guide the user

Component: `/src/app/components/ui/radio-group.tsx`

---

## When to Use

### ✅ Use Radio Buttons When:
- Users need to see all available options at once to make a decision
- For binary choices that are opposites (e.g., Yes/No)
- For a small set of related but mutually exclusive options (typically 2–5)

### ❌ Do NOT Use Radio Buttons When:
- **Toggle Switch:** Use a toggle for on/off settings
- **Dropdown:** Use a dropdown if the list of options is long (more than 5) to save space
- **Checkbox:** Use checkboxes if multiple selections are allowed

---

## Anatomy

The Radio Button is composed of three primary layers:

1. **Radio Button (Control):** The visual circular input indicator
   - **Control Pill:** The outer circle
   - **Control Switch (Dot):** The inner filled circle when selected
2. **Label Text:** The descriptive text for the option (positioned to the right of the control)
3. **Helper Text (Optional):** Additional context or description placed beneath the label

---

## Sizes

### Default (24px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Control pill**       | 24px diameter (follows label line height) |
| **Control switch (dot)** | 12px diameter                        |
| **Dot padding from pill** | 6px (inset)                         |
| **Label**              | `$body-s` (`var(--text-body-s)` — 16px) |
| **Helper text**        | `$body-xs` (`var(--text-body-xs)` — 14px) |
| **Spacing**            | 8px (`var(--space-2)`) between control pill & label |

### Small (16px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Control pill**       | 16px diameter (follows label line height) |
| **Control switch (dot)** | 8px diameter                         |
| **Dot padding from pill** | 4px (inset)                         |
| **Label**              | `$body-xs` (`var(--text-body-xs)` — 14px) |
| **Helper text**        | `$body-xs` (`var(--text-body-xs)` — 14px) |
| **Spacing**            | 8px (`var(--space-2)`) between control pill & label |

---

## States

Radio buttons support **18 state combinations** across two conditions: **Rest (Unselected)** and **Active (Selected)**, each with 9 states.

### Rest States (Unselected)

#### Rest / Normal

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-80)` (#000000a6)          |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 1px solid `var(--grey-80)`          |
| Control pill background | transparent                     |
| Control switch    | none                                   |

#### Rest / Hover

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 1px solid `var(--primary-50)`       |
| Control pill background | transparent                     |
| Control switch    | none                                   |

#### Rest / Pressed

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-80)` (#000000a6)          |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--primary-40)` (#6789F4)   |
| Control switch    | none                                   |

#### Rest / Focus

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 4px solid `var(--primary-80)` (outside) |
| Control pill background | `var(--primary-40)` (#6789F4)   |
| Control switch    | none                                   |

#### Rest / Disabled

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| General appearance | Same as Rest / Normal                 |
| General opacity   | **30%**                                |

#### Rest / Success

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-80)` (#000000a6)          |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 1px solid `var(--success-50)`       |
| Control pill background | transparent                     |
| Control switch    | none                                   |

#### Rest / Warning

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-80)` (#000000a6)          |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 1px solid `var(--warning-50)`       |
| Control pill background | transparent                     |
| Control switch    | none                                   |

#### Rest / Error

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-80)` (#000000a6)          |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 1px solid `var(--error-50)`         |
| Control pill background | transparent                     |
| Control switch    | none                                   |

---

### Active States (Selected)

#### Active / Normal

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--primary-50)` (#0F3CC9)   |
| Control switch    | `var(--primary-inverse)` (#FFFFFF)    |

#### Active / Hover

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--primary-60)` (#0A2885)   |
| Control switch    | `var(--primary-inverse)` (#FFFFFF)    |

#### Active / Pressed

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--primary-60)` (#0A2885)   |
| Control switch    | `var(--primary-40)` (#6789F4)         |

#### Active / Focus

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | 4px solid `var(--primary-80)` (outside) |
| Control pill background | `var(--primary-60)` (#0A2885)   |
| Control switch    | `var(--primary-inverse)` (#FFFFFF)    |

#### Active / Disabled

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| General appearance | Same as Active / Normal               |
| General opacity   | **30%**                                |

#### Active / Success

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--success-50)` (#25AB21)   |
| Control switch    | `var(--global-white)` (#FFFFFF)       |

#### Active / Warning

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--warning-50)` (#F06D0F)   |
| Control switch    | `var(--global-white)` (#FFFFFF)       |

#### Active / Error

| Element           | Specification                          |
| ----------------- | -------------------------------------- |
| Label color       | `var(--grey-100)` (#141414)           |
| Label font        | `$body-s` (16px for default)          |
| Control pill border | none                                |
| Control pill background | `var(--error-50)` (#FA2F40)     |
| Control switch    | `var(--global-white)` (#FFFFFF)       |

---

## Spacing

| Element                        | Spacing Value                      |
| ------------------------------ | ---------------------------------- |
| Control pill ↔ Label           | 8px (`var(--space-2)`)            |
| Radio item ↔ Radio item        | 12px (`var(--space-3)`)           |
| Label ↔ Helper text            | 8px (`var(--space-2)`)            |

---

## Behavioral Logic

### Text Overflow
- Labels should be concise (fewer than 3 words preferred)
- If long, text must wrap beneath the radio button so the control and label remain top-aligned
- **Never truncate radio labels with an ellipsis**

### Alignment

**Vertical (Recommended):**
- Preferred for scannability
- Limit to 5 options

**Horizontal:**
- Use only if there are 3 or fewer short options

**Mobile:**
- Always stack vertically

### Group Labeling
- Use "Sentence case" for group titles
- Do not use instructional phrases like "Select one of the following"

### Label-less Variant
- All variations should also work without a label
- Control pill can be used standalone where context is clear

---

## Accessibility (A11y)

### Markup
- Groups must be marked with `fieldset` and `legend` tags for screen reader context

### Target Area
- Both the radio control and the label text must be clickable to provide a larger, more accessible touch target

### Keyboard Navigation
- Users navigate between groups using **Tab**
- Within a group, use **Arrow Keys** (standard browser behavior) or **Space** to trigger selection

### ARIA Attributes
- `role="radiogroup"` on the group container
- `role="radio"` on each radio item
- `aria-checked="true|false"` for selection state
- `aria-disabled="true"` for disabled items
- `aria-describedby` for helper text association

---

## Usage Guidelines

### ✅ Do
- Select the most frequent or desired option as the default
- Arrange options in a logical order (e.g., simplest to most complex)
- Use both the radio control and label as clickable targets
- Keep labels concise and clear
- Use helper text for additional context when needed
- Use fieldset and legend for proper semantic structure
- Top-align control pill with multi-line labels

### ❌ Don't
- Center-align the radio button vertically with a multi-line label; always top-align
- Use radio buttons to trigger immediate "commands" or actions (like "Show toolbar"). Use them only for choosing options
- Use radio buttons for settings that are not mutually exclusive
- Use more than 5 options — consider a dropdown instead
- Truncate labels with ellipsis — allow text to wrap

---

## Code Examples

### Basic Radio Group

```tsx
import { RadioGroup, RadioGroupItem } from './ui/radio-group';
import { Label } from './ui/label';

function PaymentMethodSelector() {
  return (
    <RadioGroup defaultValue="upi">
      <div className="flex items-center gap-[var(--space-2)]">
        <RadioGroupItem value="upi" id="upi" />
        <Label htmlFor="upi">UPI</Label>
      </div>
      <div className="flex items-center gap-[var(--space-2)]">
        <RadioGroupItem value="card" id="card" />
        <Label htmlFor="card">Credit/Debit Card</Label>
      </div>
      <div className="flex items-center gap-[var(--space-2)]">
        <RadioGroupItem value="netbanking" id="netbanking" />
        <Label htmlFor="netbanking">Net Banking</Label>
      </div>
    </RadioGroup>
  );
}
```

### Radio Group with Fieldset

```tsx
<fieldset>
  <legend className="font-[family-name:var(--font-family-jiotype)] font-[var(--font-weight-medium)] text-[length:var(--text-body-s)] mb-[var(--space-3)]">
    Choose your subscription plan
  </legend>
  <RadioGroup defaultValue="monthly">
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="monthly" id="monthly" />
      <Label htmlFor="monthly">Monthly - ₹199/month</Label>
    </div>
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="quarterly" id="quarterly" />
      <Label htmlFor="quarterly">Quarterly - ₹499/3 months</Label>
    </div>
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="annual" id="annual" />
      <Label htmlFor="annual">Annual - ₹1,799/year (Save 25%)</Label>
    </div>
  </RadioGroup>
</fieldset>
```

### Radio Group with Helper Text

```tsx
<RadioGroup defaultValue="yes">
  <div className="flex items-start gap-[var(--space-2)]">
    <RadioGroupItem value="yes" id="yes" className="mt-1" />
    <div className="flex flex-col gap-[var(--space-2)]">
      <Label htmlFor="yes">Yes, send me updates</Label>
      <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--grey-80)]">
        You'll receive occasional product updates and newsletters
      </p>
    </div>
  </div>
  <div className="flex items-start gap-[var(--space-2)]">
    <RadioGroupItem value="no" id="no" className="mt-1" />
    <div className="flex flex-col gap-[var(--space-2)]">
      <Label htmlFor="no">No, don't send me updates</Label>
      <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--grey-80)]">
        You won't receive any marketing communications
      </p>
    </div>
  </div>
</RadioGroup>
```

### Small Size Radio Group

```tsx
<RadioGroup defaultValue="option1">
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="option1" id="option1" size="small" />
    <Label htmlFor="option1" className="text-[length:var(--text-body-xs)]">Option 1</Label>
  </div>
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="option2" id="option2" size="small" />
    <Label htmlFor="option2" className="text-[length:var(--text-body-xs)]">Option 2</Label>
  </div>
</RadioGroup>
```

### Disabled Radio Button

```tsx
<RadioGroup defaultValue="available">
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="available" id="available" />
    <Label htmlFor="available">Available</Label>
  </div>
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="unavailable" id="unavailable" disabled />
    <Label htmlFor="unavailable" className="opacity-30">
      Unavailable (Coming Soon)
    </Label>
  </div>
</RadioGroup>
```

### Feedback State Examples

#### Success State

```tsx
<fieldset>
  <legend className="font-[family-name:var(--font-family-jiotype)] font-[var(--font-weight-medium)] text-[length:var(--text-body-s)] text-[color:var(--success-60)] mb-[var(--space-3)]">
    Payment verified
  </legend>
  <RadioGroup defaultValue="saved">
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="saved" id="saved" feedback="success" />
      <Label htmlFor="saved">Use saved card</Label>
    </div>
  </RadioGroup>
</fieldset>
```

#### Warning State

```tsx
<RadioGroup>
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="limited" id="limited" feedback="warning" />
    <Label htmlFor="limited">Limited stock available</Label>
  </div>
</RadioGroup>
```

#### Error State

```tsx
<fieldset className="border-[length:var(--border-width-thin)] border-[color:var(--error-50)] rounded-[var(--radius-md)] p-[var(--space-4)]">
  <legend className="font-[family-name:var(--font-family-jiotype)] font-[var(--font-weight-medium)] text-[length:var(--text-body-s)] text-[color:var(--error-80)]">
    Choose a delivery option
  </legend>
  <RadioGroup>
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="standard" id="standard" feedback="error" />
      <Label htmlFor="standard">Standard Delivery</Label>
    </div>
    <div className="flex items-center gap-[var(--space-2)]">
      <RadioGroupItem value="express" id="express" feedback="error" />
      <Label htmlFor="express">Express Delivery</Label>
    </div>
  </RadioGroup>
  <p className="font-[family-name:var(--font-family-jiotype)] text-[length:var(--text-body-xs)] text-[color:var(--error-80)] mt-[var(--space-2)]">
    Please select a delivery option to continue
  </p>
</fieldset>
```

### Label-less Radio (Standalone Control)

```tsx
<RadioGroup defaultValue="option1" className="flex flex-row gap-[var(--space-4)]">
  <RadioGroupItem value="option1" id="option1" aria-label="Option 1" />
  <RadioGroupItem value="option2" id="option2" aria-label="Option 2" />
  <RadioGroupItem value="option3" id="option3" aria-label="Option 3" />
</RadioGroup>
```

---

## Design Tokens Used — Summary

### Colors

| Token                | Usage                                  |
| -------------------- | -------------------------------------- |
| `--grey-80`          | Rest label, rest border                |
| `--grey-100`         | Active label, hover label              |
| `--primary-40`       | Rest pressed/focus background          |
| `--primary-50`       | Active background, hover border        |
| `--primary-60`       | Active hover/pressed background        |
| `--primary-80`       | Focus ring (4px outside)               |
| `--primary-inverse`  | Active control switch (white dot)      |
| `--global-white`     | Success/Warning/Error active switch    |
| `--success-50`       | Success state border/background        |
| `--warning-50`       | Warning state border/background        |
| `--error-50`         | Error state border/background          |

### Typography

| Token                   | Usage                           |
| ----------------------- | ------------------------------- |
| `--font-family-jiotype` | All text (label, helper)        |
| `--font-weight-medium`  | Label text (500)                |
| `--text-body-s`         | Default size label (16px)       |
| `--text-body-xs`        | Small size label, helper (14px) |

### Spacing

| Token        | Usage                                      |
| ------------ | ------------------------------------------ |
| `--space-2`  | Gap between radio and label (8px)         |
| `--space-3`  | Gap between radio items (12px)            |

### Border

| Token                 | Usage                          |
| --------------------- | ------------------------------ |
| `--border-width-thin` | Rest state border (1px)        |

### Sizes

| Size    | Control Diameter | Dot Diameter | Dot Inset |
| ------- | ---------------- | ------------ | --------- |
| Default | 24px             | 12px         | 6px       |
| Small   | 16px             | 8px          | 4px       |

---

## Related Components

- **Checkbox** — Use for multiple selections
- **Toggle Switch** — Use for on/off settings
- **Select/Dropdown** — Use when options exceed 5
- **Tabs** — Use for switching between views/content sections
- **Button Group** — Use for mutually exclusive actions
- **Selector** — Use for larger touch targets with visual previews

---

## Migration Guide

If migrating from the old RadioGroup component:

**Before:**
```tsx
<RadioGroup value={selected}>
  <RadioGroupItem value="option1" />
  <span>Option 1</span>
</RadioGroup>
```

**After:**
```tsx
<RadioGroup value={selected}>
  <div className="flex items-center gap-[var(--space-2)]">
    <RadioGroupItem value="option1" id="option1" />
    <Label htmlFor="option1">Option 1</Label>
  </div>
</RadioGroup>
```

**Key Changes:**
- Always wrap RadioGroupItem + Label in a flex container with `gap-[var(--space-2)]`
- Use `id` and `htmlFor` to properly link radio and label
- Use Label component instead of plain text/span
- Add `size` prop for small variant
- Use `feedback` prop for success/warning/error states
- Maintain consistent spacing with design tokens
- All CSS values use `var()` for design system adherence
