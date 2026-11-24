---
title: Modo de inspección
description: "Guía de inicio para el modo \"Inspeccionar\" de swiftDialog: monitoreo de instalaciones y cumplimiento de los requisitos del sistema"
translationSynced: 2026-11-24T22:50:45+00:00
---


# Modo de inspección de swiftDialog

El modo de inspección de SwiftDialog es una nueva función integrada que permite la monitorización en tiempo real dentro del sistema de archivos de macOS. Realiza un seguimiento del estado del sistema de archivos (utilizando la API FSEvents de Apple) mientras monitoriza la instalación de aplicaciones y examina carpetas, archivos y el contenido de archivos plist para visualizar las comprobaciones de cumplimiento. Esta función está diseñada específicamente para su uso durante el proceso de registro de dispositivos, la implementación de software y las auditorías de cumplimiento, proporcionando a los usuarios finales una visibilidad clara de su estado de cumplimiento.

## Descripción general

El modo de inspección monitoriza continuamente las rutas de archivo y los directorios de caché especificados para rastrear el estado de las aplicaciones o los componentes del sistema. Proporciona retroalimentación visual a través de varios diseños predefinidos, cada uno adaptado a diferentes casos de uso.


### Características principales
- Monitoreo en tiempo real del sistema de archivos
- Detección del progreso de la descarga mediante el monitoreo de la caché
- Múltiples configuraciones visuales predefinidas para diferentes situaciones
- Validación sencilla basada en listas (booleano, cadena de texto y existencia).
- Personalización de la apariencia y la marca (limitada).
- Botones que se activan automáticamente al completarse la tarea

## Comenzando

### Uso básico

1. Cree un archivo de configuración en formato JSON:
```json
{
  "title": "Application Installation",
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}

```
:::tip[order of items]
Importante: el valor de "guiIndex" debe ser único y determina el orden de los elementos en la interfaz gráfica. Los números más bajos se muestran primero.
:::

2. Inicie swiftDialog con la opción de inspección:
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. Opcionalmente, puede establecer la variable de entorno que indica la ruta al archivo de configuración:
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## Referencia de configuración JSON

### Opciones generales de diálogo

El modo de inspección admite un nuevo `options` objeto en la configuración JSON para controlar el comportamiento general del diálogo. Esto le permite establecer las propiedades de la ventana directamente en la configuración de inspección, sin necesidad de pasar argumentos a la línea de comandos.

```json
{
  "options": {
    "moveable": true,
    "ontop": true,
    "resizable": true,
    "windowbuttons": "min,max,close"
  }
}
```

**Opciones disponibles:**
- `moveable` (booleano) - Permite arrastrar la ventana
- `ontop` (booleano) - Mantener la ventana visible por encima de todas las demás ventanas
- `resizable` (booleano) - Permitir que la ventana se redimensione (implica `moveable`).
- `windowbuttons` (cadena de texto) - Habilitar botones de la ventana: `close`, `min`, `max` (separados por comas).

**Prioridad:** Los argumentos de línea de comandos tienen prioridad sobre las opciones definidas en formato JSON.

**Opciones no admitidas:** Cualquier opción que no esté incluida en la lista de opciones permitidas será ignorada y se registrará un mensaje en el registro de eventos.

**Ejemplo:**
```json
{
  "title": "Application Installation",
  "options": {
    "moveable": true,
    "ontop": true
  },
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}
```

### Claves de nivel raíz

| Clave | Tipo | Requerido | Predeterminado | Descripción |
|-----|------|----------|---------|-------------|
| `preset` | Cadena | No | "predeterminado1" | Diseño visual predefinido (predeterminado 1-7). |
| `title` | Cadena | No | "Inspección del sistema" | Título de la ventana |
| `message` | Cadena | No | - | Texto principal del mensaje |
| `icon` | Cadena | No | - | Ruta del icono o símbolo de SF (por ejemplo, "sf=escudo.relleno"). |
| `size` | Cadena | No | "estándar" | Tamaño de la ventana: "compacto", "estándar", "grande" |
| `width` | Entero | No | - | Ancho de ventana personalizado (anula el tamaño predefinido). |
| `height` | Entero | No | - | Altura de la ventana personalizada (anula el tamaño predefinido). |
| `cachePaths` | Array | No | - | Directorios a monitorizar para las descargas |
| `scanInterval` | Entero | No | 2 | Intervalo de escaneo del sistema de archivos en segundos |
| `button1text` | Cadena | No | "De acuerdo" | Texto del botón principal |
| `button1disabled` | Booleano | No | falso | Deshabilitar el botón principal inicialmente |
| `button2text` | Cadena | No | "Cancelar" | Texto del botón secundario |
| `button2visible` | Booleano | No | cierto | Mostrar botón secundario |
| `autoEnableButton` | Booleano | No | cierto | Botón de activación automática al finalizar |
| `autoEnableButtonText` | Cadena | No | "De acuerdo" | Texto del botón cuando la función está habilitada automáticamente |
| `items` | Array | Sí | - | Conjunto de elementos a inspeccionar |

