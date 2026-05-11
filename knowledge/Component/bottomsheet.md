# Bottomsheet — JDS Component Style Guide

## Overview

Bottomsheets are **modal surfaces** that slide up from the bottom edge of the screen to present contextual content, actions, or forms. They maintain user context while providing an immersive secondary surface.

The component lives in `/src/app/components/ui/bottomsheet.tsx`.

All styling uses JDS design tokens from `/src/styles/theme.css`.
Typography uses JioType exclusively per typography.md.
Icons use `fill="currentColor"` per icon.md.

---

## Typography Rules (MANDATORY)

> **ALL text in Bottomsheet components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (Bottomsheet)

| Token                   | Value | Usage                                 |
| ----------------------- | ----- | ------------------------------------- |
| `--font-weight-black`   | 900   | Sheet title (heading)                 |
| `--font-weight-bold`    | 700   | Section headings, action buttons      |
| `--font-weight-medium`  | 500   | Body text, descriptions, labels       |

### Permitted Sizes (Bottomsheet)

| Token                | Value | Usage                             |
| -------------------- | ----- | --------------------------------- |
| `--text-h4`          | 24px  | Sheet title (header)              |
| `--text-heading-xs`  | 24px  | Section headings                  |
| `--text-base`        | 16px  | Body text, descriptions           |
| `--text-label`       | 14px  | Labels, helper text               |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Anatomy

A bottomsheet consists of the following elements:

```
┌─────────────────────────────────────┐
│            [Handle]                 │ ← Drag handle (optional)
├─────────────────────────────────────┤
│  [Icon] Title            [Action]   │ ← Header
├─────────────────────────────────────┤
│                                     │
│        Content Area                 │ ← Scrollable content
│        (Forms, Lists, Text)         │
│                                     │
├─────────────────────────────────────┤
│  [Secondary]  [Primary Button]      │ ← Footer actions (optional)
└─────────────────────────────────────┘
```

### Elements

1. **Handle** (Optional)
   - Visual affordance for draggable sheets
   - Centered horizontal bar
   - Size: 32px × 4px
   - Color: `var(--grey-60)` → #B5B5B5
   - Radius: `var(--radius-full)` → 9999px

2. **Header** (Required)
   - Contains title, optional icon, optional close/action button
   - Background: `var(--primary-background)` → #FFFFFF
   - Padding: `var(--space-4)` (16px) vertical, `var(--space-6)` (24px) horizontal
   - Border-bottom: `var(--border-width-thin)` (1px) solid `var(--grey-40)` → #E0E0E0

3. **Content Area** (Required)
   - Main content container
   - Background: `var(--primary-background)` → #FFFFFF
   - Padding: `var(--space-6)` (24px) horizontal
   - Scrollable when content exceeds viewport

4. **Footer** (Optional)
   - Action buttons (primary + secondary)
   - Background: `var(--primary-background)` → #FFFFFF
   - Padding: `var(--space-4)` (16px) vertical, `var(--space-6)` (24px) horizontal
   - Border-top: `var(--border-width-thin)` (1px) solid `var(--grey-40)` → #E0E0E0

5. **Overlay/Scrim** (Required)
   - Semi-transparent backdrop behind sheet
   - Background: `var(--overlay-medium)` → #000000a6 (65% black)
   - Dismisses sheet on click (optional)

---

## Variants

### 1. Standard Bottomsheet

Default modal sheet that slides up from bottom.

```
Height:         Auto (content-driven) or fixed
Max Height:     90vh
Background:     var(--primary-background)        → #FFFFFF
Border-radius:  var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Shadow:         0 -4px 24px var(--overlay-dim)   → 0 -4px 24px #0000004d
```

#### Usage

```tsx
<Bottomsheet open={isOpen} onOpenChange={setIsOpen}>
  <BottomsheetContent>
    <BottomsheetHeader>
      <BottomsheetTitle>Sheet Title</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Content */}
    </BottomsheetBody>
    <BottomsheetFooter>
      <Button variant="secondary">Cancel</Button>
      <Button variant="default">Confirm</Button>
    </BottomsheetFooter>
  </BottomsheetContent>
</Bottomsheet>
```

---

### 2. Draggable Bottomsheet

Sheet with drag handle that can be swiped to dismiss.

