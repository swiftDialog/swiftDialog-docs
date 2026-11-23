---
title: Befehlszeilenoptionen
description: Vollständige Referenz für alle Befehlszeilenoptionen und -argumente von swiftDialog
translationSynced: 2026-11-23T08:35:52+00:00
---

Dialog kann über Befehlszeilenoptionen konfiguriert werden. Alle Optionen können auch über eine JSON-Konfigurationsdatei angegeben werden. ](/de/advanced/json-configuration)

```sh
dialog --title "Hello" --message "World"
```

Verwenden Sie `--help <option>`, um detaillierte Informationen zu einem bestimmten Argument zu erhalten.

---

## Inhalt

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--title <text>` | `-t` | Legen Sie den Titel des Dialogfensters fest. Verwenden Sie `none`, um es auszublenden. |
| `--subtitle <text>` | | Eine sekundäre Textzeile wird unterhalb der Überschrift angezeigt. Sie wird auch als Untertiteltext für [Benachrichtigungen](/de/advanced/notifications)] verwendet. |
| `--message <text>` | `-m` | Legen Sie die Dialognachricht fest. Unterstützt [Markdown](/de/basic-use/markdown). |
| `--messagealignment [left\|centre\|right]` | | Horizontale Ausrichtung der Nachricht |
| `--messageposition [top\|centre\|bottom]` | | Vertikale Positionierung des Inhaltsbereichs für die Nachricht |
| `--titlefont <params\|json>` | | Ändern Sie die Schriftart für die Überschrift. Akzeptiert entweder kommaseparierte Paare oder ein JSON-Objekt: `key=value`, `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow` |
| `--messagefont <params\|json>` | | Ändern Sie die Schriftart der Nachricht. Akzeptiert entweder kommaseparierte `key=value`-Paare oder ein JSON-Objekt |

Weitere Informationen finden Sie unter [Titel](/de/basic-use/title) und [Nachricht](/de/basic-use/message).

---

## Icon

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | Legen Sie das Dialog-Icon fest. Akzeptiert Dateipfade, URLs, SF-Symbole (`SF=name`), vordefinierte Elemente oder ein JSON-Objekt |
| `--iconsize <num>` | | Größe des Icons in Punkten (Standardwert: 150). |
| `--iconalpha <num>` | | Transparenz der Icons von 0,0 (transparent) bis 1,0 (opak). |
| `--iconalttext <text>` | | Beschriftung für die Barrierefreiheit des Icons |
| `--overlayicon <file\|url\|json>` | `-y` | Das Overlay-Bild wird unten rechts des Icons angezeigt. Es werden die gleichen Formate unterstützt wie bei `--icon` |
| `--hideicon` | `-h` | Verbergen Sie das Icon, um den Nachrichtenbereich zu vergrößern |
| `--centreicon` / `--centericon` | | Verschieben Sie das Icon so, dass es sich in der Mitte zwischen Titel und Text befindet |

Weitere Informationen finden Sie unter dem [Icon](/de/basic-use/icon)].

---

## Banner und Hintergrund

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | Zeigen Sie ein Bannerbild oben im Dialogfenster an |
| `--bannertitle <text>` | | Zeigt den Titeltext, der über das Banner gelegt ist |
| `--bannertext <text>` | | Entspricht dem Einstellen von `--bannertitle` und `--title` |
| `--bannerheight <num>` | | Legen Sie die Höhe des Banners fest |
| `--background <file>` | `-bg` | Ein Hintergrundbild oder ein Wasserzeichen festlegen |
| `--bgalpha <num>` | `-ba` | Transparenz des Hintergrundbildes (Standardwert: 0,5). |
| `--bgposition <position>` | `-bp` | Positionierung des Hintergrundbildes (z.B. `center`, `topleft`). |
| `--bgfill [fill\|fit]` | `-bf` | Füllmodus für Hintergrundbilder |
| `--bgscale [fill\|fit]` | `-bs` | Skalierungsmodus für das Hintergrundbild |
| `--screenbackground <file\|url>` | | Zeigen Sie ein Bild im Vollbildmodus hinter dem Dialogfenster an |

Weitere Informationen finden Sie unter [Bannerbilder](/de/advanced/banner-images) und [Hintergrundbilder](/de/advanced/background-images).

---

## Schaltflächen

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--button1text <text>` | | Beschriftung für Schaltfläche 1 (gebunden an die "Zurück"-Taste ↵, Standardwert: `OK`). |
| `--button1action <url>` | | URL, die beim Klicken auf Schaltfläche 1 geöffnet wird |
| `--button1shellaction <cmd>` | | Shell-Befehl, der ausgeführt wird, wenn Schaltfläche 1 angeklickt wird |
| `--button1symbol <sf symbol\|json>` | | SF-Symbol oder JSON-Objekt für Schaltfläche 1 |
| `--button1disabled` | | Startvorgang mit deaktivierter Schaltfläche 1 |
| `--button2` | `-2` | Schaltfläche 2 |
| `--button2text <text>` | | Beschriftung für Schaltfläche 2 (gebunden an die Escape-Taste ⎋, Standard: `Cancel`). |
| `--button2symbol <sf symbol\|json>` | | SF-Symbol oder JSON-Objekt für Schaltfläche 2 |
| `--button2disabled` | | Startvorgang mit deaktivierter Schaltfläche 2 |
| `--infobutton` | `-3` | Zeigen Sie den Info-Schaltfläche |
| `--infobuttontext <text>` | | Beschriftung für den Info-Schaltfläche |
| `--infobuttonaction <url>` | | URL, die geöffnet wird, wenn auf die Info-Schaltfläche geklickt wird |
| `--infobuttonsymbol <sf symbol\|json>` | | SF-Symbol oder JSON-Objekt für den Info-Schaltfläche |
| `--buttonstyle [center\|stack]` | | Anordnung und Gestaltung der Bedienelemente |
| `--buttonsize [mini\|small\|regular\|large]` | | Schaltflächengröße |
| `--buttontextsize <num>` | | Schriftgröße der Beschriftung auf Schaltflächen |
| `--quitoninfo` | | Dialog zur Beendigung, der angezeigt wird, wenn die Info-Schaltfläche ausgewählt wird |