### Claves de personalización visual

| Clave | Tipo | Predeterminado | Descripción |
|-----|------|---------|-------------|
| `banner` | Cadena | - | Ruta de la imagen del banner (sustituye al icono). |
| `bannerHeight` | Entero | 100 | Altura del banner en píxeles |
| `bannerTitle` | Cadena | - | Superposición del título en el banner |
| `highlightColor` | Cadena | "#808080" | Color de acento (código hexadecimal). |
| `backgroundColor` | Cadena | - | Color de fondo (código hexadecimal). |
| `backgroundImage` | Cadena | - | Ruta de la imagen de fondo |
| `backgroundOpacity` | Doble | 1.0 | Opacidad de fondo (0-1). |
| `textOverlayColor` | Cadena | - | Color del texto superpuesto para los fondos |
| `gradientColors` | Array | - | Conjunto de códigos de color hexadecimal para un degradado |
| `iconBasePath` | Cadena | - | Ruta base para las rutas relativas de los iconos |
| `appearance` | Cadena | "automóvil" | Forzar la aparición de la ventana de inspección: `"dark"`, `"light"` o `"auto"` (seguir las indicaciones del sistema operativo). Anula la configuración del sistema operativo en ambos sentidos. |

### Configuración de elementos

Cada elemento del `items` arreglo requiere:

| Clave | Tipo | Requerido | Descripción |
|-----|------|----------|-------------|
| `id` | Cadena | Sí | Identificador único |
| `displayName` | Cadena | Sí | Nombre de visualización en la interfaz de usuario |
| `guiIndex` | Entero | Sí | Orden de clasificación (basado en cero). |
| `paths` | Array | Sí | Rutas de archivo a verificar para comprobar si existen |
| `icon` | Cadena | No | Icono específico del artículo |
| `plistKey` | Cadena | No | Clave de Plist para validar |
| `expectedValue` | Cadena | No | Valor esperado en el archivo plist |
| `evaluation` | Cadena | No | Tipo de evaluación: "igual", "booleano", "existe", "contiene", "rango" |
| `description` | Cadena | No | Descripción opcional que se muestra debajo del título del artículo (renderizada mediante las opciones de configuración 1, 2, 3, 5 y 6). |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | Cadena de texto | No | Agrupación por categoría (predeterminado5) |
| `categoryIcon` | Cadena | No | Icono de categoría (predeterminado5). | -->


## Características avanzadas

### Monitoreo de caché

