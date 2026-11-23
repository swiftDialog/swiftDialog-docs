---
title: Anpassen des Nachrichtenbereichs
description: Erfahren Sie, wie Sie den Nachrichten-Text, die Schrifteigenschaften und die Positionierung in swiftDialog einstellen und anpassen können.
translationSynced: 2026-11-23T08:35:52+00:00
---

Verwenden Sie die Kommandozeilenoption `-m` oder `--message`, um anzugeben, was Sie im Nachrichtenbereich des Dialogfensters anzeigen möchten.

Beispiel:

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

Der Nachrichtenbereich kann entweder 2/3 der Breite des Dialogfensters einnehmen oder die volle Breite, falls der Bereich mit den Icons nicht angezeigt wird.

Nachrichten werden automatisch umbrochen, wenn sie die Breite des Anzeigebereichs überschreiten, und sie werden gescrollt, wenn sie die gesamte verfügbare Anzeigefläche übersteigen.


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### Inhalte bereitstellen

Zusätzlich zur Übergabe einer Zeichenkette können Sie stattdessen den Pfad oder die URL zu einer Markdown-Datei übergeben. Jede Datei, die mit `.md` endet, wird als Markdown-Quelldatei behandelt.

Beispiel:

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## Nachrichten-Positionierung

`--messagealignment` und `--messageposition` ermöglichen es, festzulegen, an welcher Stelle im Dialog die Nachricht angezeigt wird. Dies ist nützlich, um Dialoge zu erstellen, in denen die Nachricht sowohl vertikal als auch horizontal zentriert ist.

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## Schriftart, Farbe, Größe und Ausrichtung der Nachricht anpassen

`--alignment [left | centre | center | right]`

Legen Sie die Ausrichtung der Nachricht fest. Standard ist 'left'.

`--messagefont <text>`

Ermöglicht die Änderung der Schriftart, der Textgröße und der Farbe der Nachricht.

`color,colour=<text><hex>`

> `<text>` kann eine der Standardfarben von Apple sein: `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Wenn die angegebene Option ungültig ist, wird standardmäßig die primäre Systemfarbe verwendet (normalerweise `black` im hellen Modus oder `white` im dunklen Modus).

> `<hex>` wird im Hexadezimalsystem angegeben, beispielsweise #00A4C7.

`size=<float>` akzeptiert jeden Gleitkommawert (z. B. 15.7, 20, 32.0)

`name=<fontname>` - Akzeptiert den Namen jeder installierten Schriftart.


Beispiel: `--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### Zusätzliche Farben in der Nachricht verwenden

Die Verwendung von `colour=<value>` legt die Grundfarbe der Nachricht fest. Sie können jedoch die Farbe einzelner Wörter oder Buchstaben mithilfe des Formats `:colour[text]` festlegen.

Beispiel:

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

