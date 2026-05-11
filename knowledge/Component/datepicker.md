# DatePicker — JDS Component Style Guide

## Overview

The **DatePicker** is an input control that allows users to select a single date, a date range, or a date and time from an interactive calendar interface. It combines a trigger input field with a calendar popover (desktop) or bottom sheet (mobile).

The component lives in `/src/app/components/ui/datepicker.tsx`.
The underlying calendar grid re-uses `/src/app/components/ui/calendar.tsx`.

All styling uses JDS design tokens from `/src/styles/theme.css`.
Typography uses JioType exclusively per typography.md.
Icons use `fill="currentColor"` per icon.md.

---

## Typography Rules (MANDATORY)

> **ALL text in DatePicker components — and across the entire application — MUST use the JioType variable font exclusively.**

### Font Family

- The **only** permitted font-family is `var(--font-family-jiotype)`.
- Resolves to `'JioType', system-ui, -apple-system, sans-serif` (defined in `/src/styles/theme.css`).
- **Never** use any other font-family (e.g. Inter, Roboto, Arial, monospace, serif).

### Font Loading

- `@font-face` declarations for JioType live in `/src/styles/fonts.css`.
- JioType is loaded as a **variable font** (single file, weight axis `100–900`).
- `font-display: swap` ensures text remains visible during font load.

### Permitted Weights (DatePicker)

| Token                   | Value | Usage                                              |
| ----------------------- | ----- | -------------------------------------------------- |
| `--font-weight-bold`    | 700   | Month/year header, selected day label              |
| `--font-weight-medium`  | 500   | Day-of-week column headers, input trigger label    |
| `--font-weight-normal`  | 400   | Day cell numbers, helper text, placeholder         |

### Permitted Sizes (DatePicker)

| Token               | Value | Usage                                              |
| ------------------- | ----- | -------------------------------------------------- |
| `--text-h4`         | 24px  | Sheet/popover title when used with bottom sheet    |
| `--text-base`       | 16px  | Input trigger text, month/year header label        |
| `--text-label`      | 14px  | Day cell numbers, day-of-week column headers       |
| `--text-body-xxs`   | 12px  | Helper text, error/success messages, footnotes     |

- **Never** use Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`).

---

## Anatomy

### Full DatePicker (Trigger + Calendar Popover)

```
┌─────────────────────────────────────────────────┐
│  Label                                [?]        │  ← Field label + optional info icon
├─────────────────────────────────────────────────┤
│  [📅]  DD / MM / YYYY                [▼]        │  ← Trigger Input
├─────────────────────────────────────────────────┤
│  Helper text                                     │  ← Helper / error / success text
└─────────────────────────────────────────────────┘

           ↓ opens

┌─────────────────────────────────────────────────┐
│   [<]    January  2025    [>]                    │  ← Calendar Header (Month Navigation)
├──────┬──────┬──────┬──────┬──────┬──────┬───────┤
│  Su  │  Mo  │  Tu  │  We  │  Th  │  Fr  │  Sa   │  ← Day-of-week Row
├──────┼──────┼──────┼──────┼──────┼──────┼───────┤
│      │      │      │   1  │   2  │   3  │   4   │
│   5  │   6  │   7  │   8  │   9  │  10  │  11   │  ← Day Cells
│  12  │  13  │  14  │  15  │  16  │  17  │  18   │
│  19  │  20  │  21  │  22  │  23  │  24  │  25   │
│  26  │  27  │  28  │  29  │  30  │  31  │       │
└──────┴──────┴──────┴──────┴──────┴──────┴───────┘
```

### Elements

1. **Trigger Input** (Required)
   - Text input with calendar icon (prefix) and chevron-down (suffix)
   - Displays the selected date formatted as `DD / MM / YYYY`
   - Shows placeholder text when no date selected

2. **Label** (Required in forms)
   - Positioned above the trigger input
   - Supports optional info icon for tooltip

3. **Helper / Error / Success Text** (Optional)
   - Displayed below the trigger input
   - Communicates field status

4. **Calendar Popover / Bottom Sheet** (Required)
   - Desktop: opens as a floating popover anchored below the trigger
   - Mobile: opens as a bottom sheet overlay
   - Contains header, day-of-week row, and day cells grid

5. **Calendar Header** (Required)
   - Month name + year display (center)
   - Left chevron to go to previous month
   - Right chevron to go to next month
   - Month/Year is tappable to switch to Month Picker or Year Picker views

6. **Day-of-Week Row** (Required)
   - Single-letter or two-letter abbreviation for each day
   - Fixed, non-interactive

7. **Day Cells Grid** (Required)
   - 7 columns × up to 6 rows
   - Each cell shows the day number

8. **Time Selector** (Optional — Date-Time variant only)
   - Appears below the calendar grid
   - Hour and minute fields with increment/decrement controls

---

## Variants

### 1. Single Date Picker

Allows selection of one specific date.

```
Mode:            Single
Selection:       One date cell highlighted (selected state)
Clear:           Optional clear icon in trigger input suffix area
```

#### Usage

```tsx
<DatePicker
  mode="single"
  label="Select date"
  placeholder="DD / MM / YYYY"
  value={selectedDate}
  onChange={(date) => setSelectedDate(date)}
