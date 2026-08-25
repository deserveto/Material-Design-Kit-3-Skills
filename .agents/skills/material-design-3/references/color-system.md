# Material 3 color system and Material Color Utilities

Use this reference when deriving a Material color scheme from product/source colors or when implementing dynamic color.

## Prefer deterministic generation over guessed hex values

Google's Material Color Utilities provides HCT, tonal palettes, dynamic color schemes, scheme variants, light/dark behavior, and contrast levels.

A modern dynamic scheme is conceptually driven by source color (ARGB or HCT), scheme variant, light/dark mode, contrast level, and generated tonal palettes/semantic roles.

Current Material Color Utilities guidance uses contrast levels such as `0.0` default, `0.5` higher, `1.0` highest, and `-1.0` reduced contrast.

## Workflow

```text
brand/source color
        ↓
Material Color Utilities or platform-equivalent generator
        ↓
tonal palettes / dynamic scheme
        ↓
semantic Material roles
        ↓
project token layer
        ↓
components
```

Do not take a seed/source color and hard-code it directly into every primary component.

## Brand and dynamic color

Dynamic color is a product option, not a mandatory replacement for brand identity. For strict-brand products, keep deliberate brand light/dark fallbacks, enable user-derived color only where product direction allows it, preserve semantic role relationships, and verify critical brand/status colors remain understandable.

## Scheme variants

Material Color Utilities exposes variants such as tonal spot, content, expressive, fidelity, vibrant, neutral, monochrome, rainbow, and fruit salad. Treat these as inputs to a product color strategy, not visual presets to cycle through arbitrarily.

## Platform boundaries

- Compose may expose platform dynamic-color helpers and Material theme roles directly.
- Flutter commonly uses `ColorScheme` / `ColorScheme.fromSeed`; inspect the target SDK.
- Web projects may use Material Color Utilities directly or generate tokens at build/design time.
- Android Views can consume generated Material theme resources, but new Android Material work should prefer Compose.

Always inspect the target project's existing color pipeline before adding a new generator dependency.
