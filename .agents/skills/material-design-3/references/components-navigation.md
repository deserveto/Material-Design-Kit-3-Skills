# Material 3 navigation components

Use this guide for top-level destinations, tabs, app bars, navigation bars, rails, drawers, and adaptive navigation. Navigation structure follows information architecture and available space.

## Top-level navigation

| Situation | Typical Material family |
|---|---|
| Few top-level destinations in compact layouts | Navigation bar |
| Top-level destinations with more horizontal room | Navigation rail |
| Larger persistent hierarchy or many destinations | Navigation drawer |
| Peer sections inside one screen/context | Tabs |
| Screen title plus navigation/actions | App bar / toolbar as appropriate |

A wider window is a reason to reconsider navigation form, not to stretch a compact Navigation bar across the whole canvas.

## Navigation rail

A Navigation rail is appropriate when top-level destinations benefit from persistent vertical placement and the window has enough width. Preserve destination identity and selected semantics if the compact version uses a bottom navigation bar.

Do not switch components purely at a hard-coded device label. Use the project's available-space/adaptive model.

## Selected state

- expose selection semantically;
- combine color with icon fill, indicator, text treatment, or another cue;
- retain a visible keyboard focus indicator separate from selected state;
- preserve route/state during adaptive navigation-form transitions.

## Tabs vs top-level navigation

Tabs organize peer content within the current destination. They should not become a substitute for app-wide navigation simply because both present multiple labels.

## App bars and toolbars

Keep title, navigation, contextual actions, and scrolling behavior predictable. When an Expressive toolbar or newer platform API is desired, verify availability in the pinned implementation before coding.

## Adaptive checks

Render at compact and wide sizes and verify:

1. destination count still fits;
2. labels do not truncate into ambiguity;
3. current destination remains selected after resize;
4. keyboard/rotary focus order remains logical;
5. content is not hidden behind persistent navigation;
6. back/up behavior does not change meaning across layout forms.
