# Breadcrumb — JDS Component Style Guide

## Overview

Breadcrumbs are a **navigation system** used to show hierarchy and navigational context for a user's location within a website's information architecture. They help users understand where they are and move between levels.

The component lives in `/src/app/components/ui/breadcrumb.tsx`.

All styling uses JDS design tokens from `/src/styles/theme.css`.
Typography uses JioType exclusively per typography.md.
Icons use `fill="currentColor"` per icon.md.

---

## Typography Rules (MANDATORY)

> **ALL text in Breadcrumb components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (Breadcrumb)

| Token                   | Value | Usage                                 |
| ----------------------- | ----- | ------------------------------------- |
| `--font-weight-medium`  | 500   | Parent page links, ellipsis           |
| `--font-weight-bold`    | 700   | Current page (last item)              |

### Permitted Sizes (Breadcrumb)

| Token          | Value | Usage                                    |
| -------------- | ----- | ---------------------------------------- |
| `--text-label` | 14px  | All breadcrumb items (links, ellipsis, current page) |

- **Important**: All breadcrumb text uses `var(--text-label)` (14px).
- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Anatomy

A breadcrumb consists of four main parts:

```
Breadcrumb1  >  ...  >  Breadcrumb4  >  Current page
     1       2   3   2       4        2        5
```

### Elements

1. **Parent Page Link(s)** — Interactive links to ancestor pages
2. **Separator** — Visual divider between items (chevron icon)
3. **Ellipsis** — Collapsible overflow menu (when breadcrumb trail exceeds max width)
4. **Intermediate Link** — Parent page immediately before current page
5. **Current Page** — Non-interactive text showing current location

---

## Component Specifications

### Container

```
Height:          24px (fixed)
Max Width:       6 columns (responsive, approximately 696px)
Width:           Content-dependent (auto)
Background:      Transparent
Alignment:       Left
Display:         Inline-flex
Gap:             var(--space-0)  → 0px (items are separated by chevron only)
```

### Parent Page Link

**Typography:**

```
Font Family:     var(--font-family-jiotype)  → JioType
Font Size:       var(--text-label)           → 14px
Font Weight:     var(--font-weight-medium)   → 500
Line Height:     1.5
Text Decoration: None
```

**Colors (States):**

```
Normal:          var(--primary-60)           → #0A2885
Hover:           var(--primary-50)           → #0F3CC9
Focused:         var(--primary-60)           → #0A2885
Visited:         var(--primary-60)           → #0A2885 (no visited state distinction)
Active:          var(--primary-50)           → #0F3CC9
```

**Height:**

```
Height:          24px (fixed)
```

### Ellipsis (Overflow Menu Trigger)

**Typography:**

```
Font Family:     var(--font-family-jiotype)  → JioType
Font Size:       var(--text-label)           → 14px
Font Weight:     var(--font-weight-medium)   → 500
Line Height:     1.5
Content:         "..." (three dots)
```

**Colors (States):**

```
Normal:          var(--primary-60)           → #0A2885
Hover:           var(--primary-50)           → #0F3CC9
Focused:         var(--primary-60)           → #0A2885
Active:          var(--primary-50)           → #0F3CC9
```

**Interactive:**

- Clicking the ellipsis opens a dropdown menu showing hidden breadcrumbs
- Dropdown is left-aligned to the ellipsis
- Uses standard dropdown/menu component

### Current Page (Last Item)

**Typography:**

```
Font Family:     var(--font-family-jiotype)  → JioType
Font Size:       var(--text-label)           → 14px
Font Weight:     var(--font-weight-bold)     → 700
Line Height:     1.5
```

**Color:**

```
Text:            var(--grey-80)              → #000000a6
```

**Behavior:**

- **Not clickable** (no link, no hover state)
- Always the last item in the breadcrumb trail
- Bold weight distinguishes it from parent links

### Separator (Icon)

**Icon:**

```
Icon:            ic_chevron_right (chevron pointing right)
Size:            24px (width and height)
Color:           var(--grey-60)              → #B5B5B5
Fill:            currentColor
```

