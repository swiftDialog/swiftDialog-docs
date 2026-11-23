# Translating the swiftDialog docs

The docs use [Starlight's built-in i18n](https://starlight.astro.build/guides/i18n/).
English is served from the site root (`/`). Each other language is served from `/<lang>/`, e.g. `/de/`.

## How it works

- **Pages fall back automatically.** If a page has no translation, the English version is shown at the localized URL with a "not yet translated" notice. You can translate one page at a time.
- **Starlight's own UI is already translated** (search, table of contents, pagination, and so on) for most common languages.
- The **language picker** in the header lists every configured locale.

## Translating a page

Copy the English file to the same path under the language folder and translate it:

```
src/content/docs/basic-use/title.md      →  /basic-use/title/
src/content/docs/de/basic-use/title.md   →  /de/basic-use/title/
```

Keep the same filename and folder structure, or the page won't be linked to its English original.

Guidelines:
- Translate the prose, frontmatter `title` / `description`, and comments inside code examples.
- **Do not translate** CLI options (`--title`, `--button1text`), JSON keys, command-file commands, file paths or exit codes. They have to match what swiftDialog accepts.
- Prefix links to other docs pages with the language: `/de/basic-use/title/`, not `/basic-use/title/`. Starlight does not rewrite links inside page content, so an unprefixed link sends readers back to English. Every `/de/...` URL exists (untranslated pages fall back to English), so the prefix is always safe. Leave links to files in `public/` (e.g. `/images/...`) as they are.

## Glossary

[src/i18n/glossary.md](src/i18n/glossary.md) defines the key terms of these docs (dialog, icon, button, command file…): what each one means here, which everyday meanings to avoid, and the preferred translation in each language. Read it before translating, and add a line for your language when you settle on a term.

A language's line can list words that must not be used, e.g. `de: Schaltfläche. Not "Taste", "Knopf" or "Knöpfe".` The scripts search translations for these words. Matches count from the start of a word, so `Knopf` also catches `Knopfgröße`. List any inflected form that changes the start of the word, like `Knöpfe`. To list possible slips across all translations:

```sh
python3 .claude/skills/translate-page/scripts/check_translations.py --glossary [--lang de]
```

These are warnings, not errors. Some matches are correct in context ("Taste" for a keyboard key), so check each one.

## Adding a new language

`astro.config.mjs` doesn't need editing. Each language is a set of files:

1. `src/i18n/<lang>.json`: registers the language and holds its sidebar labels.
   ```json
   {
     "label": "Français",
     "lang": "fr",
     "groups": {},
     "pages": {}
   }
   ```
   The file name is the URL prefix (`fr.json` → `/fr/`). `label` is the name shown in the language picker.
2. `src/content/i18n/<lang>.json`: custom UI strings. Start with `{}` (see below).
3. `src/i18n/glossary.md`: add a line for the new language for every glossary term (e.g. `fr: boîte de dialogue`). Read the glossary first and choose one consistent translation per term. This should be done before translating pages, since page reviews check glossary consistency.
4. `src/content/docs/<lang>/`: translated pages, added over time.

## Custom UI strings

Text in our own components (e.g. the download button on the home page) is read from `src/content/i18n/<lang>.json`. `en.json` holds every key. Copy the keys you want to translate into the other language's file. Missing keys fall back to English.

New keys must also be declared in the `i18n` collection schema in `src/content.config.ts`. Use them in a component with `Astro.locals.t('key')`.

## Sidebar labels

The sidebar structure and English labels are defined once, in `astro.config.mjs`. Translated labels go in `src/i18n/<lang>.json`:

```json
"groups": { "Basic Use": "Grundlagen" },
"pages":  { "basic-use/title": "Titel" }
```

- `groups` are keyed by the group's English label. `pages` are keyed by the page slug.
- Leave out any label that should stay in English (product and feature names, or words that are the same in both languages). Missing labels show in English.
- If you rename a group or a slug in `astro.config.mjs`, update the keys too. The build warns about keys that match no sidebar entry (`[i18n] src/i18n/de.json: "pages.…" matches no sidebar entry`).

## Drafting with the local model

The `translate-page` Claude Code skill (`.claude/skills/translate-page/`) drafts a page with the local TranslateGemma model and then reviews it.

The model can run on any machine with an OpenAI-compatible chat completions API (Open WebUI, Ollama, LM Studio). Tell the scripts where it is once. The endpoint is saved in `~/.config/swiftdialog-docs/translate.json`, outside the repo, and the API key stays in an environment variable you name:

```sh
S=.claude/skills/translate-page/scripts
python3 $S/endpoint.py add studio --url http://studio.local:3000/api/chat/completions --key-env STUDIO_API_KEY
python3 $S/endpoint.py add laptop --url http://localhost:11434/v1/chat/completions   # Ollama, no key
python3 $S/endpoint.py use laptop     # switch
python3 $S/endpoint.py list           # * marks the current one
python3 $S/endpoint.py test           # check that it answers
```

Then draft a page:

```sh
python3 .claude/skills/translate-page/scripts/translate_page.py basic-use/title de [--endpoint studio]
```

It translates only the prose, keeps code and components unchanged, adds the language prefix to internal links, and prints a report of anything it couldn't translate, along with any glossary words to avoid (`glossary_warnings`). Always review its output before committing.

Clean model results are cached in `tmp/translate-cache/` (git-ignored), keyed by model, language and text, so redrafting a page only sends new or changed text to the model. Pass `--no-cache` to ignore the cache.

Identifiers in table cells (`button1`, option values, key names) belong in backticks in the English page. The script never sends inline code to the model, so they stay as they are.

## Keeping translations up to date

When an English page changes, its translations fall behind. To list translations whose English page changed more than 2 hours after they were last updated, with the English commits since:

```sh
python3 .claude/skills/translate-page/scripts/check_translations.py          # all languages
python3 .claude/skills/translate-page/scripts/check_translations.py --lang de --diff basic-use/title   # show what changed
```

After updating a translation, or after deciding an English change needs no translation change, set `translationSynced` in its frontmatter to the current time. That marks it as checked:

```yaml
translationSynced: 2026-11-20T18:30:00+00:00
```

The `translate-page` skill does all of this in its check mode (`/translate-page check de`).
