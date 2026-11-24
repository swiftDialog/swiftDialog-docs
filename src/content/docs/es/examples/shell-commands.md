---
title: Comandos de Shell
description: Función experimental para ejecutar comandos del sistema operativo a través de acciones de botones
translationSynced: 2026-11-24T23:05:51+00:00
---

La versión 1.1.2 introduce una función experimental a través del comando `button1shellaction`


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

Recibe un único parámetro de tipo cadena y lo pasa a un intérprete de comandos para su ejecución, por ejemplo:

` --button1shellaction "say thank you for running dialog"`

Actualmente, no se realiza ninguna validación de entrada ni de salida. Si el comando especificado finaliza con un error, Dialog seguirá finalizando `0` con el código de salida del botón 1. Se mostrará en la pantalla el estado del comando, incluyendo el código de salida del comando, por ejemplo:

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

La salida del comando se enviará directamente a la salida estándar (stdout), lo que le permitirá ver o analizar los resultados según sea necesario.

## Acciones asociadas a otros botones

Los botones 2 y 3 (cancelar e información) cerrarán la ventana de diálogo con los códigos 2 y 3, respectivamente. Estos códigos de salida pueden ser detectados y analizados. Si un administrador desea realizar alguna acción en la línea de comandos después de que se haya procesado cualquiera de estas opciones, le recomiendo capturar el estado de salida de la ventana de diálogo y procesarlo en consecuencia.

## Consideraciones

El comando no se ejecuta en segundo plano, por lo que la ventana de diálogo será visible, pero no responderá, mientras se ejecuta el comando. Una vez finalizada la ejecución, la ventana de diálogo se cerrará. Tenga esto en cuenta si desea ejecutar un comando que pueda tardar algún tiempo en completarse.

El comando de la línea de comandos también hereda los permisos del proceso que lo ejecutó. Si Dialog se ejecuta con privilegios de administrador (root), el comando de la línea de comandos también tendrá esos mismos privilegios.