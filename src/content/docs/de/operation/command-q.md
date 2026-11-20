---
title: Command-Q-Verhalten ändern
description: Anpassen von Tastenkombinationen für Dialogfenster zum Beenden
translationSynced: 2026-11-20T09:57:33+00:00
---

In swiftDialog Version 1.10.2 und neueren Versionen gibt es den Befehl `--quitkey <char>`, mit dem `command+q` auf `command +<char>` neu zugewiesen werden kann

Zum Beispiel: `--quitkey x` deaktiviert die Funktion, die durch die Tastenkombination `command+q` ausgelöst wird, um das Dialogfenster zu schließen, erlaubt aber `command+x`.

Zusätzlich, wenn ein Dialog über eine `command+<char>`-Aktion beendet wird, wird ein Exit-Code von `10` zurückgegeben, was es ermöglicht, bei Bedarf entsprechende Maßnahmen zu ergreifen.

Die Tastenkombinationen `command+w`, `command+m` und `command+n` sind standardmäßig deaktiviert und können nicht neu belegt werden.