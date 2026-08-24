# Material 3 input and selection components

Use this guide for text fields, checkboxes, radio buttons, switches, segmented buttons, chips, pickers, and compact selection/input controls.

## Selection model first

| User intent | Typical family |
|---|---|
| Binary immediate setting | Switch when the setting takes effect directly |
| Independent multi-selection | Checkbox |
| Choose one from a small visible set | Radio buttons or single-choice segmented buttons |
| Choose several compact visible options | Checkboxes or multi-choice segmented buttons when appropriate |
| Apply/remove compact filters | Filter chips |
| Enter a compact user-created entity/value | Input chip where supported |
| Trigger contextual suggestion/help action | Suggestion/assist chip |

Do not use chips as generic tiny buttons for unrelated secondary actions.

## Text fields

Use filled or outlined fields according to the established product style and hierarchy. Preserve:

- persistent/understandable label behavior;
- helper and error text;
- required semantics;
- autofill/autocomplete where applicable;
- keyboard/input type;
- accessible name/description;
- disabled/read-only distinction;
- text scaling and long localization.

Error state needs text/semantics beyond color.

## Switch vs checkbox

A switch commonly represents a setting that changes state immediately. A checkbox commonly represents selection or a value submitted as part of a larger decision. Follow platform/product conventions rather than treating them as visual alternatives.

## Segmented controls

Use when the options are few, mutually understandable, and benefit from being visible together. Do not compress long labels into segments just to avoid a menu.

## Pickers

Prefer the platform's current Material date/time picker when available. Do not recreate complex picker interaction from generic text fields unless product constraints demand it.

## State contract

Selection controls must expose selected/checked state semantically, remain usable by keyboard/touch as appropriate, and preserve visible focus. Selected state must not be color-only.
