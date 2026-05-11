# ILL Sub Header — Component Specification

## Overview

The ILL Sub Header is a sticky navigation bar positioned below the main Business Header, specific to the Internet Leased Line product page. It provides quick access to key sections and a primary CTA for callback requests.

Component: `/src/app/components/ILLSubHeader.tsx`

---

## Layout

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Position              | `sticky`, `top: 64px` (below header)     |
| Z-index               | 40                                        |
| Background            | `var(--primary-20)` (#E8E8FC)            |
| Border bottom         | `1px solid var(--grey-40)`               |
| Height                | 56px                                      |
| Display               | Flexbox, space-between alignment          |
| Container padding     | px-4 md:px-10 (matches header alignment)  |

---

## Content Structure

### Left Section — Navigation Links

A horizontal list of text links aligned to the left:

- Discover
- Plans
- Services
- Segments
- Resources
- Contact Us

**Link Styling:**

| State    | Font Weight              | Color                  | Border                     |
| -------- | ------------------------ | ---------------------- | -------------------------- |
| Normal   | `--font-weight-medium`   | `--grey-80`            | None                       |
| Active   | `--font-weight-bold`     | `--primary-50`         | None (visual only)         |
| Hover    | Same as normal           | `--primary-50`         | None                       |

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Font family           | `var(--font-family-jiotype)`             |
| Font size             | `var(--text-label)` (14px)               |
| Line height           | 1.5                                      |
| Padding               | `var(--space-3)` vertical, `0` horizontal|
| Background            | `transparent`                            |
| Border                | None                                     |
| Cursor                | `pointer`                                |
| Transition            | `color 0.2s`                             |
| Gap between links     | `var(--space-8)` (32px)                  |

### Right Section — Primary CTA

A single primary button with text "Request a callback".

**Button Spec:**

| Property              | Value                                    |
| --------------------- | ---------------------------------------- |
| Variant               | `default` (primary blue)                 |
| Size                  | `default` (48px height)                  |
| Text                  | "Request a callback"                     |

Uses the standard JDS Button component from `/src/app/components/ui/button.tsx`.

---

## Responsive Behavior

| Breakpoint | Left Section                  | Right Section          |
| ---------- | ----------------------------- | ---------------------- |
| Mobile     | Horizontal scroll (overflow)  | Always visible         |
| Tablet+    | Full horizontal layout        | Fixed position, right  |

**Overflow Handling:**

- The left navigation links container has `overflow-x: auto` on mobile.
- Scrollbar is hidden via CSS (`scrollbar-width: none`, `::-webkit-scrollbar { display: none; }`).
- The right CTA button has `shrink-0` to prevent it from collapsing.

---

## State Management

Active link state is tracked via React `useState`:

```tsx
const [activeLink, setActiveLink] = React.useState('Discover');
```

Clicking a link updates the active state and applies the active styles (bold weight, primary color).

---

## Accessibility

- All links are rendered as `<button>` elements with proper focus states.
- Keyboard navigation is fully supported.
- Active link state is visually indicated by color and font weight.

---

## Design Tokens Used

| Token                   | Value         | Usage                          |
| ----------------------- | ------------- | ------------------------------ |
| `--primary-20`          | `#E8E8FC`     | Background color               |
| `--grey-40`             | `#E0E0E0`     | Bottom border                  |
| `--primary-50`          | `#3535F3`     | Active link color              |
| `--grey-80`             | `rgba(0,0,0,0.65)` | Normal link color         |
| `--font-family-jiotype` | JioType stack | Font family                    |
| `--text-label`          | `14px`        | Link font size                 |
| `--font-weight-medium`  | `500`         | Normal link weight             |
| `--font-weight-bold`    | `700`         | Active link weight             |
| `--space-3`             | `12px`        | Link padding                   |
| `--space-8`             | `32px`        | Gap between links              |

---

## Usage

```tsx
import { ILLSubHeader } from '../components/ILLSubHeader';

export function InternetLeasedLinePage() {
  return (
    <div>
      <BusinessHeader />
      <ILLSubHeader />
      {/* Page sections */}
    </div>
  );
}
```

---

## Notes

- This component is specific to the Internet Leased Line product page (`/business/internet-leased-line`).
- It is positioned `sticky` at `top: 64px` (below the main Business Header at 64px).
- The links are for visual navigation only; click handlers can be added to scroll to sections or navigate to sub-pages.
- The "Request a callback" CTA should trigger a contact form modal or navigate to a callback request page (implementation pending).
