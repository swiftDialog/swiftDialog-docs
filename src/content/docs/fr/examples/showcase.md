---
title: Vitrine
description: Projets communautaires, scripts et exemples utilisant swiftDialog
translationSynced: 2026-11-23T05:30:08+00:00
---

## Ce qui suit est une présentation des différentes manières dont swiftDialog peut être utilisé.

[Démonstrations des scripts swiftDialog](https://github.com/swiftdialog/demo)

## Ateliers et vidéos

Ce sont des vidéos filmées lors de différentes conférences.

Bart Reardon

 - [JNUC 2022](https://www.youtube.com/watch?v=HXwUeBWh20I)

 - Atelier swiftDialog [MacDevOpsYVR 2024](https://www.youtube.com/watch?v=dZgmmQbTTdg)]

Jon Crain

 - PSU MacAdmins 2023 : [Dialogues personnalisables pour macOS : Utilisation de SwiftDialog pour une meilleure expérience utilisateur. ](https://www.youtube.com/watch?v=QtWNBn76LQM)

Trevor Sysock

 - PSU MacAdmins 2024 : [Votre Installomator est dans mon swiftDialog !](https://www.youtube.com/watch?v=WU6o3iJNQM4)]

## Blogs

Comment afficher des notifications personnalisées avec swiftDialog et SimpleMDM](https://simplemdm.com/blog/how-to-display-custom-notifications-with-swiftdialog-and-simplemdm/)

[Rencontrez Bart - Jamf](https://www.jamf.com/blog/bart-reardon-swiftdialog/)


## Projets qui s'intègrent à swiftDialog

Ces projets ne nécessitent pas l'utilisation de swiftDialog, mais des intégrations facultatives sont disponibles

### [Scripting pour macOS](https://scriptingosx.com) - Installomator]

![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/Installomator/Installomator/main)

Un seul script d'installation pour tout gérer. https://github.com/Installomator/Installomator

 - [Display Installomator Progress with SwiftDialog in Jamf](https://github.com/Installomator/Installomator/tree/main/MDM/Jamf)

### [Mac Nerd](https://github.com/Mac-Nerd/) - Patchomator]

![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/Mac-Nerd/patchomator/1.1)

Un script de gestion pour Installomator. https://github.com/Mac-Nerd/patchomator

 - [Afficher la progression et d'autres messages via swiftDialog si ce dernier est installé. ](https://github.com/Mac-Nerd/patchomator#swift-dialog)

### [Application de mise à jour automatique](https://github.com/App-Auto-Patch/App-Auto-Patch)

![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/App-Auto-Patch/App-Auto-Patch)

App Auto-Patch combine la découverte automatique des applications installées, une intégration avec Installomator, et des invites intuitives SwiftDialog pour automatiser la gestion des correctifs applicatifs sur les ordinateurs Mac.

App Auto-Patch a été développé sur un concept similaire à celui du projet Patchomator, et une partie importante de son code a été empruntée à ce dernier.

## Projets supplémentaires qui sont basés sur swiftDialog ou qui l'utilisent d'une autre manière

### [Scott Kendall](https://github.com/ScottEKendall/)

 - [Scripts Jamf Pro ](https://github.com/ScottEKendall/JAMF-Pro-Scripts)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/ScottEKendall/JAMF-Pro-Scripts/main)

### [Richard Purves](https://github.com/franton/)

 - [Déploiement rapide ](https://github.com/franton/SwiftDeploy) Méthode de déploiement sans intervention pour Jamf Pro et SwiftDialog

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/franton/SwiftDeploy/main)

### [Graham Pugh](https://github.com/grahampugh/)

 - [Effacer et réinstaller](https://github.com/grahampugh/erase-install) - Réinstaller macOS directement à partir du volume système en utilisant `startosinstall`

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/grahampugh/erase-install/main)

### [Dan Snelson](https://github.com/dan-snelson/dialog-scripts)

 - [Affichage de messages](https://github.com/dan-snelson/dialog-scripts/tree/main/Display%20Message) - Utilisez les paramètres des scripts de stratégie Jamf Pro et la fonctionnalité switftDialog pour afficher facilement des messages attrayants destinés aux utilisateurs finaux.

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/dan-snelson/dialog-scripts/main)

 - [Configuration de votre Mac ](https://github.com/setup-your-mac/Setup-Your-Mac) : simplifiez la configuration initiale de l'appareil grâce à swiftDialog et aux événements personnalisés de la politique Jamf Pro

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/setup-your-mac/Setup-Your-Mac/main)


### [Adam Codega](https://github.com/acodega/dialog-scripts)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/acodega/dialog-scripts/main)

 - [Déploiement des applications MDM](https://github.com/acodega/dialog-scripts/blob/main/MDMAppsDeploy.sh) : Afficher une boîte de dialogue avec une liste d'applications et indiquer quand elles ont été installées

 - [Nom de l'ordinateur (saisi par l'utilisateur)](https://github.com/acodega/dialog-scripts/blob/main/computerNameFromInput.sh)

 - [Vérification et installation de swiftDialog](https://github.com/acodega/dialog-scripts/blob/main/dialogCheckFunction.sh) : Vérifie la version actuelle de swiftDialog installée et installe les éléments requis

### [Jon Crain](https://github.com/joncrain/)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/joncrain/swiftDialog-scripts/main)

 - [swiftDialog scripts](https://github.com/joncrain/swiftDialog-scripts) - Scripts qui utilisent [swiftDialog](https://github.com/bartreardon/swiftDialog) pour diverses tâches.

 - [Flux de travail DEP/ADE ](https://github.com/joncrain/swiftDialog-scripts/tree/main/depnotify-swiftdialog) - Flux de travail de type DEPnotify avec sélection facultative des logiciels.

 - [Alerte FileVault ](https://github.com/joncrain/swiftDialog-scripts/tree/main/fv_alert-swiftdialog) : Alerte qui se déclenche lorsque Crypt détecte un problème lié à la gestion des clés.]

 - [Avertissement de l'assistant de migration ](https://github.com/joncrain/swiftDialog-scripts/tree/main/ma_alert-swiftdialog) : afficher une notification à l'utilisateur final lorsque l'assistant de migration est lancé

 - [Software Update](https://github.com/joncrain/swiftDialog-scripts/tree/main/nudge-swiftdialog) - Nudge SwiftDialog. Loosely based off of [Nudge](https://github.com/macadmins/nudge)

 - Alert d'inscription aux appareils mobiles (MDM) ](https://github.com/joncrain/swiftDialog-scripts/tree/main/umad-swiftdialog) – Conceptuellement basé sur [umad](https://github.com/macadmins/umad), développé par Erik Gomez.

### [James Smith](https://github.com/smithjw/)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/smithjw/speedy-prestage-pkg/main)

 - [swiftDialog speedy-prestage](https://github.com/smithjw/speedy-prestage-pkg/tree/feature/swiftDialog) - Script d'inscription Jamf]

### [Thijs Xhaflaire](https://github.com/txhaflaire/)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/txhaflaire/DiskEncrypter/main)

 - [Chiffrer les supports de stockage amovibles non chiffrés ](https://github.com/txhaflaire/DiskEncrypter) - Chiffrer les supports de stockage amovibles non chiffrés]

### [Second Son Consulting](https://www.secondsonconsulting.com/)

 - [Base de référence](https://github.com/SecondSonConsulting/Baseline) : Une solution simple d'installation, compatible avec tous les systèmes de gestion des appareils (MDM), pour macOS

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/SecondSonConsulting/Baseline/main)

 - [Renew](https://github.com/SecondSonConsulting/Renew) : Un script macOS conçu pour inciter les utilisateurs à redémarrer leurs postes de travail

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/SecondSonConsulting/Renew/main)

 - [Exemples de swiftDialog](https://github.com/SecondSonConsulting/swiftDialogExamples)]

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/SecondSonConsulting/swiftDialogExamples/main) - exemples de scripts pour illustrer les différentes fonctionnalités de [SwiftDialog](https://github.com/bartreardon/swiftDialog)

### [Martin Piron](https://github.com/ooftee)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/ooftee/dialog-starterkit/main)

 - [Kit de démarrage pour les dialogues ](https://github.com/ooftee/dialog-starterkit) : une manière simple et intuitive de sélectionner et d'installer un groupe d'applications

### [PezzaD84](https://github.com/PezzaD84)

 - [Assemble](https://github.com/PezzaD84/Assemble) - Script permettant de configurer des appareils en utilisant swiftDialog.]

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/PezzaD84/Assemble/main)

 - [JAMF-LAPS-UI](https://github.com/PezzaD84/JAMF-LAPS-UI) - Une interface utilisateur pour la fonctionnalité JAMF LAPS intégrée.]

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-UI/main)

 - [JAMF-LAPS-Configurator](https://github.com/PezzaD84/JAMF-LAPS-Configurator) : Un script Bash pour faciliter la configuration de JAMF LAPS

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-Configurator/main)

 - [Informations sur l'appareil](https://github.com/PezzaD84/Device-Information) - Un script Bash permettant d'afficher des informations sur l'appareil dans une interface conviviale

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/PezzaD84/Device-Information/main)

### [Andrew Barnett](https://github.com/AndrewMBarnett)

 - [Réinscription](https://github.com/AndrewMBarnett/ReEnroll) - Automatisez le processus de réinscription des appareils dans Jamf Pro

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/AndrewMBarnett/ReEnroll/main)

### [Microsoft](https://github.com/microsoft)

 - [Déploiement d'un écran d'accueil pour l'intégration des utilisateurs, utilisant Swift Dialog et Intune.](https://github.com/microsoft/shell-intune-samples/tree/03b181ca16c8a8f677a19a3a45f5943fb36e69b9/macOS/Config/Swift%20Dialog)

   ![Dernier commit GitHub (branche)](https://img.shields.io/github/last-commit/microsoft/shell-intune-samples/master) - Écran d'accueil pour l'intégration d'Intune