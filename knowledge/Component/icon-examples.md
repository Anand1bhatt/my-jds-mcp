# Icon Component — Usage Examples

This file provides practical code examples for implementing the Icon component across various scenarios.

---

## Basic Usage

### Example 1: Simple Icon (No Background)

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome } from '@jds/core-icons';

<Icon 
  ic={IcHome} 
  size="md" 
  color="var(--primary-50)" 
/>
```

**Result:** 24×24px home icon in primary blue, no background

---

### Example 2: Icon with Color Inheritance

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcMobile } from '@jds/extended-icons';

<div style={{ color: 'var(--sparkle-50)' }}>
  <Icon ic={IcMobile} size="lg" />
  {/* Icon automatically inherits sparkle color */}
</div>
```

**Result:** 32×32px mobile icon inheriting sparkle color from parent

---

## Background Variants

### Example 3: Icon with Subtle Background

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcSupport } from '@jds/extended-icons';

<Icon 
  ic={IcSupport} 
  size="lg" 
  kind="background"
  color="var(--primary-50)" 
/>
```

**Result:** 
- Container: 32×32px circular background in primary-20 (light blue)
- Icon: 24×24px in primary-50 (blue)

---

### Example 4: Bold Background Icon

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome } from '@jds/core-icons';

<Icon 
  ic={IcHome} 
  size="xl" 
  kind="background-bold"
  color="var(--sparkle-50)" 
/>
```

**Result:** 
- Container: 40×40px circular background in sparkle-50 (purple)
- Icon: 32×32px in white (auto-inversed)

---

## Size Variants

### Example 5: All Sizes Comparison

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome } from '@jds/core-icons';

<div className="flex items-center gap-4">
  {/* Small - 16×16 */}
  <Icon ic={IcHome} size="sm" color="var(--primary-50)" />
  
  {/* Medium - 24×24 */}
  <Icon ic={IcHome} size="md" color="var(--primary-50)" />
  
  {/* Large - 32×32 */}
  <Icon ic={IcHome} size="lg" color="var(--primary-50)" />
  
  {/* Extra Large - 40×40 */}
  <Icon ic={IcHome} size="xl" color="var(--primary-50)" />
  
  {/* Extra Extra Large - 48×48 */}
  <Icon ic={IcHome} size="xxl" color="var(--primary-50)" />
</div>
```

---

### Example 6: Fill Size (Responsive)

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcMobile } from '@jds/extended-icons';

<div style={{ width: '64px', height: '64px' }}>
  <Icon 
    ic={IcMobile} 
    size="fill" 
    color="var(--secondary-50)" 
  />
  {/* Icon fills the entire 64×64 parent container */}
</div>
```

---

## Color Variants

### Example 7: Feedback Colors

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcCheckCircle, IcAlertTriangle, IcXCircle } from '@jds/core-icons';

<div className="flex gap-4">
  {/* Success */}
  <Icon 
    ic={IcCheckCircle} 
    size="md" 
    kind="background"
    color="var(--success-50)" 
  />
  
  {/* Warning */}
  <Icon 
    ic={IcAlertTriangle} 
    size="md" 
    kind="background"
    color="var(--warning-50)" 
  />
  
  {/* Error */}
  <Icon 
    ic={IcXCircle} 
    size="md" 
    kind="background"
    color="var(--error-50)" 
  />
</div>
```

**Result:** Three circular icons with appropriate feedback colors

---

### Example 8: Neutral/Grey Variations

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcInfo } from '@jds/core-icons';

<div className="flex gap-4">
  {/* Grey 60 - Muted */}
  <Icon 
    ic={IcInfo} 
    size="md" 
    kind="background"
    color="var(--grey-60)" 
  />
  
  {/* Grey 80 - Standard */}
  <Icon 
    ic={IcInfo} 
    size="md" 
    kind="background"
    color="var(--grey-80)" 
  />
  
  {/* Grey 100 - High Contrast */}
  <Icon 
    ic={IcInfo} 
    size="md" 
    kind="background"
    color="var(--grey-100)" 
  />
</div>
```

---

## Real-World Examples

### Example 9: Quick Action Button

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome } from '@jds/core-icons';

<button className="flex flex-col items-center gap-2">
  <Icon 
    ic={IcHome} 
    size="lg" 
    kind="background"
    color="var(--primary-50)" 
  />
  <span
    style={{
      fontFamily: 'var(--font-family-jiotype)',
      fontSize: 'var(--text-label)',
      fontWeight: 'var(--font-weight-medium)',
      color: 'var(--foreground)',
    }}
  >
    Get JioHome
  </span>
</button>
```

**Result:** Clickable quick-action with icon and label

---

### Example 10: Button with Icon

```tsx
import { Icon } from '@/app/components/ui/icon';
import { Button } from '@/app/components/ui/button';
import { IcArrowRight } from '@jds/core-icons';

<Button>
  Continue
  <Icon ic={IcArrowRight} size="sm" />
</Button>
```

**Result:** Button with trailing arrow icon (inherits button color)

---

### Example 11: Header Navigation Icons

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcSearch, IcShoppingCart, IcProfile } from '@jds/core-icons';

<div className="flex items-center gap-6">
  <button aria-label="Search">
    <Icon ic={IcSearch} size="md" color="var(--foreground)" />
  </button>
  
  <button aria-label="Cart">
    <Icon ic={IcShoppingCart} size="md" color="var(--foreground)" />
  </button>
  
  <button aria-label="Profile">
    <Icon ic={IcProfile} size="md" color="var(--foreground)" />
  </button>
</div>
```

