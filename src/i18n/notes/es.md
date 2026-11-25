# Spanish (es) translation notes

## Style decisions

- **Register:** formal "usted" throughout. This matches Apple's Spanish enterprise/IT documentation and is the standard register for technical documentation addressed to system administrators.
- Default button labels stay in English ("OK", "Cancel", "More Information"): the app has no Spanish localisation, so that's what a Spanish Mac shows. The buttons themselves can be named in Spanish ("el botón « Más información »") but the quoted label is the app's English string.
- Numbers users type keep the decimal point (`15.7`, never `15,7`): swiftDialog parameters are comma-separated.
- Values users type stay in English: `weight=thin`, `alignment=left`, `size=small`, `true`/`false`, key names `Enter`, `Esc`, `return`.
- Option keys users type stay in English as list labels too (`size`, `color`); descriptive labels such as "modo de renderizado" are translated.
- Proper names of external resources (GitHub repositories, blog posts) stay in English.

## Key translation decisions

- icon → ícono (not símbolo, which is reserved for SF Symbols)
- button → botón (not tecla, which is for keyboard keys)
- key → clave (for JSON/settings keys), tecla (for keyboard keys)
- policy (Jamf) → política (not regla, which is for documents/rules)
- installer package → paquete de instalación
- Default button labels ("OK", "Cancel", "More Information") kept in English since swiftDialog has no Spanish localisation

## Apple reference

Pending: read Apple's Spanish documentation (https://support.apple.com/es-es/guide/deployment/welcome/web, https://support.apple.com/es-es/guide/terminal/welcome/mac) to confirm terminology for buttons, checkboxes, menus, and Apple silicon.

## Notes for reviewers

- Tone/register consistency (formal "usted" was used throughout)
- A few judgment calls where English terms were kept (Nudge, SF Symbols names, CLI flags)

## Reviewer feedback

None yet.
