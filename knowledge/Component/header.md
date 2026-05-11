# Header — JDS Component Specification

## Overview

The Header is the primary navigation bar for all Jio pages. It supports two visual themes (**Bold** and **Light**) and adapts responsively from full desktop navigation down to a collapsed mobile hamburger drawer.

All styling uses JDS design tokens exclusively from `/src/styles/theme.css`. No hardcoded hex values. All icons from `@jds/core-icons` with `fill="currentColor"`.

---

## Typography Rules (MANDATORY)

> **ALL text in the Header must use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- **Never** use any other font-family anywhere.

### Permitted Weights

| Token                       | Value | Usage                                           |
| --------------------------- | ----- | ----------------------------------------------- |
| `--font-weight-medium`      | 500   | Result rows, quick link items                   |
| `--font-weight-bold`        | 700   | Nav links, Cancel button, Clear, section headings |

### Permitted Sizes

| JDS Token       | CSS Variable          | Value | Usage                              |
| --------------- | --------------------- | ----- | ---------------------------------- |
| `$heading-xxs`  | `--text-label`        | 14px  | Nav links, desktop results         |
| `$body-s`       | `--text-label`        | 14px  | Cancel button                      |
| —               | `--text-button-large` | 18px  | Mobile drawer links                |
| —               | `--text-button`       | 16px  | Search input text                  |
| —               | `--text-base`         | 16px  | Mobile result items                |
| —               | `--text-caption`      | 11px  | Section headings (uppercase)       |

---

## Grid Integration

The Header does **not** use the section-level grid system. It is a full-width sticky bar that spans the entire viewport. Internal layout uses flexbox with container padding tokens.

| Property                | Value                                                    |
| ----------------------- | -------------------------------------------------------- |
| Container max-width     | `var(--container-max-width)` (1280px)                    |
| Container centering     | `margin: 0 auto`                                        |
| Padding (mobile, < md)  | `var(--container-padding-mobile)` (16px / `--space-4`)   |
| Padding (desktop, md+)  | `var(--container-padding-desktop)` (40px / `--space-10`) |
| Inner layout            | `flex items-center justify-between`                      |
| Height                  | `h-16` (64px)                                            |

The Header bar itself is `w-full` with `sticky top-0 z-50`. The inner container uses `container mx-auto` which applies the stopper and padding from the grid system.

---

## Desktop Default Layout

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│  [Prefix] [Logo]  ←── 64px ──→  [Link1] [Link2] ... [Link6]      [🔍] [⚙] [👤]    │
│  Burger/  JioDot                  Nav links (left-aligned)       Search Util Prof    │
│  Back/    Icon                    $body-s-bold / max 6                               │
│  Close                                                                               │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### Key Layout Rule

**Links are placed directly after the Logo**, separated by `var(--space-16)` (64px). They belong to the left group, NOT centred. Right group is pushed via `justify-between`.

---

## Theme Variants

### Bold Theme

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |
| Background            | `var(--primary-50)`                           |
| Prefix button         | `Button variant="tertiary" appearance="contrast"` |
| Link text color       | `var(--primary-inverse)` (white)              |
| Cancel text color     | `var(--primary-inverse)` (white)              |
| Search / Utility      | `Button variant="tertiary" appearance="contrast"` |
| Profile avatar bg     | `var(--primary-20)`                           |

### Light Theme (Default)

| Property              | Value                                         |
| --------------------- | --------------------------------------------- |
| Background            | `var(--primary-background)` (white)           |
| Border-bottom         | `1px solid var(--grey-40)`                    |
| Prefix button         | `Button variant="tertiary" appearance="default"` |
| Link text color       | `var(--grey-80)`, hover `var(--grey-100)`     |
| Link active color     | `var(--primary-50)` + bottom border           |
| Cancel text color     | `var(--primary-50)`                           |
| Search / Utility      | `Button variant="tertiary" appearance="default"` |
| Profile avatar bg     | `var(--primary-20)`                           |

---

## Search Behaviour — Desktop (lg+)

### Activation

When the user clicks the search icon:

1. **All header elements are hidden** except the logo
2. The **search bar expands and animates** to the centre of the header with a scale + opacity entrance (Motion)
3. A **"Cancel" text button** appears on the right to abandon search
4. A **fly-out overlay** appears below the header on top of page content

