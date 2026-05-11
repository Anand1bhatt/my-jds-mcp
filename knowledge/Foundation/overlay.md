# Overlays

Overlays temporarily reduce the prominence of background content to
guide user attention toward an elevated surface such as a modal,
dialog, drawer, or notification.

Overlays are **functional UI layers**, not decorative elements.
They must be used intentionally, sparingly, and consistently.

---

## 1. Purpose

Overlays exist to:
- Shift focus to critical or time-sensitive content
- Prevent interaction with background surfaces
- Reinforce elevation hierarchy
- Support safe decision-making and task completion

Overlays must always be implemented using **system-defined rules and tokens**.

---

## 2. Overlay & Elevation Relationship

Overlays are always paired with **high-elevation surfaces**.

| Context | Elevation |
|------|-----------|
| Background overlay | Elevation 60 |
| Modal / Glass / Notifications | Elevation 70 |

Rules:
- Overlay always sits **below** the focused surface
- Overlay must never visually overpower the foreground content
- Overlay must fully cover the interactive background area

---

## 3. Overlay Types

The system supports **two overlay types** only.

---

### 3.1 Overlay-Tint

Overlay-Tint uses a semi-transparent neutral colour layer.

**Use When**
- Background context should remain visible
- Task interruption is moderate
- Used with drawers, bottom sheets, quick actions

**Avoid When**
- Strong focus or decision-making is required
- Background content is visually complex

---

### 3.2 Overlay-Blur

Overlay-Blur combines background blur with a darker overlay.

**Use When**
- Strong focus is required
- Critical confirmations or blocking decisions
- Used with modals, dialogs, notifications

**Avoid When**
- Performance constraints exist
- Background clarity is required

---

## 4. Overlay Creation Rules

All overlays are created using **three parameters**:
**Colour · Opacity · Blur**

---

### 4.1 Overlay-Tint Creation

**Colour**
- Neutral shade only
- Never use brand or accent colours


---

## 5. Overlay Usage Rules (NON-NEGOTIABLE)

These rules **must never be violated**.

1. Only **one overlay** may exist per interaction
2. Overlay must **block all background interaction**
3. Overlay must be dismissed when the foreground surface is dismissed
4. Overlay must not scroll independently
5. Overlay must cover the entire interactive canvas
6. Overlays must never stack visually
7. Overlay behaviour must be identical across platforms

---

## 6. Modal & Component Application

### Notifications
- Used for alerts, reminders, order updates
- **Overlay-Blur is mandatory**

---

### Dialog Boxes
- Used for confirmations and critical decisions
- **Overlay-Blur is mandatory**

---

### Drawers
- Used for navigation or contextual tasks
- **Overlay-Tint only**

---

## 7. Accessibility Considerations (MANDATORY)

Overlays must comply with accessibility requirements at all times.

### Focus Management
- Focus must move to the foreground surface on open
- Focus must be trapped within the foreground surface
- Focus must return to the triggering element on close

### Screen Readers
- Background content must be hidden from assistive technologies
- Only foreground content should be discoverable
- Overlay itself should not receive focus

### Visual Accessibility
- Overlay opacity must preserve readable contrast
- Do not rely on blur alone to indicate focus
- Foreground content must meet WCAG contrast requirements

---

## 8. Platform Behaviour

| Platform | Implementation |
|--------|----------------|
| Web | RGBA overlay + backdrop-filter |
| Android | Scrim + blur layer |
| iOS | UIVisualEffectView |

Visual rendering may vary, but **behaviour and hierarchy must remain identical**.

---

## 9. Do & Don't

### Do
- Use Overlay-Tint or Overlay-Blur only  
- Match overlay type to task importance  
- Block background interaction completely  
- Ensure clear focus transfer  

### Don't
- Use brand or accent colours  
- Reduce opacity arbitrarily  
- Stack multiple overlays  
- Allow background interaction  

---

## 10. Governance

Any change to overlays requires:
- Design System approval
- Elevation alignment
- Accessibility validation
- Token update
- Documentation update

---
