---
title: Pantalla completa
description: Crear cuadros de diálogo de pantalla completa para presentaciones y modos de quiosco
translationSynced: 2026-11-24T22:35:46+00:00
---

La opción de ocupar toda la pantalla se puede activar mediante las opciones de línea de comandos `--fullscreen` o `-f`.

En esta configuración, solo se muestran el encabezado, el título, el icono y el mensaje. Se pueden especificar otras opciones, pero no se mostrarán. Sin embargo, el diálogo seguirá respondiendo a la entrada del teclado (teclas "escape" e "enter"), y se cerrará con el código de salida correspondiente.

El área de visualización se adaptará a diferentes resoluciones, desde 1024x640 hasta 5K. (Se aceptan donaciones de pantallas XDR para probar resoluciones de 6K).

Las opciones se comportarán de manera ligeramente diferente en comparación con el modo de pantalla normal.

### `--bannerimage` `-n`

Las imágenes de los banners se muestran centradas en la parte superior de la pantalla y ocuparán un máximo del 95% del ancho del área de visualización y un máximo del 10% de la altura del área de visualización. Esto permite mostrar imágenes de banner largas y estrechas, si es necesario.

Mostrar un banner también muestra una línea horizontal debajo, que ocupa el 95% del ancho del área de visualización.

### `--title` `-t`

El título se ubicará en la parte superior de la pantalla o justo debajo de un banner, y ocupará todo el ancho de la pantalla.

### `--icon` `-i`

Las imágenes de los iconos se muestran centradas debajo del título. Se aceptan fuentes de imágenes estándar, sin embargo, esta visualización no admite la opción de superponer imágenes en los iconos.

### `--message` `-m`

El área de mensajes ocupará todo el espacio disponible en la pantalla que quede debajo del título, la barra superior y los iconos. Se centrará tanto vertical como horizontalmente y ocupará todo el ancho de la pantalla.

Si se utilizan el banner, el título y el icono, el área de mensaje ocupará el 40-50% inferior de la pantalla (se dispone de más espacio en pantallas más grandes). Si se omiten el icono y el banner, se utilizará el 60-75% inferior de la pantalla.

Cada línea de texto en el área de mensajes se muestra con un espacio doble, con un máximo de 12 líneas.

## Ejemplos

Estos ejemplos muestran cómo se ve la pantalla a pantalla en un monitor estándar de 13 pulgadas, con las áreas de contenido resaltadas.

### Vista sencilla que muestra solo el título y el mensaje

<img width="1000" alt="Screenshot1" src="https://user-images.githubusercontent.com/3598965/114690586-306d0280-9d5a-11eb-9504-1e2d25f93711.png">


### Agotando todas las opciones, incluyendo la imagen de fondo y el icono

<img width="1000" alt="Screenshot2" src="https://user-images.githubusercontent.com/3598965/114690604-3531b680-9d5a-11eb-94c5-242693f6d335.png">