### Desktop Header — Search Active State

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│  [Logo]              ┌─────────────────────────────────┐                  [Cancel]   │
│  JioDot              │  🔍  Search input...         ✕  │                   text btn  │
│                      └─────────────────────────────────┘                             │
│                              498px, centred                                           │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### Search field (in header)

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Width            | `498px` (aligned to 12-col / 1440px desktop grid)    |
| Position         | Centred in the header bar via flex                    |
| Background       | `var(--grey-20)`                                     |
| Border           | `1px solid var(--grey-40)`                           |
| Border-radius    | `var(--radius-button)` (pill)                        |
| Animation        | `motion` — initial: `opacity: 0, scale: 0.92` → animate: `opacity: 1, scale: 1`, 250ms ease-out |
| Submit icon      | `IcSearch` (clickable, submits the query)            |
| Clear icon       | `IcCloseRemove` (appears when input has value)       |
| Font             | `--text-button` (16px), `--font-weight-normal`       |

### Cancel button

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Element          | Native `<button>`, text-only (no icon)               |
| Label            | "Cancel"                                             |
| Font             | `--text-label` (14px), `--font-weight-bold`          |
| Color (Light)    | `var(--primary-50)`                                  |
| Color (Bold)     | `var(--primary-inverse)`                             |
| Action           | Dismisses search, restores default header state      |

### Fly-out overlay (below header)

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Position         | `fixed`, starts at `top: 64px`, covers remaining viewport |
| Z-index          | `z-[45]` (below header z-50)                         |
| Backdrop         | `rgba(0, 0, 0, 0.4)` — clicking dismisses search    |
| Dropdown width   | `498px` (centred, same as search field)              |
| Dropdown bg      | `var(--global-white)`                                |
| Border-radius    | `var(--radius)` (8px)                                |
| Shadow           | `0 8px 32px rgba(0, 0, 0, 0.12)`                    |
| Max-height       | `calc(100vh - 100px)`, scrollable                    |
| Animation        | `motion` — initial: `opacity: 0, y: -8` → animate: `opacity: 1, y: 0`, 200ms ease-out |
| Exit animation   | Reverse of enter (opacity 0, y -8)                   |

---

### Pre-typing state (search activated, no input yet)

The fly-out shows two possible sections:

1. **Recent Searches** (if user has previous searches)
   - Heading: "RECENT SEARCHES" (uppercase, `--text-caption`, `--font-weight-bold`, `--grey-80`)
   - "Clear" button on the right — clears all recent searches from localStorage
   - Up to 5 items, each with `IcTime` clock icon + label + `IcChevronRight`
   - Stored in `localStorage` under key `jio-recent-searches`

2. **Quick Links** (always shown)
   - Heading: "QUICK LINKS" (same heading style)
   - Up to 5 items, each with label + `IcChevronRight`
   - Navigates to the relevant page on click

```
┌────────────────────────────────────┐
│  RECENT SEARCHES            Clear  │
│  🕐  5G Plans                   ›  │
│  🕐  Recharge                   ›  │
│  🕐  JioFiber                   ›  │
│                                    │
│  QUICK LINKS                       │
│  Prepaid Plans                  ›  │
│  Postpaid Plans                 ›  │
│  JioFiber Plans                 ›  │
│  JioAirFiber                    ›  │
│  Bill Payment                   ›  │
└────────────────────────────────────┘
```

### Active typing state (user is typing)

As the user types, the fly-out content changes to search recommendations:

1. **"Based on your recent searches"** — recommendations matching recent search terms (with `IcTime` icon)
2. **"Suggestions"** — all other matching recommendations (with `IcSearch` icon)
3. If no results: "No results found for '...'" message

- Clicking a recommendation navigates to its page and saves it to recent searches
- Pressing **Enter** or clicking the **magnifier icon** submits the search
- Submitting adds the query to recent searches and navigates to `/?q=<encoded-query>`

```
┌────────────────────────────────────┐
│  BASED ON YOUR RECENT SEARCHES     │
│  🕐  Recharge prepaid mobile       │
│  🕐  Recharge plans under ₹500     │
│                                    │
│  SUGGESTIONS                       │
│  🔍  5G coverage in my area        │
│  🔍  5G unlimited plans            │
│  🔍  JioFiber broadband plans      │
└────────────────────────────────────┘
```

