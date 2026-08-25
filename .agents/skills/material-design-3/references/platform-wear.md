# Wear OS Compose Material 3

**Reviewed: 2026-08-25.** Wear OS has its own Compose Material 3 implementation and release lifecycle. Do not route Wear UI to mobile `androidx.compose.material3` guidance as if the APIs were interchangeable.

## Current version snapshot

AndroidX Wear Compose release documentation lists, as of this review:

- stable Wear Compose line: **1.6.2**;
- current preview line: **1.7.0-beta01**;
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

Stable Wear Material 3 includes Wear-specific expressive behavior and components such as `AppScaffold` and `ScreenScaffold`, `TransformingLazyColumn`, `EdgeButton`, `ButtonGroup`, shape-morphing icon/text buttons and toggles, Material3 alert/confirmation dialog families, and dynamic color support appropriate to Wear/watch-face personalization.

Availability and exact overloads still depend on the pinned Wear Compose version. Do not copy examples from a 1.7 beta page into a stable 1.6.x app without checking signatures.

## Round-screen layout

Design from Wear constraints rather than shrinking a phone screen. Keep important content and targets away from clipped curved edges unless a Wear component is intentionally edge-aware, use Wear scaffold/list defaults before inventing padding, account for short viewport height and curved text where used, keep actions reachable, and validate on multiple watch sizes when tooling allows.

## Input and focus

Verify rotary focus, focus restoration after navigation/back, current swipe behavior, meaningful haptics, and stable targets during shape morphing.

## Ambient mode and performance

Keep ambient UI intentional, avoid continuous decorative animation, test scrolling/morphing performance, use normal Compose performance tools, and respect reduced motion.

## Migration boundary

When migrating Wear Material 2/2.5 to Wear Material 3: inspect versions/imports, migrate theme/scaffolds, map to Wear M3 equivalents rather than mobile ones, remove long-term mixed M2.5/M3 usage, update screenshot/golden expectations deliberately, and verify rotary/swipe/focus/ambient behavior.

## Verification

Run the project's tests/build and render representative watch sizes. Check touch, rotary, swipe/back, focus, dynamic/brand themes, loading/error states, and performance for expressive motion. Report any beta/alpha/experimental dependency or API opt-in explicitly.
