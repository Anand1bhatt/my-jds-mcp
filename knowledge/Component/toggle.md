# Toggle

## 1. Overview

**Definition:** Toggles (also known as switches) are digital on/off controls. They allow users to switch between two mutually exclusive states with an immediate effect, without requiring a "Submit" or "Save" action.

**Core Principle:** A toggle represents the actual status of a setting. When the user "flips" the switch, the resulting action must take effect immediately.

---

## 2. Anatomy

The Toggle component consists of:

1. **Icon (Optional):** Placed to the left of the label for extra context.
2. **Label Text:** Brief description of the setting (Recommended: Max 3 words).
3. **Toggle Control:**
   - a. **Toggle Handle:** The sliding circular thumb.
   - b. **Toggle Pill:** The background track.
4. **Helper Text (Optional):** Provides additional description below the title/label.

---

## 3. Kinds & States

### Kinds

- **Rest:** The neutral, unselected (Off) state.
- **Active:** The selected (On) state where the handle slides to the opposite side.

### States

- **Normal:** Default interactive state.
- **Hover/Pressed:** Visual feedback for interaction.
- **Focused:** Required for keyboard accessibility (Tab navigation).
- **Disabled:** Used when the setting is currently unavailable but visible for layout continuity.
- **Validation:** Supports Success, Error, and Warning states with icons and messages below.

---

## 4. Behavioral & Content Logic

### Immediate Action

- Toggles should only be used for actions that do not require a "Save" or "Apply" button. If the user must confirm the choice, use a Checkbox instead.

### Static Labels

- **Crucial Rule:** The label text must remain constant regardless of the toggle state.
  - ✅ **Do:** Label "Public Profile" stays the same whether On or Off.
  - ❌ **Don't:** Change label from "Show Status" to "Hide Status" when flipped.

### Content Guidelines

- Use Sentence case and no punctuation.
- Do not include "On" or "Off" text within the toggle graphic itself.
- Labels should be clear and concise.

---

## 5. Usage Guidelines

### Use Toggle When…

- The action takes effect immediately.
- You are switching a single independent state.
- Options are binary (On/Off).
- Used in Settings or Account sections.

### Use Something Else When…

- An "Apply" or "Submit" button is required → Use **Checkbox**.
- You are choosing one from multiple options → Use **Radio Button**.
- Options are opposing (e.g., List vs Grid) → Use **Segmented Control/Selector**.
- Used to perform a command like "Download" → Use **Button**.

---

## 6. Placement & Alignment

- **In-context:** Placed near the specific content it controls.
- **Vertical Groups:** Used in Settings or List views.
- **Alignment:** Labels can be placed to the left or right of the toggle. In list views, the toggle is often standalone (right-aligned) with the list title acting as the label.

---

## 7. Specifications

### Component Anatomy

- Icon (optional)
- Label (optional)
- Toggle
- Feedback block (validation)
- Helper block (optional)

---

### Size: Default

| Element | Property | Value |
|---------|----------|-------|
| **Icon** | Size | M |
| **Icon** | Colour | `var(--grey-80)` |
| **Label** | Style | `var(--text-body-s)` — 16px |
| **Toggle Pill** | Height | 24px |
| **Toggle Pill** | Width | 44px |
| **Toggle Pill** | Radius | `var(--radius-full)` (pill) |
| **Toggle Handle** | Padding | `var(--space-1)` (4px) |
| **Toggle Handle** | Diameter | 16px |
| **Feedback Block** | Size | Large |
| **Helper Block** | Font | `var(--text-body-s)` — 16px |

**Spacing (Default):**
- Vertical spacing (Icon → Label → Toggle): `var(--space-2)` (8px)
- Horizontal spacing (Toggle → Feedback → Helper): `var(--space-2)` (8px)

---

### Size: Small

| Element | Property | Value |
|---------|----------|-------|
| **Icon** | Size | S |
| **Icon** | Colour | `var(--grey-80)` |
| **Label** | Style | `var(--text-body-xs)` — 14px |
| **Toggle Pill** | Height | 16px |
| **Toggle Pill** | Width | 28px |
| **Toggle Pill** | Radius | `var(--radius-full)` (pill) |
| **Toggle Handle** | Padding | `var(--space-1)` (4px) |
| **Toggle Handle** | Diameter | 8px |
| **Feedback Block** | Size | Small |
| **Helper Block** | Font | `var(--text-body-xs)` — 14px |