```
Height:         Auto (content-driven)
Max Height:     90vh
Handle:         32px × 4px, var(--grey-60), var(--radius-full)
Background:     var(--primary-background)        → #FFFFFF
Border-radius:  var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Shadow:         0 -4px 24px var(--overlay-dim)   → 0 -4px 24px #0000004d
```

#### Usage

```tsx
<Bottomsheet open={isOpen} onOpenChange={setIsOpen} draggable>
  <BottomsheetContent>
    <BottomsheetHandle />
    <BottomsheetHeader>
      <BottomsheetTitle>Draggable Sheet</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Content */}
    </BottomsheetBody>
  </BottomsheetContent>
</Bottomsheet>
```

---

### 3. Full-Height Bottomsheet

Sheet that takes up full viewport height (for forms, long lists).

```
Height:         100vh
Max Height:     100vh
Background:     var(--primary-background)        → #FFFFFF
Border-radius:  var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Shadow:         0 -4px 24px var(--overlay-dim)   → 0 -4px 24px #0000004d
```

#### Usage

```tsx
<Bottomsheet open={isOpen} onOpenChange={setIsOpen} fullHeight>
  <BottomsheetContent>
    <BottomsheetHeader>
      <BottomsheetTitle>Full Height Sheet</BottomsheetTitle>
      <BottomsheetClose />
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Scrollable content */}
    </BottomsheetBody>
  </BottomsheetContent>
</Bottomsheet>
```

---

### 4. Snap Bottomsheet (Multi-Position)

Sheet that snaps to predefined heights (collapsed → half → full).

```
Snap Points:    [25vh, 50vh, 90vh]
Background:     var(--primary-background)        → #FFFFFF
Border-radius:  var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Shadow:         0 -4px 24px var(--overlay-dim)   → 0 -4px 24px #0000004d
```

#### Usage

```tsx
<Bottomsheet
  open={isOpen}
  onOpenChange={setIsOpen}
  snapPoints={[0.25, 0.5, 0.9]}
  defaultSnap={0.5}
>
  <BottomsheetContent>
    <BottomsheetHandle />
    <BottomsheetHeader>
      <BottomsheetTitle>Snap Sheet</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Content */}
    </BottomsheetBody>
  </BottomsheetContent>
</Bottomsheet>
```

---

## Sizes

### Height Options

| Size          | Height   | Max Height | Usage                                          |
| ------------- | -------- | ---------- | ---------------------------------------------- |
| Auto          | Content  | 90vh       | Dynamic content (default)                      |
| Small         | 30vh     | 30vh       | Quick actions, simple forms                    |
| Medium        | 50vh     | 50vh       | Moderate content, filters                      |
| Large         | 75vh     | 75vh       | Long forms, detailed content                   |
| Full          | 100vh    | 100vh      | Full-screen experience                         |

### Width

```
Width:          100vw (full screen width)
Max Width:      100vw
Horizontal Padding: var(--space-0) (0px) — full width on mobile
```

---

## Colors

### Background

| Element       | Token                        | Value   |
| ------------- | ---------------------------- | ------- |
| Sheet         | `--primary-background`       | #FFFFFF |
| Overlay/Scrim | `--overlay-medium`           | #000000a6 (65%) |
| Header        | `--primary-background`       | #FFFFFF |
| Content       | `--primary-background`       | #FFFFFF |
| Footer        | `--primary-background`       | #FFFFFF |

### Text

| Element       | Token              | Value   |
| ------------- | ------------------ | ------- |
| Title         | `--foreground`     | #141414 |
| Body          | `--grey-80`        | #000000a6 |
| Label         | `--grey-80`        | #000000a6 |

### Borders

| Element          | Token                        | Value   |
| ---------------- | ---------------------------- | ------- |
| Header Border    | `--grey-40`                  | #E0E0E0 |
| Footer Border    | `--grey-40`                  | #E0E0E0 |
| Handle           | `--grey-60`                  | #B5B5B5 |

---

## Border Radius

```
Top Corners:     var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Bottom Corners:  0 0                                     → 0 0
Handle:          var(--radius-full)                     → 9999px
```

---

## Spacing

### Header

```
Padding Top/Bottom:    var(--space-4)   → 16px
Padding Left/Right:    var(--space-6)   → 24px
Gap (Icon to Title):   var(--space-3)   → 12px
Gap (Title to Action): var(--space-4)   → 16px
```

### Content/Body

```
Padding Top/Bottom:    var(--space-6)   → 24px
Padding Left/Right:    var(--space-6)   → 24px
Gap (Elements):        var(--space-4)   → 16px
```

