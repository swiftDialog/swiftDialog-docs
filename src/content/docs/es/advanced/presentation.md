---
title: Presentación
description: Creación de cuadros de diálogo en modo de presentación para procesos y tareas en curso
translationSynced: 2026-11-24T22:39:35+00:00
---

## Modo de presentación

`--presentation` o `--style presentation`

El modo de presentación es un modo de salida únicamente (sin interacción del usuario) de swiftDialog, diseñado para mostrar un proceso o tarea en curso.

Para actualizar la pantalla, será necesario utilizar un [archivo de comandos](/es/advanced/command-file) y los comandos correspondientes.

La interfaz se divide en dos áreas principales de contenido y un pie de página que contiene una barra de progreso y botones.

## Área de información

La parte izquierda de la ventana, que ocupa aproximadamente un tercio de su superficie, contiene un área de información y puede mostrar una de las siguientes opciones:

### Predeterminado

Un color de fondo que representa la preferencia del usuario en cuanto al color de resaltado.

Puede aplicar, opcionalmente, los siguientes modificadores:
 - `--infobox <text>` para mostrar texto (se admite formato Markdown).
   - El texto está centrado verticalmente
 - `--background color=<color|hex>` para establecer el color de fondo
   - Si no se especifica ningún color, se utiliza el color de acento predeterminado del sistema
 - `--icon <image>` para mostrar un icono en la esquina superior izquierda
 - `--iconsize <int>` para establecer el tamaño del icono.

### Imagen

Especifique uno o más `--image <image>` para rellenar esta área con una imagen

Varias imágenes se mostrarán en forma de carrusel. Incluya `--autoplay <sec>` para que las imágenes se desplacen automáticamente.

**Consejos**
* Para obtener los mejores resultados, utilice imágenes con formato vertical
* Las imágenes se ajustarán para ocupar todo el espacio, y es posible que se realicen recortes si se utilizan varias imágenes con diferentes proporciones.

Para ejecutar el modo de presentación, utilice `--debug`. Después de cerrar el cuadro de diálogo, se incluirá en el registro de depuración el tamaño de imagen recomendado para la ventana actual.

e.g.

    DEBUG: El tamaño ideal de la imagen de la barra lateral para esta configuración de ventana sería: ancho: 492.0, altura: 636.0

### Contenido web

Especifique `--webcontent <url>` para mostrar el contenido de un archivo fuente HTML.

**Consejo**
* Si se utiliza un archivo local, se debe referenciar el archivo mediante `file:///path/to/file.html`

## Área de contenido

La parte derecha de la ventana, que ocupa aproximadamente dos tercios de su superficie, está dedicada a mostrar contenido en una de las siguientes formas:

### Predeterminado

Cualquier `--message <text>` en cualquiera de los formatos admitidos.

### Lista

Una o más opciones --listitem <item> en cualquiera de los formatos admitidos.

## Pie de página

Dado que la función principal del modo de presentación es mostrar el progreso y otro contenido actualizable, la barra inferior de la ventana siempre es visible y está dedicada a una barra de progreso de ancho completo y a botones.

## Ejemplos

Aquí solo hay texto

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

**Vista web en el área de información y elementos de lista en el área de contenido.**

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">