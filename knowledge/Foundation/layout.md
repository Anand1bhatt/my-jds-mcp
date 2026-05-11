# Layout Framework

The Layout Framework defines the structural foundation for all Jio digital products.  
It ensures consistency, scalability, and clarity by providing a unified system for arranging content across devices, screen sizes, and orientations.

This document is the **single source of truth** for JDS-specific layout implementation patterns and rules.

---

## Cross-References

> **📖 For grid system fundamentals, breakpoints, and responsive behavior, see:**
> - [Layout-Grid.md](./Layout-Grid.md) - Grid system, 4-point grid, breakpoints (XS/S/M/L/XL), orientation behavior, responsive grid anatomy

This document focuses on **implementation patterns** specific to JDS pages and components.

---

## 1. Purpose

The layout framework exists to:

- Create consistent visual structure
- Maintain alignment and rhythm across screens
- Support responsive and adaptive layouts
- Reduce design and development effort
- Ensure predictable user experiences

---

## 2. Layout Philosophy

Jio layouts are:

- **Logical** – predictable structure and alignment
- **Responsive** – adaptable across screen sizes
- **Scalable** – works across platforms and products
- **System-driven** – governed by grids and spacing rules

---

## 3. Multi-Platform Support

The layout framework is shared across:

- Web
- Mobile Web
- Android
- iOS

### Rules

- Same grid logic across platforms
- Platform-specific components may vary
- Core spacing and alignment remain unchanged

---

## 4. Governance

- Layout changes require Design System approval
- New layout patterns must follow grid rules
- Exceptions must be documented
- Regular layout audits are recommended

---

## 5. Validation Checklist

✔ Grid aligned (see [Layout-Grid.md](./Layout-Grid.md))  
✔ Responsive across breakpoints (see [Layout-Grid.md](./Layout-Grid.md))  
✔ Orientation safe (see [Layout-Grid.md](./Layout-Grid.md))  
✔ Consistent spacing (see [spacing.md](./spacing.md))  
✔ Platform compatible

---

## 6. Summary

The layout framework is the backbone of all Jio interfaces.  
By following this system, interfaces remain **clean, predictable, and scalable** across devices and platforms.

**If it's not aligned to the grid — it doesn't ship.**

---

# JDS Layout Rules

Canonical specification for page-level layout patterns across all JDS pages.

---

## Section Title Alignment (MANDATORY)

> **All section-level titles and subtitles must be center-aligned — both horizontally centered within the viewport and with `text-align: center` on the text element itself.**

This is a **global rule** that applies to every content section on the page. There are no exceptions for any section.

### What qualifies as a "section title"

- Any `<h2>` or `<h3>` that serves as the primary heading of a content section (e.g. "Recharge or pay bills", "It all starts with a connection", "Explore our new services")
- Any `<p>` or `<span>` that acts as a subtitle directly below a section title

### Required implementation

```tsx
{
  /* Section heading — always center-aligned, 40px Heading/m */
}
<h2
  className="m-0 text-center"
  style={{
    fontFamily: "var(--font-family-jiotype)",
    fontSize: "var(--text-heading-m)",
    fontWeight: "var(--font-weight-black)",
    color: "var(--foreground)",
    lineHeight: 1.2,
    textAlign: "center",
  }}
>
  Section Title Here
</h2>;

{
  /* Optional subtitle / support text — also center-aligned, 18px Body/m */
}
<p
  className="m-0 text-center"
  style={{
    fontFamily: "var(--font-family-jiotype)",
    fontSize: "var(--text-body-m)",
    fontWeight: "var(--font-weight-medium)",
    color: "var(--grey-80)",
    lineHeight: 1.5,
    textAlign: "center",
    marginTop: "var(--space-2)",
    marginBottom: "var(--space-8)",
  }}
>
  Subtitle text here.
</p>;
```

### Rules

1. **`text-align: center`** must be set on the heading/subtitle element (both via the `style` prop AND the Tailwind `text-center` class as a safety net)
2. The heading must live inside a **centered container** (`container mx-auto px-4`)
3. If a subtitle exists, it should be `var(--space-2)` (8px) below the title
4. The gap from the last text element (title or subtitle) to the section content below is `var(--space-8)` (32px) — applied via `marginBottom: 'var(--space-8)'` or `mb-8`
5. **Never left-align** a section title or subtitle

### Prohibited patterns

