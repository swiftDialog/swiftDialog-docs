---
title: Schaltflächen und deren Funktionalität
description: Lernen Sie, wie Sie die Beschriftung, die Funktionen und das Verhalten von Schaltflächen in swiftDialog konfigurieren können.
---

Das Dialogfenster kann bis zu drei Schaltflächen anzeigen.

Die Schaltflächen werden im unteren Bereich des Dialogfensters angezeigt.

![Dialog-Schaltflächenbereich](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## Schaltfläche 1 – Die Standardschaltfläche
Standardmäßig wird ein einzelner Button mit der Beschriftung "**OK**" angezeigt. Der Standard-Button ist immer vorhanden, ist mit der Taste **_Enter_** verknüpft und beendet die Dialog-Anwendung mit dem Exit-Code `0`.

Die Beschriftung der Standard-Schaltfläche kann mit einer beliebigen Menge an Text geändert werden, wobei die `--button1text`-Option verwendet wird.

e.g. `--button1text "Enter to Continue"`

![Text für Schaltfläche 1 ](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

Die Aktion kann auch mithilfe der `--button1action`-Option angepasst werden, sodass Sie neben dem einfachen Beenden der Dialog-App auch andere Aktionen ausführen können.

In diesem Stadium beschränken sich die Aktionen auf das Öffnen einer URL im Standard-Webbrowser des Benutzers.

e.g. `--button1action "https://github.com/"`

## Schaltfläche 2 – Die Abbruchschaltfläche
Der zweite Button ist standardmäßig ausgeblendet. Er kann durch die Optionen `-2` oder `--button2` aktiviert werden, wodurch der Button mit der Standardbezeichnung "**Abbrechen**" angezeigt wird. Der zweite Button ist der Taste **_Esc_** zugeordnet und beendet die Dialog-Anwendung mit dem Exit-Code `2`.

Die Beschriftung des zweiten Buttons kann mit einer beliebigen Textmenge geändert werden, wobei die Option `--button2text` verwendet wird. Wenn Sie diese Option verwenden, müssen Sie die Option `--button2` nicht aktivieren. Die Anzeige des Buttons erfolgt automatisch, wenn Sie die Textbeschriftung ändern.

Beispiel:

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![Button 2 Ich habe keine Präferenz. ](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

Der zweite Button hat keine weiteren Funktionen implementiert.

## Der Button für weitere Informationen
Der Button "Mehr Informationen" ist standardmäßig ausgeblendet. Er kann über die Optionen `-3` oder `--infobutton` aktiviert werden, wodurch der Button mit der Standardbeschriftung "**Mehr Informationen**" angezeigt wird. Durch Klicken auf den Button wird swiftDialog mit einem Exit-Code von `3` beendet.

Wenn das Argument `--infobuttonaction` vorhanden ist, führt ein Klick auf den Button "Weitere Informationen" nur die Aktion `--infobuttonaction` aus, und das Dialogfenster "swiftDialog" schließt nicht automatisch. Wenn das Argument `--quitoninfo` hinzugefügt wird, wird das Standardverhalten beim Schließen wiederhergestellt.

Die Beschriftung des Info-Buttons kann mit einer beliebigen Textmenge geändert werden, wobei die Option `--infobuttontext` verwendet wird. Wenn Sie diese Option verwenden, müssen Sie die Option `--infobutton` nicht aktivieren. Die Anzeige des Buttons ist automatisch gegeben, wenn Sie die Textbeschriftung ändern.

Beispiel:

`--infobuttontext "Click here for more details"`

![Text auf dem Info-Button: Klicken Sie für weitere Details.](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

Die Aktion kann auch mithilfe der `--infobuttonaction`-Option angepasst werden, sodass Sie neben dem einfachen Beenden der Dialog-App auch andere Aktionen ausführen können.

In diesem Stadium beschränken sich die Aktionen auf das Öffnen einer URL im Standard-Webbrowser des Benutzers.

e.g. `--infobuttonaction "https://github.com/"`

## Symbole für Schaltflächen

Legt das SF-Symbol fest, das zusätzlich zur Beschriftung des Buttons verwendet werden soll.

### CSV-Syntax

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

Nimmt den Namen eines SF-Symbols als Argument entgegen.

Optionale Eigenschaften, die als kommagetrennte Werte (in beliebiger Reihenfolge) angegeben werden können:
 - Position: eine von folgenden Optionen: linksbündig, rechtsbündig, oben, unten – Standardeinstellung: linksbündig.
 - Darstellungsmodus: einer der folgenden: hierarchisch, monochrom, mehrfarbig, Palette – Standardeinstellung: monochrom.
 - Palette: Fügen Sie zwei oder drei Farben im Format "palette=Farbe1-Farbe2-Farbe3" hinzu.
   - z.B. Farbpalette = Rot-Grün-Blau.
 - Größe: im Format Größe=<num>
 - Farbe: im Format Farbe=<text|hex>
   - Wenn der Mehrfarben-Darstellungsmodus aktiviert ist, wird die Farbe ignoriert.

Beispiel:

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### JSON-Objekt-Syntax

Ab Version 3.1.1 können Buttonsymbole auch als JSON-Objekte definiert werden, um eine direktere Steuerung zu ermöglichen.

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**Eigenschaften:**
- `name` - Name des SF-Symbols (erforderlich).
- `position` - Symbolposition: `leading`, `trailing`, `top`, `bottom` (Standardwert: `leading`)
- `colour` / `color` - Symbolfarbe (in Hexadezimaldarstellung oder als Name).
- `size` - Symbolgröße in Punkten.
- `rendering` - Rendering-Modus: `hierarchical`, `monochrome`, `multicolour`, `palette`
- `palette` - Array mit 2 bis 3 Farben für mehrfarbige Symbole (durch Kommas getrennt in CSV-Dateien, als Array in JSON-Dateien).

**Beispiele:**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**Hinweis:** Wenn Sie `rendering: palette` verwenden, muss die Farbpalette ein Array im JSON-Format sein: `["red","green","blue"]`. In CSV-Form verwenden Sie Bindestriche zur Trennung: `palette=red-green-blue`.

## Knopfposition

Standardmäßig befinden sich Schaltfläche 1 und Schaltfläche 2 auf der rechten Seite, während die Info-Schaltfläche sich auf der linken Seite befindet.

Die Verwendung von `--buttonstyle center` platziert die Schaltflächen 1 (und 2, falls vorhanden) in der unteren Mitte des Dialogfensters.

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` und `--infotext` sind nicht kompatibel, wenn die Option `--buttonstyle center` verwendet wird.

## "Stack"-Layout für Schaltflächen

`--buttonstyle stack`

Zeigt Schaltfläche 1 und Schaltfläche 2 in einer gestapelten Anordnung an, die die gesamte Breite ausfüllt.

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` und `--infotext` sind nicht kompatibel, wenn die Option `--buttonstyle stack` verwendet wird.

## Verhalten der Tasten `[return]` und `[enter]`

Da es keine Eingabefelder gibt, ist das fokussierte Eingabefeld im Dialogfenster `button1`, und sowohl `[enter]` als auch `[return]` aktivieren den Button, da dies das einzige interaktive Element im Fenster ist und somit standardmäßig den Fokus der Tastatur hat. Die Folge davon ist, dass das Dialogfenster geschlossen wird (vorausgesetzt, der Button ist aktiv und nicht deaktiviert).

Die Taste `[return]` aktiviert immer den Button "Button1", es sei denn, ein Eingabefeld hat den Fokus. Die Taste `[enter]` aktiviert nur das Element, das gerade den Fokus hat (deshalb funktioniert sie, um einen Dialog in Fenstern ohne Eingabeelemente zu schließen).

In einem Textfeld für eine einzelne Zeile, `[return]` kann keine neue Zeile einfügen, sodass die Standardaktion greift und das Dialogfenster schließt (die Standardaktion wird aktiviert). Im Gegensatz dazu hat `[enter]` keine Wirkung, da es ebenfalls keine neue Zeile einfügen kann, aber da es keinen Einfluss auf die Standardaktion hat, passiert nichts.

In einem mehrzeiligen Textfeld (d. h. `--textfield` mit `editor` aktiviert), kann die Taste `[return]` einen Zeilenumbruch einfügen, und diese Aktion hat Vorrang vor jeder anderen Standardzuweisung (d. h. die Aktion, die normalerweise durch Drücken von Button1 ausgelöst wird, nämlich das Schließen des Fensters). Die Taste `[return]` funktioniert ebenfalls wie erwartet und fügt einen neuen Zeilenumbruch ein.

### Das Ändern des Standardverhaltens von `[return]`, `[enter]` oder `[esc]`

Wenn Sie das Standardverhalten von `[return]`, `[enter]` oder `[esc]` nicht wünschen, dass das Dialogfenster geschlossen wird, können Sie die Option `--hidedefaultkeyboardaction` verwenden, um dieses Verhalten zu ändern. Diese Option ändert die Standardtasten `[return]` oder `[escape]` so, dass auch die Kombination `cmd`+`shift` erforderlich ist, um die Funktion auszulösen. Dies hilft, unbeabsichtigtes Schließen von Dialogfenstern zu verhindern.

## Rückgabecodes

Die folgenden Rückgabecodes werden nach jeder Aktion gesendet. Diese können ignoriert oder in einem aufrufenden Skript für weitere Aktionen verwendet werden.

| Schaltflächenname | Optional | Hotkey | Rückgabecode |
| ----------- | -------- | ------ | ----------- |
| Schaltfläche 1     | Nein       | Enter  | 0           |
| Schaltfläche 2     | Ja      | Esc    | 2           |
| Info-Schaltfläche  | Ja      |        | 3           |

## Schaltflächen deaktivieren

Schaltfläche 1 und Schaltfläche 2 können beim Start deaktiviert werden, und zwar mit einem der folgenden Befehle:

`--button1disabled`

`--button2disabled`

Schaltfläche 1 kann vollständig ausgeblendet werden, indem der Buttontext auf `none` gesetzt wird.

_Bitte beachten Sie, dass dies auch die Verwendung der [Return]-Taste zum Schließen eines Dialogfensters deaktiviert. Stellen Sie daher sicher, dass es eine Möglichkeit gibt, das Dialogfenster zu schließen._