---

## Search Behaviour — Mobile (< lg)

### Activation

When the user taps the search icon:

1. A **full-page overlay** slides in (`fixed inset-0`), replacing the existing content
2. The top bar shows: **Back button** (`IcBack`) + **expanded search input** (pill-shaped, `--grey-20` bg)
3. Below: quick links and recent searches (same as desktop pre-typing state)

### Mobile Search — Layout

```
┌──────────────────────────────┐
│  [←]  [🔍  Search...     ✕] │  ← 64px header
├──────────────────────────────┤
│  RECENT SEARCHES       Clear │
│  🕐  5G Plans             ›  │
│  🕐  Recharge             ›  │
│                              │
│  QUICK LINKS                 │
│  Prepaid Plans            ›  │
│  Postpaid Plans           ›  │
│  JioFiber Plans           ›  │
│  JioAirFiber              ›  │
│  Bill Payment             ›  │
└──────────────────────────────┘
```

### Mobile active typing

Same as desktop — recommendations replace recent searches and quick links. User submits via keyboard Enter / "Search" CTA.

### Mobile-specific details

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Entry animation  | `motion` — slide from right (`x: 40 → 0`), 250ms   |
| Exit animation   | Reverse slide right                                  |
| Search bg        | `var(--grey-20)`                                     |
| Item font size   | `--text-base` (16px) — larger touch targets          |
| Item padding     | `var(--space-3)` vertical — comfortable tap area     |
| Clear icon       | `IcCloseRemove` (appears when input has value)       |
| Back button      | `IcBack` from `@jds/core-icons`                      |

---

## Recent Searches — Persistence

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Storage          | `localStorage` (key: `jio-recent-searches`)          |
| Max items        | 5 (UX recommendation, configurable)                  |
| Data format      | JSON array of strings `["query1", "query2", ...]`    |
| Add behaviour    | New query prepended; duplicates removed; capped at 5 |
| Clear behaviour  | "Clear" button removes all; key deleted from storage |
| Read timing      | Loaded when search is activated                      |

---

## Search Recommendations — Data

Mock recommendation data is included in the component for demo purposes. In production, this would be replaced by an API call.

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Max displayed    | 8 recommendations                                   |
| Sorting          | Recent-match items appear first, then general matches|
| Match logic      | Case-insensitive substring match on query            |
| Recent-match     | Items whose label contains a recent search term      |
| Recent icon      | `IcTime` (clock)                                     |
| Suggestion icon  | `IcSearch` (magnifier)                               |
| No results       | "No results found for '...'" centred message         |

---

## Navigation Links

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Position         | **After logo**, `var(--space-16)` (64px) gap         |
| Alignment        | Left-aligned (part of the left group)                |
| Visibility       | `hidden lg:flex` (hidden below lg breakpoint)        |
| Max items        | 6                                                    |
| Font             | `--text-label` (14px), `--font-weight-bold` (700)    |
| Active indicator  | `2px solid var(--primary-50)` bottom border          |

### Default Links (in order)

| # | Name       | Route                  |
|---|------------|------------------------|
| 1 | Mobile     | `/mobile`              |
| 2 | Home       | `/home`                |
| 3 | Shop       | `/shop`                |
| 4 | Business   | `/business`            |
| 5 | Support    | `/support`             |
| 6 | Jio Glass  | `/glass`               |

---

## Product Logo / JioDot

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Component        | `IcJioDot` from `@jds/core-icons`                   |
| Size             | `32px` (w-8 h-8)                                    |
| Border radius    | `var(--radius)`                                      |
| Clickable        | `<a>` link to homepage `/`                           |
| Always visible   | Stays visible in both default and search-active states |

---

## Right Group (default state)

| Element          | Component                                            |
| ---------------- | ---------------------------------------------------- |
| Search icon      | `Button` size `sm`, rounded-full, triggers search    |
| Utility icons    | Up to 3 `Button` size `sm`, rounded-full             |
| Profile avatar   | 36px circle, `--primary-20` bg, `IcProfile` fallback   |

---

## Prefix (Hamburger / Back / Close)