Supervisar los directorios de descarga para detectar instalaciones que se estén realizando.

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5,
  "cacheExtensions": ["download", "pkg", "dmg", "aria2"]
}
```

Por defecto, los archivos que terminan con `.pkg`, `.dmg` y `.download` dentro de `cachePaths` marcan el elemento correspondiente como "*descargando*". Configure `cacheExtensions` para modificar esta lista; por ejemplo, agregue `aria2` para que se detecten los archivos parciales de `<name>.aria2` de aria2c (problema #617). El punto al principio es opcional.

### Validación del cumplimiento de las políticas de seguridad (Plist)

Validar la configuración del sistema mediante comprobaciones de archivos plist:

```json
{
  "preset": "preset5",
  "items": [{
    "id": "findmymac",
    "displayName": "Find My Mac Status",
    "guiIndex": 0,
    "paths": ["/Library/Preferences/com.apple.FindMyMac.plist"],
    "plistKey": "FMMEnabled",
    "expectedValue": "true",
    "evaluation": "boolean"
  }]
}
```

### Umbrales de color personalizados

Defina los niveles de conformidad personalizados y sus colores correspondientes.

```json
{
  "colorThresholds": {
    "excellent": 0.95,
    "good": 0.80,
    "warning": 0.60,
    "excellentColor": "#00C853",
    "goodColor": "#2196F3",
    "warningColor": "#FF9800",
    "criticalColor": "#F44336"
  }
}
```


### Paneles de control de cumplimiento

Para la generación de informes de conformidad basados en archivos plist, se debe agregar un arreglo de nivel superior `plistSources`. swiftDialog agrupa los archivos plist referenciados en categorías, indicando el número de elementos aprobados y el total, y calcula una puntuación general. Luego, muestra esta información a través de los bloques de contenido `compliance-summary` y `findings-list` (y cualquier celda de tipo "bento"), actualizándose a intervalos regulares.

```json
{
  "plistSources": [
    {
      "path": "/Library/Preferences/com.company.compliance.plist",
      "type": "compliance",
      "healthyLabel": "Compliant",
      "attentionLabel": "Action Required"
    }
  ],
  "guidance": [
    { "type": "compliance-summary" },
    { "type": "findings-list" }
  ]
}
```

**`plistSources[]` propiedades:**

| Clave | Tipo | Predeterminado | Descripción |
|-----|------|---------|-------------|
| `path` | Cadena | - | Ruta al archivo plist |
| `type` | Cadena | - | Tipo de fuente: `compliance`, `health`, `licenses`, `preferences`, o `custom` |
| `healthyLabel` | Cadena | "Saludable" | Etiqueta para una verificación superada <br> (aparece en las tarjetas de resumen, las filas de resultados y los subtítulos del formato "bento"). |
| `attentionLabel` | Cadena | "Requiere atención" | Etiqueta para un cheque rechazado |
| `successValues` | Array | - | Valores que indican éxito |
| `expectedValue` | Cadena | - | Valor esperado de cumplimiento |
| `findingKey` | Cadena | "encontrar" | Clave secundaria para leer los detalles del resultado |
| `timestampKey` | Cadena | automóvil | Clave que almacena la fecha y hora de la última verificación (intentos automáticos `lastComplianceCheck`, `LastUpdateCheck`, `lastCheck`, `timestamp`). |
| `includePattern` | Cadena | - | Expresión regular de las claves a incluir en el descubrimiento automático |
| `excludeKeys` | Array | - | Claves que se excluirán de la detección automática |
| `keyMappings` | Array | - | Cómo interpretar las claves específicas de un archivo plist |
| `maxCheckDetails` | Entero | 15 | Máximo número de elementos mostrados por categoría |
| `icon` | Cadena | - | Símbolo de SF para la categoría |

Bloques de contenido que muestran los datos agregados

- `compliance-summary` — Un panel que muestra el estado general, junto con tarjetas informativas para cada categoría.
- `findings-list` — Una lista detallada de comprobaciones individuales, organizada por categorías y que puede ser consultada.

Las celdas de Bento también se vinculan automáticamente a los mismos datos: el subtítulo y el color del icono de una celda se actualizan en tiempo real, sin necesidad de campos de esquema adicionales. <br>

## Ejemplos completos

### Instalador básico de aplicaciones

```json
{
  "title": "Installing Office Suite",
  "message": "Please wait while we install your applications",
  "preset": "preset1",
  "icon": "sf=apps.iphone.badge.plus",
  "iconBasePath":"/Users/Shared/icons/",
  "cachePaths": ["/Users/Shared/Downloads"],
  "button1text": "Please Wait...",
  "button1disabled": true,
  "autoEnableButton": true,
  "autoEnableButtonText": "Continue",
  "items": [
    {
      "id": "microsoft_word",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"],
      "icon": "Microsoft Word.png"
    },
    {
      "id": "microsoft_excel",
      "displayName": "Microsoft Excel",
      "guiIndex": 1,
      "paths": ["/Applications/Microsoft Excel.app"],
      "icon": "Microsoft Excel.png"
    },
    {
      "id": "microsoft_powerpoint",
      "displayName": "Microsoft PowerPoint",
      "guiIndex": 2,
      "paths": ["/Applications/Microsoft PowerPoint.app"],
      "icon": "Microsoft PowerPoint.png"
    }
  ]
}
```
:::tip[iconBasePath]
Defina una ruta base para los iconos de los elementos para simplificar la configuración; los nombres de las imágenes se cargan desde `iconBasePath` cuando están disponibles. De lo contrario, especifique la ruta completa para cada elemento.
:::


## Solución de problemas

### Configuración no se está cargando
- Verifique la sintaxis de JSON utilizando `jq` o validadores en línea
- Verifique los permisos del archivo (debe ser legible).
- Asegúrese de que la variable de entorno se exporte correctamente

### Elementos no detectados
- Verificar las rutas de archivo exactas (sensibles a mayúsculas y minúsculas).
- Verificar si las rutas requieren privilegios de administrador
- Utilice `cachePaths` para la detección de descargas
- Aumente `scanInterval` para sistemas más lentos

### Modo de depuración
Activar la salida de depuración:
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### Variables de entorno comunes
- `DIALOG_INSPECT_CONFIG`: Ruta al archivo de configuración JSON
- `DIALOG_DEBUG`: Activar el registro de depuración
- `DIALOG_COMMAND_FILE`: Ruta del archivo de comandos personalizado

## Mejores prácticas

1. **Comience de forma sencilla:** Empiece con la configuración predeterminada 1 y una configuración mínima
2. **Rutas de prueba:** Verificar que todas las rutas de archivo existen o existirán
3. **Utilice el monitoreo de caché**: Añada `cachePaths` para la detección de descargas
4. **Gestión de iconos**: Almacene los iconos en una ubicación centralizada con `iconBasePath`
5. **Estados de los botones**: Utilice `autoEnableButton` para mejorar la experiencia del usuario
6. **Preajustes adecuados**: Seleccione los preajustes según el uso previsto:
   - Seguimiento de la instalación: Presintonía 1 o 2 o 3
   - Pantalla de conformidad: Presintonía 4


