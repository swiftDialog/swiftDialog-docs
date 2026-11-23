---
title: Codes de sortie
description: Comprendre les codes de sortie et les valeurs de retour de swiftDialog
translationSynced: 2026-11-23T05:24:03+00:00
---

Lorsque swiftDialog se ferme, il renvoie un code de sortie qui peut être utilisé pour déterminer quelle action, le cas échéant, a été effectuée

|Code de sortie|Cause|
|---------|-----|
|0|L'utilisateur a cliqué sur le bouton par défaut (bouton 1).|
|2|L'utilisateur a cliqué sur le bouton 2|
|3|L'utilisateur a cliqué sur le bouton "Informations"|
|5|est sorti en utilisant la commande spécifiée dans le fichier de commandes `quit:`|
|10|Le programme s'est arrêté car l'utilisateur a utilisé `cmd+q` (ou la combinaison de touches Cmd+Quit).|
|20|quitter car `--timer` a atteint 0|
|201|Une ressource image n'a pas été trouvée|
|202|Une ressource de fichier n'a pas été trouvée|
|203|Une valeur de couleur non valide a été utilisée|

Plus de détails sur cette page : [Collecte des données de sortie du dialogue pour un traitement ultérieur](/fr/operation/capturing-output)