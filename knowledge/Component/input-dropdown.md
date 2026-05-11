# Input-Dropdown Trigger — JDS Component Style Guide

## Overview

**Definition:** The Dropdown trigger allows users to select one or more options from a predefined list. It is an interactive input mechanism used to streamline user interaction, especially with lengthy lists.

**Purpose:** To help users filter and select desired options from a related list of items.

**Types:**
- **Single-Option Dropdown:** Allows selection of one item from the list
- **Multi-Select Dropdown:** Allows selection of multiple items, displayed as tags

**Kinds:**
- **Editable:** Users can type to filter options (includes type cursor)
- **Non-editable:** Users select options purely through clicking the menu

Component: `/src/app/components/ui/input-dropdown.tsx`

---

## When to Use

- **Use When:** The list contains more than 5 items, or when filtering/sorting is required.
- **Do NOT Use When:** The list is shorter than 5 items (use Radio Buttons or Checkboxes instead), or if the user needs to see all options at the same time.

---

## Anatomy

The component is composed of the following elements:

1. **Label (Optional):** Context for the field
2. **Label Asterisk (Optional):** Indicates required field
3. **Label Info Icon (Optional):** Tooltip for extra clarification
4. **Container:** The fluid-width bounding box
5. **Prefix Icon (Optional):** Icon before the value/placeholder
6. **Value/Placeholder:** The selected text or hint text
7. **Chevron Icon:** Indicates the dropdown state (flips vertically on active state)
8. **Close Icon (Active state only):** Clears input/selection
9. **Removable Tag (Multi-select):** Dismissible items with an 'X' icon
10. **Numeric Tag (Multi-select):** Non-dismissible count of additional selections (e.g., "+2")
11. **Helper Text (Optional):** Informational text below the container
12. **Feedback:** Error messages below the container

---

## Variants

### 1. Single-Option Dropdown (Editable)

```tsx
<InputDropdown
  type="single"
  kind="editable"
  size="medium"
  label="Select City"
  placeholder="Search city..."
  options={[
    { value: "mumbai", label: "Mumbai" },
    { value: "delhi", label: "Delhi" },
    { value: "bangalore", label: "Bangalore" },
  ]}
  onChange={(value) => console.log(value)}
/>
```

### 2. Single-Option Dropdown (Non-editable)

```tsx
<InputDropdown
  type="single"
  kind="non-editable"
  size="medium"
  label="Select State"
  placeholder="Choose a state"
  options={[
    { value: "mh", label: "Maharashtra" },
    { value: "dl", label: "Delhi" },
    { value: "ka", label: "Karnataka" },
  ]}
  onChange={(value) => console.log(value)}
/>
```

### 3. Multi-Select Dropdown (Editable)

```tsx
<InputDropdown
  type="multi"
  kind="editable"
  size="medium"
  label="Select Skills"
  placeholder="Search skills..."
  options={[
    { value: "react", label: "React" },
    { value: "typescript", label: "TypeScript" },
    { value: "node", label: "Node.js" },
  ]}
  onChange={(values) => console.log(values)}
/>
```

### 4. Multi-Select Dropdown (Non-editable)

```tsx
<InputDropdown
  type="multi"
  kind="non-editable"
  size="medium"
  label="Select Categories"
  placeholder="Choose categories"
  options={[
    { value: "tech", label: "Technology" },
    { value: "health", label: "Healthcare" },
    { value: "finance", label: "Finance" },
  ]}
  onChange={(values) => console.log(values)}
/>
```

### 5. Without Container

```tsx
<InputDropdown
  type="single"
  kind="non-editable"
  size="medium"
  appearance="without-container"
  placeholder="Select an option"
  options={[...]}
/>
```

### 6. With Error State

```tsx
<InputDropdown
  type="single"
  kind="editable"
  size="medium"
  label="City"
  required
  placeholder="Search city..."
  options={[...]}
  error="Please select a valid city"
/>
```

### 7. Disabled State

```tsx
<InputDropdown
  type="single"
  kind="non-editable"
  size="medium"
  label="Region"
  placeholder="Select region"
  options={[...]}
  disabled
/>
```

### 8. Read-only State

```tsx
<InputDropdown
  type="single"
  kind="non-editable"
  size="medium"
  label="Country"
  value="India"
  readOnly
  options={[...]}
/>
```

---

## Specifications

### Appearance: With Container