/>
```

---

### 2. Date Range Picker

Allows selection of a start date and an end date.

```
Mode:            Range
Selection:       Start date, end date, and all days in between highlighted
Start Cell:      var(--primary-50)  background, var(--primary-inverse) text
End Cell:        var(--primary-50)  background, var(--primary-inverse) text
Middle Cells:    var(--primary-20)  background, var(--foreground)      text
```

#### Usage

```tsx
<DatePicker
  mode="range"
  label="Date range"
  startPlaceholder="Start date"
  endPlaceholder="End date"
  value={dateRange}
  onChange={(range) => setDateRange(range)}
/>
```

---

### 3. Date-Time Picker

Allows selection of a date combined with a specific time.

```
Mode:            datetime
Calendar:        Standard single date picker grid
Time Selector:   Below calendar grid
  Hour Field:    00–23 (24-hour) or 01–12 + AM/PM (12-hour)
  Minute Field:  00–59
  Separator:     ":"
  Controls:      Up/down chevron icons per field
```

#### Usage

```tsx
<DatePicker
  mode="datetime"
  label="Appointment date & time"
  placeholder="DD / MM / YYYY  HH : MM"
  value={dateTime}
  onChange={(dt) => setDateTime(dt)}
  timeFormat="24h"
/>
```

---

### 4. Month Picker View

Intermediate view shown when tapping the month/year header. Allows selecting a month.

```
Grid:            3 columns × 4 rows  (Jan – Dec)
Selection:       Same selected/hover states as day cells
Navigation:      Year chevrons (previous / next year)
```

---

### 5. Year Picker View

Intermediate view shown when tapping the year portion of the header. Allows selecting a year.

```
Grid:            3 columns × N rows  (range of years)
Selection:       Same selected/hover states as day cells
Navigation:      Decade chevrons (previous / next decade)
```

---

## Trigger Input Specifications

### Layout

```
Height (Large):    56px
Height (Medium):   48px
Width:             var(--width-input)   → 340px (default), or 100% in fluid layouts
Display:           Flex, row, align-center
Padding Left:      var(--space-3)       → 12px
Padding Right:     var(--space-3)       → 12px
Gap (icon–text):   var(--space-2)       → 8px
Border Radius:     var(--radius)        → 8px
```

### Colors (Trigger Input States)

| State      | Border Token              | Border Value | Background Token       | Background Value |
| ---------- | ------------------------- | ------------ | ---------------------- | ---------------- |
| Default    | `--grey-60`               | #B5B5B5      | `--primary-background` | #FFFFFF          |
| Hover      | `--primary-50`            | #0F3CC9      | `--primary-background` | #FFFFFF          |
| Focused    | `--primary-50`            | #0F3CC9      | `--primary-background` | #FFFFFF          |
| Filled     | `--grey-60`               | #B5B5B5      | `--primary-background` | #FFFFFF          |
| Error      | `--error-50`              | #FA2F40      | `--error-20`           | #FFF1F0          |
| Success    | `--success-50`            | #25AB21      | `--primary-background` | #FFFFFF          |
| Disabled   | `--grey-40`               | #E0E0E0      | `--grey-20`            | #F5F5F5          |
| Read-Only  | `--grey-40`               | #E0E0E0      | `--grey-20`            | #F5F5F5          |

### Trigger Input Text Colors

| Element         | Token              | Value     |
| --------------- | ------------------ | --------- |
| Placeholder     | `--grey-60`        | #B5B5B5   |
| Filled value    | `--foreground`     | #141414   |
| Label           | `--foreground`     | #141414   |
| Disabled text   | `--grey-60`        | #B5B5B5   |
| Error message   | `--error-50`       | #FA2F40   |
| Success message | `--success-50`     | #25AB21   |
| Helper text     | `--grey-80`        | #000000a6 |

### Trigger Input Typography

```
Label:
  Font Family:    var(--font-family-jiotype)
  Font Size:      var(--text-label)           → 14px
  Font Weight:    var(--font-weight-medium)   → 500
  Color:          var(--foreground)           → #141414

Input text / placeholder:
  Font Family:    var(--font-family-jiotype)
  Font Size:      var(--text-base)            → 16px
  Font Weight:    var(--font-weight-normal)   → 400
  Color (value):  var(--foreground)           → #141414
  Color (placeholder): var(--grey-60)        → #B5B5B5

Helper / Error text:
  Font Family:    var(--font-family-jiotype)
  Font Size:      var(--text-body-xxs)        → 12px
  Font Weight:    var(--font-weight-normal)   → 400
