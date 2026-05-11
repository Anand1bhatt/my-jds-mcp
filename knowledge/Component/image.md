# JDS Image Rules

Canonical specification for image usage across all JDS pages.

---

## Mandatory Rule: Indian Context Only

Every image used on the website — hero banners, card backgrounds, promotional visuals, lifestyle photos — **must** be strictly in an **Indian context**.

### What qualifies as "Indian context"

- **People:** Indian individuals/families (South Asian appearance, traditional or modern Indian attire)
- **Settings:** Indian cities, landmarks, homes, streets, markets, offices, campuses
- **Cultural cues:** Indian festivals (Diwali, Holi, etc.), cricket matches, Indian food, Indian architecture
- **Products/scenarios:** UPI/mobile payments in India, Indian grocery shopping, Indian classrooms/students

### What is prohibited

- Generic Western lifestyle images with no Indian connection
- Stock photos featuring exclusively non-Indian people or settings, unless the context is clearly universal (e.g. a global sports event)
- Placeholder images or images from non-Indian cultural contexts

### Unsplash search guidelines

When searching for images via the Unsplash API, **always** include "Indian" or "India" as a keyword in the query:

```
Good:  "Indian family watching cricket television"
Good:  "Indian woman shopping vegetables market"
Good:  "Indian student laptop online education"
Good:  "India cricket stadium night floodlights"

Bad:   "family watching TV"           (too generic)
Bad:   "woman grocery shopping"       (no Indian context)
Bad:   "student using laptop"         (no Indian context)
```

### Alt text

Alt text must accurately describe the Indian context of the image:

```tsx
// Correct
alt="Indian family celebrating Diwali together"
alt="Indian woman shopping for vegetables at a local market"

// Incorrect
alt="Family celebrating"            (missing Indian context)
alt="Woman shopping for groceries"  (missing Indian context)
```

---

## Image Sizing & Fit

| Context             | Fit mode       | Notes                                  |
|---------------------|----------------|----------------------------------------|
| Hero banner slides  | `object-cover` | Full-bleed, fills entire slide area    |
| Image card bg       | `object-cover` | Full-bleed, fills card area            |
| Thumbnail / avatar  | `object-cover` | Cropped to circle or rounded square    |

Images must always fill their container completely using `object-cover`. Never leave blank space or use `object-contain` for background/hero images.

---

## Typography Rules

All text overlaid on images must use:

- **Font family:** `var(--font-family-jiotype)` exclusively
- **Font weights:** Only the four permitted JDS weight tokens:
  - `var(--font-weight-normal)` (400)
  - `var(--font-weight-medium)` (500)
  - `var(--font-weight-bold)` (700)
  - `var(--font-weight-black)` (900)
- **Text color on images:** Always `var(--global-white)` with a gradient overlay for readability
- **No other fonts or weights** are allowed.
