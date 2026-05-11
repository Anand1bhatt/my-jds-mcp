# Layout and Grid

This is Layout on JioDesign. The layout is the structure that supports all the visual components of a UI. Our responsive grid system is the foundation for all our designs, keeping our content clean and consistent across all platforms and screen sizes.

---

## Logic System

Our core logic creates consistent and flexible layouts throughout our products. Our layout system organises components on the grid in multiples of 8px. Columns can range from 2-12 depending on the device size you're working with, and margins and padding are always applied consistently.

### Core Rules

**Rule 1:** Always lay components on the grid in multiples of 8px (8, 16, 24, 32, 40).

**Rule 2:** Columns range from 2-12 depending on the product or device size.

**Rule 3:** All UI elements and text baselines must snap to the grid.

---

## Layout Anatomy

Users expect to find certain types of content in certain areas. We call these areas layout regions. Three main layout regions form the foundation for our interactive experiences, each made up of different elements such as headers or footers, or containers such as cards or actions. It is especially important for these regions to be consistent across devices and adapt across breakpoints.

### Main Layout Regions

1. **Header**
2. **Body**
3. **Footer**

---

## Responsive Grid

The number of columns displayed in the grid is determined by the breakpoint range, a range of predetermined screen sizes. JioDesign provides responsive layouts based on 2-column, 4-column, 8-column, and 12-column grids, available for use across different screens, devices, and orientations.

### Responsive Grid
Designed to adapt seamlessly across various screen sizes and devices.

### Orientation

Our responsive grid instantly adapts to screen size and device orientation without you having to lift a finger. At any given breakpoint range, the columns will automatically adjust from portrait to landscape, or vice versa.

Our responsive grid instantly adapts to screen size and device orientation.

---

## 4-Point Grid

We use a 4-point grid to measure line height, spacing tokens, corner radius, typography and layout tokens. This means everything is a multiple of 4 (4, 8, 12, 16, 20, 24, 28, 32, 36, 40), which gives us more granularity, greater flexibility and a cleaner UI as a result.

We use a 4-point grid for line height, spacing, and layout tokens, ensuring all elements are multiples of 4 for enhanced flexibility and a cleaner UI.

### Why it matters

**Greater consistency:** Consistent measuring rules means a more consistent grid, which means a better user experience.

**Fewer decisions = less time:** Fewer spacing options means less trial and error and a quicker move from design to code.

**Multi-platform design:** Since most screen sizes are divisible by 4 on at least one axis, the 4-point grid is an obvious solution. By keeping padding and margin dimensions consistent and adjusting the size of the element to fill any white space, we ensure our grid works seamlessly across all platforms and screen sizes.

---

## Typography Grid

Here's a 4px baseline grid being used to achieve better spacing accuracy in a block of typography:

This 4px baseline grid enhances spacing accuracy in a block of typography.

---

## Breakpoints

Breakpoints define the range of predetermined screen sizes and their specific layout requirements. To make your life easier when it comes to working across our different products, our responsive layouts will automatically adapt to different breakpoints based on the user's screen size and orientation.

This document is the **single source of truth** for breakpoints in the Jio Design System.

### Purpose

The breakpoint system exists to:
- Support responsive and adaptive layouts
- Define consistent grid behaviour across screen sizes
- Reduce ambiguity in layout decisions
- Align design and development implementation
- Ensure predictable user experiences on all devices

### Breakpoint System

Our breakpoint system defines the number of columns, margins and gutters recommended for each canvas size. We offer our creators a choice of 5 different canvas size presets (XS-XL) depending on the specific product and service in question. Our system also enables the creation of custom canvases if something more bespoke is needed.

Each breakpoint defines:
- Screen size range
- Grid behaviour
- Recommended number of layout columns

The system supports both **fluid** and **fixed** layout behaviours where required.

---

## Breakpoint Tokens

| Token | Screen Size | Body | Layout Columns |
|-------|-------------|------|----------------|
| XS | 240–323px | Fluid grid | 4 |
| S | 324–619px | Fluid grid | 4 |
| M | 620–991px | Fluid grid | 6 |
| L | 992–1919px | Fluid grid with stopper | 12 |
| XL | ≥1920px | Fluid grid | 12 |

