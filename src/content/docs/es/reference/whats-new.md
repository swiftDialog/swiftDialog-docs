---
title: ¿Qué hay de nuevo?
description: Novedades y actualizaciones recientes en swiftDialog
translationSynced: 2026-11-24T23:07:18+00:00
---

## swiftDialog 2.5.6

## Correcciones:

 - Se corrigió un problema por el cual, al especificar un icono a partir de un archivo JSON, era necesario que el icono estuviera dentro de un array, incluso si solo había un único icono. Soluciona el problema #493
 - En la versión 2.5.5, al hacer clic en la notificación, se cierran los cuadros de diálogo. #499
 - Actualizar el mensaje de la versión del script de diálogo cuando no hay ningún usuario conectado, por @HowardGMac en https://github.com/swiftDialog/swiftDialog/pull/510
 - Utilizar la ruta completa para `scutil` (reenvío) por @MikeRich88 en https://github.com/swiftDialog/swiftDialog/pull/515
 - Se agregó un relleno adicional a la imagen de ayuda
 - Agrega una autorización clave para el envío de notificaciones, en caso de que sea necesaria. #485
 - Corregir las opciones que faltaban para `--textfield` en la ayuda. #485

## Contribuciones:

### Opciones adicionales para trabajar con las notificaciones

 - Agrega la posibilidad de establecer un identificador para una notificación, lo que permite reemplazar fácilmente una notificación con una versión actualizada. También se incluye la opción de eliminar una notificación específica mediante su identificador, o eliminar todas las notificaciones.

_Ejemplo:_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

Gracias a @chrisgrande

### Se agregó la variable "buttonsize" como opción de línea de comandos y como variable en el archivo de configuración

 - Soporte para tamaños de botones pequeños, medianos y grandes, utilizando los tamaños predefinidos de macOS. Si no se especifica un tamaño o el valor no es válido, el tamaño del botón se establecerá por defecto al tamaño "regular".
 - Soporte para el tamaño de los botones en el modo de edición para pruebas y generación de archivos JSON.

El estilo de los botones se aplica a `button1`, `button2` y al botón de información. También se aplica en las disposiciones de botones estándar y apilados.

 No ajusta el tamaño del botón de ayuda, que tiene un tamaño fijo.

Ejemplos:

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

Gracias a @k2graham

### Opciones para ocultar y mostrar la ventana de diálogo desde el archivo de comandos

 - Se han añadido los comandos `hide:` y `show:` a la lista de comandos del archivo de comandos para ocultar y mostrar ventanas. Esto no impide que las ventanas se actualicen mientras están ocultas.

Gracias a @fabienconus

