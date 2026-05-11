# BottomNav — OneUI Micropattern

## Figma Source
File: OneUI Micropatterns (`y4r5eCoZhqvPw1U1bm2qfw`) — Pages: BottomNav (node `2:13445`), BottomNav.Item (node `2:15048`)

## Overview
Primary navigation bar anchored to the bottom of mobile screens. Persistent across all main sections.

## Variants (BottomNav)
- **Item count**: 3, 4, 5 items
- **Style**: Icon only, Icon + Label

## Variants (BottomNav.Item)
- **State**: Default, Active, Disabled
- **Badge**: None, Dot, Count

## Anatomy
- Container: full-width, fixed bottom, respects safe area inset
- Items: equal-width flex children
  - Icon (24px)
  - Label (System 3XS, Label Medium) — optional
  - Badge overlay (top-right of icon)

## Tokens
- Background: `02 Surface` default
- Active icon/label: `[Theme] high` OR `indigo/surface/fg-minimal`
- Inactive icon/label: `grey/on-default/low-t`
- Active indicator pill: `[appearance] tinted` background behind icon
- Height: 56px + safe area bottom inset
- Border top: `grey/on-default/low-s` (1px)
- Item touch target: full height × equal width

## Rules
- 3–5 items maximum. More than 5: use a drawer/menu instead
- Active state: only one item active at a time
- Labels: max 12 characters, no wrapping
- Bottom safe area: always add `env(safe-area-inset-bottom)` padding
