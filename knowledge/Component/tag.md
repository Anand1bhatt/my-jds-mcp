# Tag

## 1. Overview

**Function:** Tags are keywords used to describe, categorize, or filter content. They help users differentiate between multiple categories mapped to the same content.

**How to use:** Use tags when users need to identify metadata at a glance or filter content within a specific page view.

---

## 2. Variants

### A. Tag Link

- **Purpose:** Acts as a trigger to navigate to or populate a relevant content view.
- **Anatomy:** Container + Label + Optional Add/Remove Icon.
- **Interaction:** Clicking anywhere on the tag triggers the associated action.

### B. Removable Tag

- **Purpose:** Specifically used for filtering content within a page.
- **Logic:** Can be toggled between "Checked" and "Unchecked" states.
- **Constraint:** These are not links; they represent active/inactive filters.

---

## 3. Anatomy

1. **Tag Container:** The bounding box with defined padding and radius.
2. **Label:** The text content (Max 2 words).
3. **Icon:** An optional "Add" (+) or "Remove" (×) icon to indicate selection status.

---

## 4. Visual States

1. **Default:** The standard state. For Removable Tags, this is the "Unchecked" state.
2. **Active:** Specific to Removable Tags; indicates the tag is "Checked."
3. **Hover:** Visual highlight when the user moves the cursor over the tag.
4. **Pressed:** Feedback for a user-initiated click or tap before release.
5. **Focus:** State triggered by keyboard navigation (Tab).
6. **Disabled:** Non-interactive state; the user cannot click or select.

---

## 5. Responsive Behavior

- **Overflow Logic:** If the label exceeds the available width or a maximum character limit, the text must be truncated with an ellipsis.
- **Grouping Logic:** When used in a group (Tag Cloud), tags must wrap to the next line when horizontal space is restricted.

---

## 6. Designer & Author Guidelines

- **Label Length:** Maximum of 2 words.
- **Word Choice:** Use adjectives rather than verbs for labels.
- **Grouping:** Removable tags should always be used in groups. Never use a single Removable Tag to filter content on a page.
- **Accessibility:** Maintain consistent coloring across tags for easy identification. Ensure all custom colors meet the minimum AAA/AA contrast requirements.

---

## 7. Specifications

### Component Anatomy

- Container
- Label
- Icon

---

### Size: Medium

| Element | Property | Value |
|---------|----------|-------|
| **Container** | Height | 32px |
| **Container** | Radius | `var(--radius-tag)` — 80px (pill) |
| **Label** | Font | `var(--text-body-s)` — 16px |
| **Icon** | Size | S (16px) |

### Size: Small

| Element | Property | Value |
|---------|----------|-------|
| **Container** | Height | 24px |
| **Container** | Radius | `var(--radius-tag)` — 80px (pill) |
| **Label** | Font | `var(--text-body-xs)` — 14px |
| **Icon** | Size | S (16px) |

---

## 8. Tag Kinds

### Removable

- This type of Tag is **not a link** and can either be checked or unchecked.
- It enables the user to multi-select content categories.

### Link

- Clicking anywhere on the Tag will trigger an action which is usually the population of a relevant content view.
- When placed at the top of content or product listing, they can provide in-page filtering.

---

## 9. State Specifications

> Same properties apply to both kinds: **Removable** and **Link** tags.

### Rest States

| State | Label Color | Icon Color | Pill Border | Pill Background |
|-------|------------|-----------|------------|----------------|
| **Normal** | `var(--grey-100)` | `var(--grey-100)` | 1px solid `var(--grey-80)` | none |
| **Hover** | `var(--sparkle-80)` | `var(--sparkle-80)` | 1px solid `var(--grey-80)` | none |
| **Pressed** | `var(--sparkle-80)` | `var(--sparkle-80)` | 1px solid `var(--sparkle-20)` | none |
| **Focus** | `var(--sparkle-80)` | `var(--sparkle-80)` | 4px solid `var(--sparkle-80)` | none |
| **Disabled** | Same as Normal | Same as Normal | Same as Normal | Same as Normal |

> **Disabled:** Same aspect as Normal with general opacity: 30%.

### Active States

| State | Label Color | Icon Color | Pill Border | Pill Background |
|-------|------------|-----------|------------|----------------|
| **Normal** | `var(--sparkle-80)` | `var(--sparkle-80)` | none | `var(--sparkle-20)` |
| **Hover** | `var(--sparkle-80)` | `var(--sparkle-80)` | none | `var(--sparkle-30)` |
| **Pressed** | `var(--sparkle-80)` | `var(--sparkle-80)` | 1px solid `var(--grey-40)` | none |
| **Focus** | `var(--sparkle-80)` | `var(--sparkle-80)` | 4px solid `var(--sparkle-80)` | `var(--sparkle-30)` |
| **Disabled** | Same as Active Normal | Same as Active Normal | Same as Active Normal | Same as Active Normal |

> **Disabled:** Same aspect as Active Normal with general opacity: 30%.

---

## 10. Accessibility (A11y)

- **Focusable:** Must be reachable via Tab and activatable via Space or Enter.
- **Screen Readers:**
  - Link tags: announce as "link" with label text.
  - Removable tags: announce as "toggle" or "checkbox" with checked/unchecked state.
- **Keyboard Navigation:** Full Tab support with visible Focus state.
- **Contrast:** All custom colors must meet minimum AA contrast requirements.

---

## 11. Token Mapping (CSS Variables)

| Spec Token | CSS Variable |
|-----------|-------------|
| `$theme/primary/grey-100` | `var(--grey-100)` |
| `$theme/primary/grey-80` | `var(--grey-80)` |
| `$theme/primary/grey-40` | `var(--grey-40)` |
| `$theme/sparkle/80` | `var(--sparkle-80)` |
| `$theme/sparkle/30` | `var(--sparkle-30)` |
| `$theme/sparkle/20` | `var(--sparkle-20)` |
| `$body-s` | `var(--text-body-s)` — 16px |
| `$body-xs` | `var(--text-body-xs)` — 14px |
| `$radius/tag` | `var(--radius-tag)` — 80px |
| `$s` (icon size) | 16px |

---

## 12. Related Documentation

- **Badge:** `/guidelines/MD/Component/badge.md`
- **Button:** `/guidelines/MD/Component/button.md`
- **Selector:** `/guidelines/MD/Component/selector.md`
- **Icon:** `/guidelines/MD/Component/icon.md`
- **Design Tokens:** `/src/styles/theme.css`

---
