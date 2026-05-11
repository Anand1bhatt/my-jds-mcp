# Glass

Glass is a **translucent surface treatment** that creates a sense of depth
when elevated above a page or image. It allows background content to remain
visible while subtly separating foreground elements.

Glass is used to **highlight information or actions** without fully obscuring
the underlying content.

Glass is **functional**, not decorative.

---

## 1. Purpose

Glass exists to:
- Create depth without heavy shadows
- Preserve background context while elevating content
- Support lightweight, contextual interactions
- Enhance visual hierarchy on imagery and coloured backgrounds

Glass must always be created using **system-defined rules and tokens**.

---

## 2. Glass & Elevation Relationship

Glass surfaces always sit at **high elevation levels**.

| Context | Elevation |
|------|-----------|
| Glass surfaces | Elevation 70 |

Rules:
- Glass always appears above overlays
- Glass must never appear at low elevations
- Glass must always visually separate from its background

---

## 3. Glass Types

The system supports **two glass levels**, selected based on surface size and importance.

---

### 3.1 Soft Blur Glass

Used for **small surfaces** and lightweight interactions.

**Typical Use**
- Pills
- Buttons
- Small badges
- Compact contextual actions

**Characteristics**
- Subtle blur
- Preserves background detail
- Low visual dominance

---

### 3.2 Heavy Blur Glass

Used for **large surfaces** that must maintain readability over imagery.

**Typical Use**
- Image cards
- Content panels
- Large contextual surfaces

**Characteristics**
- Stronger blur
- Reduced background distraction
- High readability

---

## 4. Glass Creation Rules

Glass is created using **three parameters**:
**Colour · Opacity · Blur**

---

### 4.1 Soft Blur Glass — Creation

**Colour**

---

## 5. Glass Usage Rules (NON-NEGOTIABLE)

These rules must **never** be violated.

1. Glass must always be used at **Elevation 70**
2. Only **one glass surface** per interaction layer
3. Glass must always maintain readable foreground content
4. Glass must never be used without blur
5. Glass must never replace overlays for blocking actions
6. Glass must never be stacked on glass
7. Glass must always respect contrast and accessibility rules

---

## 6. Application Patterns

### Service to Service
- Small glass buttons with icon + label
- Used to move users between services

---

### Feature-led
- Glass pills over imagery
- Used to add context to image cards

---

### Contextual
- Glass panels containing text + icon
- Used to notify or prompt user actions


---

## 7. Accessibility Considerations (MANDATORY)

Glass must remain accessible in all contexts.

### Readability
- Foreground text must meet WCAG contrast requirements
- Heavy blur must be used on text-heavy glass surfaces
- Never place low-contrast text on glass

### Focus & Interaction
- Glass elements must be keyboard accessible
- Focus indicators must be clearly visible on glass
- Glass must not interfere with screen reader navigation

### Motion & Performance
- Blur effects must not cause motion discomfort
- Avoid glass on low-performance devices when possible

---

## 8. Platform Behaviour

| Platform | Implementation |
|--------|----------------|
| Web | `backdrop-filter: blur()` |
| Android | RenderEffect / blur layer |
| iOS | UIVisualEffectView |

Visual rendering may differ, but **semantic behavior must remain identical**.

---

## 9. Do & Don't

### Do
- Use glass for contextual elevation  
- Choose blur level based on surface size  
- Ensure text readability at all times  
- Pair glass with elevation, not shadows  

### Don't
- Use glass for blocking interactions  
- Apply glass without blur  
- Stack multiple glass layers  
- Use coloured glass backgrounds  

---

## 10. Governance

Any change to glass requires:
- Design System approval
- Elevation alignment
- Accessibility validation
- Token update
- Documentation update

---
