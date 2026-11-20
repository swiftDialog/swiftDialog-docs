---
title: Fallstricke
description: Häufige Probleme und Tipps zur Fehlerbehebung für swiftDialog
translationSynced: 2026-11-20T10:11:03+00:00
---

# Probleme mit Befehlsdateien

## Unzureichende Berechtigungen

Wenn Sie swiftDialog starten und die Befehlsdatei nicht geschrieben werden kann, erhalten Sie eine Fehlermeldung:

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

Die Befehlsdatei sollte entweder gelöscht oder ihre Berechtigungen so geändert werden, dass sie für alle Benutzer lesbar und beschreibbar ist `-rw-rw-rw` (666).

---

# swiftDialog 3.1.1: Änderungen im Verhalten

## `--alwaysreturninput` Erträge für alle Ausstiegspfade

**Was sich geändert hat:** Ab Version 3.1.1 gibt `--alwaysreturninput` ausgewählte Ergebnisse (Listen oder JSON-Formate) für **alle** möglichen Beendigungswege zurück, nicht nur bei einem Klick auf eine Schaltfläche.

**Betroffene Ausstiegspfade:**
- Befehlsdatei zum Beenden
- Zeitüberschreitung des Timers
- Taste zum Beenden drücken
- Beendeter Prozess

**Migration:** Skripte, die sich auf das alte Verhalten verlassen (nur wenn eine Schaltfläche gedrückt wird), könnten neue Ergebnisse liefern. Überprüfen Sie Ihre Parsing-Logik, falls Sie `--alwaysreturninput` verwenden.

## `--ontop` Beachtet die Dock-Position

**Was sich geändert hat:** Die Option `--ontop` berücksichtigt jetzt die Position des Docks und platziert den Dialog innerhalb des Bildschirmbereichs (nicht über dem Dock).

**Auswirkungen:** Dialogfenster werden bei Verwendung von `--ontop` nicht mehr den Bereich des Docks verdecken. Dies stellt eine Änderung einer bewussten Entscheidung aus einer früheren Version dar.

## Datumsauswahl-Modifikatoren

**Was sich geändert hat:** Der Modifikator `isdate` wurde als **veraltet** markiert und durch `date` und `time` ersetzt.

**Migration:** Aktualisieren Sie Ihre Skripte:

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# Häufige Fallstricke

## Wiederholbare Optionen als letztes Argument

**Problem:** Wiederholbare Optionen (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`), die als letztes Argument verwendet werden, könnten zu einem Programmabsturz führen.

**Status:** Behoben in Version 3.1.1

## Das Datumsfeld gibt keinen Wert zurück

**Problem:** Die Verwendung von `--textfield ...,isdate` ergab keinen Wert, da es sich um eine Hilfsfunktion handelte, die niemals Werte zurückgab.

**Status:** Behoben in Version 3.1.1. Verwenden Sie stattdessen die Modifikatoren `date` oder `time`.

## Die Funktion zum Einfügen von Bildbeschreibungen funktioniert nicht

**Problem:** Der `imagecaption:`-Befehl in der Befehlsdatei hatte keine Wirkung, da er nur in `appvars.imageCaptionArray` geschrieben wurde (wird einmal beim Start verwendet), anstatt in `observedData.imageArray` (die aktive Quelle).

**Status:** Behoben in Version 3.1.1

## Preset5 Group Headers Rendering Incorrectly

**Problem:** Die Überschriften für die Bereitstellungsgruppen ("Completed", "Pending Installation") werden an der falschen Position angezeigt oder werden dupliziert.

**Status:** Behoben in Version 3.1.1

## Die Tastaturaktion der Schaltflächenleiste funktioniert nicht

**Problem:** `--hidedefaultkeyboardaction` funktionierte nicht, da eine Regression in der Schaltflächenleiste vorlag.

**Status:** Behoben in Version 3.1.1