#### Large Size (48px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 48px (field only)                      |
| Label                  | `var(--text-body-s)` (16px)           |
| Label Asterisk         | `var(--text-body-s)` (16px)           |
| Label Info Icon        | Small (20px)                           |
| Prefix Icon            | 24px                                   |
| Tag                    | See Tag component UI blueprint         |
| Placeholder text       | `var(--text-body-m)` (18px)           |
| Cursor stroke          | 24px (1px, inside)                     |
| Suffix close icon btn  | Medium (active state only)             |
| Suffix chevron icon btn| Medium                                 |
| Container              | H-48px, W-depends on use              |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Feedback               | See Feedback Block UI Blueprint        |
| Helper text            | `var(--text-body-s)` (16px)           |

**Spacing:**
- Label -> DropdownInput -> HelperText -> Feedback: **4px** (`var(--space-1)`)
- Label with asterisk: **4px** (`var(--space-1)`)
- Prefix -> Tag -> Label & Suffix elements between: **12px** (`var(--space-3)`)
- Left & Right padding in InputDropdown: **16px** (`var(--space-4)`)

---

#### Medium Size (40px) -- Default

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 40px (field only)                      |
| Label                  | `var(--text-body-xs)` (14px)          |
| Label Asterisk         | `var(--text-body-xs)` (14px)          |
| Label Info Icon        | Small (20px)                           |
| Prefix Icon            | 24px                                   |
| Tag                    | See Tag component UI blueprint         |
| Placeholder text       | `var(--text-body-s)` (16px)           |
| Cursor stroke          | 20px (1px, inside)                     |
| Suffix close icon btn  | Medium (active state only)             |
| Suffix chevron icon btn| Medium                                 |
| Container              | H-40px, W-depends on use              |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Feedback               | See Feedback Block UI Blueprint        |
| Helper text            | `var(--text-body-s)` (16px)           |

**Spacing:**
- Label -> DropdownInput -> HelperText -> Feedback: **4px** (`var(--space-1)`)
- Label with asterisk: **4px** (`var(--space-1)`)
- Prefix -> Tag -> Label & Suffix elements between: **12px** (`var(--space-3)`)
- Left & Right padding in InputDropdown: **16px** (`var(--space-4)`)

---

#### Small Size (32px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 32px (field only)                      |
| Label                  | `var(--text-body-xs)` (14px)          |
| Label Asterisk         | `var(--text-body-xs)` (14px)          |
| Label Info Icon        | Small (20px)                           |
| Prefix Icon            | 16px                                   |
| Tag                    | See Tag component UI blueprint         |
| Placeholder text       | `var(--text-body-s)` (16px)           |
| Cursor stroke          | 20px (1px, inside)                     |
| Suffix close icon btn  | Medium (active state only)             |
| Suffix chevron icon btn| Small                                  |
| Container              | H-32px, W-depends on use              |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Feedback               | See Feedback Block UI Blueprint        |
| Helper text            | `var(--text-body-s)` (16px)           |

**Spacing:**
- Label -> DropdownInput -> HelperText -> Feedback: **4px** (`var(--space-1)`)
- Label with asterisk: **4px** (`var(--space-1)`)
- Prefix -> Tag -> Label & Suffix elements between: **12px** (`var(--space-3)`)
- Left & Right padding in InputDropdown: **12px** (`var(--space-3)`)

---

### Appearance: Without Container

#### Large Size (48px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 48px                                   |
| Placeholder text       | `var(--text-body-m)` (18px)           |
| Suffix chevron icon btn| Medium                                 |

#### Medium Size (40px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 40px                                   |
| Placeholder text       | `var(--text-body-s)` (16px)           |
| Suffix chevron icon btn| Medium                                 |

#### Small Size (32px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 32px                                   |
| Placeholder text       | `var(--text-body-s)` (16px)           |
| Suffix chevron icon btn| Small                                  |

**Without Container Spacing (With Padding):**
- Large: **12px** (`var(--space-3)`) Left & Right padding, label-chevron between
- Medium: **8px** (`var(--space-2)`) Left & Right padding, label-chevron between
- Small: **4px** (`var(--space-1)`) Left & Right padding, label-chevron between

**Without Container Spacing (Without Padding):**
- Large: **12px** (`var(--space-3)`) Label-chevron icon between
- Medium: **8px** (`var(--space-2)`) Label-chevron icon between
- Small: **4px** (`var(--space-1)`) Label-chevron icon between

---

## Visual States

### With Container

