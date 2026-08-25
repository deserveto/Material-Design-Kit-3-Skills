# Design tokens and interoperability

Use this reference when introducing, migrating, exporting, or mapping Material 3 tokens.

## Token layers

Prefer a clear chain:

```text
source/reference values -> semantic system roles -> component roles
```

Components should normally consume semantic/component roles, not source values.

## DTCG 2025.10

The Design Tokens Community Group 2025.10 format is the first stable DTCG format and is suitable as an interchange representation between design/tooling systems.

Use DTCG when it improves portability across tooling. Do not force a second token format into a project that already has a strong token pipeline unless export/interchange is a real requirement.

A minimal conceptual example:

```json
{
  "color": {
    "primary": {
      "$type": "color",
      "$value": "#6750A4"
    }
  }
}
```

The exact serialized color form and resolver behavior must follow the target DTCG tooling; do not invent unsupported syntax.

## Mapping into existing projects

If a project already uses tokens such as `--color-brand-action`, `theme.colors.primary`, or `tokens.color.action.primary`, map the Material semantic meaning into that vocabulary instead of introducing duplicate `--md-sys-*` values everywhere.

Create a parallel Material token namespace only when the project is explicitly adopting Material as its design-system source, the namespace has a clear ownership/migration plan, and duplication will not leave two competing sources of truth.

## Cross-platform mapping

Preserve semantic meaning while translating implementation:

- Web -> CSS custom properties, theme objects, design-token build output;
- Compose -> `ColorScheme`, `Typography`, `Shapes`, motion/theme APIs available in the pinned version;
- Flutter -> `ThemeData`, `ColorScheme`, `TextTheme`, component themes;
- Android Views -> Material theme/style resources for maintenance/migration work.

Do not expect token names or component APIs to be identical across platforms.

## Verification

For a token change, verify light/dark schemes, foreground/container pairings, disabled/selected/error states, text/icon contrast, absence of unnecessary duplicate values, and reproducibility from the token source.
