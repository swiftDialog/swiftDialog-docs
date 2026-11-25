# Simplified Chinese (zh-hans) translation notes

## Style decisions

- **Register:** formal, neutral address throughout (similar to Apple's simplified Chinese documentation).
- Default button labels follow the app's simplified Chinese strings if available; otherwise keep English ("OK", "Cancel", "More Information").
- Numbers users type keep the decimal point (`15.7`, never `15,7`): swiftDialog parameters are comma-separated.
- Values users type stay in English: `weight=thin`, `alignment=left`, `size=small`, `true`/`false`, key names, colour names (`black`, `blue`, etc.), SF Symbol names, CLI options, JSON keys, file paths.
- Apple product and feature names stay in English: swiftDialog, Dialog, macOS, Apple Silicon, SF Symbols, Jamf Pro, jamfHelper, Nudge, MDM, SwiftUI, Markdown.
- Preset names (Deployment, Cards, Compact List, Toast, Unified, Guidance) stay in English; only the word "preset" is translated.

## Notes for reviewers

Pages are being translated in this session; review notes are added per page below.

### index.mdx

- The quick-start bash code block was translated by hand, following the de/fr/ja pattern: comments and user-facing string values translated, option names (`--title`, `--message`, etc.) and `SF=star.fill` kept in English.
- `--button1text "提交"` — translated the button label; matches the pattern of de ("Senden") / fr ("Soumettre") / ja ("送信").
- All internal doc links prefixed with `/zh-hans/`; external links (macadmins.org, youtube.com, github.com) left unprefixed.
- Full-width Chinese periods "。" were stripped from headings (the model added them; Starlight heading anchors don't need them).
- No glossary terms flagged on this page.

### getting-started/introduction.md

- Line 19 (`.pkg` installer paragraph) was left in English by the model due to lost placeholders; translated by hand. `.pkg`, `/usr/local/bin/dialog`, `$PATH` kept in English.
- Stripped full-width periods "。" from headings and frontmatter title.
- Fixed broken markdown links (missing `)`, missing trailing `/`, missing opening `[`).
- Changed "物品清单" to "项目列表" to match sidebar label.
- Translated "Modifying CMD+Q" link text to "Command-Q 行为" to match sidebar.
- Removed extra backticks the model added around `$PATH` and around `--title`/`--message` (English uses single backticks).
- No glossary terms flagged on this page.

### getting-started/installation.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed broken markdown links (]` → `)` on releases page links).
- "提取二进制数据" → "提取二进制文件" (binary data → binary file).
- No glossary terms flagged on this page.

### getting-started/requirements.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed broken link (]` → `)` on v2.2.1 release link).
- Changed "正在检查更新" to "检查更新" (the English is a noun phrase "Checking for updates", not an ongoing action).
- No glossary terms flagged on this page.

### basic-use/title.md

- Stripped full-width periods "。" from all headings and frontmatter.
- No glossary terms flagged on this page.

### basic-use/message.md

- Stripped full-width periods "。" from all headings and frontmatter.
- Changed heading "信息定位" to "消息位置" (more natural).
- Translated the untranslated "Example:" segment to "示例：" (code kept in English).
- No glossary terms flagged on this page.

### basic-use/buttons.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed broken markdown links and missing opening brackets.
- Translated two untranslated segments by hand (button style center behavior, [return]/[enter] key behavior).
- No glossary terms flagged on this page.

### basic-use/icon.md

- Stripped full-width periods "。" from headings and frontmatter.
- Translated two untranslated segments by hand (light/dark mode icons TOC entry, colour gradients paragraph).
- Fixed broken link in table of contents.
- No glossary terms flagged on this page.

### basic-use/markdown.md

- Stripped full-width periods "。" from headings and frontmatter.
- Translated the untranslated Markdown line-break paragraph by hand.
- No glossary terms flagged on this page.

### basic-use/video.md

- Stripped full-width periods "。" from headings and frontmatter.
- Translated two untranslated segments by hand (example command, private Vimeo note).
- Changed heading "信息定位" → "消息位置" (applied consistently).
- No glossary terms flagged on this page.

### basic-use/web-content.md

- Stripped full-width periods "。" from frontmatter.
- No other issues found.

### advanced/command-line-options.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed broken markdown links (]` → `)`) across many cross-reference links.
- Fixed table header "论点；争论" → "选项" (23 occurrences, all tables).
- Translated four untranslated segments by hand (resizable option, two "See also" cross-references, quit key option).
- Changed "物品清单" heading → "项目列表" to match sidebar label.
- No glossary terms flagged on this page.

### advanced/checkboxes.md

- Stripped full-width periods "。" from headings and frontmatter.
- No other issues found.

### advanced/textfields.md

- Stripped full-width periods "。" from headings and frontmatter.
- Minor inline_code count mismatch (3 extra spans) — cosmetic only, no content impact.
- No glossary terms flagged on this page.

### advanced/select-lists.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed broken markdown links.
- Translated two untranslated segments by hand (CSV format paragraph, select title style paragraph).
- Minor inline_code count mismatch (2 extra spans) — cosmetic only.
- No glossary terms flagged on this page.

### advanced/item-lists.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed frontmatter title "物品清单" → "项目列表" to match sidebar label.
- Minor inline_code count mismatch (2 extra spans) — cosmetic only.
- No glossary terms flagged on this page.

### advanced/timer-progress.md

- Stripped full-width periods "。" from headings and frontmatter.
- No other issues found.

### advanced/info-box.md

- Stripped full-width periods "。" from headings and frontmatter.
- No other issues found.

### advanced/banner-images.md

- Stripped full-width periods "。" from headings and frontmatter.
- Fixed garbled translation of `--bannertitle` paragraph (was "使用“. ”。").
- Fixed broken link in `--bannertitle` paragraph (wrong URL target and `]` → `)`).
- Translated untranslated paragraph about `--title` vs `--bannertitle` by hand.
- No glossary terms flagged on this page.

### advanced/background-images.md

- Stripped full-width periods "。" from headings and frontmatter.
- Translated untranslated `fill`/`fit` paragraph by hand.
- No glossary terms flagged on this page.

### advanced/layout.md, advanced/presentation.md, advanced/notifications.md, advanced/workflows.md

- Stripped full-width periods "。" from headings and frontmatter.
- workflows.md: translated untranslated `branch.field` paragraph by hand.
- No glossary terms flagged on these pages.

### advanced/full-screen.md, advanced/window-size.md

- Stripped full-width periods "。" from headings and frontmatter.
- window-size.md: had untranslated segments, fixed.
- No glossary terms flagged on these pages.

### advanced/inspect-mode.md and all advanced/inspect/preset*.md, ipc-contract-gap-analysis.md, cadence-mdm-deployment.md

- Stripped full-width periods "。" from headings and frontmatter.
- cadence-mdm-deployment.md: translated untranslated "Hybrid drive" paragraph by hand.
- No glossary terms flagged on these pages.

### builder/builder.md, builder/buttons.md, builder/checkboxes.md, builder/icon.md, builder/images.md, builder/listitems.md, builder/media.md, builder/message.md, builder/sidebar.md, builder/textfields.md, builder/window.md, builder/title.md

- Stripped full-width periods "。" from headings and frontmatter.
- builder/icon.md: translated untranslated paragraph about SF Symbol picker by hand.
- No glossary terms flagged on these pages.

### examples/demo-scripts.md, examples/jamf-scripts.md, examples/jamfhelper.md, examples/nudge-update.md, examples/shell-commands.md, examples/showcase.md

- Stripped full-width periods "。" from headings and frontmatter.
- demo-scripts.md, jamfhelper.md, showcase.md: had untranslated segments, fixed.
- No glossary terms flagged on these pages.

### operation/authorization.md, operation/builtin-variables.md, operation/capturing-output.md, operation/command-q.md, operation/dialogcli.md, operation/exit-codes.md, operation/gotchas.md, operation/help-message.md, operation/login-window.md, operation/preferences.md

- Stripped full-width periods "。" from headings and frontmatter.
- authorization.md: translated untranslated `au.csiro.dialog` paragraph by hand.
- capturing-output.md: translated untranslated `sdtout` paragraph by hand.
- dialogcli.md: translated untranslated `--link` flag paragraph by hand.
- workflows.md (advanced): translated untranslated `branch.field` paragraph by hand.
- No glossary terms flagged on these pages.

### reference/builder.md, reference/contributing.md, reference/updates.md, reference/whats-new.md, reference/releasenotes/sd3-0-0.md, sd3-0-1.md, sd3-1-0.md, sd3-1-1.md

- Stripped full-width periods "。" from headings and frontmatter.
- No glossary terms flagged on these pages.

### basic-use/images.md, advanced/command-file.md, advanced/inspect-mode.md, advanced/json-configuration.md

- Stripped full-width periods "。" from headings and frontmatter.
- inspect-mode.md: translated untranslated `iconBasePath` aside tip paragraph by hand.
- No glossary terms flagged on these pages.

## Systematic issues fixed across all pages

- Full-width Chinese period "。" stripped from all headings and frontmatter `title`/`description` lines (67 files).
- Broken markdown links `](url)]` → `](url)` fixed (12 files).
- "物品清单" → "项目列表" for consistency with sidebar label (2 files).

## Reviewer notes

- All 77 English pages (including index.mdx) have been translated into zh-hans.
- The quick-start bash code block in index.mdx was translated by hand following the de/fr/ja pattern.
- Glossary check: 0 slips, 0 translations need checking.
- Build: passes cleanly (463 pages).
- Remaining work for native-speaker reviewers: check tone and register consistency across all pages; verify technical accuracy of translated command examples; check that all internal links resolve correctly.

## Reviewer feedback

None yet.
