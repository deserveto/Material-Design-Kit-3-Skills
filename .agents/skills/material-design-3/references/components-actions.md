# Material 3 action components

Use this guide when choosing buttons, icon buttons, FABs, split buttons, or action prominence. Choose the action model from task hierarchy first; appearance is secondary.

## Prominence ladder

| Intent | Typical family | Guardrail |
|---|---|---|
| Highest-priority local action | Filled button | Usually one strongest action per local decision area. |
| Strong secondary action | Filled tonal or elevated button | Must remain visibly subordinate to the primary action. |
| Medium-priority bounded action | Outlined button | Useful beside a stronger action or where boundary helps discovery. |
| Low-priority action | Text button | Avoid when the action must be highly discoverable. |
| Compact glyph action | Icon button | Requires accessible name and adequate target size. |
| Primary floating screen action | FAB / extended FAB | Only when a floating primary action model fits the screen. |
| Primary action plus related menu | Split button where supported | Primary side must remain predictable and independently activatable. |

The same screen can contain several actions without giving them equal visual weight.

## Destructive actions

A destructive action is not automatically the primary filled action.

- use explicit labels such as Delete account rather than vague Confirm;
- distinguish irreversible from recoverable actions;
- require confirmation only when risk warrants interruption;
- place destructive actions so accidental activation is unlikely;
- use error/destructive color semantics only when the platform/product system defines them;
- preserve keyboard focus and error/recovery behavior.

## FAB decision

Use a FAB when all are true:

1. there is a single high-value screen-level action;
2. floating placement improves persistent access;
3. the action remains meaningful while content scrolls;
4. it does not obscure content or compete with navigation.

Do not use a FAB as a decorative oversized button or for every create/add action.

## Icon actions

- icon visual size and hit target are separate;
- provide an accessible name independent of tooltip/icon font;
- toggles expose pressed/checked state semantically;
- selected/toggled state must not rely on color alone;
- keep focus indication visible.

## Async actions

For Save/Submit/Upload-style actions, define loading, duplicate activation, error, retry, and success behavior. Preserve stable control geometry where practical and do not leave controls permanently disabled after recoverable failures.

## Agent questions

Before choosing an action component, answer:

1. Is this local, screen-level, floating, compact, or destructive?
2. What is its priority relative to neighbors?
3. Can the user predict what activation will do?
4. What states can it enter?
5. Is there already a shared product component for this role?
