# Material 2 / legacy to Material 3 migration

Use this reference when the user explicitly asks to migrate an existing Material 2, Material 2.5, legacy Material, or partially migrated interface to Material 3. A migration is a semantic/component-system change, not a color-and-radius reskin.

## 1. Inventory before editing

Record the current state:

- platform and pinned dependencies/SDK;
- theme/color source and dark mode;
- typography and shape definitions;
- component library and custom wrappers;
- navigation model;
- adaptive layout strategy;
- interaction/accessibility primitives;
- screenshot/golden/e2e coverage;
- experimental APIs already accepted by the project.

Identify where M2 and M3 are already mixed. Do not assume a single flag or theme wrapper reveals the whole migration state.

## 2. Map semantics, not pixels

Migration order should follow system responsibilities:

1. **Theme roles**: move raw/legacy palette usage toward M3 semantic color roles.
2. **Typography**: map information hierarchy into M3 display/headline/title/body/label roles.
3. **Shape**: centralize component shape semantics rather than adding roundness locally.
4. **Components**: replace components whose interaction model changed, not just their visual defaults.
5. **Navigation**: adopt current M3 navigation patterns where the product structure calls for them.
6. **Layout/adaptive**: replace device-label branching or stretched phone layouts with available-space reasoning.
7. **States/accessibility**: re-verify focus, selected, disabled, error, loading, touch targets, text scaling, and reduced motion.
8. **Expressive**: only after the baseline migration is coherent, optionally add Expressive treatments where they improve hierarchy.

## 3. Prefer a phased migration

For non-trivial products, use a **phased** migration that keeps each step releasable:

### Phase A — foundation

Introduce/repair centralized color, typography, shape, motion, and icon tokens without rewriting unrelated screens.

### Phase B — shared components

Migrate shared buttons, fields, selection controls, cards/lists, dialogs/sheets, and feedback primitives. Preserve stable public APIs where practical so screens can migrate incrementally.

### Phase C — navigation and adaptive structure

Handle navigation bars/rails/drawers, app bars, pane scaffolds, and route/layout transitions. This is where cosmetic-only migrations most often fail.

### Phase D — screen migration

Move screens in coherent slices and remove old local styling as each slice converts.

### Phase E — cleanup

Remove dead M2 dependencies/tokens/wrappers, reconcile screenshots/goldens, and document any intentional legacy exceptions.

Do not leave two competing theme systems indefinitely. Temporary coexistence needs a defined boundary and removal plan.

## 4. Platform boundaries

### Web

There is no universal official M2→M3 React API mapping. Preserve the project's framework and accessible primitives; migrate semantic tokens, component behavior, hierarchy, and adaptive patterns rather than imitating an Android screenshot.

### Jetpack Compose mobile

Inspect the pinned `androidx.compose.material3` version and current Material2 imports. Prefer stable Material3 APIs supported by the project. Do not silently upgrade to an alpha line only to access Expressive APIs.

### Wear OS

Wear Material2/2.5 and Wear Material3 have separate libraries and Wear-specific component mappings. Use `platform-wear.md`; do not substitute mobile Material3 components.

### Flutter

`ThemeData.useMaterial3` being true is not proof that migration is complete. Inspect `ColorScheme`, `TextTheme`, component themes, old navigation widgets/patterns, and golden/widget tests. Replace legacy components deliberately where Material3 introduces a new model.

## 5. Visual-diff expectations

A correct M3 migration can legitimately change:

- default padding/height;
- navigation presentation;
- typography metrics;
- surface/color relationships;
- shape/elevation defaults;
- focus/state treatment;
- animation and transitions.

Do not force new components to reproduce an old screenshot pixel-for-pixel when the old screenshot encodes M2 defaults. Instead verify task flow, hierarchy, accessibility, product branding, and approved visual intent.

## 6. Migration acceptance checklist

Before calling migration complete:

1. no accidental parallel theme systems remain in migrated scope;
2. raw component colors/radii/type sizes are replaced by project semantic roles where appropriate;
3. component models and navigation are intentionally M3, not cosmetic M2;
4. adaptive behavior uses available space;
5. keyboard/focus/touch/semantics/text scaling are verified;
6. light/dark/dynamic/high-contrast modes supported by the product are verified;
7. tests/build and rendered states pass;
8. experimental/alpha adoption is explicitly documented;
9. remaining legacy scope is listed rather than hidden.
