---
title: Ventana de inicio de sesión
description: Ejecutar cuadros de diálogo swiftDialog en el contexto de la ventana de inicio de sesión de macOS
translationSynced: 2026-11-24T22:58:11+00:00
---

## Soporte para la ventana de inicio de sesión (a partir de la versión 2.5.0).

`--loginwindow`

En swiftDialog 2.5, puede ejecutar cuadros de diálogo en la ventana de inicio de sesión.

Se admiten diálogos estándar, con o sin `--blurscreen`

## Requisitos

Para ejecutarlo en el contexto de la ventana de inicio de sesión, deberá configurar lo siguiente:

 - Un script que inicia swiftDialog con la configuración que desee
   - Incluya el argumento `--loginwindow`
 - Un agente de inicio

### Configuración de LaunchAgent

#### Configuración manual

A continuación, se presenta un ejemplo de un LaunchAgent básico:

```xml
<plist version="1.0">
<dict>
	<key>OnDemand</key>
	<false/>
	<key>LaunchOnlyOnce</key>
	<true/>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/script.sh</string>
	</array>
	<key>LimitLoadToSessionType</key>
	<string>LoginWindow</string>
	<key>Label</key>
	<string>com.swiftDialog.example-login-window</string>
</dict>
</plist>
```

Asigne un nombre adecuado, por ejemplo, `com.swiftDialog.example-login-window.plist`, e instálelo en `/Library/LaunchAgents/`

#### Utilizando Outset

La herramienta de código abierto Macadmins, [Outset](https://github.com/macadmins/outset/), tiene funcionalidades para ejecutar elementos en la ventana de inicio de sesión.

Además de simplificar el proceso, también obtendrá acceso a controles que le permiten evitar que un usuario desactive los elementos de inicio de sesión. Consulte la [wiki de Outset](https://github.com/macadmins/outset/wiki/Deployment#login-items-management)] para obtener más detalles.

Coloque su script en el directorio `/usr/local/outset/login-window/`, con los permisos configurados como `root:root` `0755` (`-rwxr-xr-x`), y outset se encargará de iniciar el script cuando aparezca la ventana de inicio de sesión.

### Consideraciones

Deberá considerar qué sucede después de que el script se haya ejecutado. Si no desea que se ejecute cada vez que se muestra la ventana de inicio de sesión, deberá incluir condiciones en su script para que, ya sea, no realice ninguna acción o se desinstale automáticamente cuando ya no sea necesario.

### Caso de uso de ejemplo

#### Política de uso aceptable de la organización

A continuación, se muestra un ejemplo de un diálogo de política de uso aceptable que requiere que se marque una casilla y que incluye contenido de un archivo Markdown (ejemplo: [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)]) y se muestra utilizando el modo `--eula`. Se mostraría cada vez que se presenta la ventana de inicio de sesión.

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>