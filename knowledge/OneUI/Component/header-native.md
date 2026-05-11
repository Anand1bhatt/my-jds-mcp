# HeaderNative — OneUI Micropattern

## Figma Source
File: OneUI Micropatterns (`y4r5eCoZhqvPw1U1bm2qfw`) — Page: HeaderNative (node `1:46627`)

## Overview
The native mobile app header/navigation bar. Used for all React Native and native mobile screens.

## Variants
- **secondaryNav**: true / false
- **Type**: Default, Search active, Back navigation
- **Theme**: follows `09 Theme` collection mode (MyJio, JioHome, etc.)

## Anatomy
- Left zone: Back/Menu icon OR app logo
- Center: Page title (Title M, Title High weight) OR search bar
- Right zone: Action icons (max 3)
- Optional: Secondary nav bar below (tab strip or breadcrumb)

## Tokens
- Background: `[Theme] surface`
- Title text: `grey/on-default/medium-t`, Title M
- Icon color: `grey/on-default/medium-t`
- Height: 56px (standard), 96px (with secondary nav)
- Border bottom: `grey/on-default/low-s` (1px, optional)

## Usage Rules
- Page title: max 1 line, truncate with ellipsis
- Action icons: max 3 in right zone, 24×24px each, 8px gap
- Back button: always leftmost, 44×44px touch target
- Search: replace title with InputField when search is active

## Secondary Nav
When `secondaryNav=true`, renders a horizontal tab strip or contextual sub-navigation below the main header bar.
