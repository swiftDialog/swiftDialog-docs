---
title: Présentation
description: Création de boîtes de dialogue en mode présentation pour les processus et les tâches en cours
translationSynced: 2026-11-23T04:20:38+00:00
---

## Mode présentation

`--presentation` ou `--style presentation`

Le mode présentation est un mode de fonctionnement de swiftDialog qui ne permet que l'affichage (sans interaction utilisateur) et qui est destiné à visualiser un processus ou une tâche en cours.

La mise à jour de l'affichage nécessitera l'utilisation d'un [fichier de commandes](/fr/advanced/command-file) et des commandes appropriées.

La page est divisée en deux zones principales de contenu, ainsi qu'en une partie inférieure contenant une barre de progression et des boutons.

## Zone d'informations

Le tiers gauche de la fenêtre contient une zone d'informations et peut afficher l'un des éléments suivants :

### Par défaut

Une couleur de fond représentant la préférence de couleur de surlignement de l'utilisateur.

Vous pouvez, si vous le souhaitez, appliquer les modifications suivantes :
 - `--infobox <text>` pour afficher du texte (format Markdown pris en charge).
   - Le texte est centré verticalement
 - `--background color=<color|hex>` pour définir la couleur de fond
   - Si aucune couleur n'est spécifiée, la couleur d'accentuation par défaut du système est utilisée
 - `--icon <image>` pour afficher une icône en haut à gauche
 - `--iconsize <int>` pour définir la taille de l'icône.

### Image

Spécifiez une ou plusieurs `--image <image>` pour remplir cette zone avec une image

Plusieurs images seront présentées sous forme de diaporama. Incluez `--autoplay <sec>` pour que les images se succèdent automatiquement.

**Conseils**
* Utilisez des images au format portrait pour obtenir les meilleurs résultats
* Les images seront redimensionnées pour remplir l'espace, et des recadrages peuvent être effectués si plusieurs images de proportions différentes sont utilisées.

Lancez le mode présentation avec `--debug`, et une taille d'image recommandée pour la fenêtre actuelle sera incluse dans la sortie du journal de débogage une fois que vous aurez fermé la boîte de dialogue.

e.g.

    DEBUG : La taille idéale de l'image de la barre latérale pour ces dimensions de fenêtre serait une largeur de 492.0 pixels et une hauteur de 636.0 pixels

### Contenu web

Spécifiez `--webcontent <url>` pour afficher le contenu d'un fichier source HTML.

**Conseil**
* Si vous utilisez un fichier local, faites référence à ce fichier en utilisant `file:///path/to/file.html`

## Contenu

Les deux tiers droits de la fenêtre sont réservés au contenu, qui peut se présenter sous l'une des formes suivantes :

### Par défaut

Tout `--message <text>`, quelle que soit la forme prise parmi celles qui sont supportées.

### Liste

Un ou plusieurs éléments de liste --listitem <item>, dans l'un des formats supportés.

## Pied de page

Étant donné que l'affichage de la progression et d'autres informations actualisables est la fonction principale du mode présentation, la barre de statut de la fenêtre est toujours visible et est entièrement dédiée à une barre de progression de largeur totale ainsi qu'à des boutons.

## Exemples

**Texte uniquement**

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

Affichage web dans la zone d'informations et éléments de liste dans la zone de contenu

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">