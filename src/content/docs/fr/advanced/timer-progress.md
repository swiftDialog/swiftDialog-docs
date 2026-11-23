---
title: Compteur de temps et barre de progression
description: Création de boîtes de dialogue avec des compteurs à rebours et des barres de progression interactives
translationSynced: 2026-11-23T03:50:02+00:00
---

Une boîte de dialogue peut être lancée grâce à un minuteur qui se déclenchera une fois le nombre de secondes spécifié écoulé

`--timer (<seconds>)`


Remplace le bouton par défaut par un compte à rebours. Une fois le compte à rebours terminé, la boîte de dialogue se ferme avec le code de sortie `4`. La valeur par défaut du minuteur est de `10` secondes. Une valeur optionnelle `<seconds>` peut être spécifiée pour définir la durée souhaitée. Si `<seconds>` est supérieur à 60, le compte à rebours sera affiché dans le format `HH:MM:SS`, par exemple, 280 secondes seront affichées sous la forme `4:40` pour le compte à rebours initial.

Si utilisé en conjonction avec `--button1text`, le bouton par défaut sera affiché, mais il sera désactivé pendant les 3 premières secondes du minuteur. Après ce délai, il devient actif et peut être utilisé pour fermer la boîte de dialogue avec le code de sortie 0

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` masquera la barre de progression et le compte à rebours.

Cela permet de rendre le bouton par défaut visible, ce qui évite l'affichage de boîtes de dialogue impossibles à fermer, sans indication de la durée du compte à rebours.

---

## Barre de progression

swiftDialog peut afficher une barre de progression interactive qui peut être mise à jour dynamiquement via le [fichier de commandes](/fr/advanced/command-file).

`--progress [<int>]`

Affiche une barre de progression avec le nombre d'étapes spécifié. Si aucune valeur n'est fournie, le nombre par défaut d'étapes est de 10.

Pour faire avancer la barre de progression, envoyez une commande au fichier de commandes de la boîte de dialogue :

```sh
echo "progress: <int>" >> /var/tmp/dialog.log
```

`--progresstext <text>`

Définit le texte initial affiché sous la barre de progression. Ce texte peut être mis à jour à tout moment :

```sh
echo "progresstext: Installing software..." >> /var/tmp/dialog.log
```

### Alignement du texte de progression

`--progresstextalignment [left | right]`

Définit l'alignement horizontal du texte de progression affiché sous la barre de progression. La valeur par défaut est centrée.