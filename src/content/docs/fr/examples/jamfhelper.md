---
title: Support technique pour jamfHelper
description: Utiliser swiftDialog comme une solution de remplacement simple pour jamfHelper
translationSynced: 2026-11-23T05:28:08+00:00
---

Dialog dispose désormais de la possibilité d'accepter un ensemble de base d'options de ligne de commande au format jamfHelper grâce au nouveau paramètre `--jh`.

Cela facilite son intégration dans les flux de travail et les scripts existants en remplaçant l'appel à `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` par `/usr/local/bin/dialog --jh`

L'utilisation de cet indicateur permet au système de dialogue de convertir les options de `jamfHelper` en options de dialogue équivalentes. Toutes les options ne sont pas prises en charge. Les options de dialogue standard qui n'ont pas d'équivalent dans `jamfHelper` restent disponibles, par exemple `--width`, `--height` et `--image`.

<br/>

## Caractéristiques et comportement

***
### Mis en œuvre

#### `-windowType [hud | utility | fs]`

`hud` et `utility` sont ignorés. `fs` est converti en dialogue `--fullscreen` et s'affichera en mode plein écran dans les boîtes de dialogue

#### `-windowPosition [ul | ll | ur | lr]`

Positionnez la fenêtre dans le coin supérieur droit, supérieur gauche, inférieur droit ou inférieur gauche de l'écran de l'utilisateur. Il s'agit de la seule fonctionnalité qui ne fait pas actuellement partie des options standard des boîtes de dialogue, mais qui est implémentée pour assurer la compatibilité avec jamfHelper.

#### `-title "string"`
Converti en `--title`

Définit le titre de la fenêtre avec la chaîne de caractères spécifiée

#### `-heading "string"` et `-description "string"`
Converti en `--message`

Les éléments `-heading` et `-description` sont fusionnés dans l'option de dialogue `--message`. `-heading` est converti en un titre de niveau 4 en Markdown `####`, suivi d'une ligne vide, puis de `-description`

#### `-icon path`
Converti en `--icon`

Si cette option n'est pas présente, elle force les dialogues à adopter le comportement de `jamfHelpers`, qui consiste à afficher le résultat sans l'identifiant si celui-ci n'est pas spécifié. `--hideicon`

#### `-button1 "string"`
Converti en `--button1text`

**_Comportement modifié :_** La boîte de dialogue affiche toujours le bouton par défaut, ce qui diffère du fonctionnement de jamfHelper. Le texte du bouton par défaut est `OK`

#### `-button2 "string"`
Converti en `--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
Converti en `--alignment`

Les seules options mises en œuvre sont `right`, `centre` et `left`

#### `-timeout int` et `-countdown`
Converti en `--timer`.

`-countdown` est toujours implicite, car la barre de temporisation apparaît toujours dans la boîte de dialogue, et l'absence de barre de temporisation n'est pas prévue dans la conception de la boîte de dialogue.

<br/>

***
### Non implémenté

#### `-defaultButton [1 | 2]`
Le bouton par défaut est toujours le bouton numéro 1

#### `-cancelButton [1 | 2]`
Le bouton "Annuler" est toujours le bouton numéro 2 (s'il est affiché).

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`