Weitere Informationen finden Sie unter [Schaltflächen](/de/basic-use/buttons)].

---

## Ablauf

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--nextbuttontext <text>` | | Beschriftung für die Schaltfläche "Weiter" im Arbeitsablauf (Standard: `Next`). |
| `--previousbuttontext <text>` | | Beschriftung für die "Zurück"-Schaltfläche im Arbeitsablauf (Standard: `Previous`). |
| `--onadvance <command>` | | Shell-Befehl, der ausgeführt wird, wenn zwischen den Seiten eines Arbeitsablaufs gewechselt wird <br> (Eingabe erfolgt über die Standardeingabe; ein Exit-Code ungleich Null verhindert den Wechsel). |

Weitere Informationen finden Sie im Abschnitt [Workflow](/de/advanced/workflows)].

---

## Hilfemeldung

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--helpmessage <text>` | | Zeigen Sie einen Hilfeknopf mit einem eingebetteten Hilfetext an. Unterstützt Markdown-Formatierung. |
| `--helpimage <file\|url>` | | Fügen Sie ein Bild zum Hilfetext-Popover hinzu |
| `--helpsheetbuttontext <text>` | | Beschriftung für die "Schließen"-Schaltfläche im Hilfefenster (Standard: `OK`). |
| `--helpalignment [left\|centre\|right]` | | Ausrichtung des Inhalts von Hilfenachrichten |

Weitere Informationen finden Sie in der [Hilfenachricht](/de/operation/help-message).

---

## Bilder, Videos und Web-Inhalte

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--image <file\|url>` | `-g` | Zeigt ein Bild an. Mehrere Instanzen erzeugen eine Bildergalerie. |
| `--imagecaption <text>` | | Beschriftung, die unterhalb des Bildes angezeigt wird |
| `--video <file\|url>` | | Zeigt ein Video. Unterstützt die Kurzformen `youtube=<id>` und `vimeo=<id>`. |
| `--videocaption <text>` | | Untertitel, die unterhalb des Videos angezeigt werden |
| `--autoplay` | | Automatische Wiedergabe von Videos beim Start |
| `--webcontent <url>` | | Zeigen Sie eine Webseite im Nachrichtenbereich an |

Weitere Informationen finden Sie unter [Bilder](/de/basic-use/images), [Video](/de/basic-use/video) und [Web-Inhalte](/de/basic-use/web-content).

---

## Informationsbereich

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--infotext <text>` | | Ersetzen Sie die Info-Schaltfläche durch einen statischen Text |
| `--infobox <text>` | | Zeigen Sie Text (mit Unterstützung von Markdown) unterhalb des Icons an |
| `--infoboxwidth <num>` | | Legen Sie die Breite des Informationsfensters unabhängig von der Größe des Icons fest |

