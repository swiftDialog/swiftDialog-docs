---
title: Sélection de listes et de boutons radio
description: Création de listes déroulantes et de groupes de boutons radio pour permettre aux utilisateurs de faire des choix
translationSynced: 2026-11-23T03:09:40+00:00
---

swiftDialog a la capacité de prendre une liste de valeurs et de les afficher sous forme de menu déroulant, avec la possibilité de définir une valeur par défaut.

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## Comment utiliser


### Titre de la liste sélectionnée

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

L'étiquette peut être attribuée à la liste en utilisant l'option de ligne de commande `--selecttitle`. Par exemple : `--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


Ce nom apparaîtra dans la sortie de swiftDialog sur la sortie standard (STDOUT), et il affichera la valeur de l'élément sélectionné. Pour une liste de sélection unique, le format de la sortie standard sera le suivant :
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

Plusieurs `--selecttitle` arguments peuvent être spécifiés. Des arguments `--selectvalues` et `--selectdefault` connexes peuvent également être spécifiés et sont associés à une liste déroulante dans l'ordre de leur présentation

Si plusieurs listes de sélection sont utilisées, les propriétés "SelectedOption" et "SelectedIndex" ne sont pas prises en charge.

L'affichage des résultats pour certains éléments ne s'effectue que si le code de sortie de swiftDialog est égal à 0

### Sélectionner les valeurs de la liste

`--selectvalues <text><csv>`

Les valeurs sont spécifiées au format CSV et sont transmises via l'option de ligne de commande `--selectvalues`, par exemple : `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### Liste sélectionnée par défaut

`--selectdefault <text>`

L'option par défaut peut être définie à l'aide de l'option de ligne de commande `--selectdefault`, par exemple `--selectdefault "Option 4"`

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

Si une valeur par défaut n'est pas spécifiée, et que l'utilisateur ne sélectionne aucun élément de la liste, aucun résultat n'est affiché.


exemple de résultat :
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

La liste des éléments sélectionnés n'est affichée que si le code de sortie de swiftDialog est égal à 0

### Configuration JSON par argument

Les listes sélectionnables peuvent également être définies à l'aide d'objets JSON via `--selectitem` (ou `--selecttitle` avec une valeur JSON). Cela permet de contrôler plus directement les propriétés de chaque élément.

**Syntaxe :**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**Caractéristiques :**
- `title` - L'étiquette pour la liste déroulante
- `values` - Tableau de valeurs possibles
- `default` - La valeur sélectionnée par défaut
- `required` - Indique si le champ est obligatoire (cette option est ignorée pour les boutons radio).
- `style` - Style d'affichage : `list`, `radio`, `searchable` ou `multiselect`
- `name` - Nom alternatif de la clé de sortie

**Exemples :**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

Les éléments JSON sont indépendants des arguments positionnels `--selectvalues/--selecttitle/--selectdefault`. Lors de l'utilisation de JSON, les valeurs sont filtrées à partir de la liste des étiquettes positionnelles afin d'éviter les doublons.

## Schéma JSON

Des listes spécifiques peuvent être définies à l'aide de JSON pour un contrôle plus direct.

### Fichier de configuration JSON complet.

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### JSON par argument

Des éléments individuels peuvent également être définis en utilisant `--selectitem` ou `--selecttitle`, avec un objet JSON :

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

**Remarque :** `--selecttitle` traite les objets JSON de la même manière que `--selectitem`.

### Exemples :

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## Modificateurs

### Nom

Cela permet d'enregistrer la sortie avec le texte spécifié `name` au lieu d'utiliser le titre

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### Recherchable

Le `searchable` modificateur ajoute un champ de recherche à la liste. La saisie de texte dans la zone de texte permettra de filtrer la liste.

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### Radio

Le modificateur `radio` modifie la liste de sélection pour afficher un groupe avec des boutons radio. Lorsqu'on utilise `radio` sans spécifier d'élément par défaut, le premier élément de la liste devient l'élément sélectionné par défaut. Par conséquent, l'utilisation de boutons radio force toujours la sélection d'une des valeurs, et les modificateurs comme `required` sont ignorés.

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### Obligatoire

Le `required` modificateur transformera cet élément de liste spécifique en un champ obligatoire qui doit comporter une valeur avant que swiftDialog ne se ferme

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### Sélection multiple

Le `multiselect` modificateur permet de sélectionner plusieurs options parmi la liste. Les éléments sélectionnés apparaissent sous forme d'étiquettes pouvant être supprimées, et le résultat est une liste de valeurs choisies, séparées par des virgules.

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

Lorsque vous utilisez `multiselect`, les valeurs sélectionnées sont renvoyées sous la forme d'une seule chaîne de caractères séparée par des virgules :

```
"Choose options" : "Option One, Option Three"
```

Ou, au format JSON :
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## Style mondial

`--selectstyle [list | radio | searchable | multiselect]`

Définit le style d'affichage pour **tous** les éléments de la liste sélectionnés dans la boîte de dialogue. Il s'agit d'une option globale équivalente à la définition du modificateur de style pour chaque élément `--selecttitle` individuellement. Les modificateurs de style appliqués à chaque liste `--selecttitle` ont priorité sur ce paramètre global.

| Valeur | Description |
|---|---|
| `list` | Menu déroulant standard (par défaut). |
| `radio` | Groupe de boutons radio |
| `searchable` | Liste déroulante avec un champ de texte pour le filtrage |
| `multiselect` | Champ de recherche permettant de sélectionner plusieurs options |

## Ajouter des sections à la liste

Ajoutez trois tirets ou plus `---` dans votre liste, là où vous avez besoin de séparateurs

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**NOTE :** Chaque `---` sera comptabilisé dans l'index, même si le séparateur lui-même n'est pas sélectionnable. Dans l'exemple ci-dessus, il y aura 7 éléments dans le tableau de la liste, même si seulement 5 sont affichés dans le menu. Veuillez tenir compte de cela lors de la création de vos listes de sélection

## Sortie

Au moment de sa fermeture, le dialogue affichera la valeur sélectionnée par l'utilisateur (ou la valeur par défaut si elle est définie et que l'utilisateur n'a sélectionné aucune valeur) sur `stdout`. Cette sortie peut être analysée par un script, qui pourra ensuite agir en conséquence.

Il y a deux lignes dans la sortie.
* La première ligne contient le texte de l'élément de la liste et sera affichée comme `SelectedOption: <text of item>`
* La deuxième ligne indique l'index de l'élément sélectionné et aura le format suivant : `SelectedIndex: <index of item>`

L'index commence à `0`, donc si le troisième élément de la liste est sélectionné, la valeur de sortie de `SelectedIndex` sera `SelectedIndex: 2`

## Exemple de résultat de lecture

étant donné le résultat suivant :
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

Utilisez les commandes `grep` et `awk` pour extraire la valeur que vous souhaitez traiter

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

ou

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## Ajouter des listes de sélection multiple

Pour ajouter plusieurs listes de sélection, il suffit de spécifier plusieurs occurrences de `--selectvalues`, `--selecttitle` et `--selectdefault`. Le titre et la valeur par défaut seront attribués dans l'ordre dans lequel ils sont définis.


### sélection multiple de résultats

Lorsqu'on utilise plusieurs listes de sélection, la sortie est modifiée pour permettre l'analyse des différentes listes nommées. Par exemple, si l'on utilise le format JSON ci-dessus et que l'on sélectionne "two" et "red", le résultat suivant sera obtenu :

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

Si la sortie est envoyée au format JSON, le résultat serait le suivant :

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```