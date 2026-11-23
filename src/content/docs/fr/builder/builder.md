---
title: Mode constructeur
description: Modifiez les propriétés et l'apparence d'une fenêtre de dialogue et enregistrez les résultats au format JSON
translationSynced: 2026-11-23T05:18:50+00:00
---


## swiftDialog : Kit de développement

Pour activer la fonction, exécutez `dialog --builder`. Lorsqu'elle est appelée, une fenêtre supplémentaire s'affiche, vous permettant de modifier le contenu et les propriétés de la boîte de dialogue, et de visualiser les résultats en temps réel.

Vous pouvez ensuite exporter le résultat au format **JSON** ou sous forme de **ligne de commande** prête à l'emploi, afin de recréer la boîte de dialogue telle que vous l'avez conçue. `dialog`

** REMARQUE : Cette fonctionnalité ne couvre pas 100 % de toutes les fonctionnalités de swiftDialog, et certains paramètres ne sont pas disponibles ou n'apparaîtront pas dans la sortie générée. Le développement est en cours. **

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### Basique
 - [Titre](/fr/builder/title/)
 - [Message](/fr/builder/message/)
 - [Icône](/fr/builder/icon/)
 - [Barre latérale](/fr/builder/sidebar/)
 - [Fenêtre](/fr/builder/window/)
 - [Boutons](/fr/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### Avancé
 - [Cases à cocher](/fr/builder/checkboxes/)
 - [Images](/fr/builder/images/)
 - [Éléments de liste](/fr/builder/listitems/)
 - [Médias](/fr/builder/media/)
 - [Champs de texte](/fr/builder/textfields/)

</div>

</div>

### Sortie

La vue **Sortie** affiche la conception actuelle, soit au format **JSON**, soit sous forme de commande à exécuter en ligne de commande. Vous pouvez basculer entre ces deux formats à l'aide de l'onglet. À partir de cette vue, vous pouvez **copier vers le presse-papiers** ou **enregistrer le fichier**. Le bouton **Exporter la commande** situé dans le pied de page copie la commande en ligne de commande, quel que soit l'endroit où vous vous trouvez dans l'outil de création.