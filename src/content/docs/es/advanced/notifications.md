---
title: Notificaciones
description: Enviar notificaciones del sistema utilizando swiftDialog en lugar de mostrar ventanas de diálogo
translationSynced: 2026-11-24T22:41:25+00:00
---

## Notificaciones

swiftDialog le permite enviar notificaciones utilizando el argumento `--notification`. Esto indica que swiftDialog debe enviar una notificación en lugar de mostrar una ventana de diálogo.

Las notificaciones utilizan los mismos argumentos `--title`, `--message` y `--icon` para mostrar texto y contenido multimedia. Cualquier otro argumento que no se liste en esta página será ignorado.

Existe un argumento adicional `--subtitle` que permite añadir un subtítulo a la notificación.

### Estilos de notificación (versión 3.1 y posteriores).

A partir de la versión 3.1, swiftDialog enruta las notificaciones a través de aplicaciones auxiliares específicas integradas dentro de `Dialog.app`. Utilice el argumento `--style` para seleccionar el tipo de notificación:

| `--style` valor | Comportamiento | Herramienta utilizada |
|---|---|---|
| `banner` | Notificación del sistema que aparece brevemente y se desaparece automáticamente | `Dialog Banner` |
| `alert` | Notificación del sistema que permanece visible hasta que el usuario la elimina | `Dialog Alert` |
| `pseudo` | Banner de notificación simulado (igual que `pseudo-banner`). | Aplicación principal |
| `pseudo-banner` | Una notificación simulada que se cierra automáticamente después de un período de tiempo determinado | Aplicación principal |
| `pseudo-alert` | Notificación simulada que permanece visible hasta que el usuario interactúa con ella | Aplicación principal |

El valor predeterminado cuando `--style` se omite depende de la configuración de las notificaciones del sistema que se hayan configurado para la aplicación.

> #### Ruta de compatibilidad (obsoleta en la versión 3.1).
>
> Llamar `--notification` **sin** `--style` sigue funcionando para mantener la compatibilidad con versiones anteriores, pero la llamada se enruta a través del paquete principal `Dialog.app`. Esta ruta está obsoleta y generará una advertencia en la salida de error estándar:
> En una futura versión, el envío de una notificación sin [`--style`] se realizará por defecto de la siguiente manera: [`--style banner`].

Para garantizar que los tipos de estilo se configuren correctamente para las notificaciones del sistema, implemente un archivo de configuración móvil (mobileconfig) que preapruebe las notificaciones para las aplicaciones auxiliares relevantes (`au.csiro.dialog.notifier.banner` y `au.csiro.dialog.notifier.alert`) con el estilo de notificación deseado.

### Usar

Enviar una notificación básica en formato de banner:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

