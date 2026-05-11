# Checkbox — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Checkbox (node `552:6539`)

## Variants
- **State**: Unchecked, Checked, Indeterminate, Disabled
- **Size**: S (16px), M (20px)
- **Label position**: Right (default), None

## Usage
- Multi-select lists
- Form agreements / terms
- Filter panels
- Table row selection (indeterminate for partial select)

## Anatomy
- Checkbox control (square with rounded corners)
- Checkmark / dash icon (checked/indeterminate)
- Label text (optional, right-aligned)

## Tokens
- Unchecked border: `grey/on-default/medium-s`
- Unchecked background: transparent
- Checked background: `[appearance] high` (Indigo by default)
- Checked icon color: `[appearance] on bold medium [t]` (#ffffff)
- Indeterminate: same as checked with dash icon
- Disabled: `04.1 Disabled` opacity
- Border radius: scale 0-5 (2px)
- Touch target: min 44×44px

## Rules
- Always use indeterminate state for "select all" when partial selection exists
- Disabled checkboxes must still show current state visually
- Label click area must trigger checkbox toggle
