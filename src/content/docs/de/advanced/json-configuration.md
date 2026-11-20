---
title: JSON-Konfiguration
description: Die Verwendung von JSON zur Definition von Dialogoptionen für komplexe Konfigurationen
translationSynced: 2026-11-20T11:03:20+00:00
---

Anstatt zahlreiche Kommandozeilenoptionen für die Erstellung komplexer Dialoge zu verwenden, können Sie die Optionen `--jsonfile` oder `--jsonstring` nutzen, um Parameter zu definieren.

Das JSON-Format verwendet dieselben Optionen wie die, die über die Befehlszeile angegeben werden, mit einigen Ausnahmen und Einschränkungen.

**Hinweis:**
 - **Befehlszeilenoptionen können in Kombination mit JSON verwendet werden, jedoch haben alle in JSON definierten Optionen Vorrang.**
 - Um spezielle Zeichen `\n` im Text einer Nachricht zu unterstützen, erwartet `--jsonstring`, dass die JSON-Eingabe in einer einzigen, zusammenhängenden Zeile vorliegt

Beispiel:

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## Unterschiede zu Befehlszeilenoptionen

Optionen, die mehrfach verwendet werden können, können als Array eingegeben werden.

Um beispielsweise mehrere Bilder und Bildunterschriften anzugeben, verwenden Sie ein `image` Array mit `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

Kontrollkästchen können als aktiviert und/oder deaktiviert festgelegt werden. Der Standardwert ist `"disabled" : false` und muss nicht explizit angegeben werden

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

Für mehrere `textfield` Optionen ist ein einzelnes Textfeld anzugeben, wobei die Namen der Felder als ein Array angegeben werden

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### Zeichenketten und boolesche Werte

Die meisten Optionen werden als String-Werte übergeben, wobei für die angegebenen Werte Anführungszeichen erforderlich sind. Einige Werte können jedoch auch als boolesche Werte angegeben werden (`true` oder `false`, ohne Anführungszeichen). Optionen, die einen booleschen Wert akzeptieren, sind:

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### Optionen nicht über JSON verfügbar

Es gibt eine Reihe von Optionen, die nicht über JSON verwendet werden können, da sie in einem produktiven Umfeld keinen Sinn ergeben. Dazu gehören:

* `--jh` - Wird als direkter Ersatz verwendet, um Befehlszeilenoptionen von JamfHelper zu akzeptieren.
* `--listfonts` - Wird während der Prototypenentwicklung verwendet, um eine Liste der verfügbaren Schriftarten anzuzeigen
* `--help` - Zeigt Hilfetext an und beendet das Programm. Wird während der Entwicklung verwendet
* `--demo` - Zeigt einen Dialog an, der ausschließlich mit den Standardeinstellungen konfiguriert ist. Wird während der Prototypentwicklung verwendet
* `--version` - Gibt Versionsinformationen des Dialogs aus und beendet das Programm.
* `--showlicense` - Gibt Lizenzinformationen aus und beendet das Programm
* `--coffee` - Gibt Kaffeeinformationen aus und beendet das Programm

## Beispiel: Generierung von JSON in Python und Übergabe als Datei oder als Zeichenkette

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```