### Footer

```
Padding Top/Bottom:    var(--space-4)   → 16px
Padding Left/Right:    var(--space-6)   → 24px
Gap (Buttons):         var(--space-3)   → 12px
```

### Handle

```
Width:                 32px
Height:                4px
Margin Top:            var(--space-3)   → 12px
Margin Bottom:         var(--space-2)   → 8px
```

---

## States

### 1. Closed (Default)

```
Transform:       translateY(100%)
Opacity:         0
Pointer Events:  none
Transition:      transform 0.3s ease-out, opacity 0.2s ease-out
```

### 2. Open

```
Transform:       translateY(0)
Opacity:         1
Pointer Events:  auto
Transition:      transform 0.3s ease-out, opacity 0.2s ease-out
```

### 3. Dragging

```
Transform:       translateY(var(--drag-offset))
Opacity:         1
User Select:     none
Cursor:          grabbing
Transition:      none (during drag)
```

### 4. Dismissing

```
Transform:       translateY(100%)
Opacity:         0.8 → 0
Pointer Events:  none
Transition:      transform 0.25s ease-in, opacity 0.2s ease-in
```

---

## Overlay/Scrim States

### Closed

```
Opacity:         0
Pointer Events:  none
Transition:      opacity 0.2s ease-out
```

### Open

```
Opacity:         1
Pointer Events:  auto
Transition:      opacity 0.2s ease-out
```

---

## Shadows

```
Sheet Shadow:    0 -4px 24px var(--overlay-dim)  → 0 -4px 24px #0000004d
```

---

## Animations

### Open Animation

```
Duration:        300ms
Easing:          ease-out
Transform:       translateY(100%) → translateY(0)
Opacity:         0 → 1
```

### Close Animation

```
Duration:        250ms
Easing:          ease-in
Transform:       translateY(0) → translateY(100%)
Opacity:         1 → 0
```

### Overlay Fade

```
Duration:        200ms
Easing:          ease-out (open) / ease-in (close)
Opacity:         0 ↔ 1
```

---

## Accessibility (A11y)

### ARIA Attributes

```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="sheet-title"
  aria-describedby="sheet-description"
>
  <h2 id="sheet-title">Sheet Title</h2>
  <div id="sheet-description">Sheet description content</div>
</div>
```

### Keyboard Support

| Key            | Action                                |
| -------------- | ------------------------------------- |
| `Escape`       | Close bottomsheet                     |
| `Tab`          | Move focus forward within sheet       |
| `Shift + Tab`  | Move focus backward within sheet      |

### Focus Management

- **Focus trap**: When sheet opens, focus moves to first focusable element (usually title or close button)
- **Focus restoration**: When sheet closes, focus returns to triggering element
- **Focus visible**: Keyboard users see clear focus indicators (use `:focus-visible`)

### Screen Readers

- Use `role="dialog"` and `aria-modal="true"` on sheet container
- Include `aria-labelledby` pointing to sheet title
- Include `aria-describedby` pointing to sheet description (if present)
- Close button should have `aria-label="Close"` or visible text

---

## Design Token Reference

### Colors

| Token                  | Value        | Usage                           |
| ---------------------- | ------------ | ------------------------------- |
| `--primary-background` | #FFFFFF      | Sheet background                |
| `--foreground`         | #141414      | Title text                      |
| `--grey-80`            | #000000a6    | Body text                       |
| `--grey-60`            | #B5B5B5      | Handle color                    |
| `--grey-40`            | #E0E0E0      | Header/footer borders           |
| `--overlay-medium`     | #000000a6    | Scrim/overlay (65% black)       |
| `--overlay-dim`        | #0000004d    | Sheet shadow (30% black)        |

### Typography

| Token                   | Value   | Usage                        |
| ----------------------- | ------- | ---------------------------- |
| `--text-h4`             | 24px    | Sheet title                  |
| `--text-heading-xs`     | 24px    | Section headings             |
| `--text-base`           | 16px    | Body text                    |
| `--text-label`          | 14px    | Labels, helper text          |
| `--font-weight-black`   | 900     | Sheet title                  |
| `--font-weight-bold`    | 700     | Section headings, buttons    |
| `--font-weight-medium`  | 500     | Body text, labels            |
| `--font-family-jiotype` | JioType | Font family (all text)       |

### Spacing