Weitere Informationen finden Sie im [Infobox](/de/advanced/info-box)].

---

## Benutzereingabe

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--textfield <text\|json>[,options]` | | Fügen Sie ein Textfeld hinzu. Unterstützt `required`, `secure`, `prompt`, `regex`, `fileselect`, `date`, `time`, `mindate`, `maxdate` und mehr. Kann auch als JSON-Objekt definiert werden |
| `--textfieldlivevalidation` | | Zeigen Sie eine Echtzeit-Validierungsanzeige für reguläre Ausdrücke in Textfeldern |
| `--checkbox <text\|json>` | | Fügen Sie ein Kontrollkästchen mit der angegebenen Beschriftung hinzu. Es kann auch als JSON-Objekt angegeben werden |
| `--checkboxstyle [checkbox\|switch][,size]` | | Ändern des Aussehens der Kontrollkästchen |
| `--selecttitle <text>[,options]` | | Fügen Sie eine Auswahlliste mit dem angegebenen Namen hinzu |
| `--selectvalues <csv>` | | Kommagetrennte Werte für die Auswahlliste |
| `--selectdefault <text>` | | Standardmäßig ausgewählter Wert für die Auswahlliste |
| `--selectstyle` | | Formatierung für die Auswahlliste |
| `--selectitem <json>` | | Definieren Sie ein ausgewähltes Listenelement mithilfe der JSON-Objektnotation |

Weitere Informationen finden Sie in den Abschnitten "Textfelder", "Kontrollkästchen" und "Auswahllisten". ](/de/advanced/textfields) ](/de/advanced/checkboxes) ](/de/advanced/select-lists)

### JSON-Konfiguration pro Argument

Viele Argumente, die kommagetrennte Werte akzeptieren, können auch als JSON-Objekte angegeben werden. Dies ermöglicht eine direktere Kontrolle und ist besonders nützlich für komplexe Konfigurationen.

**Erkennung:** Wenn ein Wert als JSON-Objekt interpretiert werden kann, wird der JSON-Parser verwendet; andernfalls wird die CSV-Analyse angewendet.

**Unterstützte Argumente:**
- `--textfield` - Vollständige Feldeinstellung mit allen Modifikatoren
- `--checkbox` - Kontrollkästchen mit Icon und Schaltflächenaktivierung
- `--listitem` - Listeneintrag mit verschachtelten Icon-Objekten
- `--selecttitle` - Wird genauso behandelt wie `--selectitem`
- `--selectitem` - Elemente der Auswahlliste, die in JSON definiert sind
- `--titlefont` / `--messagefont` - Schriftkonfiguration mit Farbe, Größe, Gewicht und Schatten
- `--icon` / `--overlayicon` - Icon-Objekte mit Symbolen, Farben, Paletten und Animationen
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - Symbole für Schaltflächen mit Positionsangaben

Bitte beachten Sie die einzelnen Dokumentationsseiten für detaillierte JSON-Schemas und Beispiele.

---

## Artikel-Listen

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--listitem <text\|json>` | | Fügen Sie einen Listeneintrag hinzu. Unterstützt Status-Icons und anklickbare Aktionen. Kann auch als JSON-Objekt mit Unterstützung für verschachtelte Icons angegeben werden |
| `--liststyle [expanded\|compact]` | | Vertikaler Abstand zwischen den Zeilen einer Liste |
| `--enablelistselect` | | Ermöglichen Sie die Auswahl von Elementen aus einer Liste; die ausgewählten Elemente werden beim Verlassen zurückgegeben |

Weitere Informationen finden Sie in den [Listen der Artikel](/de/advanced/item-lists)].

---

