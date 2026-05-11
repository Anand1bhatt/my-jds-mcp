# Avatar — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Avatar (node `220:17469`)

## Variants
- **Type**: Image, Initials, Icon, Brand
- **Size**: 2XS (16px), XS (24px), S (32px), M (40px), L (48px), XL (64px), 2XL (80px), 3XL (96px)
- **Shape**: Circle (default), Rounded Square
- **Status indicator**: Online, Away, Busy, Offline (optional badge overlay)

## Usage
- User identity in headers, list items, comments, profiles
- Brand avatar for app/product representation
- Group avatars (stack with −8px overlap)

## Anatomy
- Container (circle or rounded square)
- Image fill OR initials text OR icon
- Optional status ring (2px border, status color)
- Optional notification badge (top-right)

## Tokens
- Background (initials/icon): `grey/surface/fg-minimal`
- Text/icon color: `grey/on-bold/medium-t`
- Status Online: Positive semantic color
- Status Away: Warning semantic color
- Status Busy: Negative semantic color
- Border (status ring): surface background color (creates separation)

## Rules
- Always provide alt text or aria-label for accessibility
- Initials: max 2 characters, Label High weight
- Image avatars: use object-fit cover, aspect-ratio 1:1
