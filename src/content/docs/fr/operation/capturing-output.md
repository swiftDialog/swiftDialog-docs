---
title: Capturer la sortie des dialogues
description: Méthodes de capture des entrées utilisateur et de traitement des résultats des dialogues
translationSynced: 2026-11-23T05:23:41+00:00
---

Il existe plusieurs façons d'obtenir des résultats de Dialog ou de connaître l'action effectuée par un utilisateur, ainsi que toutes les données saisies.

## Codes de retour

Le dialogue le plus simple aura toujours au moins un bouton qui, lorsqu'on clique dessus, permettra de fermer la fenêtre et de renvoyer un code de retour de `0`.

Les boutons optionnels, activés via `--button2`, `--infobutton` (ou leurs équivalents), renvoient un code de retour `2` ou `3`, selon le bouton qui a été cliqué.

Les codes de retour suivants sont envoyés après chaque action. Ils peuvent être ignorés ou utilisés dans un script appelant pour effectuer des actions supplémentaires

| Action      | Facultatif | Raccourci clavier | Code de retour |
| ----------- | -------- | ------ | ----------- |
| bouton1     | Non       | Entrer  | 0           |
| bouton2     | Oui      | Je suis désolé, mais je ne peux pas répondre à cette demande    | 2           |
| bouton d'information  | Oui      |        | 3           |
| \<timer\>   | Oui      |        | 4           |
| fichier de commandes `quit:` | Oui |    | 5           |
| `--quitkey` | Oui      | Cmd+Q  | 10          |
| Échec de l'authentification principale | Oui  |        | 30          |
| Ressource image introuvable | |    | 201         |
| Fichier introuvable |       |        | 202         |


Pour traiter le code de retour dans votre script, il suffit de capturer le résultat provenant de `$?` en utilisant bash ou via le langage de script de votre choix.

Exemple : traitement des codes de retour dans `zsh` :

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## sortie standard

En plus des codes de retour, la sortie sera envoyée à `sdtout` si un ou plusieurs `--textfield` ou `--selectvalues` sont présents. La sortie par défaut n'est pas formatée, hormis la séparation de l'étiquette et de la sortie à l'aide d'un caractère `:`.

Compte tenu du dialogue et des entrées utilisateur suivants :

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

Le résultat serait le suivant :

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` est le texte de l'option sélectionnée dans la liste déroulante. `SelectedIndex` est l'index de l'option sélectionnée (les index commencent à 0, donc l'index 2 correspond à la troisième option listée).

Les champs de texte sont présentés en utilisant l'étiquette transmise à la boîte de dialogue, qui sert d'étiquette dans la sortie. Ainsi, pour l'exemple ci-dessus :

`text 1` affiche le texte que l'utilisateur a saisi dans le champ de texte intitulé "texte 1", et il en va de même pour `text 2`

Pour séparer ces éléments, vous pouvez utiliser `awk` pour traiter chaque ligne de sortie qui vous intéresse, par exemple.
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

Pour un traitement plus avancé, vous pouvez utiliser le paramètre `--json`, qui formatera alors la sortie au format JSON, permettant ainsi son traitement par un analyseur JSON (par exemple, en Python).

La sortie JSON pour l'exemple ci-dessus serait la suivante :
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## Exemples supplémentaires

Capturer la sortie et le code de retour en utilisant Python :
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```