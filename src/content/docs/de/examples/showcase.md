---
title: Ausstellung
description: Gemeinschaftsprojekte, Skripte und Beispiele, die swiftDialog verwenden
translationSynced: 2026-11-23T00:11:48+00:00
---

## Im Folgenden werden verschiedene Anwendungsmöglichkeiten von swiftDialog vorgestellt.

[swiftDialog Demo Scripts](https://github.com/swiftdialog/demo)

## Workshops und Videos

Dies sind Videos, die bei verschiedenen Konferenzen aufgenommen wurden.

Bart Reardon

 - [JNUC 2022](https://www.youtube.com/watch?v=HXwUeBWh20I)

 - swiftDialog Workshop [MacDevOpsYVR 2024](https://www.youtube.com/watch?v=dZgmmQbTTdg)

Jon Crain

 - PSU MacAdmins 2023: [Anpassbare Dialogfenster für macOS: Verwendung von SwiftDialog für eine bessere Benutzererfahrung](https://www.youtube.com/watch?v=QtWNBn76LQM)

Trevor Sysock

 - PSU MacAdmins 2024: [Ihr Installomator ist jetzt in meinem swiftDialog!](https://www.youtube.com/watch?v=WU6o3iJNQM4)

## Blogs

[Benutzerdefinierte Benachrichtigungen mit swiftDialog und SimpleMDM anzeigen](https://simplemdm.com/blog/how-to-display-custom-notifications-with-swiftdialog-and-simplemdm/)

[Bart Reardon – Jamf](https://www.jamf.com/blog/bart-reardon-swiftdialog/)

## Projekte, die mit swiftDialog integriert werden können

Diese Projekte benötigen swiftDialog nicht unbedingt, aber es stehen optionale Integrationen zur Verfügung

### [Scripting OS X](https://scriptingosx.com) – Installomator

![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/Installomator/Installomator/main)

Das eine Installationsskript, um sie alle zu beherrschen. https://github.com/Installomator/Installomator

 - [Fortschritt von Installomator mit SwiftDialog in Jamf anzeigen](https://github.com/Installomator/Installomator/tree/main/MDM/Jamf)

### [Mac Nerd](https://github.com/Mac-Nerd/) – Patchomator

![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/Mac-Nerd/patchomator/1.1)

Ein Verwaltungsskript für Installomator. https://github.com/Mac-Nerd/patchomator

 - [Fortschritt und andere Meldungen über swiftDialog anzeigen, falls installiert.](https://github.com/Mac-Nerd/patchomator#swift-dialog)

### [App Auto Patch](https://github.com/App-Auto-Patch/App-Auto-Patch)

![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/App-Auto-Patch/App-Auto-Patch)

App Auto-Patch kombiniert die Erkennung lokaler Anwendungen, eine Installomator-Integration und benutzerfreundliche swiftDialog-Aufforderungen, um die Verwaltung von Software-Patches auf Mac-Computern zu automatisieren.

App Auto-Patch basiert auf einem ähnlichen Konzept wie das Patchomator-Projekt, wobei ein erheblicher Teil des Codes von dort übernommen wurde.

## Weitere Projekte, die auf swiftDialog basieren oder es anderweitig verwenden

### [Scott Kendall](https://github.com/ScottEKendall/)

 - [Jamf-Pro-Skripte](https://github.com/ScottEKendall/JAMF-Pro-Scripts)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/ScottEKendall/JAMF-Pro-Scripts/main)

### [Richard Purves](https://github.com/franton/)

 - [Swift Deploy](https://github.com/franton/SwiftDeploy) – Zero-Touch-Bereitstellungsmethode für Jamf Pro und SwiftDialog

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/franton/SwiftDeploy/main)

### [Graham Pugh](https://github.com/grahampugh/)

 - [Erase Install](https://github.com/grahampugh/erase-install) – macOS direkt vom Systemvolume neu installieren unter Verwendung von `startosinstall`

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/grahampugh/erase-install/main)

### [Dan Snelson](https://github.com/dan-snelson/dialog-scripts)

 - [Display Message](https://github.com/dan-snelson/dialog-scripts/tree/main/Display%20Message) – swiftDialog und Jamf Pro-Richtlinienskript-Parameter nutzen, um ansprechende Endbenutzermeldungen anzuzeigen.

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/dan-snelson/dialog-scripts/main)

 - [Setup Your Mac](https://github.com/setup-your-mac/Setup-Your-Mac) – die anfängliche Gerätekonfiguration vereinfachen, indem swiftDialog und Jamf Pro-Richtlinien-Custom-Events genutzt werden

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/setup-your-mac/Setup-Your-Mac/main)

### [Adam Codega](https://github.com/acodega/dialog-scripts)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/acodega/dialog-scripts/main)

 - [MDM Apps Deploy](https://github.com/acodega/dialog-scripts/blob/main/MDMAppsDeploy.sh) – einen Dialog mit einer Liste von Anwendungen anzeigen und anzeigen, wann diese installiert wurden

 - [Computername aus der Eingabe](https://github.com/acodega/dialog-scripts/blob/main/computerNameFromInput.sh)

 - [Dialogprüfung und -installation](https://github.com/acodega/dialog-scripts/blob/main/dialogCheckFunction.sh) – Die aktuell installierte Version von swiftDialog überprüfen und erforderliche Komponenten installieren

### [Jon Crain](https://github.com/joncrain/)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/joncrain/swiftDialog-scripts/main)

 - [swiftDialog-Skripte](https://github.com/joncrain/swiftDialog-scripts) – Skripte, die [swiftDialog](https://github.com/bartreardon/swiftDialog) für verschiedene Aufgaben verwenden.

 - [DEP/ADE-Workflow](https://github.com/joncrain/swiftDialog-scripts/tree/main/depnotify-swiftdialog) – DEPnotify-Typ-Workflow mit optionaler Softwareauswahl.

 - [FileVault-Warnung](https://github.com/joncrain/swiftDialog-scripts/tree/main/fv_alert-swiftdialog) – Warnung, die ausgelöst wird, wenn Crypt ein Problem mit der Schlüsselspeicherung erkennt.

 - [Migrationsassistenten-Warnung](https://github.com/joncrain/swiftDialog-scripts/tree/main/ma_alert-swiftdialog) – eine Benachrichtigung für den Endbenutzer öffnen, wenn der Migrationsassistent gestartet wird

 - [Software-Update](https://github.com/joncrain/swiftDialog-scripts/tree/main/nudge-swiftdialog) – Nudge SwiftDialog. Lockere Anleihen bei [Nudge](https://github.com/macadmins/nudge)

 - [MDM-Anmeldungswarnung](https://github.com/joncrain/swiftDialog-scripts/tree/main/umad-swiftdialog) – konzeptionell aufgebaut auf [umad](https://github.com/macadmins/umad) von Erik Gomez.

### [James Smith](https://github.com/smithjw/)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/smithjw/speedy-prestage-pkg/main)

 - [swiftDialog speedy-prestage](https://github.com/smithjw/speedy-prestage-pkg/tree/feature/swiftDialog) – Jamf-Anmeldeskript

### [Thijs Xhaflaire](https://github.com/txhaflaire/)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/txhaflaire/DiskEncrypter/main)

 - [Nicht verschlüsselte, entnehmbare Speichermedien verschlüsseln](https://github.com/txhaflaire/DiskEncrypter) – Nicht verschlüsselte, entnehmbare Speichermedien verschlüsseln

### [Second Son Consulting](https://www.secondsonconsulting.com/)

 - [Baseline](https://github.com/SecondSonConsulting/Baseline) – eine MDM-agnostische Zero-Touch-Lösung für macOS

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/SecondSonConsulting/Baseline/main)

 - [Renew](https://github.com/SecondSonConsulting/Renew) – ein macOS-Skript, um Benutzer dazu zu ermutigen, ihre Workstations neu zu starten

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/SecondSonConsulting/Renew/main)

 - [swiftDialog-Beispiele](https://github.com/SecondSonConsulting/swiftDialogExamples)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/SecondSonConsulting/swiftDialogExamples/main) – Beispielskripte, um die verschiedenen Funktionen von [SwiftDialog](https://github.com/bartreardon/swiftDialog) zu demonstrieren

### [Martin Piron](https://github.com/ooftee)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/ooftee/dialog-starterkit/main)

 - [Dialog Starter Kit](https://github.com/ooftee/dialog-starterkit) – einfache und intuitive Möglichkeit, eine Gruppe von Apps auszuwählen und zu installieren

### [PezzaD84](https://github.com/PezzaD84)

 - [Assemble](https://github.com/PezzaD84/Assemble) – Skript zur Bereitstellung von Geräten mit swiftDialog

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/PezzaD84/Assemble/main)

 - [JAMF-LAPS-UI](https://github.com/PezzaD84/JAMF-LAPS-UI) – eine Benutzeroberfläche für das integrierte JAMF LAPS-Feature

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-UI/main)

 - [JAMF-LAPS-Configurator](https://github.com/PezzaD84/JAMF-LAPS-Configurator) – ein Bash-Skript, das bei der Konfiguration von JAMF LAPS hilft

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-Configurator/main)

 - [Device-Information](https://github.com/PezzaD84/Device-Information) – ein Bash-Skript, das Geräteinformationen in einer benutzerfreundlichen Eingabeaufforderung anzeigt

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/PezzaD84/Device-Information/main)

### [Andrew Barnett](https://github.com/AndrewMBarnett/)

 - [ReEnroll](https://github.com/AndrewMBarnett/ReEnroll) – den erneuten Einschreibungsprozess von Geräten in Jamf Pro automatisieren

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/AndrewMBarnett/ReEnroll/main)

### [Microsoft](https://github.com/microsoft)

 - [Bereitstellung eines Onboarding-Splash-Screens mit Swift Dialog und Intune](https://github.com/microsoft/shell-intune-samples/tree/03b181ca16c8a8f677a19a3a45f5943fb36e69b9/macOS/Config/Swift%20Dialog)

   ![Letzter Commit (Branch) auf GitHub](https://img.shields.io/github/last-commit/microsoft/shell-intune-samples/master) – Onboarding-Splash-Screen für Intune