**Spacing:**

```
Margin:          var(--space-0)              → 0px (no additional spacing)
```

**Behavior:**

- **Not interactive** (no click, no hover)
- Purely decorative
- Cannot be replaced (fixed icon)

---

## States

### 1. Normal (Parent Link)

```
Text Color:      var(--primary-60)           → #0A2885
Font Weight:     var(--font-weight-medium)   → 500
Text Decoration: None
Cursor:          pointer
Background:      Transparent
Border:          None
```

### 2. Hover (Parent Link)

```
Text Color:      var(--primary-50)           → #0F3CC9
Font Weight:     var(--font-weight-medium)   → 500
Text Decoration: Underline (optional)
Cursor:          pointer
Background:      Transparent
Border:          None
Transition:      color 0.2s ease
```

### 3. Focused (Parent Link)

```
Text Color:      var(--primary-60)           → #0A2885
Font Weight:     var(--font-weight-medium)   → 500
Outline:         var(--border-width-thick) solid var(--primary-50)  → 2px solid #0F3CC9
Outline Offset:  2px
Border Radius:   var(--radius)               → 8px
Background:      Transparent
```

### 4. Current Page (Non-Interactive)

```
Text Color:      var(--grey-80)              → #000000a6
Font Weight:     var(--font-weight-bold)     → 700
Text Decoration: None
Cursor:          default
Background:      Transparent
Border:          None
```

---

## Position

Breadcrumbs are placed in the **top left** portion of the page:

- **Below**: Header and navigation
- **Above**: Page title / page content
- **Alignment**: Left-aligned with page content

This placement ensures the "Skip to main content" link allows users to skip all navigation links, including breadcrumbs.

---

## Variants

### 1. Default Breadcrumbs (Without Ellipsis)

Standard breadcrumb trail when all items fit within max width.

```
Structure:       Link1 > Link2 > Link3 > Current page
Max Items:       No limit (as long as total width < max width)
```

#### Usage

```tsx
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink href="/category">Category</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Current page</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

---

### 2. Overflowing Breadcrumbs (With Ellipsis)

Breadcrumb trail with collapsed items when exceeding max width.

```
Structure:       Link1 > ... > Link(n-1) > Current page
Collapsed Items: All intermediate links between first and parent of current page
Ellipsis:        Interactive (click to show dropdown menu)
```

#### Truncation Rules

When breadcrumbs exceed max width, apply these rules in order:

**Rule 1: Collapse intermediate breadcrumbs**

```
Breadcrumb1 > ... > Breadcrumb(n-1) > Current page
```

- Show: First breadcrumb, ellipsis, parent breadcrumb, current page
- Hide: All intermediate breadcrumbs (inside ellipsis dropdown)

**Rule 2: Truncate first breadcrumb label (if still exceeds max width)**

```
Maximum width:   248px
Truncation:      "Long breadcrumb name..." (ellipsis at end)
```

**Rule 3: Truncate parent breadcrumb label (if still exceeds max width)**

```
Maximum width:   248px
Truncation:      "Long breadcrumb name..." (ellipsis at end)
```

**Rule 4: Truncate current page label (if still exceeds max width)**

```
Maximum width:   248px
Truncation:      "Long breadcrumb name..." (ellipsis at end)
```

**Special Case: 2-Level Breadcrumbs**

For breadcrumbs with only 2 levels (`Breadcrumb1 > Current page`):

- **No ellipsis option** (always show both items)
- Truncate individual labels if necessary
- Never hide the current page

#### Usage

```tsx
<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink href="/">Home</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbEllipsis>
        <BreadcrumbDropdown>
          <BreadcrumbLink href="/level2">Level 2</BreadcrumbLink>
          <BreadcrumbLink href="/level3">Level 3</BreadcrumbLink>
          <BreadcrumbLink href="/level4">Level 4</BreadcrumbLink>
        </BreadcrumbDropdown>
      </BreadcrumbEllipsis>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbLink href="/parent">Parent page</BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator />
    <BreadcrumbItem>
      <BreadcrumbPage>Current page</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

