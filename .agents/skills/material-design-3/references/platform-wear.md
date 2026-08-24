# Wear OS Compose Material 3

**Reviewed: 2026-08-24.** Wear OS has its own Compose Material 3 implementation and release lifecycle. Do not route Wear UI to mobile `androidx.compose.material3` guidance as if the APIs were interchangeable.

## Current version snapshot

AndroidX Wear Compose release documentation lists, as of this review:

- stable Wear Compose line: **1.6.2**;
- alpha line: **1.7.0-alpha07**;
- `androidx.wear.compose:compose-material3` is the recommended Material library for current Wear UI;
- Wear Compose Material 3 has supported the Material 3 Expressive design system since the 1.5 stable generation.

Check the target project's pinned versions before coding. Wear foundation, navigation, and Material3 artifacts move together often enough that dependency compatibility matters.

## Use Wear libraries, not mobile substitutes

Prefer:

```text
androidx.wear.compose:compose-material3
androidx.wear.compose:compose-foundation
androidx.wear.compose:compose-navigation / navigation3 as supported
```

Do not mix mobile `androidx.compose.material3.MaterialTheme` into a Wear hierarchy without an explicit, justified reason. Mobile Material components are not optimized for the wrist and can create inconsistent color, typography, shape, input, and layout behavior.

## Wear Material 3 Expressive baseline

Stable Wear Material 3 includes Wear-specific expressive behavior and components such as:

- `AppScaffold` and `ScreenScaffold` for coordinated screen structure;
- `TransformingLazyColumn` for Wear scrolling behavior;
- `EdgeButton` for a bottom-edge primary action where appropriate;
- `ButtonGroup` for expressive grouped actions;
- shape-morphing icon/text buttons and toggles;
- Material3 alert/confirmation dialog families;
- dynamic color support appropriate to Wear/watch-face personalization.

Availability and exact overloads still depend on the pinned Wear Compose version. Do not copy examples from a 1.7 alpha page into a stable 1.6.x app without checking signatures.

## Round-screen layout

Design from Wear constraints rather than shrinking a phone screen:

- keep important content and targets away from clipped curved edges unless a Wear component is intentionally edge-aware;
- use Wear scaffold/list defaults before inventing padding;
- account for short viewport height and curved text where the product uses it;
- keep actions reachable and labels concise without sacrificing accessibility;
- validate on multiple watch sizes when tooling allows.

## Input and focus

Wear interaction includes touch, rotary input, swipe navigation, and haptics.

Verify:

- rotary focus moves predictably through scrollable content;
- focus returns to the correct element after navigation/back gestures;
- swipe-to-dismiss/reveal behavior uses the current Wear APIs;
- haptics reinforce meaningful thresholds rather than firing decoratively;
- shape morphing does not make targets unstable.

## Ambient mode and performance

Wear devices have tighter power/CPU/GPU constraints than typical phones.

- keep ambient UI intentional and compatible with the app's supported Wear versions;
- avoid continuous decorative animation;
- test scrolling/morphing performance on representative hardware/emulators;
- use baseline profiles and normal Compose performance tools for performance-sensitive flows;
- respect reduced motion and avoid expensive effects that do not improve task understanding.

## Migration boundary

When migrating Wear Material 2/2.5 to Wear Material 3:

1. inspect Wear Compose versions and imports;
2. migrate the theme and scaffolds;
3. map components using Wear Material3 equivalents rather than mobile equivalents;
4. remove long-term mixed Material2.5/Material3 usage;
5. expect screenshot/golden defaults to change because M3 spacing, sizing, motion, and component behavior differ;
6. verify rotary, swipe, focus, ambient, and multiple watch sizes.

## Verification

For Wear changes, run the project's tests/build and render at least the supported representative watch sizes. Check touch, rotary, swipe/back, focus, dynamic/brand themes, loading/error states, and performance for expressive motion. Report any alpha/experimental dependency or API opt-in explicitly.
