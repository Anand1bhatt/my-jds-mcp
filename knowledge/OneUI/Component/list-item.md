# ListItem & ListItemGroup — OneUI Micropattern

## Figma Source
File: OneUI Micropatterns (`y4r5eCoZhqvPw1U1bm2qfw`) — Pages: ListItem (node `2428:2233`), ListItemGroup (node `2427:2233`)

## Overview
Versatile row component for rendering lists, menus, settings, and content feeds. ListItemGroup wraps multiple ListItems with optional section header.

## ListItem Variants
- **Leading**: None, Icon, Avatar, Image, Checkbox, Radio
- **Trailing**: None, Icon, Switch, Badge, Metadata text, Chevron
- **Lines**: Single, Double, Triple (multiline)
- **State**: Default, Pressed, Selected, Disabled
- **Divider**: With, Without

## Anatomy
- Leading element (optional, 40–48px zone)
- Content area (flex-grow)
  - Primary text (System M, Label High)
  - Secondary text (System S, Label Low) — optional
  - Tertiary text (System XS, Label Low) — optional
- Trailing element (optional, right-aligned)

## Tokens
- Background Default: transparent / `02 Surface` default
- Background Pressed: `grey/on-default/medium-t` at state layer opacity
- Background Selected: `[appearance] tinted`
- Primary text: `grey/on-default/medium-t`
- Secondary text: `grey/on-default/low-t`
- Divider: `grey/on-default/low-s` (1px, inset left to content start)
- Min height: 48px (single), 64px (double), 80px (triple)
- Horizontal padding: scale 4 (16px)
- Vertical padding: scale 3 (12px)

## ListItemGroup
- Optional section header (System XS, Label High, uppercase)
- Header background: `02 Surface` bg-subtle
- Groups separated by 8px gap or divider line

## Rules
- Touch target: full row width, min 48px height
- Trailing chevron: always for navigable items
- Trailing switch/checkbox: triggers toggle, not navigation
- Disabled items: `04.1 Disabled` opacity, no interaction
