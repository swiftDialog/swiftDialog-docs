# French (fr) translation notes

## Style decisions

- **Register:** "vous" throughout.
- Default button labels follow the app's French strings (`fr.lproj`): "D'accord", "Annuler", "Plus d'information". The button itself is "le bouton « Plus d'informations »"; only the quoted label is singular.
- Numbers users type keep the decimal point (`72.3`, never `72,3`): swiftDialog parameters are comma-separated.
- Values users type stay in English: `weight=thin`, `alignment=left`, `size=small`, `true`/`false`, key names `Enter`, `Esc`, `return`.
- Option keys users type stay in English as list labels too (`size`, `color`); descriptive labels such as "mode de rendu" are translated.
- Proper names of external resources (GitHub repositories, blog posts) stay in English.

## Notes for reviewers

From the full translation, 2026-11-23:

- `advanced/inspect/ipc-contract-gap-analysis.md` (high priority): dense technical page. Several blockquotes were rewritten by hand after meaning drift in the draft. "écart" is used for "gap" throughout; "vitalité du processus" for "process vitality" may need review.
- `examples/showcase.md`: repository and resource titles left in English on purpose.

## Reviewer feedback

### 2026-11-24: native-speaker reviewer (annotated PDF of the getting-started and basic-use pages)

Applied in commit 9d1713a. Summary of points and outcomes:

- Missing full stops (introduction, title): accepted. The English source had the same gap; fixed there too.
- "paquet d'installation" for the .pkg, not "programme d'installation" / "installateur": accepted, applied site-wide, added to glossary.
- Jamf policy → "règle", not "politique"; trigger names "Inscription terminée, Check-in récurrent, Self Service": accepted, applied site-wide, added to glossary.
- "Apple Silicon", not "silicium Apple": accepted, added to the glossary's Keep in English list.
- `propriété=valeur` for the `property=value` placeholder (title): accepted; it's a pattern, not something users type.
- images, web-content and icon wording fixes: accepted, with two grammar corrections to the suggestions ("présent", "plus d'une image est spécifiée").
- "Objets iconiques" heading → "Spécifier des icônes au format JSON": accepted ("iconiques" meant "iconic").
- Overlay background "cadre": changed differently, to "carré arrondi". The English says "squircle"; the draft's "cercle" was wrong, and "cadre" means frame.
- Default button labels "D'accord", "Annuler", "Plus d'information": accepted; they match the app's French strings.
- Button symbol list labels `size`, `color` kept in English: accepted; "mode de rendu" stays translated, since "rendering mode" is not typed.
- "Kandji" → "Iru": accepted as an English source change, applied in all languages.
- Broken images on the icon page: also broken in English; not yet fixed.
