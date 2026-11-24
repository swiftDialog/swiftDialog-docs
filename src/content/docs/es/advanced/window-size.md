---
title: Tamaño y comportamiento de la ventana
description: Controlar la posición, el tamaño y la apariencia visual de la ventana de diálogo
translationSynced: 2026-11-24T22:36:30+00:00
---

El comportamiento predeterminado de la ventana de diálogo es que se posicione en el centro de la pantalla y no se puede mover. Otras ventanas pueden colocarse encima de ella. Es posible modificar este comportamiento utilizando las siguientes opciones de línea de comandos.

Ambas opciones pueden utilizarse de forma independiente, sin depender una de la otra.

## Visibilidad de la ventana

`-p` o `--ontop`

Utilice esta opción para forzar que la ventana de diálogo siempre se muestre en primer plano.

## Posición de la ventana

`-o` o `--moveable`

Utilice esta opción para permitir que la ventana se pueda arrastrar por toda la pantalla.

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

Ubica la ventana de diálogo en la posición definida en la pantalla

`--positionoffset <num>`

Establece el desplazamiento de los bordes de la ventana (la distancia entre los bordes de la pantalla y la ventana).

`--position <x>,<y>`

Ubica la ventana de diálogo en las coordenadas x,y especificadas, por ejemplo: `--position 100,200`

**Notas:**
 - La posición 0,0 corresponde a la esquina superior izquierda del área visible de la pantalla
 - El área visible de la pantalla no incluye el espacio ocupado por la barra de acceso rápido o la barra de menú. Por ejemplo, si la barra de acceso rápido se encuentra en el lado izquierdo de la pantalla, el punto de origen estará desplazado hacia el interior.


## Tamaño de la ventana

Puede modificar el tamaño para que sea mayor o menor que el tamaño predeterminado, dependiendo de la cantidad de información que desee incluir en su mensaje o si desea mostrar diferentes tamaños en pantallas de distintos tamaños. Las imágenes se ajustan proporcionalmente. El tamaño de la fuente del texto permanece igual.

`-b` o `--big`

Esto hace que la ventana parezca aproximadamente un 25% más grande de lo normal, lo que aumenta la visibilidad del área donde se muestran los iconos

![image](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` o `--small`

Esto hace que la ventana parezca aproximadamente un 25% más pequeña de lo normal

![image](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## Apariencia de la ventana

Puede forzar el modo oscuro o el modo claro, y el sistema utilizará esa apariencia, independientemente de la preferencia actual del usuario

`--appearance dark` o `--appearance light`

## Modo mini

El modo "mini" se activa pasando el argumento `--mini`.

El modo "mini" fuerza la aparición de una ventana pequeña con un diseño modificado y opciones limitadas para mostrar contenido. `--title` es más pequeño y se ubica centrado en la parte superior de la ventana, o puede desactivarse con `--title none`. `--message` puede contener hasta cuatro líneas de texto (cualquier texto más largo será truncado). `--icon`, cuando es visible, ocupa la parte izquierda de la ventana, y todo el contenido restante se muestra a la derecha. `--hideicon` y `--icon none` se respetan. `--button1text` y `--button2text` están disponibles, pero el botón de información no.

![image](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

Si se utiliza el argumento `--progress`, el área del botón se elimina y se reemplaza con una barra de progreso y una línea de texto que indica el progreso. Para cerrar el diálogo, es necesario pasar el comando `quit:` al archivo de comandos.

![image](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - Configure un estilo de ventana predefinido

Modifica los valores predeterminados para cambiar la forma en que se muestra un cuadro de diálogo.

Los estilos distintos de `--mini` no tienen atributos especiales, y la apariencia visual se puede lograr utilizando los diferentes parámetros para configurar las propiedades de la ventana.

`centered`, `alert` y `caution` utilizarán el valor de `--title` y lo añadirán como un encabezado al área de mensajes, y luego deshabilitarán el título. Esto coloca el título debajo del icono central que se muestra.

    "mini" es funcionalmente equivalente a "--mini". "centered" establece todas las opciones para contenido centrado. "alert" define una ventana de diálogo preconfigurada de 300x300 con contenido centrado. "caution" (precaución) y "warning" (advertencia) son equivalentes a "alert", pero con el icono configurado

Ejemplo de `dialog --style alert`:

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

Esto es equivalente a escribir:

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## Tamaños de ventanas personalizados

El diálogo puede tener el tamaño que desee, en lugar de los valores predeterminados, las opciones `--small` o `--big`.

`--width` y `--height` se pueden utilizar para definir el tamaño del diálogo deseado. El contenido se ajustará para adaptarse al tamaño.

swiftDialog permite el uso de `%` como una función del tamaño actual de la pantalla, por ejemplo, `--width 50%` establecerá el ancho del cuadro de diálogo al 50% de la resolución actual de la pantalla.

![image](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` superpondrá todos los elementos de la pantalla con un fondo desenfocado y colocará la ventana de diálogo por encima de todas las demás ventanas. Esto permite tanto una comunicación más enfocada como flujos de trabajo en los que no se desea que el usuario interactúe con otras aplicaciones o con el escritorio (por ejemplo, durante el proceso de incorporación).


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### Comportamiento de `--ontop` con `--blurscreen` y las ventanas de diálogo existentes

Si existe un diálogo activo `--blurscreen`, el uso de `--ontop` hará que los diálogos posteriores aparezcan por encima de la capa de desenfoque. Esto permite ejecutar un diálogo en segundo plano y abrir diálogos adicionales, manteniéndolos visibles. Es importante tener en cuenta que, si planea interactuar con estos diálogos mediante programación, asegúrese de utilizar archivos de comandos únicos para cada uno.

## `--showonallscreens`

Cuando se utiliza, la ventana de diálogo aparecerá en todos los escritorios virtuales

Si se están utilizando múltiples pantallas, el cuadro de diálogo aparecerá en todos los escritorios virtuales asociados con la pantalla desde la que se haya iniciado.