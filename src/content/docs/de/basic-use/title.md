---
title: Anpassen des Titels.
description: Erfahren Sie, wie Sie den Titeltext und die Schriftart-Eigenschaften in swiftDialog festlegen und anpassen können.
---

## Einstellungen: Titeltext.

Verwenden Sie die Befehlszeilenoption `-t` oder `--title`, um anzugeben, was Sie im Titelbereich des Dialogfensters anzeigen möchten.

Beispiel:

`--title "An Important Message"`

`-t "An Important Message"`

Der Titelbereich ist ein fest definierter, fetter Bereich am oberen Rand des Dialogfensters. Text, der länger ist als die Breite des Fensters, wird abgeschnitten.

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## Anpassen der Schriftart-Eigenschaften für Titel.

Verwenden Sie die `--titlefont` Kommandozeilenoption, um die Schriftart-Eigenschaften für den Titel festzulegen.

### CSV-Syntax.

Die Eigenschaften einer Schriftart werden in Form von `property=value` ausgedrückt, und mehrere Eigenschaften werden durch ein Komma voneinander getrennt.

Folgende Eigenschaften können angepasst werden:
 * `colour=<hex_value>` (alternativ `color=<hex_value>`)
   * angegeben im Hexadezimalsystem, z.B. #00A4C7.
 * `size=<float>`
   * Akzeptiert jeden Gleitkommawert, z. B. 30, 65, 72,3.
 * `weight=<text>`
   * Akzeptiert eine der folgenden Schriftstärken: dünn, leicht, normal, mittel, fett oder fett (Standard).
 * `name=<fontname>`
   * Akzeptiert einen Schriftnamen oder eine Schriftfamilie. Eine Liste der verfügbaren Namen kann mit `--listfonts` oder durch die Verwendung der macOS-Anwendung "Schriftbuch" ermittelt werden.
 * `alignment=[left|right]`
   * Platziert den Titeltext linksbündig oder rechtsbündig.
 * `offset=<float>`
   * Verschiebt den Titeltext horizontal um die angegebene Anzahl von Punkten. Positive Werte verschieben den Text nach rechts, negative Werte nach links. Wenn `alignment=right` verwendet wird, wird die Verschieberichtung automatisch umgekehrt, sodass ein positiver Wert den Text weiterhin in Richtung des rechten Rands verschiebt.
 * `shadow`
   * Fügt einen Schlagschatten zum Text hinzu (boolescher Wert, kein Wert erforderlich).

 > **ACHTUNG:** Seien Sie vorsichtig, wenn Sie Schriftnamen und Schriftstärken kombinieren. Wenn Sie eine Schriftart oder Schriftfamilie anhand ihres Namens angeben, sind möglicherweise nicht alle Schriftstärken verfügbar. In diesem Fall wird die angegebene Schriftstärke ignoriert.

Sie können eines oder mehrere dieser Elemente verwenden, und die Reihenfolge, in der sie angegeben werden, ist nicht wichtig. Wenn Sie beispielsweise nur die Größe ändern möchten, könnten Sie Folgendes verwenden:

`--titlefont "size=60"`

Beispiel 1: `--titlefont "colour=#00A4C7,weight=light,size=60"`

Dieses Beispiel setzt die Farbe auf den Wert `#00A4C7`, die Stärke auf `light` und die Schriftgröße auf `60` und wird wie folgt dargestellt:

<img width="400" alt="image" src="/images/titlefont1.png" />

Beispiel 2: `--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

Dieses Beispiel setzt die Farbe auf den Wert `#D054A0 `, die Größe auf `40` und verwendet den Schriftnamen "Chalkboard-Bold":

<img width="400" alt="image" src="/images/titlefont2.png" />

Beispiel – Ausrichtung: links/rechts.

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### JSON-Objekt-Syntax.

Ab Version 3.1.1 können `--titlefont` und `--messagefont` auch als JSON-Objekte angegeben werden, um eine direktere Steuerung zu ermöglichen:

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**Eigenschaften:**
- `name` - Schriftname oder Schriftfamilie.
- `size` - Schriftgröße in Punkten.
- `colour` / `color` - Textfarbe (in Hexadezimaldarstellung oder als Farbname).
- `weight` - Schriftstärke: `thin`, `light`, `regular`, `medium`, `heavy`, `bold`
- `alignment` - Textausrichtung: `left`, `right` (nur für Überschriften)
- `offset` - Horizontale Verschiebung in Punkten (nur für den Titel).
- `shadow` - Schlagschatten hinzufügen (Boolesch).

**Beispiele:**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**Hinweis:** Der Schlüssel `shadow` wird jetzt im JSON-Format unterstützt (vorher war er nur im CSV-Format verfügbar).

### Die Verwendung von Farben im Titel.

Die Verwendung von `colour=<value>` legt die Grundfarbe des Textes fest, jedoch können Sie die Farbe einzelner Wörter oder Buchstaben mithilfe des Formats `:colour[text]` ändern.

Beispiel:

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## Untertitel.

Verwenden Sie `--subtitle <text>`, um eine zusätzliche Textzeile unterhalb des Titels anzuzeigen, wobei die gleiche Schriftart in einer kleineren Größe verwendet wird.

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

Der Untertitel übernimmt den gleichen Schriftnamen, die gleiche Schriftstärke und die gleiche Farbe wie der Titel, wird aber in einer anderen Größe dargestellt. `titlefont size − 10pt`

#### Verbergen des Titelbereichs.

Verwenden Sie das Schlüsselwort `none`, um den Titelbereich auszublenden. Dadurch wird die Titelleiste sowie die horizontale Trennlinie entfernt.

e.g. `--title none`




