---
title: Mostrar imágenes
description: Aprenda cómo mostrar imágenes, leyendas de imágenes y presentaciones de imágenes en swiftDialog
translationSynced: 2026-11-24T22:14:01+00:00
---

## Mostrar imágenes

Las imágenes pueden mostrarse y, por defecto, reemplazarán el área de mensajes.

`--imagecaption` está disponible para una breve descripción de una línea de cada imagen. Si también hay un `--message`, este se mostrará debajo de las imágenes y las leyendas.

```
-g, --image  <file> | <url>
  Display an image instead of a message.
  Images will be resized to fit the available display area

    --imagecaption <text>
    Text that will appear underneath the displayed image.
```

Cualquier formato de imagen soportado puede ser utilizado, ya sea como entrada `<file>` o como entrada `<url>`

Aquí hay un ejemplo:

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/129476046-5b0cdef0-346b-4af6-a0eb-e8e72c72715d.png">

### Imágenes en formato base64

Donde sea posible utilizar una imagen, ahora se pueden especificar en formato base64, utilizando el prefijo `base64=`, por ejemplo: `--icon base64=<base64_text>`

### Imágenes múltiples

Especificar más de una imagen `--image` mostrará las imágenes en un carrusel con flechas de navegación (siguiente/anterior) e indicación de qué imagen de la secuencia se está mostrando.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/148642555-96247bff-8d95-414d-bf96-1fe28e27ed9c.png">

Además de mostrar las imágenes de forma estática, puede utilizar `--autoplay <sec>` para que la siguiente imagen se muestre después del número de segundos especificado (el valor predeterminado es 10). Un indicador de progreso se mostrará debajo de la imagen para indicar cuándo se producirá el siguiente cambio. Después de que se muestre la última imagen, la pantalla se reiniciará y comenzará desde la primera imagen.

Utilice `--hidetimer` para ocultar el indicador de cuenta regresiva que se muestra durante las transiciones de reproducción automática.