---
title: Personnalisation de la zone de message
description: Apprenez à configurer et personnaliser le texte du message, les propriétés de la police et le positionnement dans swiftDialog
translationSynced: 2026-11-23T02:40:16+00:00
---

Utilisez l'option de ligne de commande `-m` ou `--message` pour spécifier le contenu que vous souhaitez afficher dans la zone de message de la boîte de dialogue.

Exemple :

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

La zone de message peut occuper soit les 2/3 de la largeur de la fenêtre de dialogue, soit toute la largeur si la zone des icônes n'est pas affichée

Les messages seront coupés en plusieurs lignes si leur longueur dépasse la largeur de la zone d'affichage, et ils défilent si leur longueur dépasse la zone d'affichage totale.


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### Source du contenu

En plus de fournir une chaîne de texte, vous pouvez également fournir le chemin d'accès ou l'URL vers un fichier Markdown. Tout fichier se terminant par `.md` sera considéré comme un fichier source Markdown.

Exemple :

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## Positionnement du message

`--messagealignment` et `--messageposition` vous permettent de spécifier la position du message dans la boîte de dialogue. Cela est utile pour créer des boîtes de dialogue où le message est centré verticalement et horizontalement.

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## Modifier la police, la couleur, la taille et l'alignement du message

`--alignment [left | centre | center | right]`

Définissez l'alignement du message. La valeur par défaut est 'left'

`--messagefont <text>`

Permet de modifier la police de caractères, la taille du texte et la couleur du message.

`color,colour=<text><hex>`

> `<text>` peut être n'importe quelle des couleurs standard d'Apple : `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Par défaut, si l'option est invalide, la couleur principale du système est utilisée (généralement `black` en mode clair ou `white` en mode sombre).

> `<hex>` est spécifié au format hexadécimal, par exemple : #00A4C7

`size=<float>` accepte toute valeur décimale (par exemple, 15.7, 20, 32.0).

`name=<fontname>` - accepte le nom de toute police de caractères installée


Exemple : `--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### Utiliser une couleur supplémentaire dans le message

L'utilisation de `colour=<value>` permet de définir la couleur de base du message, mais vous pouvez définir la couleur de mots ou de lettres individuels en utilisant le format `:colour[text]`.

Exemple :

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

