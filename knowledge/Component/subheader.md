# SubHeader — JDS Component Style Guide

## Overview

The SubHeader is a sticky secondary navigation bar that sits directly below the Header. It provides horizontally-scrollable tab navigation for page-specific sections (e.g., Prepaid, Postpaid, True 5G on the Mobile page, or Discover, Locate Us on the Support page).

**Background is `var(--primary-20)`** (#E8E8FC) — a light purple tint that visually separates it from the white Header above and the white page content below.

**Tab alignment: Tabs start from the same horizontal position as the Jio logo** in the Header. This is achieved by wrapping tabs in a `container mx-auto px-4 md:px-10` matching the Header's container padding.

All styling uses JDS design tokens exclusively. No hardcoded hex values.

---

## Visual Structure

```
┌──────────────────────────────────────────────────────────────────────┐
│  bg: --primary-20 | border-bottom: 1px solid --grey-40 | sticky     │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────────┐│
│  │ container mx-auto px-4 md:px-10 (matches Header container)      ││
│  │                                                                  ││
│  │ Discover  Prepaid  Postpaid  True 5G  Intl Services  Devices ...││
│  │ ▂▂▂▂▂▂▂▂                                                        ││
│  │ (active underline)                            → scrolls right    ││
│  └──────────────────────────────────────────────────────────────────┘│
│                                                                      │
│  Tab start aligns with Jio logo in Header above                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Container

| Property          | Value                                                 |
| ----------------- | ----------------------------------------------------- |
| Position          | `sticky top-16 z-40` (below 64px Header)              |
| Width             | `w-full`                                              |
| Background        | **`var(--primary-20)`** (#E8E8FC) — MANDATORY         |
| Border-bottom     | `1px solid var(--grey-40)` (#E0E0E0)                  |
| Inner container   | `container mx-auto px-4 md:px-10` (matches Header)    |
| Overflow          | `overflow-x-auto` with hidden scrollbar               |

### Scrollbar Hiding

```css
scrollbarWidth: 'none'       /* Firefox */
msOverflowStyle: 'none'     /* IE/Edge */
::-webkit-scrollbar { display: none; }  /* Chrome/Safari */
```

---

## Tab Alignment (MANDATORY)

> **Tabs must start from the same horizontal position as the Jio logo in the Header.** This is achieved by using the same container and padding as the Header: `container mx-auto px-4 md:px-10`.

### Prohibited patterns

```tsx
/* PROHIBITED — tabs not aligned with Header */
<TabsList style={{ paddingLeft: 'var(--space-4)' }}>  /* uses its own padding */

/* PROHIBITED — no container wrapper */
<div className="w-full overflow-x-auto">
  <TabsList>  /* starts from viewport edge, not logo position */

/* CORRECT — same container as Header */
<div className="container mx-auto overflow-x-auto px-4 md:px-10">
  <TabsList style={{ backgroundColor: 'transparent' }}>
```

---

## Tabs Component

| Property            | Value                                          |
| ------------------- | ---------------------------------------------- |
| Component           | `Tabs` > `TabsList` > `TabsTrigger`            |
| TabsList display    | `inline-flex w-max` (allows horizontal scroll) |
| TabsList height     | `h-auto`                                       |
| TabsList background | `transparent` (inherits primary-20 from parent)|
| TabsList gap        | `var(--space-6)` (24px, `$space-m`)           |
| TabsList padding    | `p-0` (container handles padding)              |
| TabsList radius     | `rounded-none`                                 |

---

## Tab Trigger Styling

| Property                  | Value                                          |
| ------------------------- | ---------------------------------------------- |
| Font-family               | `var(--font-family-jiotype)`                   |
| Font-size                 | `var(--text-label)` (14px)                    |
| Font-weight (active)      | `var(--font-weight-bold)` (700)               |
| Font-weight (inactive)    | `var(--font-weight-medium)` (500)             |
| Color (active)            | `var(--primary-50)` (#3535F3)                  |
| Color (inactive)          | `var(--grey-80)` (rgba(0,0,0,0.65))           |
| Padding horizontal        | `var(--space-3)` (12px)                       |
| Padding vertical          | `var(--space-3)` (12px)                       |
| Border-bottom (active)    | `2px solid var(--primary-50)`                  |
| Border-bottom (inactive)  | `2px solid transparent`                        |
| Background                | `transparent`                                  |
| White-space               | `nowrap`                                       |
| Border-radius             | `none` (rounded-none)                          |
| Transition                | `color 0.2s, border-color 0.2s`               |
| Cursor                    | `pointer`                                      |

---

## SubHeader Variants

### Mobile Page SubHeader

| Tab name                | Default active |
| ----------------------- | -------------- |
| Discover                | Yes            |
| Prepaid                 |                |
| Postpaid                |                |
| True 5G                 |                |
| International Services  |                |
| Devices                 |                |
| Apps                    |                |
| Recharge                |                |
| Get Jio SIM             |                |
| Pay Bills               |                |

### Support Page SubHeader

| Tab name      | Default active |
| ------------- | -------------- |
| Discover      | Yes            |
| Locate Us     |                |
| Track Order   |                |
| Contact Us    |                |

### Shop Page SubHeader

| Tab name           | Default active |
| ------------------ | -------------- |
| All Products       | Yes            |
| Connectivity       |                |
| Entertainment      |                |
| Smart Devices      |                |
| Business Solutions |                |

---

## Design Tokens Used — Summary

### Colors

| Token              | Usage                                         |
| ------------------ | --------------------------------------------- |
| `--primary-20`     | **SubHeader background** (#E8E8FC) — MANDATORY|
| `--primary-50`     | Active tab text + underline                   |
| `--grey-80`        | Inactive tab text                             |
| `--grey-40`        | Bottom border                                 |

### Typography

| Token                    | Usage                      |
| ------------------------ | -------------------------- |
| `--font-family-jiotype`  | All tab text               |
| `--font-weight-bold`     | Active tab (700)           |
| `--font-weight-medium`   | Inactive tab (500)         |
| `--text-label`           | Tab font size (14px)       |

### Spacing

| Token              | Usage                             |
| ------------------ | --------------------------------- |
| `--space-3`        | Tab padding (horizontal + vertical)|
| `--space-4`        | Container padding (mobile)        |
| `px-10` (40px)     | Container padding (md+)           |

---

## Responsive Behavior

| Breakpoint | Behavior                                              |
| ---------- | ----------------------------------------------------- |
| Mobile     | Tabs scroll horizontally, `px-4` container padding    |
| md+        | Tabs scroll horizontally, `px-10` container padding   |

Tabs are always horizontally scrollable regardless of breakpoint. The scrollbar is hidden for a clean appearance.

---

## Accessibility

- All tab triggers are keyboard-focusable
- Active tab is visually indicated by `primary-50` color and 2px bottom border
- Tab list uses `role="tablist"` (provided by Radix Tabs)
- Individual tabs use `role="tab"` with `aria-selected` (provided by Radix Tabs)

---

## File Dependencies

- `./ui/tabs` — Tabs, TabsList, TabsTrigger
- `/src/styles/theme.css` — All JDS design tokens

---

## Usage Guidelines

1. **Background must be `var(--primary-20)`** — never white, grey, or any other color.
2. **Tabs must align with the Header logo** — always use `container mx-auto px-4 md:px-10`.
3. **TabsList background must be `transparent`** — the parent div provides the primary-20 background.
4. **Font-family** must always be `var(--font-family-jiotype)`.
5. **Font sizes** use `var(--text-label)` (14px) only — never Tailwind text utilities.
6. **Active state** uses `var(--primary-50)` for both text color and 2px bottom border.
7. **Inactive state** uses `var(--grey-80)` text with `var(--font-weight-medium)` and transparent bottom border.
8. **Never** add additional left padding to TabsList — the container padding handles alignment.
9. **This SubHeader pattern must be followed** on all pages that use a secondary navigation strip.