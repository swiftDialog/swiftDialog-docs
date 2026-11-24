---
title: Affichage des images
description: Apprenez comment afficher des images, des légendes et des carrousels d'images dans swiftDialog
translationSynced: 2026-11-23T03:02:46+00:00
---

## Affichage des images

Les images peuvent être affichées et, par défaut, elles remplacent la zone de message.

L'argument `--imagecaption` permet d'ajouter une courte description d'une ligne pour chaque image. Si l'argument `--message` est également présent, le message sera affiché sous les images et les légendes.

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

Tout format d'image pris en charge peut être utilisé, soit via un fichier `<file>`, soit via une adresse internet `<url>`

Exemple :

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Images au format base64

Dans tous les cas où une image peut être utilisée, il est désormais possible de la spécifier en utilisant le format base64, en utilisant le préfixe `base64=`, par exemple : `--icon base64=<base64_text>`

### Plusieurs images

Si plus d'une image est spécifiée, l'argument `--image` affichera les images dans un carrousel, avec des flèches de navigation pour passer à l'image suivante ou précédente, et une indication de l'image actuellement affichée dans la séquence.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

En plus d'afficher les images de manière statique, vous pouvez utiliser `--autoplay <sec>` pour que l'image suivante s'affiche après un nombre de secondes spécifié (la valeur par défaut est de 10). Un indicateur de progression sera affiché sous l'image pour indiquer le moment où la transition suivante aura lieu. Une fois la dernière image affichée, l'affichage se réinitialise et reprend à partir de la première image.

Utilisez `--hidetimer` pour masquer l'indicateur de compte à rebours affiché pendant les transitions automatiques.