---

## Small Screen Device (JioPhone) - XS

### Devices
- JioPhone
- Older small-screen Android and iOS devices

Small screen devices such as the JioPhone or older iPhones and Androids have a very small screen size that falls into the 240-323px range. They are therefore assigned the XS token and use a 4-column grid.

### Characteristics
- Very small viewport width
- Limited horizontal space

### Layout Rules
- 4-column grid
- Fluid layout
- Minimal horizontal padding
- Prioritise vertical stacking

---

## Responsive Web (Mobile, Phablet) & Native App - S

### Devices
- Mobile phones (portrait)
- Phablets
- Native mobile apps

Mobile portrait, phablets and native apps have a smaller screen size. Since their screen size falls into the 324-619px range, they are assigned the S token and use a 4-column grid.

### Characteristics
- Small screen size
- Touch-first interaction

### Layout Rules
- 4-column grid
- Fluid layout
- Generous touch spacing
- Single-column content where possible

---

## Responsive Web (Mobile Landscape & Tablet) - M

### Devices
- Mobile landscape
- Tablets (portrait)

Mobile landscape and tablets have a medium screen size. Since their screen size falls into the 620-991px range, they are assigned the M token and use a 6-column grid.

### Characteristics
- Medium screen width
- Increased horizontal space

### Layout Rules
- 6-column grid
- Fluid layout
- Multi-column content supported
- Increased gutters and margins

---

## Responsive Web (Tablet Landscape & Desktop) - L

### Devices
- Tablets (landscape)
- Laptops
- Standard desktops

Tablets, landscape and desktop screen sizes fall into the 992-1919px range. They are therefore assigned the L token and use our largest 12-column grid.

### Characteristics
- Large screen width
- High information density

### Layout Rules
- 12-column grid
- Fluid grid with stopper (max-width: 1184px)
- No horizontal padding (edge-to-edge layout within max-width container)
- Content width capped at 1184px for readability
- Increased spacing between sections

---

## Responsive Web (Desktop & External Monitors) - XL

### Devices
- Large desktops
- External monitors
- Ultra-wide displays

Desktop and external monitors have the largest screen size falling above the 1920px range. They are therefore assigned the XL token and use a 12-column fixed grid.

### Characteristics
- Very large screen width
- Risk of overextended content

### Layout Rules
- 12-column grid
- Fixed maximum content width (max-width: 1184px)
- No horizontal padding (edge-to-edge layout within max-width container)
- Center-aligned layouts
- Prevent overly long line lengths

---

## Orientation Behaviour

Layouts automatically adapt to orientation changes.

### Supported Orientations
- Portrait
- Landscape

### Rules
- Columns reflow based on available width
- Content hierarchy remains intact
- No breakpoint-specific redesign required

---

## Spacing & Grid Relationship

Breakpoints work in conjunction with:
- Layout Framework
- Spacing tokens
- 4-point grid system

### Rules
- Spacing scales progressively at larger breakpoints
- Gutters increase with screen size
- Core spacing logic remains consistent

---

## Best Practices

### Do
✔ Design mobile-first  
✔ Test layouts across all breakpoints  
✔ Use breakpoint tokens consistently  
✔ Maintain content readability  

### Don't
✖ Hardcode screen widths  
✖ Design for a single device  
✖ Stretch content edge-to-edge on large screens  
✖ Break grid consistency  

---

## Governance

- Breakpoints are owned by the Design System
- Custom breakpoints are not allowed without approval
- All responsive behaviour must follow this system
- Exceptions must be documented and reviewed

---

## Validation Checklist

✔ Correct breakpoint token used  
✔ Grid adapts correctly  
✔ Content readable at all sizes  
✔ Orientation-safe  
✔ Spacing scales appropriately  

---

## Summary

Breakpoints enable Jio interfaces to scale gracefully across devices.  
By following this system, layouts remain **consistent, readable, and user-friendly** from the smallest screens to the largest displays.

If it doesn't respect the breakpoint system — it doesn't ship.