---
title: Opciones de línea de comandos
description: Referencia completa de todas las opciones y argumentos de línea de comandos de swiftDialog
translationSynced: 2026-11-24T22:24:26+00:00
---

El diálogo se puede configurar a través de opciones de línea de comandos. Todas las opciones también se pueden especificar utilizando un archivo de configuración [JSON](/es/advanced/json-configuration).

```sh
dialog --title "Hello" --message "World"
```

Utilice `--help <option>` para obtener información detallada sobre un argumento específico.

---

## Contenido

| Argumento | Corto | Descripción |
|---|---|---|
| `--title <text>` | `-t` | Establezca el título del diálogo. Utilice `none` para ocultarlo. |
| `--subtitle <text>` | | Una línea de texto secundaria que se muestra debajo del título. También se utiliza como texto de subtítulo para [notificaciones](/es/advanced/notifications). |
| `--message <text>` | `-m` | Establezca el mensaje del diálogo. Admite [Markdown](/es/basic-use/markdown). |
| `--messagealignment [left\|centre\|right]` | | Alineación horizontal del mensaje |
| `--messageposition [top\|centre\|bottom]` | | Posición vertical del bloque de contenido del mensaje |
| `--titlefont <params\|json>` | | Modifique la fuente del título. Acepta pares separados por comas o un objeto JSON: `key=value`, `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow` |
| `--messagefont <params\|json>` | | Modificar la fuente del mensaje. Acepta pares separados por comas `key=value` o un objeto JSON |

Consulte [Título](/es/basic-use/title) y [Mensaje](/es/basic-use/message) para más detalles.

---

## Icono

| Argumento | Corto | Descripción |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | Establezca el icono del diálogo. Acepta la ruta de un archivo, una URL, un símbolo de SF (`SF=name`), elementos predefinidos o un objeto JSON |
| `--iconsize <num>` | | Tamaño del icono en puntos (valor predeterminado: 150). |
| `--iconalpha <num>` | | Opacidad del icono, desde 0.0 (transparente) hasta 1.0 (opaco). |
| `--iconalttext <text>` | | Etiqueta de accesibilidad para el icono |
| `--overlayicon <file\|url\|json>` | `-y` | La imagen superpuesta se muestra en la esquina inferior derecha del icono. Admite los mismos formatos que `--icon` |
| `--hideicon` | `-h` | Ocultar el icono para ampliar el área de texto |
| `--centreicon` / `--centericon` | | Mover el icono para que quede centrado entre el título y el mensaje |

Consulte [Icono](/es/basic-use/icon)] para obtener más detalles.

---

## Banner y fondo

| Argumento | Corto | Descripción |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | Muestra una imagen de encabezado en la parte superior del cuadro de diálogo |
| `--bannertitle <text>` | | Mostrar el texto del título superpuesto en el banner |
| `--bannertext <text>` | | Equivalente a establecer `--bannertitle` y `--title` |
| `--bannerheight <num>` | | Establezca la altura del banner |
| `--background <file>` | `-bg` | Establecer una imagen de fondo/marca de agua |
| `--bgalpha <num>` | `-ba` | Opacidad de la imagen de fondo (valor predeterminado: 0,5). |
| `--bgposition <position>` | `-bp` | Posición de la imagen de fondo (por ejemplo, `center`, `topleft`). |
| `--bgfill [fill\|fit]` | `-bf` | Modo de relleno de la imagen de fondo |
| `--bgscale [fill\|fit]` | `-bs` | Modo de escalado de la imagen de fondo |
| `--screenbackground <file\|url>` | | Mostrar una imagen a pantalla completa, detrás de la ventana de diálogo |

Consulte [Imágenes de banners](/es/advanced/banner-images) e [Imágenes de fondo](/es/advanced/background-images) para más detalles.

---

## Botones

