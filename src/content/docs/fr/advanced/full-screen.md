---
title: Plein écran
description: Création de boîtes de dialogue en plein écran pour les présentations et les modes kiosque
translationSynced: 2026-11-23T03:24:55+00:00
---

L'affichage en plein écran est pris en charge grâce aux options de ligne de commande `--fullscreen` ou `-f`.

Dans cette configuration, seuls le titre, l'icône et le message sont visibles. Les autres options peuvent être spécifiées, mais ne seront pas affichées. Cependant, la boîte de dialogue réagit toujours aux entrées clavier (touches `escape` et `enter`), et se ferme avec le code de sortie approprié.

La zone d'affichage s'adaptera à différentes résolutions, allant de 1024x640 jusqu'à 5K. (Nous acceptons les dons de moniteurs XDR pour tester les résolutions 6K).

Les options se comporteront légèrement différemment en mode plein écran par rapport au mode normal.

### `--bannerimage` `-n`

Les images de bannière sont affichées au centre, en haut de l'écran, et peuvent occuper jusqu'à une largeur maximale de 95 % de la surface d'affichage et une hauteur maximale de 10 % de la surface d'affichage. Cela permet d'afficher des images de bannière longues et étroites, si nécessaire.

L'affichage d'une bannière affiche également une ligne horizontale en dessous, qui occupe également 95 % de la largeur de la zone d'affichage.

### `--title` `-t`

Le titre, placé en haut de l'écran ou directement sous une bannière, occupera toute la largeur de l'affichage.

### `--icon` `-i`

Les images d'icônes sont affichées, centrées, sous le titre. Les sources d'images standard sont acceptées, mais cette fonctionnalité ne prend pas en charge l'option de superposition d'icônes.

### `--message` `-m`

La zone de message occupera tout l'espace disponible à l'écran, en dessous du titre, de la bannière et des icônes. Elle sera centrée verticalement et horizontalement, et occupera toute la largeur de l'écran.

Si la bannière, le titre et l'icône sont tous utilisés, la zone de message occupera les 40 à 50 % inférieurs de l'écran (une plus grande surface d'affichage est disponible sur les écrans plus grands). Si l'icône et la bannière sont omis, les 60 à 75 % inférieurs de l'écran sont utilisés.

Chaque ligne de texte dans la zone de message est espacée double, jusqu'à un maximum de 12 lignes.

## Exemples

Ces exemples illustrent l'apparence de l'écran en mode plein écran sur un écran standard de 13 pouces, avec les zones de contenu mises en évidence.

### Vue simplifiée, affichant uniquement le titre et le message

<img width="1000" alt="Screenshot1" src="https://user-images.githubusercontent.com/3598965/114690586-306d0280-9d5a-11eb-9504-1e2d25f93711.png">


### Utilisation de toutes les options, avec ajout d'une image de bannière et d'une icône

<img width="1000" alt="Screenshot2" src="https://user-images.githubusercontent.com/3598965/114690604-3531b680-9d5a-11eb-94c5-242693f6d335.png">