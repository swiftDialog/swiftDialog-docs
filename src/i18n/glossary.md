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

swiftDialog · Dialog (the app, `Dialog.app`) · Inspect Mode · the preset names (Deployment, Cards, Compact List, Toast, Unified, Guidance) · SF Symbols · Markdown · Jamf Pro · jamfHelper · Nudge · MDM · macOS · SwiftUI

## Terms

### dialog
- **Means:** the window swiftDialog shows on screen, created by running the `dialog` command. It's the subject of almost every page.
- **Not:** a conversation, an exchange between people, or dialogue in the literary sense.
- **Rule:** "Dialog" with a capital D and no article, or `Dialog.app`, is the product name; keep it. "dialog window" refers to the window frame, e.g. its size or position.
- de: Dialog. "dialog window" → Dialogfenster. Not "Dialogfeld".

### message
- **Means:** the main body text of a dialog, set with `--message`. "Message area" is the part of the dialog where it appears.
- **Not:** a chat message, email or notification.
- de: Nachricht. "message area" → Nachrichtenbereich.

### title
- **Means:** the heading text at the top of a dialog, set with `--title`.
- **Not:** a job title or a book title.
- de: Titel

### icon
- **Means:** the image shown on the left of a dialog (`--icon`), or in a notification or list item. It can be an image file, an app icon or an SF Symbol.
- **Not:** a symbol in the general sense. Many languages translate "icon" as "symbol", which clashes with SF Symbols, also a frequent term in these docs.
- **Rule:** use a word that can't be confused with SF Symbols.
- de: Icon. Not "Symbol" (reserved for SF Symbols).

### overlay icon
- **Means:** a small second image drawn over the bottom-right corner of the icon (`--overlayicon`).
- de: Overlay-Icon

### button
- **Means:** a clickable on-screen control in the dialog (`--button1text`, `--button2text`, `--infobuttontext`).
- **Not:** a keyboard key or a physical button.
- de: Schaltfläche. Not "Taste" or "Knopf".

### info button
- **Means:** the optional extra button, usually bottom-left, set with `--infobuttontext`.
- de: Info-Schaltfläche

### info box
- **Means:** the panel of extra text shown below the icon (`--infobox`).
- de: Infobox

### checkbox
- **Means:** a tick-box input in the dialog (`--checkbox`).
- de: Kontrollkästchen

### text field
- **Means:** a single-line text input in the dialog (`--textfield`).
- de: Textfeld

### select list
- **Means:** a drop-down or radio-button choice in the dialog (`--selectvalues`).
- de: Auswahlliste

### item list
- **Means:** a list of rows showing items with a status, such as apps being installed (`--listitem`).
- de: Elementliste

### banner
- **Means:** an image or coloured strip across the top of a dialog (`--bannerimage`).
- **Not:** an advertising banner or a flag.
- de: Banner

### progress bar
- **Means:** the bar showing progress through a task (`--progress`).
- de: Fortschrittsbalken

### command file
- **Means:** a text file that swiftDialog watches while it runs. A script writes commands to it to update the open dialog (`--commandfile`).
- **Not:** a script file, or "the command line".
- de: Befehlsdatei

### option
- **Means:** a command-line argument such as `--title` (also called "argument" or "flag" in the docs).
- **Not:** a choice in a menu or a select list.
- de: Option

### notification
- **Means:** a macOS system notification sent by swiftDialog (`--notification`), shown in Notification Center.
- **Not:** a general alert or message, or the dialog itself.
- de: Mitteilung. This is Apple's German term for macOS notifications.

### exit code
- **Means:** the number `dialog` returns when it closes, which tells the calling script which button was pressed.
- de: Exit-Code

### login window
- **Means:** the macOS login screen. swiftDialog can display over it.
- **Rule:** follow Apple's term for the login screen in each language.
- de: Anmeldefenster

### preset
- **Means:** one of the ready-made Inspect Mode layouts.
- **Rule:** individual preset names stay in English (see above). Translate only the word "preset" itself.
- de: Preset

### workflow
- **Means:** a sequence of dialogs or steps driven by a script.
- de: Workflow
