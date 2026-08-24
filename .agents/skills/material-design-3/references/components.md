# Material 3 component selection

Choose a component because its interaction model matches the user's task. Visual similarity is secondary.

## Action hierarchy

| Need | Typical choice | Notes |
|---|---|---|
| Highest-priority action in a local context | Filled button | Avoid multiple competing highest-priority actions. |
| Strong but lower-prominence action | Filled tonal or elevated button | Choose based on surrounding hierarchy and platform implementation. |
| Medium-priority action needing boundary | Outlined button | Useful beside a stronger action. |
| Low-prominence action | Text button | Do not use when the action must be visually discoverable as primary. |
| Compact icon action | Icon button | Requires accessible name and adequate target. |
| Primary floating screen action | FAB / extended FAB | Only when a floating primary action model makes sense. Not a generic decorative button. |
| Primary action plus closely related menu | Split button where supported | Keep the primary action predictable. |

Destructive actions need clear language and risk-appropriate emphasis. Destructive does not automatically mean “make it the primary filled action.”

## Selection and filtering

| User intent | Component family |
|---|---|
| Binary setting | Switch or checkbox depending on immediate/stateful context |
| Choose one from a small visible set | Radio buttons or single-choice segmented buttons |
| Choose several independent items | Checkboxes or multi-choice segmented buttons where suitable |
| Apply/remove compact filters | Filter chips |
| Enter a user-created compact value/entity | Input chip where supported |
| Trigger a contextual suggestion/action | Suggestion or assist chip |

Do not use chips as small buttons for every secondary action.

## Input

Use filled or outlined text fields according to the product's established field style and hierarchy. Preserve label, helper/error text, required semantics, keyboard behavior, autofill, and accessible naming. Error styling needs text/semantics in addition to color.

Date/time pickers should match the platform's Material implementation when available. Do not recreate a picker from generic fields unless product constraints require it.

## Navigation

| Structure | Typical component |
|---|---|
| Few top-level destinations in compact layout | Navigation bar |
| Top-level destinations with more horizontal room | Navigation rail |
| Larger persistent app hierarchy | Navigation drawer |
| Peer sections inside a screen | Tabs |
| Navigation/action container near content | App bar / toolbar as appropriate |

Navigation may change form at wider window classes. Do not simply stretch a compact bottom bar across an expanded canvas.

Selected navigation state must be perceivable without color alone.

## Surfaces and content organization

- **Card**: a grouped content/action unit that benefits from its own container semantics. Do not card-wrap every section.
- **List/list item**: repeated structured content where alignment and scanning matter.
- **Divider**: use sparingly when spacing/surface grouping is insufficient.
- **Surface**: structural container for theme, elevation, shape, or interaction semantics.
- **Carousel**: horizontally browsable collection where the content model justifies it; not a substitute for any grid.

## Temporary surfaces and feedback

- **Dialog**: interrupts for a focused decision or critical input. Avoid for routine navigation.
- **Bottom sheet**: contextual or supplementary content/actions that benefit from a temporary surface.
- **Menu**: compact set of contextual choices.
- **Tooltip**: supporting label/help for controls; not a replacement for accessible names.
- **Snackbar**: brief, non-blocking feedback, optionally with one related action.
- **Badge**: concise status/count attached to another element.

## Progress and loading

Use determinate progress when meaningful progress can be measured; indeterminate when it cannot. M3 Expressive implementations may provide wavy progress or morphing loading indicators, but availability/stability is platform-specific.

Avoid indefinite loading with no timeout, recovery, or status when an operation may fail or hang.

## Component decision questions

Before introducing a component, answer:

1. What exact user intent does it represent?
2. Is this navigation, action, selection, input, feedback, or content grouping?
3. What prominence should it have relative to neighboring controls?
4. What states can it enter?
5. Is there already a shared component/variant for this role?
6. Does the chosen component remain appropriate at other window sizes/input modes?
