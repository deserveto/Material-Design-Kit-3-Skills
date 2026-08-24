# Material 3 typography

**Reviewed: 2026-08-24.** Use this reference when choosing, creating, migrating, or reviewing a Material 3 type system. The numbers below are a **baseline reference**, not a mandatory brand specification.

## 1. Choose a semantic role first

Material 3 organizes its baseline type scale into **15 semantic roles**: five families with large, medium, and small variants.

- **Display**: the largest, shortest, highest-emphasis text. Reserve for genuinely prominent content.
- **Headline**: major page or section hierarchy.
- **Title**: medium-emphasis, relatively short headings such as component or subsection titles.
- **Body**: reading, descriptions, and general content.
- **Label**: controls, compact annotations, and supporting UI text.

Choose the role from meaning and hierarchy before choosing a font size. Do not use a display role merely because a layout has empty space, and do not shrink body/label text just to make dense UI fit.

## 2. Baseline reference scale

Google's current Compose Material 3 guidance documents this default reference scale:

| Role | Reference style | Size | Line height |
|---|---|---:|---:|
| `displayLarge` | Roboto | 57sp | 64sp |
| `displayMedium` | Roboto | 45sp | 52sp |
| `displaySmall` | Roboto | 36sp | 44sp |
| `headlineLarge` | Roboto | 32sp | 40sp |
| `headlineMedium` | Roboto | 28sp | 36sp |
| `headlineSmall` | Roboto | 24sp | 32sp |
| `titleLarge` | Roboto Medium | 22sp | 28sp |
| `titleMedium` | Roboto Medium | 16sp | 24sp |
| `titleSmall` | Roboto Medium | 14sp | 20sp |
| `bodyLarge` | Roboto | 16sp | 24sp |
| `bodyMedium` | Roboto | 14sp | 20sp |
| `bodySmall` | Roboto | 12sp | 16sp |
| `labelLarge` | Roboto Medium | 14sp | 20sp |
| `labelMedium` | Roboto Medium | 12sp | 16sp |
| `labelSmall` | Roboto Medium | 11sp | 16sp |

The same data is available to tooling in `../assets/typography-baseline.json`.

### How to interpret the table

- `sp` is the Android/Compose reference unit. It is **not** a command to use CSS pixels on the web.
- Roboto/Roboto Medium are reference-theme styles, not branding requirements.
- A product may intentionally use fewer than all 15 roles if its hierarchy remains coherent.
- Preserve role relationships when mapping a custom typeface. Different fonts have different metrics, x-heights, optical sizes, and weight behavior, so visual tuning may be required.
- If the project already has a coherent Material typography theme, reuse it instead of recreating this baseline locally.

## 3. Font family and weight

A custom typeface is valid Material 3. Keep semantic hierarchy stable even when the actual family changes.

When adapting a brand font:

1. inspect the font's available weights, variable axes, and metrics;
2. map regular reading roles to legible weights rather than blindly copying a numeric weight;
3. map title/label emphasis deliberately;
4. verify that line height still avoids clipping and cramped multiline text;
5. test fallback fonts and loading behavior.

Do not fake unavailable weights with browser synthesis or platform-specific tricks unless the project intentionally accepts that rendering trade-off.

## 4. Letter spacing and custom metrics

Material implementations expose letter spacing and other text-style properties. Use the platform/project defaults first. If customizing them, do so as part of a centralized typography system rather than scattering tracking values across components.

The Compose guidance demonstrates that individual roles may carry different tracking values. Do not infer one universal letter-spacing value for the entire scale.

## 5. M3 Expressive emphasized roles

Current Compose Material3 **1.5.0-alpha26** exposes emphasized counterparts for the ordinary typography roles, such as `titleLargeEmphasized`, `bodyMediumEmphasized`, and `labelSmallEmphasized`.

These are newer alpha-line API surface as of the review date. They strengthen hierarchy; they are not a replacement for the ordinary 15-role baseline and are not a reason to silently move a stable production dependency to alpha.

## 6. Platform translation

### Web

Map Material semantics into the project's existing token system. Use scalable CSS units and preserve browser/user text scaling.

A reasonable token shape is:

```css
:root {
  --md-sys-typescale-body-large-size: 1rem;
  --md-sys-typescale-body-large-line-height: 1.5rem;
}
```

That example expresses the 16/24 relationship for a common 16px root, but the baseline table is not a requirement to lock the root font size or disable zoom. Prefer `rem`/relative units and existing design tokens over raw `px` duplication.

### Jetpack Compose

Use `MaterialTheme.typography` and `TextStyle`/`sp`. Inspect the pinned Material3 version before using emphasized alpha APIs. Keep typography centralized in the app theme.

### Flutter

Use the current `ThemeData`/`TextTheme` Material 3 model supported by the project's Flutter version. Preserve platform text scaling and avoid hard-coded text sizes in individual widgets when a semantic theme role exists.

## 7. Accessibility and localization

Typography is incomplete until it survives real content.

Verify:

- text scaling / large-font settings;
- reflow without clipping or hidden actions;
- long translations and different scripts;
- fallback glyph coverage;
- readable contrast and disabled states;
- adequate line height for multiline text;
- truncation only where the product explicitly permits it.

Do not disable text scaling to preserve a screenshot-perfect layout.

## 8. Agent decision checklist

Before writing a new text value:

1. Is there already a semantic typography role in the project?
2. What information hierarchy does this text represent?
3. Is the baseline value actually appropriate for this platform/font?
4. Does this need a custom brand mapping or simply the existing theme role?
5. Will larger text, localization, and fallback fonts still work?
6. If using an emphasized role, does the pinned platform version support it without an unapproved dependency change?