---

### Example 12: Feature Card with Background-Bold Icon

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcZap } from '@jds/extended-icons';

<div className="flex flex-col items-center gap-4 p-6">
  <Icon 
    ic={IcZap} 
    size="xxl" 
    kind="background-bold"
    color="var(--sparkle-50)" 
  />
  
  <h3
    style={{
      fontFamily: 'var(--font-family-jiotype)',
      fontSize: 'var(--text-heading-s)',
      fontWeight: 'var(--font-weight-black)',
    }}
  >
    Lightning Fast
  </h3>
  
  <p
    style={{
      fontFamily: 'var(--font-family-jiotype)',
      fontSize: 'var(--text-body-m)',
      fontWeight: 'var(--font-weight-normal)',
      color: 'var(--grey-80)',
    }}
  >
    Experience blazing-fast speeds with JioFiber
  </p>
</div>
```

**Result:** Feature card with bold sparkle icon and descriptive text

---

### Example 13: Inverse Icons (Dark Background)

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcFacebook, IcTwitter, IcInstagram } from '@jds/extended-icons';

<div style={{ backgroundColor: 'var(--global-black)', padding: '24px' }}>
  <div className="flex gap-4">
    <Icon 
      ic={IcFacebook} 
      size="md" 
      color="var(--primary-inverse)" 
    />
    <Icon 
      ic={IcTwitter} 
      size="md" 
      color="var(--primary-inverse)" 
    />
    <Icon 
      ic={IcInstagram} 
      size="md" 
      color="var(--primary-inverse)" 
    />
  </div>
</div>
```

**Result:** White icons on dark background (footer social links)

---

### Example 14: Custom Size with Style Override

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome } from '@jds/core-icons';

<Icon 
  ic={IcHome} 
  size="custom"
  color="var(--primary-50)"
  style={{
    width: '28px',
    height: '28px',
  }}
/>
```

**Result:** Custom-sized 28×28px icon

---

### Example 15: Accessible Icon Button

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcClose } from '@jds/core-icons';

<button 
  aria-label="Close dialog"
  style={{
    background: 'transparent',
    border: 'none',
    cursor: 'pointer',
    padding: 'var(--space-2)',
  }}
>
  <Icon 
    ic={IcClose} 
    size="md" 
    color="var(--grey-80)" 
  />
</button>
```

**Result:** Accessible close button with proper ARIA label

---

### Example 16: Responsive Icon Grid

```tsx
import { Icon } from '@/app/components/ui/icon';
import { IcHome, IcMobile, IcSwap, IcSupport } from '@jds/core-icons';

const actions = [
  { icon: IcHome, label: 'Home', color: 'var(--primary-50)' },
  { icon: IcMobile, label: 'Mobile', color: 'var(--secondary-50)' },
  { icon: IcSwap, label: 'Port', color: 'var(--sparkle-50)' },
  { icon: IcSupport, label: 'Support', color: 'var(--grey-80)' },
];

<div 
  style={{
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(80px, 1fr))',
    gap: 'var(--space-6)',
  }}
>
  {actions.map(({ icon, label, color }) => (
    <div key={label} className="flex flex-col items-center gap-2">
      <Icon 
        ic={icon} 
        size="lg" 
        kind="background"
        color={color}
      />
      <span
        style={{
          fontFamily: 'var(--font-family-jiotype)',
          fontSize: 'var(--text-label)',
          fontWeight: 'var(--font-weight-medium)',
        }}
      >
        {label}
      </span>
    </div>
  ))}
</div>
```

**Result:** Responsive grid of action icons with labels

---

## Integration with Existing Components

### With Button Component

```tsx
import { Icon } from '@/app/components/ui/icon';
import { Button } from '@/app/components/ui/button';
import { IcDownload } from '@jds/core-icons';

<Button variant="primary" size="large">
  <Icon ic={IcDownload} size="sm" />
  Download App
</Button>
```

---

### With Card Component

```tsx
import { Icon } from '@/app/components/ui/icon';
import { Card } from '@/app/components/ui/card';
import { IcTrendingUp } from '@jds/extended-icons';

<Card>
  <div className="flex items-center gap-3">
    <Icon 
      ic={IcTrendingUp} 
      size="md" 
      kind="background"
      color="var(--success-50)"
    />
    <div>
      <h4>Sales Growth</h4>
      <p>+23% this month</p>
    </div>
  </div>
</Card>
```

---

## Best Practices Summary

✅ **DO:**
```tsx
// Use inherit for automatic color matching
<Icon ic={IcHome} color="inherit" />

// Use design tokens for explicit colors
<Icon ic={IcHome} color="var(--primary-50)" />

// Use background for standalone emphasis
<Icon ic={IcHome} kind="background" color="var(--primary-50)" />
```

❌ **DON'T:**
```tsx
// Don't use hard-coded colors
<Icon ic={IcHome} color="#0066FF" />

// Don't use arbitrary sizes outside the scale
<Icon ic={IcHome} size="md" style={{ width: '27px' }} />

// Don't mix outline and filled icons
<IcHome /> {/* Missing fill="currentColor" */}
```

---

**End of Icon Examples**
