# Adaptive layout and accessibility

Material 3 quality depends on behavior across available space, input modes, and accessibility needs. Treat these as design constraints, not cleanup tasks.

## Window size classes

Current Android guidance (reviewed 2026-08-24) classifies available **width** independently of device type:

| Width class | Available width |
|---|---:|
| Compact | `< 600dp` |
| Medium | `600dp–839dp` |
| Expanded | `840dp–1199dp` |
| Large | `1200dp–1599dp` |
| Extra large | `>= 1600dp` |

Height has its own classes. A wide but short window may not have room for the same multi-pane layout as a wide/tall one.

Do not implement `isTablet` as the primary adaptive model. Window size can change at runtime because of split-screen, desktop resizing, rotation, or folding/unfolding.

For web, translate the same principle to actual CSS/container/window space instead of copying `dp` breakpoints blindly if the project's layout system uses different breakpoints.

## Canonical adaptive patterns

- **List-detail**: collection + selected item. Compact may show one pane at a time; expanded can show both.
- **Supporting pane**: primary task + related contextual/supporting content.
- **Feed**: stream/grid that changes density and column strategy as space grows.

Use extra space to improve information architecture, not merely to increase margins.

## Navigation adaptation

A compact bottom navigation bar may become a rail or drawer on wider layouts. Choose based on destination count, task flow, and available space. Preserve destination identity and selection semantics across forms.

## Interactive targets

Material guidance commonly uses a minimum **48dp × 48dp** interactive region. The visible glyph can be smaller, such as a 24dp icon, while the hit/focus target remains large enough.

On web, also respect platform accessibility guidance and pointer/keyboard realities; do not mechanically equate CSS pixels with Android dp in every context.

## Required interaction checks

For applicable controls, verify:

- semantic element/role;
- accessible name and description when needed;
- logical keyboard focus order;
- visible focus indication;
- keyboard activation behavior;
- adequate pointer/touch target and spacing;
- hover/focus/pressed/selected/disabled/error states;
- state changes announced or exposed semantically;
- no meaning conveyed by color alone;
- text zoom/font scaling without clipping or loss of function;
- reflow at narrow widths;
- localized/longer text does not break controls;
- reduced-motion preference respected;
- contrast remains sufficient in supported themes and states.

## Icon-only controls

An icon's visual identity is not an accessible name. Provide an explicit label via the platform's semantic/accessibility API. Tooltips can supplement discoverability but are not the sole accessible name.

Use filled/unfilled Material Symbol states only as one cue among semantic selected/toggled state and other visual cues.

## Motion accessibility

When `prefers-reduced-motion`, platform accessibility settings, or equivalent signals exist, reduce or remove non-essential movement. Keep state changes understandable without relying on animated travel or morphing.

## Verification widths

For a feature with adaptive behavior, render at minimum:

1. a compact/narrow case;
2. the layout transition region relevant to the app;
3. an expanded/wide case.

Also test any known short-height case where two-pane or modal behavior could fail.
