---
title: Boutons et comportement des boutons
description: Apprenez comment configurer le texte, les actions et le comportement des boutons dans swiftDialog
translationSynced: 2026-11-23T08:35:52+00:00
---

La boîte de dialogue peut afficher jusqu'à trois boutons.

Les boutons sont affichés dans la partie inférieure de la fenêtre de dialogue

![Zone des boutons de dialogue](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## Bouton 1 : Le bouton par défaut
Par défaut, un seul bouton est affiché, avec le libellé "**OK**". Le bouton par défaut est toujours présent, est associé à la touche **_Enter_** et permet de quitter l'application Dialog avec le code de sortie `0`

L'étiquette du bouton par défaut peut être modifiée avec n'importe quelle quantité de texte en utilisant l'option `--button1text`

e.g. `--button1text "Enter to Continue"`

![Texte du bouton 1 ](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

L'action peut également être modifiée en utilisant l'option `--button1action`, ce qui signifie qu'en plus de simplement quitter l'application Dialog, vous pouvez effectuer une autre action

À ce stade, les actions possibles se limitent à l'ouverture d'une URL dans le navigateur par défaut de l'utilisateur.

e.g. `--button1action "https://github.com/"`

## Bouton 2 : Le bouton d'annulation
Le deuxième bouton est masqué par défaut. Il peut être affiché en utilisant l'option `-2` ou `--button2`, qui fera apparaître le bouton avec le libellé par défaut "**Cancel**". Le deuxième bouton est associé à la touche **_Esc_** et permet de quitter l'application Dialog avec le code de sortie `2`

L'étiquette du deuxième bouton peut être modifiée avec n'importe quelle quantité de texte en utilisant l'option `--button2text`. Lorsque vous utilisez cette option, vous n'avez pas besoin d'utiliser l'option `--button2`. L'affichage du bouton est implicite si vous modifiez l'étiquette textuelle.

Exemple :

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![Bouton 2 avec le texte "I Don't Care"](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

Le bouton 2 ne possède aucune autre fonction programmée

## Le bouton "Pour plus d'informations"
Le bouton "Plus d'informations" est masqué par défaut. Il peut être affiché en utilisant l'option `-3` ou `--infobutton`, ce qui fera apparaître le bouton avec le libellé par défaut "**More Information**". Cliquer sur le bouton fermera swiftDialog et renverra un code de sortie de `3`

Si l'argument `--infobuttonaction` est présent, cliquer sur le bouton "Plus d'informations" ne déclenchera que l'action `--infobuttonaction`, et la fenêtre swiftDialog ne se fermera pas automatiquement. Si l'argument `--quitoninfo` est ajouté, le comportement de fermeture sera rétabli.

L'étiquette du bouton d'information peut être modifiée avec une quantité de texte arbitraire en utilisant l'option `--infobuttontext`. Lorsque vous utilisez cette option, vous n'avez pas besoin d'activer l'option `--infobutton`. L'affichage du bouton est implicite si vous modifiez l'étiquette textuelle.

Exemple :

`--infobuttontext "Click here for more details"`

![Bouton "Info" : cliquez pour plus de détails](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

L'action peut également être modifiée en utilisant l'option `--infobuttonaction`, ce qui signifie qu'en plus de simplement quitter l'application Dialog, vous pouvez effectuer une autre action

À ce stade, les actions possibles se limitent à l'ouverture d'une URL dans le navigateur par défaut de l'utilisateur.

e.g. `--infobuttonaction "https://github.com/"`

## Symboles des boutons

Définit le symbole SF à utiliser en complément de la légende du bouton

### Syntaxe CSV

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

Prend le nom du symbole SF en argument

Propriétés facultatives fournies sous forme de valeurs séparées par des virgules (dans n'importe quel ordre) :
 - position : l'une des valeurs suivantes : leading, trailing, top, bottom. La valeur par défaut est leading
 - mode de rendu : l'un des modes suivants : hierarchical, monochrome, multicolour, palette. Par défaut : monochrome
 - palette : ajoutez deux ou trois couleurs en utilisant le format suivant : palette=colour1-colour2-colour3
   - Par exemple : palette = red-green-blue
 - taille : au format size=<num>
 - couleur : au format color=<text|hex>
   - Si le mode de rendu multicolore est activé, la couleur est ignorée

Exemple :

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### Syntaxe des objets JSON

À partir de la version 3.1.1, les symboles des boutons peuvent également être spécifiés sous forme d'objets JSON, ce qui permet un contrôle plus précis.

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**Caractéristiques :**
- `name` - Nom du symbole SF (obligatoire).
- `position` - Position du symbole : `leading`, `trailing`, `top`, `bottom` (par défaut : `leading`)
- `colour` / `color` - Couleur du symbole (code hexadécimal ou nom).
- `size` - Taille du symbole en points
- `rendering` - Mode de rendu : `hierarchical`, `monochrome`, `multicolour`, `palette`
- `palette` - Tableau de 2 à 3 couleurs pour les symboles multicolores (séparés par des virgules dans un fichier CSV, sous forme de tableau dans un fichier JSON).

**Exemples :**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**Remarque :** Lorsque vous utilisez `rendering: palette`, la palette doit être un tableau au format JSON : `["red","green","blue"]`. Sous forme de fichier CSV, utilisez des tirets pour séparer les valeurs : `palette=red-green-blue`.

## Position du bouton

Par défaut, le bouton 1 et le bouton 2 se trouvent à droite, tandis que le bouton d'information se trouve à gauche.

L'utilisation de `--buttonstyle center` placera les boutons 1 (et 2, s'ils sont présents) au centre inférieur de la fenêtre de dialogue

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` et `--infotext` ne sont pas compatibles lors de l'utilisation de l'option `--buttonstyle center`

## Style "empilé" pour les boutons

`--buttonstyle stack`

Affiche les boutons 1 et 2 dans un bloc occupant toute la largeur.

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` et `--infotext` ne sont pas compatibles lors de l'utilisation de l'option `--buttonstyle stack`

## Comportement des touches `[return]` et `[enter]`

Sans champs de saisie, l'élément de contrôle de saisie actif dans la boîte de dialogue est `button1`, et les touches `[enter]` et `[return]` activeront le bouton, car il s'agit du seul élément interactif de la fenêtre et bénéficie donc de la saisie par défaut du clavier. L'effet est que cela ferme la boîte de dialogue (en supposant que le bouton est actif et non désactivé).

La touche `[return]` active toujours le bouton1, sauf si un champ de saisie est sélectionné. La touche `[enter]` n'active que l'élément actuellement sélectionné (c'est pourquoi elle permet de fermer la boîte de dialogue sur les fenêtres qui ne contiennent pas d'éléments de saisie).

Dans un champ de texte à une seule ligne, `[return]` ne permet pas d'ajouter un saut de ligne, et donc l'action par défaut prend le dessus et ferme la boîte de dialogue (active le gestionnaire par défaut). En revanche, `[enter]` n'a aucun effet, car il ne permet pas non plus d'ajouter un saut de ligne, mais comme il n'a aucun contrôle sur l'action du gestionnaire par défaut, rien ne se passe.

Dans un champ de texte multiligne (c'est-à-dire `--textfield` avec `editor` activée), la touche `[return]` *peut* insérer un retour à la ligne, et cette action prend le pas sur toute autre action par défaut (par exemple, l'action d'un bouton1 qui fermerait la fenêtre). La touche `[return]` fonctionne également comme prévu et insère une nouvelle ligne.

### Modifier le comportement par défaut de `[return]`, `[enter]` ou `[esc]`

Si vous ne souhaitez pas que les actions par défaut de `[return]`, `[enter]` ou `[esc]` ferment la fenêtre de dialogue, vous pouvez utiliser l'option `--hidedefaultkeyboardaction` pour modifier ce comportement. Cette option modifiera les touches par défaut `[return]` ou `[escape]` pour qu'elles nécessitent également l'utilisation des touches `cmd`+`shift` pour être activées. Cela permet de réduire le risque de fermer accidentellement une fenêtre de dialogue.

## Codes de retour

Les codes de retour suivants sont envoyés après chaque action. Ils peuvent être ignorés ou utilisés dans un script appelant pour effectuer des actions supplémentaires

| Nom du bouton | Facultatif | Raccourci clavier | Code de retour |
| ----------- | -------- | ------ | ----------- |
| `button1`   | Non       | Enter  | 0           |
| `button2`   | Oui      | Esc    | 2           |
| `infobutton` | Oui      |        | 3           |

## Désactivation des boutons

Les boutons 1 et 2 peuvent être désactivés au démarrage en utilisant l'une des commandes suivantes :

`--button1disabled`

`--button2disabled`

Le bouton 1 peut être complètement masqué en définissant le texte du bouton sur `none`

_Notez que cela désactive également l'utilisation de la touche [return] pour fermer une boîte de dialogue, assurez-vous donc de prévoir un moyen de fermer la boîte de dialogue._