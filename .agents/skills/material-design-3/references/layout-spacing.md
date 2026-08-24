# Material 3 layout and spacing

Use this reference when composing page structure, panes, gutters, margins, content widths, edge-to-edge regions, or spacing relationships. Material layout is driven by **available space, content hierarchy, and task flow**, not by device-name branches.

## 1. Start with regions, not decoration

Before choosing padding or card shapes, identify the screen's structural regions:

- primary content or task area;
- top-level navigation;
- supporting/contextual content;
- persistent actions;
- transient overlays;
- system/viewport insets and safe areas.

Use spacing to clarify those relationships. Do not add containers merely to manufacture separation that spacing, alignment, typography, or surface roles already communicate.

## 2. Use a spacing system

Prefer the project's existing spacing tokens and official component defaults. If a Material project needs a new spacing layer, centralize a small reusable scale instead of scattering one-off margins through components.

Rules:

- choose spacing from semantic relationships: inside a component, between related items, between groups, and between major regions;
- keep repeated structures consistent;
- avoid arbitrary values chosen only to make one screenshot look balanced;
- do not copy Android `dp` references literally into CSS pixels or Flutter values;
- preserve enough room for focus indicators, touch targets, translated labels, and text scaling;
- let component defaults win unless the product has a deliberate system-level override.

A layout with many unrelated `13px`, `19px`, `27px`, and `31px` gaps is usually evidence that the system has leaked into local styling.

## 3. Adaptive composition

Material adaptive guidance uses canonical patterns such as list-detail, supporting pane, and feed. Change composition when more space enables a better information architecture; do not merely stretch the compact layout.

Typical reasoning:

| Available space | Useful response |
|---|---|
| Narrow/compact | One primary task or pane at a time; compact navigation; avoid horizontal compression. |
| Transition/medium | Re-evaluate navigation and whether a secondary pane can coexist without harming readability. |
| Wide/expanded | Consider list-detail/supporting panes, wider navigation forms, or bounded readable content instead of stretching everything edge to edge. |

State must survive layout transitions. Resizing a list-detail app must not silently lose the selected detail item or change the meaning of navigation.

## 4. Width and readable content

More width is not a command to make every line longer.

For text-heavy or form-heavy content:

- use the project's content-width or container tokens when they exist;
- bound reading width when extremely long lines reduce comprehension;
- use remaining space for useful supporting content, navigation, or breathing room when appropriate;
- avoid centering every application surface by default if task-oriented panes benefit from stable alignment.

For grids and feeds, prefer adaptive column strategies based on minimum useful item size and available space rather than fixed device categories.

## 5. Insets and edge-to-edge

Treat system bars, cutouts, rounded screens, browser safe areas, and platform chrome as layout inputs.

- Edge-to-edge content may extend behind system areas when the platform and design call for it, but interactive/text content still needs correct insets.
- Do not bake one device's status/navigation bar measurements into reusable layout code.
- On web, account for viewport-safe areas and browser UI only when relevant to the target environment.
- On Wear OS, use Wear-specific scaffolds and curved/round-screen guidance rather than mobile padding assumptions.

## 6. Alignment and containment

Use alignment to make scanning predictable:

- align related labels, controls, and repeated list content;
- keep primary actions in stable, expected regions;
- prefer shared edges and consistent baselines to decorative centering;
- use containment when it clarifies grouping or interaction, not because every section "needs a card".

Expressive containment can increase emphasis, but repeated utility regions should remain calm and efficient.

## 7. Platform translation

### Web

Use the project's grid/flex/container-query system. Prefer relative or tokenized spacing and content-width values. Container queries are often a better expression of component-level available space than global device breakpoints.

### Jetpack Compose

Use `WindowSizeClass`/adaptive APIs and Material3 Adaptive scaffolds supported by the pinned dependencies. Respect `WindowInsets` and scaffold defaults instead of hard-coding system-bar padding.

### Flutter

Use constraints, layout builders, safe areas, and the project's adaptive strategy. Keep spacing in theme/design tokens where practical instead of local constants repeated across widgets.

### Wear OS

Use Wear Compose Material 3 layout primitives such as screen/app scaffolds and Wear-specific lists. Round screens, rotary input, edge actions, and ambient behavior change what "good spacing" means.

## 8. Agent checklist

Before finalizing layout:

1. What are the primary and supporting regions?
2. Which spacing values come from the existing system or component defaults?
3. What changes because of available space rather than a device label?
4. Does wide space improve information architecture instead of merely increasing empty margins?
5. Do insets, focus rings, touch targets, larger text, and localization still fit?
6. Have compact, transition, and expanded states been rendered when the feature is adaptive?
