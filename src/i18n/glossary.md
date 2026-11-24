# Translation glossary

These terms have one precise meaning in the swiftDialog docs. Translate them by that meaning, not by the everyday sense of the English word, and translate each one **the same way on every page**.

Each entry has:
- **Means**: what the term refers to in these docs. This part is language-neutral and is the source of truth.
- **Not**: everyday senses of the English word that must not leak into a translation.
- **Rule**, when the term needs special handling.
- One line per language with the preferred translation (`de:`, `fr:` …). A language with no line hasn't decided yet. Pick a translation, use it consistently, and add the line here.

Text in `code` is never translated, whatever this glossary says. See TRANSLATING.md.

## Keep in English

Product, feature and Apple names stay as they are in every language:

swiftDialog · Dialog (the app, `Dialog.app`) · Inspect Mode · the preset names (Deployment, Cards, Compact List, Toast, Unified, Guidance) · SF Symbols · Markdown · Jamf Pro · jamfHelper · Nudge · MDM · macOS · SwiftUI · Apple Silicon

## Terms

### dialog
- **Means:** the window swiftDialog shows on screen, created by running the `dialog` command. It's the subject of almost every page.
- **Not:** a conversation, an exchange between people, or dialogue in the literary sense.
- **Rule:** "Dialog" with a capital D and no article, or `Dialog.app`, is the product name; keep it. "dialog window" refers to the window frame, e.g. its size or position.
- de: Dialog. "dialog window" → Dialogfenster. Not "Dialogfeld".
- fr: boîte de dialogue. "dialog window" → fenêtre de dialogue. Not "conversation".
- ja: ダイアログ. "dialog window" → ダイアログウィンドウ. Not "会話" (conversation).

### message
- **Means:** the main body text of a dialog, set with `--message`. "Message area" is the part of the dialog where it appears.
- **Not:** a chat message, email or notification.
- de: Nachricht. "message area" → Nachrichtenbereich.
- fr: message. "message area" → zone de message.
- ja: メッセージ. "message area" → メッセージ領域.

### title
- **Means:** the heading text at the top of a dialog, set with `--title`.
- **Not:** a job title or a book title.
- de: Titel
- fr: titre
- ja: タイトル

### icon
- **Means:** the image shown on the left of a dialog (`--icon`), or in a notification or list item. It can be an image file, an app icon or an SF Symbol.
- **Not:** a symbol in the general sense. Many languages translate "icon" as "symbol", which clashes with SF Symbols, also a frequent term in these docs.
- **Rule:** use a word that can't be confused with SF Symbols.
- de: Icon. Not "Symbol" (reserved for SF Symbols).
- fr: icône. Not "symbole" (réservé aux SF Symbols).
- ja: アイコン. Not "シンボル" (SF Symbols用).

### overlay icon
- **Means:** a small second image drawn over the bottom-right corner of the icon (`--overlayicon`).
- de: Overlay-Icon
- fr: icône de superposition
- ja: オーバーレイアイコン

### button
- **Means:** a clickable on-screen control in the dialog (`--button1text`, `--button2text`, `--infobuttontext`).
- **Not:** a keyboard key or a physical button.
- de: Schaltfläche. Not "Taste", "Knopf", "Knöpfe" or "Button".
- fr: bouton. Not "touche" or "bouton physique".
- ja: ボタン. Not "キー" or "押しボタン".
- **Rule:** a default button label in quotes ("OK", "Cancel", "More Information") is the text the app shows, so copy it from the app's localisation for that language (`swiftDialog/dialog/extras/Localisations/<lang>.lproj/Localizable.strings`), not a free translation. If the app has no localisation for the language, keep the English label.

### info button
- **Means:** the optional extra button, usually bottom-left, set with `--infobuttontext`.
- de: Info-Schaltfläche
- fr: bouton d'info
- ja: 情報ボタン

