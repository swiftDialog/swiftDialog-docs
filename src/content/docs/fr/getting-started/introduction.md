---
title: Comment démarrer avec swiftDialog
description: Présentation de swiftDialog, un utilitaire de dialogue moderne pour macOS, conçu pour les administrateurs
translationSynced: 2026-11-23T01:41:31+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialog Exemple de message d'accueil](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

L'objectif de swiftDialog est de servir d'outil d'assistance aux administrateurs Mac, qui peuvent l'utiliser via des scripts pour afficher une boîte de dialogue présentant des informations à l'utilisateur et pour signaler l'action que l'utilisateur a effectuée. Ces informations peuvent ensuite être utilisées pour un traitement plus poussé par le script, ou simplement pour afficher un certain type d'information.

swiftDialog accepte les entrées depuis la ligne de commande, en utilisant une ou plusieurs [options de ligne de commande](/fr/advanced/command-line-options) pour indiquer à swiftDialog ce qu'il doit afficher et comment l'afficher.

Il existe plusieurs options qui peuvent être utilisées pour personnaliser l'affichage, allant d'une présentation d'informations très simple à des traitements plus complexes incluant la saisie de texte, des listes déroulantes, l'affichage d'images, et bien plus encore.

## Exécution de swiftDialog

Le programme d'installation **.pkg** de la page [versions](https://github.com/swiftDialog/swiftDialog/releases) installera swiftDialog à l'emplacement `/usr/local/bin/dialog`, qui devrait également figurer dans le `$PATH` par défaut sous macOS

Pour appeler dialog depuis votre script, vous pouvez utiliser le chemin d'accès complet ou vous appuyer sur `$PATH`

```bash
$ dialog --title ...
```

ou

```bash
$ /usr/local/bin/dialog --title ...
```

Au niveau le plus élémentaire, dialog peut simplement utiliser les options de ligne de commande `--title` et `--message` pour afficher une boîte de dialogue avec le message souhaité.

swiftDialog peut faire bien plus que cela, et il est recommandé de consulter la page [Options de ligne de commande](/fr/advanced/command-line-options) pour obtenir la liste complète des options disponibles, ou d'utiliser la commande `dialog` avec l'option `--help`.

## Liens rapides

### Caractéristiques de base
- [Personnalisation du titre de swiftDialog](/fr/basic-use/title)
- [Personnalisation de l'affichage des messages dans swiftDialog](/fr/basic-use/message)
- [Personnalisation de l'image affichée dans la zone d'icône de swiftDialog](/fr/basic-use/icon)
- [Ajouter une image de bannière](/fr/advanced/banner-images)
- [Personnalisation des boutons et de leur comportement](/fr/basic-use/buttons)

### Fonctionnalités avancées
- [Boîte d'informations](/fr/advanced/info-box)
- [Images de bannière](/fr/advanced/banner-images)
- [Message d'aide](/fr/operation/help-message)
- [Listes déroulantes et boutons radio](/fr/advanced/select-lists)
- [Entrée de texte](/fr/advanced/textfields)
- [Cases à cocher](/fr/advanced/checkboxes)
- [Minuteur avec barre de progression](/fr/advanced/timer-progress)
- [Taille et comportement de la fenêtre](/fr/advanced/window-size)
- [Mode plein écran](/fr/advanced/full-screen)
- [Mode présentation](/fr/advanced/presentation)
- [Listes d'éléments](/fr/advanced/item-lists)
- [Notifications système](/fr/advanced/notifications)
- [Modification de CMD+Q](/fr/operation/command-q)
- [Variables intégrées](/fr/operation/builtin-variables)

## Soutien

swiftDialog a été créé en partie comme un exercice d'apprentissage pour développer des applications en utilisant SwiftUI, et en partie pour répondre à un besoin de communiquer des informations aux utilisateurs de Mac d'une manière qui me plaisait.

L'assistance peut être fournie en [ouvrant un ticket](https://github.com/swiftDialog/swiftDialog/issues). Les suggestions d'améliorations sont également les bienvenues.

## Contact

Vous pouvez contacter l'auteur sur le canal #swiftdialog du groupe Slack [Macadmins](https://www.macadmins.org/slack) (nom d'utilisateur @bartreardon, généralement présent dans le canal #anzmac). Cependant, veuillez limiter les demandes de support et les questions générales à GitHub, afin que votre problème puisse être suivi et résolu. Merci ! 😃