# Flutter Material 3

**Reviewed: 2026-08-25.** Current Flutter documentation at review time reflects Flutter 3.44.7; check the target project's SDK before relying on version-specific behavior.

## Baseline

Material 3 has been the default Flutter Material style since **Flutter 3.16** (`ThemeData.useMaterial3` defaults to true). That flag alone does not guarantee a complete M2-to-M3 migration.

Inspect:

- Flutter/Dart version;
- `ThemeData` and `ColorScheme` setup;
- component-specific themes;
- old Material 2 widgets/patterns;
- navigation and adaptive layout code;
- existing golden/widget/integration tests.

## Theme

Prefer centralized `ThemeData.colorScheme` and `ThemeData.textTheme`. `ColorScheme.fromSeed` is a useful Material 3 scheme generator when appropriate to the brand/theme strategy. Use component theme properties for deliberate product-level overrides instead of local one-off colors and shapes.

## Migration

Some Material 2 widgets required newer component implementations rather than a visual reskin. Flutter's migration guidance specifically calls out navigation changes such as moving to `NavigationBar` where appropriate.

Do not:

- assume setting `useMaterial3: true` completes migration;
- replace the entire component architecture when a targeted migration is enough;
- keep a mix of old/new navigation behavior without checking interaction and layout consistency.

## Adaptive behavior

Use available window constraints and Flutter's responsive/adaptive layout tools rather than phone/tablet labels. Navigation form and pane strategy may change as space grows.

## Expressive caution

Material 3 Expressive is part of current Material direction, but feature parity and API naming differ across platforms. Do not copy Compose-only classes such as `MotionScheme` or `MaterialShapes` into Flutter guidance. Verify whether Flutter exposes an equivalent before coding; otherwise implement the design principle with stable Flutter primitives.

## Verification

Run the project's analyzer/tests and relevant golden/widget/integration tests. Render supported light/dark themes and relevant widths. Check focus/keyboard behavior on desktop/web targets when the application supports them.
