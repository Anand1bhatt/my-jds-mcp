# Input Field — JDS Component Style Guide

## Overview

**Definition:** A text field allows users to enter, edit, and select short-form text or numbers. It is primarily used in forms and dialogs to capture user data.

**Types:**
- **Text:** Accepts letters, numbers, and special characters
- **Numeric:** Specifically constrained to numeric values (e.g., Phone numbers, OTPs)
- **Password/PIN:** Masks input for security using dots; includes show/hide functionality

Component: `/src/app/components/ui/input.tsx`

---

## When to Use

- ✅ **Use Input Fields** for capturing short-form user data (single line)
- ✅ **Use in forms** for collecting information like name, email, phone number
- ✅ **Use for search** functionality with appropriate prefix/suffix icons
- ✅ **Use numeric inputs** for phone numbers, OTPs, amounts
- ✅ **Use password inputs** for secure credential entry
- ❌ **Do NOT use for long-form content** — use Textarea instead
- ❌ **Do NOT use placeholder as label replacement** — always provide a label
- ❌ **Do NOT write "Error" as error message** — be specific

---

## Anatomy

The component is composed of nine distinct elements:

1. **Label Text:** Identifies the field (Mandatory except in edge cases)
2. **Info Icon:** Provides further clarification via tooltip
3. **Prefix (Icon/Image/Text):** Fixed content at the start (e.g., country code +91)
4. **Placeholder/Input Text:** Hint text that disappears on focus/typing
5. **Suffix (Icon/Button/Text):** Fixed content or action at the end (e.g., "kg", "Show" button)
6. **Container:** The bounding box for the input
7. **Feedback:** Visual indicators for Success/Error
8. **Helper Text:** Crucial information needed to complete the task
9. **Helper Button:** Actions to resolve issues (e.g., "Resend OTP", "Forgot Password")

---

## Variants

### 1. Text Input (Default)

```tsx
<Input
  size="medium"
  label="Email address"
  placeholder="Enter your email"
  helperText="We'll never share your email"
/>
```

### 2. Text Input with Required Field

```tsx
<Input
  size="medium"
  label="Full name"
  required
  placeholder="Enter your full name"
/>
```

### 3. Text Input with Info Icon

```tsx
<Input
  size="medium"
  label="JioHome Number"
  infoIcon={<IcInfo className="w-5 h-5" fill="currentColor" />}
  onInfoClick={() => alert('What is a JioHome number?')}
  placeholder="Enter your JioHome number"
/>
```

### 4. Text Input with Prefix

```tsx
<Input
  size="large"
  label="Mobile number"
  prefixText="+91"
  placeholder="Enter mobile number"
/>
```

### 5. Text Input with Suffix

```tsx
<Input
  size="medium"
  label="Weight"
  placeholder="Enter weight"
  suffixText="kg"
/>
```

### 6. Numeric Input (Non-editable Country Code)

```tsx
<Input
  type="tel"
  size="large"
  label="Mobile number"
  prefixText="+91"
  placeholder="Enter mobile number"
  helperText="10-digit mobile number"
/>
```

### 7. Password Input

```tsx
<Input
  type="password"
  size="medium"
  label="Password"
  required
  placeholder="Enter your password"
  suffixIcon={<IcEye className="w-5 h-5" fill="currentColor" />}
  onSuffixClick={() => togglePasswordVisibility()}
/>
```

### 8. Input with Error State

```tsx
<Input
  size="medium"
  label="Email"
  placeholder="Enter email"
  error="Please enter a valid email address"
/>
```

### 9. Input with Success State

```tsx
<Input
  size="medium"
  label="Email"
  placeholder="Enter email"
  success="Email verified successfully"
/>
```

### 10. Loading State

```tsx
<Input
  size="medium"
  label="UPI ID"
  placeholder="Enter UPI ID"
  loading
  helperText="Validating UPI ID..."
/>
```

### 11. Disabled State

```tsx
<Input
  size="medium"
  label="Account ID"
  value="ACC123456"
  disabled
/>
```

### 12. Read-only State

```tsx
<Input
  size="medium"
  label="Reference Number"
  value="REF987654"
  readOnly
/>
```

---

## Specifications

### Variant: Text

