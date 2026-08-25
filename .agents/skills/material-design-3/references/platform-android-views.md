# Android Views / Material Components (maintenance profile)

**Reviewed: 2026-08-25.**

Material Components for Android (Views-based MDC-Android) is now in official maintenance mode after Android/Material moved to a Compose-first direction in 2026.

Current snapshot:

- latest MDC-Android release: **1.14.0**;
- 1.14.0 includes Material 3 Expressive themes/styles and updated component styles;
- the project states that no more feature releases are planned for Views;
- existing Views applications should begin or continue migrating toward Compose for new Material/platform capabilities.

## When to use this profile

Use it for maintaining an existing XML/View-based app, targeted M2/M3 migration, applying supported 1.14.0 Material3Expressive styles to an app that intentionally remains on Views, or planning phased interop/migration to Compose.

Do not choose Views as the default greenfield Material implementation when Compose is viable.

## Implementation rules

1. Inspect the pinned `com.google.android.material:material` version and `minSdk`.
2. Reuse centralized themes/styles instead of local one-off colors/radii.
3. Prefer existing Material components over recreating interaction behavior.
4. If Expressive styles require `1.14.0`, make the dependency change explicit.
5. Keep Views/Compose interop boundaries clear during migration; do not rewrite unrelated screens solely for consistency.

## Migration posture

```text
theme/token alignment
    -> high-value component replacements
    -> screen-by-screen Compose adoption
    -> navigation/adaptive architecture where justified
```

Do not call a theme-only reskin a full migration.

## Verification

Run existing Gradle/unit/instrumentation checks and render affected Views. Verify accessibility, keyboard/D-pad behavior where relevant, touch targets, text scaling, light/dark themes, and mixed Views/Compose state restoration.
