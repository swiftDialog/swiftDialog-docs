---
title: Listes d'éléments
description: Création de listes ordonnées dynamiques avec indicateurs de statut et icônes
translationSynced: 2026-11-23T03:21:30+00:00
---

Les listes d'éléments vous permettent d'afficher un nombre raisonnable d'éléments dans une liste ordonnée. Si la liste dépasse la zone visible, elle devient défilante.

Les listes peuvent être intégrées dans une fenêtre de dialogue avec toutes les options de personnalisation existantes, à l'exception des images, qui utilisent toute la surface d'affichage du message.

<hr />
Il existe trois façons de créer une liste d'éléments :

### 1) Ligne de commande

Spécifiez une ou plusieurs `--listitem <text>` entrées comme argument de ligne de commande. La liste sera construite dans l'ordre indiqué.

Les icônes des éléments de liste peuvent être configurées à l'aide d'arguments de ligne de commande `--listitem "<text>,icon=<image>"`, mais si vous avez besoin d'options plus avancées, vous devez utiliser le format JSON.

### 2) JSON

Lorsque vous utilisez JSON comme source de configuration, spécifiez les éléments sous forme d'un tableau unidimensionnel.

#### Basique

La méthode de base est un moyen simple de créer une liste d'éléments sans statut défini.

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### Avancé

L'approche avancée vous permet d'initialiser une liste et, optionnellement, de définir une icône, un statut et un texte de statut pour celle-ci

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### Options de statut

Le statut des éléments de la liste peut être l'un des suivants : `wait`, `success`, `fail`, `error`, `pending` ou `progress`, et une icône appropriée sera affichée dans la zone de statut.

Lorsque `progress` est utilisé comme statut, un compteur de progression circulaire s'affichera comme icône de statut. L'ajout d'un nombre, par exemple `progress: 20`, animera l'indicateur pour le positionner correctement en fonction du pourcentage à afficher. L'indicateur de progression accepte toutes les valeurs comprises entre `0` et `100`

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### Configuration JSON pour chaque argument

À partir de la version 3.1.1, les éléments de liste peuvent également être spécifiés sous forme d'objets JSON via `--listitem` (au lieu d'utiliser le fichier JSON de configuration global). Cela offre un contrôle plus direct et est particulièrement utile pour les configurations complexes avec des objets d'icônes imbriqués.

**Syntaxe :**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**Caractéristiques :**
- `title` - Le texte de l'étiquette de l'élément de la liste
- `status` - Indicateur de statut : `wait`, `success`, `fail`, `error`, `pending`, `progress` ou `progress:<value>` (0-100).
- `statustext` - Texte descriptif affiché à côté de l'indicateur de statut
- `icon` - Chemin d'accès à l'icône, URL, ou **objet JSON représentant une icône imbriquée**

**Objets d'icônes imbriqués :**

Le champ `icon` accepte des objets JSON pour la configuration avancée des icônes :

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**Plusieurs articles :**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**Note :** Lors de l'utilisation de JSON par argument, chaque `--listitem` est indépendant. Le format JSON de configuration globale est toujours pris en charge pour l'initialisation par lots.


### 3) En tant que commande envoyée au fichier de commandes

Envoyez les éléments sous forme de valeurs séparées par des virgules

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## Mettre à jour une liste existante

Les entrées d'une liste déjà affichée peuvent être mises à jour avec un statut en envoyant des commandes au fichier de commandes.


#### Basique

La syntaxe de base requise est la suivante :

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` doit correspondre au nom/titre de l'élément de la liste et la distinction entre majuscules et minuscules est importante
 - `<status text>` peut être n'importe quelle chaîne de caractères Unicode
   - Si l'un des mots-clés de statut pris en charge est envoyé, un indicateur correspondant sera affiché au lieu du texte

#### Avancé

La syntaxe avancée vous permet de modifier le texte et l'indicateur de statut, ainsi que de référencer l'élément de la liste par son index. Les mots-clés sont séparés par des virgules (ce qui signifie que les entrées `title` et `statustext` ne peuvent pas contenir de texte qui inclut une virgule) :

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` commence à 0

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

De nouveaux éléments peuvent être ajoutés à la fin d'une liste existante grâce à la commande `add:`, et les éléments peuvent être supprimés grâce à la commande `delete:`. Lors de l'ajout d'une ligne, les champs "statut" et "statustext" sont facultatifs.

Exemples :

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

supprimer par index : `echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

Supprimer par référence au titre `echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

Il est possible d'ajouter ou de supprimer des éléments d'une liste, même si cette liste n'est pas actuellement affichée.

## Afficher ou masquer une liste

La liste peut être masquée ou affichée sans affecter son contenu.

afficher `echo "list: show"`

cacher `echo "list: hide"`

## Supprimer une liste

Une liste existante peut être supprimée en envoyant la commande `list: clear` au fichier de commandes.

La suppression d'une liste efface toutes les entrées et tous les statuts qui lui sont associés.

## Exemples


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

Ensuite, l'exécution des commandes suivantes mettra à jour l'état de la liste

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### Format JSON avancé

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)