# Material 3 foundations

Use this reference for platform-independent design decisions. Implementation details belong in the platform references.

## 1. Semantic token model

Think in three layers:

```text
reference/source values -> semantic system roles -> component roles
```

A component should usually consume a semantic role rather than own a raw color, radius, duration, or type size. This enables light/dark themes, brand variants, dynamic color, high-contrast adjustments, and future design-system changes without rewriting every component.

Avoid inventing token values when the project already has a coherent Material theme. Extend the system only when a real semantic role is missing.

## 2. Color

Material 3 builds schemes from primary, secondary, tertiary, neutral, and neutral-variant tonal families plus error roles. Components consume semantic roles.

Core relationship examples:

| Container/background | Foreground content |
|---|---|
| `primary` | `onPrimary` |
| `primaryContainer` | `onPrimaryContainer` |
| `secondary` | `onSecondary` |
| `tertiary` | `onTertiary` |
| `error` | `onError` |
| `surface` / `surfaceContainer*` | `onSurface` / `onSurfaceVariant` as appropriate |

Modern schemes also include surface hierarchy roles such as `surfaceContainerLowest`, `surfaceContainerLow`, `surfaceContainer`, `surfaceContainerHigh`, and `surfaceContainerHighest`, plus `surfaceDim`, `surfaceBright`, outline roles, inverse roles, and fixed accent families on platforms that expose them.

Rules:

- Do not pair an `on*` color with an unrelated container just because contrast looks acceptable.
- Do not treat a reference hex as a component API. Convert product colors into theme roles.
- Use error roles for error semantics, not merely for any red-looking decoration.
- Dynamic color is optional product behavior. Preserve a deliberate fallback scheme.
- Use color with typography, iconography, text, shape, or state semantics; do not make color the only state cue.

## 3. Typography

The baseline M3 type hierarchy has five semantic families with large/medium/small roles:

- Display: `displayLarge`, `displayMedium`, `displaySmall`
- Headline: `headlineLarge`, `headlineMedium`, `headlineSmall`
- Title: `titleLarge`, `titleMedium`, `titleSmall`
- Body: `bodyLarge`, `bodyMedium`, `bodySmall`
- Label: `labelLarge`, `labelMedium`, `labelSmall`

Reference-theme Roboto sizes are useful defaults, not branding requirements. Preserve the semantic hierarchy when using a custom typeface.

Choose a text role from meaning and information hierarchy, not from which font size happens to fit. Avoid using display/headline styles for ordinary dense UI merely to create drama.

M3 Expressive may add emphasized type roles on implementations that support them. Treat these as hierarchy tools, not a reason to emphasize everything.

## 4. Shape

Two concepts coexist:

1. **Component shape scale**: semantic corner shapes used by containers and components.
2. **Expressive polygon shapes**: decorative/morphable shapes introduced with M3 Expressive on implementations that expose them.

Use the shape scale coherently across a product. Do not assign arbitrary unique radii to each component. Shape can communicate grouping, hierarchy, state, and brand, but familiar controls must remain recognizable.

## 5. Motion

Use motion to explain spatial/state change, reinforce hierarchy, and make direct manipulation feel connected.

Current M3 Expressive distinguishes semantic motion for:

- **effects**: values with strict bounds such as color or alpha;
- **spatial**: position, size, shape, and bounds changes.

It also distinguishes **standard** motion for recurring/utilitarian interactions from **expressive** motion for prominent or hero interactions. Prefer semantic motion tokens when the platform exposes them; otherwise encode equivalent project-level tokens instead of scattering durations/easings.

Always respect reduced-motion preferences and avoid motion that delays routine tasks.

## 6. Elevation and surfaces

Do not equate hierarchy with drop shadow. M3 can communicate layering through surface-container tones plus physical/shadow elevation where needed.

Use higher/lower surface roles consistently to separate regions. Add shadow only when it clarifies spatial relationship, interaction, or platform convention.

## 7. Material Symbols

Material Symbols provide more than 2,500 glyphs and variable axes useful for state and hierarchy:

- `FILL`: unfilled to filled; useful for selected/toggled state.
- `wght`: stroke weight.
- `GRAD`: more granular emphasis adjustment with less effect on glyph size.
- `opsz`: optical size, typically 20–48dp.

Load only the axes and glyphs the product needs. An icon's visual size is separate from its interactive target size.

## 8. Theme checklist

Before creating local values, find the project's existing:

- color scheme and semantic token definitions;
- typography roles and font loading;
- shape scale;
- motion tokens/scheme;
- elevation/surface rules;
- icon system;
- light/dark/dynamic/high-contrast support.

If these already exist, reuse them.
