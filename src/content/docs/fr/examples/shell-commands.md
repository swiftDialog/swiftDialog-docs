---
title: Commandes Shell
description: Fonctionnalité expérimentale permettant d'exécuter des commandes shell à partir des actions déclenchées par des boutons
translationSynced: 2026-11-23T05:27:43+00:00
---

La version 1.1.2 introduit une fonctionnalité expérimentale via la commande `button1shellaction`


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

Elle prend un seul paramètre de type chaîne de caractères et le transmet à un shell pour qu'il l'exécute, par exemple.

` --button1shellaction "say thank you for running dialog"`

Actuellement, il n'y a ni de validation des entrées, ni de validation des sorties. Si la commande spécifiée se termine avec une erreur, Dialog se terminera tout de même `0` avec le code de sortie du bouton 1. L'état de la commande sera affiché à l'écran, y compris le code de sortie de la commande, par exemple :

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

La sortie des commandes sera directement redirigée vers la sortie standard, ce qui vous permettra de visualiser ou d'analyser les résultats selon vos besoins.

## Actions possibles pour d'autres boutons

Les boutons 2 et 3 (annuler et informations) permettent de quitter la boîte de dialogue avec les codes 2 et 3 respectivement. Ces codes de sortie peuvent être détectés et interprétés. Si un administrateur souhaite effectuer une action dans le terminal après le traitement de l'une de ces actions, je recommande de capturer le statut de sortie de la boîte de dialogue et de le traiter en conséquence.

## Considérations

La commande n'est pas exécutée en arrière-plan, donc la fenêtre Dialog sera visible, mais ne répondra pas, pendant l'exécution de la commande. Une fois la commande terminée, la fenêtre Dialog se fermera. Gardez cela à l'esprit si vous souhaitez exécuter une commande qui peut prendre un certain temps.

La commande du shell hérite également des autorisations du processus qui l'a appelée. Si Dialog est exécuté par l'utilisateur root, la commande du shell aura également les privilèges de root.