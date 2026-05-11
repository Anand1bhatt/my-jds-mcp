# TabGroup & Tab.Item — OneUI Micropattern

## Figma Source
File: OneUI Micropatterns (`y4r5eCoZhqvPw1U1bm2qfw`) — Pages: TabGroup (node `1:57286`), Tab.Item (node `1:54773`)

## Overview
Horizontal tab navigation for switching between content views on a single screen. Scrollable on mobile when tabs overflow.

## Variants (TabGroup)
- **Style**: Underline, Filled/Pill, Compact
- **Scroll**: Fixed (equal width), Scrollable (natural width)

## Variants (Tab.Item)
- **State**: Default, Active, Disabled
- **Content**: Text only, Text + Icon, Icon only
- **Badge**: None, Dot, Count

## Anatomy (Tab.Item)
- Icon (optional, 20px)
- Label text (System S/M, Label Medium)
- Active indicator (underline or pill background)
- Badge (optional, overlaid top-right)

## Tokens
- Active label: `[appearance] high` or `indigo/surface/fg-minimal`
- Inactive label: `grey/on-default/low-t`
- Active underline: `[appearance] high` (2px bottom border)
- Active pill background: `[appearance] tinted`
- Tab height: 44px (touch target compliant)
- Padding: scale 3 (12px) horizontal per item
- Active indicator height: 2px (underline style)

## Rules
- Minimum 2 tabs, maximum 6 (fixed), unlimited (scrollable)
- Active tab: always visible without scrolling on initial load
- Tab labels: max 2 words, no wrapping
- Scrollable tabs: show fade/gradient at edge to indicate overflow
- Never use tabs for steps/wizards — use Stepper instead
