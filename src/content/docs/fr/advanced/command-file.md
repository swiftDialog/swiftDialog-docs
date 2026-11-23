---
title: Fichier de commandes
description: Mise à jour dynamique des boîtes de dialogue avec du nouveau contenu, en utilisant des fichiers de commandes
translationSynced: 2026-11-23T03:39:39+00:00
---

Certain éléments du contenu d'une boîte de dialogue peuvent être mis à jour en temps réel après son lancement. Cela est possible grâce à l'envoi de commandes à un fichier de commandes que swiftDialog lit et interprète.

---

Le processus swiftDialog doit être lancé en arrière-plan afin de permettre l'envoi de commandes depuis le même script.

```sh
/usr/local/bin/dialog & sleep 0.1
```

Le système `sleep 0.1` accorde 100 millisecondes à swiftDialog pour son initialisation avant l'envoi de la première commande.

Le chemin d'accès par défaut au fichier de commandes est `/var/tmp/dialog.log`. Un chemin personnalisé peut être défini à l'aide de l'argument `--commandfile` :

```sh
dialog --commandfile /var/tmp/my.log
```

Envoyer les commandes en utilisant :

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## Contenu

| Commande | Description |
|---|---|
| `title: <text>` | Mettre à jour le titre de la boîte de dialogue |
| `title: none` | Masquer la zone de titre |
| `titlefont: <params>` | Mettre à jour les propriétés de la police du titre. Accepte des paires séparées par des espaces : `key=value`, `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>` |
| `message: <text>` | Remplacez le contenu du message. Prise en charge du format Markdown. |
| `message: + <text>` | Ajouter le contenu à la fin du message existant (insère un retour à la ligne avant le nouveau contenu). |
| `message: /path/to/file.md` | Charger le contenu du message à partir d'un fichier Markdown local |
| `alignment: [left\|center\|right]` | Définir l'alignement du texte du message |

---

## Icône

| Commande | Description |
|---|---|
| `icon: <path\|url\|SF Symbol>` | Modifier l'icône affichée |
| `icon: none` | Masquer l'icône |
| `icon: centre` / `icon: center` | Déplacez l'icône vers le centre |
| `icon: left` / `icon: default` | Déplacez l'icône vers sa position par défaut, à gauche |
| `icon: size: <num>` | Modifier la taille de l'icône |
| `iconalpha: <float>` | Définir l'opacité de l'icône (0.0 : transparent → 1.0 : opaque). |
| `overlayicon: <path\|url\|SF Symbol>` | Définir l'icône de superposition |
| `overlayicon: none` | Masquer l'icône de superposition |

---

## Bannière et arrière-plan

| Commande | Description |
|---|---|
| `bannerimage: <path\|url>` | Définir l'image de bannière |
| `bannerimage: none` | Supprimez l'image de bannière |
| `bannertext: enable` | Afficher le titre comme texte de bannière (la couleur de la police est définie sur blanc). |
| `bannertext: disable` | Restaurer l'apparence par défaut du titre |
| `bannertext: shadow` | Activer l'effet d'ombre portée pour le texte du titre de la bannière |
| `bannertext: <text>` | Définissez le texte du titre de la bannière et activez le mode de texte pour la bannière |

---

## Images et médias