| Argumento | Corto | Descripción |
|---|---|---|
| `--button1text <text>` | | Etiqueta para el Botón 1 (vinculado a la tecla "Retorno" ↵, valor predeterminado: `OK`). |
| `--button1action <url>` | | URL que se abrirá al hacer clic en el Botón 1 |
| `--button1shellaction <cmd>` | | Comando de shell que se ejecutará al hacer clic en el botón 1 |
| `--button1symbol <sf symbol\|json>` | | Símbolo SF o objeto JSON para el botón 1 |
| `--button1disabled` | | Iniciar con el botón 1 desactivado |
| `--button2` | `-2` | Mostrar botón 2 |
| `--button2text <text>` | | Etiqueta para el Botón 2 (vinculado a la tecla Esc ⎋, valor predeterminado: `Cancel`). |
| `--button2symbol <sf symbol\|json>` | | Símbolo de SF o objeto JSON para el botón 2 |
| `--button2disabled` | | Iniciar con el botón 2 desactivado |
| `--infobutton` | `-3` | Mostrar el botón de información |
| `--infobuttontext <text>` | | Etiqueta para el botón de información |
| `--infobuttonaction <url>` | | URL que se abrirá cuando se haga clic en el botón de información |
| `--infobuttonsymbol <sf symbol\|json>` | | Símbolo SF o objeto JSON para el botón de información |
| `--buttonstyle [center\|stack]` | | Diseño de la disposición de los botones |
| `--buttonsize [mini\|small\|regular\|large]` | | Tamaño del botón |
| `--buttontextsize <num>` | | Tamaño de fuente de la etiqueta del botón |
| `--quitoninfo` | | Cerrar el cuadro de diálogo cuando se selecciona el botón de información |

Consulte [Botones](/es/basic-use/buttons)] para obtener más detalles.

---

## Flujo de trabajo

| Argumento | Corto | Descripción |
|---|---|---|
| `--nextbuttontext <text>` | | Etiqueta para el botón "Siguiente" en el flujo de trabajo (valor predeterminado: `Next`). |
| `--previousbuttontext <text>` | | Etiqueta para el botón "Anterior" del flujo de trabajo (por defecto: `Previous`). |
| `--onadvance <command>` | | Comando de shell que se ejecuta al avanzar entre las páginas del flujo de trabajo <br> (la entrada se proporciona a través de la entrada estándar; un código de salida diferente de cero impide el avance). |

Consulte [Flujo de trabajo](/es/advanced/workflows)] para obtener más detalles.

---

## Mensaje de ayuda

| Argumento | Corto | Descripción |
|---|---|---|
| `--helpmessage <text>` | | Mostrar un botón de ayuda con contenido emergente. Admite Markdown. |
| `--helpimage <file\|url>` | | Añadir una imagen al cuadro de ayuda emergente |
| `--helpsheetbuttontext <text>` | | Etiqueta para el botón de cerrar en la página de ayuda (valor predeterminado: `OK`). |
| `--helpalignment [left\|centre\|right]` | | Alineación del contenido del mensaje de ayuda |

Consulte [el mensaje de ayuda](/es/operation/help-message) para obtener más información.

---

## Imágenes, videos y contenido web

| Argumento | Corto | Descripción |
|---|---|---|
| `--image <file\|url>` | `-g` | Mostrar una imagen. Varias instancias crean un carrusel. |
| `--imagecaption <text>` | | Leyenda que se muestra debajo de la imagen |
| `--video <file\|url>` | | Mostrar un video. Compatible con los atajos `youtube=<id>` y `vimeo=<id>`. |
| `--videocaption <text>` | | Título que se muestra debajo del video |
| `--autoplay` | | Reproducir automáticamente el vídeo al iniciar la aplicación |
| `--webcontent <url>` | | Mostrar una página web en el área de mensajes |

Consulte [Imágenes](/es/basic-use/images), [Vídeo](/es/basic-use/video) y [Contenido web](/es/basic-use/web-content) para obtener más detalles.