---

## Behavior

### Ellipsis Dropdown

When clicking the ellipsis (`...`):

1. **Opens**: Dropdown menu showing hidden breadcrumbs
2. **Alignment**: Left-aligned to ellipsis
3. **Content**: List of hidden breadcrumb links
4. **Spacing**: Standard dropdown spacing (`var(--space-2)` between items)
5. **Dismissal**: Click outside or press Escape to close

### Text Truncation

When breadcrumb labels are truncated:

```
Max Width:       248px per label
Truncation:      "Long breadcrumb name..."
Text Overflow:   ellipsis
White Space:     nowrap
Overflow:        hidden
```

### No Wrapping

- Breadcrumbs **never wrap** to multiple lines
- Always display on a single horizontal line
- Use ellipsis/truncation to fit within max width

---

## Spacing

### Container

```
Padding:         var(--space-0)              → 0px
Gap:             var(--space-0)              → 0px (items separated by chevron only)
```

### Items

```
Gap:             var(--space-0)              → 0px (no gap — chevron provides separation)
```

### Separator (Chevron)

```
Margin Left:     var(--space-0)              → 0px
Margin Right:    var(--space-0)              → 0px
```

### Dropdown Menu (Ellipsis)

```
Padding:         var(--space-2)              → 8px
Gap (Items):     var(--space-2)              → 8px
```

---

## Colors

### Parent Links

| State      | Token            | Value    |
| ---------- | ---------------- | -------- |
| Normal     | `--primary-60`   | #0A2885  |
| Hover      | `--primary-50`   | #0F3CC9  |
| Focused    | `--primary-60`   | #0A2885  |
| Active     | `--primary-50`   | #0F3CC9  |

### Ellipsis

| State      | Token            | Value    |
| ---------- | ---------------- | -------- |
| Normal     | `--primary-60`   | #0A2885  |
| Hover      | `--primary-50`   | #0F3CC9  |
| Focused    | `--primary-60`   | #0A2885  |
| Active     | `--primary-50`   | #0F3CC9  |

### Current Page

| State      | Token            | Value       |
| ---------- | ---------------- | ----------- |
| Default    | `--grey-80`      | #000000a6   |

### Separator

| State      | Token            | Value    |
| ---------- | ---------------- | -------- |
| Default    | `--grey-60`      | #B5B5B5  |

---

## Interactions

### Mouse

- **Click**: Triggers navigation to parent page (opens link)
- **Hover**: Changes link color to `--primary-50` (hover state)
- **Ellipsis Click**: Opens dropdown menu showing hidden breadcrumbs
- **Separator**: Not interactive (no click, no hover)

### Keyboard

- **Tab**: Navigate forward through breadcrumb links
- **Shift + Tab**: Navigate backward through breadcrumb links
- **Enter**: Activate focused link (navigate to page)
- **Escape**: Close ellipsis dropdown (if open)
- **Space**: Activate focused link (alternative to Enter)

### Focus Management

- Focus visible indicator: 2px outline with `--primary-50` color
- Focus moves sequentially through breadcrumb links
- Ellipsis is included in tab order (when present)
- Current page is not included in tab order (not interactive)

---

## Usage Guidance

### When to Use Breadcrumbs

✅ **Use breadcrumbs when:**

- User is **more than 1 level** deep in navigation hierarchy
- Website has a **hierarchical structure** (e.g., e-commerce, documentation)
- Current page does **not have its own navigation**
- User needs to **quickly go back** to a parent page
- Users are likely to have **landed from external sources** (e.g., search engines)
- Other navigation elements are **hidden or collapsed** (e.g., sidebar, mega menu)

### When NOT to Use Breadcrumbs

❌ **Don't use breadcrumbs when:**

- Website has a **flat structure** (single-level navigation)
- User is in a **transactional journey** (checkout, multi-step form)
- Showing **linear progress** (use stepper/progress indicator instead)
- Navigation structure is **unclear or orphaned**
- Other navigation already shows **hierarchy clearly** (redundant)
- Showing **session history** (breadcrumbs show structure, not browsing history)

