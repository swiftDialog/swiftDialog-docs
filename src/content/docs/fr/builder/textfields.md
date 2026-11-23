---
title: Mode constructeur - Champs de texte
description: Modifiez les propriétés et l'apparence d'une fenêtre de dialogue et enregistrez les résultats au format JSON
translationSynced: 2026-11-23T05:18:03+00:00
---

Configurez les entrées `--textfield`

<img width="500" alt="image" src="/builder/builder_textfields.png" />

Cliquez sur le bouton `[+]` pour ajouter une nouvelle entrée

Cliquez sur l'icône de la corbeille pour supprimer une entrée

Faites glisser la poignée (☰) située à gauche de chaque ligne pour modifier l'ordre des éléments


<img width="500" alt="image" src="/builder/builder_textfields_popualated.png" />


## Propriétés

Les propriétés suivantes peuvent être configurées

#### Formatez la sortie au format JSON

Définit le format de sortie. Cette propriété est partagée avec les [cases à cocher](/fr/builder/checkboxes/)

#### Obligatoire

Définit l'indicateur `required`.

#### Confirmer

Active le `confirm` indicateur. L'activation de cette option affichera un champ de texte dupliqué pour l'entrée configurée

#### Sélectionner un fichier

Active le bouton `fileselect`

##### Type de fichier

À utiliser avec `fileselect`. Entrez le type de fichier souhaité (ou les types, sous forme de fichier CSV), par exemple : `"png,jpg"`

##### Parcours initial

Utilisé avec `fileselect`. Définit le chemin initial à utiliser lors de l'affichage de la boîte de dialogue de sélection de fichier

#### Titre

Définit le titre ou l'étiquette du champ de texte

#### Nom

Définit le nom du champ de texte. Si cette option est utilisée, cette valeur représentera cette entrée dans la sortie au lieu de l'étiquette

#### Valeur par défaut

Définissez la valeur par défaut qui s'affichera dans le champ de texte. Ce contenu apparaîtra dans la sortie

#### Invite

Définit un texte à afficher dans le champ de texte. Ce contenu ne figurera pas dans la sortie

#### Expressions régulières

Définissez une expression régulière que le contenu du champ de texte doit respecter

#### Erreur d'expression régulière

Définir le message d'erreur à afficher lorsque le contenu du champ de texte ne correspond pas à l'expression régulière fournie

[Retour](/fr/builder/builder/)