**Spacing (Small):**
- Vertical spacing (Icon → Label → Toggle): `var(--space-2)` (8px)
- Horizontal spacing (Toggle → Feedback → Helper): `var(--space-1)` (4px)

---

## 8. State Specifications

> **Notes:**
> - All variations can work without a label, but the variation with icon on the left **must** have a label.
> - Properties on colour and typography apply to both sizes.

---

### Rest States

| State | Label Color | Label Font | Pill Border | Pill BG | Handle BG | Icon Color | Helper Color | Helper Font |
|-------|------------|-----------|------------|--------|----------|-----------|-------------|------------|
| **Normal** | `var(--grey-80)` | `var(--text-body-s)` | 1px solid `var(--grey-80)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Hover** | `var(--grey-100)` | `var(--text-body-s)` | 1px solid `var(--primary-40)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Pressed** | `var(--grey-100)` | `var(--text-body-s)` | 1px solid `var(--primary-60)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Focus** | `var(--grey-100)` | `var(--text-body-s)` | 4px solid `var(--primary-60)` (outside) | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Disabled** | Same as Normal | — | Same as Normal | — | — | — | — | — |
| **Success** | `var(--grey-80)` | `var(--text-body-s)` | 1px solid `var(--grey-80)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Warning** | `var(--grey-80)` | `var(--text-body-s)` | 1px solid `var(--grey-80)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Error** | `var(--grey-80)` | `var(--text-body-s)` | 1px solid `var(--grey-80)` | none | `var(--grey-80)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |

> **Disabled:** Same aspect as Normal with general opacity: 30%.

---

### Active States

| State | Label Color | Label Font | Pill Border | Pill BG | Handle BG | Icon Color | Helper Color | Helper Font |
|-------|------------|-----------|------------|--------|----------|-----------|-------------|------------|
| **Normal** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-50)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Hover** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-40)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Pressed** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-60)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Focus** | `var(--grey-100)` | `var(--text-body-s)` | 4px solid `var(--primary-60)` (outside) | `var(--primary-50)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Disabled** | Same as Normal | — | — | — | — | — | — | — |
| **Success** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-50)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Warning** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-50)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |
| **Error** | `var(--grey-100)` | `var(--text-body-s)` | none | `var(--primary-50)` | `var(--primary-inverse)` | `var(--grey-80)` | `var(--grey-80)` | `var(--text-body-s)` |

> **Disabled:** Same aspect as Normal with general opacity: 30%.

---

## 9. Accessibility (A11y)

- **Focusable:** Must be reachable via Tab and toggleable via Space or Enter.
- **Screen Readers:** Must announce the element as a "switch" or "toggle" and clearly state the "On" or "Off" status.
- **Touch Target:** Both the toggle and the label must be interactive to create a larger, more accessible hit area.

---

## 10. Designer Do's & Don'ts

### Do
- ✅ Use for "Dark Mode" or "Reading Mode" toggles.
- ✅ Use in list settings for independent controls (e.g., "Allow notifications").

### Don't
- ❌ Use a toggle to perform a command like "Download all".
- ❌ Change the label when the state changes.
- ❌ Use for opposing views like "List view vs Grid view."

---

## 11. Token Mapping (CSS Variables)

| Spec Token | CSS Variable |
|-----------|-------------|
| `$theme/primary/grey-80` | `var(--grey-80)` |
| `$theme/primary/grey-100` | `var(--grey-100)` |
| `$theme/primary/50` | `var(--primary-50)` |
| `$theme/primary/40` | `var(--primary-40)` |
| `$theme/primary/60` | `var(--primary-60)` |
| `$theme/primary/inverse` | `var(--primary-inverse)` |
| `$body-s` | `var(--text-body-s)` — 16px |
| `$body-xs` | `var(--text-body-xs)` — 14px |
| `$radius/pill` | `var(--radius-full)` — 9999px |
| `$xxs` | `var(--space-1)` — 4px |
| `$success-50` | `var(--success-50)` |
| `$warning-50` | `var(--warning-50)` |
| `$error-50` | `var(--error-50)` |

---

## 12. Related Documentation

- **Checkbox:** `/guidelines/MD/Component/checkbox.md`
- **Radio Button:** `/guidelines/MD/Component/radio-button.md`
- **Selector:** `/guidelines/MD/Component/selector.md`
- **Icon:** `/guidelines/MD/Component/icon.md`
- **Design Tokens:** `/src/styles/theme.css`

---