```tsx
/* PROHIBITED — left-aligned section title */
<h2 style={{ textAlign: 'left' }}>Section Title</h2>

/* PROHIBITED — no text-align specified (inherits left) */
<h2 className="m-0 mb-8">Section Title</h2>

/* PROHIBITED — right-aligned */
<h2 className="text-right">Section Title</h2>
```

---

## Page Structure

The page follows a single-column, full-width layout:

```
┌──────────────────────────────────────────────┐
│  Header (sticky top, z-50)                    │
├──────────────────────────────────────────────┤
│  <main>                                       │
│    Section 1 — Hero Carousel (full-bleed)     │
│    Section 2 — Recharge (centered, max-w-2xl) │
│    Section 3 — Quick Actions (icon shortcuts)  │
│    Section 4 — Grid Banner (2-col cards)      │
│    Section 5 — Connects (2×2 cards)           │
│    Section 6 — Feature Cards (4-col grid)     │
│    Section 7 — Explore Services (3-col cards) │
│  </main>                                      │
├──────────────────────────────────────────────┤
│  Footer (full-width)                          │
└──────────────────────────────────────────────┘
```

### Section wrapper pattern

Every section uses this consistent wrapper:

```tsx
<section
  className="w-full"
  style={{
    paddingTop: "var(--space-12)",
    paddingBottom: "var(--space-12)",
    backgroundColor: "var(--global-white)",
  }}
>
  <div className="container mx-auto px-4">
    {/* Center-aligned title (optional — some sections have no title) */}
    {/* Center-aligned subtitle (optional) */}
    {/* Section content */}
  </div>
</section>
```

### Equal Section Spacing (MANDATORY — all pages)

> **Every `<section>` on every page (`/`, `/mobile`, `/support`, `/business`) must use the same vertical padding: `paddingTop: 'var(--space-12)'` and `paddingBottom: 'var(--space-12)'` (48px each).** This ensures uniform visual rhythm between all sections across the entire application.

- This rule applies to **all new sections** created in the future.
- No section may use a different vertical padding value unless it is a full-bleed hero with no inner content padding (e.g., `SupportHero` which sizes via height, not padding).
- Adjacent sections with the same white background produce a total gap of 96px (48px bottom + 48px top). This is intentional and consistent.

### Rules

| Property                 | Value                                               |
| ------------------------ | --------------------------------------------------- |
| Section background       | `var(--global-white)` — always white                |
| Section vertical padding | `var(--space-12)` (48px) — uniform across all pages |
| Container                | `container mx-auto px-4`                            |
| Title alignment          | `text-align: center` (mandatory)                    |
| Title → content gap      | `var(--space-8)` (32px)                             |
| Title → subtitle gap     | `var(--space-2)` (8px)                              |

---

## Grid Layouts

| Pattern        | Grid classes                                     | Gap     |
| -------------- | ------------------------------------------------ | ------- |
| 2-column cards | `grid grid-cols-1 md:grid-cols-2`                | `gap-5` |
| 3-column cards | `grid grid-cols-1 md:grid-cols-3`                | `gap-5` |
| 4-column cards | `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4` | `gap-6` |

All grids collapse to single-column on mobile.

> **📖 See [Layout-Grid.md](./Layout-Grid.md) for breakpoint definitions (S: 324-619px, M: 620-991px, L: 992-1919px)**

---

## Responsive Container

The `.container` class provides `max-width` breakpoints and overrides Tailwind CSS defaults with `!important` declarations. Horizontal padding is handled by:

- `px-4` (16px) on mobile (XS and S grids: < 768px)
- `px-10` (40px) on tablet (M grid: 768px - 991px)
- No horizontal padding on desktop (L and XL grids: ≥ 992px)

**Container max-width:** 1184px (enforced with `!important` for L and XL grids)

The container follows the L grid layout specification with a 1184px stopper, and removes horizontal padding at 992px and above to allow edge-to-edge layout within the max-width container. All container styles use `!important` to ensure they override Tailwind's default breakpoint-based max-width values (sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px).

---

## Typography Rules

All text must use:

- **Font family:** `var(--font-family-jiotype)` exclusively
- **Font weights:** Only the four permitted JDS weight tokens:
  - `var(--font-weight-normal)` (400)
  - `var(--font-weight-medium)` (500)
  - `var(--font-weight-bold)` (700)
  - `var(--font-weight-black)` (900)
- **No other fonts or weights** are allowed.

> **📖 See [typography.md](./typography.md) for the full typography specification.**