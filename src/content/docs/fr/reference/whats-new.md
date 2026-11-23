---
title: Quoi de neuf ?
description: Nouvelles fonctionnalités et mises à jour de swiftDialog
translationSynced: 2026-11-23T05:33:19+00:00
---

## swiftDialog 2.5.6

## Corrections :

 - Correction d'un problème où la spécification d'une icône à partir d'un fichier JSON nécessitait que l'icône soit placée dans un tableau, même s'il n'y avait qu'une seule icône. Résout le problème n° 493
 - Dans la version 2.5.5, un clic sur la notification ferme les boîtes de dialogue. #499
 - Mise à jour du message de version du script de dialogue lorsque aucun utilisateur n'est connecté, par @HowardGMac dans https://github.com/swiftDialog/swiftDialog/pull/510
 - Utiliser le chemin complet pour `scutil` (soumission à nouveau) par @MikeRich88 dans https://github.com/swiftDialog/swiftDialog/pull/515
 - J'ai ajouté un espacement supplémentaire à la fin de l'image d'aide
 - Ajoute une autorisation essentielle pour l'envoi de notifications, si celle-ci est requise. #485
 - Corriger les options manquantes pour `--textfield` dans l'aide, problème #485

## Contributions :

### Options supplémentaires pour la gestion des notifications

 - Ajoute la possibilité de définir un identifiant pour une notification, ce qui vous permet de remplacer facilement une notification par une version mise à jour. De plus, elle offre la possibilité de supprimer une notification spécifique en utilisant son identifiant, ou de supprimer toutes les notifications.

_Exemple :_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

Merci à @chrisgrande

### La taille du bouton a été ajoutée comme variable pouvant être spécifiée en ligne de commande et dans le fichier de configuration

 - Prise en charge des tailles de boutons miniatures, petites et grandes, en utilisant les tailles intégrées de macOS. Si la taille du bouton n'est pas spécifiée ou n'est pas valide, la valeur par défaut sera celle de la taille "normale".
 - Prise en charge de la taille des boutons dans le mode création, pour les tests et la génération de fichiers JSON.

Le style des boutons est appliqué aux éléments `button1`, `button2` et au bouton d'information. Il est également appliqué dans les configurations de boutons classiques et empilés.

 Il ne modifie pas la taille du bouton d'aide, qui a une taille fixe.

Exemples :

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

Merci à @k2graham

### Options permettant de masquer et d'afficher la fenêtre de dialogue à partir du fichier de commandes

 - Les commandes `hide:` et `show:` ont été ajoutées à la liste des commandes du fichier de configuration pour masquer et afficher les fenêtres. Cela n'empêche pas les mises à jour des fenêtres pendant qu'une fenêtre est masquée.

Merci à @fabienconus

