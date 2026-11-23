---
title: jamfHelper-Support
description: Die Verwendung von swiftDialog als direkter Ersatz für jamfHelper
translationSynced: 2026-11-23T00:09:16+00:00
---

Dialog kann jetzt mit dem neuen `--jh`-Flag grundlegende Befehlszeilenoptionen im Format von jamfHelper akzeptieren.

Dies erleichtert die Integration in bestehende Arbeitsabläufe und Skripte, indem der Aufruf von `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` durch `/usr/local/bin/dialog --jh` ersetzt wird

Die Verwendung des Flags bewirkt, dass das Dialogprogramm die Optionen von jamfHelper in entsprechende Dialogoptionen umwandelt. Nicht alle Optionen werden unterstützt. Standard-Dialogoptionen, für die es keine Entsprechung in jamfHelper gibt, sind weiterhin verfügbar, z. B. `--width`, `--height` und `--image`.

<br/>

## Funktionen und Verhalten

***
### Implementiert

#### `-windowType [hud | utility | fs]`

`hud` und `utility` werden ignoriert. `fs` wird in einen Dialog `--fullscreen` umgewandelt und wird in Dialogfenstern im Vollbildmodus angezeigt

#### `-windowPosition [ul | ll | ur | lr]`

Die Position des Fensters kann in der oberen rechten, oberen linken, unteren rechten oder unteren linken Ecke des Bildschirms des Benutzers festgelegt werden. Dies ist die einzige Funktion, die derzeit nicht Teil der Standardoptionen von Dialogen ist, aber zur Kompatibilität mit jamfHelper implementiert wurde.

#### `-title "string"`
Umgewandelt in `--title`

Legt den Titel des Fensters auf die angegebene Zeichenkette fest

#### `-heading "string"` und `-description "string"`
Umgewandelt in `--message`

Sowohl `-heading` als auch `-description` werden in die Dialogoption `--message` integriert. `-heading` wird in eine Markdown-Überschrift der Ebene 4 `####` umgewandelt, gefolgt von einem leeren Zeilenumbruch und dann `-description`

#### `-icon path`
Umgewandelt in `--icon`

Wenn diese Option nicht aktiviert ist, werden Dialoge so dargestellt, dass sie sich wie `jamfHelpers` verhalten: Wenn keine ID angegeben ist, wird keine ID angezeigt. `--hideicon`

#### `-button1 "string"`
Umgewandelt in `--button1text`

**_Geänderte Funktionalität:_** Der Dialog zeigt immer die Standard-Schaltfläche, was sich von der Funktionsweise von jamfHelper unterscheidet. Der Text der Standard-Schaltfläche ist `OK`

#### `-button2 "string"`
Umgewandelt in `--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
Umgewandelt in `--alignment`

Die einzigen implementierten Optionen sind `right`, `centre` und `left`

#### `-timeout int` und `-countdown`
Umgewandelt in `--timer`.

`-countdown` wird immer impliziert, da der Dialog immer die Zeitablaufanzeige (Timer-Balken) anzeigt. Eine Zeitablaufanzeige, die nicht angezeigt wird, ist im Dialog nicht implementiert.

<br/>

***
### Nicht implementiert

#### `-defaultButton [1 | 2]`
Der Standard-Button ist immer Button 1

#### `-cancelButton [1 | 2]`
Der "Abbrechen"-Button ist immer der zweite Button (falls angezeigt).

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`