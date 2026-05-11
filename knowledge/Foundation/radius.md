# Radius

Radius tokens define the border-radius values used throughout the JDS design system. They create visual consistency and help establish the brand's design language.

## Radius Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-s` | 4px | Small radius for subtle rounding on compact elements |
| `--radius-m` | 8px | Medium radius for standard UI components |
| `--radius-l` | 16px | Large radius for prominent elements and cards |
| `--radius-xl` | 24px | Extra-large radius for bold, distinctive elements |
| `--radius-xxl` | 32px | Double extra-large radius for hero elements |
| `--radius-pill` | 250px | Pill-shaped radius for buttons and badges |

## Visual Reference

### Small (4px)
Used for subtle rounding on compact elements like tags, small buttons, and input fields.

### Medium (8px)
The default radius for most UI components, providing a balanced modern look.

### Large (16px)
Applied to cards, modals, and larger containers to create visual prominence.

### XL (24px)
Used for hero cards and featured content sections.

### XXL (32px)
Applied to large feature blocks and promotional content.

### Pill (250px)
Creates fully rounded ends on buttons, tags, and navigation items.

## Application

- **Buttons**: Use `--radius-pill` for primary actions,
- **Cards**: Use `--radius-l` for standard cards, `--radius-xl` for featured cards
- **Input Fields**: Use `--radius-s` or `--radius-m` for consistent form styling
- **Modals & Dialogs**: Use `--radius-l` or `--radius-xl` for larger overlays
- **Tags & Badges**: Use `--radius-pill` or `--radius-s` for compact labels

## Design Principles

All radius values follow the 4px base unit grid system, ensuring visual harmony across the interface. Choose radius values that match the component's visual weight and importance in the hierarchy.