| Commande | Description |
|---|---|
| `image: <path\|url>` | Afficher une image (l'ajouter à la diapositive si une image est déjà affichée). |
| `image: show` | Afficher l'image actuelle |
| `image: hide` | Masquer l'image actuelle |
| `image: clear` | Supprimer toutes les images |
| `imagecaption: <text>` | Placez la légende sous l'image affichée |
| `video: <path\|url>` | Afficher une vidéo. Prend en charge les raccourcis `youtube=<id>` et `vimeo=<id>`. |
| `video: none` | Supprimer la vidéo |
| `webcontent: <url>` | Chargez une URL dans la zone de contenu web |
| `webcontent: none` | Supprimer le contenu web |

---

## Boutons

| Commande | Description |
|---|---|
| `button1: enable` / `button1: show` | Activer le bouton 1 |
| `button1: disable` / `button1: hide` | Désactiver le bouton 1 |
| `button1text: <text>` | Mettre à jour l'étiquette du bouton 1 |
| `button2: enable` / `button2: show` | Activer le bouton 2 |
| `button2: disable` / `button2: hide` | Désactiver le bouton 2 |
| `button2text: <text>` | Mettre à jour l'étiquette du bouton 2 |
| `buttonsize: [mini\|small\|regular\|large]` | Définir la taille des boutons |
| `infobutton: <text>` | Mettre à jour le libellé du bouton "Informations" |
| `infotext: <text>` | Mettre à jour le champ de texte d'information |
| `infotext: disable` / `infotext: hide` | Masquer le texte d'information |
| `infotext: reset` / `infotext: clear` | Effacer la valeur du texte d'information |

---

## Boîte d'informations

| Commande | Description |
|---|---|
| `infobox: <text>` | Remplacez le contenu de la boîte d'informations. Le format Markdown est pris en charge. |
| `infobox: + <text>` | Ajouter le contenu suivant à la boîte d'information existante |
| `infobox: /path/to/file.md` | Charger le contenu de la boîte d'informations à partir d'un fichier Markdown local |

---

## Barre de progression

| Commande | Description |
|---|---|
| `progress: <int>` | Définissez la barre de progression à une valeur spécifique correspondant à une étape |
| `progress: increment` | Incrémentez la barre de progression d'une étape |
| `progress: increment <n>` | Incrémentez la barre de progression de `n` étapes |
| `progress: complete` | Définissez la barre de progression à sa valeur maximale |
| `progress: reset` / `progress: indeterminate` | Réinitialisez la barre de progression en mode indéterminé |
| `progress: show` / `progress: enable` / `progress: create` | Afficher la barre de progression |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | Masquer la barre de progression |
| `progresstext: <text>` | Mettre à jour le libellé situé sous la barre de progression |

---

## Listes

| Commande | Description |
|---|---|
| `list: <csv>` | Remplacez la liste par de nouveaux éléments séparés par des virgules |
| `list: clear` | Effacer tous les éléments de la liste et masquer la liste |
| `list: show` | Afficher la liste |
| `list: hide` | Masquer la liste sans effacer son contenu |

### Mise à jour des éléments de la liste

Mettre à jour un élément existant en utilisant son titre (formulaire simple) :

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

Mettre à jour un élément en ayant un contrôle total grâce à une liste de propriétés séparées par des virgules :

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

Ajouter un nouvel élément à la fin de la liste :

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

Supprimer un élément :

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**Propriétés disponibles `listitem` :**

| Propriété | Description |
|---|---|
| `title: <text>` | Faire correspondre les éléments en fonction du titre |
| `index: <int>` | Correspondance par index (en commençant à 0). |
| `subtitle: <text>` | Définir le sous-titre de l'article |
| `icon: <path\|url\|SF Symbol>` | Définir l'icône de l'élément |
| `iconalpha: <float>` | Définir l'opacité de l'icône de l'élément |
| `status: <status>` | Définissez l'icône de statut. Choisissez parmi `wait`, `success`, `fail`, `error`, `pending`, `progress`, ou un nom de symbole SF (facultativement avec un suffixe de couleur, par exemple `lock.shield.fill-green`). |
| `statustext: <text>` | Définir le texte de l'étiquette de statut |
| `progress: <float>` | Définir une valeur de progression intégrée (affiche un statut de type "progression"). |
| `action: <url>` | URL à ouvrir lorsque l'élément est cliqué |
| `add:` | Ajouter un nouvel élément à la liste |
| `delete:` | Supprimer l'élément correspondant |

---

## Message d'aide

| Commande | Description |
|---|---|
| `helpmessage: <text>` | Mettre à jour le contenu du message d'aide. Prise en charge du format Markdown. |

---

## Fenêtre

| Commande | Description |
|---|---|
| `width: <num>` | Modifier la largeur de la fenêtre |
| `height: <num>` | Modifier la hauteur de la fenêtre |
| `position: <position>` | Déplacez la fenêtre. Choisissez parmi les options suivantes : `top`, `bottom`, `left`, `right`, `centre`, ou une combinaison de celles-ci (par exemple, `topright`). |

---

## Visibilité des fenêtres

| Commande | Description |
|---|---|
| `activate:` | Amenez la fenêtre de dialogue au premier plan |
| `show:` | Rendre la fenêtre de dialogue visible |
| `hide:` | Masquer la fenêtre de dialogue |
| `minimize:` / `minimise:` | Réduire la fenêtre de dialogue à la barre des applications |
| `maximize:` / `maximise:` | Restaurer une fenêtre de dialogue minimisée |
| `blurscreen: enable` | Activer l'effet de flou d'écran |
| `blurscreen: disable` | Désactivez l'effet de flou d'écran |

---

## Icône de la barre des applications

| Commande | Description |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | Afficher l'icône de la boîte de dialogue dans la barre des applications |
| `showdockicon: <any other value>` | Masquer l'icône de la boîte de dialogue dans la barre des applications |
| `dockicon: <file\|url>` | Définir une image personnalisée comme icône de la barre des applications |
| `dockicon: none` / `dockicon: default` | Restaurer l'icône Dock par défaut de swiftDialog |
| `dockiconbadge: <text>` | Afficher un badge sur l'icône du Dock |
| `dockiconbadge: none` / `dockiconbadge: remove` | Supprimer le badge de l'icône du Dock |
| `bounce:` | Faire rebondir l'icône du Dock une fois (à titre informatif). |
| `bounce: critical` | Faire rebondir l'icône du Dock en continu jusqu'à ce que la fenêtre soit mise au premier plan |

---

## Quitter

| Commande | Description |
|---|---|
| `quit:` | Quitter swiftDialog avec le code de sortie 5 |
