---
title: Mensajes de ayuda
description: Añadir mensajes de ayuda contextual a los cuadros de diálogo
translationSynced: 2026-11-24T22:59:20+00:00
---

## Mensajes de ayuda

Los mensajes de ayuda pueden ser una forma de proporcionar información adicional cuando sea necesario, sin ocupar espacio adicional en la interfaz de diálogo

`--helpmessage <text>`

`<text>` aceptará el formato Markdown para la redacción de mensajes

Cuando esté disponible, un botón de "ayuda" adicional aparecerá junto al botón predeterminado.


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

Hacer clic en él mostrará el mensaje de ayuda en una ventana emergente

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

La altura de la hoja que se muestra se adaptará al tamaño del mensaje.

### `--helpimage`

Añade una imagen con `--helpimage /path/to/image.png`.

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

Admite los argumentos estándar para los iconos, incluyendo el código QR:

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

Establece la alineación del texto del contenido del mensaje de la hoja de ayuda. La alineación predeterminada coincide con la configuración de alineación actual.

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

Establece la etiqueta del botón utilizado para cerrar la ventana de ayuda. El valor predeterminado es `OK`.