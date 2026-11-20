---
title: Anmeldefenster
description: Ausführen von swiftDialog-Dialogen im Kontext des macOS-Anmeldefensters
translationSynced: 2026-11-20T09:49:34+00:00
---

## Unterstützung für Anmeldefenster (ab Version 2.5.0)

`--loginwindow`

In swiftDialog 2.5 können Sie Dialoge im Anmeldefenster ausführen.

Standarddialoge werden unterstützt, mit oder ohne `--blurscreen`

## Anforderungen

Um swiftDialog im Kontext des Anmeldefensters auszuführen, müssen Sie Folgendes einrichten:

 - Ein Skript, das swiftDialog mit der von Ihnen gewünschten Konfiguration startet
   - Fügen Sie das Argument `--loginwindow` hinzu
 - Ein LaunchAgent

### Einrichtung von LaunchAgents

#### Manuelle Konfiguration

Das Folgende ist ein Beispiel für einen einfachen LaunchAgent:

```xml
<plist version="1.0">
<dict>
	<key>OnDemand</key>
	<false/>
	<key>LaunchOnlyOnce</key>
	<true/>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/script.sh</string>
	</array>
	<key>LimitLoadToSessionType</key>
	<string>LoginWindow</string>
	<key>Label</key>
	<string>com.swiftDialog.example-login-window</string>
</dict>
</plist>
```

Benennen Sie die Datei entsprechend, z. B. `com.swiftDialog.example-login-window.plist`, und installieren Sie sie in `/Library/LaunchAgents/`

#### Die Verwendung von Outset

Das Open-Source-Tool von Macadmins, [Outset](https://github.com/macadmins/outset/), bietet Funktionen zum Ausführen von Elementen im Anmeldefenster.

Neben der Vereinfachung des Prozesses erhalten Sie außerdem Zugriff auf Funktionen, mit denen Sie verhindern können, dass ein Benutzer Anmeldeelemente deaktiviert. Weitere Details finden Sie im [Outset-Wiki](https://github.com/macadmins/outset/wiki/Deployment#login-items-management) für weitere Details.

Platzieren Sie Ihr Skript im Verzeichnis `/usr/local/outset/login-window/` mit den Berechtigungen `root:root` `0755` (`-rwxr-xr-x`), und Outset verwaltet dann den Start des Skripts, sobald das Anmeldefenster erscheint.

### Überlegungen

Sie müssen bedenken, was nach der Ausführung des Skripts passiert. Wenn Sie nicht möchten, dass das Skript jedes Mal ausgeführt wird, wenn das Anmeldefenster angezeigt wird, müssen Sie Bedingungen in Ihrem Skript definieren, die entweder dazu führen, dass keine Aktion ausgeführt wird, oder dass das Skript sich selbst deinstalliert, wenn es nicht mehr benötigt wird.

### Beispielhafte Anwendungsfälle

#### Richtlinien zur akzeptablen Nutzung

Folgendes ist ein Beispiel für einen Dialog zur Nutzungsrichtlinie, der die Auswahl eines Kontrollkästchens erfordert und Inhalte aus einer Markdown-Datei (Beispiel: [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)) enthält, die im `--eula`-Modus angezeigt werden. Er würde jedes Mal angezeigt, wenn das Anmeldefenster angezeigt wird.

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>