---
title: Personalización del área de mensajes
description: Aprenda a configurar y personalizar el texto del mensaje, las propiedades de la fuente y la posición en swiftDialog
translationSynced: 2026-11-24T22:12:13+00:00
---

Utilice la opción de línea de comandos `-m` o `--message` para especificar el contenido que desea mostrar en el área de mensajes del cuadro de diálogo.

Ejemplo:

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

El área de mensaje puede ocupar ya sea 2/3 del ancho de la ventana de diálogo, o el ancho completo si el área de los iconos no se está mostrando

Los mensajes se ajustarán automáticamente al ancho del área de visualización y, si son más largos, se mostrarán con una barra de desplazamiento si exceden el área de visualización disponible.


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### Obtención de contenido

Además de proporcionar una cadena de texto, puede indicar la ruta o la URL de un archivo Markdown. Cualquier archivo que termine con la extensión `.md` se considerará un archivo fuente de Markdown.

Ejemplo:

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## Posicionamiento del mensaje

`--messagealignment` y `--messageposition` le permiten especificar la posición en el diálogo donde aparecerá el mensaje. Esto es útil para crear diálogos en los que el mensaje esté centrado vertical y horizontalmente.

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## Modificar la fuente, el color, el tamaño y la alineación del mensaje

`--alignment [left | centre | center | right]`

Establezca la alineación del mensaje. El valor predeterminado es "izquierda"

`--messagefont <text>`

Le permite modificar la fuente, el tamaño y el color del texto del mensaje.

`color,colour=<text><hex>`

> `<text>` Puede ser cualquiera de los colores estándar de Apple: `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Si la opción no es válida, el color predeterminado es el color primario del sistema (generalmente `black` si está en modo claro o `white` si está en modo oscuro).

> `<hex>` se especifica en formato hexadecimal, por ejemplo, #00A4C7

`size=<float>` acepta cualquier valor de punto flotante (por ejemplo, 15.7, 20, 32.0).

`name=<fontname>` - Acepta el nombre de cualquier fuente de letra instalada

Ejemplo: `--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### Utilizar un color adicional en el mensaje

Utilizar `colour=<value>` establecerá el color base del mensaje; sin embargo, puede definir el color de palabras o letras individuales utilizando el formato `:colour[text]`.

Ejemplo:

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