| Prefix    | Visibility        | Icon           | Action                        |
| --------- | ----------------- | -------------- | ----------------------------- |
| `burger`  | `lg:hidden`       | `IcBurgerMenu` | Opens mobile nav drawer       |
| `back`    | Always            | `IcBack`       | Navigate back                 |
| `close`   | Always            | `IcClose`      | Dismiss current view          |

---

## Mobile Navigation Drawer

| Property         | Value                                                |
| ---------------- | ---------------------------------------------------- |
| Drawer width     | `clamp(280px, 80vw, 360px)`                         |
| Background       | `var(--global-white)`                                |
| Backdrop         | `rgba(0, 0, 0, 0.5)`                                |
| Link font        | `--text-button-large` (18px), `--font-weight-bold`   |
| Active link      | `var(--primary-50)` color, `var(--primary-20)` bg    |

---

## Responsive Behavior

| Breakpoint       | Nav Links            | Search                            | Hamburger     |
| ---------------- | -------------------- | --------------------------------- | ------------- |
| Mobile (< lg)    | Hidden (in drawer)   | Icon → full-page takeover         | Visible       |
| Desktop (lg+)    | Visible after logo   | Icon → centred bar + fly-out      | Hidden        |

---

## Component Props

```tsx
interface HeaderProps {
  theme?: 'bold' | 'light';
  links?: Array<{ name: string; href: string }>;
  prefix?: 'burger' | 'back' | 'close';
  onPrefixAction?: () => void;
  utilityIcons?: Array<{ icon: JdsIcon; label: string; onClick?: () => void }>;
}
```

---

## Design Tokens Summary

### Spacing

| Token           | Usage                              |
| --------------- | ---------------------------------- |
| `--space-16`    | 64px gap between Logo and Links    |
| `--space-10`    | Container padding desktop (md+)    |
| `--space-4`     | Container padding mobile, panel padding |
| `--space-3`     | Link padding, mobile item padding, input padding |
| `--space-2`     | Dropdown top gap                   |
| `--space-1`     | Link gap, utility icon gap, heading bottom gap |

### Colors

| Token                    | Usage                                            |
| ------------------------ | ------------------------------------------------ |
| `--primary-50`           | Active link, Cancel text (light), link border    |
| `--primary-background`   | Header bg (light)                                |
| `--primary-inverse`      | Text/icons on bold theme                         |
| `--primary-20`           | Avatar bg, active drawer link bg                 |
| `--grey-100`             | Result text, drawer link text                    |
| `--grey-80`              | Nav link color, section headings, subtitle       |
| `--grey-60`              | Placeholder, icons (clock, chevron, magnifier)   |
| `--grey-40`              | Borders, search field border                     |
| `--grey-20`              | Search field bg, hover bg                        |
| `--global-white`         | Dropdown bg, page bg, drawer bg                  |

---

## File Dependencies

- `@jds/core-icons` — `IcJioDot`, `IcBurgerMenu`, `IcSearch`, `IcProfile`, `IcClose`, `IcBack`, `IcChevronRight`, `IcTime`, `IcCloseRemove`
- `motion/react` — `motion`, `AnimatePresence` for search animations
- `./ui/button` — JDS Button component (all icon buttons)
- `react-router` — `useNavigate`, `useLocation` for client-side routing
- `/src/styles/theme.css` — All JDS design tokens

---

## Accessibility

- Logo is a focusable `<a>` link
- All icon buttons have `aria-label` attributes
- Mobile overlays have `role="dialog"` and `aria-modal="true"`
- Escape key dismisses search overlay and drawer
- Result rows are `<button>` elements — keyboard accessible
- Body scroll is locked when overlays are active
- Search input auto-focuses on activation (150ms delay for animation)

---

## Usage Guidelines

1. **All colors** use JDS tokens — never hardcode hex values
2. **Font-family** must always be `var(--font-family-jiotype)`
3. **Font weights** use only token references (400/500/700/900)
4. **Icons** always use `@jds/core-icons` with `fill="currentColor"`
5. **Never** use Tailwind font-size or font-weight utilities
6. **Navigation links** are left-aligned after the logo with 64px gap — never centred
7. **Search active**: Desktop hides all header elements except logo + shows centred search + Cancel; Mobile shows full-page takeover
8. **Recent searches** persist in localStorage; max 5; clearable
9. **Desktop search field + dropdown** are both 498px wide, centred
10. **Max 6 nav links** — if more needed, use secondary navigation