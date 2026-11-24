---
title: Ritmo controlado en una implementación de MDM
description: Utilizando el tipo de paso "gated-cadence", se crea una pantalla de despliegue controlada por atributos que avanza en función del estado real del sistema, siendo adecuada para implementaciones de MDM con herramientas como Fleet, Jamf, Intune, entre otras.
translationSynced: 2026-11-24T22:53:12+00:00
---

El sistema de pasos secuenciados con control de acceso transforma una pantalla de despliegue en una secuencia **basada en atributos**: cada mensaje se muestra hasta que se cumple una **condición real**, momento en el que avanza. Las condiciones se leen del estado real del sistema, por lo que la pantalla nunca indica que ha finalizado antes de que realmente lo haya hecho.

Esto es **independiente de cualquier solución MDM**. Las señales que lee, como las aplicaciones instaladas, los recibos de paquetes y las **preferencias gestionadas a través de mobileconfig bajo `/Library/Managed Preferences/`**, se generan de la misma manera por **Fleet, Jamf, Intune, Mosyle, Kandji, Munki, Installomator** y otros. Los ejemplos que se muestran a continuación utilizan **Fleet** como caso de estudio, pero nada es específico de Fleet.

## Cómo se adapta a un plan de implementación

El sistema MDM realiza las tareas (instala software, configura perfiles); swiftDialog lo **monitorea**.

| Tarea de implementación | Atributo de cadencia | Lo que dice |
|---|---|---|
| Aplicación instalada | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| Paquete instalado | `file` | recibo en `/var/db/receipts/<pkgid>.bom` |
| **Se han implementado las funcionalidades de perfil y de configuración móvil.** | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (dispositivo) o `…/<user>/<domain>.plist` |
| Configuración basada en scripts | `file` | un archivo de marcador que el script modifica |
| Verificación no observable | `source:"ipc"` | Un script de MDM llama a `cadence:satisfy:<id>` (osquery, registro de Installomator, API de MDM). |

**Sistema híbrido:** la mayoría de las entradas se recopilan directamente (sin necesidad de un orquestador, funciona sin conexión o en la ventana de inicio de sesión); algunas `source:"ipc"` entradas se gestionan mediante un script de MDM para tareas que no se pueden supervisar directamente. El verbo IPC es `cadence:satisfy:<id>` (también `advance` / `goto`).

`timeout` Si una tarea nunca se completa, el sistema avanza automáticamente a la siguiente fase, de modo que una política fallida no puede bloquear la interfaz de usuario.

## Dos fases

Dado que la fase de la ventana de inicio de sesión/asistente de configuración **no tiene una sesión de usuario** (no incluye aplicaciones de usuario, solo preferencias gestionadas a nivel de dispositivo), se utilizan dos configuraciones, seleccionadas por el lanzador en función de la sesión.

### Fase A: Ventana de inicio de sesión / Asistente de configuración (solo a nivel de dispositivo).
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### Fase B: Escritorio después de la autenticación (señales completas).
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
La `compliance` entrada es `source:"ipc"`: un script de MDM realiza la verificación (a través de osquery o una API del proveedor) y luego `… ipc send "cadence:satisfy:compliance"`.

## La implementación (ejemplo de Fleet: la misma estructura se aplica a cualquier solución de gestión de dispositivos móviles).
1. **Paquete:** swiftDialog, el lanzador y ambos archivos JSON de Cadence.
2. **Perfil (mobileconfig):** Configuración del lanzador: qué configuración se aplica por sesión y qué opciones se utilizan en la ventana de inicio de sesión.
   (El lanzador también lee sus propias preferencias gestionadas de la misma manera: bajo `/Library/Managed Preferences/`.)
3. **LaunchAgents** (dispositivo + ventana de inicio de sesión) para iniciar swiftDialog en la sesión correcta.
4. **GitOps / políticas:** Los perfiles y el software que los "gates" de Cadence controlan, junto con el pequeño script que...
   emite `cadence:satisfy` para cualquier `source:"ipc"` registro.

Genere los archivos de configuración para dispositivos móviles (mobileconfig) y los artefactos de GitOps utilizando las herramientas `contour` `fleet-gitops`, que validan el perfil según el esquema de Apple.

## Identidad de marca y mensajes personalizados para cada inquilino, basados en preferencias gestionadas

Para implementaciones en entornos multi-inquilino, la información sobre la frecuencia de los ciclos y el color de la marca puede leerse desde una configuración gestionada en lugar de estar codificada de forma rígida. Esto permite que cada perfil MDM de cada inquilino proporcione sus propios valores sin modificar la configuración predeterminada. Ambos utilizan un `ManagedValueRef`:

| Clave | Tipo | Descripción |
|---|---|---|
| `domain` | Cadena | Dominio de preferencias gestionadas, por ejemplo: `nl.root3.support` |
| `key` | Cadena | Un parámetro clave dentro de ese dominio es el valor de brillo asignado a los colores. |
| `darkKey` | Cadena | Tecla opcional para activar el modo oscuro (solo colores). |

- `cadenceRef` — Lee la matriz de reclamaciones de cadencia (los `CadenceEntry` diccionarios) desde una configuración de preferencias gestionada, en lugar de una `cadence` matriz incrustada.
- `brandColorRef` — Lee el color de la marca/tono (claro, con opción de oscuro) a partir de una preferencia gestionada.

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

Dado que los valores se derivan de `/Library/Managed Preferences/<domain>.plist`, adoptan el mismo comportamiento que los atributos `managedpref` mencionados anteriormente, es decir, "se actualizan en el instante en que se carga el perfil".

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## Notas
- `managedpref` Lee el archivo directamente, por lo que avanza en el instante en que se carga el perfil (no...
  CFPreferences: Retraso en la actualización de la caché. `evaluation:"exists"` = "el perfil está presente"; `equals`/`boolean` = "se aplica un valor específico".
- En la fase de la ventana de inicio de sesión, solo existe el ámbito del dispositivo; las preferencias gestionadas a nivel de usuario y las `app` verificaciones
  Debe incluirse en la Fase B.
- Volviendo a una cadencia completada (Atrás), las **reproducciones rápidas** se inician `cadenceMinDwell` y se detienen
  No volver a cerrar la puerta con la cadena ni poner el candado.
