---
name: translate-page
description: Translate one swiftDialog docs page into another language. A local TranslateGemma model writes the draft, then you review and fix it. Use when asked to translate a docs page, or to add or update a page under src/content/docs/<lang>/.
argument-hint: <page path or slug> <lang code>
---

# Translate a docs page

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
- Spot-check that no English prose is left (`grep` for a few distinctive English phrases from the source). English inside inline code or code blocks is expected; leave it.

## 7. Report back

Say which page and language you did, what you fixed in the draft, and anything a native speaker should check: terms you weren't sure of, or sentences where the meaning was ambiguous.
