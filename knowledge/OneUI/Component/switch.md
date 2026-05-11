# Switch — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Switch (node `556:7958`)

## Variants
- **State**: Off, On, Disabled Off, Disabled On
- **Size**: S, M

## Usage
- Toggle binary settings (on/off)
- Immediate effect settings (no submit required)
- Prefer over checkbox when action takes effect immediately

## Anatomy
- Track (rounded pill container)
- Thumb (circle, slides left/right)

## Tokens
- Track Off: `grey/on-default/medium-s`
- Track On: `[appearance] high` (Indigo)
- Thumb: `#ffffff` (always white)
- Disabled: `04.1 Disabled` opacity
- Track size M: 51×31px
- Track size S: 40×24px
- Thumb size M: 27px diameter
- Thumb size S: 20px diameter
- Thumb offset: 2px from edge

## Rules
- Always animate thumb slide on state change (150ms ease)
- Include visible label describing what the switch controls
- Disabled state must convey current value (not just grey)
- Touch target: full switch width + 8px padding each side