```

### Trigger Input Icons

```
Calendar Icon (Prefix):
  Icon:           ic_calendar (or ic_date_range for range mode)
  Size:           24px × 24px
  Color:          var(--grey-60)              → #B5B5B5  (default)
              → var(--primary-50)            → #0F3CC9  (focused / filled)
  Fill:           currentColor

Chevron Icon (Suffix):
  Icon:           ic_chevron_down
  Size:           20px × 20px
  Color:          var(--grey-80)              → #000000a6
  Rotation:       0deg (closed), 180deg (open)
  Transition:     transform 0.2s ease
  Fill:           currentColor

Clear Icon (Suffix, optional — when value present):
  Icon:           ic_close_circle
  Size:           20px × 20px
  Color:          var(--grey-60)              → #B5B5B5
  Fill:           currentColor
```

---

## Calendar Popover / Bottom Sheet Specifications

### Desktop — Popover Container

```
Background:      var(--primary-background)    → #FFFFFF
Border Radius:   var(--radius-lg)             → 24px
Border:          var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Shadow:          var(--shadow-card)           → 0 4px 16px #0000001a
Padding:         var(--space-4)               → 16px (all sides)
Min Width:       280px
Max Width:       360px
z-index:         Popover layer (above content, below modals)
```

### Mobile — Bottom Sheet Container

```
Background:      var(--primary-background)    → #FFFFFF
Border Radius:   var(--radius-lg) var(--radius-lg) 0 0  → 24px 24px 0 0
Shadow:          0 -4px 24px var(--overlay-dim)  → 0 -4px 24px #0000004d
Padding:         var(--space-4)               → 16px
Width:           100vw
Max Height:      90vh
Overlay (Scrim): var(--overlay-medium)        → #000000a6
```

---

## Calendar Header

```
Layout:          Flex, row, space-between, align-center
Height:          40px
Padding:         var(--space-2) var(--space-0)  → 8px 0px
```

### Month/Year Label

```
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-base)             → 16px
Font Weight:     var(--font-weight-bold)      → 700
Color:           var(--foreground)            → #141414
Cursor:          pointer (tappable to switch view)
```

### Navigation Chevrons (Prev / Next Month)

```
Icon:            ic_chevron_left / ic_chevron_right
Size:            32px × 32px (touch target)
Icon Size:       20px × 20px (visual)
Color (default): var(--grey-80)               → #000000a6
Color (hover):   var(--primary-50)            → #0F3CC9
Color (disabled):var(--grey-40)               → #E0E0E0
Background:      Transparent
Border Radius:   var(--radius-full)           → 9999px
Hover BG:        var(--grey-20)               → #F5F5F5
Fill:            currentColor
```

---

## Day-of-Week Row

```
Layout:          Grid, 7 columns, equal width
Height:          32px
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-label)            → 14px
Font Weight:     var(--font-weight-medium)    → 500
Color:           var(--grey-60)               → #B5B5B5
Text Align:      Center
Padding Bottom:  var(--space-1)               → 4px
```

---

## Day Cells Grid

```
Layout:          Grid, 7 columns, equal width
Cell Size:       36px × 36px (desktop), 40px × 40px (mobile)
Gap:             var(--space-1)               → 4px
Margin Top:      var(--space-1)               → 4px
```

### Day Cell Typography

```
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-label)            → 14px
Font Weight:     var(--font-weight-normal)    → 400
Text Align:      Center
Line Height:     1
```

---

## Day Cell States

### 1. Default (Normal)

```
Background:      Transparent
Text Color:      var(--foreground)            → #141414
Border Radius:   var(--radius-full)           → 9999px
Border:          None
```

### 2. Hover

```
Background:      var(--grey-20)               → #F5F5F5
Text Color:      var(--foreground)            → #141414
Border Radius:   var(--radius-full)           → 9999px
Cursor:          pointer
Transition:      background-color 0.15s ease
```

### 3. Selected (Single)

```
Background:      var(--primary-50)            → #0F3CC9
Text Color:      var(--primary-inverse)       → #FFFFFF
Border Radius:   var(--radius-full)           → 9999px
Font Weight:     var(--font-weight-bold)      → 700
```

### 4. Today (Current Date)

```
Background:      Transparent
Text Color:      var(--primary-50)            → #0F3CC9
Border:          var(--border-width-thin) solid var(--primary-50)  → 1px solid #0F3CC9
Border Radius:   var(--radius-full)           → 9999px
Font Weight:     var(--font-weight-bold)      → 700
```

> When today is also the selected date, the Selected state takes precedence over the Today state.

### 5. Disabled

```
Background:      Transparent
Text Color:      var(--grey-40)               → #E0E0E0
Border Radius:   var(--radius-full)           → 9999px
Cursor:          not-allowed
Pointer Events:  none
```

### 6. Outside Current Month

```
Background:      Transparent
Text Color:      var(--grey-60)               → #B5B5B5
Border Radius:   var(--radius-full)           → 9999px
Opacity:         1  (visible but visually de-emphasised via color)
```

> Clicking an outside-month cell navigates to that month and selects the date.

### 7. Focused (Keyboard Navigation)

```
Background:      var(--grey-20)               → #F5F5F5
Text Color:      var(--foreground)            → #141414
Outline:         var(--border-width-thick) solid var(--primary-50)  → 2px solid #0F3CC9
Outline Offset:  2px
Border Radius:   var(--radius-full)           → 9999px
```

---

## Range Selection States (Date Range Mode Only)

### Range Start Cell

```
Background:      var(--primary-50)            → #0F3CC9
Text Color:      var(--primary-inverse)       → #FFFFFF
Border Radius:   var(--radius-full) 0 0 var(--radius-full)   → 9999px 0 0 9999px
  (right half of cell has a "tail" blending into range-middle)
