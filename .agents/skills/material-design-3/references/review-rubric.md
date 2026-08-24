# Material 3 review rubric

Use this reference for audits and code/UI reviews so findings are evidence-based and consistently prioritized. Do not reduce Material review to subjective comments such as "doesn't look Material enough."

## Severity

### BLOCKER

A release-stopping issue in the reviewed scope, such as:

- inaccessible or unusable primary interaction;
- invalid platform/API usage that does not compile or requires an unapproved dependency channel;
- destructive/critical action semantics that can cause serious user harm or data loss;
- navigation/layout failure that makes a supported viewport or input mode unusable.

### HIGH

A major Material/system problem that significantly harms usability, accessibility, hierarchy, or maintainability:

- missing keyboard focus on core workflows;
- wrong component model for the task;
- compact-only navigation stretched into an unusable wide layout;
- parallel hard-coded theme values that undermine supported themes;
- silent alpha/experimental adoption;
- migration that is only cosmetic while retaining conflicting legacy behavior.

### MEDIUM

A meaningful inconsistency that should be fixed but does not block the primary flow:

- one-off radii/type/color values where shared semantic tokens already exist;
- inconsistent state treatment;
- excessive card containment or elevation;
- weak hierarchy between primary and secondary actions;
- layout spacing that breaks consistency but remains usable.

### LOW

Polish, cleanup, or future hardening with limited user impact:

- minor token naming/organization inconsistency;
- non-critical spacing refinement;
- optional reduction of decorative Expressive effects;
- documentation/test coverage improvements around already-correct behavior.

Severity is based on impact, not how visually noticeable the issue is.

## Review order

Review in this order so cosmetic observations do not hide functional failures:

1. **Platform/dependency correctness**
2. **Semantics and accessibility**
3. **Task/action hierarchy**
4. **Component choice and interaction states**
5. **Navigation and adaptive layout**
6. **Theme/tokens: color, type, shape, motion, elevation, icons**
7. **Expressive restraint**
8. **Rendered verification and test evidence**

## Finding format

Each finding should contain:

```text
Severity: HIGH
Area: Interaction states / accessibility
Evidence: Save icon button has no accessible name and removes the browser focus outline.
Impact: Keyboard and screen-reader users cannot reliably identify or locate the primary save action.
Recommendation: Use the shared icon-button primitive, provide an accessible label, and preserve/reimplement a visible focus-visible treatment.
Verification: Tab through the form and inspect the accessibility tree in supported themes.
```

Prefer concrete file/component/state evidence. When reviewing a screenshot only, say which implementation facts cannot be proven from the image.

## Category checklist

### Theme and tokens

- semantic roles instead of repeated raw values;
- correct `on*`/container relationships;
- coherent typography and shape system;
- surface/elevation hierarchy without shadow dependence;
- supported theme modes remain coherent.

### Components and hierarchy

- component matches navigation/action/selection/input/feedback semantics;
- only genuinely highest-priority actions receive highest prominence;
- destructive actions communicate risk without becoming primary by accident;
- chips/FABs/cards are not generic styling substitutes.

### Interaction states

- focus, pressed, selected/checked, disabled, loading, and error states where applicable;
- selected/error meaning is not color-only;
- async actions recover from failures;
- reduced-motion fallback preserves state meaning.

### Layout and adaptive behavior

- available-space logic instead of device labels;
- compact/transition/expanded layouts remain usable;
- wide layouts improve structure instead of stretching phone UI;
- insets/safe areas and readable content widths are intentional.

### Accessibility

- names/roles/states;
- logical keyboard/rotary focus order;
- visible focus;
- adequate target size/spacing;
- text scaling/reflow/localization;
- contrast and high-contrast behavior where supported.

### Expressive

- color/shape/size/motion/containment solves a hierarchy problem;
- familiar controls remain recognizable;
- utility workflows remain efficient;
- experimental APIs are knowingly accepted.

## Release gate

Do not assign a fake universal numeric "Material score." Report findings by severity and evidence.

A strong release gate for the reviewed scope is:

- zero unresolved **BLOCKER** findings;
- **HIGH** findings fixed or explicitly accepted with rationale;
- project tests/build and relevant rendered verification completed;
- known **MEDIUM/LOW** findings recorded rather than silently omitted.
