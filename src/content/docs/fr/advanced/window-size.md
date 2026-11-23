---
title: Taille et comportement des fenêtres
description: Contrôle du positionnement, de la taille et de l'apparence visuelle des boîtes de dialogue
translationSynced: 2026-11-23T03:52:26+00:00
---

Le comportement par défaut de la boîte de dialogue est de s'afficher au centre de l'écran et elle ne peut pas être déplacée. D'autres boîtes de dialogue peuvent être placées au-dessus. Vous pouvez modifier ce comportement en utilisant les options de ligne de commande suivantes.

Chacune de ces options peut être utilisée indépendamment de l'autre.

## Visibilité des fenêtres

`-p` ou `--ontop`

Utilisez cette option pour forcer la fenêtre de dialogue à rester toujours au premier plan.

## Position de la fenêtre

`-o` ou `--moveable`

Utilisez cette option pour permettre de déplacer la fenêtre en la faisant glisser sur l'écran.

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

Positionne la fenêtre de dialogue à l'emplacement spécifié sur l'écran

`--positionoffset <num>`

Définit le décalage des bords de la fenêtre (distance entre les bords de l'écran et la fenêtre).

`--position <x>,<y>`

Positionne la fenêtre de dialogue aux coordonnées x,y spécifiées, par exemple `--position 100,200`

**Remarques :**
 - La position 0,0 correspond au coin supérieur gauche de la zone visible de l'écran
 - La zone visible de l'écran ne comprend pas la surface occupée par la barre d'accès ou la barre de menu. Par exemple, si la barre d'accès est positionnée sur le côté gauche de l'écran, le point d'origine sera décalé vers l'intérieur.


## Taille de la fenêtre

Vous pouvez modifier la taille pour qu'elle soit plus grande ou plus petite que la taille par défaut, en fonction de la quantité de texte que vous souhaitez inclure dans votre message, ou si vous voulez afficher différentes tailles sur des écrans de différentes dimensions. Les images sont redimensionnées en conséquence. La taille de la police de caractères reste inchangée.

`-b` ou `--big`

Cela donne l'impression que la fenêtre est environ 25 % plus grande qu'à l'habitude, ce qui augmente la surface visible des icônes

![image](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` ou `--small`

Cela donne l'impression que la fenêtre est environ 25 % plus petite qu'à l'habitude

![image](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## Apparence de la fenêtre

Vous pouvez forcer l'affichage en mode clair ou en mode sombre, et le système utilisera ce mode, indépendamment des préférences de l'utilisateur

`--appearance dark` ou `--appearance light`

## Mode miniature

Le mode "mini" est activé en passant l'argument `--mini`.

Le mode miniature affiche une petite fenêtre avec une disposition modifiée et des options limitées pour l'affichage du contenu. `--title` est plus petit et est centré en haut de la fenêtre, ou peut être désactivé avec `--title none`. `--message` peut contenir jusqu'à quatre lignes de texte (tout texte plus long sera tronqué). `--icon`, lorsqu'il est visible, occupe la partie gauche de la fenêtre, et tout le contenu restant est affiché à droite. `--hideicon` et `--icon none` sont pris en compte. `--button1text` et `--button2text` sont disponibles, mais le bouton d'information ne l'est pas.

![image](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

Si l'argument `--progress` est utilisé, la zone du bouton est supprimée et remplacée par une barre de progression et une ligne de texte indiquant l'avancement. Pour fermer la boîte de dialogue, la commande `quit:` doit être transmise au fichier de commandes.

![image](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - Configurer un style de fenêtre prédéfini

Modifie les valeurs par défaut pour modifier l'affichage d'une boîte de dialogue.

Les styles autres que `--mini` ne possèdent pas d'attributs spécifiques, et l'apparence visuelle peut être obtenue en utilisant les différents paramètres pour définir les propriétés de la fenêtre.

`centered`, `alert` et `caution` utiliseront la valeur provenant de `--title` et l'ajouteront sous forme de titre dans la zone de message, puis désactiveront l'affichage du titre. Cela place le titre sous l'icône affichée au centre.

    "mini" est fonctionnellement équivalent à "--mini". "centered" définit toutes les options pour un contenu centré. "alert" crée une fenêtre de dialogue préconfigurée de 300x300 pixels avec un contenu centré. "caution" et "warning" sont identiques à "alert", mais affichent une icône

Exemple de `dialog --style alert` :

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

Ceci équivaut à taper :

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## Dimensions de fenêtres sur mesure

swiftDialog peut être de n'importe quelle taille, au lieu des options `--small` ou `--big` par défaut.

`--width` et `--height` peuvent être utilisés pour définir la taille de la fenêtre de dialogue souhaitée. Le contenu sera redimensionné pour s'adapter.

swiftDialog prend en charge l'utilisation de `%` en fonction de la taille actuelle de l'écran, par exemple, `--width 50%` définira la largeur de la boîte de dialogue à 50 % de la résolution actuelle de l'écran.

![image](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` superposera tous les affichages avec un arrière-plan flouté et placera la fenêtre de dialogue au-dessus de toutes les autres fenêtres. Cela permet soit d'afficher des messages plus précis, soit de mettre en place des flux de travail où l'utilisateur ne doit pas interagir avec d'autres applications ou avec le bureau (par exemple, lors de l'intégration).


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### Comportement de `--ontop` avec `--blurscreen` et les fenêtres de dialogue existantes

Si une boîte de dialogue existante est présente et `--blurscreen` est activé, l'utilisation de `--ontop` fera apparaître les boîtes de dialogue suivantes au-dessus de la couche de flou. Cela permet d'afficher un dialogue en arrière-plan tout en lançant des dialogues supplémentaires, qui seront visibles. Il est important de noter que si vous prévoyez d'interagir avec ces dialogues par programmation, assurez-vous d'utiliser des fichiers de commande uniques pour chacun d'eux.

## `--showonallscreens`

Lorsqu'elle est utilisée, la fenêtre de dialogue s'affiche sur tous les bureaux virtuels

Si plusieurs écrans sont utilisés, la boîte de dialogue apparaîtra sur tous les bureaux virtuels associés à l'écran sur lequel elle a été lancée.