Font Weight:     var(--font-weight-bold)      → 700
```

### Range End Cell

```
Background:      var(--primary-50)            → #0F3CC9
Text Color:      var(--primary-inverse)       → #FFFFFF
Border Radius:   0 var(--radius-full) var(--radius-full) 0   → 0 9999px 9999px 0
  (left half of cell has a "tail" blending into range-middle)
Font Weight:     var(--font-weight-bold)      → 700
```

### Range Middle Cells

```
Background:      var(--primary-20)            → #E7EBF8
Text Color:      var(--foreground)            → #141414
Border Radius:   var(--space-0)               → 0px  (no rounding for continuous band)
```

### Range Start = Range End (Same Day)

```
Background:      var(--primary-50)            → #0F3CC9
Text Color:      var(--primary-inverse)       → #FFFFFF
Border Radius:   var(--radius-full)           → 9999px  (full circle, like single selection)
```

### Range Preview (Hover over potential end date)

```
Background:      var(--primary-20)            → #E7EBF8  (cells between start and hovered)
Text Color:      var(--foreground)            → #141414
Border Radius:   Same rules as Range Middle
Transition:      background-color 0.1s ease
```

---

## Time Selector (Date-Time Variant Only)

### Layout

```
Position:        Below calendar grid, separated by a border
Border Top:      var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Padding Top:     var(--space-3)                                 → 12px
Margin Top:      var(--space-3)                                 → 12px
Display:         Flex, row, justify-center, align-center
Gap:             var(--space-2)                                 → 8px
```

### Time Field (Hour / Minute)

```
Width:           56px
Height:          40px
Border:          var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Border Radius:   var(--radius)             → 8px
Background:      var(--primary-background) → #FFFFFF
Text Align:      Center
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-base)          → 16px
Font Weight:     var(--font-weight-medium) → 500
Color:           var(--foreground)         → #141414
```

### Time Field States

| State     | Border Token           | Background Token        |
| --------- | ---------------------- | ----------------------- |
| Default   | `--grey-40`            | `--primary-background`  |
| Focused   | `--primary-50`         | `--primary-background`  |
| Hover     | `--primary-50`         | `--primary-background`  |

### Time Separator

```
Character:       ":"
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-base)          → 16px
Font Weight:     var(--font-weight-bold)   → 700
Color:           var(--foreground)         → #141414
```

### AM/PM Toggle (12-hour mode)

```
Layout:          Flex, row
Height:          40px
Border:          var(--border-width-thin) solid var(--grey-40)  → 1px solid #E0E0E0
Border Radius:   var(--radius)             → 8px
Font Family:     var(--font-family-jiotype)
Font Size:       var(--text-label)         → 14px
Font Weight:     var(--font-weight-medium) → 500

Active segment:
  Background:    var(--primary-50)         → #0F3CC9
  Color:         var(--primary-inverse)    → #FFFFFF
  Border Radius: var(--radius)             → 8px

Inactive segment:
  Background:    Transparent
  Color:         var(--grey-80)            → #000000a6
