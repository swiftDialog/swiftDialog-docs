---
title: Dialog-CLI-Launcher
description: Wie die Kommandozeilen-Binärdatei von Dialog funktioniert und welche Optionen auf Benutzerebene verfügbar sind
translationSynced: 2026-11-23T08:35:52+00:00
---

Der Befehl `dialog`, der unter `/usr/local/bin/dialog` verfügbar ist, ist nicht Dialog.app selbst – es ist ein schlanker Befehlszeilenstarter (`dialogcli`), der die Dialog.app-Binärdatei umschließt. Das Verständnis seiner Funktionsweise ist hilfreich, wenn man swiftDialog für die Bereitstellung oder Skripterstellung einsetzt.

---

## Was der Launcher bewirkt

Wenn Sie `dialog` ausführen, startet der Launcher:

1. **Sucht die Dialog.app-Binärdatei** relativ zum eigenen Pfad innerhalb des App-Bundels.
2. **Erstellt die Befehlsdatei** an `/var/tmp/dialog.log` (oder dem angegebenen Pfad mit `--commandfile`), falls sie noch nicht existiert. Wenn der Pfad ein symbolischer Link ist, bricht der Launcher ab, um Sicherheitsrisiken zu vermeiden.
3. **Identifiziert den aktuell angemeldeten GUI-Benutzer** mithilfe von `SCDynamicStoreCopyConsoleUser`. Wenn kein GUI-Benutzer angemeldet ist und `--loginwindow` nicht angegeben wurde, beendet der Launcher mit dem Exit-Code `1`.
4. **Führt Dialog im richtigen Benutzerkontext aus.** Wenn der Launcher als root aufgerufen wird (z. B. durch eine Jamf-Richtlinie oder einen LaunchDaemon), verwendet er `launchctl asuser`, um Dialog als der aktuell angemeldete GUI-Benutzer auszuführen, sodass das Fenster in der richtigen Anzeigesitzung erscheint.
5. **Übergibt automatisch `--pid`** — die eigene Prozess-ID (PID) des Launchers wird als `--pid <pid>` eingefügt, sodass Dialog den aufrufenden Prozess überwachen und sich beenden kann, falls dieser beendet wird.
6. **Routet Benachrichtigungen mit bestimmtem Stil** – wenn sowohl `--notification` als auch `--style alert` oder `--style banner` verwendet werden, leitet der Launcher den Aufruf an die entsprechende integrierte Mitteilungs-Helfer-App weiter, statt an Dialog.app.

---

## Erstellen eines symbolischen Links

Der Launcher enthält die `--link` Option, die einen `/usr/local/bin/dialog` symbolischen Link erstellt, der auf sich selbst verweist. Dieser Befehl muss als root ausgeführt werden:

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

Dies wird normalerweise automatisch vom Installationspaket von swiftDialog erledigt.

---

## Nutzungsoptionen

Diese Optionen werden direkt vom Dialog-Programm selbst verwaltet und sind hauptsächlich für Verwaltungsaufgaben oder für Skripte zur Installation und Konfiguration nützlich.

### `--setappicon <file>`

Legt das App-Icon von swiftDialog auf die angegebene Bilddatei fest und beendet sich sofort. Dies aktualisiert auch die Icons aller integrierten Mitteilungs-Helfer-Apps.

```sh
dialog --setappicon /path/to/custom-icon.png
```

Dies ist eine einmalige Operation – Dialog zeigt kein Fenster an. Sie dient dazu, Dialog nach der Installation an Ihre individuellen Bedürfnisse anzupassen, sodass das Icon im Dock und die Mitteilungen zum Corporate Design Ihres Unternehmens passen.

### `--callingpid <int>`

Überwacht die angegebene Prozess-ID. Wenn dieser Prozess beendet wird, beendet Dialog automatisch mit dem Exit-Code `40`.

```sh
dialog --title "Installing..." --callingpid 12345
```

Dies wird automatisch vom `dialogcli`-Launcher eingefügt (unter Verwendung seiner eigenen Prozess-ID), sodass Dialog beendet wird, wenn das aufrufende Skript oder der Prozess beendet wird.

Der Exit-Code 40 wird zurückgegeben, wenn Dialog aufgrund des Beendens des überwachten Prozesses beendet wird.
