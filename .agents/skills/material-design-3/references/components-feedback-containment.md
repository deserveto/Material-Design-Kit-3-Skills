# Material 3 feedback and containment components

Use this guide for cards, lists, surfaces, dialogs, sheets, menus, Snackbar, badges, progress, tooltips, and carousels.

## Containment

### Card

Use a card for a grouped content/action unit that benefits from its own container semantics. Do not wrap every section in a card merely to make the page look Material.

### List/list item

Prefer lists for repeated structured content where alignment and scanning matter. Avoid replacing a straightforward list with a grid of decorative cards without a content reason.

### Surface and divider

Use surface roles for structural hierarchy and state. Use dividers sparingly when spacing, alignment, or surface separation already communicates grouping.

### Carousel

Use for horizontally browsable collections where browsing that dimension makes sense. It is not a generic replacement for every grid.

## Temporary surfaces

| Need | Typical family |
|---|---|
| Focused blocking decision/input | Dialog |
| Contextual supplementary actions/content | Bottom sheet or side sheet where platform/product supports it |
| Compact contextual choices | Menu |
| Supporting label/help | Tooltip |

Dialogs should not become routine navigation containers.

## Feedback

### Snackbar

Use Snackbar for brief non-blocking feedback, optionally with one directly related action. Do not place long workflows, multiple decisions, or critical consent inside a snackbar.

### Badge

Use for concise count/status attached to another destination/control. The status must remain available semantically when important.

### Progress

Use determinate progress only when meaningful progress is measurable. Use indeterminate treatment when it is not. Long operations need failure/recovery/timeout thinking rather than an eternal spinner.

## Loading, empty, error

Containment should not collapse when data changes state. Design loading, empty, partial, and error states as part of the component/screen contract; preserve useful context and recovery actions.
