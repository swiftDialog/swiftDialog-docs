---
title: Cuadro de información
description: Mostrar información adicional en un área de contenido secundaria
translationSynced: 2026-11-24T22:32:26+00:00
---

## Cuadro de información - `--infobox`

El cuadro de información es el área que se encuentra debajo de donde se muestra el icono.

Muestra un tamaño de fuente más pequeño, utilizando un tono secundario, y es útil para mostrar información adicional, como datos del sistema.

`--infobox` acepta cualquier texto con formato Markdown.

#### Aquí hay un ejemplo:

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

![Captura de pantalla del 10 de septiembre de 2024 a las 4:13 PM](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## Ancho del cuadro de información - `--infoboxwidth`

Por defecto, el cuadro de información comparte el ancho de la columna de iconos. `--infoboxwidth <number>` establece el ancho del área de texto del cuadro de información (en puntos) de forma independiente al tamaño del icono, lo que le permite ampliar el cuadro de información sin aumentar el tamaño del icono.

`--infoboxwidth 300`