---

## Área de información

| Argumento | Corto | Descripción |
|---|---|---|
| `--infotext <text>` | | Reemplace el botón de información con texto estático |
| `--infobox <text>` | | Mostrar texto (se admite formato Markdown) debajo del icono |
| `--infoboxwidth <num>` | | Establezca el ancho del cuadro de información de forma independiente al tamaño del icono |

Consulte [la caja de información](/es/advanced/info-box)] para obtener más detalles.

---

## Entrada del usuario

| Argumento | Corto | Descripción |
|---|---|---|
| `--textfield <text\|json>[,options]` | | Añada un campo de entrada de texto. Admite `required`, `secure`, `prompt`, `regex`, `fileselect`, `date`, `time`, `mindate`, `maxdate` y más. También puede especificarse como un objeto JSON |
| `--textfieldlivevalidation` | | Mostrar retroalimentación en tiempo real sobre la validación de expresiones regulares en los campos de texto |
| `--checkbox <text\|json>` | | Añada una casilla de verificación con la etiqueta especificada. También se puede especificar como un objeto JSON |
| `--checkboxstyle [checkbox\|switch][,size]` | | Cambiar la apariencia de la casilla de verificación |
| `--selecttitle <text>[,options]` | | Agregue una lista desplegable con el nombre especificado |
| `--selectvalues <csv>` | | Valores separados por comas para la lista de selección |
| `--selectdefault <text>` | | Valor predeterminado seleccionado para la lista desplegable |
| `--selectstyle` | | Estilo para la lista desplegable |
| `--selectitem <json>` | | Defina un elemento de una lista seleccionable utilizando la sintaxis de objeto JSON |

Consulte las secciones de "Campos de texto" ](/es/advanced/textfields), "Casillas de verificación" ](/es/advanced/checkboxes) y "Listas desplegables" ](/es/advanced/select-lists) para obtener más detalles.

### Configuración JSON para argumentos individuales

Muchos argumentos que aceptan valores separados por comas también pueden especificarse como objetos JSON. Esto proporciona un mayor control y es especialmente útil para configuraciones complejas.

**Detección:** Si un valor se puede interpretar como un objeto JSON, se utiliza el constructor de JSON; de lo contrario, se aplica el análisis CSV.

**Argumentos respaldados:**
- `--textfield` - Configuración completa del campo, con todos los modificadores
- `--checkbox` - Casilla de verificación con icono y opción de habilitar botón
- `--listitem` - Elemento de lista con objetos de icono anidados
- `--selecttitle` - Se trata de forma idéntica a `--selectitem`
- `--selectitem` - Elementos de la lista de selección definidos en JSON
- `--titlefont` / `--messagefont` - Configuración de la fuente: color, tamaño, grosor, sombra
- `--icon` / `--overlayicon` - Objetos de iconos con símbolos, colores, paletas y animaciones
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - Símbolos de botones con indicaciones de posición

Consulte las páginas de documentación individuales para obtener información detallada sobre los esquemas JSON y ejemplos.

---

## Listados de elementos

| Argumento | Corto | Descripción |
|---|---|---|
| `--listitem <text\|json>` | | Añadir un elemento a la lista. Admite iconos de estado y acciones al hacer clic. También se puede especificar como un objeto JSON con soporte para iconos anidados |
| `--liststyle [expanded\|compact]` | | Espaciado vertical entre las filas de la lista |
| `--enablelistselect` | | Permitir la selección de elementos de la lista; la selección realizada se devuelve al salir |

Consulte [Listas de elementos](/es/advanced/item-lists)] para obtener más detalles.

---

## Temporizador y progreso