#### Large Size (48px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 48px                                   |
| Label                  | `var(--text-body-s)` (16px)           |
| Label Asterisk         | `var(--text-body-s)` (16px)           |
| Label Info Icon        | Small (20px)                           |
| Prefix image/icon      | 24px                                   |
| Prefix text            | `var(--text-body-m)` + `--font-weight-bold` |
| Placeholder/Input text | `var(--text-body-m)` (18px)           |
| Suffix text            | `var(--text-body-m)` (18px)           |
| Suffix icon button A   | Medium                                 |
| Suffix icon button B   | Medium                                 |
| Suffix Text Button     | Medium (Tertiary)                      |
| Container              | H-48px, W-depends on use               |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Helper text            | `var(--text-body-s)` (16px)           |
| Helper Button          | Small (Tertiary)                       |

**Spacing:**
- Label → Input → Feedback → Helper text → Helper button: **4px** (`var(--space-1)`)
- Input (inside) → Left, Right, Suffix all elements between: **12px** (`var(--space-3)`)
- Input (inside) → Prefix all elements between: **8px** (`var(--space-2)`)

---

#### Medium Size (40px) — Default

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 40px                                   |
| Label                  | `var(--text-body-xs)` (14px)          |
| Label Asterisk         | `var(--text-body-xs)` (14px)          |
| Label Info Icon        | Small (20px)                           |
| Prefix image/icon      | 24px                                   |
| Prefix text            | `var(--text-body-s)` + `--font-weight-bold` |
| Placeholder/Input text | `var(--text-body-s)` (16px)           |
| Suffix text            | `var(--text-body-s)` (16px)           |
| Suffix icon button A   | Medium                                 |
| Suffix icon button B   | Medium                                 |
| Suffix Text Button     | Medium (Tertiary)                      |
| Container              | H-40px, W-depends on use               |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Helper text            | `var(--text-body-xs)` (14px)          |
| Helper Button          | Small (Tertiary)                       |

**Spacing:**
- Label → Input → Feedback → Helper text → Helper button: **4px** (`var(--space-1)`)
- Input (inside) → Left, Right, Prefix & Suffix all elements between: **8px** (`var(--space-2)`)

---

#### Small Size (32px)

| Element                | Specification                          |
| ---------------------- | -------------------------------------- |
| **Height**             | 32px                                   |
| Label                  | `var(--text-body-xs)` (14px)          |
| Label Asterisk         | `var(--text-body-xs)` (14px)          |
| Label Info Icon        | Small (20px)                           |
| Prefix image/icon      | 16px                                   |
| Prefix text            | `var(--text-body-s)` + `--font-weight-bold` |
| Placeholder/Input text | `var(--text-body-s)` (16px)           |
| Suffix text            | `var(--text-body-s)` (16px)           |
| Suffix icon button A   | Small                                  |
| Suffix icon button B   | Small                                  |
| Suffix Text Button     | Small (Tertiary)                       |
| Container              | H-32px, W-depends on use               |
| Container Stroke       | 1px inside                             |
| Container Radius       | `var(--radius)` (8px)                 |
| Helper text            | `var(--text-body-xs)` (14px)          |
| Helper Button          | Small (Tertiary)                       |

**Spacing:**
- Label → Input → Feedback → Helper text → Helper button: **4px** (`var(--space-1)`)
- Input (inside) → Left, Right, Prefix & Suffix all elements between: **8px** (`var(--space-2)`)

---

### Variant: Numeric

#### Type: Non-editable Country Code (+91)

Same specifications as **Text variant** with:
- `prefixText="+91"` (non-editable)
- `type="tel"` for numeric keyboard on mobile
- Dynamic text below helper text for character count/validation

#### Type: Editable Country Code (+91)

Includes an additional dropdown/selector for country code selection before the input field.

**Elements:**
1. Label
2. Country Code Container (separate field with dropdown)
3. Main input field for number
4. All other elements same as Text variant

---

### Variant: Password/PIN

Same specifications as **Text variant** with:
- `type="password"` to mask input as dots
- Suffix icon button (eye icon) to toggle visibility
- Helper button for "Forgot Password" link

---

## Visual States

### Default (Empty)

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Input text        | none (label is on its position) |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--grey-60)`            |
| Helper            | `var(--grey-80)`            |

---

### Hover

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Input text        | none (label is on its position) |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--primary-50)` ✨       |
| Helper            | `var(--grey-80)`            |

