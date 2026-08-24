# Material 3 Expressive

Material 3 Expressive is an evolution/expansion of M3, not a separate “Material 4” system. Use it to strengthen hierarchy, usability, personality, and emotional character without discarding familiar interaction models.

## Five useful expressive levers

Google's M3 Expressive research and guidance emphasize the combined use of:

1. **Color**: stronger, intentional contrast and hierarchy.
2. **Shape**: contrasting silhouettes and, where supported, shape morphing.
3. **Size**: visibly larger treatment for genuinely important actions/content.
4. **Motion**: responsive spatial relationships and prominent transitions.
5. **Containment**: grouping and emphasis through containers.

Use one or a few levers to solve a hierarchy problem. Do not max out all five on every screen.

## Restraint rules

- Keep repeated utility actions calm and efficient.
- Reserve expressive motion for prominent/hero interactions.
- Preserve familiar labels, placement, and information architecture unless there is evidence a change improves the task.
- Decorative geometry must not make controls harder to recognize or target.
- More personality is not automatically more usability.
- Respect reduced motion and high-contrast/accessibility modes.

## Motion model

Current Compose M3 Expressive APIs expose `MotionScheme.standard()` and `MotionScheme.expressive()` plus fast/default/slow **effects** and **spatial** motion specifications.

Conceptually:

- effects -> color/alpha and other strictly bounded visual changes;
- spatial -> position, bounds, size, shape, and related movement.

**Status as of 2026-08-24:** AndroidX Compose Material3 stable is 1.4.0; `MotionScheme` is added in 1.5.0-alpha26. Treat it as alpha-version API unless the target project intentionally opts into that dependency line.

## Expressive shape library

Current Compose exposes 35 predefined normalized polygon shapes under the experimental `MaterialShapes` API:

`Arch`, `Arrow`, `Boom`, `Bun`, `Burst`, `Circle`, `ClamShell`, `Clover4Leaf`, `Clover8Leaf`, `Cookie12Sided`, `Cookie4Sided`, `Cookie6Sided`, `Cookie7Sided`, `Cookie9Sided`, `Diamond`, `Fan`, `Flower`, `Gem`, `Ghostish`, `Heart`, `Oval`, `Pentagon`, `Pill`, `PixelCircle`, `PixelTriangle`, `Puffy`, `PuffyDiamond`, `SemiCircle`, `Slanted`, `SoftBoom`, `SoftBurst`, `Square`, `Sunny`, `Triangle`, `VerySunny`.

**Status as of 2026-08-24:** `MaterialShapes` is annotated `ExperimentalMaterial3ExpressiveApi` in current Compose docs. Do not silently introduce it into a stable-only production codebase.

The semantic component corner-shape scale and this decorative polygon library are different systems. Do not replace ordinary component shapes with decorative polygons by default.

## Expressive typography

Newer Material implementations may expose emphasized typography roles. Use them to establish deliberate emphasis, not to make every label or body block louder. The ordinary display/headline/title/body/label hierarchy remains the baseline mental model.

## Expressive components

Google's current Material site advertises an updated Figma M3 Design Kit with Material 3 Expressive components/styles and highlights newer/updated families such as toolbars, split buttons, progress treatments, and button groups.

Actual component/API availability differs by platform and version. Verify the target implementation before coding.

## Review questions

Before accepting an expressive treatment, ask:

- What important thing becomes easier to notice or understand?
- Does the treatment improve hierarchy or only add novelty?
- Is a familiar control still recognizable?
- Does motion communicate a relationship or merely decorate it?
- Is the same effect being overused elsewhere?
- Does the design still work with reduced motion, larger text, high contrast, and keyboard navigation?
