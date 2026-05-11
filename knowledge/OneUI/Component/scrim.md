# Scrim — OneUI Component

## Figma Source
File: OneUI Components (`eYJriZveeBwZDzGlCts22f`) — Page: Scrim (node `4078:17919`)

## Overview
Semi-transparent overlay that dims background content when a modal, bottom sheet, or drawer is open.

## Variants
- **Opacity**: Low, Medium, High
- **Color**: Dark (default), Light (for dark backgrounds)

## Tokens
- Dark scrim: `#000000` at opacity 0.38 (Low), 0.54 (Medium), 0.72 (High)
- Light scrim: `#ffffff` at opacity 0.38–0.72
- Use `12 Material` collection: `[Material] medium [t]` and `[Material] low [t]`

## Usage
- Always shown behind: Modals, Bottom Sheets, Drawers, Context Menus
- Tap on scrim = dismiss the overlaid component

## Rules
- z-index: always between page content and the overlay component
- Animate: fade in 200ms ease, fade out 150ms ease
- On mobile: scrim covers full screen (100vw × 100vh)
- On desktop: scrim covers full viewport or just the content area (not side nav)
- Always trap focus within the overlay when scrim is visible
