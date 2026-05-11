# Pagination & PaginationDots — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Pages: Pagination (node `7710:13075`), PaginationDots (node `4266:5954`)

## Pagination (numbered)
### Variants
- **Style**: Numbered pages, Previous/Next only
- **Size**: S, M
- **State**: Page items — Default, Active, Disabled

### Anatomy
- Previous button (chevron left)
- Page number items (up to 7 visible, with ellipsis for overflow)
- Next button (chevron right)

### Tokens
- Active page: `[appearance] high` background, `on bold` text
- Default page: transparent, `grey/on-default/medium-t`
- Disabled: `04.1 Disabled` opacity
- Item size M: 40×40px, Item size S: 32×32px
- Border radius: scale 2 (8px)
- Gap between items: scale 1 (4px)

## PaginationDots (carousel indicator)
### Variants
- **Active dot size**: S (6px), M (8px), L (10px)
- **Style**: Dots only, Dots with progress bar

### Anatomy
- Row of dots (inactive: small, active: larger or elongated)
- Optional progress bar variant

### Tokens
- Active dot: `[appearance] high`
- Inactive dot: `grey/on-default/medium-s`
- Active dot width: 16–24px (elongated pill), height: 6–8px
- Inactive dot: 6–8px circle
- Gap: scale 1 (4px)

## Rules
- Pagination: show ellipsis when total pages > 7
- PaginationDots: max 10 dots before switching to `X/Y` text counter
- Always indicate current position clearly
