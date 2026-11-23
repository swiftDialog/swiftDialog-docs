---
title: Boîte d'informations
description: Afficher des informations supplémentaires dans une zone de contenu secondaire
translationSynced: 2026-11-23T04:11:27+00:00
---

## Boîte d'informations - `--infobox`

La zone d'informations se trouve sous l'endroit où l'icône est affichée.

Elle utilise une police de caractères plus petite et une couleur secondaire, et est utile pour afficher des informations complémentaires, comme les informations système.

`--infobox` Accepte tout texte formaté en Markdown.

#### Exemple :

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

![Capture d'écran du 10 septembre 2024 à 16h13](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## Largeur de la boîte d'informations - `--infoboxwidth`

Par défaut, la zone d'informations a la même largeur que la colonne des icônes. `--infoboxwidth <number>` permet de définir la largeur de la zone de texte de la zone d'informations (en points) indépendamment de la taille de l'icône, ce qui vous permet d'élargir la zone d'informations sans agrandir l'icône.

`--infoboxwidth 300`