## Timer und Fortschrittsbalken

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--timer [<seconds>]` | | Zeigt einen Countdown-Timer an (Standardwert: 10 Sekunden). Beendet den Vorgang mit dem Exit-Code 4, wenn die Zeit abläuft. |
| `--hidetimerbar` | | Verbergen Sie den Fortschrittsbalken, während der Countdown weiterhin läuft |
| `--hidetimer` | | Verbergen Sie den Timer vollständig |
| `--progress [<int>]` | | Zeigen Sie einen Fortschrittsbalken mit der angegebenen Anzahl von Schritten |
| `--progresstext <text>` | | Anfangstext wird unterhalb des Fortschrittsbalkens angezeigt |

Siehe [Timer und Fortschrittsbalken](/de/advanced/timer-progress) für Details.

---

## Fenstergröße und -position

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--width <num>` | | Breite des Dialogfensters in Punkten |
| `--height <num>` | | Höhe des Dialogfensters in Punkten |
| `--small` | `-s` | Reduzieren Sie die Standardfenstergröße um 25 % |
| `--big` | `-b` | Erhöhen Sie die Standardgröße des Fensters um 25 % |
| `--position <position>` | | Fensterposition (z. B. `center`, `topright` oder `x,y`). |
| `--positionoffset <int>` | | Abstand der Kanten beim Verwenden von `--position` (Standardwert: 16). |
| `--moveable` | `-o` | Erlauben Sie, dass das Fenster verschoben werden kann |
| `--resizable` | | Erlauben Sie, dass das Fenster in der Größe verändert werden kann (impliziert `--moveable`). |
| `--ontop` | `-p` | Halten Sie dieses Fenster immer im Vordergrund, also oberhalb aller anderen Fenster |
| `--windowbuttons [close,min,max]` | | Aktivieren Sie die Schaltflächen zum Schließen, Minimieren und Maximieren des Fensters |
| `--showonallscreens` | | Zeigen Sie das Fenster auf allen verbundenen Bildschirmen |
| `--appearance [dark\|light]` | | Das Erscheinungsbild des Fensters ändern |

Weitere Informationen finden Sie unter [Fenstergröße](/de/advanced/window-size) und [Layout](/de/advanced/layout).

---

## Voreinstellungen für Fensterdesigns

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--style <preset>` | | Eine vordefinierte Formatvorlage anwenden: `presentation`, `mini`, `centered`, `alert`, `caution`, `warning` |
| `--mini` | | Kompaktes Fenster, das Titel, Icon und eine zweizeilige Meldung anzeigt |
| `--fullscreen` | `-f` | Vollbildmodus (ohne Schaltflächen; Tastaturfunktionen bleiben weiterhin aktiv). |
| `--presentation` | | Präsentationsmodus mit Fortschrittsbalken und strukturierter Anordnung |
| `--eula` | | Anzeigen im Modus zur Akzeptanz der Endbenutzer-Lizenzvereinbarung |
| `--blurscreen` | | Verwischen Sie alle Bildschirminhalte hinter dem Dialogfenster |
| `--hideotherapps` | | Verbergen Sie beim Start alle anderen Anwendungen |

Weitere Informationen finden Sie unter [Vollbild](/de/advanced/full-screen) und [Präsentation](/de/advanced/presentation).

---

## Benachrichtigungen

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--notification` | | Senden Sie eine Systembenachrichtigung für macOS |
| `--identifier <text>` | `-id` | Eindeutige Kennung für die Benachrichtigung |
| `--remove` | | Entfernen Sie die Benachrichtigung mit der entsprechenden `--identifier` |
| `--enablenotificationsounds` | | Benachrichtigungstöne aktivieren |

Weitere Informationen finden Sie in [Benachrichtigungen](/de/advanced/notifications)].

---

## Ton

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--sound <file\|url>` | | Spielen Sie eine Audiodatei beim Starten |
| `--showsoundcontrols` | | Zeigt die Wiedergabesteuerung (Abspielen/Pause, Stummschaltung, Zeitbalken). |

---

## Dock-Icon

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--showdockicon` | | Zeigen Sie das Dialog-Icon im macOS-Dock an |
| `--dockicon <file\|url>` | | Zeigen Sie ein benutzerdefiniertes Bild als Icon in der Dock-Leiste an (impliziert `--showdockicon`). |
| `--dockiconbadge <text>` | | Zeigen Sie ein Icon auf dem sichtbaren Dock-Icon an |

