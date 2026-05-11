# Button — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Buttons (node `207:5633`)

## Variants
- **Type**: Filled, Outlined, Ghost, Danger
- **Size**: Large, Medium, Small
- **State**: Default, Hover, Pressed, Disabled, Loading

## Usage
- Filled: primary actions (CTA, submit)
- Outlined: secondary actions
- Ghost: tertiary/low-emphasis actions
- Danger: destructive actions (delete, remove)

## Anatomy
- Container (touch target min 44px height)
- Label text — System M, Label High weight (700)
- Optional leading/trailing icon (24px)
- Optional loading spinner

## Tokens
- Background (Filled): `[appearance] high`
- Text (Filled): `[appearance] on bold medium [t]`
- Background (Outlined): transparent
- Border (Outlined): `[appearance] medium [s]`
- Text (Outlined): `[appearance] medium [t]`
- Disabled opacity: `04.1 Disabled` collection
- Padding: scale 3 (12px) vertical, scale 5 (20px) horizontal
- Border radius: scale 2 (8px)

## SelectableButtons
Toggleable button group — used for filter chips, segmented selections.
- Selected state uses Filled appearance
- Unselected uses Ghost/Outlined
- Group wraps in horizontal scroll container on mobile