| Token        | Value | Usage                               |
| ------------ | ----- | ----------------------------------- |
| `--space-2`  | 8px   | Handle bottom margin                |
| `--space-3`  | 12px  | Handle top margin, button gap       |
| `--space-4`  | 16px  | Header/footer padding, content gap  |
| `--space-6`  | 24px  | Content padding, header/footer horizontal |

### Radius

| Token              | Value  | Usage                               |
| ------------------ | ------ | ----------------------------------- |
| `--radius-lg`      | 24px   | Sheet top corners                   |
| `--radius-full`    | 9999px | Handle border radius                |

### Borders

| Token                  | Value | Usage                        |
| ---------------------- | ----- | ---------------------------- |
| `--border-width-thin`  | 1px   | Header/footer borders        |

---

## Props

| Prop              | Type                                    | Default   | Description                                      |
| ----------------- | --------------------------------------- | --------- | ------------------------------------------------ |
| `open`            | `boolean`                               | `false`   | Controls sheet visibility                        |
| `onOpenChange`    | `(open: boolean) => void`               | —         | Callback when open state changes                 |
| `defaultOpen`     | `boolean`                               | `false`   | Initial open state (uncontrolled)                |
| `draggable`       | `boolean`                               | `false`   | Enable drag-to-dismiss with handle               |
| `dismissible`     | `boolean`                               | `true`    | Allow dismissing via overlay click or Escape key |
| `fullHeight`      | `boolean`                               | `false`   | Full viewport height (100vh)                     |
| `snapPoints`      | `number[]`                              | —         | Snap positions (e.g., `[0.25, 0.5, 0.9]`)        |
| `defaultSnap`     | `number`                                | —         | Default snap position (from snapPoints array)    |
| `size`            | `'auto' \| 'sm' \| 'md' \| 'lg' \| 'full'` | `'auto'`  | Predefined height size                           |
| `modal`           | `boolean`                               | `true`    | Render as modal with overlay                     |
| `className`       | `string`                                | —         | Additional CSS classes for sheet                 |
| `overlayClassName`| `string`                                | —         | Additional CSS classes for overlay               |
| `children`        | `React.ReactNode`                       | —         | Sheet content                                    |

---

## Usage Examples

### Basic Bottomsheet

```tsx
import { Bottomsheet, BottomsheetContent, BottomsheetHeader, BottomsheetTitle, BottomsheetBody, BottomsheetFooter } from '@/components/ui/bottomsheet';
import { Button } from '@/components/ui/button';

function Example() {
  const [open, setOpen] = useState(false);

  return (
    <>
      <Button onClick={() => setOpen(true)}>Open Sheet</Button>

      <Bottomsheet open={open} onOpenChange={setOpen}>
        <BottomsheetContent>
          <BottomsheetHeader>
            <BottomsheetTitle>Confirm Action</BottomsheetTitle>
          </BottomsheetHeader>
          <BottomsheetBody>
            <p>Are you sure you want to proceed with this action?</p>
          </BottomsheetBody>
          <BottomsheetFooter>
            <Button variant="secondary" onClick={() => setOpen(false)}>
              Cancel
            </Button>
            <Button variant="default" onClick={handleConfirm}>
              Confirm
            </Button>
          </BottomsheetFooter>
        </BottomsheetContent>
      </Bottomsheet>
    </>
  );
}
```

---

### Draggable Bottomsheet with Handle

```tsx
<Bottomsheet open={open} onOpenChange={setOpen} draggable>
  <BottomsheetContent>
    <BottomsheetHandle />
    <BottomsheetHeader>
      <BottomsheetTitle>Filter Options</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Filter form */}
    </BottomsheetBody>
    <BottomsheetFooter>
      <Button variant="default" onClick={applyFilters}>
        Apply Filters
      </Button>
    </BottomsheetFooter>
  </BottomsheetContent>
</Bottomsheet>
```

---

### Full-Height Bottomsheet (Form)

```tsx
<Bottomsheet open={open} onOpenChange={setOpen} fullHeight>
  <BottomsheetContent>
    <BottomsheetHeader>
      <BottomsheetTitle>Create Account</BottomsheetTitle>
      <BottomsheetClose />
    </BottomsheetHeader>
    <BottomsheetBody>
      <form>
        <Input label="Full Name" />
        <Input label="Email" type="email" />
        <Input label="Phone Number" type="tel" />
        {/* More form fields */}
      </form>
    </BottomsheetBody>
    <BottomsheetFooter>
      <Button variant="default" type="submit">
        Create Account
      </Button>
    </BottomsheetFooter>
  </BottomsheetContent>
</Bottomsheet>
```