---

## Befehlsdatei

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--commandfile [<file>]` | | Pfad zur Konfigurationsdatei für Echtzeit-Updates des Dialogs (Standard: `/var/tmp/dialog.log`). |
| `--displaylog <file>` | | Zeigen Sie den Inhalt einer Datei so an, wie er geschrieben ist |
| `--loghistory [<int>]` | | Füllen Sie `--displaylog` vorab mit den letzten N Zeilen (Standard: 100). |

Weitere Informationen finden Sie in der [Befehlsdatei](/de/advanced/command-file).

---

## JSON-Eingabe und -Ausgabe

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--jsonfile <file>` | | Laden der Dialogkonfiguration aus einer JSON-Datei |
| `--jsonstring <text>` | | Laden der Dialogkonfiguration aus einer JSON-Zeichenkette |
| `--json` | `-j` | Die Ergebnisse werden im JSON-Format ausgegeben |

Weitere Informationen finden Sie in der [JSON-Konfiguration](/de/advanced/json-configuration)].

---

## Tastatur und Interaktion

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--quitkey <char>` | | Benutzerdefinierte Taste zum Beenden (wird als `⌘ + <key>` verwendet, Standard: `q`). |
| `--hidedefaultkeyboardaction` | | Eine bestimmte Aktion `⌘ + ⇧` muss ausgelöst werden, um die Funktionen "Zurück" oder "Abbrechen" über die Tastatur zu aktivieren |
| `--alwaysreturninput` | | Geben Sie bei Programmende immer die Benutzereingabe zurück, unabhängig vom Exit-Code |
| `--ignorednd` | `-d` | Zeigen Sie den Dialog auch dann an, wenn der "Nicht stören"-Modus aktiviert ist |
| `--vieworder <csv>` | | Die Anzeigereihenfolge der Eingabeelementtypen überschreiben |

---

## Autorisierung

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--key <string>` | `-k` | Ein Authentifizierungsschlüssel ist erforderlich, um den Dialog zu starten |
| `--checksum <string>` | | Erstellen Sie einen SHA256-Hash (zur Verwendung mit `--key`). |

Weitere Informationen finden Sie unter [Autorisierung](/de/operation/authorization)].

---

## Anmeldefenster

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--loginwindow` | | Zeigt den Dialog beim Anmeldevorgang an (erfordert einen entsprechenden LaunchAgent). |

Weitere Informationen finden Sie im Abschnitt [Anmeldefenster](/de/operation/login-window)].

---

## Inspektionsmodus

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--inspect-mode` | | Starten Sie im Überprüfungsmodus |
| `--inspect-config <file>` | | Konfiguration für den Inspektionsmodus festlegen |
| `--inspect-schema <file>` | | Geben Sie das Schema für den Inspektionsmodus an |
| `--schema-validate <file>` | | Eine Konfiguration anhand eines Schemas validieren |

Weitere Informationen finden Sie unter [Inspektionsmodus](/de/advanced/inspect-mode)].

---

## Nützliche Funktionen und Debugging-Tools

| Argument | Kurz | Beschreibung |
|---|---|---|
| `--version` | `-v` | Drucken Sie die Versionsinformationen aus |
| `--help [<argument>]` | | Drucken Sie eine Hilfeseite oder eine detaillierte Hilfeseite für ein bestimmtes Argument |
| `--licence` | `-l` | Drucken Sie die Lizenz |
| `--debug [<colour>]` | | Aktivieren Sie den Debug-Modus mit optionalen Hervorhebungen für Inhaltsgrenzen |
| `--verbose` | `-vvv` | Aktivieren Sie die ausführliche Protokollausgabe |
| `--listfonts` | | Geben Sie die verfügbaren Schriftnamen aus |
| `--demo` | | Starten Sie im Demomodus |
| `--builder` | | Starten Sie die Benutzeroberfläche des Baukastens |
| `--jh` | `-jh` | Aktivieren Sie den Kompatibilitätsmodus für jamfHelper |

Weitere Informationen finden Sie unter [Builder](/de/reference/builder)].