| Argumento | Corto | Descripción |
|---|---|---|
| `--timer [<seconds>]` | | Mostrar un temporizador de cuenta regresiva (por defecto: 10 segundos). Finaliza con el código 4 si se alcanza el tiempo límite. |
| `--hidetimerbar` | | Ocultar la barra de temporizador mientras se sigue contando el tiempo |
| `--hidetimer` | | Ocultar el temporizador por completo |
| `--progress [<int>]` | | Mostrar una barra de progreso con el número de pasos especificado |
| `--progresstext <text>` | | Texto inicial que se muestra debajo de la barra de progreso |

Consulte [Temporizador y progreso](/es/advanced/timer-progress)] para obtener más detalles.

---

## Tamaño y posición de la ventana

| Argumento | Corto | Descripción |
|---|---|---|
| `--width <num>` | | Ancho de la ventana de diálogo en puntos |
| `--height <num>` | | Altura de la ventana de diálogo, medida en puntos |
| `--small` | `-s` | Reducir el tamaño predeterminado de la ventana en un 25% |
| `--big` | `-b` | Aumentar el tamaño predeterminado de la ventana en un 25% |
| `--position <position>` | | Posición de la ventana (por ejemplo, `center`, `topright` o `x,y`). |
| `--positionoffset <int>` | | Desplazamiento del borde al usar `--position` (valor predeterminado: 16). |
| `--moveable` | `-o` | Permitir que la ventana se pueda arrastrar |
| `--resizable` | | Permitir que la ventana se redimensione (implica `--moveable`). |
| `--ontop` | `-p` | Mantenga esta ventana siempre visible, por encima de todas las demás |
| `--windowbuttons [close,min,max]` | | Habilitar los botones para cerrar, minimizar y maximizar la ventana |
| `--showonallscreens` | | Mostrar la ventana en todas las pantallas conectadas |
| `--appearance [dark\|light]` | | Modificar la apariencia de la ventana |

Consulte [Tamaño de la ventana](/es/advanced/window-size) y [Disposición](/es/advanced/layout) para más detalles.

---

## Estilos de ventana predefinidos

| Argumento | Corto | Descripción |
|---|---|---|
| `--style <preset>` | | Aplicar un estilo predefinido: `presentation`, `mini`, `centered`, `alert`, `caution`, `warning` |
| `--mini` | | Ventana compacta que muestra el título, el icono y un mensaje de dos líneas |
| `--fullscreen` | `-f` | Modo de pantalla completa (sin botones; los eventos del teclado siguen funcionando). |
| `--presentation` | | Modo de presentación con barra de progreso y diseño estructurado |
| `--eula` | | Mostrar en modo de aceptación de la licencia de usuario final |
| `--blurscreen` | | Desenfoque todo el contenido de la pantalla que se encuentra detrás de la ventana de diálogo |
| `--hideotherapps` | | Ocultar todas las demás aplicaciones al iniciar |

Consulte [Pantalla completa](/es/advanced/full-screen) y [Presentación](/es/advanced/presentation) para obtener más detalles.

---

## Notificaciones

| Argumento | Corto | Descripción |
|---|---|---|
| `--notification` | | Enviar una notificación del sistema en macOS |
| `--identifier <text>` | `-id` | Identificador único para la notificación |
| `--remove` | | Elimine la notificación que coincida con el elemento `--identifier` |
| `--enablenotificationsounds` | | Activar los sonidos de notificación |

Consulte [Notificaciones](/es/advanced/notifications)] para obtener más detalles.

---

## Sonido

| Argumento | Corto | Descripción |
|---|---|---|
| `--sound <file\|url>` | | Reproducir un archivo de audio al iniciar |
| `--showsoundcontrols` | | Mostrar los controles de reproducción (reproducir/pausar, silenciar, barra de progreso). |

---

## Icono de la barra de tareas

| Argumento | Corto | Descripción |
|---|---|---|
| `--showdockicon` | | Mostrar el icono de "Diálogo" en el Dock de macOS |
| `--dockicon <file\|url>` | | Mostrar una imagen personalizada como el icono de la barra de aplicaciones (implica `--showdockicon`). |
| `--dockiconbadge <text>` | | Mostrar un distintivo en el icono de la barra de tareas (Dock) visible |

