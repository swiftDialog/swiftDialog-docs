---
title: Personnalisation du titre
description: Apprenez comment définir et personnaliser le texte du titre ainsi que les propriétés de la police dans swiftDialog
translationSynced: 2026-11-23T02:17:19+00:00
---

## Définition du texte du titre

Utilisez l'option de ligne de commande `-t` ou `--title` pour spécifier le texte que vous souhaitez afficher dans la zone de titre de la boîte de dialogue.

Exemple :

`--title "An Important Message"`

`-t "An Important Message"`

La zone de titre est une zone de largeur fixe et en gras, située en haut de la fenêtre de dialogue. Tout texte qui dépasse la largeur de la fenêtre sera tronqué

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## Personnalisation des propriétés de la police de caractères du titre

Utilisez l'option de ligne de commande `--titlefont` pour définir les propriétés de police du titre.

### Syntaxe CSV

Les propriétés de la police sont exprimées sous la forme de `property=value`, et plusieurs propriétés sont séparées par une virgule

Les propriétés pouvant être modifiées sont les suivantes :
 * `colour=<hex_value>` (alternativement `color=<hex_value>`)
   * spécifié au format hexadécimal, par exemple : #00A4C7
 * `size=<float>`
   * Accepte toute valeur décimale, par exemple 30, 65, 72.3
 * `weight=<text>`
   * Accepte les valeurs : thin, light, regular, medium, heavy ou bold (par défaut).
 * `name=<fontname>`
   * Accepte un nom de police ou une famille de polices. La liste des noms disponibles peut être obtenue à l'aide de `--listfonts` ou en consultant l'application macOS Font Book.
 * `alignment=[left|right]`
   * Positionne le texte du titre en alignement à gauche ou à droite
 * `offset=<float>`
   * Déplace le texte du titre horizontalement d'un nombre de points spécifié. Les valeurs positives déplacent le texte vers la droite, tandis que les valeurs négatives le déplacent vers la gauche. Lorsque vous utilisez `alignment=right`, la direction du décalage est automatiquement inversée, de sorte qu'une valeur positive déplace toujours le texte vers le bord droit.
 * `shadow`
   * Ajoute une ombre portée au texte (booléen, aucune valeur n'est nécessaire).

 > **ATTENTION :** Soyez prudent lorsque vous combinez les noms de polices et les épaisseurs. Lorsque vous spécifiez une police ou une famille de polices par son nom, certaines épaisseurs peuvent ne pas être disponibles. Si cela se produit, l'épaisseur de police spécifiée sera ignorée.

Vous pouvez utiliser une ou plusieurs de ces options, et l'ordre dans lequel elles sont spécifiées n'a pas d'importance. Par exemple, si vous souhaitez uniquement modifier la taille, vous pouvez utiliser la configuration suivante :

`--titlefont "size=60"`

Exemple 1 : `--titlefont "colour=#00A4C7,weight=light,size=60"`

Cet exemple définit la couleur à la valeur `#00A4C7`, le poids à `light` et la taille de la police à `60`, et apparaîtra ainsi :

<img width="400" alt="image" src="/images/titlefont1.png" />

Exemple 2 : `--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

Cet exemple définit la couleur à la valeur `#D054A0 `, la taille à `40` et utilise le nom de police "Chalkboard-Bold" :

<img width="400" alt="image" src="/images/titlefont2.png" />

Exemple : Alignement à gauche/à droite :

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### Syntaxe des objets JSON

À partir de la version 3.1.1, `--titlefont` et `--messagefont` peuvent également être spécifiés sous forme d'objets JSON pour un contrôle plus précis :

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**Caractéristiques :**
- `name` - Nom ou famille de police
- `size` - Taille de la police en points
- `colour` / `color` - Couleur du texte (code hexadécimal ou nom de couleur).
- `weight` - Épaisseur de la police : `thin`, `light`, `regular`, `medium`, `heavy`, `bold`
- `alignment` - Alignement du texte : `left`, `right` (titre uniquement).
- `offset` - Décalage horizontal en points (pour le titre uniquement).
- `shadow` - Ajouter une ombre portée (booléen).

**Exemples :**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**Remarque :** La clé `shadow` est désormais prise en charge au format JSON (elle n'était auparavant disponible qu'au format CSV).

### Utiliser la couleur dans le titre

L'utilisation de `colour=<value>` permet de définir la couleur de base du texte, mais vous pouvez définir la couleur de mots ou de lettres individuels en utilisant le format `:colour[text]`

Exemple :

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## Sous-titre

Utilisez `--subtitle <text>` pour afficher une ligne de texte secondaire en dessous du titre, en utilisant la même police mais d'une taille plus petite.

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

Le sous-titre hérite du même nom de police, de la même épaisseur et de la même couleur que le titre, mais il est affiché à `titlefont size − 10pt`.

#### Masquer la zone du titre

Utilisez le mot-clé `none` pour masquer la zone du titre. Cela supprimera la barre de titre et la ligne de séparation horizontale

e.g. `--title none`




