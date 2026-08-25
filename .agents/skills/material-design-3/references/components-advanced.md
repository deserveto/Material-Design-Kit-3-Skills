# Advanced Material 3 component contracts

Use this reference for components whose interaction model is easy to oversimplify or whose platform availability varies.

## Search

Search can be an action, persistent field, or dedicated search surface. Decide whether search is primary enough to stay visible, whether it searches immediately or after submission, how suggestions/history/results differ, how loading/empty/error states work, and how keyboard focus moves between query, suggestions, and results.

Do not copy a platform-specific `SearchBar` API into another stack. Consult `assets/platform-capabilities.json` and the target dependency.

## Menus and selection

Menus are for contextual choices, not arbitrary containers. Keep keyboard navigation, focus return, disabled items, checked/selected semantics, submenu behavior, and localization complete. Use radio/checkbox/segmented/chip families when persistent visible selection is more appropriate.

## Pickers

Prefer the platform's maintained Material date/time picker. Verify locale, 12/24-hour behavior, keyboard entry, validation, range constraints, screen-reader labels, and dialog/sheet focus management.

## Sliders

Sliders require meaningful min/max/step, current value semantics, keyboard adjustment, accessible value text when numeric value is insufficient, adequate target geometry, and correct range-slider thumb behavior. Do not use a slider when exact typed input is the primary task.

## Tooltips

Tooltips supplement discoverability; they are not the sole accessible name. They should not contain multi-step workflows or critical information unavailable elsewhere.

## Progress and loading

Choose determinate progress only when progress is meaningful. For long async work, define timeout/stall/retry/error behavior. Expressive progress treatments are platform/version specific.

## Newer APIs

Before using newer component families:

1. read `assets/platform-capabilities.json`;
2. inspect the target project's pinned dependency;
3. check the relevant platform reference;
4. explicitly disclose alpha/experimental/maintenance status when it changes engineering risk.

The capability matrix is a reviewed decision aid, not an exhaustive API catalog.
