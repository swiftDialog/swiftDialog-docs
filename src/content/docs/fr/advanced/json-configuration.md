---
title: Configuration JSON
description: Utiliser JSON pour définir les options de swiftDialog dans les configurations complexes
translationSynced: 2026-11-23T03:26:34+00:00
---

Au lieu d'utiliser de nombreuses options en ligne de commande pour créer des boîtes de dialogue complexes, vous pouvez utiliser les options `--jsonfile` ou `--jsonstring` pour définir les paramètres.

Le format JSON utilise les mêmes options que celles spécifiées dans la ligne de commande, avec quelques exceptions et considérations.

**Remarque :**
 - Les options de ligne de commande peuvent être utilisées en conjonction avec le format JSON, mais les options définies dans le fichier JSON auront toujours la priorité
 - Pour prendre en charge les caractères littéraux `\n` dans le texte du message, `--jsonstring` s'attend à ce que les données JSON soient fournies sur une seule ligne continue

Exemple :

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## Différences par rapport aux options de ligne de commande

Les options qui peuvent être utilisées plusieurs fois peuvent être saisies sous forme de tableau.

Par exemple, pour spécifier plusieurs images et leurs légendes, utilisez un tableau `image` contenant les informations relatives à chaque image et à sa légende `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

Les cases à cocher peuvent être définies comme étant cochées et/ou désactivées. Par défaut, elles ne sont pas cochées `"disabled" : false`, et il n'est pas nécessaire de le spécifier

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

Pour plusieurs options `textfield`, spécifiez un seul champ de texte contenant les noms des champs sous forme de tableau

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### Chaînes de caractères et valeurs booléennes

La plupart des options seront transmises sous forme de chaînes de caractères, nécessitant l'utilisation de guillemets pour les valeurs spécifiées. Certaines valeurs peuvent cependant être spécifiées comme des valeurs booléennes (`true` ou `false`, sans guillemets). Les options qui acceptent une valeur booléenne sont les suivantes :

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### Options non disponibles via JSON

Il existe plusieurs options qui ne peuvent pas être utilisées directement à partir de JSON, car elles n'ont pas de sens dans un contexte de déploiement. Voici les options concernées :

* `--jh` - Utilisé comme un remplacement direct pour accepter les options de ligne de commande de JamfHelper.
* `--listfonts` - utilisé lors de la phase de prototypage pour afficher une liste des polices de caractères disponibles
* `--help` - Affiche le texte d'aide et quitte le programme. Utilisé lors de la phase de prototypage
* `--demo` - affiche une boîte de dialogue en utilisant uniquement les paramètres par défaut. Utilisée lors de la phase de prototypage
* `--version` - Affiche les informations de version de swiftDialog et se termine.
* `--showlicense` - Affiche les informations de licence et se termine
* `--coffee` - Affiche les informations relatives au café et se termine

## Exemple : générer du code JSON en Python et le transmettre sous forme de fichier ou de chaîne de caractères

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```