---

### Focus

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Placeholder text  | `var(--grey-100)`           |
| Cursor Stroke     | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--primary-60)` ✨       |
| Helper            | `var(--grey-80)`            |

---

### Active (Typing)

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)` ✨         |
| Cursor Stroke     | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--primary-60)`         |
| Helper            | `var(--grey-80)`            |

---

### Filled

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--grey-60)`            |
| Helper            | `var(--grey-80)`            |

---

### Filled and Read-only

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--grey-40)` ✨          |
| Helper            | `var(--grey-80)`            |

---

### Disabled

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| All elements      | Same as Empty state          |
| **General opacity** | **30%** ✨                 |

---

### Loading

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)`           |
| Suffix Spinner    | Size/small ✨                |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--grey-60)`            |
| Helper            | `var(--grey-80)`            |

---

### Success

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--success-50)` ✨       |
| Helper            | `var(--grey-80)`            |
| Feedback icon     | `var(--success-50)` ✨       |
| Feedback text     | `var(--success-80)` ✨       |

---

### Error

| Element           | Color Token                  |
| ----------------- | ---------------------------- |
| Label             | `var(--grey-80)`            |
| Asterisk          | `var(--grey-100)`           |
| Info icon         | `var(--grey-80)`            |
| Prefix icon       | `var(--grey-80)`            |
| Prefix text       | `var(--grey-80)`            |
| Input text        | `var(--grey-100)`           |
| Suffix button     | `var(--grey-80)`            |
| Suffix text       | `var(--grey-80)`            |
| Container         | `var(--global-white)`       |
| Container Stroke  | `var(--error-50)` ✨         |
| Helper            | `var(--grey-80)`            |
| Feedback icon     | `var(--error-50)` ✨         |
| Feedback text     | `var(--error-80)` ✨         |

---

## Behavioral Logic

### Horizontal Overflow
- Content does not wrap
- It moves horizontally to the left as the user types beyond the container width

### Password Masking
- Defaults to dots (`type="password"`)
- Suffix button (eye icon) toggles visibility

### Mandatory Fields
- Indicated by a colored asterisk (*) at the top-right of the label
- Uses `required` prop

### Clear Content
- A cross icon appears in the filled state (positioned to the left of other suffixes) to wipe input
- Can be added via `suffixIcon` prop

### Numeric Separators
- Supports hyphens or spaces for readability (e.g., 7678-6736)
- Handled via custom formatting logic

---

## Alignment

### Prefix, Suffix & Placeholder Text
- **Always center-aligned vertically** within the field
- Uses `align-items: center` on container

### Label with Asterisk & Info Icon
- Recommended: Use concise and short labels
- In exceptional cases, if label extends to double line, asterisk and info icon appear at the end of the label

---

## Accessibility (A11y)

### Screen Readers
- ✅ **Do NOT read placeholder text** — Screen readers ignore placeholders
- ✅ **Critical info must be in Label or Helper Text**
- ✅ **Required fields** use `aria-label="Required"` on asterisk element

### Focus Management
- ✅ **TAB key** moves focus between fields
- ✅ **Disabled fields** are ignored in tab order
- ✅ **Interactive suffixes** (buttons) must be announced as actions by screen readers

### ARIA Attributes
- `aria-invalid="true"` when error state is active
- `aria-required="true"` for required fields
- `aria-describedby` links to helper text and error messages

---

## Usage Guidelines

### ✅ Do

- Use Helper Text to explain complex requirements (e.g., "Min 8 characters")
- Maintain consistent width for all fields in a single section
- Always provide a Label (mandatory except in edge cases)
- Use specific error messages (e.g., "Enter a valid email")
- Use appropriate input types (`type="email"`, `type="tel"`, etc.)
- Use placeholder text as a hint, not as a replacement for label

### ❌ Don't

- Don't use Placeholder text as a replacement for a Label
- Don't use colons at the end of labels
- Don't write "Error" as the error message — be specific
- Don't disable fields without clear indication why
- Don't use arbitrary values — only CSS design tokens

---

## Code Examples

### Basic Text Input

