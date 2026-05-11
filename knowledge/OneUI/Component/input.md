# Input — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Pages: Input (node `4298:3803`), InputText (`4298:7166`), InputField (`4298:7167`), InputHelper (`3450:1387`)

## Component Hierarchy
- **Input**: top-level container — wraps Label + InputField + InputHelper
- **InputField**: the actual text input box
- **InputText**: text content inside InputField
- **InputHelper**: below-field help/error/character count text

## Variants (InputField)
- **State**: Default, Focused, Filled, Error, Disabled, Read-only
- **Size**: L (56px height), M (48px height), S (40px height)
- **Leading**: None, Icon, Text prefix
- **Trailing**: None, Icon, Clear button, Password toggle, Character count

## Anatomy
1. Label (System S, Label Medium) — above field
2. InputField container
   - Leading element (optional)
   - InputText (placeholder/value)
   - Trailing element (optional)
3. InputHelper row (optional)
   - Helper/error text (left)
   - Character count (right)

## Tokens
- Background: `02 Surface` default
- Border Default: `grey/on-default/medium-s`
- Border Focused: `indigo/surface/fg-minimal` (Indigo accent)
- Border Error: Negative semantic color
- Text (value): `grey/on-default/medium-t`
- Text (placeholder): `grey/on-default/low-t`
- Label text: `grey/on-default/medium-t`, System S
- Helper text: `grey/on-default/low-t`, System XS
- Error text: Negative semantic color, System XS
- Border radius: scale 2 (8px)
- Padding: scale 3 (12px) horizontal, scale 2-5 (10px) vertical

## Rules
- Always pair InputField with a visible Label — never placeholder-only
- Error state MUST show InputHelper with error message
- Disabled state: use `04.1 Disabled` opacity token
- Character count shown in trailing position when maxLength is set
