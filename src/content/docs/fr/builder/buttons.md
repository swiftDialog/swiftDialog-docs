---
title: Mode constructeur - Boutons
description: Modifiez les propriétés et l'apparence d'une fenêtre de dialogue et enregistrez les résultats au format JSON
translationSynced: 2026-11-23T05:20:37+00:00
---

Permet de définir les propriétés de la zone de boutons

<img width="500" alt="image" src="/builder/builder buttons.png" />

#### Taille du bouton

Définir la taille de l'un des quatre boutons (ce réglage affecte tous les boutons).

 - miniature
 - petit(e)
 - normal (par défaut)
 - grand(e)

#### Bouton 1

Définit le texte à afficher sur le bouton 1, également appelé le bouton par défaut

Par défaut `"OK"`

Le paramètre "Désactivé" définira l'état du bouton 1 comme étant désactivé (et pourra être réactivé via une commande dans le fichier de configuration `button1: enable`).

#### Bouton 2

Définissez le texte qui sera affiché sur le bouton 2

Par défaut `"Cancel"`

#### Bouton d'information

Définissez le texte qui s'affiche sur le bouton Info

Activez l'option "Fermer à l'appui sur Info" pour que la fenêtre de dialogue se ferme lorsque le bouton "Info" est cliqué

Définissez l'action du bouton "Info" pour qu'il ouvre une URL spécifique lorsqu'il est cliqué.

#### Symbole

Les boutons 1, bouton 2 et le bouton Info peuvent chacun afficher un symbole SF à côté de leur libellé. L'éditeur de symboles expose les propriétés du symbole sous forme de contrôles individuels :

 - Nom du symbole SF
 - **Position** — en tête, en queue, en haut ou en bas
 - Mode de rendu : hiérarchique, monochrome, multicolore ou palette
 - **Couleur** : une seule couleur, ou 2 à 3 couleurs de la palette, lorsque le mode de rendu de la palette est sélectionné
 - Taille personnalisée

Une prévisualisation en direct du symbole créé est affichée, et le bouton de la fenêtre de dialogue se met à jour en temps réel au fur et à mesure que vous effectuez des modifications.

[Retour](/fr/builder/builder/)