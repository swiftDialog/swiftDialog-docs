---
title: Guiones de demostración
description: Guion completo para la demostración de cómo seleccionar e instalar aplicaciones
translationSynced: 2026-11-24T23:03:12+00:00
---

Una completa suite de demostraciones se puede encontrar en https://github.com/swiftDialog/demo

## Conjunto completo de demostraciones de swiftDialog

Una colección de scripts para zsh que demuestran cada una de las funciones principales de [swiftDialog](https://github.com/swiftDialog/swiftDialog), a través de un recorrido interactivo y autoguiado.

## Requisitos

- macOS 15 o versiones posteriores
- [**swiftDialog versión 3 o superior**](https://github.com/swiftDialog/swiftDialog/releases)

## Guía de inicio rápido

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

El controlador principal utiliza directamente swiftDialog. Seleccione las demostraciones que incluyen casillas de verificación y, a continuación, revise cada una de ellas paso a paso.

## Habilidades de inteligencia artificial para la creación de contenido en swiftDialog

**¿Es la primera vez que usa swiftDialog?** Comience con la página oficial de [swiftDialog Builder](https://swiftdialog.app/builder/builder/) para familiarizarse y crear prototipos visuales. Luego, utilice uno de los paquetes de herramientas incluidos en el repositorio para transformar ese conocimiento en scripts de shell con la estructura del repositorio. El "Builder" es útil, pero no es exhaustivo y no sustituye las decisiones finales sobre el tamaño, la limpieza y el flujo de trabajo.

### Habilidades disponibles

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** — Para GitHub Copilot / OpenAI Codex

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Flujo de trabajo de Codex y selección de niveles
- [`references/`](skills/codex-swiftdialog-builder/references/) — Guía para la creación y diseño de demostraciones
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — Scripts de inicio básicos]
- Incluye un proceso de ejecución de Jamf/root `/var/tmp`, además de un mecanismo de transferencia de propiedad para flujos de trabajo de comandos y archivos que se ejecutan como `root`

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** — Para Claude Sonnet

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Flujo de trabajo de Claude y selección de planes
- [`references/`](skills/claude-swiftdialog-builder/references/) — Guía para la creación y diseño de demostraciones
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — Scripts de inicio básicos]
- Incluye un proceso de ejecución de Jamf/root `/var/tmp`, además de un mecanismo de transferencia de propiedad para flujos de trabajo de comandos y archivos que se ejecutan como `root`

Ambas habilidades siguen las mismas convenciones de repositorio y producen la misma salida de script; elija la que se adapte a su plataforma de inteligencia artificial. Consulte [`skills/README.md`](skills/README.md) para obtener instrucciones detalladas sobre su uso.

Estos son paquetes de habilidades para asistentes de inteligencia artificial, y no demostraciones funcionales que se puedan ejecutar dentro del sistema.

## Entorno de desarrollo asistido por inteligencia artificial

Después de explorar el conjunto de demostraciones y comprender las capacidades de swiftDialog, utilice el directorio [`playground/`](playground/)] para crear sus propios scripts personalizados con la ayuda de la inteligencia artificial. El entorno de pruebas incluye una guía completa y detallada que le muestra cómo:

- Utilice los asistentes de IA (Claude, Copilot) aprovechando las funciones integradas
- Elija el nivel adecuado para su flujo de trabajo (diálogos básicos → formularios → actualizaciones de progreso → modo de inspección).
- Siga escenarios detallados y realistas, con indicaciones precisas y ejemplos de las interacciones esperadas con la inteligencia artificial
- Cree scripts listos para producción para tareas de administración de Mac (configuración inicial, cumplimiento normativo, despliegue, monitorización, confirmación de acciones destructivas).

**Comience aquí:** [`playground/README.md`](playground/README.md) — Su espacio de trabajo para el desarrollo rápido de scripts de swiftDialog con la ayuda de la inteligencia artificial.

## Índice de demostraciones

