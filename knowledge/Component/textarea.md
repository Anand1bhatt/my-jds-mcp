# Input TextArea — JDS Component Style Guide

## Overview

**Definition:** The text area element serves the purpose of displaying, inputting, and editing long unformatted textual content spanning multiple lines, primarily through keyboard input.

**Component:** `/src/app/components/ui/textarea.tsx`

---

## When to Use

- To be used when the expected user input is more than one sentence and might span to multiple lines.
- To be used when user must enter quick-entry text data that can be written free-hand rather than with a more complicated control.

## When NOT to Use

- Not to be used when the entry is specifically only numeric. Use the type text field:numeric instead.
- Not to be used when the entry is a password. Use the type text field:password instead.
- Not to be used when the input necessitates formatting with various styles and colours.
- Not to be used when the user requires a tool for texts that demand additional formatting.
- Not to be used when the input is a known date. Use input date instead.
- Not to be used when selecting is easier than typing.

---

## Variants

### 1. Default

The standard multi-line text area with a fixed minimum height and optional drag-handle resize.

```tsx
<TextArea
  variant="default"
  size="md"
  label="Description"
  placeholder="Enter a description..."
/>
```

**Anatomy:**
1. Label
2. Input container (mostly squarical)
3. Drag handle (optional — `resizable` prop)

**When to use:** Expected input is more than one sentence spanning multiple lines.

**When NOT to use:** Do not use if the input should grow into multiple lines dynamically — use auto-expandable instead.

**Accessibility:**
- The entire text area comes into focus at once.
- If the resizable property is enabled, assistive technology should announce "Resizable text area, drag handle to adjust size."

### 2. Auto-expandable

Starts as a compact field and expands automatically as the user types more content.

```tsx
<TextArea
  variant="auto-expandable"
  size="md"
  label="Quick note"
  placeholder="Start typing..."
/>
```

**Anatomy:**
1. Label
2. Input container (expands dynamically)

**When to use:**
- Input starts as a single line but expands automatically as more text is added.
- Ideal for compact layouts that need to handle longer text without taking up too much space initially.

**When NOT to use:**
- Do not use when the input is strictly limited to a single line — use a Text Field instead.
- Do not use if the input should remain a fixed height and not expand dynamically.

**Accessibility:**
- The entire text area comes into focus at once.
- Pressing Enter or typing should expand the field while maintaining focus visibility.

---

## Feature Variants (Props)

### 3. With Label

```tsx
<TextArea label="Comments" size="md" />
```

**Accessibility:** Should show `<label alt text> edit text` as alt text.

### 4. With Mandatory Indicator

```tsx
<TextArea label="Feedback" required size="md" />
```

Asterisk appears top-right of the label.

**Accessibility:** Focus shows `<label alt text> edit text entry required` as alt text. Avoid pale greys or low-contrast colours for the mandatory indicator.

### 5. With Info Icon

```tsx
import { IcInfo } from '@jds/core-icons';

<TextArea
  label="Notes"
  required
  infoIcon={<IcInfo style={{ width: '16px', height: '16px' }} />}
  onInfoClick={() => alert('Clarification here')}
  size="md"
/>
```

Info icon appears right of the label (or right of asterisk if present). Displays a tooltip on hover.

**Accessibility:** Should maintain min. contrast of 3:1 with the background.

### 6. With Placeholder Text

```tsx
<TextArea
  label="Message"
  placeholder="Type your message here..."
  size="md"
/>
```

**Behaviour:**
- Disappears once the user focuses and begins to type.
- Restored if the value is removed and the field loses focus.

**Accessibility:** Should maintain min. contrast of 3:1 with the background. Font colour toned down from input text.

### 7. With Suffix Button

```tsx
import { IcMic } from '@jds/core-icons';

<TextArea
  label="Voice note"
  suffixButton={<IcMic style={{ width: '20px', height: '20px' }} />}
  onSuffixClick={() => console.log('Start voice input')}
  size="md"
/>
```

Suffix button positioned extreme right of the input container (top-right). Text content flows to next line maintaining space between suffix and content.

### 8. With Helper Text

```tsx
<TextArea
  label="Grocery list"
  helperText="Use commas to separate each item in the list."
  size="md"
/>
```

Helper text appears below the input container, aligning left. Recommended to be shown even in validation state (especially error).

**Accessibility:** Links not to be included within helper text. Long paragraphs not to be used.

### 9. With Character Counter

```tsx
<TextArea
  label="Bio"
  maxLength={200}
  showCharacterCounter
  helperText="Maximum 200 characters allowed"
  size="md"
/>
```

