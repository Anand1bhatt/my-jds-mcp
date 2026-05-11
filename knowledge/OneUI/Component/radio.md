# Radio — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Radio (node `554:7747`)

## Variants
- **State**: Unselected, Selected, Disabled
- **Size**: S (16px), M (20px)
- **Label position**: Right (default)

## Usage
- Single-select from a group of mutually exclusive options
- Settings panels, form option groups

## Anatomy
- Radio circle (outer ring + inner fill dot)
- Label text (right)

## Tokens
- Unselected border: `grey/on-default/medium-s`
- Unselected fill: transparent
- Selected border: `[appearance] high`
- Selected inner dot: `[appearance] high`
- Disabled: `04.1 Disabled` opacity
- Touch target: min 44×44px
- Outer circle: 20px (M), 16px (S)
- Inner dot: 10px (M), 8px (S)

## Rules
- Always group radios with a shared name attribute
- Exactly one radio in a group must be selected at all times (except on initial load before user selection)
- Never use checkbox for single-select scenarios