#### Default

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Placeholder text (editable) | `var(--grey-60)`                          |
| Placeholder text (non-edit) | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)` (background)        |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--grey-80)`                          |
| Helper                      | `var(--grey-80)`                          |

---

#### Hover

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Placeholder text (editable) | `var(--grey-60)`                          |
| Placeholder text (non-edit) | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--primary-60)` |
| Helper                      | `var(--grey-80)`                          |

---

#### Focus

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Placeholder text (editable) | `var(--grey-60)`                          |
| Placeholder text (non-edit) | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--primary-60)` |
| Helper                      | `var(--grey-80)`                          |

---

#### Active

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Tag                         | See Tag component UI blueprint             |
| Placeholder text            | `var(--grey-100)`                         |
| Cursor Line (editable only) | `var(--grey-100)`                         |
| Close icon                  | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--primary-60)` |
| Helper                      | `var(--grey-80)`                          |

---

#### Filled

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Tag                         | See Tag component UI blueprint             |
| Placeholder text            | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--grey-80)`                          |
| Helper                      | `var(--grey-80)`                          |

---

#### Disabled

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| All elements      | Same as Empty state          |
| **General opacity** | **30%**                    |

---

#### Locked & Read-only

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Placeholder text            | `var(--grey-80)`                          |
| Chevron icon                | `var(--grey-100)` (30% opacity)           |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--grey-40)`                          |
| Helper                      | `var(--grey-80)`                          |

---

#### Error

| Element                     | Color Token                                |
| --------------------------- | ------------------------------------------ |
| Label                       | `var(--grey-80)`                          |
| Asterisk                    | `var(--grey-100)`                         |
| Info icon                   | `var(--grey-80)`                          |
| Prefix icon                 | `var(--grey-80)`                          |
| Placeholder text            | `var(--grey-100)`                         |
| Chevron icon                | `var(--grey-100)`                         |
| Container (editable)        | `var(--global-white)`                     |
| Container (non-editable)    | `var(--grey-20)`                          |
| Container Stroke            | `var(--error-50)`                         |
| Helper                      | `var(--grey-80)`                          |
| Feedback icon               | `var(--error-50)`                         |
| Feedback text               | `var(--error-80)`                         |

---

### Without Container

#### Default (Filled)

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Placeholder text  | `var(--grey-100)`           |
| Chevron icon      | `var(--grey-100)`           |

#### Hover

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Placeholder text  | `var(--primary-50)`         |
| Chevron icon      | `var(--primary-50)`         |

#### Focus

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Placeholder text  | `var(--grey-100)`           |
| Chevron icon      | `var(--grey-100)`           |
| Container stroke  | `var(--primary-60)` (outside)|
| Container radius  | `var(--radius)` (8px)       |

#### Active

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Placeholder text  | `var(--grey-100)`           |
| Chevron icon      | `var(--grey-100)`           |

#### Disabled

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| All elements      | Same as Empty state          |
| **General opacity** | **30%**                    |

#### Filled & Read-only

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Placeholder text  | `var(--grey-100)`           |
| Chevron icon      | `var(--grey-100)` (30% opacity)|

---

## Behavioral Logic

### Filtering (Editable Only)

- System begins filtering once the user enters at least **3 characters**
- If no results match, a **"No options found"** message is displayed in the error state

### Multi-select Tag Handling

- **Limit:** Accommodates a maximum of **3 removable tags**
- **Overflow:** If more than 3 items are selected, or if space is insufficient, remaining items are consolidated into a non-dismissible numeric tag (e.g., "+N")
- **Clear All:** A "Clear All" icon appears in the filled state of a multi-select dropdown

### Sizing & Responsive

- **Height:** Small (Table viewports), Medium (Default), Large (High emphasis)
- **Mobile:** If the list exceeds 7 items, it is recommended to open the list in a new full-screen page rather than a standard overlay

---

## Alignment

- Prefix, suffix & placeholder text will always **center align vertically** in the field
- Recommended: Use concise and short labels
- In exceptional cases, if label extends to double line, asterisk and info icon appear at the end of the label

---

## Accessibility (A11y)

- **Inactive:** Default view
- **Hover:** Background color shift on input or result items (`var(--grey-20)`)
- **Typing:** The microphone icon (if present) is replaced by the [X] clear icon
- **Focus:** Square focus ring (accessibility) around the input or selected result item
- `aria-expanded` indicates dropdown open/closed state
- `aria-haspopup="listbox"` on trigger
- `role="listbox"` on the menu
- `role="option"` on each menu item
- `aria-selected` on selected options
- `aria-required` for required fields
- `aria-invalid` for error state
- `aria-describedby` links to helper text and error messages
- Keyboard navigation: Arrow keys to navigate, Enter to select, Escape to close

---

## Designer Do's & Don'ts

- **Do:** Use concise, meaningful labels
- **Do:** Include an "Honorable Reset" option (e.g., "Select City") in the menu to allow users to return to the null state
- **Do:** Maintain the same width for multiple dropdowns in a single section for consistency
- **Don't:** Use nested dropdowns within a single select component
- **Don't:** Leave the component empty without a default placeholder or value
- **Don't:** Use for less than 5 options

---

## Dropdown with Tags (Multi-select)

- Only **one** removable tag added for multi option variant in **editable** kind
- Maximum **three** removable tags added and **one link tag** for multi option variant in **non-editable** kind

---

## Code Examples

### Basic Single Select (Editable)

```tsx
import { InputDropdown } from './ui/input-dropdown';

