# Spinner (CircularProgressIndicator) — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Pages: CircularProgressIndicator (node `2314:1039`), Spinner (node `2314:1241`)

## CircularProgressIndicator
### Variants
- **Type**: Determinate (progress %), Indeterminate (continuous)
- **Size**: S (16px), M (24px), L (40px), XL (56px)
- **Appearance**: follows `[appearance]` roles

### Tokens
- Track color: `grey/on-default/low-s`
- Progress color: `[appearance] high`
- Stroke width: 2px (S/M), 3px (L/XL)

## Spinner (indeterminate only)
### Variants
- **Size**: S (16px), M (24px), L (40px)
- **Color**: Inherited from context or explicit appearance

### Usage
- Inline loading states (button loading, inline content)
- Page/section loading overlay
- Pull-to-refresh indicator

### Tokens
- Spinner color: `[appearance] high` or `grey/on-default/medium-t`
- Animation: 360° rotation, 800ms linear, infinite

## Rules
- Determinate: show % only when actual progress is known
- Indeterminate: no % label
- Always pair with accessible loading announcement (aria-live)
- Spinner inside a Button: replaces label, keeps button size fixed
