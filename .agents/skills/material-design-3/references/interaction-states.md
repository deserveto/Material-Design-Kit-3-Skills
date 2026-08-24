# Material 3 interaction states

Use this reference when implementing or reviewing hover, focus, pressed, selected, checked, disabled, dragged, loading, or error behavior. A component is not complete merely because its resting appearance matches Material.

## 1. Semantic state first

Represent the real interaction state in the platform's semantic/accessibility model before styling it.

Examples:

- a toggle exposes checked/pressed state;
- a selected navigation destination exposes selection semantically;
- a disabled action is actually non-activatable when appropriate, not merely gray;
- a loading control communicates busy/progress state where users need it;
- invalid input exposes error text/semantics in addition to color.

Visual state is a consequence of interaction meaning, not a substitute for it.

## 2. State contract

For every interactive component, consider the states that actually apply:

| State | Contract |
|---|---|
| Enabled/resting | Clear affordance and readable label/content. |
| Hover | Pointer-only enhancement; never the only way to reveal essential information. |
| Focus | Keyboard/assistive navigation can locate the control with a visible indicator. |
| Pressed | Immediate acknowledgement of direct manipulation without delaying the action. |
| Selected/checked | Exposed semantically and perceivable without color alone. |
| Disabled | Clearly unavailable where disabling is justified; preserve enough contrast/readability for context. |
| Dragged | Spatial state remains understandable and reachable; drop targets are discoverable. |
| Loading | Prevent accidental duplicate activation when necessary and keep progress/recovery understandable. |
| Error | Explain the problem and recovery path; do not rely on red alone. |

Do not invent states that the interaction model does not have.

## 3. Focus is non-negotiable

Never remove a browser/platform focus indicator without providing an equal or better replacement.

- Prefer `:focus-visible` on web when distinguishing keyboard focus from pointer interaction improves usability.
- Ensure the indicator is not clipped by `overflow`, rounded containers, or transforms.
- Keep sufficient separation from backgrounds and adjacent controls in supported themes.
- Focus order should follow task and reading order; do not patch a bad DOM/semantic order with arbitrary positive tab indexes.

A tooltip is not a focus indicator and an icon is not an accessible name.

## 4. State layers, ripple, and indication

Use the established Material/platform indication system or project primitive when available rather than recreating per-component opacity rules.

- Keep state feedback consistent across the component family.
- Do not apply one universal hover/pressed alpha to every surface without checking the theme/component model.
- Ripple/press indication should reinforce the target actually activated.
- Expressive shape or size changes may augment state on supported platforms, but must not move targets unpredictably or obscure focus.

## 5. Loading and async actions

For async actions:

- decide whether repeated activation is safe;
- preserve button/control width where practical to avoid layout jumping;
- use determinate progress only when progress is truly measurable;
- provide timeout, retry, cancel, or error recovery when operations can hang or fail;
- do not leave a control permanently disabled after a recoverable error.

A spinner replacing all context is usually weaker than keeping the action/status relationship visible.

## 6. Reduced motion

When motion communicates a state transition, preserve the state meaning when reduced motion is requested.

- remove or shorten non-essential travel/morphing;
- keep static shape, text, icon, position, or color cues as appropriate;
- do not require an animation to finish before a routine action becomes usable.

## 7. Platform notes

### Web

Prefer native elements and accessible component primitives. Verify mouse, keyboard, touch/pointer, and `:focus-visible`. Do not use `outline: none`/`outline: 0` unless a tested replacement focus treatment is present.

### Jetpack Compose

Prefer Material3 components and the project's `InteractionSource`/indication patterns. Inspect the pinned Material3 version before adopting newer ripple, focus-ring, or Expressive state APIs.

### Flutter

Use Material widgets/theme states and the project's `MaterialState`/`WidgetState` patterns supported by its Flutter version. Test keyboard focus on desktop/web targets as well as touch.

### Wear OS

Account for rotary focus, swipe gestures, round screens, haptics, ambient mode, and Wear-specific morphing components. Do not copy mobile focus/navigation behavior directly.

## 8. Verification checklist

For each applicable control, verify:

1. accessible name/role/state;
2. keyboard and pointer activation;
3. visible focus;
4. hover/pressed feedback;
5. selected/checked cue beyond color;
6. disabled behavior;
7. loading/error recovery;
8. reduced-motion fallback;
9. supported light/dark/high-contrast themes;
10. no clipping or target movement at large text/localized labels.
