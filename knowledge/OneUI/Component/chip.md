# Chip — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Chip (node `2597:3111`)

## Variants
- **Type**: Filter, Input (removable), Suggestion
- **State**: Default, Selected, Disabled
- **Size**: S, M
- **Leading**: None, Icon, Avatar
- **Trailing**: None, Close/Remove icon (input chips)

## Usage
- Filter chips: toggle-able category filters in search/browse
- Input chips: selected values in multi-select fields (with remove button)
- Suggestion chips: quick-reply options in chat

## Anatomy
- Container (pill shape)
- Optional leading icon/avatar (16px)
- Label text (System S/M, Label Medium)
- Optional trailing close icon (16px, input type only)

## Tokens
- Default background: `grey/surface/fg-minimal` at low opacity
- Default border: `grey/on-default/medium-s`
- Selected background: `[appearance] high`
- Selected text: `[appearance] on bold medium [t]`
- Default text: `grey/on-default/medium-t`
- Border radius: pill (999px)
- Height M: 32px, Height S: 24px
- Padding: scale 2 (8px) horizontal, scale 1 (4px) vertical

## Rules
- Max chip label: 2 lines, then truncate with ellipsis
- Remove button (input chips): always 16×16px, never smaller
- Chips in a group: wrap to next line or horizontal scroll
- Never use chip as primary action — use Button instead
