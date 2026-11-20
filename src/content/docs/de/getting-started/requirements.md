---
title: Systemanforderungen
description: Systemanforderungen und Kompatibilität für swiftDialog unter macOS
translationSynced: 2026-11-20T09:23:03+00:00
---

## Systemvoraussetzungen für macOS

swiftDialog ist eine universelle Binäranwendung, die mit SwiftUI entwickelt wurde.

### 3.0+
- **Mindestversion von macOS**: macOS 15 (Sonoma)
- **Architektur**: Universelle Binärdatei (Intel und Apple Silicon)
- **Framework**: SwiftUI

### 2.3+
- **Mindestversion von macOS**: macOS 12 (Monterey)

### Vorherige Versionen
- Die letzte Version, die **macOS 11 (Big Sur)** unterstützt, ist [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## Abhängigkeiten

swiftDialog ist eine eigenständige Anwendung, die keine externen Abhängigkeiten benötigt. Alle notwendigen Frameworks sind im Programm-Paket enthalten.

## Berechtigungen

Je nach Nutzung kann swiftDialog bestimmte Berechtigungen erfordern:

### Grundlegende Bedienung
- Für die grundlegende Anzeige von Dialogfenstern sind keine besonderen Berechtigungen erforderlich

### Erweiterte Funktionen
- **Mitteilungen:** Der Benutzer muss die Berechtigungen für Systemmitteilungen erteilen
- **Vollzugriff auf die Festplatte:** Kann erforderlich sein, wenn auf geschützte Bereiche gelesen oder geschrieben werden soll

## Netzwerkanforderungen

- **Offline-Funktion:** swiftDialog funktioniert vollständig offline
- **Online-Aktivitäten:**
  - Überprüfung auf Updates
  - Anzeigen von Webinhalten
  - Herunterladen von Bildern aus dem Internet

