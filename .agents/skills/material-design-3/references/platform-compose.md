# Jetpack Compose Material 3

**Reviewed: 2026-08-24.** Re-check primary sources before relying on version-sensitive APIs.

## Current version snapshot

AndroidX Compose Material3 release documentation lists:

- stable: **1.4.0**;
- alpha: **1.5.0-alpha26** (released 2026-08-12);
- Material3 Adaptive stable: **1.3.0**.

Do not change a project's dependency channel just to access an Expressive API unless the user/product explicitly accepts alpha or experimental dependencies.

## Stable-first implementation

Inspect the app's actual dependency/BOM versions before coding. Prefer APIs available in the pinned stable line.

Core theme concepts include:

- `MaterialTheme.colorScheme`;
- `MaterialTheme.typography`;
- `MaterialTheme.shapes`;
- dynamic light/dark color schemes on supported Android versions;
- Material3 components matching the interaction semantics.

A top-level theme should centralize product color, typography, and shape. Do not create a second local theme in each screen.

## Dynamic color

Dynamic color is supported on Android 12+ through platform Material APIs. Treat it as a product-controlled mode and provide brand/fallback light and dark schemes for unsupported or intentionally fixed-brand cases.

## Expressive API status

As of the review date:

- `MotionScheme` is added in **1.5.0-alpha26**;
- latest `MaterialTheme` alpha API exposes `motionScheme` alongside color, typography, and shapes;
- `MaterialShapes` is marked `ExperimentalMaterial3ExpressiveApi`;
- some Expressive component APIs remain experimental or are evolving.

Therefore:

1. inspect the pinned dependency;
2. check whether the desired API exists there;
3. if not, implement the Material concept using stable primitives where practical;
4. only propose an alpha/experimental upgrade explicitly, with the trade-off stated.

## Adaptive Compose

Use current window size/adaptive APIs rather than device-type tests. Material3 Adaptive provides scaffolds/patterns for list-detail, supporting panes, and adaptive navigation. Match usage to the project's current adaptive dependency version.

## Accessibility

Prefer Material components because they carry useful semantics and interaction behavior, but still verify labels, focus, target sizes, traversal order, custom gestures, high-contrast/theme behavior, and text scaling for the specific screen.

## Verification

For a Compose UI change:

- run unit/instrumentation/UI tests already used by the project;
- compile against the project's pinned dependency versions;
- use previews/emulator/device screenshots when available;
- test dynamic/brand light and dark schemes that the app supports;
- test compact and expanded window states for adaptive screens;
- explicitly report any `@ExperimentalMaterial3ExpressiveApi` opt-in.
