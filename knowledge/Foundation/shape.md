# Shapes

Shapes are a foundational part of the Jio Design System.  
They are the **building blocks of all UI components**, helping communicate
meaning, hierarchy, interaction, and brand character consistently across
every touchpoint.

Shapes are not decorative.  
They are **semantic, functional, and intentional**.

---

## 1. Purpose

Shapes exist to:
- Communicate hierarchy and affordance
- Guide user attention
- Express brand character
- Create consistency across components and layouts
- Support interaction and state change

All shapes must follow the **core shape system** defined in this document.

---

## 2. Core Shapes

Jio's shape language is built on **three core shapes**:

1. Circle  
2. Pill  
3. Rounded Rectangle  

These shapes form the foundation for all UI components and visual elements

---

## 3. Circle

### Meaning
The circle is the **mother of all shapes** in the Jio system.
It represents Jio's core identity: **dynamic, warm, friendly, and inclusive**

### Usage
- Logos and brand marks
- Decorative accents
- Shape primitives (JioDot, Ribbon, Rainbow)
- Supporting UI elements

### Construction Rules
- Radius must be **fully rounded**
- Circle must always be **perfectly symmetrical**
- Never stretch, skew, or compress a circle

### Do
- Ensure radius is fully rounded  
- Maintain symmetry  

### Don't
- Distort the radius  
- Obscure the circle's geometry  

---

## 4. Pill

### Meaning
The pill is formed by **two connected circles**.
It is primarily used for **interactive elements**

### Usage
- Buttons
- Toggles
- Interactive pills
- Page navigators

### Construction Rules
- Corner radius must be **exactly half the height**
- Radius must remain consistent across sizes
- Size scales with content, not arbitrarily

### Interaction Guidance
- Rounded hemispherical corners reinforce interactivity
- Pills should visually invite action

### Do
- Fully round the corners  
- Maintain consistent radius  

### Don't
- Reduce radius when resizing  
- Flatten pill ends  

---

## 5. Rounded Rectangle

### Meaning
The rounded rectangle is an **extension of the pill**, designed to
house larger and nested content

### Usage
- Cards
- Containers
- Sheets
- Panels
- Content blocks

### Construction Rules
- All corners must be rounded
- Radius must scale with viewport and breakpoint
- Rounded corners should **direct attention inward**, not outward

### Do
- Use rounded rectangles for containers  
- Ensure corners are fully rounded  

### Don't
- Use straight edges for elevated content  
- Use "almost rounded" corners  

---

## 6. Shapes in UI

Shapes play a critical role in **interaction, hierarchy, and usability**

---

### 6.1 Corner Radius System

Corner radius must be **consistent and proportional**.

#### Outer vs Inner Radius
- Outer containers use **larger radius**
- Inner containers use **smaller radius**

#### Responsive Scaling

| Device | Outer Radius | Inner Radius |
|------|-------------|-------------|
| Feature phone | 16px | 8px |
| Mobile / Tablet | 24px | 16px |
| Desktop | 32px | 24px |
| Large screens | 32px | 24px |

---

### 6.2 Symmetry

Symmetry is critical to:
- Build trust
- Improve comfort
- Maintain visual harmony

Rules:
- All corners in a shape must match
- Avoid asymmetrical rounding

### Do
- Use consistent radius across shape families  

### Don't
- Mix different corner radii in one shape  

---

### 6.3 Combining Shapes

Core shapes can be combined to create components.

Rules:
- Maintain consistent corner radius
- Prefer rounded edges for interactive elements
- Avoid straight edges for elevated content

### Do
- Round image card corners  
- Use shape to guide focus inward  

### Don't
- Use straight edges for interactive UI  
- Mix sharp and rounded edges inconsistently  

---

### 6.4 Shape & State

Shape can be used to communicate **state change**.

Examples:
- Pill inside a group of rounded rectangles → interactive
- Shape change on selection → active state

Rules:
- Shape change must be consistent
- Do not introduce new shapes for states

---

### 6.5 Elevated vs Embedded Content

- **Elevated content** → Rounded edges (buttons, cards)
- **Embedded content** → Straight edges (static content)

This distinction helps users understand what is interactive

---

## 7. The Rainbow

The Rainbow is a **brand expression shape**, extending from the Ribbon
to add delight and dimension to experiences

---

### 7.1 Purpose

The Rainbow is used to:
- Highlight content
- Frame imagery or text
- Create moments of joy

---

### 7.2 Rainbow Generation

Rainbow creation follows **three steps**:

1. **Orientation**
   - Always centered
   - Anchored to bottom or left of canvas

2. **Scale**
   - Size equals the shortest canvas edge
   - Scales relative to device size

3. **Colour**
   - Uses primary colours
   - On coloured backgrounds, rainbow should be lighter

---

### 7.3 Framing Content

- Rainbow can sit behind images or illustrations
- Used to frame headlines or subheadings
- Adds depth without overpowering content

---

### 7.4 Z-Axis Rules

- Text inside the rainbow → image/illustration goes underneath
- Text outside the rainbow → image/illustration goes above

---

### 7.5 Application

- Outside Jio ecosystem → must include JioDot logo
- Inside ecosystem → can act as standalone enhancement

---

## 8. Accessibility Considerations

- Shapes must not be the only indicator of interaction
- Pair shape cues with colour, text, or motion
- Maintain sufficient contrast between shape and background
- Avoid excessive decoration that distracts from content

---

## 9. Do & Don't

### Do
- Use core shapes consistently  
- Scale radius with breakpoints  
- Use rounded edges for interactive content  
- Maintain symmetry  

### Don't
- Invent new shape styles  
- Mix sharp and rounded edges arbitrarily  
- Distort core shapes  
- Use shape without meaning  

---

## 10. Governance

Any change to shapes requires:
- Design System approval
- Cross-platform validation
- Component audit
- Documentation update

---
