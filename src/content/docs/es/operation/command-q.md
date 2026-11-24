---
title: Modificación del comportamiento del comando Comando+Q
description: Personalizar los atajos de teclado para los cuadros de diálogo de salida
translationSynced: 2026-11-24T22:59:12+00:00
---

En swiftDialog 1.10.2 y versiones posteriores, el comando `--quitkey <char>` volverá a asignar `command+q` a `command +<char>`

Por ejemplo, `--quitkey x` deshabilitará la función de cerrar la ventana de diálogo al presionar la combinación de teclas Command+Q, pero permitirá `command+x`.

Además, si se cierra un diálogo mediante una acción de comando+<char>, el código de salida será `10`, lo que permite realizar cualquier acción si se detecta este evento.

Las combinaciones de teclas `command+w`, `command+m` y "comando + n" también están desactivadas de forma predeterminada y no se pueden reasignar.