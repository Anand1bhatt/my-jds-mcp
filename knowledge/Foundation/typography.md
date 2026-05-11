# JDS Typography Rules

Canonical specification for all typography across JDS pages. Every text element must follow these rules with no exceptions.

---

## Font Family (MANDATORY)

> **The ONLY permitted font family is `var(--font-family-jiotype)`.**

- Resolves to: `'JioType', system-ui, -apple-system, sans-serif`
- Defined in `/src/styles/theme.css`
- `@font-face` declarations live in `/src/styles/fonts.css`
- **Never** use any other font family (Inter, Roboto, Arial, monospace, serif, etc.)

Every text element — headings, paragraphs, labels, buttons, inputs, spans — must either inherit or explicitly set:

```css
font-family: var(--font-family-jiotype);
```

---

## Permitted Font Weights

Only these four JDS weight tokens are allowed:

| Token                       | Value | Usage                                     |
| --------------------------- | ----- | ----------------------------------------- |
| `var(--font-weight-normal)` | 400   | Body text, descriptions, input text       |
| `var(--font-weight-medium)` | 500   | Brand labels, paragraph text, subtitles   |
| `var(--font-weight-bold)`   | 700   | CTA buttons, sub-headings                 |
| `var(--font-weight-black)`  | 900   | Section titles, card headlines, hero text |

### Prohibited

- Arbitrary `font-weight` numbers (e.g. `600`, `800`, `100`)
- Tailwind font-weight utilities (e.g. `font-semibold`, `font-thin`, `font-extrabold`)

---

## Permitted Font Sizes

| Token                 | Value | Usage                                 |
| --------------------- | ----- | ------------------------------------- |
| `--text-h1`           | 88px  | Hero display                          |
| `--text-h2`           | 64px  | Page-level section headings (raw)     |
| `--text-heading-l`    | 64px  | **Desktop section headings** ($heading/L) |
| `--text-heading-m`    | 40px  | **Tablet section headings** ($heading/M) |
| `--text-heading-s`    | 24px  | **Mobile section headings** ($heading/S) |
| `--text-h3`           | 32px  | Card headlines (clamp max)            |
| `--text-h4`           | 24px  | Card headlines (clamp min)            |
| `--text-heading-xs`   | 24px  | Grid Banner product name (Heading/xs) |
| `--text-body-large`   | 24px  | Large body / intro text               |
| `--text-body-l`       | 24px  | **Desktop section support text** ($body/L) |
| `--text-body-m`       | 18px  | **Tablet section support text** ($body/M) |
| `--text-body-s`       | 16px  | **Mobile section support text** ($body/S) |
| `--text-button-large` | 18px  | Large CTA button text                 |
| `--text-base`         | 16px  | Body text, card descriptions          |
| `--text-button`       | 16px  | Standard button text                  |
| `--text-label`        | 14px  | Brand labels, small CTA buttons       |

### Responsive sizing

Use `clamp()` with JDS tokens — never arbitrary pixel values:

```css
font-size: clamp(var(--text-h4), 3vw, var(--text-h3));
```

### Prohibited

- Tailwind text-size utilities (e.g. `text-2xl`, `text-sm`, `text-xs`)
- Arbitrary pixel sizes not in the token table

---

## Section Title & Subtitle Typography (RESPONSIVE)

### Desktop (992px and above — L/XL breakpoints)

**Section Title (`--text-heading-M`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-heading-m)      — 40px ($heading/M) — MANDATORY
font-weight:  var(--font-weight-black)   — 900
color:        var(--foreground)
line-height:  1.2
text-align:   center                     — MANDATORY
```

**Section Support Text (`--text-body-M`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-body-m)         — 18px ($body/M) — MANDATORY
font-weight:  var(--font-weight-medium)  — 500
color:        var(--grey-80)
line-height:  1.5
text-align:   center                     — MANDATORY
margin-top:   var(--space-4)             — 16px below the title
margin-bottom: var(--space-8)            — 32px above section content
```

---

### Tablet (620px - 991px — M breakpoint)

**Section Title (`--text-heading-M`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-heading-m)      — 40px ($heading/M) — MANDATORY
font-weight:  var(--font-weight-black)   — 900
color:        var(--foreground)
line-height:  1.2
text-align:   center                     — MANDATORY
```

**Section Support Text (`--text-body-M`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-body-m)         — 18px ($body/M) — MANDATORY
font-weight:  var(--font-weight-medium)  — 500
color:        var(--grey-80)
line-height:  1.5
text-align:   center                     — MANDATORY
margin-top:   var(--space-3)             — 12px below the title
margin-bottom: var(--space-8)            — 32px above section content
```

---

### Mobile (< 620px — XS/S breakpoints)

