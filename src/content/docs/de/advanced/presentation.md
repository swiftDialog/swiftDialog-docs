---
title: Präsentation
description: Erstellung von Dialogfenstern für den Präsentationsmodus, die laufende Prozesse und Aufgaben darstellen
translationSynced: 2026-11-20T10:47:50+00:00
---

## Präsentationsmodus

`--presentation` oder `--style presentation`

Der Präsentationsmodus ist ein Ausgabemodus von swiftDialog, der keine Benutzereingaben erfordert und dazu dient, einen laufenden Prozess oder eine Aufgabe anzuzeigen.

Um die Anzeige zu aktualisieren, ist die Verwendung einer [Befehlsdatei](/de/advanced/command-file) sowie geeigneter Befehle erforderlich.

Die Ansicht ist in zwei Hauptbereiche für Inhalte sowie einen Fußbereich unterteilt, der einen Fortschrittsbalken und Schaltflächen enthält.

## Informationsbereich

Der linke Teil des Fensters (ungefähr ein Drittel) enthält einen Informationsbereich und kann eine der folgenden Informationen anzeigen:

### Standardmäßig

Eine Hintergrundfarbe, die die bevorzugte Highlight-Farbe des Benutzers widerspiegelt.

Sie können optional die folgenden Modifikatoren verwenden:
 - `--infobox <text>` Um Text anzuzeigen (Unterstützung für Markdown-Format).
   - Der Text ist vertikal zentriert
 - `--background color=<color|hex>` um die Hintergrundfarbe festzulegen
   - Wenn keine Farbe angegeben ist, wird die vom System definierte Akzentfarbe verwendet
 - `--icon <image>` um ein Symbol in der oberen linken Ecke anzuzeigen
 - `--iconsize <int>` um die Größe des Symbols festzulegen.

### Bild

Geben Sie einen oder mehrere `--image <image>` an, um diesen Bereich mit einem Bild zu füllen

Mehrere Bilder werden als eine Bilderserie dargestellt. Verwenden Sie `--autoplay <sec>`, um die Bilder automatisch zu verschieben.

**Tipps**
* Verwenden Sie Bilder im Hochformat, um die besten Ergebnisse zu erzielen
* Die Bilder werden so skaliert, dass sie den verfügbaren Bereich ausfüllen. Bei der Verwendung mehrerer Bilder mit unterschiedlichen Seitenverhältnissen kann es zu Zuschneidungen kommen.

Starten Sie den Präsentationsmodus mit `--debug`, und eine empfohlene Bildgröße für das aktuelle Fenster wird in der Debug-Ausgabe angezeigt, nachdem Sie das Dialogfenster geschlossen haben.

e.g.

    DEBUG: Die ideale Größe für das Seitenbild in der Seitenleiste bei diesen Fensterabmessungen wäre: Breite: 492,0, Höhe: 636,0

### Web-Inhalte

Geben Sie `--webcontent <url>` ein, um den Inhalt einer HTML-Quelldatei anzuzeigen.

**Tipp:**
* Wenn eine lokale Datei verwendet wird, verweisen Sie auf die Datei mit `file:///path/to/file.html`

## Inhaltsbereich

Der rechte, etwa zwei Drittel große Bereich des Fensters ist für Inhalte reserviert, die in einer der folgenden Formen dargestellt werden:

### Standardmäßig

Beliebige Eingabe in einem der unterstützten Formate. `--message <text>`

### Liste

Ein oder mehrere --listitem-Elemente <item> in einer der unterstützten Formate.

## Fußzeile

Da die primäre Funktion des Präsentationsmodus die Anzeige von Fortschritt und anderen aktualisierbaren Inhalten ist, ist der Fußbereich des Fensters stets sichtbar und enthält einen Fortschrittsbalken, die die gesamte Breite des Fensters einnimmt, sowie Schaltflächen.

## Beispiele

**Nur Textinhalt**

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

**Webansicht im Informationsbereich und Listenelemente im Inhaltsbereich.**

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">