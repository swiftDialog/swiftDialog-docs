---
name: translate-page
description: Translate one swiftDialog docs page into another language, or check which translations are out of date with their English originals. A local TranslateGemma model writes drafts, then you review and fix them. Use when asked to translate a docs page, add or update a page under src/content/docs/<lang>/, or check or sync translations after English pages changed.
argument-hint: <page path or slug> <lang code> | check [lang] [page]
---

# Translate a docs page

This skill has two modes:
- **Translate** (the default, steps 1–7): draft and review one page.
- **Check** (`check`, see the end of this file): find translations whose English page changed since they were last synced, and bring them up to date.

Translate **one page at a time**. The local model (`translategemma:12b` on the Mac Studio) writes a first draft. Your job is to make that draft correct, natural and consistent, and to keep the page building. Read [TRANSLATING.md](../../../TRANSLATING.md) for the project conventions.

## 1. Inputs

- **Page**: a path (`src/content/docs/basic-use/title.md`) or slug (`basic-use/title`). It must be an English page, not one under a locale folder.
- **Language**: a locale code such as `de`. If either input is missing, ask.

## 2. Make sure the locale exists

Check that `src/i18n/<lang>.json` exists (each file there registers one language). If it doesn't, add the locale as TRANSLATING.md describes ("Adding a new language"), and tell the user you did.

## 3. Don't clobber existing work

If `src/content/docs/<lang>/<same path>` already exists, it may be a human translation. Ask before replacing it. To compare without replacing, write the draft somewhere else with `--out <scratch path>` and merge by hand.

## 4. Draft with the local model

```sh
python3 .claude/skills/translate-page/scripts/translate_page.py <page> <lang>
```

- This needs `MACSTUDIO_API_KEY`. The endpoint and model can be overridden with `TRANSLATE_API_URL` and `TRANSLATE_MODEL`.
- Only prose goes to the model. Code blocks, imports, JSX/HTML, inline code and URLs are copied unchanged. Root-relative links to doc pages get the `/<lang>/` prefix.
- The script prints a JSON report. Exit 0 means clean. Exit 2 means the draft was written but has `untranslated_segments` (the model mangled placeholders, so the line stayed in English) or `structure_mismatches`. Exit 1 means nothing was written.
- If the key isn't in the environment, the script reads it from the user's zsh/bash startup files. Never print or log the key.
- The endpoint is on the local network. If you run commands in a sandbox, "No route to host" usually means the sandbox is blocking LAN access. Rerun with local network access allowed.
- If the endpoint is still unreachable or the key is missing, stop and tell the user. Don't translate the page yourself unless they ask.
- For a page whose language isn't built in, pass `--lang-name "<English name>"`.

## 5. Review the draft (this is the important part)

First read the glossary, [src/i18n/glossary.md](../../../src/i18n/glossary.md). It defines what key terms mean in these docs and how each language translates them. Then read the English source and the draft side by side. A small local model gets the gist right but slips on details. Fix:

- **Glossary terms.** Every glossary term must be translated by its documented meaning, using the preferred translation for this language, the same way everywhere on the page. Typical slips: a "dialog" rendered as a conversation, "icon" rendered so it clashes with SF Symbols, or two different words for the same term on one page. If a term has no line for this language yet, choose a translation, use it consistently, add the line to the glossary, and tell the user. If you hit a word that needs a precise meaning and isn't in the glossary, suggest an entry to the user rather than adding one yourself.
- **Untranslated segments** listed in the report. Translate them yourself and keep inline code and links unchanged.
- **Never edit inline code or code blocks**, even when they contain English. Example commands like `--message "Welcome to swiftDialog"` usually sit above a screenshot showing exactly that text, and a translated example no longer matches the image. The script leaves code unchanged on purpose. Only comments inside fenced code blocks may be translated.
- **Values users type stay in English, even in prose.** Colour names (`black, blue, gray…`), alignment values (`left`, `centre`, `right`), defaults such as "Default is 'left'", key names (`size=`, `name=`), numbers users type (keep `15.7`, never the decimal comma `15,7`: swiftDialog parameters are comma-separated) and SF Symbol names are input to swiftDialog, so translating them breaks the command. The model often translates these, so check every option description.
- **Names and identifiers.** Never translate CLI options (`--button1text`), JSON keys, command-file commands, file paths, or the names in the glossary's "Keep in English" list.
- **Consistency across pages.** Use one register for the whole site; for German, check the existing `/de/` pages (currently formal "Sie"). Grep `src/content/docs/<lang>/` to check how other pages phrase things.
- **Meaning drift.** Watch for literal or wrong renderings, dropped negations, and changed numbers or defaults.
- **Heading anchors.** Starlight builds anchor IDs from heading text, so translated headings change them. Update `#fragment` links in this page to the new IDs (lowercase, spaces → `-`, punctuation dropped). Grep other `/<lang>/` pages for links to this page that carry a fragment and fix those too.
- **Frontmatter.** `title` and `description` should read naturally. Quote YAML values that contain `: `.
- **Component props**, such as `<Card title="...">` and aside titles `:::tip[...]`, are not sent to the model. Translate them by hand.

Edit the draft in place. Keep the structure the same as the English page: same sections, same code blocks, same components.

## 6. Verify

- `pnpm build` must succeed. MDX errors name the file and line.
- The script sets `translationSynced` in the frontmatter to the time of the draft. Leave it in place; the check mode relies on it.
- Spot-check that no English prose is left (`grep` for a few distinctive English phrases from the source). English inside inline code or code blocks is expected; leave it.

## 7. Report back

Say which page and language you did, what you fixed in the draft, and anything a native speaker should check: terms you weren't sure of, or sentences where the meaning was ambiguous.

---

# Check mode: are translations up to date?

Use this when asked to check translations, after English pages were edited, or before a release.

## 1. Find stale translations

```sh
python3 .claude/skills/translate-page/scripts/check_translations.py [--lang de] [page ...]
```

A translation needs checking when its English page changed **more than 2 hours** after the translation was last updated. The 2 hours allow for editing both in the same session. Change it with `--threshold` (e.g. `--threshold 1d`). A translation's "last updated" time is the later of its last git commit (or file time, if it has uncommitted edits) and its `translationSynced` frontmatter date.

The report lists each stale page with the English commits since. Exit 0 means everything is up to date, exit 2 means something needs checking. `orphan` means the English page was deleted or renamed; tell the user, and don't delete anything yourself.

## 2. See what changed in English

```sh
python3 .claude/skills/translate-page/scripts/check_translations.py --lang <lang> --diff <page>
```

This prints the English diff since the translation was last synced. Uncommitted English edits are included.

## 3. Update each stale translation

Work one page at a time:
- **Small changes** (a sentence, a value, a new option row): edit the matching place in the translation directly. Follow every rule of the review step above, especially the glossary and "never edit code".
- **Large changes** (new sections, restructured page): draft the whole page again into a scratch file with `translate_page.py <page> <lang> --out <scratch path>`, then copy the new or changed sections into the existing translation. Don't overwrite the translation wholesale: it may contain human corrections.
- **No translation change needed** (typo fix, whitespace, a change only inside code that the translation already carries, or a code change you copied over): still mark the page as checked.

In every case, finish by setting `translationSynced` in the translation's frontmatter to the current UTC time (`date -u +%Y-%m-%dT%H:%M:%S+00:00`). That clears the page from the check.

## 4. Verify and report

Run `pnpm build`, then run the check again; the pages you handled should no longer be listed. Report which pages you updated, which needed no change, and anything a native speaker should look at.