**Section Title (`--text-heading-S`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-heading-s)      — 24px ($heading/S) — MANDATORY
font-weight:  var(--font-weight-black)   — 900
color:        var(--foreground)
line-height:  1.2
text-align:   center                     — MANDATORY
```

**Section Support Text (`--text-body-S`):**
```
font-family:  var(--font-family-jiotype)
font-size:    var(--text-body-s)         — 16px ($body/S) — MANDATORY
font-weight:  var(--font-weight-medium)  — 500
color:        var(--grey-80)
line-height:  1.5
text-align:   center                     — MANDATORY
margin-top:   var(--space-2)             — 8px below the title
margin-bottom: var(--space-8)            — 32px above section content
```

---

### Implementation Pattern (Responsive)

Use responsive font-size with CSS custom properties and media queries:

```tsx
<h2
  className="m-0 text-center"
  style={{
    fontFamily: "var(--font-family-jiotype)",
    fontSize: "var(--text-heading-s)", // Mobile first
    fontWeight: "var(--font-weight-black)",
    color: "var(--foreground)",
    lineHeight: 1.2,
    textAlign: "center",
  }}
>
  <style jsx>{`
    @media (min-width: 620px) {
      h2 {
        fontSize: var(--text-heading-m);
      }
    }
    @media (min-width: 992px) {
      h2 {
        fontSize: var(--text-heading-l);
      }
    }
  `}</style>
  Section Title Here
</h2>
```

**Preferred approach using Tailwind breakpoints:**

Create utility classes or use inline media query logic. For consistency, sections should implement:
- Mobile (default): `fontSize: 'var(--text-heading-s)'`
- Tablet (@media min-width: 620px): `fontSize: 'var(--text-heading-m)'`
- Desktop (@media min-width: 992px): `fontSize: 'var(--text-heading-l)'`

> **All section titles and subtitles are always center-aligned across all breakpoints.** Both `text-align: center` on the text element AND horizontal centering within the container. See `layout.md` → "Section Title Alignment" for the canonical rule.

---

## Alignment Rules (MANDATORY)

### Section-level headings & subtitles

| Element          | Alignment     | Rule                                 |
| ---------------- | ------------- | ------------------------------------ |
| Section title    | `text-center` | Always center-aligned, no exceptions |
| Section subtitle | `text-center` | Always center-aligned, no exceptions |

### Card-level text (inside Image Cards)

| Element       | Alignment   | Rule                                     |
| ------------- | ----------- | ---------------------------------------- |
| Brand label   | `text-left` | Left-aligned within the card overlay     |
| Card headline | `text-left` | Left-aligned within the card overlay     |
| CTA buttons   | `flex` left | Left-aligned row within the card overlay |

### Prohibited patterns

```tsx
/* PROHIBITED — left-aligned section title */
<h2 style={{ textAlign: 'left' }}>Section Title</h2>

/* PROHIBITED — no alignment specified (defaults to left) */
<h2 className="m-0 mb-8">Section Title</h2>
```

---

## Implementation Examples

### Section heading (center-aligned)

```tsx
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
</h2>
```

### Section subtitle / support text (center-aligned)

```tsx
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
</p>
```

### Card headline (left-aligned inside card overlay)

```tsx
<h3
  className="m-0 mt-1.5 whitespace-pre-line"
  style={{
    fontFamily: "var(--font-family-jiotype)",
    fontSize: "clamp(var(--text-h4), 2.5vw, var(--text-h3))",
    fontWeight: "var(--font-weight-black)",
    color: "var(--global-white)",
    lineHeight: 1.2,
  }}
>
  Card headline here
</h3>
```

### CTA button

```tsx
<button
  style={{
    fontFamily: "var(--font-family-jiotype)",
    fontSize: "var(--text-label)",
    fontWeight: "var(--font-weight-bold)",
    lineHeight: 1.5,
    borderRadius: "var(--radius-button)",
  }}
>
  Button Label
</button>
```

---

## Line Heights

| Element type           | Line-height |
| ---------------------- | ----------- |
| Display / hero (h1)    | 1.1         |
| Section titles (h2/h3) | 1.2         |
| Card headlines         | 1.2         |
| Sub-headings (h4)      | 1.4         |
| Body / paragraph text  | 1.5         |
| Labels / buttons       | 1.5         |

---

## Color Tokens for Text

| Context                   | Color token           |
| ------------------------- | --------------------- |
| Default body text         | `var(--foreground)`   |
| Subtitle / secondary text | `var(--grey-80)`      |
| Text on dark overlay      | `var(--global-white)` |
| Primary accent text       | `var(--primary-50)`   |
| Muted text                | `var(--grey-60)`      |
| Error text                | `var(--error-50)`     |

---

## Checklist

Before merging any component, verify:

- [ ] All text uses `font-family: var(--font-family-jiotype)`
- [ ] All font weights use one of the four permitted tokens (400/500/700/900)
- [ ] All font sizes use JDS `--text-*` tokens (or `clamp()` with tokens)
- [ ] All section titles and subtitles have `text-align: center`
- [ ] No Tailwind text-size or font-weight utilities are used
- [ ] No arbitrary font families, weights, or sizes appear anywhere