### Hierarchy Rules

- **Highest level**: Homepage or section root (based on context)
- **Structure**: Reflects information architecture, not user's browsing path
- **Linear progression**: Each level deeper in hierarchy
- **Last item**: Always current page (recommended) or parent page

### Current Page Display

**Recommendation**: Include current page as last item in breadcrumb trail.

**Option 1 (Recommended)**: Show current page in breadcrumbs

```
Home > Category > Current page
```

**Option 2**: Hide current page, but show page title separately

```
Home > Category
──────────────────
Current page (as H1)
```

**Rule**: For 2-level breadcrumbs (`Breadcrumb1 > Current page`), **never hide** the current page.

---

## Content Guidelines

### Label Best Practices

✅ **Do:**

- Use **short, clear labels** that reflect the page or section
- Match labels to **page titles exactly** (for screen readers and consistency)
- Start with **highest level** and progress deeper
- Use **sentence case** (e.g., "Product category", not "Product Category")

❌ **Don't:**

- Use **long, verbose labels** (truncate if necessary)
- Include **unnecessary words** (e.g., "Page" suffix)
- Show **more than 6-7 levels** (consider information architecture redesign)

### Link Behavior

✅ **Do:**

- Make all items **interactive links** except the current page
- Link to the **actual parent pages** (not placeholder URLs)
- Ensure links are **keyboard accessible**

❌ **Don't:**

- Make the **current page a link** (if showing it)
- Show links **after the current page** (no future/sibling pages)
- Use breadcrumbs for **lateral navigation** (use tabs or sidebar instead)

---

## Do's and Don'ts

### ✅ Do: Remove link from current page

```
Women > Footwear > Flip flop & slippers
                    ─────────────────────
                    (Bold, no link)
```

If the current page is the last item, do **not** make it a link.

---

### ❌ Don't: Show links after current page

```
Home > Movies > Horror > The Ring
                         ────────
                         (Current page)
```

Do **not** display links to pages after the current page.

---

### ❌ Don't: Use as primary navigation

```
Home > Explore > More itineraries
```

Do **not** use breadcrumbs as the primary way to navigate. They supplement other navigation.

---

### ❌ Don't: Show session history

```
Visit > Exhibitions and events > Collection > Galleries > Virtual galleries
```

Breadcrumbs show **site structure**, not the user's browsing history.

---

### ❌ Don't: Wrap to multiple lines

```
Home > All categories > Groceries
Home and kitchen > Dining >
```

Breadcrumbs must always be **single-line**. Use ellipsis/truncation instead.

---

### ❌ Don't: Modify for lateral navigation

```
Character styles
Object styles          ← Don't use breadcrumbs for this
Work with styles
```

Use alternate navigation (tabs, sidebar) for traversing within a single hierarchy level.

---

## Accessibility (A11y)

### ARIA Attributes

```tsx
<nav aria-label="Breadcrumb">
  <ol role="list">
    <li>
      <a href="/">Home</a>
    </li>
    <li aria-hidden="true">/</li>
    <li>
      <a href="/category">Category</a>
    </li>
    <li aria-hidden="true">/</li>
    <li aria-current="page">Current page</li>
  </ol>
</nav>
```

### Semantic HTML

- Use `<nav>` element with `aria-label="Breadcrumb"`
- Use ordered list `<ol>` to represent hierarchy
- Use list items `<li>` for each breadcrumb
- Mark current page with `aria-current="page"`
- Hide separators from screen readers with `aria-hidden="true"`

### Keyboard Support

| Key            | Action                                |
| -------------- | ------------------------------------- |
| `Tab`          | Move focus forward through links      |
| `Shift + Tab`  | Move focus backward through links     |
| `Enter`        | Activate focused link                 |
| `Space`        | Activate focused link (alternative)   |
| `Escape`       | Close ellipsis dropdown (if open)     |

### Focus Visible

```
Outline:         var(--border-width-thick) solid var(--primary-50)  → 2px solid #0F3CC9
Outline Offset:  2px
Border Radius:   var(--radius)                                       → 8px
```

