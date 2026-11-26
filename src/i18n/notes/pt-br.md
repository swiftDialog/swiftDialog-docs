# Portuguese (pt-BR) translation notes

## Style decisions

- **Register:** "você" throughout (informal but standard Brazilian Portuguese for admin docs). Imperative mood for instructions: "Use a sua experiência", "digite uma palavra ou frase", "Clique em ...". Not "tu".
- **Apple reference (2026-11-25):** Read https://support.apple.com/pt-br/guide/deployment/welcome/web and https://support.apple.com/pt-br/guide/terminal/welcome/mac.
- Findings:
  - **Second-person "você":** "para que você gerencie facilmente seus projetos", "digite uma palavra ou frase no campo de busca". Admin and end-user pages use the same register.
  - **Short active imperatives:** "Use a sua experiência com scripts", "Clique em ...". Explanations use "Você pode … ao …".
  - **UI labels:** not bolded; quoted only when needed for clarity.
  - **Terms:** botão (on-screen button), tecla (keyboard key), ícone (icon), menu (menu), caixa de seleção (checkbox), campo de texto (text field), Janela de Início de Sessão (login window), computadores Mac (Mac computers), administrador (administrator), pacote/instalador (package/installer), política (policy), perfil de configuração (configuration profile), script (kept), comando (command), linha de comando (command line), Apple Silicon (kept in English).
- Numbers users typed keep the decimal point (`15.7`, never `15,7`): swiftDialog parameters are comma-separated.
- Default button labels follow the app's localisation for pt-BR (`pt-BR.lproj` / `pt_BR.lproj`): copy from `swiftDialog/dialog/extras/Localisations/`, not a free translation.
- `--vieworder` CSV values (`textfile`, `webcontent`, `listitem`, `checkbox`, `textfield`, `radiobutton`, `dropdown`) are user-typed command values and stay in English.

## Notes for reviewers

All 76 English pages have been translated to pt-BR. Build passes. Glossary check: 0 slips requiring action (all 57 flagged words are correct in context — "tecla" = keyboard keys, "símbolo" = SF Symbols, "regra" = workflow/IPC rules).

Pages reviewed and fixed during translation:
- getting-started/introduction: fixed broken markdown links, "dialog" → "caixa de diálogo" (not "função de diálogo"), decimal comma "72,3" → "72.3".
- getting-started/installation: fixed "Homebrew" → "Homebrew" (was "produção caseira"), removed double `]]` on external link.
- basic-use/title: fixed heading "Título da configuração" → "Definindo o título", decimal comma, font-weight values kept in English, alignment "à esquerda" → `left`.
- basic-use/message: fixed decimal comma "15,7"/"32,0" → "15.7"/"32.0", alignment "à esquerda" → `left`.
- basic-use/icon: fixed "símbolos de segurança animados" → "símbolos SF animados", "Teclas suportadas" → "Chaves suportadas" (JSON keys), weight/animation values kept in English, double `]]` on external link, TOC anchors.
- basic-use/buttons: fixed CSV position/rendering values kept in English, `palette`/`size` parameter names kept, "Entrar" → "Enter" in table, missing periods.
- basic-use/video: fixed "conversa" → "caixa de diálogo" (glossary violation), "Quicktime" → "QuickTime".
- advanced/layout: fixed --vieworder CSV values (user-typed, kept in English: textfile, webcontent, listitem, checkbox, textfield, radiobutton, dropdown).
- advanced/timer-progress: fixed "conversa" → "caixa de diálogo" (glossary violation).
- advanced/command-line-options: fixed untranslated "See [Full Screen] and [Presentation] for details." sentence.
- advanced/command-file: fixed "## Quit" → "## Sair".
- advanced/info-box: translated image alt text.
- advanced/inspect/cadence-mdm-deployment: translated "Hybrid drive" paragraph.
- advanced/notifications: translated image alt text, fixed double `]]` on image link.
- advanced/select-lists: translated "Sets the display style..." paragraph.
- advanced/workflows: fixed "Confirm branch.field matches..." → Portuguese.
- builder/checkboxes: fixed "#### Disabled" → "#### Desabilitado".
- builder/window: fixed "#### Moveable" → "#### Pode ser movido".
- examples/showcase: fixed title "Showcase" → "Vitrine", translated untranslated link descriptions, fixed `]:` → `](` on a link.
- operation/builtin-variables: translated variable descriptions.
- reference/updates: fixed "conversas" → "caixas de diálogo" (glossary violation).

Items for a native speaker to verify:
- Register "você" consistency across all 76 pages.
- Default button labels ("OK", "Cancelar", "Mais informações") match the app's pt-BR localisation.
- Term "caixa de diálogo" vs "dialog" usage consistency.
- TOC anchor links in icon.md work (slugs with accents stripped).
- Inline-code structure mismatches reported by the draft script (minor line-position shifts in textfields, notifications, sd3-0-0, ipc-contract-gap-analysis, jamfhelper) — these don't break the build but a native speaker may want to confirm inline code formatting is preserved.

## Reviewer feedback

None recorded yet.
