---
title: Archivo de comandos
description: Actualizar dinámicamente el diálogo con contenido nuevo, utilizando archivos de comandos
translationSynced: 2026-11-24T22:28:45+00:00
---

Alguno del contenido de los cuadros de diálogo puede actualizarse en tiempo real, incluso después de que se hayan mostrado. Esto se facilita mediante el envío de comandos a un archivo de comandos que Dialog lee e interpreta.

---

Es necesario iniciar el programa Dialog en segundo plano para permitir que se le envíen comandos desde el mismo script.

```sh
/usr/local/bin/dialog & sleep 0.1
```

El dispositivo `sleep 0.1` otorga 100 milisegundos para que el sistema se inicialice antes de que se envíe el primer comando.

La ruta predeterminada del archivo de comandos es `/var/tmp/dialog.log`. Se puede establecer una ruta personalizada utilizando el argumento `--commandfile`:

```sh
dialog --commandfile /var/tmp/my.log
```

Envíe comandos utilizando:

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## Contenido

| Comando | Descripción |
|---|---|
| `title: <text>` | Actualizar el título del diálogo |
| `title: none` | Ocultar el área del título |
| `titlefont: <params>` | Actualizar las propiedades de la fuente del título. Acepta pares separados por espacios: `key=value`, `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>` |
| `message: <text>` | Reemplace el contenido del mensaje. Admite Markdown. |
| `message: + <text>` | Añadir al mensaje existente (agrega una línea nueva antes del contenido nuevo). |
| `message: /path/to/file.md` | Cargue el contenido del mensaje desde un archivo Markdown local |
| `alignment: [left\|center\|right]` | Establezca la alineación del texto del mensaje |

---

## Icono

| Comando | Descripción |
|---|---|
| `icon: <path\|url\|SF Symbol>` | Cambiar el icono que se muestra |
| `icon: none` | Ocultar el icono |
| `icon: centre` / `icon: center` | Mueva el icono a la posición central |
| `icon: left` / `icon: default` | Mueva el icono de nuevo a su posición predeterminada, que es a la izquierda |
| `icon: size: <num>` | Cambiar el tamaño del icono |
| `iconalpha: <float>` | Establecer la opacidad del icono (0.0: transparente → 1.0: opaco). |
| `overlayicon: <path\|url\|SF Symbol>` | Establezca el icono de la superposición |
| `overlayicon: none` | Ocultar el icono superpuesto |

---

## Banner y fondo

| Comando | Descripción |
|---|---|
| `bannerimage: <path\|url>` | Establezca la imagen de encabezado |
| `bannerimage: none` | Eliminar la imagen de encabezado |
| `bannertext: enable` | Mostrar el título como texto de encabezado (establece el color de la fuente en blanco). |
| `bannertext: disable` | Restaurar la apariencia predeterminada del título |
| `bannertext: shadow` | Activar la sombra difusa en el texto del título del banner |
| `bannertext: <text>` | Establezca el texto del título del banner y active el modo de texto del banner |

---

## Imágenes y medios

| Comando | Descripción |
|---|---|
| `image: <path\|url>` | Mostrar una imagen (se añade a la galería de imágenes si ya se está mostrando alguna). |
| `image: show` | Mostrar la imagen actual |
| `image: hide` | Ocultar la imagen actual |
| `image: clear` | Eliminar todas las imágenes |
| `imagecaption: <text>` | Coloque el texto descriptivo debajo de la imagen que se muestra |
| `video: <path\|url>` | Mostrar un video. Compatible con los atajos `youtube=<id>` y `vimeo=<id>`. |
| `video: none` | Eliminar el video |
| `webcontent: <url>` | Cargue una URL en el área de contenido web |
| `webcontent: none` | Eliminar el contenido web |

---

## Botones

| Comando | Descripción |
|---|---|
| `button1: enable` / `button1: show` | Activar el botón 1 |
| `button1: disable` / `button1: hide` | Desactivar el botón 1 |
| `button1text: <text>` | Botón "Actualizar" 1 (etiqueta) |
| `button2: enable` / `button2: show` | Activar el botón 2 |
| `button2: disable` / `button2: hide` | Desactivar el botón 2 |
| `button2text: <text>` | Botón "Actualizar" (etiqueta 2) |
| `buttonsize: [mini\|small\|regular\|large]` | Establecer el tamaño del botón |
| `infobutton: <text>` | Actualizar la etiqueta del botón de información |
| `infotext: <text>` | Actualice el área de texto informativo |
| `infotext: disable` / `infotext: hide` | Ocultar el texto informativo |
| `infotext: reset` / `infotext: clear` | Borrar el texto informativo |

---

## Cuadro de información