---

### Snap Bottomsheet (Multi-Position)

```tsx
<Bottomsheet
  open={open}
  onOpenChange={setOpen}
  snapPoints={[0.25, 0.5, 0.9]}
  defaultSnap={0.5}
  draggable
>
  <BottomsheetContent>
    <BottomsheetHandle />
    <BottomsheetHeader>
      <BottomsheetTitle>Location Details</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      {/* Content that adjusts to snap heights */}
    </BottomsheetBody>
  </BottomsheetContent>
</Bottomsheet>
```

---

### Bottomsheet with Icon in Header

```tsx
<Bottomsheet open={open} onOpenChange={setOpen}>
  <BottomsheetContent>
    <BottomsheetHeader>
      <IcInfo className="w-6 h-6" fill="currentColor" />
      <BottomsheetTitle>Information</BottomsheetTitle>
      <BottomsheetClose />
    </BottomsheetHeader>
    <BottomsheetBody>
      <p>Here's some important information for you.</p>
    </BottomsheetBody>
  </BottomsheetContent>
</Bottomsheet>
```

---

### Non-Dismissible Bottomsheet

```tsx
<Bottomsheet
  open={open}
  onOpenChange={setOpen}
  dismissible={false}
>
  <BottomsheetContent>
    <BottomsheetHeader>
      <BottomsheetTitle>Required Action</BottomsheetTitle>
    </BottomsheetHeader>
    <BottomsheetBody>
      <p>You must complete this action to continue.</p>
    </BottomsheetBody>
    <BottomsheetFooter>
      <Button variant="default" onClick={handleComplete}>
        Complete
      </Button>
    </BottomsheetFooter>
  </BottomsheetContent>
</Bottomsheet>
```

---

## Implementation Checklist

When implementing bottomsheet components, verify:

- [ ] Uses `font-family: var(--font-family-jiotype)` for all text
- [ ] Uses only JDS color tokens from `/src/styles/theme.css`
- [ ] Uses only JDS spacing tokens (e.g., `var(--space-4)`, `var(--space-6)`)
- [ ] Border radius is `var(--radius-lg)` for top corners (24px)
- [ ] Overlay uses `var(--overlay-medium)` (65% black)
- [ ] Shadow uses `var(--overlay-dim)` (30% black)
- [ ] Handle is 32px × 4px with `var(--grey-60)` color
- [ ] Title uses `var(--text-h4)` (24px) and `var(--font-weight-black)` (900)
- [ ] Body text uses `var(--text-base)` (16px) and `var(--font-weight-medium)` (500)
- [ ] Header/footer borders use `var(--grey-40)` (1px)
- [ ] Includes proper ARIA attributes (`role="dialog"`, `aria-modal="true"`)
- [ ] Keyboard support (Escape to close, Tab navigation)
- [ ] Focus trap and focus restoration work correctly
- [ ] Close button has accessible label
- [ ] Animation durations match spec (300ms open, 250ms close)
- [ ] No custom/hardcoded colors, spacing, or typography values

---

## Design Considerations

### When to Use

- **Quick Actions**: Payment options, share menu, quick settings
- **Forms**: Short forms, filters, input collection
- **Details**: Product details, location info, event details
- **Lists**: Selection lists, menu options, contacts
- **Confirmations**: Destructive actions, important decisions

### When NOT to Use

- **Complex Multi-Step Flows**: Use full-page forms instead
- **Primary Navigation**: Use main navigation patterns
- **Critical Information**: Use dedicated pages for important content
- **Long-Form Content**: Consider full-page layout for better readability

### Best Practices

1. **Keep content focused**: One clear purpose per sheet
2. **Use clear titles**: Users should understand context immediately
3. **Provide dismissal options**: Always allow users to close (except required actions)
4. **Optimize for one-handed use**: Place primary actions within thumb reach
5. **Avoid nested bottomsheets**: Don't open sheets from within sheets
6. **Consider keyboard users**: Ensure all interactions work without mouse/touch
7. **Test on various devices**: Verify drag behavior and snap points on different screen sizes

---

## Browser Compatibility

- Modern browsers with support for CSS transforms, transitions, and viewport units
- Requires JavaScript for interactive behavior (drag, snap, dismiss)
- Gracefully degrades to modal overlay if advanced features unsupported
