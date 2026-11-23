---
title: Images de bannière
description: Affichage d'images en haut des boîtes de dialogue, avec possibilité d'ajouter un texte de titre en superposition
translationSynced: 2026-11-23T03:15:14+00:00
---

Utilisez l'option de ligne de commande `-n` ou `--bannerimage` pour spécifier une image à afficher en haut de la boîte de dialogue.

Utilisation :

`--bannerimage <file | url | colour= >`

L'utilisation d'une image de bannière désactivera l'affichage de la zone de l'image de l'icône. Cela équivaut à utiliser l'option `--hideicon`

## Utilisation de base

swiftDialog accepte les images aux formats png et jpg et affiche l'image spécifiée dans la zone de bannière. L'image de bannière fait au maximum 150 points de hauteur et s'étend sur toute la largeur de la boîte de dialogue. Combinée à l'option `-s` ou `--small`, la hauteur de l'image de bannière est limitée à 100 points

Toute image de taille quelconque peut être utilisée. La zone d'affichage de l'image s'adaptera à la taille de l'image de bannière que vous souhaitez utiliser, jusqu'à une hauteur maximale de 150 points.

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

Une hauteur spécifique peut être définie en utilisant l'option `--bannerheight`. Cela remplacera la hauteur par défaut.

De plus, une couleur unie peut être spécifiée en utilisant le préfixe `colour=`. La couleur peut être définie soit par une valeur hexadécimale, soit par un nom de couleur.

Exemple :

`--bannerimage colour=red` ou `--bannerimage colour=#ff0000`

Par défaut, un dégradé subtil, passant du blanc à une couleur puis au noir, est appliqué aux couleurs unies. Ajoutez `,nogradient` pour le désactiver :

`--bannerimage colour=red,nogradient`

### Bannières dégradées

Un dégradé linéaire peut être spécifié en utilisant le préfixe `gradient=`. Indiquez deux couleurs ou plus, séparées par des virgules, et, facultativement, définissez la direction avec `:angle=<degrees>` :

```sh
--bannerimage "gradient=red,blue"
--bannerimage "gradient=red,orange,yellow:angle=135"
```

Conventions d'angle : `0` = de bas en haut, `90` = de gauche à droite (par défaut), `180` = de haut en bas, `270` = de droite à gauche.

Si une seule couleur est fournie à `gradient=`, le résultat est identique à `colour=` (effet de superposition du blanc à la couleur, puis au noir).

## Texte du titre affiché dans la zone de bannière

`--bannertitle`

En utilisant cette commande, vous pouvez afficher le texte du titre dans la bannière. Cela impose par défaut une couleur blanche pour le texte, mais celle-ci peut être modifiée grâce aux [options de personnalisation de la police du titre](/fr/basic-use/title#personnalisation-des-propriétés-de-la-police-de-caractères-du-titre).

Vous pouvez l'utiliser comme une option pour `--title`, ou vous pouvez fournir une chaîne de caractères qui sera affichée comme titre. Si `--title` et `--bannertitle` reçoivent tous deux des arguments de type chaîne de caractères, `--bannertitle` prendra le pas.

Tous les modificateurs `--titlefont` s'appliquent au texte du titre de la bannière, y compris `shadow`, `colour`, `size`, `weight`, `alignment` et `offset`.

`--titlefont shadow=1` Applique une ombre portée sous le texte.

Si `--subtitle` est également activé, le sous-titre est affiché sous le titre, à l'intérieur de la zone de bannière, en utilisant la même police, mais avec une taille plus petite.

![image](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)