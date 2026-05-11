# Table (Simple Table)

## 1. Overview

**Function:** Simple Tables display information in a tabular data format with rows and columns. They organize information in a way that's easy to scan so that users can look for patterns and develop insights from data.

**How to use:** Use Simple Tables on wide viewports only or whenever their layout can easily fit on the screen — not too many columns.

---

## 2. Anatomy

A Simple Table is composed of columns and rows with the following cell types:

1. **Header cells:** Cells at the top row (or left column) that label the data.
2. **Data cells:** Cells where data is displayed.

### Component Anatomy Elements

1. **Label:** Maximum two lines of text are allowed; text exceeding two lines will be truncated. Paragraphs are not supported.
2. **Vertical divider:** Optional column separator between cells.
3. **Horizontal divider:** Row separator between cells.

---

## 3. States

| State | Description |
|-------|-------------|
| **Header cell** | A header cell at the top row or left column. |
| **Data cell** | A cell where data is displayed. |
| **Data zebra row/column** | A data cell on a table with alternate zebra stripes. |
| **Footer** | Defines the style of the table footer. |

---

## 4. Variants

### Table with Footer

This type of Simple Table can have a footer row at the bottom. The footer uses the same styling as a header but is positioned at the end of the table body.

### Table with Zebra Stripes

Alternating different color backgrounds for each row (or column) helps users keep their place while reading. This style is recommended for larger data sets where the alternating pattern will be clear and not cause confusion that a particular row is highlighted.

> **Note:** Zebra stripes can be either **horizontal** (alternating rows) or **vertical** (alternating columns).

---

## 5. Responsive Behaviour

**All Viewports:** Simple Table is only recommended if the content of the entire table can be comfortably fitted on the screen. For tables that may overflow horizontally, wrap in a scrollable container with `overflow-x: auto`.

---

## 6. Designer Guidelines

### Zebra Stripes

Alternating different color backgrounds for each row is a good way to help users keep their place while reading. This style is recommended for larger data sets where the alternating pattern will be clear and not cause confusion that a particular row is highlighted.

### Align Columns Properly

- Align **textual data** to the left (e.g., Name).
- Align **numeric data not related to size** to the left (e.g., date, zip code, phone number).
- Align **numeric data related to size** to the right (e.g., count, percent).
- Align **headers** according to their column data.

### Content — Header / Body Text

- The table text should clearly convey what the data has in common and its purpose within the UI.
- Column text should be short, concise, and clearly describe the data in the column.
- In cases where a column header/body text is too long, wrap the text to two lines and then truncate the rest of the text. The full text should be shown in a tooltip on hover.
- If the text in one column wraps to two lines, then every column should expand to two lines.

---

## 7. Specifications — Spacing & Size

### Cell Density

#### Condensed Cell

| Element | Property | Value |
|---------|----------|-------|
| **Cell** | Padding vertical | `var(--space-2)` — 8px |
| **Cell** | Padding horizontal | `var(--space-3)` — 12px |

#### Relaxed Cell

| Element | Property | Value |
|---------|----------|-------|
| **Cell** | Padding vertical | `var(--space-3)` — 12px |
| **Cell** | Padding horizontal | `var(--space-4)` — 16px |

### Header Density

#### Condensed Header

| Element | Property | Value |
|---------|----------|-------|
| **Header** | Padding vertical | `var(--space-2)` — 8px |
| **Header** | Padding horizontal | `var(--space-3)` — 12px |

#### Relaxed Header

| Element | Property | Value |
|---------|----------|-------|
| **Header** | Padding vertical | `var(--space-3)` — 12px |
| **Header** | Padding horizontal | `var(--space-4)` — 16px |

---

## 8. State Specifications — Cell Types

### Cell (Default)

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-body-s)` — 16px |
| Horizontal divider | `var(--border-width-thin)` solid `var(--grey-40)` |
| Vertical divider | none |
| Background | none |

### Cell / col-divider on

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-body-s)` — 16px |
| Horizontal divider | `var(--border-width-thin)` solid `var(--grey-40)` |
| Vertical divider | `var(--border-width-thin)` solid `var(--grey-40)` |
| Background | none |

### Cell / Zebra

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-body-s)` — 16px |
| Horizontal divider | none |
| Vertical divider | none |
| Background | `var(--primary-20)` |

### Cell / Zebra / col-divider on

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-body-s)` — 16px |
| Horizontal divider | none |
| Vertical divider | `var(--border-width-thin)` solid `var(--grey-40)` |
| Background | `var(--primary-20)` |

---

## 9. State Specifications — Header Types

### Heading / NoBg

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-heading-xxs)` — 16px, `var(--font-weight-bold)` |
| Horizontal divider | `var(--border-width-header)` solid `var(--grey-40)` (4px) |
| Vertical divider | none |
| Background | none |

### Heading / NoBg / col-divider on

| Property | Value |
|----------|-------|
| Label color | `var(--grey-100)` |
| Label font | `var(--text-heading-xxs)` — 16px, `var(--font-weight-bold)` |
| Horizontal divider | `var(--border-width-header)` solid `var(--grey-40)` (4px) |
| Vertical divider | `var(--border-width-thin)` solid `var(--grey-40)` |
| Background | none |

### Heading / Color (Default)

| Property | Value |
|----------|-------|
| Label color | `var(--global-white)` (`$theme/ui-inverse`) |
| Label font | `var(--text-heading-xxs)` — 16px, `var(--font-weight-bold)` |
| Horizontal divider | none |
| Vertical divider | none |
| Background | `var(--primary-50)` |

### Heading / Color / col-divider on

| Property | Value |
|----------|-------|
| Label color | `var(--global-white)` (`$theme/ui-inverse`) |
| Label font | `var(--text-heading-xxs)` — 16px, `var(--font-weight-bold)` |
| Horizontal divider | none |
| Vertical divider | `var(--border-width-thin)` solid `var(--primary-60)` |
| Background | `var(--primary-50)` |

---

## 10. Accessibility (A11y)

- Use semantic `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<th>`, `<td>` elements.
- Header cells must use `<th>` with appropriate `scope="col"` or `scope="row"`.
- Truncated text must provide the full text via `title` attribute or tooltip on hover.
- Ensure sufficient color contrast between text and backgrounds (minimum AA).
- Tables should have a `<caption>` or `aria-label` describing the table's content.

---

## 11. Token Mapping (CSS Variables)

| Spec Token | CSS Variable | Value |
|-----------|-------------|-------|
| `$theme/greyscale100` | `var(--grey-100)` | #141414 |
| `$theme/greyscale40` | `var(--grey-40)` | #E0E0E0 |
| `$theme/primary20` | `var(--primary-20)` | #E7EBF8 |
| `$theme/primary50` | `var(--primary-50)` | #0F3CC9 |
| `$theme/primary60` | `var(--primary-60)` | #0A2885 |
| `$theme/ui-inverse` | `var(--global-white)` | #FFFFFF |
| `$body-s` (label font) | `var(--text-body-s)` | 16px |
| `$heading-xxs` (header font) | `var(--text-heading-xxs)` | 16px |
| 1px border | `var(--border-width-thin)` | 1px |
| 4px header border | `var(--border-width-header)` | 4px |

---

## 12. Related Documentation

- **Card:** `/guidelines/MD/Component/card.md`
- **Badge:** `/guidelines/MD/Component/badge.md`
- **Section:** `/guidelines/MD/Component/section.md`
- **Design Tokens:** `/src/styles/theme.css`

---