| Comando | Descripción |
|---|---|
| `infobox: <text>` | Reemplace el contenido del cuadro de información. Admite Markdown. |
| `infobox: + <text>` | Añadir contenido a la información que ya se encuentra en el cuadro informativo |
| `infobox: /path/to/file.md` | Cargue el contenido del cuadro de información desde un archivo Markdown local |

---

## Barra de progreso

| Comando | Descripción |
|---|---|
| `progress: <int>` | Establezca la barra de progreso en un valor específico |
| `progress: increment` | Aumente la barra de progreso en un paso |
| `progress: increment <n>` | Incrementar la barra de progreso en `n` pasos |
| `progress: complete` | Establezca la barra de progreso al máximo |
| `progress: reset` / `progress: indeterminate` | Restablezca la barra de progreso al modo indeterminado |
| `progress: show` / `progress: enable` / `progress: create` | Mostrar la barra de progreso |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | Ocultar la barra de progreso |
| `progresstext: <text>` | Actualice la etiqueta que se encuentra debajo de la barra de progreso |

---

## Listas

| Comando | Descripción |
|---|---|
| `list: <csv>` | Reemplace la lista con nuevos elementos separados por comas |
| `list: clear` | Eliminar todos los elementos de la lista y ocultar la lista |
| `list: show` | Mostrar la lista |
| `list: hide` | Ocultar la lista sin borrar su contenido |

### Actualizar elementos de la lista

Actualizar un elemento existente mediante su título (formulario sencillo):

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

Actualice un elemento con control total utilizando propiedades separadas por comas:

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

Añadir un nuevo elemento al final de la lista:

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

Eliminar un elemento:

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**Propiedades disponibles `listitem`:**

| Propiedad | Descripción |
|---|---|
| `title: <text>` | Coincidir el elemento con el título |
| `index: <int>` | Coincidir el elemento por índice (basado en cero). |
| `subtitle: <text>` | Establezca el subtítulo del artículo |
| `icon: <path\|url\|SF Symbol>` | Establecer el icono del elemento |
| `iconalpha: <float>` | Establecer la opacidad del icono del elemento |
| `status: <status>` | Establezca el icono de estado. Puede ser uno de los siguientes: `wait`, `success`, `fail`, `error`, `pending`, `progress`, o el nombre de un símbolo de SF (opcionalmente con un sufijo de color, por ejemplo, `lock.shield.fill-green`). |
| `statustext: <text>` | Establezca el texto de la etiqueta de estado |
| `progress: <float>` | Establece un valor de progreso en línea (muestra un estado tipo "barra de progreso"). |
| `action: <url>` | URL que se abrirá cuando se haga clic en el elemento |
| `add:` | Añadir un nuevo elemento a la lista |
| `delete:` | Eliminar el elemento coincidente |

---

## Mensaje de ayuda

| Comando | Descripción |
|---|---|
| `helpmessage: <text>` | Actualice el contenido del mensaje de ayuda. Admite formato Markdown. |

---

## Ventana

| Comando | Descripción |
|---|---|
| `width: <num>` | Cambiar el ancho de la ventana |
| `height: <num>` | Cambie la altura de la ventana |
| `position: <position>` | Mueva la ventana. Una de las opciones `top`, `bottom`, `left`, `right`, `centre`, o una combinación (por ejemplo, `topright`). |

---

## Visibilidad de la ventana

| Comando | Descripción |
|---|---|
| `activate:` | Mueva la ventana de diálogo al frente |
| `show:` | Mostrar la ventana de diálogo |
| `hide:` | Ocultar la ventana de diálogo |
| `minimize:` / `minimise:` | Minimiza la ventana de diálogo para que aparezca en la barra de acceso rápido |
| `maximize:` / `maximise:` | Restaurar una ventana de diálogo minimizada |
| `blurscreen: enable` | Activar el efecto de desenfoque de pantalla |
| `blurscreen: disable` | Desactive el efecto de desenfoque de pantalla |

---

## Icono de la barra de tareas

| Comando | Descripción |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | Mostrar el icono de "Diálogo" en la barra de acceso rápido |
| `showdockicon: <any other value>` | Ocultar el icono de la ventana de diálogo en la barra de acceso rápido |
| `dockicon: <file\|url>` | Establezca una imagen personalizada como el icono de la barra de acceso rápido |
| `dockicon: none` / `dockicon: default` | Restaurar el icono predeterminado del panel de diálogo |
| `dockiconbadge: <text>` | Mostrar un distintivo en el icono de la barra de aplicaciones |
| `dockiconbadge: none` / `dockiconbadge: remove` | Eliminar el indicador del icono de la barra de acceso rápido |
| `bounce:` | Pulse una vez el icono de Dock (informativo). |
| `bounce: critical` | Mantenga presionada la tecla "Bounce" en el icono de la aplicación "Dock" hasta que la ventana aparezca en primer plano |

---

## Dejar

| Comando | Descripción |
|---|---|
| `quit:` | Cuadro de diálogo de salida con código de error 5 |
