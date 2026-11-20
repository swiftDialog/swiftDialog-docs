---
title: Markdown-Unterstützung
description: Erfahren Sie, wie Sie die Markdown-Formatierung in Nachrichten von swiftDialog verwenden können.
---

## Unterstützung für Markdown

Sie können Markdown in Ihrem Nachrichtentext verwenden, um die Darstellung anzupassen.

Die unterstützte Markdown-Formatierung entspricht dem Stil von GitHub. Tabellen, Einrückungen, Codeblöcke usw. werden unterstützt.

<img width="500" alt="Screenshot 2023-08-10 at 9 06 14 am" src="https://github.com/bartreardon/swiftDialog/assets/3598965/5fd6bb4a-a5b6-46c3-9fc9-7beace658420">

### Zeilenumbrüche

In Markdown führt die [Definition⟧ ](https://daringfireball.net/projects/markdown/syntax#p) dafür, wie Absätze und Zeilenumbrüche behandelt werden, dazu, dass ein einzelnes Zeichen `\n` nicht ausreicht, um eine neue Zeile zu erstellen. Eine Zeile sollte mit **zwei Leerzeichen** enden, gefolgt von einem Zeilenumbruch `\n`, oder Sie können einen neuen Absatz durch ein doppeltes Zeilenumbruchzeichen `\n\n` erzwingen.

Sie können das `<br>`-Tag auch verwenden, um einen Zeilenumbruch zu kennzeichnen, der dann als `  \n` (`[space][space]\n`) interpretiert wird.

### Farbverlängerungen

swiftDialog 3+ enthält Erweiterungen zur Unterstützung von Farbcodierungen innerhalb des Textes. Die Syntax dafür ist:

```
colour:[Text here]
```

Zum Beispiel, wenn Sie grünen Text wünschen, könnten Sie `green:[My green text here]` verwenden.

Hexadezimalwerte werden ebenfalls unterstützt, z. B. `:a62991[Colourful Text]`.

Sie können mehrere Farben kombinieren, z. B. `--message ":e74c3c[scarlet], :e67e22[tangerine], :f1c40f[gold], :2ecc71[emerald], :3498db[sapphire], and :9b59b6[amethyst]"`.

<img width="400" alt="image" src="/images/markdown_colour.png" />

### Beispiele:

`dialog --message "Line 1  \nLine2  \nLine 3\n\nParagraph 2"`

`dialog --message "Line 1<br>Line2<br>Line 3<br><br>Paragraph 2"`

`dialog --message "Text can include **bold** and _italics_`

`dialog --message "### Heading 3"`

`dialog --message " * point 1\n * point 2\n * point 3"`

`dialog --message "[A link that will open in the default browser](https://some.link.com/)"`

`dialog --message "\![Inline images are also supported](https://upload.wikimedia.org/wikipedia/commons/8/85/Logo-Test.png)"`

**Vorsicht:** Wenn Sie Inline-Bilder verwenden, müssen Sie das führende `!` durch `\!` ersetzen, andernfalls könnte Ihre Shell dies als einen Befehl interpretieren.

