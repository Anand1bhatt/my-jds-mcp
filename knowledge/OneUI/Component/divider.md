# Divider — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Divider (node `2896:17172`)

## Variants
- **Orientation**: Horizontal, Vertical
- **Style**: Full-bleed, Inset (left offset), Middle-inset
- **Weight**: Thin (1px), Thick (2px)
- **Content**: None, Label (with text), Icon

## Usage
- Section separation within a list or card
- Visual grouping between content areas
- Never use as a border substitute on interactive elements

## Tokens
- Color: `grey/on-default/low-s`
- Thickness: 1px (default), 2px (thick)
- Inset left offset: matches ListItem leading zone (56–72px)
- Label text: System XS, Label Medium, `grey/on-default/low-t`
- Label background: surface color (to break the line)

## Rules
- Inset dividers: align with text content start, not edge of screen
- Vertical dividers: used only within horizontal layouts (e.g., inline between actions)
- Avoid stacking multiple dividers — use spacing instead
