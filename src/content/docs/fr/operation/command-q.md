---
title: Modification du comportement de la commande Cmd+Q
description: Personnalisation des raccourcis clavier pour les boîtes de dialogue de fermeture
translationSynced: 2026-11-23T05:23:49+00:00
---

Dans swiftDialog 1.10.2 et versions ultérieures, la commande `--quitkey <char>` permet de réaffecter `command+q` à `command +<char>`

Par exemple, `--quitkey x` désactivera la fonction raccourci Cmd+Q pour fermer la boîte de dialogue, mais permettra `command+x`.

De plus, si une boîte de dialogue est fermée en utilisant une combinaison de touches + <char>, le code de sortie sera `10`, ce qui permet d'effectuer une action si cela est détecté.

Les raccourcis `command+w`, `command+m` et la combinaison de touches "command+n" sont également désactivés par défaut et ne peuvent pas être réassignés.