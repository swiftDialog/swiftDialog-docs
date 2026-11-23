---
title: Neuerungen
description: Aktuelle Funktionen und Updates in swiftDialog
translationSynced: 2026-11-23T08:35:52+00:00
---

## swiftDialog Version 2.5.6

## Behebungen:

 - Ein Problem wurde behoben, bei dem die Angabe eines Icons aus einer JSON-Datei erforderlich machte, dass das Icon in einem Array enthalten sein musste, selbst wenn es sich nur um ein einzelnes Icon handelte. Behebt Fehler #493
 - Klicks auf Benachrichtigungen schließen Dialogfenster in Version 2.5.5. (Ticket #499)
 - Aktualisierte die Dialogmeldung für die Versionsinformationen, wenn kein Benutzer angemeldet ist, von @HowardGMac in https://github.com/swiftDialog/swiftDialog/pull/510
 - Verwendung des vollständigen Pfads für `scutil` (erneute Einreichung) von @MikeRich88 in https://github.com/swiftDialog/swiftDialog/pull/515
 - Zusätzlichen Abstand am unteren Rand des Bildes hinzugefügt
 - Fügt eine wichtige Autorisierung für das Senden von Benachrichtigungen hinzu, falls eine solche erforderlich ist. (#485)
 - Fehler bei fehlenden Optionen für `--textfield` in der Hilfe behoben (Ticket #485)

## Beiträge:

### Zusätzliche Optionen für die Arbeit mit Benachrichtigungen

 - Fügt die Möglichkeit hinzu, einer Benachrichtigung eine Kennung zuzuweisen, wodurch Sie eine Benachrichtigung einfach durch eine aktualisierte Version ersetzen können. Außerdem können Sie eine bestimmte Benachrichtigung anhand ihrer Kennung oder alle Benachrichtigungen löschen.

_Beispiel:_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

Vielen Dank an @chrisgrande

### Die Option "buttonsize" wurde als Variable sowohl für die Kommandozeile als auch für die Konfigurationsdatei hinzugefügt

 - Unterstützung für Mini-, Klein- und Großtasten, wobei die in macOS integrierten Größen verwendet werden. Wenn keine bestimmte Größe angegeben wird oder die Angabe ungültig ist, wird standardmäßig die Größe für normale Schaltflächen verwendet.
 - Unterstützung für die Einstellung der Schaltflächengröße im Bearbeitungsmodus, um Tests durchzuführen und JSON-Dateien zu generieren.

Das Aussehen der Schaltflächen wird auf `button1`, `button2` und die Infotaste angewendet. Es wird auch in den normalen und gestapelten Anordnungen von Schaltflächen verwendet.

 Es skaliert den Hilfebutton nicht, da dieser eine feste Größe hat.

Beispiele:

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

Vielen Dank an @k2graham

### Optionen zum Verbergen und Anzeigen des Dialogfensters aus der Befehlsdatei

 - Es wurden die Befehle `hide:` und `show:` zur Liste der Befehle in der Konfigurationsdatei hinzugefügt, um Fenster ein- und auszublenden. Dies verhindert jedoch nicht, dass Fensteraktualisierungen durchgeführt werden, während ein Fenster ausgeblendet ist.

Vielen Dank an @fabienconus

