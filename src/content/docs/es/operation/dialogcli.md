---
title: Lanzador de la interfaz de línea de comandos de Dialog
description: Cómo funciona el ejecutable de línea de comandos de Dialog y las opciones disponibles a nivel de utilidad
translationSynced: 2026-11-24T23:00:40+00:00
---

El comando `dialog` disponible en `/usr/local/bin/dialog` no es la propia aplicación Dialog; es un lanzador de línea de comandos (CLI) ligero (`dialogcli`) que encapsula el archivo ejecutable de Dialog.app. Comprender su funcionamiento es útil al implementar o crear scripts con swiftDialog.

---

## ¿Qué función cumple el lanzador?

Cuando ejecutas `dialog`, el lanzador:

1. Localiza el archivo ejecutable de Dialog.app en relación con la ruta de su propio directorio dentro del paquete de la aplicación.
2. Crea el archivo de comandos en `/var/tmp/dialog.log` (o en la ruta especificada con `--commandfile`) si aún no existe. Si la ruta es un enlace simbólico, el programa de inicio se detiene para evitar riesgos de seguridad.
3. Identifica al usuario de la interfaz gráfica de usuario (GUI) actual, utilizando `SCDynamicStoreCopyConsoleUser`. Si no hay ningún usuario de la interfaz gráfica de usuario activo y `--loginwindow` no está especificado, el lanzador se cierra con el código `1`.
4. **Ejecuta el diálogo en el contexto de usuario correcto.** Cuando se invoca como usuario root (por ejemplo, desde una política de Jamf o un LaunchDaemon), el lanzador utiliza `launchctl asuser` para ejecutar el diálogo como el usuario de la interfaz gráfica que ha iniciado sesión, de modo que la ventana se muestra en la sesión de pantalla correcta.
5. **Se transfiere automáticamente** — el PID propio del lanzador se inyecta como `--pid`, de modo que Dialog puede supervisar el proceso que lo inició y cerrarse si este finaliza. `--pid <pid>`
6. **Notificaciones con estilos específicos para rutas** — cuando se utilizan tanto `--notification` como `--style alert` o `--style banner`, el lanzador redirige la llamada a la aplicación auxiliar de notificaciones integrada correspondiente, en lugar de al programa principal de Dialog.

---

## Creación del enlace simbólico

El programa de instalación incluye una `--link` opción que crea un `/usr/local/bin/dialog` enlace simbólico que apunta a sí mismo. Esto debe ejecutarse como usuario root:

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

Normalmente, esto se gestiona automáticamente mediante el paquete de instalación de swiftDialog.

---

## Opciones de utilidad

Estas opciones son gestionadas directamente por el programa Dialog y son principalmente útiles para tareas de administración o para scripts de despliegue.

### `--setappicon <file>`

Establece el icono de la aplicación swiftDialog en el archivo de imagen especificado y luego se cierra inmediatamente. Esto también actualiza los iconos de cualquier aplicación auxiliar de notificaciones integrada.

```sh
dialog --setappicon /path/to/custom-icon.png
```

Esta es una operación única: Dialog no mostrará ninguna ventana. Está diseñada para la personalización posterior a la instalación, de modo que el icono del Dock y las notificaciones se ajusten a la imagen corporativa de su organización.

### `--callingpid <int>`

Monitorea el identificador de proceso especificado. Si ese proceso finaliza, Dialog se cierra automáticamente con el código `40`.

```sh
dialog --title "Installing..." --callingpid 12345
```

Esto se inyecta automáticamente por el `dialogcli` lanzador (utilizando su propio PID), por lo que Dialog se cerrará si el script o proceso que lo llama es finalizado. Se podría proporcionar un PID diferente de forma explícita, lo que vincularía Dialog a un proceso distinto, sin embargo, este caso de uso no está soportado.

El código de salida **40** se devuelve cuando Dialog se cierra debido a que el proceso supervisado ha finalizado.
