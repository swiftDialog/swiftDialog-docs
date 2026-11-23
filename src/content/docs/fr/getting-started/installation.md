---
title: Installation
description: Comment installer swiftDialog sur macOS
translationSynced: 2026-11-23T01:52:14+00:00
---

## Méthodes d'installation

### Installateur de paquets (recommandé)

La manière la plus simple d'installer swiftDialog est d'utiliser le programme d'installation **.pkg** disponible sur la [page des versions](https://github.com/swiftDialog/swiftDialog/releases).

L'installateur placera swiftDialog à `/usr/local/bin/dialog`, qui devrait se trouver dans le `$PATH` par défaut sous macOS.

### Installation manuelle

Si vous préférez une installation manuelle :

1. Téléchargez la dernière version depuis la [page des versions](https://github.com/swiftDialog/swiftDialog/releases)
2. Extrayez le fichier binaire
3. Copiez-le dans `/usr/local/bin/dialog` ou dans un autre emplacement de votre `$PATH`
4. Assurez-vous que le fichier binaire dispose des permissions d'exécution : `chmod +x /usr/local/bin/dialog`

### Installation avec Homebrew

Bientôt disponible : la formule Homebrew est en cours de développement.

## Vérification

Après l'installation, vérifiez que swiftDialog fonctionne correctement :

```bash
dialog --version
```

Ou testez-le avec une simple boîte de dialogue :

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## Mise à jour de swiftDialog

Pour mettre à jour swiftDialog, il suffit de télécharger et d'installer la dernière version. Le programme d'installation remplacera la version existante.

Vous pouvez vérifier la présence de mises à jour de manière programmatique en utilisant :

```bash
dialog --checkupdates
```

## Désinstallation

Pour supprimer swiftDialog :

```bash
sudo rm /usr/local/bin/dialog
```

## Déploiement via MDM (Mobile Device Management)

swiftDialog peut être déployé via des solutions de gestion des appareils mobiles (MDM) telles que Jamf Pro, Mosyle ou Kandji. Il suffit de déployer le fichier d'installation .pkg sur les appareils gérés.

### Exemple de politique Jamf

1. Téléchargez le fichier .pkg de swiftDialog vers Jamf Pro
2. Établir une politique de déploiement pour ce paquet
3. Adaptez les paramètres à vos appareils
4. Définir un déclencheur (enregistrement, récurrent, auto-service, etc.).