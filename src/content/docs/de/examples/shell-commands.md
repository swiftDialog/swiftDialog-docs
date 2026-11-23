---
title: Shell-Befehle
description: Experimentelle Funktion zum Ausführen von Shell-Befehlen über Schaltflächenaktionen
translationSynced: 2026-11-23T08:35:52+00:00
---

Version 1.1.2 führt eine experimentelle Funktion über den Befehl `button1shellaction` ein


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

Es nimmt einen einzelnen String-Parameter entgegen und übergibt diesen an eine Shell zur Ausführung, beispielsweise:

` --button1shellaction "say thank you for running dialog"`

Derzeit gibt es keine Eingabevalidierung oder Ausgabebeschränkung. Wenn der angegebene Befehl mit einem Fehler beendet wird, beendet Dialog trotzdem `0` mit dem Exit-Code für Schaltfläche 1. Der Status des Befehls wird auf dem Bildschirm angezeigt, einschließlich des Exit-Codes des Befehls, z. B.

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

Die Ausgabe der Befehle wird direkt an die Standardausgabe weitergeleitet, sodass Sie die Ergebnisse bei Bedarf anzeigen oder analysieren können.

## Aktionen für andere Schaltflächen (im Kontext von Shell-Befehlen)

Die Schaltfläche 2 und die Schaltfläche 3 (Abbrechen und Info) beenden den Dialog mit den Codes 2 bzw. 3. Diese Exit-Codes können erkannt und interpretiert werden. Wenn ein Administrator nach der Verarbeitung einer dieser Aktionen eine Aktion in der Shell ausführen möchte, empfehle ich, den Exit-Status des Dialogs zu erfassen und entsprechend zu verarbeiten.

## Überlegungen

Der Befehl wird nicht im Hintergrund ausgeführt, sodass das Dialogfenster sichtbar bleibt, aber während der Ausführung des Befehls nicht reagiert. Nach Abschluss des Befehls schließt sich das Dialogfenster. Bitte beachten Sie dies, wenn Sie einen Befehl ausführen möchten, der möglicherweise einige Zeit benötigt, um abgeschlossen zu werden.

Der Shell-Befehl erbt auch die Berechtigungen des Prozesses, der ihn aufgerufen hat. Wenn Dialog mit Root-Rechten ausgeführt wird, dann verfügt auch der Shell-Befehl über Root-Rechte.