```tsx
import { Input } from './ui/input';

function ContactForm() {
  return (
    <Input
      size="medium"
      label="Email address"
      type="email"
      placeholder="you@example.com"
      helperText="We'll never share your email"
    />
  );
}
```

### Required Field with Error

```tsx
<Input
  size="medium"
  label="Full name"
  required
  placeholder="Enter your full name"
  error="Please enter your full name"
/>
```

### Phone Number with Country Code

```tsx
<Input
  size="large"
  label="Mobile number"
  type="tel"
  prefixText="+91"
  placeholder="Enter mobile number"
  helperText="10-digit mobile number"
/>
```

### Password with Toggle

```tsx
import { IcEye, IcEyeOff } from '@jds/core-icons';

function PasswordInput() {
  const [showPassword, setShowPassword] = React.useState(false);

  return (
    <Input
      size="medium"
      label="Password"
      required
      type={showPassword ? "text" : "password"}
      placeholder="Enter your password"
      suffixIcon={
        showPassword ? (
          <IcEyeOff className="w-5 h-5" fill="currentColor" />
        ) : (
          <IcEye className="w-5 h-5" fill="currentColor" />
        )
      }
      onSuffixClick={() => setShowPassword(!showPassword)}
      helperText="Minimum 8 characters"
    />
  );
}
```

### Loading State (UPI Validation)

```tsx
<Input
  size="medium"
  label="UPI ID"
  placeholder="yourname@upi"
  loading
  helperText="Validating UPI ID..."
/>
```

### Success State

```tsx
<Input
  size="medium"
  label="Email"
  type="email"
  value="user@example.com"
  success="Email verified successfully"
/>
```

---

## Design Tokens Used — Summary

### Colors

| Token                | Usage                              |
| -------------------- | ---------------------------------- |
| `--global-white`     | Container background               |
| `--grey-40`          | Read-only border                   |
| `--grey-60`          | Default border                     |
| `--grey-80`          | Label, helper text, icons          |
| `--grey-100`         | Input text, asterisk, placeholder  |
| `--primary-50`       | Hover border                       |
| `--primary-60`       | Focus/Active border                |
| `--success-50`       | Success border, feedback icon      |
| `--success-80`       | Success feedback text              |
| `--error-50`         | Error border, feedback icon        |
| `--error-80`         | Error feedback text                |

### Typography

| Token                   | Usage                           |
| ----------------------- | ------------------------------- |
| `--font-family-jiotype` | All text (label, input, helper) |
| `--font-weight-normal`  | Label, input text, helper text  |
| `--font-weight-bold`    | Prefix text                     |
| `--text-body-xs`        | Small/Medium labels, helper     |
| `--text-body-s`         | Large labels, Small/Medium input |
| `--text-body-m`         | Large input text                |

### Spacing

| Token        | Usage                                      |
| ------------ | ------------------------------------------ |
| `--space-1`  | Gap between label, input, feedback, helper (4px) |
| `--space-2`  | Small/Medium internal padding (8px)        |
| `--space-3`  | Large internal padding (12px)              |

### Radius

| Token      | Usage                          |
| ---------- | ------------------------------ |
| `--radius` | Input container border radius (8px) |

### Width

| Token          | Usage                          |
| -------------- | ------------------------------ |
| `--width-input` | Input field width (340px)     |

---

## Related Components

- **Textarea** — Use for multi-line text input
- **Select/Dropdown** — Use when users need to choose from predefined options
- **Button** — Use for suffix/helper button actions
- **Checkbox/Radio** — Use for boolean or multiple-choice selections

---

## Migration Guide

If migrating from the old Input component:

**Before:**
```tsx
<Input
  type="tel"
  placeholder="Enter mobile number"
  className="w-full"
  style={{
    fontFamily: 'var(--font-family-jiotype)',
    fontSize: 'var(--text-base)',
  }}
/>
```

**After:**
```tsx
<Input
  size="medium"
  label="Mobile number"
  type="tel"
  placeholder="Enter mobile number"
/>
```

**Key Changes:**
- Add `size` prop (default is "medium")
- Add `label` prop for accessibility
- Remove manual style overrides — component uses design tokens
- Use `error`, `success`, `helperText` props instead of external elements
- Use `prefixIcon`, `suffixIcon` props for icons
- Use `loading` prop for loading state