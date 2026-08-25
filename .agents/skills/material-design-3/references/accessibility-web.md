# Web accessibility for Material 3

Use this reference with `adaptive-accessibility.md` for web implementations. Material styling does not replace WCAG 2.2 or ARIA interaction requirements.

## Native semantics first

Prefer native HTML elements when they already express the interaction: `<button>` for actions, `<a>` for navigation, and native form elements where suitable.

When using custom primitives, follow the appropriate WAI-ARIA Authoring Practices interaction pattern and implement keyboard/state semantics completely.

## WCAG-oriented checks

For applicable UI, verify:

- text can resize/reflow without loss of content or function;
- browser/pinch zoom is not disabled;
- focus is visible and not obscured by sticky/fixed UI;
- pointer targets and spacing are usable;
- dragging interactions have a non-drag alternative when required;
- status/error meaning is not color-only;
- non-text UI boundaries/focus indicators have sufficient contrast;
- dialogs, menus, tabs, comboboxes, sliders, and disclosure controls follow their keyboard model.

A CSS `px` font size by itself is not proof of an accessibility failure. The real test is whether user scaling/zoom/reflow works and whether the project bypasses its semantic type system.

## Material-specific web checks

Icon-only controls need an accessible name independent from Material Symbols; selected/toggled state needs semantic state plus a non-color cue; focus treatment must remain visible over Material state layers; temporary surfaces must manage focus entry/return; adaptive navigation changes must preserve route/selection semantics; reduced motion must keep state changes understandable.

## Verification tools

Combine semantic/component tests, keyboard walkthrough, browser zoom/text scaling, an accessibility engine such as axe, rendered viewport inspection, and screen-reader testing for critical flows when available.

The bundled `audit_m3.py` is static and heuristic. The optional `audit_runtime.mjs` can collect rendered axe findings, console errors, overflow, and a basic focus probe. Neither is certification.