---

## Archivo de comandos

| Argumento | Corto | Descripción |
|---|---|---|
| `--commandfile [<file>]` | | Ruta al archivo de comandos para las actualizaciones en tiempo real del diálogo (valor predeterminado: `/var/tmp/dialog.log`). |
| `--displaylog <file>` | | Mostrar el contenido de un archivo tal como está escrito |
| `--loghistory [<int>]` | | Pre-llenar `--displaylog` con las últimas N líneas (por defecto: 100). |

Consulte el [archivo de comandos](/es/advanced/command-file) para más detalles.

---

## Entrada y salida en formato JSON

| Argumento | Corto | Descripción |
|---|---|---|
| `--jsonfile <file>` | | Cargar la configuración del diálogo desde un archivo JSON |
| `--jsonstring <text>` | | Cargar la configuración del diálogo desde una cadena JSON |
| `--json` | `-j` | Los resultados se muestran en formato JSON |

Consulte [la configuración JSON](/es/advanced/json-configuration)] para obtener más detalles.

---

## Teclado e interacción

| Argumento | Corto | Descripción |
|---|---|---|
| `--quitkey <char>` | | Tecla de salida personalizada (utilizada como `⌘ + <key>`, valor predeterminado: `q`). |
| `--hidedefaultkeyboardaction` | | Exigir `⌘ + ⇧` para activar las acciones del teclado "Retorno/Esc" |
| `--alwaysreturninput` | | Siempre que el programa finalice, debe mostrar la información que el usuario haya introduido, independientemente del código de salida |
| `--ignorednd` | `-d` | Mostrar la ventana de diálogo incluso cuando el modo "No molestar" está activado |
| `--vieworder <csv>` | | Modificar el orden de visualización de los tipos de elementos de entrada |

---

## Autorización

| Argumento | Corto | Descripción |
|---|---|---|
| `--key <string>` | `-k` | Se requiere una clave de autenticación para iniciar el diálogo |
| `--checksum <string>` | | Generar un hash SHA256 (para su uso con `--key`). |

Consulte [Autorización](/es/operation/authorization)] para obtener más detalles.

---

## Ventana de inicio de sesión

| Argumento | Corto | Descripción |
|---|---|---|
| `--loginwindow` | | Mostrar el diálogo en la ventana de inicio de sesión (requiere un LaunchAgent adecuado). |

Consulte [la ventana de inicio de sesión](/es/operation/login-window)] para obtener más detalles.

---

## Modo de inspección

| Argumento | Corto | Descripción |
|---|---|---|
| `--inspect-mode` | | Iniciar en modo de inspección |
| `--inspect-config <file>` | | Especificar la configuración para el modo de inspección |
| `--inspect-schema <file>` | | Especificar el esquema para el modo de inspección |
| `--schema-validate <file>` | | Validar una configuración frente a un esquema |

Consulte [Modo de inspección](/es/advanced/inspect-mode)] para obtener más detalles.

---

## Utilidades y depuración

| Argumento | Corto | Descripción |
|---|---|---|
| `--version` | `-v` | Imprima la cadena de versión |
| `--help [<argument>]` | | Imprima la ayuda, o la ayuda detallada para un argumento específico |
| `--licence` | `-l` | Imprima la licencia |
| `--debug [<colour>]` | | Habilite el modo de depuración con resaltado opcional de los límites de contenido |
| `--verbose` | `-vvv` | Habilitar la salida detallada de los registros |
| `--listfonts` | | Imprimir los nombres de las fuentes disponibles |
| `--demo` | | Iniciar en modo de demostración |
| `--builder` | | Iniciar la interfaz de usuario del kit de construcción |
| `--jh` | `-jh` | Activar el modo de compatibilidad de jamfHelper |

Consulte [Builder](/es/reference/builder)] para obtener más detalles.