### info box
- **Means:** the panel of extra text shown below the icon (`--infobox`).
- de: Infobox
- fr: encadré d'info
- ja: 情報ボックス

### checkbox
- **Means:** a tick-box input in the dialog (`--checkbox`).
- de: Kontrollkästchen
- fr: case à cocher
- ja: チェックボックス

### text field
- **Means:** a single-line text input in the dialog (`--textfield`).
- de: Textfeld
- fr: champ de texte
- ja: テキストフィールド

### select list
- **Means:** a drop-down or radio-button choice in the dialog (`--selectvalues`).
- de: Auswahlliste
- fr: liste de sélection
- ja: 選択リスト

### item list
- **Means:** a list of rows showing items with a status, such as apps being installed (`--listitem`).
- de: Elementliste
- fr: liste d'éléments
- ja: 項目リスト

### banner
- **Means:** an image or coloured strip across the top of a dialog (`--bannerimage`).
- **Not:** an advertising banner or a flag.
- de: Banner
- fr: bannière
- ja: バナー

### progress bar
- **Means:** the bar showing progress through a task (`--progress`).
- de: Fortschrittsbalken
- fr: barre de progression
- ja: 進捗バー

### command file
- **Means:** a text file that swiftDialog watches while it runs. A script writes commands to it to update the open dialog (`--commandfile`).
- **Not:** a script file, or "the command line".
- de: Befehlsdatei
- fr: fichier de commandes
- ja: コマンドファイル

### key
- **Means:** the name of a field in JSON, a command-file command or a list of settings, e.g. "the `colour` key" or "supported keys". In "map keys" it is the value a choice is compared against.
- **Not:** a key on the keyboard, or a key that unlocks something (encryption, licence).
- **Rule:** the key names themselves are code and stay in English. Only the word "key" is translated.
- de: Schlüssel. Not "Taste".
- fr: clé. Not "touche".
- ja: キー. Not "キーボードのキー".

### option
- **Means:** a command-line argument such as `--title` (also called "argument" or "flag" in the docs).
- **Not:** a choice in a menu or a select list.
- de: Option
- fr: option
- ja: オプション

### notification
- **Means:** a macOS system notification sent by swiftDialog (`--notification`), shown in Notification Center.
- **Not:** a general alert or message, or the dialog itself.
- de: Mitteilung. This is Apple's German term for macOS notifications.
- fr: notification. C'est le terme d'Apple pour les notifications macOS.
- ja: 通知. macOS用語に従う.

### exit code
- **Means:** the number `dialog` returns when it closes, which tells the calling script which button was pressed.
- de: Exit-Code
- fr: code de sortie
- ja: 終了コード

### login window
- **Means:** the macOS login screen. swiftDialog can display over it.
- **Rule:** follow Apple's term for the login screen in each language.
- de: Anmeldefenster
- fr: fenêtre d'ouverture de session (terme d'Apple pour l'écran de connexion)
- ja: ログインウィンドウ

### preset
- **Means:** one of the ready-made Inspect Mode layouts.
- **Rule:** individual preset names stay in English (see above). Translate only the word "preset" itself.
- de: Preset
- fr: préset
- ja: プリセット

### workflow
- **Means:** a sequence of dialogs or steps driven by a script.
- de: Workflow
- fr: workflow
- ja: ワークフロー

### installer package
- **Means:** the `.pkg` file from the releases page that installs swiftDialog.
- de: Installationsprogramm (".pkg-Installationsprogramm")
- fr: paquet d'installation. Not "programme d'installation" or "installateur".
- ja: インストーラー (".pkgインストーラー")

### policy (Jamf)
- **Means:** a Jamf Pro policy, the object that runs scripts or installs packages on managed Macs. Also used loosely for the equivalent in other MDMs.
- **Not:** a rule document, such as an acceptable use policy.
- de: Richtlinie
- fr: règle. Not "politique" (keep that for documents, such as an acceptable use policy).
- ja: ポリシー
