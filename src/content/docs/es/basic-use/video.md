---
title: Mostrar videos
description: Aprenda cómo mostrar videos y contenido de video en swiftDialog, incluyendo soporte para YouTube y Vimeo
translationSynced: 2026-11-24T22:21:59+00:00
---

## Mostrar videos

Los videos pueden mostrarse en lugar de un mensaje. Cuando se especifica, el tamaño predeterminado del cuadro de diálogo cambiará a 900x600 para adaptarse a un video con relación de aspecto 16:9. Se pueden especificar tamaños personalizados utilizando los modificadores `--width` y `--height`.

```
--video  <file> | <url>
  Display a video instead of a message.
  Videos will be resized to fit the available display area (depending on video resolution, some letterboxing may occur)

    --videocaption <text>
    Text that will appear underneath the displayed video.

    --autoplay
    Video will start playing automatically on launch without requiring the user to press play
```

Cualquier formato de video compatible con Quicktime debería poder ser reproducido. Si se utiliza una URL, es necesario incluir la ruta completa al recurso de video.

`--title "Video Demo" --video /Users/Shared/Videos/day4session3.mp4`

![image](https://user-images.githubusercontent.com/3598965/138063195-19011cc7-840f-4701-9209-8405ffabcbeb.png)

### Soporte para YouTube y Vimeo (requiere swiftDialog versión 2.0 o superior).

Para insertar un video de YouTube o Vimeo, puede pasar el identificador del video como un parámetro al comando `--video`, utilizando el prefijo `youtubeid=` o `vimeoid=`

El identificador (ID) suele encontrarse en la dirección web (URL) tanto en YouTube como en Vimeo

Ejemplo de YouTube:

`dialog --video youtubeid=XXXXXXXXXX`

Ejemplo de Vimeo:

`dialog --video vimeoid=XXXXXXXXXX`

_Nota: Para los identificadores de videos privados de Vimeo, es posible que también deba capturar información adicional en la URL de incrustación. Esto se representará como información adicional `h=YYYYYYYY`; por lo tanto, el comando completo para swiftDialog sería `dialog --video "vimeoid=XXXXXXXXXX?h=YYYYYYYY"`._


## Actualizar un diálogo en curso con contenido web o de video nuevo

Envíe los siguientes comandos para actualizar un diálogo con contenido web o de video nuevo

```bash
echo "webcontent: https://some.website.com" >> /var/tmp/dialog.log
echo "video: https://some.website.com/video.mov" >> /var/tmp/dialog.log
echo "video: /path/to/file.mov" >> /var/tmp/dialog.log
```

Sin embargo, hay algunas limitaciones: actualmente, no es posible actualizar el contenido web o de video directamente. Para cambiar a otro sitio web, deberá borrar el contenido existente y luego enviar el nuevo contenido.

```bash
echo "webcontent: none" >> /var/tmp/dialog.log
echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log
```

Aunque puedes combinar esas opciones, también funciona así. `echo "webcontent: none" >> /var/tmp/dialog.log && echo "webcontent: https://some.new.website.com" >> /var/tmp/dialog.log`