### Screen Reader Requirements

- Breadcrumb items **must match page titles exactly**
- Separators should be **hidden from screen readers** (`aria-hidden="true"`)
- Current page should be announced with **"Current page"** or `aria-current="page"`
- Ellipsis button should announce **"Show hidden breadcrumbs"** or similar

### Color Contrast

- **Parent links**: `--primary-60` on white → 8.5:1 (WCAG AAA ✓)
- **Current page**: `--grey-80` on white → 7.1:1 (WCAG AAA ✓)
- **Separator**: `--grey-60` on white → 2.8:1 (Decorative, no text)

---

## Design Token Reference

### Typography

| Token                   | Value   | Usage                                 |
| ----------------------- | ------- | ------------------------------------- |
| `--text-label`          | 14px    | All breadcrumb text                   |
| `--font-weight-medium`  | 500     | Parent links, ellipsis                |
| `--font-weight-bold`    | 700     | Current page                          |
| `--font-family-jiotype` | JioType | Font family (all breadcrumb text)     |

### Colors

| Token              | Value       | Usage                           |
| ------------------ | ----------- | ------------------------------- |
| `--primary-60`     | #0A2885     | Parent links (normal, focused)  |
| `--primary-50`     | #0F3CC9     | Parent links (hover, active)    |
| `--grey-80`        | #000000a6   | Current page text               |
| `--grey-60`        | #B5B5B5     | Separator (chevron)             |

### Spacing

| Token        | Value | Usage                               |
| ------------ | ----- | ----------------------------------- |
| `--space-0`  | 0px   | Container padding, item gap         |
| `--space-2`  | 8px   | Dropdown menu padding/gap           |

### Borders

| Token                  | Value | Usage                        |
| ---------------------- | ----- | ---------------------------- |
| `--border-width-thick` | 2px   | Focus outline width          |

### Radius

| Token       | Value | Usage                        |
| ----------- | ----- | ---------------------------- |
| `--radius`  | 8px   | Focus outline border radius  |

---

## Props

| Prop           | Type                  | Default | Description                                      |
| -------------- | --------------------- | ------- | ------------------------------------------------ |
| `separator`    | `React.ReactNode`     | `>`     | Custom separator element (default: chevron icon) |
| `className`    | `string`              | —       | Additional CSS classes for container             |
| `aria-label`   | `string`              | `"Breadcrumb"` | Accessible label for breadcrumb navigation |
| `children`     | `React.ReactNode`     | —       | Breadcrumb items and separators                  |

---

## Implementation Checklist

When implementing breadcrumb components, verify:

- [ ] Uses `font-family: var(--font-family-jiotype)` for all text
- [ ] All text uses `var(--text-label)` (14px)
- [ ] Parent links use `var(--font-weight-medium)` (500)
- [ ] Current page uses `var(--font-weight-bold)` (700)
- [ ] Parent link color is `var(--primary-60)` (normal) and `var(--primary-50)` (hover)
- [ ] Current page color is `var(--grey-80)`
- [ ] Separator uses chevron icon with `var(--grey-60)` color
- [ ] Focus outline is 2px with `var(--primary-50)` color
- [ ] Current page is **not a link** (no href attribute)
- [ ] Includes proper ARIA attributes (`aria-label`, `aria-current`)
- [ ] Separators are hidden from screen readers (`aria-hidden="true"`)
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Ellipsis opens dropdown when clicked (for overflowing breadcrumbs)
- [ ] Labels truncate at 248px max width (when necessary)
- [ ] No wrapping to multiple lines (single-line only)
- [ ] No custom/hardcoded colors, spacing, or typography values

---

## Related Components

- **Link**: Parent page links use link styling and behavior
- **Dropdown**: Ellipsis uses dropdown component for overflow menu
- **Icon**: Chevron separator uses icon component

---

## Browser Compatibility

- Modern browsers with CSS flexbox support
- Truncation requires `text-overflow: ellipsis` and `white-space: nowrap`
- Focus-visible pseudo-class for keyboard focus indicators
