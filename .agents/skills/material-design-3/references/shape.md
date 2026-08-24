# Material 3 shape

**Reviewed: 2026-08-24.** Use this reference when choosing component corners, creating a shape theme, reviewing random radii, or considering Material 3 Expressive polygon/morph shapes.

Material shape has two related but different systems:

1. a semantic **component corner scale** used by ordinary containers and controls;
2. the newer **MaterialShapes** polygon library used for selected expressive treatments on implementations that expose it.

Do not treat these as interchangeable.

## 1. Baseline component shape scale

Material shapes direct attention, identify components, communicate state, group content, and express brand. The shape scale should be centralized so components consume semantic roles instead of owning arbitrary radii.

Current Compose Material 3 guidance demonstrates five themed `Shapes` slots with this baseline example:

| Compose slot | Baseline example |
|---|---:|
| `extraSmall` | 4dp |
| `small` | 8dp |
| `medium` | 12dp |
| `large` | 16dp |
| `extraLarge` | 24dp |

Compose also provides `RectangleShape` as the square/no-radius endpoint and `CircleShape` as the fully rounded endpoint.

The same data is available to tooling in `../assets/shape-baseline.json`.

### Important scope

These values are a Compose documentation **example/baseline reference**, not universal CSS values and not permission to overwrite an existing product shape theme.

- Do not mechanically translate `16dp` into `16px` on every platform.
- Do not assign one-off radii component by component when a semantic theme role exists.
- Do not override official/project component defaults unless there is a product reason.
- Do not make every container fully rounded merely because Material 3 supports rounder shapes.

## 2. Component semantics before radius

A shape choice should follow component semantics and the existing theme. Current Compose documentation gives examples such as cards using `medium` and FABs using `large`; the `Shapes` API documentation also describes default mappings for several components.

When implementing:

1. identify the component or container's semantic role;
2. inspect the platform/component default and project theme;
3. reuse the existing shape slot when it fits;
4. customize centrally when the product needs a coherent brand treatment;
5. override locally only when the exception communicates something meaningful.

A visually balanced collection of random `10px`, `14px`, `18px`, and `22px` radii is not a shape system.

## 3. Newer Compose 1.5 alpha shape slots

Current Compose Material3 `Shapes` **1.5.0-alpha26** expands the constructor with:

- `largeIncreased`
- `extraLargeIncreased`
- `extraExtraLarge`

`ShapeDefaults` exposes corresponding defaults. These are newer 1.5 alpha-line API additions as of the review date; do not assume they exist in a stable 1.4.x project.

If a design calls for these concepts but the target is stable-only, prefer the project's existing stable shape primitives unless the user explicitly accepts an alpha upgrade.

## 4. Material 3 Expressive polygon shapes

Current Compose exposes **35** normalized predefined `RoundedPolygon` shapes through `MaterialShapes`:

`Arch`, `Arrow`, `Boom`, `Bun`, `Burst`, `Circle`, `ClamShell`, `Clover4Leaf`, `Clover8Leaf`, `Cookie12Sided`, `Cookie4Sided`, `Cookie6Sided`, `Cookie7Sided`, `Cookie9Sided`, `Diamond`, `Fan`, `Flower`, `Gem`, `Ghostish`, `Heart`, `Oval`, `Pentagon`, `Pill`, `PixelCircle`, `PixelTriangle`, `Puffy`, `PuffyDiamond`, `SemiCircle`, `Slanted`, `SoftBoom`, `SoftBurst`, `Square`, `Sunny`, `Triangle`, `VerySunny`.

As of 2026-08-24, `MaterialShapes` is annotated `ExperimentalMaterial3ExpressiveApi` and belongs to the current Compose Material3 1.5 alpha API line. It can provide shapes directly or participate in a `Morph`.

### Use expressive polygons when

- shape contrast strengthens hierarchy or state;
- a prominent/hero interaction benefits from shape morphing;
- the platform and pinned dependency actually support the API;
- the result remains recognizable, targetable, and accessible.

### Do not use expressive polygons when

- the only reason is that the API exists;
- an ordinary button/card/container is clearer with its normal component shape;
- the product is stable-only and would require an unapproved experimental dependency;
- many competing silhouettes create visual noise;
- the shape makes touch targets or focus outlines unclear.

## 5. Shape morphing

Morphing is most useful when it communicates a state or spatial relationship. The start/end shapes should be compatible with the interaction's meaning, and the transition should not delay routine work.

Respect reduced-motion preferences. If motion is reduced, preserve the state change through static shape, color, iconography, text, or another non-motion cue as appropriate.

## 6. Platform translation

### Web

Use the project's existing radius/shape tokens. CSS border radii can represent the ordinary corner scale, but Android `dp` values are references rather than mandatory CSS pixels. Expressive polygon shapes require an intentional web implementation; do not pretend a Compose `RoundedPolygon` API exists in CSS.

### Jetpack Compose

Use `MaterialTheme.shapes` and component defaults for ordinary shape semantics. Inspect the pinned Material3 version before referencing increased slots or `MaterialShapes`; report any `@ExperimentalMaterial3ExpressiveApi` opt-in explicitly.

### Flutter

Use the Material/theme shape APIs available in the project's Flutter version and component defaults. Do not copy Compose API names into Flutter code.

## 7. Agent decision checklist

Before adding a radius or polygon:

1. Does the project already have a Material shape theme?
2. Which component semantic/default applies?
3. Is this a reusable theme decision or a justified local exception?
4. Is an Android `dp` reference being incorrectly copied into another platform?
5. Is an Expressive polygon actually improving hierarchy/state?
6. Does the pinned dependency expose the requested API?
7. Will the shape still work with focus outlines, large text, touch targets, and reduced motion?
