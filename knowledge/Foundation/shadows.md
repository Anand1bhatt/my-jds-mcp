# Shadows

Shadows are used to illustrate the dimensional space between surfaces created by elevation. Shadows provide important visual cues about hierarchy by adding depth and highlighting actionable content.

## Shadow Types

Shadows come in three sizes which reflect their dimensional elevation. Surfaces at higher elevations have larger shadows, while surfaces at lower elevations have smaller shadows. These can be used to reflect component or surface states and provide visual feedback.

### Small Shadow (S)
Small shadows are used for default, static elements such as cards.

**Token:** `--shadow-s`  
**Value:** `0px 4px 16px rgba(0, 0, 0, 0.08)`  
**Usage:** Default state for cards, tooltips, and elevated surfaces

### Medium Shadow (M)
Medium shadows add additional information when an element is in a hover state.

**Token:** `--shadow-m`  
**Value:** `0px 4px 16px rgba(0, 0, 0, 0.16)`  
**Usage:** Hover state for interactive cards and buttons

### Large Shadow (L)
Large shadows are used for elements that are in a pressed/active state.

**Token:** `--shadow-l`  
**Value:** `0px 4px 16px rgba(0, 0, 0, 0.24)`  
**Usage:** Active/pressed state, modals, drawers, and high-priority overlays

## Shadow Creation

Shadows can be created using three simple steps: Direction, Blur, and Opacity.

### Direction
The direction of the shadow should always be on the Y axis, pointing down.

- **Formula:** Y = 4px (consistent across all shadow sizes)

### Blur
The blur affects the softness of the shadow, creating a natural diffusion.

- **Formula:** Blur = 16px (consistent across all shadow sizes)

### Opacity
Opacity controls the intensity of the shadow. It should always feel natural and never too stark.

- **Small Shadow:** #000000 at 8%
- **Medium Shadow:** #000000 at 16%
- **Large Shadow:** #000000 at 24%

## Shadow Token Reference

| Token | Y-Offset | Blur | Color | Opacity | Full Value |
|-------|----------|------|-------|---------|------------|
| `--shadow-s` | 4px | 16px | #000000 | 8% | `0px 4px 16px rgba(0, 0, 0, 0.08)` |
| `--shadow-m` | 4px | 16px | #000000 | 16% | `0px 4px 16px rgba(0, 0, 0, 0.16)` |
| `--shadow-l` | 4px | 16px | #000000 | 24% | `0px 4px 16px rgba(0, 0, 0, 0.24)` |

## Application

Shadows can be applied to various UI components to create depth and visual hierarchy.

### Cards
Cards serve as entry points to more detailed information and contain contextual content in text and image form.

- **Default State:** Use `--shadow-s`
- **Hover State:** Use `--shadow-m`
- **Active/Focused State:** Use `--shadow-l`

### Tooltips
Tooltips are short and informative prompts that appear in a small overlay when a customer hovers over an element.

- **Default:** Use `--shadow-m` for clear visibility

### Drawers
Drawers are scrollable layers of content that provide contextual information about the page being viewed.

- **Default:** Use `--shadow-l` to emphasize elevation

### Modals & Dialogs
Modal overlays that require user attention.

- **Default:** Use `--shadow-l` to create clear separation from background

### Dropdown Menus
Menu overlays that appear on interaction.

- **Default:** Use `--shadow-m` for subtle elevation

## Design Principles

- Shadows should enhance usability by providing visual feedback on interactive states
- Use shadows consistently to maintain a coherent elevation system
- Higher opacity shadows indicate higher elevation and greater importance
- Avoid using shadows on flat design elements or when elevation is not needed
- All shadow values maintain consistent Y-offset (4px) and blur (16px) for visual harmony
