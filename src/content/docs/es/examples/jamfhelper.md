---
title: Soporte técnico de jamfHelper
description: Utilizar swiftDialog como un reemplazo directo de jamfHelper
translationSynced: 2026-11-24T23:06:03+00:00
---

Dialog ahora tiene la capacidad de aceptar un conjunto básico de opciones de línea de comandos en formato jamfHelper, gracias a la nueva opción `--jh`.

Esto facilita su implementación en los flujos de trabajo y scripts existentes, ya que se puede reemplazar la llamada a `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` con `/usr/local/bin/dialog --jh`

El uso de esta opción permitirá que el diálogo convierta las opciones de `jamfHelper` en opciones de diálogo equivalentes. No todas las opciones son compatibles. Las opciones de diálogo estándar que no tienen un equivalente en `jamfHelper` siguen estando disponibles, por ejemplo, `--width`, `--height` y `--image`.

<br/>

## Características y comportamiento

***
### Implementado

#### `-windowType [hud | utility | fs]`

`hud` y `utility` se ignoran. `fs` se convierte en un cuadro de diálogo `--fullscreen` y se mostrará en una ventana de diálogo a pantalla completa

#### `-windowPosition [ul | ll | ur | lr]`

La ventana de posiciones se puede ubicar en la esquina superior derecha, superior izquierda, inferior derecha o inferior izquierda de la pantalla del usuario. Esta es la única función que actualmente no forma parte de las opciones estándar de la interfaz, pero se ha implementado para garantizar la compatibilidad con jamfHelper.

#### `-title "string"`
Convertido a `--title`

Establece el título de la ventana con la cadena de texto especificada

#### `-heading "string"` y `-description "string"`
Convertido a `--message`

Tanto `-heading` como `-description` se integran en la opción de diálogo `--message`. `-heading` se convierte en un encabezado de nivel 4 en formato Markdown `####`, seguido de una línea en blanco y luego de `-description`

#### `-icon path`
Convertido a `--icon`

Si no está presente, la opción "forces dialogs" imita el comportamiento de jamfHelpers, mostrando el diálogo sin un ID si este no se especifica. `--hideicon`

#### `-button1 "string"`
Convertido a `--button1text`

**_Comportamiento modificado:_** El cuadro de diálogo siempre muestra el botón predeterminado, lo cual es diferente a cómo funciona jamfHelper. El texto del botón predeterminado es `OK`

#### `-button2 "string"`
Convertido a `--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
Convertido a `--alignment`

Las únicas opciones implementadas son `right` `centre` y `left`

#### `-timeout int` y `-countdown`
Convertido a `--timer`.

`-countdown` siempre se entiende implícitamente, ya que el indicador de tiempo siempre se muestra en la ventana de diálogo, y no se ha implementado una opción para ocultar dicho indicador.

<br/>

***
### No implementado

#### `-defaultButton [1 | 2]`
El botón predeterminado es siempre el botón número 1

#### `-cancelButton [1 | 2]`
El botón de "Cancel" siempre es el botón número 2 (si se muestra).

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`