```

---

## Sizes

### Trigger Input Sizes

| Size    | Height | Font Size Token   | Usage                                       |
| ------- | ------ | ----------------- | ------------------------------------------- |
| Large   | 56px   | `--text-base`     | Default — forms and standalone fields       |
| Medium  | 48px   | `--text-base`     | Compact layouts, tables                     |

### Calendar Cell Sizes

| Breakpoint | Cell Size | Rationale                        |
| ---------- | --------- | -------------------------------- |
| Mobile     | 40×40px   | Comfortable touch target (≥ 44px WCAG recommended; 40px acceptable within scrollable sheet) |
| Desktop    | 36×36px   | Pointer-based, smaller grid fits popover |

---

## Spacing

### Trigger Input

```
Padding Left/Right:   var(--space-3)   → 12px
Padding Top/Bottom:   var(--space-0)   → 0px (height is fixed, content centred vertically)
Label Gap (to input): var(--space-1)   → 4px
Input Gap (to helper):var(--space-1)   → 4px
Icon Gap (to text):   var(--space-2)   → 8px
```

### Calendar Popover

```
Padding (all sides):  var(--space-4)   → 16px
Header Bottom Gap:    var(--space-3)   → 12px
Day-row Bottom Gap:   var(--space-1)   → 4px
Cell Gap:             var(--space-1)   → 4px
```

### Calendar Bottom Sheet (Mobile)

```
Padding Top:          var(--space-3)   → 12px  (below handle)
Padding Horizontal:   var(--space-4)   → 16px
Padding Bottom:       var(--space-6)   → 24px
Footer Button Gap:    var(--space-3)   → 12px
```

---

## Colors — Full Reference

### Trigger Input

| Element              | Token                  | Value     |
| -------------------- | ---------------------- | --------- |
| Border (default)     | `--grey-60`            | #B5B5B5   |
| Border (focus/hover) | `--primary-50`         | #0F3CC9   |
| Border (error)       | `--error-50`           | #FA2F40   |
| Border (success)     | `--success-50`         | #25AB21   |
| Border (disabled)    | `--grey-40`            | #E0E0E0   |
| Background           | `--primary-background` | #FFFFFF   |
| Background (error)   | `--error-20`           | #FFF1F0   |
| Background (disabled)| `--grey-20`            | #F5F5F5   |
| Text (value)         | `--foreground`         | #141414   |
| Text (placeholder)   | `--grey-60`            | #B5B5B5   |
| Text (disabled)      | `--grey-60`            | #B5B5B5   |
| Icon (default)       | `--grey-60`            | #B5B5B5   |
| Icon (focused/filled)| `--primary-50`         | #0F3CC9   |
| Error message        | `--error-50`           | #FA2F40   |
| Success message      | `--success-50`         | #25AB21   |
| Helper text          | `--grey-80`            | #000000a6 |

### Calendar Popover

| Element                  | Token                  | Value     |
| ------------------------ | ---------------------- | --------- |
| Popover background       | `--primary-background` | #FFFFFF   |
| Popover border           | `--grey-40`            | #E0E0E0   |
| Month/year label         | `--foreground`         | #141414   |
| Nav chevron (default)    | `--grey-80`            | #000000a6 |
| Nav chevron (hover)      | `--primary-50`         | #0F3CC9   |
| Nav chevron (disabled)   | `--grey-40`            | #E0E0E0   |
| Day column headers       | `--grey-60`            | #B5B5B5   |
| Day cell (default)       | `--foreground`         | #141414   |
| Day cell (outside month) | `--grey-60`            | #B5B5B5   |
| Day cell (disabled)      | `--grey-40`            | #E0E0E0   |
| Today border             | `--primary-50`         | #0F3CC9   |
| Today text               | `--primary-50`         | #0F3CC9   |
| Selected background      | `--primary-50`         | #0F3CC9   |
| Selected text            | `--primary-inverse`    | #FFFFFF   |
| Range middle background  | `--primary-20`         | #E7EBF8   |
| Range middle text        | `--foreground`         | #141414   |
| Hover background         | `--grey-20`            | #F5F5F5   |
| Focus outline            | `--primary-50`         | #0F3CC9   |
| Mobile scrim/overlay     | `--overlay-medium`     | #000000a6 |

---

## Border Radius Reference

| Element                   | Token                 | Value        |
| ------------------------- | --------------------- | ------------ |
| Trigger input             | `--radius`            | 8px          |
| Calendar popover          | `--radius-lg`         | 24px         |
| Mobile bottom sheet (top) | `--radius-lg`         | 24px (top corners only) |
| Day cell (default/hover)  | `--radius-full`       | 9999px       |
| Day cell (range start)    | `--radius-full` left  | 9999px 0 0 9999px |
| Day cell (range end)      | `--radius-full` right | 0 9999px 9999px 0 |
| Day cell (range middle)   | `--space-0`           | 0px          |
| Nav chevron button        | `--radius-full`       | 9999px       |
| Time field                | `--radius`            | 8px          |
| AM/PM toggle              | `--radius`            | 8px          |

---

## Borders

| Element                | Token                  | Value  |
| ---------------------- | ---------------------- | ------ |
| Trigger input (default)| `--border-width-thin`  | 1px    |
| Trigger input (focus)  | `--border-width-medium`| 1.5px  |
| Popover border         | `--border-width-thin`  | 1px    |
| Today indicator        | `--border-width-thin`  | 1px    |
| Focus outline          | `--border-width-thick` | 2px    |
| Time field border      | `--border-width-thin`  | 1px    |
| Time divider border    | `--border-width-thin`  | 1px    |

---

## Shadows

```
Popover shadow:    var(--shadow-card)         → 0 4px 16px #0000001a
Mobile sheet:      0 -4px 24px var(--overlay-dim) → 0 -4px 24px #0000004d
```

---

## Animations

### Popover Open

```
Duration:          200ms
Easing:            ease-out
Transform:         translateY(-4px) → translateY(0)
Opacity:           0 → 1
```

### Popover Close

```
Duration:          150ms
Easing:            ease-in
Transform:         translateY(0) → translateY(-4px)
Opacity:           1 → 0
```

### Mobile Bottom Sheet Open

```
Duration:          300ms
Easing:            ease-out
Transform:         translateY(100%) → translateY(0)
Opacity:           0 → 1
```

### Mobile Bottom Sheet Close

```
Duration:          250ms
Easing:            ease-in
Transform:         translateY(0) → translateY(100%)
Opacity:           1 → 0
```

### Month Transition (slide between months)

```
Duration:          200ms
Easing:            ease-in-out
Transform:         translateX(±100%) → translateX(0)  (next/prev direction)
```

---

## Keyboard Support

| Key                      | Action                                              |
| ------------------------ | --------------------------------------------------- |
| `Enter` / `Space`        | Open datepicker (on trigger), select focused date   |
| `Escape`                 | Close datepicker / discard pending selection        |
| `Tab`                    | Move focus forward (trigger → calendar nav → days)  |
| `Shift + Tab`            | Move focus backward                                 |
| `Arrow Left`             | Move focus to previous day                          |
| `Arrow Right`            | Move focus to next day                              |
| `Arrow Up`               | Move focus to same day in previous week             |
| `Arrow Down`             | Move focus to same day in next week                 |
| `Page Up`                | Navigate to previous month                          |
| `Page Down`              | Navigate to next month                              |
| `Home`                   | Move focus to first day of current week             |
| `End`                    | Move focus to last day of current week              |

---

## Accessibility (A11y)

### ARIA Attributes

```tsx
{/* Trigger input */}
<div
  role="combobox"
  aria-expanded={isOpen}
  aria-haspopup="dialog"
  aria-label="Select date"
  aria-describedby="datepicker-helper"
