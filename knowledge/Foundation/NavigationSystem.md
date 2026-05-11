# Navigation System

The Navigation System defines how users **move, explore, and orient themselves**
across Jio digital products.

It combines:
- Structural framework
- Navigation patterns
- User behaviours
- Screen transitions

Together, these ensure navigation is **predictable, flexible, and scalable**
across platforms and services.

---

## 1. Purpose

The navigation system exists to:
- Enable effortless movement across services
- Maintain orientation and hierarchy
- Support exploration without confusion
- Scale consistently across devices

Navigation is **systemic**, not component-driven.

---

## 2. Navigation Framework (Structural Model)

Navigation is organised into **three tiers**.

### 2.1 Global Navigation

**Purpose**
- Provides access to global actions and settings
- Remains consistent across services

**Elements**
- Brandmark
- Search
- Profile

Rules:
- Always visible
- Always accessible
- Never context-dependent

---

### 2.2 Local Navigation

**Purpose**
- Helps users navigate within a service

**Elements**
- Primary links
- Secondary links
- Utilities

Rules:
- Changes per service
- Reflects information hierarchy
- Can expand or collapse

---

### 2.3 Contextual Navigation

**Purpose**
- Supports navigation within a specific task or screen

Examples:
- Tabs
- Breadcrumbs
- Contextual headers

Rules:
- Always contextual
- Never global
- Scope-limited

---

## 3. Navigation Patterns

Patterns are **reusable navigation structures** built on the framework.

### Supported Patterns
- Global Header
- Contextual Header
- Mega Menu
- Burger Navigation
- Tabs
- Breadcrumb
- Bottom Navigation
- Footer Navigation

Patterns map to specific tiers and navigation types.

---

### Pattern Mapping

| Pattern | Navigation Tier | Navigation Type |
|------|-----------------|-----------------|
| Global Header | Global | Forward |
| Contextual Header | Contextual | Reverse |
| Mega Menu | Local | Forward |
| Burger Navigation | Local | Forward |
| Tabs | Contextual | Lateral |
| Breadcrumb | Contextual | Forward / Reverse |
| Bottom Navigation | Local | Lateral |
| Footer Navigation | Local | Forward |

---

## 4. Navigation Behaviour

Behaviours define **how navigation responds to user interaction**.

### 4.1 Brandmark Behaviour

- Acts as orientation anchor
- On mobile → JioDot
- On desktop → Service logo + name
- Clicking brandmark returns to home (optional)

---

### 4.2 Search Behaviour

Search exists in three modes:
1. Active Search
2. Recent Search
3. Results Screen

Rules:
- Always accessible
- Adapts to service context
- Does not interrupt navigation flow

---

### 4.3 Profile Behaviour

- Anchored to top-right
- Opens profile drawer
- Provides access to global & local settings

Behaviour:
- Mobile → Full screen
- Desktop → Side drawer

---

### 4.4 Switcher Behaviour

- Allows movement between services
- Opens from global header
- Auto-closes after selection

Rules:
- Single selection at a time
- Organised by categories

---

## 5. Navigation Transitions (Motion Rules)

Transitions define **how users move between screens**.

---

### 5.1 Lateral Transitions

**Purpose**
- Switch between screens at the same hierarchy level

Examples:
- Tabs
- Bottom navigation
- Sibling screens

Subtypes:
- Top-level transitions
- Sibling transitions

---

### 5.2 Forward Transitions

**Purpose**
- Move deeper into hierarchy

Types:
- Downward (parent → child)
- Direct (any screen → any screen)

Examples:
- List → detail
- Card → content

---

### 5.3 Reverse Transitions

**Purpose**
- Move backward in hierarchy or history

Types:
- Upward (child → parent)
- Chronological (back button)

Rules:
- Must always feel reversible
- Must preserve context

---

## 6. Component Navigation Relationship

Navigation components must:
- Respect navigation tier
- Use correct transition type
- Follow behaviour rules

Components must never invent navigation logic.

---

## 7. Accessibility Considerations

- Navigation must be keyboard accessible
- Screen readers must announce hierarchy
- Focus order must follow navigation flow
- Back actions must be predictable

---

## 8. Do & Don't

### Do
- Use the defined navigation tiers  
- Match patterns to hierarchy  
- Use correct transition direction  
- Preserve user orientation  

### Don't
- Mix navigation tiers  
- Skip hierarchy levels  
- Use motion without meaning  
- Break back navigation  

---

## 9. Governance

Any navigation change requires:
- Design System approval
- Behaviour validation
- Transition validation
- Accessibility review
- Documentation update

---