Counter appears bottom-right. When over limit, displays warning state with contextual feedback message.

**Behaviour:** When characters exceed limit, user can continue typing but counter shows warning state. Pasted text that exceeds limit is selected automatically.

### 10. With Drag Handle (Default variant only)

```tsx
<TextArea
  variant="default"
  label="Long description"
  resizable
  size="md"
/>
```

Drag handle at extreme bottom-right of the container. Constrained resize within defined area.

**Accessibility:**
- Provide clear labels for resizing handles using ARIA attributes.
- Communicate resize limitations to users.
- When handle receives focus, ensure visible distinction.

---

## States

### Interaction States

| State              | Border Stroke             | Input Text        | Suffix/Icons      | Opacity |
| ------------------ | ------------------------- | ----------------- | ----------------- | ------- |
| **Empty/Default**  | `var(--grey-60)`          | —                 | `var(--grey-80)`  | 1       |
| **Hover**          | `var(--primary-50)`       | —                 | `var(--grey-80)`  | 1       |
| **Focused/Active** | `var(--primary-60)`       | `var(--grey-100)` | `var(--grey-80)`  | 1       |
| **Filled**         | `var(--grey-60)`          | `var(--grey-100)` | `var(--grey-80)`  | 1       |
| **Filled+ReadOnly**| `var(--grey-40)`          | `var(--grey-80)`  | `var(--grey-80)`  | 1       |
| **Disabled**       | `var(--grey-60)`          | —                 | `var(--grey-80)`  | 0.3     |
| **Loading**        | `var(--grey-60)`          | `var(--grey-100)` | Spinner           | 1       |

**Common across all states:**
- Label text/icon: `var(--grey-80)`
- Asterisk: `var(--grey-100)`
- Placeholder text: `var(--grey-60)`
- Helper text: `var(--grey-80)`
- Character counter: `var(--grey-80)`
- Drag handle icon: `var(--grey-60)`
- Container fill: `var(--global-white)` (background)

### Validation States

| State       | Feedback Icon Color          | Feedback Text Color          |
| ----------- | ---------------------------- | ---------------------------- |
| **Error**   | `var(--error-50)`            | `var(--error-80)`            |
| **Success** | `var(--success-50)`          | `var(--success-80)`          |
| **Warning** | `var(--warning-50)`          | `var(--warning-80)`          |

```tsx
// Error
<TextArea label="Email body" error="This field is required" size="md" />

// Success
<TextArea label="Notes" success="Saved successfully" size="md" />

// Warning (e.g. character limit approaching)
<TextArea label="Bio" warning="Only 10 characters remaining" size="md" />
```

---

## Sizes

### Default Variant

| Token     | Size | Label Font          | Input/Placeholder Font | Helper/Counter Font | Min Height | Radius              |
| --------- | ---- | ------------------- | ---------------------- | ------------------- | ---------- | ------------------- |
| **lg**    | L    | `var(--text-body-s)` | `var(--text-body-m)`  | `var(--text-body-s)` | 76px      | `var(--radius)` (8px) |
| **md**    | M    | `var(--text-body-xs)`| `var(--text-body-s)`  | `var(--text-body-xs)`| 72px      | `var(--radius)` (8px) |
| **sm**    | S    | `var(--text-body-xs)`| `var(--text-body-s)`  | `var(--text-body-xs)`| 60px      | `var(--radius)` (8px) |
| **xs**    | XS   | `var(--text-body-xs)`| `var(--text-body-xs)` | `var(--text-body-xxs)`| 46px     | `calc(var(--radius) / 2)` (4px) |

### Auto-expandable Variant

Same sizing table as Default variant. The auto-expandable variant uses `minHeight` as the starting height but expands dynamically as text is entered.

**Note:** Max height and width are use-case dependent.

---

## Spacing

| Between                  | Token                    |
| ------------------------ | ------------------------ |
| Label → Container        | `var(--space-1)` (4px)   |
| Container padding (lg)   | `var(--space-3)` (12px)  |
| Container padding (md/sm)| `var(--space-2)` (8px)   |
| Container padding (xs)   | `var(--space-2)` H / `var(--space-1)` V |
| Container → Helper text  | `var(--space-1)` (4px)   |
| Container → Feedback     | `var(--space-1)` (4px)   |
| Feedback icon → text     | `var(--space-1)` (4px)   |

---

## Typography

All text uses `var(--font-family-jiotype)`.