>
  <input
    type="text"
    readOnly
    aria-autocomplete="none"
    value={formattedDate}
    placeholder="DD / MM / YYYY"
  />
</div>

{/* Calendar dialog */}
<div
  role="dialog"
  aria-modal="true"
  aria-label="Choose date"
>
  {/* Calendar grid */}
  <table role="grid" aria-label="January 2025">
    <thead>
      <tr role="row">
        <th role="columnheader" abbr="Sunday">Su</th>
        {/* … */}
      </tr>
    </thead>
    <tbody>
      <tr role="row">
        <td
          role="gridcell"
          aria-selected="true"   {/* selected date */}
          aria-current="date"    {/* today */}
          aria-disabled="true"   {/* disabled date */}
          tabIndex={0}           {/* focused cell */}
        >
          15
        </td>
        {/* … */}
      </tr>
    </tbody>
  </table>
</div>
```

### Focus Management

- When the datepicker opens, focus moves to the **selected date** (or today if no selection).
- When the datepicker closes, focus returns to the **trigger input**.
- Focus is **trapped within** the calendar dialog while open.
- Selected date cell has `tabIndex={0}`; all other cells have `tabIndex={-1}`.

### Screen Readers

- Trigger announces: `"Select date, DD MMMM YYYY, press Enter to open calendar"`
- Calendar header announces: `"January 2025"`
- Each day cell announces: `"Wednesday, 15 January 2025"` (full date)
- Selected cell additionally announces: `"selected"`
- Today cell additionally announces: `"today"`
- Disabled cell announces: `"unavailable"`
- Range cells announce: `"start of range"` / `"end of range"` / `"in range"`

### Color Contrast

- **Selected day text** (white on `--primary-50`): 4.6:1 (WCAG AA ✓)
- **Today text** (`--primary-50` on white): 4.6:1 (WCAG AA ✓)
- **Day cell default** (`--foreground` on white): 14:1 (WCAG AAA ✓)
- **Outside month** (`--grey-60` on white): 2.8:1 (Decorative context; supplement with shape/weight cues)
- **Disabled** (`--grey-40` on white): Intentionally below contrast — disabled state is conveyed via `aria-disabled`

---

## Interaction Patterns

### Single Date Selection

1. User clicks/taps trigger → calendar opens
2. User navigates months using `<` / `>` chevrons (or keyboard)
3. User clicks/taps a day cell → date is selected, calendar closes, trigger input updates
4. Selecting a new date replaces the existing selection

### Date Range Selection

1. User clicks/taps trigger → calendar opens
2. User clicks/taps a **start date** → first date is highlighted
3. As user hovers (pointer) or arrows (keyboard), range preview updates
4. User clicks/taps an **end date** → range is confirmed, calendar closes
5. If end date < start date, the two dates are swapped automatically
6. Clicking an already-selected start date again resets the selection

### Date-Time Selection

1. User selects a date (same as single mode)
2. Calendar stays open, revealing the time selector
3. User adjusts hour and minute fields
4. User clicks/taps **Apply** (or equivalent confirm button) → calendar closes

### Clearing a Selection

- Clicking the **clear icon** (×) in the trigger input clears the selected date and resets to placeholder.

### Disabling Dates

```tsx
<DatePicker
  mode="single"
  disabledDates={[new Date(2025, 0, 1)]}           // specific dates
  minDate={new Date(2025, 0, 10)}                  // before this date
  maxDate={new Date(2025, 2, 31)}                  // after this date
  disabledDaysOfWeek={[0, 6]}                      // 0=Sunday, 6=Saturday
