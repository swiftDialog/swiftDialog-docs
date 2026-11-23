---
title: Messages d'aide
description: Ajouter des messages d'aide contextuels aux boîtes de dialogue
translationSynced: 2026-11-23T05:25:59+00:00
---

## Messages d'aide

Les messages d'aide peuvent être un moyen de fournir des informations supplémentaires si nécessaire, sans occuper d'espace supplémentaire dans la fenêtre de dialogue

`--helpmessage <text>`

`<text>` acceptera le format Markdown pour la mise en forme des messages

Lorsqu'elle est disponible, un bouton d'aide supplémentaire apparaîtra à côté du bouton par défaut.


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

En cliquant dessus, un message d'aide s'affichera dans une fenêtre contextuelle

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

La hauteur de la feuille affichée s'ajustera automatiquement en fonction de la taille du message.

### `--helpimage`

Ajoutez une image `--helpimage /path/to/image.png`.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

Prend en charge les arguments standard pour les icônes, y compris les codes QR.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

Définit l'alignement du texte du contenu du message de l'aide. L'alignement par défaut correspond au paramètre d'alignement du message actuel.

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

Définit le texte affiché sur le bouton utilisé pour fermer la fenêtre d'aide. La valeur par défaut est `OK`.