Enviar una notificación de alerta persistente:

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![image](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

Si el mensaje es más largo de lo que la notificación puede mostrar, el mensaje se truncará y se mostrarán puntos suspensivos `...` para indicar esto. También debería aparecer una flecha en la esquina superior derecha de la notificación cuando el usuario pasa el cursor sobre ella, lo que permite al usuario expandir el contenido

![Captura de pantalla del 13 de noviembre de 2022 a las 5:26 p. m.](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![Captura de pantalla del 13 de noviembre de 2022 a las 5:26 p. m.](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

Añadir un subtítulo:

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![image](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

Un mensaje, incluyendo el título y el subtítulo, puede tener hasta 5 líneas de texto. Un carácter `\n` dentro del cuerpo del mensaje creará un salto de línea en la notificación.

Se puede añadir una imagen utilizando `--icon`, y esta acepta todos los formatos y fuentes de imagen existentes.

![image](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

Cuando se muestra una imagen, el usuario puede ampliar el contenido de la notificación

![image](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

_Nota: No es posible reemplazar el icono predeterminado que se muestra en la notificación. Las imágenes añadidas utilizando `--icon` aparecerán dentro de la notificación._

## Establecer una acción

Puede configurar una acción que se ejecute cuando el usuario hace clic en la notificación. Esta acción puede ser una dirección URL o un comando del sistema.

_NOTA: Las notificaciones son iniciadas por el usuario, y por lo tanto, las acciones que se realizan a través de la notificación se ejecutan en el contexto del usuario._

El uso principal de esta función es:

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

Puede especificar una acción adicional y definir las etiquetas de los botones.

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` es la acción predeterminada que se ejecuta cuando se hace clic en el cuerpo de la notificación o en el botón 1. `--button2action` solo se activa cuando se hace clic en el botón 2.

## Identificadores de notificaciones y eliminación

Puede asignar un identificador persistente a una notificación utilizando `--identifier`. Esto le permite eliminar una notificación específica más adelante:

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

Llamar a `--remove` sin `--identifier` elimina todas las notificaciones pendientes de ese componente.

Los identificadores también funcionan con notificaciones simuladas (véase la sección siguiente).

## Habilitar los sonidos de notificación

Utilice `--enablenotificationsounds` para reproducir el sonido de notificación predeterminado cuando se entrega la notificación:

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## Notificaciones simuladas

Las notificaciones personalizadas son ventanas con el estilo de las notificaciones creadas directamente por swiftDialog, en lugar de ser las notificaciones del sistema macOS. Aparecen deslizándose desde el borde derecho de la pantalla y emulan la apariencia de las notificaciones nativas, con un fondo translúcido.

### ¿Por qué utilizar notificaciones falsas?

- **Soporte para iconos personalizados** — El icono que se muestra en la notificación es totalmente personalizable mediante `--icon`, incluyendo símbolos SF, URLs, rutas de archivos y paquetes de aplicaciones. A diferencia de las notificaciones del sistema, esto no requiere establecer el icono del paquete de Dialog.app ni reiniciar NotificationCenter.
- **No se requiere un perfil MDM** — Las notificaciones simuladas no se muestran en el centro de notificaciones de macOS, por lo que no es necesario configurar ni permisos de "mobileconfig" ni de notificaciones.
- **Imágenes incrustadas:** Utilice `--image` para mostrar una imagen dentro del cuerpo de la notificación.
- **Formato Markdown en línea** — El `--message` contenido admite el formato Markdown en línea.

### ¿Qué no son las notificaciones falsas?

Las notificaciones "falsas" no son notificaciones del sistema. No permanecen visibles una vez que se descartan y no siguen las normas estándar para las notificaciones del sistema de macOS. Tampoco se apilan. Se pueden enviar múltiples notificaciones "falsas", pero aparecerán una encima de la otra hasta que se descarten. Si esto es importante para usted, utilice las notificaciones del sistema estándar.



### Estilos de notificación simulados

| `--style` valor | Comportamiento |
|---|---|
| `pseudo` | Igual que `pseudo-banner` |
| `pseudo-banner` | Se cierra automáticamente después de 6 segundos (o del valor de `--timer`). |
| `pseudo-alert` | Permanece en la pantalla hasta que el usuario haga clic o la cierre |

### Uso básico

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### Icono e imagen personalizados

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### Botones de acción

Cuando se especifica `--button2text` o `--button2action`, aparece una barra de acciones en la parte inferior de la notificación, con dos botones:

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- Hacer clic en el cuerpo de la notificación o en el **Botón 1** ejecuta `--button1action`.
- Hacer clic en el **Botón 2** ejecuta `--button2action`.
- Si ni `--button2text` ni `--button2action` se especifican, la barra de acciones se oculta y hacer clic en cualquier parte de la notificación activa `--button1action`.

### Temporizador de autocierre

Para el estilo `pseudo-banner`, la notificación se cierra automáticamente después de 6 segundos por defecto. Utilice `--timer` para establecer una duración personalizada en segundos:

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### Botón de cerrar

<img width="400" alt="image" src="/images/restart-hover-button.png" />

Cuando el usuario pasa el cursor sobre una notificación simulada, aparece un botón de cierre (×) en la esquina superior izquierda. Al hacer clic en él, la notificación desaparece, comportándose de la misma manera que si se hubiera alcanzado el tiempo de espera (se desliza hacia afuera, se cierra con el código 0, y no se ejecuta ninguna acción del botón).

### Marca de tiempo en tiempo real

Las notificaciones falsas muestran una marca de tiempo que indica "ahora" junto al título. Después de 60 segundos, esta marca de tiempo se actualiza a "hace 1 minuto" y continúa actualizándose cada 60 segundos mientras la notificación permanece visible.

### Identificadores y eliminación

Las notificaciones simuladas ofrecen soporte `--identifier` para la eliminación selectiva:

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

Cuando se envía una nueva notificación "pseudo" con el mismo identificador que una notificación existente, la notificación antigua se elimina automáticamente antes de que aparezca la nueva.

### Sonidos de notificación

Utilice `--enablenotificationsounds` para reproducir el sonido de alerta del sistema cuando aparezca la notificación simulada:

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## Aprobación y configuración del tipo de notificación a través de MDM

La primera vez que utilice las notificaciones, es posible que no reciba ninguna respuesta ni se le solicite que las active.

Para permitir manualmente las notificaciones, deberá acceder a la configuración del sistema -> Notificaciones y activar las notificaciones para la(s) aplicación(es) correspondientes. También puede seleccionar entre los estilos "Ninguno", "Banda" o "Alerta".

Al implementar swiftDialog a través de un sistema de gestión de dispositivos móviles (MDM), es preferible utilizar un archivo de configuración móvil (mobileconfig) que pre-apruebe las notificaciones y defina el tipo de notificación.

### Identificadores de paquetes

| Versión | Identificador de paquete | Notas |
|---|---|---|
| Versiones 2.2.1 y anteriores | `au.bartreardon.dialog` | Legado |
| v2.3 – v3.0 | `au.csiro.dialog` | Paquete de aplicaciones principal |
| Versión 3.1 o superior (estilo de banner). | `au.csiro.dialog.notifier.banner` | `Dialog Banner` ayudante |
| Versión 3.1 o superior (estilo de alerta). | `au.csiro.dialog.notifier.alert` | `Dialog Alert` ayudante |

> Para confirmar los identificadores de paquete exactos de una versión instalada, ejecute el siguiente comando:
> ```bash
> defaults read \"/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist\" CFBundleIdentifier
> lee los valores predeterminados del archivo "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" y extrae el valor de CFBundleIdentifier
> ```

Si tiene una instalación mixta, puede incluir múltiples entradas de paquete en el mismo perfil. Un ejemplo de carga útil para notificaciones con estilo de banner podría ser el siguiente:

```xml
<key>PayloadContent</key>
<array>
    <dict>
        <key>PayloadDisplayName</key>
        <string>Notifications Payload</string>
        <key>PayloadIdentifier</key>
        <string>449B1259-E631-4051-ADCE-9532B813ADDC</string>
        <key>PayloadOrganization</key>
        <string>Org Name</string>
        <key>PayloadType</key>
        <string>com.apple.notificationsettings</string>
        <key>PayloadUUID</key>
        <string>12EA8FDA-B204-4AD0-802C-C980615F0BA5</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>NotificationSettings</key>
        <array>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.bartreardon.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.banner</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>2</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.alert</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
        </array>
    </dict>
</array>
```

Tenga en cuenta que la opción `AlertType` controla el estilo de la notificación de forma independiente de la opción `--style`:
- `1` = Anuncio (se cierra automáticamente).
- `2` = Alerta (permanece visible hasta que se desactive).

Al implementar con `--style alert`, establezca `AlertType` en `2` en la entrada `au.csiro.dialog.notifier.alert`, y viceversa para los banners.

 > #### Una nota sobre los errores de notificación
 >
 > Si recibe lo siguiente:
 >
 > ```
 > Las notificaciones no están disponibles: No se pudo establecer comunicación con una aplicación auxiliar
 > ```
 >
 > Verifique que la aplicación de Dialog correspondiente tenga las notificaciones habilitadas en la configuración del sistema, ya sea aplicando uno de los archivos de configuración móviles (mobileconfig) mencionados anteriormente a través de un sistema de gestión de dispositivos móviles (MDM) o manualmente en la configuración del sistema.

## Actualizar el icono de notificación predeterminado

Las notificaciones utilizarán el icono predeterminado de swiftDialog. Si desea personalizar la aplicación utilizando un icono diferente, por ejemplo, uno que represente la identidad corporativa, puede seguir los siguientes pasos para actualizar el icono del paquete de la aplicación y utilizar uno más adecuado para su uso.

> #### Compatibilidad con macOS desde la versión 26.4
>
> En macOS 26.4, la actualización del icono del paquete de la aplicación y, por lo tanto, del icono de notificación, ya no funciona correctamente. Si la imagen de marca es importante, utilice la nueva función de "notificaciones simuladas", que presenta una interfaz de usuario similar a las notificaciones del sistema, pero no utiliza el sistema de notificaciones de macOS, por lo que puede no ser adecuada para todas las situaciones.

### Requisitos previos

 - Última versión del paquete swiftDialog
 - Se requiere una imagen de reemplazo con una resolución adecuada, de al menos 512x512 píxeles (se prefiere una resolución de 1024x1024 píxeles).

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### Generación de una imagen

   Puede generar una imagen desde la aplicación de autoservicio de sus proveedores de MDM utilizando el comando `sips`. Por ejemplo:

    ##### Kandji

    ```bash
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sips -s format png /Applications/Kandji\ Self\ Service.app/Contents/Resources/AppIcon.icns --out /Library/Application\ Support/Dialog/Dialog.png
    ```

    ##### Jamf

    ```bash
    temp_file=$(/usr/bin/mktemp)
    /usr/bin/xxd -p -s 260 "$(defaults read /Library/Preferences/com.jamfsoftware.jamf self_service_app_path)"/Icon$'\r'/..namedfork/rsrc | /usr/bin/xxd -r -p > "$temp_file"
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sudo /usr/bin/sips -s format png "$temp_file" --out /Library/Application\ Support/Dialog/Dialog.png
    ```

### Pasos

  1. Copie la imagen del icono de reemplazo a `/Library/Application Support/Dialog/Dialog.png` (sensible a mayúsculas y minúsculas).
  2. Instale swiftDialog utilizando el `.pkg` instalador.

Una vez que el reemplazo `Dialog.png` esté instalado, el programa sustituirá el icono predeterminado por la imagen especificada. A partir de ese momento, las notificaciones utilizarán esta imagen personalizada como icono.

 ![Captura de pantalla del 14 de noviembre de 2022 a las 9:55 AM](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