/>
```

---

## Props

| Prop                 | Type                                           | Default         | Description                                              |
| -------------------- | ---------------------------------------------- | --------------- | -------------------------------------------------------- |
| `mode`               | `'single' \| 'range' \| 'datetime'`            | `'single'`      | Selection mode                                           |
| `label`              | `string`                                       | —               | Field label above trigger                                |
| `placeholder`        | `string`                                       | `'DD / MM / YYYY'` | Trigger placeholder text                              |
| `value`              | `Date \| DateRange \| null`                    | `null`          | Controlled selected value                                |
| `defaultValue`       | `Date \| DateRange \| null`                    | `null`          | Initial value (uncontrolled)                             |
| `onChange`           | `(value: Date \| DateRange \| null) => void`   | —               | Callback when selection changes                          |
| `minDate`            | `Date`                                         | —               | Earliest selectable date                                 |
| `maxDate`            | `Date`                                         | —               | Latest selectable date                                   |
| `disabledDates`      | `Date[]`                                       | `[]`            | Specific dates to disable                                |
| `disabledDaysOfWeek` | `number[]`                                     | `[]`            | Days of week to disable (0=Sun…6=Sat)                    |
| `size`               | `'large' \| 'medium'`                          | `'large'`       | Trigger input height                                     |
| `state`              | `'default' \| 'error' \| 'success' \| 'disabled' \| 'read-only'` | `'default'` | Field validation state             |
| `helperText`         | `string`                                       | —               | Helper / error / success message below trigger           |
| `required`           | `boolean`                                      | `false`         | Marks field as required                                  |
| `clearable`          | `boolean`                                      | `true`          | Shows clear icon when value is set                       |
| `showOutsideDays`    | `boolean`                                      | `true`          | Show days from adjacent months                           |
| `timeFormat`         | `'12h' \| '24h'`                               | `'24h'`         | Time format (datetime mode only)                         |
| `locale`             | `Locale`                                       | `enIN`          | Date locale for formatting and calendar labels           |
| `weekStartsOn`       | `0 \| 1 \| 6`                                  | `0`             | First day of week (0=Sun, 1=Mon, 6=Sat)                  |
| `className`          | `string`                                       | —               | Additional CSS classes for trigger wrapper               |
| `calendarClassName`  | `string`                                       | —               | Additional CSS classes for calendar panel                |

---

## Usage Examples

### Basic Single DatePicker

```tsx
import { DatePicker } from '@/components/ui/datepicker';

function Example() {
  const [date, setDate] = React.useState<Date | null>(null);

  return (
    <DatePicker
      mode="single"
      label="Select a date"
      placeholder="DD / MM / YYYY"
      value={date}
      onChange={setDate}
    />
  );
}
```

---

### Date Range Picker

```tsx
import { DatePicker } from '@/components/ui/datepicker';
import type { DateRange } from '@/components/ui/datepicker';

function RangeExample() {
  const [range, setRange] = React.useState<DateRange | null>(null);

  return (
    <DatePicker
      mode="range"
      label="Travel dates"
      value={range}
      onChange={setRange}
    />
  );
}
```

---

### Date-Time Picker

```tsx
<DatePicker
  mode="datetime"
  label="Appointment date & time"
  placeholder="DD / MM / YYYY  HH : MM"
  value={dateTime}
  onChange={setDateTime}
  timeFormat="24h"
/>
```

---

### DatePicker with Validation State

```tsx
{/* Error state */}
<DatePicker
  mode="single"
  label="Date of birth"
  state="error"
  helperText="Date of birth cannot be in the future"
  value={dob}
  onChange={setDob}
  maxDate={new Date()}
/>

{/* Success state */}
<DatePicker
  mode="single"
  label="Delivery date"
  state="success"
  helperText="Date is available"
  value={deliveryDate}
  onChange={setDeliveryDate}
/>
```

---

### DatePicker with Disabled Dates

```tsx
<DatePicker
  mode="single"
  label="Book a slot"
  disabledDaysOfWeek={[0, 6]}          // disable weekends
  minDate={new Date()}                  // no past dates
  maxDate={addMonths(new Date(), 3)}    // max 3 months ahead
  value={selectedDate}
  onChange={setSelectedDate}
