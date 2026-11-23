---
title: Cases à cocher
description: Création de cases à cocher interactives et de commutateurs dans swiftDialog
translationSynced: 2026-11-23T03:28:24+00:00
---

Les cases à cocher peuvent être utilisées pour proposer un certain nombre d'options qui peuvent être sélectionnées ou non, puis traitées.

## Utilisation de base

Spécifiez un ou plusieurs `--checkbox <text>` paramètres, et une case à cocher apparaîtra dans la boîte de dialogue, avec `<text>` comme étiquette.

### Style

Les cases à cocher peuvent également être affichées sous forme de commutateur, plutôt que sous forme de case à cocher.

Par défaut, cela se présente sous la forme d'une case à cocher placée à côté de la légende.

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

Utilisez l'option `--checkboxstyle switch` pour modifier le style de l'interrupteur :

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

Si vous préférez un style de bouton plus grand, vous pouvez spécifier cette préférence en tant que paramètre du style du bouton :

Les options sont `mini`, `small`, `regular` ou `large`

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## Utilisation avancée

Lorsque vous utilisez une [configuration JSON](/fr/advanced/json-configuration) pour définir les options de la boîte de dialogue, des paramètres de case à cocher facultatifs deviennent disponibles.

Le format du fichier JSON est le suivant :

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```

`"checked" : [true|false]` - Initialisera la case à cocher en position cochée si la valeur est fixée à `true`. Par défaut, la case n'est pas cochée.

`"disabled" : [true|false]` - désactivera la case à cocher si elle est réglée sur `true`, quel que soit son état (cochée ou non)

`"icon" : "<file|url>"` - Est disponible en tant que paramètre JSON lorsque `checkboxstyle` est réglé sur `switch`, sinon, il sera ignoré

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### Configuration JSON par argument

À partir de la version 3.1.1, les cases à cocher peuvent également être spécifiées sous forme d'objets JSON via `--checkbox` (au lieu d'utiliser le fichier JSON de configuration complet). Cela offre un contrôle plus précis et est particulièrement utile pour les configurations complexes.

**Syntaxe :**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**Caractéristiques :**
- `label` - Le texte de la légende de la case à cocher
- `checked` - État initial (true/false, par défaut : false).
- `disabled` - Indique si la case à cocher est désactivée (true/false, valeur par défaut : false).
- `enableButton1` - Activer le bouton 1 lorsque cette case à cocher est sélectionnée (true/false).
- `icon` - Chemin d'accès à l'icône ou objet JSON représentant l'icône (uniquement utilisé avec le style `switch`).

**Exemples :**

```bash
# Basic checkbox
dialog --checkbox '{"label":"I agree to terms"}'

# Checked by default
dialog --checkbox '{"label":"Enable notifications","checked":true}'

# Checkbox that enables Button 1
dialog --checkbox '{"label":"I understand","enableButton1":true}' --button1disabled

# Checkbox with icon (switch style)
dialog --checkbox '{"label":"Enable feature","checked":true,"icon":"/System/Library/CoreServices/Software Update.app"}' --checkboxstyle switch

# Checkbox with JSON icon object
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}' --checkboxstyle switch
```

**Remarque :** Lorsque vous utilisez `enableButton1`, assurez-vous également de définir `--button1disabled` pour empêcher l'utilisateur de cliquer sur le bouton avant de cocher la case.

### Configuration JSON complète

Le format JSON pour la configuration complète est toujours pris en charge.

```json
{
  "checkbox" : [
    {"label" : "Option 1", "checked" : true, "disabled" : true },
    {"label" : "Option 2", "checked" : true, "disabled" : false },
    {"label" : "Option 3", "checked" : false }
  ],
  "checkboxstyle" : {
    "style" : "switch",
    "size" : "large"
  }
}
```

### exemple

Le code JSON suivant et la capture d'écran de la boîte de dialogue qui en résulte illustrent le fonctionnement de ces paramètres.

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![image](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## Utilisation d'une case à cocher pour contrôler l'état du bouton1

Vous pouvez utiliser une case à cocher pour contrôler l'état du bouton par défaut. Cela peut être utile si vous souhaitez vous assurer que l'utilisateur a sélectionné une option obligatoire avant de continuer.

Exemple :

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

Ceci peut également être configuré à l'aide de JSON :

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > Il est important de désactiver initialement le bouton1, sinon l'utilisateur pourrait cliquer sur le bouton avant que la case à cocher ne soit cochée. Ce paramètre n'est pas activé par défaut. Il convient également de noter que définir les propriétés `disabled` et `enablebutton1` sur une case à cocher n'est pas recommandé, car cela rendrait la case inaccessible

## Sortie

Les résultats sont envoyés à sdtout et, par défaut, s'affichent comme suit :
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

Facultativement, vous pouvez spécifier le paramètre `--json` et obtenir les résultats au format JSON :

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```