| Element          | Font Weight                    | Color               |
| ---------------- | ------------------------------ | -------------------- |
| Label            | `var(--font-weight-normal)`    | `var(--grey-80)`     |
| Asterisk         | `var(--font-weight-normal)`    | `var(--grey-100)`    |
| Input text       | `var(--font-weight-normal)`    | `var(--grey-100)`    |
| Placeholder      | `var(--font-weight-normal)`    | `var(--grey-60)`     |
| Read-only text   | `var(--font-weight-normal)`    | `var(--grey-80)`     |
| Helper text      | `var(--font-weight-normal)`    | `var(--grey-80)`     |
| Character counter| `var(--font-weight-normal)`    | `var(--grey-80)`     |
| Feedback text    | `var(--font-weight-normal)`    | Per validation state |

---

## Behaviour

### Text Overflow — Default Variant

- Text wraps to the next line when it exceeds container width.
- If resizable is disabled and content exceeds the set max-height, content overflows with a native vertical scrollbar.
- Exiting the text area shows the beginning of content at the top-left.
- Upon reaching a set character limit, the cursor halts; an error message can be displayed.

### Text Overflow — Auto-expandable Variant

- Appears compact by default.
- When entered text exceeds available width, the text area automatically expands vertically.
- Adjacent elements are pushed downward — no horizontal scrollbar.
- Text wraps onto new lines instead of being truncated.
- Deleting text dynamically reduces field height.
- Retains at least one visible line to prevent unintended height changes.

### Interactions

**Mouse:**
- Clicking activates the text area for input.
- Clicking inside places the cursor at the exact position.

**Keyboard:**
- Tab to move focus. Once focused, the area is activated.
- Backspace removes content.
- Tab moves focus to next interactive element.
- Disabled textarea is ignored in tab order.
- If suffix is interactive, it follows in the tab order after the input.

**Touch:**
- Tapping activates for manual input and shows native keyboard.
- Long press on info icon shows details.

### Clear Content

**Default:** Clear button (when provided via suffix) removes content and returns to active state.

**Auto-expandable:** Deleting text dynamically reduces field height. Shrinks only when a full line is removed.

---

## API Reference

```tsx
import { TextArea } from './components/ui/textarea';

interface TextAreaProps {
  // Variant & size
  variant?: "default" | "auto-expandable";  // default: "default"
  size?: "xs" | "sm" | "md" | "lg";         // default: "md"

  // Label area
  label?: string;
  required?: boolean;
  infoIcon?: React.ReactNode;
  onInfoClick?: () => void;

  // Suffix
  suffixButton?: React.ReactNode;
  onSuffixClick?: () => void;

  // Feedback
  helperText?: string;
  error?: string;
  success?: string;
  warning?: string;

  // Character counter
  maxLength?: number;
  showCharacterCounter?: boolean;

  // Resize (default variant only)
  resizable?: boolean;

  // States
  loading?: boolean;
  disabled?: boolean;
  readOnly?: boolean;

  // Wrapper
  containerClassName?: string;

  // Plus all native <textarea> props
}
```

---

## Alignment

- Placeholder text always top-left aligned.
- Suffix button always top-right in the container.
- Labels should be concise. In exceptional cases, extended labels (double-line) can use asterisk and info icon at the end.

---

## Input Constraints

- Text areas accommodate various input types or can have specific validation/formatting rules (e.g., text-only, character limit).
- Constraints should be enforced when underlying data is well-defined and unlikely to change.
- Helper text like "Maximum 200 characters allowed" should communicate constraints clearly.

---

## Complete Example — All Features

```tsx
import { IcInfo, IcMic, IcClose } from '@jds/core-icons';

// Default with all features
<TextArea
  variant="default"
  size="lg"
  label="Feedback"
  required
  infoIcon={<IcInfo style={{ width: '16px', height: '16px' }} />}
  onInfoClick={() => alert('Tell us about your experience')}
  placeholder="Share your thoughts..."
  helperText="Be specific about what you liked or disliked"
  maxLength={500}
  showCharacterCounter
  resizable
  suffixButton={<IcMic style={{ width: '20px', height: '20px' }} />}
  onSuffixClick={() => console.log('Voice input')}
/>

// Auto-expandable with validation
<TextArea
  variant="auto-expandable"
  size="md"
  label="Quick note"
  placeholder="Start typing..."
  error="This field cannot be empty"
/>

// Read-only filled state
<TextArea
  variant="default"
  size="md"
  label="System log"
  readOnly
  value="Application started successfully at 10:32 AM.\nAll services are running."
/>

// Loading state
<TextArea
  variant="default"
  size="md"
  label="Pasting content"
  loading
  value="Processing pasted content..."
/>
```
