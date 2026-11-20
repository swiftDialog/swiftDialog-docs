---
title: Exit-Codes
description: Verständnis der Exit-Codes und Rückgabewerte von swiftDialog
translationSynced: 2026-11-20T09:42:58+00:00
---

Wenn swiftDialog geschlossen wird, gibt swiftDialog einen Exit-Code zurück, der verwendet werden kann, um festzustellen, welche Aktion, falls überhaupt eine, ausgeführt wurde

|Exit-Code|Ursache|
|---------|-----|
|0|Der Benutzer hat auf die Standard-Schaltfläche (Schaltfläche 1) geklickt|
|2|Der Benutzer hat auf Schaltfläche 2 geklickt|
|3|Der Benutzer hat auf die Info-Schaltfläche geklickt|
|5|beendet über den Befehl `quit:` der Befehlsdatei|
|10|beendet, weil der Benutzer `cmd+q` (oder `--quitkey`) verwendet hat.|
|20|beendet, weil `--timer` den Wert 0 erreicht hat|
|201|Eine Bildquelle konnte nicht gefunden werden|
|202|Eine Datei konnte nicht gefunden werden|
|203|Ein ungültiger Farbwert wurde verwendet|

Weitere Informationen finden Sie auf dieser Seite: [Erfassung der Dialogausgabe zur weiteren Verarbeitung](/de/operation/capturing-output)