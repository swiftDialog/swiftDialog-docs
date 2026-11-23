---
title: Images de fond
description: Ajouter des images de fond et des filigranes aux fenêtres de dialogue
translationSynced: 2026-11-23T03:18:50+00:00
---

## Images de fond

Les images peuvent être affichées en arrière-plan, au sein de la boîte de dialogue principale, ce qui permet d'intégrer un filigrane ou une autre image derrière le contenu habituel de la fenêtre.

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

Les arrière-plans peuvent être contrôlés à l'aide des éléments suivants :

### `--background`

```
-bg, --background <file | url | colour= >
```

Affiche le fichier sélectionné en tant qu'image de fond. Si l'image est plus grande que la taille par défaut de la boîte de dialogue (820x380) et qu'aucune option de taille de fenêtre n'est spécifiée (notamment la hauteur de la fenêtre), la hauteur de la boîte de dialogue sera ajustée pour que l'image remplisse toute la largeur de la fenêtre, soit par défaut 820, ou selon la valeur spécifiée en utilisant `--width`

Alternativement, une couleur unie peut être spécifiée en utilisant le préfixe `colour=`. La couleur peut être définie par une valeur hexadécimale ou par un nom de couleur.

Par exemple : `--background colour=red` ou `--background colour=#ff0000`

Par défaut, un dégradé subtil est appliqué aux couleurs unies. Ajoutez `,nogradient` pour le désactiver :

`--background colour=red,nogradient`

Un dégradé linéaire peut être spécifié en utilisant le préfixe `gradient=`. Indiquez deux couleurs ou plus, séparées par des virgules, et, facultativement, définissez la direction avec `:angle=<degrees>` :

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

Conventions d'angle : `0` = de bas en haut, `90` = de gauche à droite (par défaut), `180` = de haut en bas, `270` = de droite à gauche.

Si une seule couleur est fournie à `gradient=`, le résultat est identique à celui obtenu avec `colour=`.


### `--bgalpha`

```
-ba, --bgalpha <number>
```

Définit la valeur alpha, ou la transparence, de la couche de fond. La valeur peut être n'importe quel nombre compris entre `0` (totalement transparent) et `1` (totalement opaque). La valeur par défaut est `0.5`


### --bgposition

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

Positionne l'image de fond dans la fenêtre. Cette fonctionnalité fonctionne le mieux si les dimensions de l'image sont inférieures à celles de la fenêtre principale, par exemple pour un logo d'entreprise. La position par défaut est `centre`


### --bgfill

```
-bf, --bgfill [fill | fit]
```

Indique à swiftDialog comment afficher l'image à l'intérieur de la boîte de dialogue

`fill` Redimensionne l'image pour qu'elle remplisse toute la fenêtre. L'image sera rognée si nécessaire. `fit` Redimensionne l'image pour qu'elle s'adapte à la fenêtre, mais ne la rogne pas, ce qui peut entraîner des bandes noires sur les zones non transparentes (si l'image source est au format PNG).

Par défaut, la valeur est `none`, ce qui affiche l'image à sa résolution réelle

## Fond d'écran - `--screenbackground`

```
--screenbackground <file | url>
```

Affiche l'image spécifiée en mode plein écran, *derrière* la fenêtre de dialogue — contrairement à `--background`, qui est affiché *à l'intérieur* de la fenêtre de dialogue. Toutes les autres fonctions de la fenêtre de dialogue restent accessibles, mais l'utilisateur ne peut interagir avec aucune autre application tant que swiftDialog est actif (similaire à `--blurscreen`, mais affichant une image au lieu d'un flou).

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```