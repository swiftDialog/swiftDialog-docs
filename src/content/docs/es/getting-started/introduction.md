---
title: Comenzando con swiftDialog
description: Introducción a swiftDialog, una utilidad de diálogo moderna para macOS diseñada para administradores
translationSynced: 2026-11-24T22:09:26+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![Ejemplo de bienvenida de swiftDialog](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

El propósito de swiftDialog es ser una herramienta de utilidad para los administradores de sistemas macOS, que pueden utilizar a través de scripts para mostrar un cuadro de diálogo que presente información al usuario e informe sobre la acción que este haya realizado. Esta información puede ser utilizada posteriormente para procesar el script o simplemente para mostrar un determinado dato.

swiftDialog acepta entradas desde la línea de comandos, utilizando una o más [opciones de línea de comandos](/es/advanced/command-line-options) para indicar a swiftDialog qué mostrar y cómo mostrarlo.

Existen varias opciones disponibles que pueden utilizarse para personalizar la información que se muestra, y estas opciones van desde una visualización informativa muy sencilla hasta procesos más complejos que incluyen la entrada de texto, listas desplegables, la visualización de imágenes y mucho más.

## Ejecutando swiftDialog

El instalador **.pkg** de la [página de versiones](https://github.com/swiftDialog/swiftDialog/releases) instalará swiftDialog en `/usr/local/bin/dialog`, que también debería estar en el `$PATH` predeterminado en macOS.

Para llamar a la función de diálogo desde su script, puede utilizar la ruta completa o confiar en `$PATH`

```bash
$ dialog --title ...
```

o

```bash
$ /usr/local/bin/dialog --title ...
```

A su nivel más básico, el programa "dialog" puede simplemente utilizar las opciones de línea de comandos `--title` y `--message` para mostrar una ventana de diálogo con el mensaje deseado.

SwiftDialog puede hacer mucho más que eso, y es recomendable que consulte la página de "[Opciones de línea de comandos](/es/advanced/command-line-options)" para ver una lista completa de las opciones disponibles, o que llame a la función "dialog" con la opción `--help`.

## Enlaces rápidos

### Características básicas
- [Personalización del título de swiftDialog](/es/basic-use/title)
- [Personalización de la visualización de mensajes en swiftDialog](/es/basic-use/message)
- [Personalización de la imagen que se muestra en el área de icono de swiftDialog. ](/es/basic-use/icon)
- [Añadir una imagen de encabezado](/es/advanced/banner-images)
- [Personalización de los botones y su comportamiento](/es/basic-use/buttons)

### Características avanzadas
- [Recuadro de información](/es/advanced/info-box)
- [Imágenes para banners ](/es/advanced/banner-images)
- [Mensaje de ayuda](/es/operation/help-message)
- [Menús desplegables y botones de opción](/es/advanced/select-lists)
- [Entrada de texto](/es/advanced/textfields)
- [Casillas de verificación](/es/advanced/checkboxes)
- [Temporizador con barra de progreso](/es/advanced/timer-progress)
- [Tamaño y comportamiento de la ventana](/es/advanced/window-size)
- [Modo de pantalla completa](/es/advanced/full-screen)
- [Modo de presentación](/es/advanced/presentation)
- [Listas de elementos](/es/advanced/item-lists)
- [Notificaciones del sistema](/es/advanced/notifications)
- [Modificar CMD+Q](/es/operation/command-q)
- [Variables integradas](/es/operation/builtin-variables)

## Soporte

swiftDialog se creó, en parte, como un ejercicio de aprendizaje sobre cómo desarrollar aplicaciones utilizando SwiftUI, y en parte para satisfacer la necesidad de una forma de comunicar información a los usuarios de Mac de una manera que me resultara atractiva.

Se puede ofrecer soporte [creando un problema](https://github.com/swiftDialog/swiftDialog/issues). También se aceptan sugerencias de nuevas funcionalidades.

## Contacto

Puede contactar al autor a través del canal #swiftdialog en el grupo de Slack de [Macadmins](https://www.macadmins.org/slack)] (nombre de usuario @bartreardon, que suele estar en el canal #anzmac). Sin embargo, le pedimos que limite las consultas de soporte o las preguntas generales al repositorio de GitHub, al menos para que podamos rastrear y resolver su problema. Gracias 😃