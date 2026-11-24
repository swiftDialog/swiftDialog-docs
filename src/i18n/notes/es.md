# Spanish (es) translation notes

## Style decisions

- **Register:** formal "usted" throughout. This matches Apple's Spanish enterprise/IT documentation and is the standard register for technical documentation addressed to system administrators.
- Default button labels stay in English ("OK", "Cancel", "More Information"): the app has no Spanish localisation, so that's what a Spanish Mac shows. The buttons themselves can be named in Spanish ("el botón « Más información »") but the quoted label is the app's English string.
- Numbers users type keep the decimal point (`15.7`, never `15,7`): swiftDialog parameters are comma-separated.
- Values users type stay in English: `weight=thin`, `alignment=left`, `size=small`, `true`/`false`, key names `Enter`, `Esc`, `return`.
- Option keys users type stay in English as list labels too (`size`, `color`); descriptive labels such as "modo de renderizado" are translated.
- Proper names of external resources (GitHub repositories, blog posts) stay in English.

## Apple reference

Pending: read Apple's Spanish documentation (https://support.apple.com/es-es/guide/deployment/welcome/web, https://support.apple.com/es-es/guide/terminal/welcome/mac) to confirm terminology for buttons, checkboxes, menus, and Apple silicon.

## Notes for reviewers

None recorded. The Spanish pages were translated before this file existed.

## Reviewer feedback

None yet.
