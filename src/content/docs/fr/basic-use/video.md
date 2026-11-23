---
title: Affichage des vidéos
description: Apprenez comment afficher des vidéos et du contenu vidéo dans swiftDialog, y compris le support de YouTube et de Vimeo
translationSynced: 2026-11-23T03:05:42+00:00
---

## Affichage des vidéos

Les vidéos peuvent être affichées à la place d'un message. Lorsqu'une vidéo au format 16:9 est utilisée, la taille par défaut de la fenêtre de dialogue passe automatiquement à 900x600. Des tailles personnalisées peuvent être spécifiées à l'aide des modificateurs `--width` et `--height`.

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

Tous les formats vidéo pris en charge par QuickTime devraient être visualisables. Si vous utilisez une URL, il est impératif d'indiquer le chemin complet vers le fichier vidéo.

Exemple : `--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### Prise en charge de YouTube et de Vimeo (nécessite swiftDialog version 2.0 ou supérieure)

Pour intégrer une vidéo YouTube ou Vimeo, vous pouvez transmettre l'identifiant de la vidéo comme paramètre à la commande `--video` en utilisant le préfixe `youtubeid=` ou `vimeoid=`

L'identifiant peut généralement être trouvé dans l'URL, soit sur YouTube, soit sur Vimeo

Exemple YouTube :

`dialog --video youtubeid=XXXXXXXXXX`

Exemple sur Vimeo :

`dialog --video vimeoid=XXXXXXXXXX`

_Note : pour les identifiants de vidéos privées sur Vimeo, il peut également être nécessaire de récupérer des informations supplémentaires dans l'URL d'intégration. Ces informations seront représentées par des éléments supplémentaires `h=YYYYYYYY` – la commande d'intégration complète pour swiftDialog serait donc `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`._


## Mettre à jour une boîte de dialogue en cours avec de nouveaux contenus web ou vidéo

Envoyez les commandes suivantes pour mettre à jour une boîte de dialogue avec du nouveau contenu web ou vidéo

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

Cependant, il y a quelques limitations : actuellement, il n'est pas possible de modifier directement le contenu web ou vidéo. Pour passer à un autre site web, il est nécessaire de supprimer le contenu existant, puis d'envoyer le nouveau contenu.

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

Vous pouvez cependant les assembler, donc cela `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log` fonctionne également.