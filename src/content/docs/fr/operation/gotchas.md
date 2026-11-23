---
title: Pièges à éviter
description: Problèmes courants et conseils de dépannage pour swiftDialog
translationSynced: 2026-11-23T05:26:36+00:00
---

# Problèmes liés aux fichiers de commandes

## Permissions insuffisantes

Si vous lancez swiftDialog et que le fichier de commandes ne peut pas être enregistré, vous recevrez un message d'erreur :

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

Le fichier de commande doit être supprimé ou, à défaut, ses permissions doivent être modifiées pour qu'elles soient définies à `-rw-rw-rw` (666).

---

# Modifications du comportement de swiftDialog, version 3.1.1

## `--alwaysreturninput` Rendements pour tous les parcours de cessation

**Ce qui a changé :** À partir de la version 3.1.1, `--alwaysreturninput` renvoie des résultats au format sélection/liste/JSON sur **tous** les chemins de sortie, et non plus seulement lorsqu'on appuie sur un bouton.

**Chemins d'arrêt affectés :**
- Fichier de commandes : quitter
- Délai d'expiration du minuteur
- Appuyer sur la touche pour quitter
- Process arrêté

**Migration :** Les scripts qui reposent sur l'ancien comportement (qui ne renvoient de résultats qu'au moment d'une pression sur un bouton) pourraient afficher de nouveaux résultats. Veuillez vérifier votre logique de traitement si vous utilisez `--alwaysreturninput`.

## `--ontop` Respecte la position de la cale

**Ce qui a changé :** L'option `--ontop` tient désormais compte de la position de la barre des applications et positionne la fenêtre de dialogue à l'intérieur de l'écran (et non au-dessus de la barre des applications).

**Impact :** Les fenêtres de dialogue ne recouvriront plus la barre d'outils lorsque `--ontop` est utilisé. Cela annule une décision délibérée prise dans une version antérieure.

## Modificateurs de sélecteur de date

**Ce qui a changé :** Le modificateur `isdate` a été **déprécié** au profit de `date` et `time`.

**Migration :** Mettez à jour vos scripts.

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# Erreurs fréquentes à éviter

## Options répétables en tant que dernier argument

**Problème :** Les options répétables (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`) utilisées comme argument final pourraient provoquer un plantage.

**Statut :** Corrigé dans la version 3.1.1

## Le sélecteur de date ne renvoie aucune valeur

**Problème :** L'utilisation de `--textfield ...,isdate` ne renvoyait aucune valeur, car il s'agissait d'une structure temporaire qui ne retournait jamais de valeurs.

**Statut :** Corrigé dans la version 3.1.1. Utilisez les modificateurs `date` ou `time` à la place.

## La commande de légende pour les images ne fonctionne pas

**Problème :** Le fichier de commandes `imagecaption:` n'avait aucun effet car il ne faisait que écrire dans `appvars.imageCaptionArray` (utilisé une seule fois au démarrage) au lieu de `observedData.imageArray` (source réactive).

**Statut :** Corrigé dans la version 3.1.1

## Les en-têtes de groupe prédéfinis s'affichent incorrectement

**Problème :** Les en-têtes des groupes de déploiement ("Terminé", "Installation en cours") sont affichés à une position incorrecte ou sont dupliqués.

**Statut :** Corrigé dans la version 3.1.1

## La barre de boutons du clavier ne fonctionne pas

**Problème :** `--hidedefaultkeyboardaction` ne fonctionnait pas en raison d'un problème apparu lors de la refonte de la barre d'outils.

**Statut :** Corrigé dans la version 3.1.1