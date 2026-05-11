# Selector Button

## 1. Overview

**Definition:** A selector button is an interactive control that allows the user to perform a selection action. It functions as a toggle between a **Deselected** (default) and **Selected** state.

---

## 2. Anatomy

The selector button component anatomy is made up of:

1. **Label:** The text content describing the selection.
2. **Icon:** An optional icon placed to the left or right of the label.
3. **Container:** The bounding box with defined padding, radius, and background.

---

## 3. Sizes

### Large

Large is the size to use whenever possible.

### Medium

Restricted to interaction elements where space is more critical, such as navigation bars and contextual actions within components.

### Small

Restricted to interaction elements where space is more critical, such as navigation bars and contextual actions within components.

---

## 4. Variants

### Default

The variant Default is composed of:

1. Label.

### Icon-left

The variant Icon-left is composed of:

1. Label.
2. Icon (placed to the left of the label).

### Icon-right

The variant Icon-right is composed of:

1. Label.
2. Icon (placed to the right of the label).

### Icon-right-pin

The variant Icon-right-pin is composed of:

1. Label.
2. Icon (placed to the right, pinned to the container edge).

### Icon-only

The variant Icon-only is composed of:

1. Icon (no label).

---

## 5. States

### Deselected (Default)

Its default state. The component is idle and available for interaction.

### Hover

Triggered when the user hovers over the element with the mouse pointer (cursor).

### Pressed

State in which the component is held while the user interaction occurs.

### Focus

Triggered when the user clicks or taps on an element, or selects it with the keyboard's Tab key.

### Selected

Component state once the user has made the selection.

---

## 6. Accessibility Guidelines

- **Keyboard-friendly:** On desktop interfaces, users should be able to trigger selector buttons using only the keyboard (Space / Enter to toggle, Tab to navigate).
- **Screen Readers:** Must announce the component role (e.g., "toggle button") and its current state ("selected" / "not selected").
- **Touch Target:** Container must serve as the full hit area for accessible touch targets.

---

## 7. Designer Guidelines

- **Font size:** Do not use sizes smaller than 16pt.
- **Avoid Caps Labels:** Never use all caps, or else the labels would be difficult to read and much harder to quickly scan, as there are no differences in character height any more.
- **Labels copies:** Clear and short descriptive labels make users feel more confident that they are understanding things in the right way, and taking the right actions.

---

## 8. Specifications

### Component Anatomy — Size: Large

| Element | Property | Value |
|---------|----------|-------|
| **Icon left** | Size | 24×24 px |
| **Label** | Font | `var(--text-button)` — 16px |
| **Icon right** | Size | 24×24 px |
| **Container** | Top padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Bottom padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Left padding | `var(--space-6)` — 24px (`$spacing-m`) |
| **Container** | Right padding | `var(--space-6)` — 24px (`$spacing-m`) |
| **Container** | Gap | `var(--space-2)` — 8px (`$spacing-xs`) |
| **Container** | Radius | `var(--radius-button)` — 250px (`$Radius/pill`) |

### Component Anatomy — Size: Medium

| Element | Property | Value |
|---------|----------|-------|
| **Icon left** | Size | 24×24 px |
| **Label** | Font | `var(--text-button)` — 16px |
| **Icon right** | Size | 24×24 px |
| **Container** | Top padding | `var(--space-3)` — 12px (`$spacing-s`) |
| **Container** | Bottom padding | `var(--space-3)` — 12px (`$spacing-s`) |
| **Container** | Left padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Right padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Gap | `var(--space-2)` — 8px (`$spacing-xs`) |
| **Container** | Radius | `var(--radius-button)` — 250px (`$Radius/pill`) |

### Component Anatomy — Size: Small

| Element | Property | Value |
|---------|----------|-------|
| **Icon left** | Size | 16×16 px |
| **Label** | Font | `var(--text-button)` — 16px |
| **Icon right** | Size | 16×16 px |
| **Container** | Top padding | `var(--space-1)` — 4px (`$spacing-xxs`) |
| **Container** | Bottom padding | `var(--space-1)` — 4px (`$spacing-xxs`) |
| **Container** | Left padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Right padding | `var(--space-4)` — 16px (`$spacing-base`) |
| **Container** | Gap | `var(--space-2)` — 8px (`$spacing-xs`) |
| **Container** | Radius | `var(--radius-button)` — 250px (`$Radius/pill`) |

---

## 9. State Specifications — Colour & Layer Effects

> Same properties apply to all sizes and all variants.

| State | Background | Label Color | Icon Color | Stroke |
|-------|-----------|-------------|------------|--------|
| **Deselected (Default)** | none | `var(--primary-40)` | `var(--primary-40)` | none |
| **Hover** | `var(--primary-20)` | `var(--primary-60)` | `var(--primary-60)` | none |
| **Pressed** | `var(--primary-30)` | `var(--primary-60)` | `var(--primary-60)` | none |
| **Focused** | `var(--primary-20)` (same as Hover) | `var(--primary-60)` | `var(--primary-60)` | 4px outside `var(--primary-80)` |
| **Selected** | `var(--primary-70)` | `var(--primary-30)` | `var(--primary-30)` | none |

---

## 10. Edge Cases

### Multiple Lines — Selector Button

The icon variants have all the elements **vertically aligned** within the selector button area.

### Text Only

Text is **center aligned** within the container.

### With Icon

Text and icon are **left or right aligned** depending on language translation (LTR / RTL support).

---

## 11. Token Mapping (CSS Variables)

| Spec Token | CSS Variable | Value |
|-----------|-------------|-------|
| `$button` (typography) | `var(--text-button)` | 16px |
| `$spacing-xxs` | `var(--space-1)` | 4px |
| `$spacing-xs` | `var(--space-2)` | 8px |
| `$spacing-s` | `var(--space-3)` | 12px |
| `$spacing-base` | `var(--space-4)` | 16px |
| `$spacing-m` | `var(--space-6)` | 24px |
| `$Radius/pill` | `var(--radius-button)` | 250px |
| `$theme/primary/20` | `var(--primary-20)` | #E7EBF8 |
| `$theme/primary/30` | `var(--primary-30)` | #9EB5FA |
| `$theme/primary/40` | `var(--primary-40)` | #6789F4 |
| `$theme/primary/60` | `var(--primary-60)` | #0A2885 |
| `$theme/primary/70` | `var(--primary-70)` | #061951 |
| `$theme/primary/80` | `var(--primary-80)` | #070E21 |

---

## 12. Related Documentation

- **Button:** `/guidelines/MD/Component/button.md`
- **Selector:** `/guidelines/MD/Component/selector.md`
- **Tag:** `/guidelines/MD/Component/tag.md`
- **Icon:** `/guidelines/MD/Component/icon.md`
- **Design Tokens:** `/src/styles/theme.css`

---
