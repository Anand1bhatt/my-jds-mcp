# QuickNavigationIcons Component

**Component:** QuickNavigationIcons  
**Status:** Active  
**Last Updated:** 2026-02-20

---

## 1. Overview

The QuickNavigationIcons component displays a collection of navigational shortcuts with icons and labels. It provides quick access to key features or pages through visually consistent, tappable cards. Designed for landing pages and dashboards.

**Use Cases:**
- Landing page quick actions (Get JioHome, Get JioSim, Port to Jio, Support)
- Dashboard navigation shortcuts
- Feature discovery sections
- Service access points

---

## 2. Anatomy & Configuration

### Anatomy Elements

1. **Container** — Individual card wrapper (116px × 112px)
2. **Icon Background** — Circular background container (48px diameter)
3. **Icon** — XXL-sized vector glyph (32px × 32px)
4. **Text Label** — Descriptive label below icon

### Item Structure
```
┌─────────────────────┐
│    Container Card   │
│  ┌───────────────┐  │
│  │   Icon BG     │  │
│  │   (Circle)    │  │
│  │      🔷       │  │
│  └───────────────┘  │
│                     │
│    Text Label       │
└─────────────────────┘
```

---

## 3. Technical Specifications

### Container (Card)

| Property | Value | Token |
|----------|-------|-------|
| **Width** | 116px | Fixed |
| **Height** | 112px | Fixed |
| **Border Radius** | 16px | Fixed |
| **Padding** | 8px | `var(--space-2)` |
| **Background (Normal)** | Transparent | — |
| **Background (Hover)** | Primary/20 | `var(--primary-20)` |

### Icon

| Property | Value | Token |
|----------|-------|-------|
| **Size** | XXL | — |
| **Container Size** | 48px × 48px | Fixed |
| **Icon Size** | 32px × 32px | Fixed (2/3 ratio) |
| **Icon Color** | Primary/50 | `var(--primary-50)` |
| **Background** | Primary/20 | `var(--primary-20)` |
| **Background Shape** | Circle | `var(--radius-circle)` |

### Text Label

| Property | Value | Token |
|----------|-------|-------|
| **Font Size** | 16px | `var(--text-body-s)` ($body/XS) |
| **Font Family** | JioType | `var(--font-family-jiotype)` |
| **Font Weight** | Medium (500) | `var(--font-weight-medium)` |
| **Color** | Grey/80 | `var(--grey-80)` |
| **Line Height** | 1.3 | Fixed |
| **Text Align** | Center | — |

### Spacing

| Property | Value | Token |
|----------|-------|-------|
| **Icon & Text Gap** | 8px | `var(--space-2)` |
| **Between Items** | 32px | `var(--space-8)` |

---

## 4. States

### Normal State

- **Container Background:** Transparent
- **Icon Background:** `var(--primary-20)` (always visible)
- **Icon Color:** `var(--primary-50)`
- **Text Color:** `var(--grey-80)`

### Hover State

- **Container Background:** `var(--primary-20)`
- **Icon Background:** `var(--primary-20)` (unchanged)
- **Icon Color:** `var(--primary-50)` (unchanged)
- **Text Color:** `var(--grey-80)` (unchanged)
- **Icon Scale:** Optional 110% scale on hover

### Focus State

- Follows standard browser focus outline
- Accessible via keyboard navigation

---

## 5. Behavior & Layout

### Grid Behavior

- **Alignment:** Center-aligned on page
- **Wrapping:** Items wrap to next line when maximum width is reached
- **Responsive:** Uses `flex-wrap` to automatically wrap items

### Item Count Constraints

| Constraint | Value |
|------------|-------|
| **Minimum Items** | 3 |
| **Maximum Items** | 9 |
| **Recommended** | 4-6 items for optimal visual balance |

### Responsive Behavior

- Items maintain fixed 116px × 112px size across all breakpoints
- Container wraps items to multiple rows on smaller screens
- Center alignment is preserved at all viewport sizes
- Gap between items remains consistent (32px)

---

## 6. Implementation

### Component Props

```typescript
export interface QuickNavigationItem {
  /** Unique identifier */
  id?: string;
  /** Display label text */
  label: string;
  /** Icon component from @jds/core-icons or @jds/extended-icons */
  icon: React.ComponentType<{ className?: string; fill?: string; style?: React.CSSProperties }>;
  /** Optional click handler */
  onClick?: () => void;
  /** Optional href for navigation */
  href?: string;
}

export interface QuickNavigationIconsProps {
  /** Array of navigation items (3-9 items) */
  items: QuickNavigationItem[];
  /** Optional additional CSS classes */
  className?: string;
}
```

### Usage Example

```tsx
import { QuickNavigationIcons } from './components/ui/quick-navigation-icons';
import { IcHome, IcSwap } from '@jds/core-icons';
import { IcMobile, IcSupport } from '@jds/extended-icons';

const navigationItems = [
  { label: 'Get JioHome', icon: IcHome, href: '/jiohome' },
  { label: 'Get JioSim', icon: IcMobile, href: '/jiosim' },
  { label: 'Port to Jio', icon: IcSwap, href: '/port' },
  { label: 'Support', icon: IcSupport, href: '/support' },
];

function LandingPage() {
  return (
    <section className="section-padding">
      <QuickNavigationIcons items={navigationItems} />
    </section>
  );
}
```

---

## 7. Accessibility

- **Semantic HTML:** Uses `<button>` or `<a>` elements for proper keyboard navigation
- **Focus Management:** All items are keyboard accessible
- **Screen Readers:** Icon labels provide context for assistive technology
- **Touch Targets:** 116px × 112px size exceeds minimum 44px × 44px touch target requirement
- **Color Contrast:** Text color (Grey/80) provides sufficient contrast against white background

---

## 8. Design Tokens Reference

All styling uses CSS variables from `/src/styles/theme.css`:

```css
/* Colors */
--primary-50: #0F3CC9;
--primary-20: #E7EBF8;
--grey-80: #000000a6;

/* Typography */
--text-body-s: 16px;
--font-family-jiotype: 'JioType', system-ui, -apple-system, sans-serif;
--font-weight-medium: 500;

/* Spacing */
--space-2: 8px;
--space-8: 32px;

/* Radius */
--radius-circle: 50%;
```

---

## 9. Best Practices

### Do's ✅

- Keep item count between 3-9 items
- Use clear, concise labels (1-3 words)
- Choose icons that clearly represent the action/destination
- Maintain consistent icon style (all from JDS icon library)
- Ensure proper spacing for touch targets
- Center-align the entire group

### Don'ts ❌

- Don't use fewer than 3 or more than 9 items
- Don't use long text labels that wrap to multiple lines
- Don't mix icon styles from different libraries
- Don't override the fixed card dimensions
- Don't change the Primary/20 background color scheme
- Don't remove hover states

---

## 10. Related Components

- **Icon** — Base icon component used within QuickNavigationIcons
- **Button** — Alternative for single call-to-action elements
- **Tabs** — For horizontal navigation between views
- **SubHeader** — For primary navigation menus

---

## 11. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-20 | Initial component specification |
