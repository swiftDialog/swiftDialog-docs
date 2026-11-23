---
title: Lanceur d'interface en ligne de commande Dialog
description: Comment fonctionne l'exécutable de l'interface en ligne de commande (CLI) de Dialog, ainsi que les options de niveau utilitaire
translationSynced: 2026-11-23T05:22:49+00:00
---

La commande `dialog` disponible à `/usr/local/bin/dialog` n'est pas l'application Dialog elle-même, mais un lanceur CLI (ligne de commande) léger (`dialogcli`) qui englobe le fichier binaire Dialog.app. Comprendre ce qu'elle fait est utile lors du déploiement ou de la création de scripts avec swiftDialog.

---

## Ce que fait le lanceur

Lorsque vous exécutez `dialog`, le lanceur :

1. Localise le fichier exécutable de Dialog.app par rapport à son propre chemin, situé à l'intérieur du paquet de l'application.
2. **Crée le fichier de commandes** à `/var/tmp/dialog.log` (ou au chemin spécifié avec `--commandfile`) s'il n'existe pas déjà. Si le chemin est un lien symbolique, le lanceur s'interrompt pour éviter les risques de sécurité.
3. **Identifie l'utilisateur de l'interface graphique (GUI) actuel** en utilisant `SCDynamicStoreCopyConsoleUser`. Si aucun utilisateur de l'interface graphique n'est actif et que `--loginwindow` n'est pas spécifié, le lanceur se termine avec le code `1`.
4. **Exécute la boîte de dialogue dans le contexte utilisateur approprié.** Lorsqu'il est appelé en tant que root (par exemple, à partir d'une politique Jamf ou d'un LaunchDaemon), le lanceur utilise `launchctl asuser` pour exécuter la boîte de dialogue en tant qu'utilisateur graphique connecté, de sorte que la fenêtre apparaisse sur la session d'affichage correcte.
5. **Transmission automatique `--pid`** — l'identifiant de processus (PID) propre au lanceur est injecté `--pid <pid>` afin que Dialog puisse surveiller le processus appelant et se terminer si celui-ci se termine.
6. **Notifications avec style spécifique** — lorsque les éléments `--notification` et `--style alert` ou `--style banner` sont utilisés, le lanceur transfère l'appel à l'application auxiliaire de notification intégrée appropriée, plutôt qu'à l'exécutable principal de Dialog.

---

## Création du lien symbolique

Le lanceur inclut un `--link` indicateur qui crée un `/usr/local/bin/dialog` lien symbolique pointant vers lui-même. Cette opération doit être exécutée avec les droits de l'administrateur (root) :

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

Cela est généralement géré automatiquement par le paquet d'installation de swiftDialog.

---

## Options de fonctionnalités

Ces options sont gérées directement par le logiciel Dialog et sont principalement utiles pour les scripts d'administration ou de déploiement.

### `--setappicon <file>`

Définit l'icône de l'application swiftDialog sur le fichier image spécifié, puis se termine immédiatement. Cela met également à jour les icônes de toutes les applications auxiliaires de notification intégrées.

```sh
dialog --setappicon /path/to/custom-icon.png
```

Il s'agit d'une opération unique : Dialog n'affichera aucune fenêtre. Elle est conçue pour permettre une personnalisation après l'installation, afin que l'icône du Dock et les notifications correspondent à l'identité visuelle de votre organisation.

### `--callingpid <int>`

Surveille l'identifiant de processus spécifié. Si ce processus se termine, Dialog se ferme automatiquement avec le code `40`.

```sh
dialog --title "Installing..." --callingpid 12345
```

Ceci est injecté automatiquement par le `dialogcli` lanceur (en utilisant son propre PID), de sorte que Dialog se fermera si le script ou le processus appelant est interrompu. Vous pourriez spécifier un PID différent, ce qui lierait Dialog à un processus différent, mais ce cas d'utilisation n'est pas pris en charge.

Le code de sortie **40** est renvoyé lorsque Dialog se termine en raison de la fin du processus surveillé.
