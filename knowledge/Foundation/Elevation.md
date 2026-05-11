# Elevation

Elevation defines the **relative distance between UI surfaces along the Z-axis**.
It is used to establish hierarchy, focus, and spatial relationships between surfaces.

Elevation is **not decorative**.  
It exists to communicate **structure, interactivity, and importance**.

---

## 1. Purpose

Elevation helps to:
- Separate surfaces visually
- Indicate interactivity
- Communicate hierarchy and focus
- Reflect spatial relationships between UI elements

Elevation must always be applied using **tokens**, never arbitrary values.

---

## 2. What Is Elevation

Elevation is the measured distance between two surfaces along the Z-axis.

Elevated surfaces:
- Sit visually above other surfaces
- May cast shadows or appear layered
- Help users understand which elements are interactive or in focus

:contentReference[oaicite:1]{index=1}

---

## 3. Ways to Depict Elevation

Elevation can be expressed in **three approved ways**:

### 3.1 Shadows
- Indicates physical distance between surfaces
- Commonly used for cards and interactive elements
- Strongly associated with interactivity

### 3.2 Overlay Tints
- Uses a translucent overlay to separate layers
- Useful when shadows are insufficient
- Often paired with drawers or overlays

### 3.3 Overlay Blurs
- Blurs background content
- Strongly shifts focus to foreground elements
- Used for modals and critical interruptions

:contentReference[oaicite:2]{index=2}

---

## 4. Elevation Hierarchy

Every elevation level has a **unique semantic meaning**.
Higher elevation always visually dominates lower elevation.

Elevation is used to:
- Move surfaces in front of others
- Indicate spatial relationships
- Draw attention to the most important element on screen

:contentReference[oaicite:3]{index=3}

---

## 5. Elevation Tokens (Canonical)

| Token | Role | Value |
|-----|------|------|
| `elevation.10` | Canvas | 10 |
| `elevation.20` | Cards | 20 |
| `elevation.30` | Tooltips | 30 |
| `elevation.40` | Navigation | 40 |
| `elevation.50` | FAB / Drawers | 50 |
| `elevation.60` | Overlays / Blurred Backgrounds | 60 |
| `elevation.70` | Glass Interaction / Modals / Notifications / Toasts | 70 |

---

## 6. Elevation Levels — Usage Rules

### Elevation 10 — Canvas
- Base surface of the application
- All other elements sit above this layer
- Never casts shadows

---

### Elevation 20 — Cards
- Content containers
- List items
- Grouped information blocks

Rules:
- Must feel liftable
- Indicates passive interactivity or grouping

---

### Elevation 30 — Tooltips
- Contextual help
- Temporary information surfaces

Rules:
- Must appear above cards
- Must disappear automatically

---

### Elevation 40 — Navigation
- App bars
- Bottom navigation
- Persistent navigation elements

Rules:
- Always above content
- Never scrolls under content

---

### Elevation 50 — FAB / Drawers
- Floating Action Buttons
- Side drawers
- Expandable panels

Rules:
- Indicates primary or secondary actions
- Must visually dominate navigation

---

### Elevation 60 — Overlays / Blurred Backgrounds
- Background dimming layers
- Focus-shifting overlays

Rules:
- Blocks interaction with underlying content
- Often paired with modals

---

### Elevation 70 — Glass / Modals / Notifications / Toasts
- Modal dialogs
- System notifications
- Toast messages
- Glass-style interactions

Rules:
- Highest elevation in the system
- Demands immediate user attention
- Must be dismissible or time-bound

---

## 7. Elevation Ordering Rules (Non-Negotiable)

- Higher elevation **always appears above** lower elevation
- Two elements with the same elevation must not visually overlap
- Never skip levels without justification
- Do not stack multiple elevations unnecessarily

---

## 8. Accessibility Considerations

- Elevation must not be the only indicator of focus
- Always pair elevation with:
  - Contrast
  - Motion (when applicable)
  - Clear boundaries
- Overlays must block background interaction for assistive technologies

---

## 9. Platform Notes

| Platform | Implementation |
|--------|----------------|
| Web | `box-shadow`, `backdrop-filter`, z-index |
| Android | Elevation & shadow APIs |
| iOS | Z-position, blur materials |

Visual appearance may vary, but **semantic hierarchy must remain identical**.

---

## 10. Do & Don't

### Do
✔ Use elevation tokens only  
✔ Use elevation to communicate hierarchy  
✔ Match elevation to component role  

### Don't
✖ Invent new elevation values  
✖ Use elevation purely for decoration  
✖ Stack shadows excessively  

---

## 11. Governance

Any change to elevation requires:
- Design System approval
- Cross-platform validation
- Token update
- Documentation update

---

## References
- Elevation Standards & Hierarchy :contentReference[oaicite:4]{index=4}
