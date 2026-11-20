---
title: Erste Schritte mit swiftDialog
description: Einführung in swiftDialog, ein modernes macOS-Dialog-Dienstprogramm für Administratoren
translationSynced: 2026-11-20T09:10:01+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialog Beispiel für die Willkommensnachricht](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

Das Ziel von swiftDialog ist es, ein Hilfsprogramm für macOS-Administratoren bereitzustellen, das über Skripte verwendet werden kann, um ein Dialogfenster anzuzeigen, das Informationen für den Benutzer präsentiert und die vom Benutzer durchgeführte Aktion meldet. Diese Informationen können später für weitere Skriptverarbeitung verwendet oder einfach dazu dienen, bestimmte Informationen anzuzeigen.

swiftDialog akzeptiert Eingaben über die Kommandozeile und verwendet dabei eine oder mehrere [Kommandozeilenoptionen](/de/advanced/command-line-options), um swiftDialog mitzuteilen, was angezeigt werden soll und wie die Anzeige erfolgen soll.

Es gibt eine Reihe von Optionen, mit denen Sie die Darstellung anpassen können. Diese reichen von einfachen Informationsanzeigen bis hin zu komplexeren Funktionen, die Texteingabe, Dropdown-Listen, Bildanzeigen und mehr umfassen.

## Ausführen von swiftDialog

Das **.pkg**-Installationsprogramm von der Seite mit den [Veröffentlichungen](https://github.com/swiftDialog/swiftDialog/releases) installiert swiftDialog unter `/usr/local/bin/dialog`, das sich auch im Standard-`$PATH` auf macOS befinden sollte.

Um Dialoge aus Ihrem Skript aufzurufen, können Sie entweder den vollständigen Pfad verwenden oder sich auf `$PATH` verlassen

```bash
$ dialog --title ...
```

oder

```bash
$ /usr/local/bin/dialog --title ...
```

Auf der grundlegendsten Ebene kann dialog einfach die Kommandozeilenoptionen `--title` und `--message` verwenden, um ein Dialogfenster mit der gewünschten Nachricht anzuzeigen.

swiftDialog kann viel mehr als das, und Sie sollten die Seite "[Kommandozeilenoptionen](/de/advanced/command-line-options)" lesen, um eine vollständige Liste der verfügbaren Optionen zu erhalten, oder dialog mit der Option `--help` aufrufen.

## Schnelle Links

### Grundlegende Funktionen
- [Anpassen des Titels von swiftDialog](/de/basic-use/title)
- [Anpassung der Nachrichtenanzeige in swiftDialog](/de/basic-use/message)
- [Anpassen des im Icon-Bereich von swiftDialog angezeigten Bildes](/de/basic-use/icon)
- [Ein Bannerbild hinzufügen](/de/advanced/banner-images)
- [Anpassen der Schaltflächen und deren Funktionalität](/de/basic-use/buttons)

### Erweiterte Funktionen
- [Informationsbox](/de/advanced/info-box)
- [Bannerbilder](/de/advanced/banner-images)
- [Hilfemeldung](/de/operation/help-message)
- [Auswahllisten und Optionsfelder](/de/advanced/select-lists)
- [Texteingabe](/de/advanced/textfields)
- [Kontrollkästchen](/de/advanced/checkboxes)
- [Timer mit Fortschrittsbalken](/de/advanced/timer-progress)
- [Fenstergröße und -verhalten](/de/advanced/window-size)
- [Vollbildmodus](/de/advanced/full-screen)
- [Präsentationsmodus](/de/advanced/presentation)
- [Elementlisten](/de/advanced/item-lists)
- [Systemmitteilungen](/de/advanced/notifications)
- [Command-Q-Verhalten](/de/operation/command-q)
- [Integrierte Variablen](/de/operation/builtin-variables)

## Unterstützung

swiftDialog wurde zum Teil als eine Art Lernübung entwickelt, um herauszufinden, wie man Anwendungen mit SwiftUI erstellt, und zum Teil, um eine Möglichkeit zu schaffen, Informationen an Mac-Nutzer in einer Weise zu vermitteln, die meinen Vorstellungen entsprach.

Unterstützung kann angeboten werden, indem [ein Problem gemeldet wird](https://github.com/swiftDialog/swiftDialog/issues). Vorschläge für neue Funktionen sind ebenfalls willkommen.

## Kontakt

Sie können den Autor im [Macadmins Slack](https://www.macadmins.org/slack) im Kanal #swiftdialog erreichen (Benutzername @bartreardon – er ist meistens im Kanal #anzmac unterwegs). Bitte beschränken Sie jedoch alle Support-Anfragen oder allgemeinen Fragen auf GitHub, damit Ihr Problem nachverfolgt und bearbeitet werden kann. Vielen Dank 😃