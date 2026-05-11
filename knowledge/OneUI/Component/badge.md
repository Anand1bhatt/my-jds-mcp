# Badge — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Badge (node `220:17472`)

## Variants
- **Type**: Dot, Count, Label
- **Appearance**: Neutral, Primary (Indigo), Positive, Negative, Warning, Informative
- **Size**: S, M

## Usage
- Notification counts on icons/avatars
- Status indicators on list items
- Label badges on cards/tags

## Anatomy
- Dot: 8px circle, no content
- Count: pill shape, numeric label (System 3XS, Label High)
- Label: pill shape, short text string

## Tokens
- Background: `[appearance] high` per appearance role
- Text: `[appearance] on bold medium [t]`
- Min width: 16px (count/label), 8px (dot)
- Height: 16px (S), 20px (M)
- Border radius: pill (999px)
- Padding: 0 scale-1 (0 4px) for count/label

## Rules
- Count badges: show `99+` when value > 99
- Dot badges: no text, used for unread/new state only
- Always position relative to parent (top-right corner by default)
