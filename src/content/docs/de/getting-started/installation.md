---
title: Installation
description: So installieren Sie swiftDialog unter macOS
translationSynced: 2026-11-20T09:26:57+00:00
---

## Installationsmethoden

### Paket-Installationsprogramm (empfohlen)

Die einfachste Möglichkeit, swiftDialog zu installieren, ist die Verwendung des **.pkg**-Installationsprogramms von der [Seite mit den Veröffentlichungen](https://github.com/swiftDialog/swiftDialog/releases).

Das Installationsprogramm installiert swiftDialog unter `/usr/local/bin/dialog`, das sich standardmäßig im `$PATH` auf macOS befinden sollte.

### Manuelle Installation

Wenn Sie eine manuelle Installation bevorzugen:

1. Laden Sie die neueste Version von der [Seite mit den Veröffentlichungen](https://github.com/swiftDialog/swiftDialog/releases) herunter
2. Extrahieren Sie die Binärdatei
3. Kopieren Sie sie in `/usr/local/bin/dialog` oder einen anderen Ordner auf Ihrem `$PATH`
4. Stellen Sie sicher, dass die ausführbare Datei die entsprechenden Ausführungsrechte besitzt: `chmod +x /usr/local/bin/dialog`

### Installation von Homebrew

Bald erhältlich – die Homebrew-Formel befindet sich in der Entwicklung.

## Verifizierung

Nach der Installation sollte überprüft werden, ob swiftDialog ordnungsgemäß funktioniert:

```bash
dialog --version
```

Oder testen Sie es mit einem einfachen Dialog:

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## Aktualisierung von swiftDialog

Um swiftDialog zu aktualisieren, laden Sie einfach die neueste Version herunter und installieren Sie sie. Der Installationsprozess ersetzt die bestehende Version.

Sie können programmatisch nach Updates suchen, indem Sie Folgendes verwenden:

```bash
dialog --checkupdates
```

## Deinstallation

Um swiftDialog zu entfernen:

```bash
sudo rm /usr/local/bin/dialog
```

## Bereitstellung über Mobile Device Management (MDM)

swiftDialog kann über Mobile Device Management (MDM)-Lösungen wie Jamf Pro, Mosyle oder Iru bereitgestellt werden. Installieren Sie einfach das .pkg-Installationsprogramm auf Ihren verwalteten Geräten.

### Beispiel für eine Jamf-Richtlinie

1. Laden Sie das swiftDialog-.pkg-Paket in Jamf Pro hoch
2. Erstellen Sie eine Richtlinie zur Installation des Pakets
3. Legen Sie die Zielgeräte fest
4. Legen Sie einen Auslöser fest (z. B. Check-in, wiederkehrend, Selbstbedienung usw.).