/>
```

---

### Disabled / Read-Only DatePicker

```tsx
{/* Disabled — no interaction */}
<DatePicker
  mode="single"
  label="Locked field"
  state="disabled"
  value={lockedDate}
  onChange={() => {}}
/>

{/* Read-Only — shows value, no interaction */}
<DatePicker
  mode="single"
  label="Confirmation date"
  state="read-only"
  value={confirmedDate}
  onChange={() => {}}
/>
```

---

## Implementation Checklist

When implementing DatePicker components, verify:

- [ ] Uses `font-family: var(--font-family-jiotype)` for all text
- [ ] Trigger input height is 56px (large) or 48px (medium)
- [ ] Trigger border is `var(--grey-60)` default, `var(--primary-50)` on focus/hover
- [ ] Trigger error state uses `var(--error-50)` border and `var(--error-20)` background
- [ ] Trigger disabled state uses `var(--grey-40)` border and `var(--grey-20)` background
- [ ] Calendar icon and chevron use `fill="currentColor"` per icon.md
- [ ] Popover uses `var(--radius-lg)` (24px) border radius
- [ ] Popover shadow uses `var(--shadow-card)` → `0 4px 16px #0000001a`
- [ ] Mobile bottom sheet uses `var(--overlay-medium)` scrim
- [ ] Day cells are 36×36px desktop / 40×40px mobile
- [ ] Day-of-week header text uses `var(--grey-60)`, `--text-label` (14px), `--font-weight-medium`
- [ ] Month/year header text uses `--text-base` (16px), `--font-weight-bold`, `var(--foreground)`
- [ ] Day cell default text uses `var(--foreground)` (14px, normal weight)
- [ ] Selected day uses `var(--primary-50)` bg + `var(--primary-inverse)` text + bold weight
- [ ] Today cell uses `var(--primary-50)` border and text (not bg)
- [ ] Disabled cells use `var(--grey-40)` text + `aria-disabled="true"`
- [ ] Outside-month cells use `var(--grey-60)` text
- [ ] Range start/end use `var(--primary-50)` bg + asymmetric border-radius
- [ ] Range middle cells use `var(--primary-20)` bg + no border-radius
- [ ] Hover state uses `var(--grey-20)` background
- [ ] Focus outline uses `var(--border-width-thick)` (2px) solid `var(--primary-50)`
- [ ] Keyboard arrows navigate the day grid correctly
- [ ] `role="dialog"`, `aria-modal="true"` on calendar panel
- [ ] Day cells have `role="gridcell"`, `aria-selected`, `aria-current="date"` (today)
- [ ] Focus trap active while calendar is open
- [ ] Focus returns to trigger input on calendar close
- [ ] `Escape` key dismisses calendar
- [ ] No custom/hardcoded colors, spacing, or typography values

---

## Design Considerations

### When to Use

- **Forms**: Collecting date of birth, appointment dates, validity periods
- **Filters**: Date range filters in reports, booking systems, searches
- **Scheduling**: Appointment booking, event creation
- **Date-sensitive inputs**: Expiry date, delivery date, check-in/check-out

### When NOT to Use

- **Known dates with few options**: Use a Dropdown or Selector instead (e.g., birth year only)
- **Relative date inputs**: Use a Selector for "Today / Tomorrow / This week"
- **Date parts only**: Use separate Inputs for month-only or year-only fields

### Best Practices

1. **Always show a label**: Users need context to understand what date is required
2. **Provide helper text for constraints**: e.g., "Must be at least 18 years old"
3. **Support manual text entry**: Allow typing DD/MM/YYYY in addition to calendar selection for power users
4. **Indicate required fields**: Use `required` prop and asterisk to communicate mandatory fields
5. **Default to sensible focus**: On open, focus the selected date (or today if no selection)
6. **Constrain where necessary**: Use `minDate` / `maxDate` / `disabledDaysOfWeek` for valid ranges
7. **Format consistently**: Use `DD / MM / YYYY` as the default display format (Indian locale)
8. **Avoid pre-filling critical dates**: Don't pre-fill date of birth or payment dates unless certain

---

## Related Components

- **Input** (`/src/app/components/ui/input.tsx`): Trigger input follows the same styling as a text input
- **Popover** (`/src/app/components/ui/popover.tsx`): Desktop calendar panel uses popover positioning
- **Bottomsheet** (`/guidelines/MD/Component/bottomsheet.md`): Mobile calendar panel uses bottom sheet
- **Calendar** (`/src/app/components/ui/calendar.tsx`): Underlying calendar grid component
- **Icon** (`/guidelines/MD/Component/icon.md`): Navigation chevrons and trigger icons

---

## Browser Compatibility

- Modern browsers with CSS Grid, CSS Custom Properties, and CSS transitions
- Touch events required for drag-to-dismiss on mobile bottom sheet
- `focus-visible` pseudo-class for keyboard-only focus indicators
- `date-fns` or equivalent for locale-aware date formatting and manipulation
