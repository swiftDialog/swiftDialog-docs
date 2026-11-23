---
name: translate-page
description: Translate one swiftDialog docs page into another language, or check which translations are out of date with their English originals. A local TranslateGemma model writes drafts, then you review and fix them. Use when asked to translate a docs page, add or update a page under src/content/docs/<lang>/, or check or sync translations after English pages changed.
argument-hint: <page path or slug> <lang code> | check [lang] [page] | endpoint [list|use NAME|add]
---

# Translate a docs page

This skill has three modes:
- **Translate** (the default, steps 1–7): draft and review one page.
- **Check** (`check`, see the end of this file): find translations whose English page changed since they were last synced, and bring them up to date.
- **Endpoint** (`endpoint`, or when the user says the model has moved or asks to switch where it runs): see "The model endpoint" below.

## The model endpoint

Where the model runs is saved per user, outside the repo, by `endpoint.py`. Several endpoints can be saved; one is current.

```sh
E=.claude/skills/translate-page/scripts/endpoint.py
python3 $E show      # current endpoint; exit 3 = none set up yet
python3 $E list      # all saved, * = current
python3 $E add NAME --url URL [--model M] [--key-env VAR] [--use] [--force]
python3 $E use NAME
python3 $E remove NAME
python3 $E test [NAME]
```

**Before the first draft in a session, run `show`.** If it exits 3 (nothing set up), ask the user, in one question:
- where the model runs: host and port, or the full URL. Open WebUI is `http://<host>:3000/api/chat/completions`, Ollama `http://<host>:11434/v1/chat/completions`, LM Studio `http://<host>:1234/v1/chat/completions`. If they give only a host and port, ask which server it is rather than guessing the path.
- the model name (default `translategemma:12b`).
- if the server needs an API key, the name of the environment variable that holds it (e.g. `MACSTUDIO_API_KEY`). Never ask for the key itself, and never pass a key on the command line.
- a short name for the endpoint (e.g. the machine's name).

Then `add ... --use` and `test`. If the test fails, show the error and ask whether to fix the URL or keep it anyway.

**Switching.** When the user says the model moved, or a run fails because the endpoint is unreachable, run `list`. If another saved endpoint fits, offer to `use` it; otherwise ask for the new location and `add` it. For a single run on another endpoint, pass `--endpoint NAME` to `translate_page.py` instead of changing the current one. `TRANSLATE_API_URL` and `TRANSLATE_MODEL` override the saved values for one command.

Translate **one page at a time**. A local model (TranslateGemma, on whichever machine the user has set up, see "The model endpoint" below) writes a first draft. Your job is to make that draft correct, natural and consistent, and to keep the page building. Read [TRANSLATING.md](../../../TRANSLATING.md) for the project conventions.

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

- This uses the current endpoint (see "The model endpoint"). Exit 3 means none is set up: ask the user and add one, then rerun.
- Only prose goes to the model. Code blocks, imports, JSX/HTML, inline code and URLs are copied unchanged. Root-relative links to doc pages get the `/<lang>/` prefix.
- The script prints a JSON report. Exit 0 means clean. Exit 2 means the draft was written but has `untranslated_segments` (the model mangled placeholders, so the line stayed in English) or `structure_mismatches`. Exit 1 means nothing was written.
- If the endpoint's key variable isn't in the environment, the script reads it from the user's zsh/bash startup files. Never print or log the key.
- The script tries Python's HTTP client first, then falls back to `/usr/bin/curl`. If both fail with "No route to host" on a LAN address while `curl` works from the user's own terminal, the cause is usually the command sandbox or macOS Local Network privacy, not the server. Rerun with local network access allowed.
- If the endpoint is still unreachable, offer to switch to another saved endpoint or add a new one (see "Switching"). If the key is missing, tell the user which variable to set. Don't translate the page yourself unless they ask.
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