- `01_basic_styles.zsh` — `--style` (alerta, precaución, advertencia, centrado), sobrescritura de estilos
- `02_title_message.zsh` — `--title`, `--titlefont`, `--message`, `--messagefont`, `--messagealignment`, `--messageposition`, `--bannertitle`, título "ninguno"
- `03_icons.zsh` — `--icon` (Símbolos del sistema, aplicaciones, funciones integradas, códigos QR, paleta de colores, color automático, grosor), `--iconsize`, `--iconalpha`, `--centreicon`, `--overlayicon`, `--hideicon`
- `04_buttons.zsh` — `--button1text`, `--button1symbol`, `--button1disabled`, `--button2text`, `--button2symbol`, `--infobuttontext`, `--infobuttonsymbol`, `--infobuttonaction`, `--buttonstyle` (centrado, apilado), `--buttonsize`, `--buttontextsize`, `--hidedefaultkeyboardaction`
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` — `--progress` (absoluto, incremento, restablecer, completar), `--progresstext`, `--progresstextalignment`, `--timer`, `--hidetimerbar`, actualizaciones del progreso del archivo de comandos
- `07_text_fields.zsh` — `--textfield` (obligatorio, seguro, rápido, valor, expresión regular, error de expresión regular, confirmar, selección de archivos, tipo de archivo, ruta, nombre), `--textfieldlivevalidation`
- `08_dropdowns.zsh` — `--selecttitle`, `--selectvalues`, `--selectdefault`, modificadores (obligatorios: radio, búsqueda, selección múltiple, nombre), separadores
- `09_checkboxes.zsh` — `--checkbox` (modificador de nombre), `--checkboxstyle` (casilla de verificación, interruptor, tallas).
- `10_list_items.zsh` — `--listitem` (estado, texto de estado, símbolos personalizados de Salesforce), `--liststyle`, `--enablelistselect`, archivo de comandos (lista:, elemento de lista:, añadir, eliminar, índice).
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — Descripción completa del archivo de configuración: título:, tipo de letra del título:, mensaje: (+añadir), alineación:, icono:, icono superpuesto:, transparencia del icono:, texto del botón 1:, botón 1:, texto informativo:, cuadro de información:, icono: centrado/izquierda
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (con indicador de progreso), `--presentation` (con elemento de lista, cuadro de información, indicador de progreso).
- `15_web_video.zsh` — `--webcontent`, `--video` (youtube = acceso directo), `--videocaption`, `--autoplay`
- `16_json_input.zsh`: Arrays JSON para casillas de verificación, elementos de selección, campos de texto e imágenes. `--jsonstring`, `--jsonfile`
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` — `--helpmessage`, `--infotext`, `--infobox`, `--vieworder`, `--quitkey`, `--sound`, `--showsoundcontrols`, `--displaylog`, `--loghistory`, `--debug`, `--eula`, `--alwaysreturninput`, explicación de la clave de autenticación/checksum
- `19_inspect_mode.zsh` — `--inspect-mode`, `--inspect-config`, `--published-sessions-dir`, `stepType: "cadence"`, `cadenceStyle: "carousel"`, cadencia IPC (`cadence:satisfy`, `cadence:advance`, `cadence:goto`), rediseño de la opción predefinida 3, logotipo en el pie de página, forzado `appearance`, `cacheExtensions` con `aria2`
- `20_branched_workflows.zsh` — matriz de nivel superior, `workflow`, `branch.map`, `branch.default`, `branch.ifTrue`, `branch.ifFalse`, `nextpage`, `finalpage`, con capacidad de recordar el historial

## Realización de demostraciones individuales

Cada guion de demostración es independiente.

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## Notas

- Las demostraciones que utilizan `--blurscreen` o `--fullscreen` ocuparán brevemente la pantalla
- Las demostraciones de notificaciones requieren los permisos de notificación para funcionar correctamente con swiftDialog
- Algunas demostraciones de imágenes utilizan imágenes de fondo del sistema, que pueden variar según la versión de macOS
- La versión de demostración 19 ahora se centra en la actualización de la función de inspección v3.1.0b4, que incluye el carrusel de cadencia, el rediseño compacto de la opción predefinida 3, la publicación de sesiones y un ejemplo de archivo JSON para la gestión de preferencias.
- Las versiones 19 y 20 de Demo requieren **swiftDialog v3.1.0b4 o una versión más reciente** para el soporte de flujos de trabajo secuenciales y ramificados.
- Consulte las notas de la versión [swiftDialog v3.1.0b4](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4)] para conocer el conjunto exacto de funciones que se describen aquí.