function CitySelector() {
  return (
    <InputDropdown
      type="single"
      kind="editable"
      size="medium"
      label="Select City"
      placeholder="Search city..."
      options={[
        { value: "mumbai", label: "Mumbai" },
        { value: "delhi", label: "Delhi" },
        { value: "bangalore", label: "Bangalore" },
        { value: "chennai", label: "Chennai" },
        { value: "kolkata", label: "Kolkata" },
        { value: "hyderabad", label: "Hyderabad" },
      ]}
      onChange={(value) => console.log(value)}
    />
  );
}
```

### Multi-select with Tags

```tsx
<InputDropdown
  type="multi"
  kind="non-editable"
  size="medium"
  label="Select Skills"
  required
  placeholder="Choose your skills"
  options={[
    { value: "react", label: "React" },
    { value: "typescript", label: "TypeScript" },
    { value: "node", label: "Node.js" },
    { value: "python", label: "Python" },
    { value: "aws", label: "AWS" },
    { value: "docker", label: "Docker" },
  ]}
  onChange={(values) => console.log(values)}
/>
```

### Without Container

```tsx
<InputDropdown
  type="single"
  kind="non-editable"
  size="medium"
  appearance="without-container"
  placeholder="Sort by"
  options={[
    { value: "newest", label: "Newest First" },
    { value: "oldest", label: "Oldest First" },
    { value: "popular", label: "Most Popular" },
  ]}
/>
```

---

## Design Tokens Used -- Summary

### Colors

| Token                | Usage                              |
| -------------------- | ---------------------------------- |
| `--global-white`     | Container background (editable)    |
| `--grey-20`          | Container background (non-editable), hover bg |
| `--grey-40`          | Read-only border                   |
| `--grey-60`          | Placeholder text (editable)        |
| `--grey-80`          | Default border, label, helper text, icons |
| `--grey-100`         | Asterisk, text values, chevron     |
| `--primary-50`       | Without-container hover text       |
| `--primary-60`       | Hover/Focus/Active border          |
| `--error-50`         | Error border, feedback icon        |
| `--error-80`         | Error feedback text                |

### Typography

| Token                   | Usage                           |
| ----------------------- | ------------------------------- |
| `--font-family-jiotype` | All text (label, value, helper) |
| `--font-weight-normal`  | Label, value, helper text       |
| `--font-weight-medium`  | Tag text                        |
| `--font-weight-bold`    | Selected value emphasis          |
| `--text-body-xs`        | Small/Medium labels, helper     |
| `--text-body-s`         | Large labels, Small/Medium text |
| `--text-body-m`         | Large input text                |

### Spacing

| Token        | Usage                                      |
| ------------ | ------------------------------------------ |
| `--space-1`  | Gap between label, input, feedback, helper (4px) |
| `--space-2`  | Without-container medium spacing (8px)     |
| `--space-3`  | Internal element spacing, small padding (12px) |
| `--space-4`  | Large/Medium left/right padding (16px)     |

### Radius

| Token      | Usage                          |
| ---------- | ------------------------------ |
| `--radius` | Container border radius (8px)  |

---

## Related Components

- **Input** -- Use for free-form text input
- **Checkbox** -- Use for selecting from a small set (< 5 items)
- **Radio Button** -- Use for selecting one from a small set (< 5 items)
- **Badge/Tag** -- Used internally for multi-select tags
- **Accordion** -- Use for expandable content sections
