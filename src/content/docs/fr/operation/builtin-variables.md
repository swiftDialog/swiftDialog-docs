---
title: Variables intégrées
description: Utilisation de variables dynamiques pour afficher des informations système dans les boîtes de dialogue
translationSynced: 2026-11-23T05:21:16+00:00
---

## Variables intégrées

swiftDialog contient désormais des variables intégrées qui seront remplies avec des informations spécifiques à chaque serveur. Incluez-les dans vos chaînes de texte comme `{variablename}`

Les variables incluses sont les suivantes :

    {computername}  - nom d'hôte de l'ordinateur
    {computermodel} - modèle d'ordinateur, par exemple "Mac mini (2023)"
    {serialnumber}  - numéro de série
    {username}      - nom d'utilisateur actuel, par exemple `johndoe`
    {userfullname}  - nom complet, par exemple `John Doe`
    {osversion}     - version de macOS, par exemple `14.4.1`
    {osname}        - nom de macOS, par exemple `Sonoma`

Toutes les variables d'environnement sont également accessibles de cette manière

    dialog --icône ordinateur --titre "{computermodel}" --message "Exécution de {osname} {osversion}" --style centré

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">