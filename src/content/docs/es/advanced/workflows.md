---
title: Flujo de trabajo de swiftDialog
description: Flujos de diálogo con múltiples pasos en swiftDialog
translationSynced: 2026-11-24T22:45:36+00:00
---

> **NOTA:** La función de flujo de trabajo (Workflow) se introdujo en la versión 3.1 de swiftDialog.

# Documentación de la función de flujo de trabajo de swiftDialog

## Descripción general

La función **Flujo de Trabajo** permite crear flujos de diálogo con múltiples pasos en swiftDialog, lo que le permite diseñar interfaces de usuario tipo "asistente" que guían a los usuarios a través de varias pantallas de información y datos. Cada tarjeta representa una pantalla separada con su propia configuración, y los usuarios pueden navegar hacia adelante y hacia atrás dentro del flujo de trabajo.

Los flujos de trabajo se definen mediante archivos de configuración JSON, lo que facilita la creación de diálogos complejos y con múltiples pasos sin necesidad de escribir código.

## Características principales

- **Flujos de trabajo con múltiples pasos:** Divida los diálogos complejos en etapas más sencillas
- **Controles de navegación:** Botones automáticos de "Siguiente", "Anterior" y "Finalizar"
- **Ramificación condicional:** Dirija el flujo de trabajo a diferentes tarjetas según la selección en un menú desplegable o el estado de una casilla de verificación, sin necesidad de un script de retorno
- **Persistencia de datos:** Los datos ingresados por el usuario se conservan al navegar entre las diferentes etapas del flujo de trabajo
- **Configuraciones globales:** Defina ajustes comunes una sola vez y luego modifíquelos individualmente para cada elemento
- **Sustitución de variables**: Utilice la sintaxis `{fieldname}` para referenciar valores de tarjetas de flujo de trabajo anteriores
- **Validación:** Se requiere la validación de los campos obligatorios antes de continuar
- **Configuración dinámica:** Cada tarjeta puede tener elementos de interfaz de usuario y configuraciones únicas
- **Llamadas de retorno:** Ejecute scripts de shell al pasar de una tarjeta a otra en el flujo de trabajo

## Conceptos básicos

### Estructura del flujo de trabajo

Se define un diálogo basado en un flujo de trabajo en un archivo de configuración JSON con la siguiente estructura:

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### Configuración global

Las propiedades definidas a nivel raíz (fuera del `workflow` array) sirven como valores predeterminados para todas las tarjetas de flujo de trabajo. Las tarjetas de flujo de trabajo individuales pueden anular estos valores predeterminados:

```json
{
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertNoteIcon.icns",
  "button1text": "Continue",
  "workflow": [
    { "title": "Step 1", "message": "Uses default icon" },
    { "title": "Step 2", "icon": "SF=checkmark.circle", "message": "Custom icon" }
  ]
}
```

### Identificación de tarjetas

Las tarjetas se ordenan automáticamente según su posición en el arreglo. Opcionalmente, puede especificar un criterio de ordenamiento explícito `id` para personalizar el orden.

```json
{
  "workflow": [
    { "id": 0, "title": "First" },
    { "id": 10, "title": "Second" },
    { "id": 5, "title": "Third (will be displayed second)" }
  ]
}
```

## Navegación

### Comportamiento del botón

En modo de flujo de trabajo, el comportamiento del botón cambia automáticamente:

- **Botón 1** (lado derecho):
  - Muestra el botón "Siguiente" en las tarjetas de flujo de trabajo del 1 al n-1
  - Muestra la palabra "Finalizar" en la última tarjeta (o texto personalizado a través de `button1text`).
  - Valida los campos obligatorios antes de continuar
  
- **Botón 2** (lado izquierdo):
  - Oculto en la primera tarjeta
  - Muestra el botón "Anterior" en las tarjetas de flujo de trabajo desde la número 2 hasta la n
  - No se realiza ninguna validación al retroceder

### Personalización del texto de los botones

Por defecto, los botones de navegación muestran las etiquetas "**Siguiente**", "**Anterior**" y "**Finalizar**". Para modificarlos, haga lo siguiente:

- `--nextbuttontext "<text>"` — Texto para el botón "Siguiente" (valor predeterminado: `Next`).
- `--previousbuttontext "<text>"` — Texto para el botón "Anterior" (valor predeterminado: `Previous`).
- `button1text` (de nivel superior o por cada tarjeta) — texto para el botón final de "**Finalizar**"

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### Flujo de navegación

<img width="650" alt="image" src="/images/navigation-flow.png" />


## Navegación con opciones

Por defecto, las tarjetas de flujo de trabajo se muestran en orden de secuencia. Puede modificar este comportamiento utilizando tres propiedades opcionales que se pueden configurar individualmente para cada tarjeta:

| Propiedad | Tipo | Propósito |
|---|---|---|
| `branch` | objeto | Seleccione la siguiente carta basándose en un valor específico que se encuentre en la carta actual |
| `nextpage` | entero | Sobreescritura estática: vaya a esta tarjeta `id` después de "Siguiente" |
| `finalpage` | booleano | Esta tarjeta finaliza el flujo de trabajo; el siguiente estado se convierte en "Finalizar" |

Cuando el usuario hace clic en "Siguiente", swiftDialog determina el destino en el siguiente orden:

1. `branch` (si está establecido y se encuentra una regla coincidente).
2. `nextpage` (si está activado).
3. La siguiente tarjeta en la secuencia
4. Fin del flujo de trabajo (si no existe la siguiente tarjeta, o si `finalpage` es verdadero).

El botón "Anterior" tiene en cuenta el historial de navegación: regresa a la tarjeta desde la cual el usuario realmente accedió, y no simplemente a la tarjeta con el índice "actual - 1". Esto funciona correctamente en todas las secciones.

> swiftDialog no verifica la presencia de bucles ni tarjetas inaccesibles. Si su flujo de trabajo puede volver sobre sí mismo, el usuario simplemente revisitará esas tarjetas; en ese caso, depure la lógica del flujo de trabajo si esa no es la intención.

### Derivación a partir de un menú desplegable

El valor `branch.field` coincide con el valor del campo `name` (preferido) o con su `title`/`label`. Para un menú desplegable, el valor seleccionado se compara con las claves que se encuentran en `branch.map`:

```json
{
  "workflow": [
    {
      "id": 1,
      "title": "Choose your path",
      "message": "Pick an option to control which card appears next.",
      "selectitems": [
        {
          "name": "userType",
          "title": "Account type",
          "values": ["Admin", "Standard", "Guest"],
          "default": "Standard"
        }
      ],
      "branch": {
        "field": "userType",
        "map": {
          "Admin":    10,
          "Standard": 20,
          "Guest":    30
        },
        "default": 99
      }
    },
    { "id": 10, "title": "Admin setup", "nextpage": 99 },
    { "id": 20, "title": "Standard setup", "nextpage": 99 },
    { "id": 30, "title": "Guest setup", "nextpage": 99 },
    { "id": 99, "title": "Summary", "finalpage": true }
  ]
}
```

`branch.default` es opcional. Si se establece y el valor seleccionado no aparece en `map`, el flujo de trabajo avanza a esa tarjeta de respaldo.

### Ramificación a partir de una casilla de verificación

Para un campo booleano individual, utilice la abreviatura `ifTrue` / `ifFalse` en lugar de `map`:

```json
{
  "id": 5,
  "checkbox": [
    { "name": "wantsExtras", "label": "Show advanced options" }
  ],
  "branch": {
    "field": "wantsExtras",
    "ifTrue":  6,
    "ifFalse": 99
  }
}
```

También puede usar `map` con las opciones `"true"` y `"false"` si lo prefiere, pero `ifTrue`/`ifFalse` es más fácil de entender.

### Sobrescritura `nextpage` estática

Si no necesita enrutamiento dinámico, pero desea una opción para avanzar, configure `nextpage`:

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### Finalizar el flujo de trabajo de forma anticipada

Para detener el flujo de trabajo en una tarjeta específica, marque esa tarjeta como "final".

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

En la última tarjeta, el botón 1 muestra la palabra "Finalizar" y cierra el diálogo cuando se hace clic en él, independientemente de cuántas tarjetas de flujo de trabajo queden en la lista.

## Ejemplos de uso

### Ejemplo 1: Asistente sencillo de tres pasos

```json
{
  "title": "Setup Wizard",
  "icon": "SF=gearshape.2",
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to the setup wizard. Click Continue to begin."
    },
    {
      "title": "Enter Information",
      "message": "Please provide your details:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email Address", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Setup is complete! Click Finish to close this wizard.",
      "button1text": "Finish"
    }
  ]
}
```

Ejecútelo
```bash
dialog --jsonfile /path/to/config.json
```

### Ejemplo 2: Uso de la sustitución de variables

La sustitución de variables le permite referenciar valores de tarjetas de flujo de trabajo anteriores utilizando la sintaxis `{fieldname}`:

```json
{
  "title": "User Registration",
  "workflow": [
    {
      "title": "Personal Information",
      "message": "Step 1: Enter your details",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true }
      ]
    },
    {
      "title": "Confirmation",
      "message": "Hello {First Name} {Last Name}! Please confirm your information is correct.",
      "infobox": "**Name:** {First Name} {Last Name}"
    }
  ]
}
```

Los campos `{First Name}` y `{Last Name}` de la Tarjeta 2 serán reemplazados con los valores que se hayan introducido en la Tarjeta 1.

### Ejemplo 3: Valores predeterminados globales con opciones de personalización

```json
{
  "icon": "SF=info.circle",
  "width": 600,
  "height": 400,
  "workflow": [
    {
      "title": "Introduction",
      "message": "This card uses the default icon and size."
    },
    {
      "title": "Custom Layout",
      "icon": "SF=wrench.and.screwdriver",
      "width": 800,
      "height": 500,
      "message": "This card has a custom icon and larger size."
    },
    {
      "title": "Back to Normal",
      "message": "This card reverts to default icon and size."
    }
  ]
}
```

### Ejemplo 4: Recopilación de datos en múltiples etapas

```json
{
  "title": "System Configuration",
  "icon": "/System/Library/PreferencePanes/Appearance.prefPane/Contents/Resources/AppIcon.icns",
  "workflow": [
    {
      "title": "Network Settings",
      "message": "Configure network preferences:",
      "selectitems": [
        {
          "title": "Network Type",
          "values": ["WiFi", "Ethernet", "VPN"],
          "default": "WiFi"
        }
      ]
    },
    {
      "title": "User Preferences",
      "message": "Set user preferences:",
      "checkbox": [
        { "label": "Enable notifications", "checked": true },
        { "label": "Auto-update", "checked": true },
        { "label": "Send analytics", "checked": false }
      ]
    },
    {
      "title": "Summary",
      "message": "Review your settings:",
      "infobox": "**Network:** {Network Type}\\n\\n**Notifications:** {Enable notifications}\\n**Auto-update:** {Auto-update}\\n**Analytics:** {Send analytics}"
    }
  ]
}
```

### Ejemplo 5: Indicador de progreso con tarjetas

```json
{
  "title": "Installation Wizard",
  "workflow": [
    {
      "title": "Preparing (1 of 3)",
      "message": "Preparing installation...",
      "progress": 100,
      "progresstext": "Checking system requirements"
    },
    {
      "title": "Installing (2 of 3)",
      "message": "Installing software...",
      "progress": 100,
      "progresstext": "Copying files"
    },
    {
      "title": "Complete (3 of 3)",
      "message": "Installation complete!",
      "icon": "SF=checkmark.circle.fill",
      "progress": 100,
      "progresstext": "Finished"
    }
  ]
}
```

### Ejemplo 6: Validación de campos obligatorios

```json
{
  "title": "Registration Form",
  "workflow": [
    {
      "title": "Account Details",
      "message": "All fields marked with * are required",
      "textfield": [
        { "title": "Username", "required": true, "prompt": "Enter username" },
        { "title": "Password", "required": true, "secure": true },
        { "title": "Confirm Password", "required": true, "secure": true }
      ]
    },
    {
      "title": "Contact Information",
      "message": "Please provide at least one contact method",
      "textfield": [
        { "title": "Email", "required": true },
        { "title": "Phone", "required": false }
      ]
    }
  ]
}
```

Si los usuarios intentan hacer clic en "Siguiente" sin completar los campos obligatorios, aparecerá un mensaje de error.

## Características avanzadas

### Propiedades específicas del flujo de trabajo

Cualquier propiedad estándar de swiftDialog puede utilizarse en un flujo de trabajo. Las propiedades más comunes incluyen:

- **Diseño**: `width`, `height`, `position`
- **Contenido**: `title`, `message`, `icon`, `iconsize`
- **Entrada**: `textfield`, `selectitems`, `checkbox`, `radio`
- **Pantalla**: `image`, `video`, `webcontent`, `listitem`
- **Progreso**: `progress`, `progresstext`
- **Información**: `infobox`, `helpmessage`
- **Estilo**: `messagefont`, `alignment`, `bannerimage`
- **Navegación**: `branch`, `nextpage`, `finalpage` (ver [Navegación con opciones⟧ ](#navegación-con-opciones)).

### Nomenclatura de los campos de entrada

Para que la sustitución de variables funcione correctamente, los campos de entrada deben tener nombres consistentes.

```json
{
  "textfield": [
    { "title": "First Name" }  // Referenced as {First Name}
  ],
  "selectitems": [
    { "title": "Department", "values": ["IT", "HR", "Sales"] }  // Referenced as {Department}
  ]
}
```

Si un campo no tiene una especificación explícita `title`, puede utilizar una propiedad `name`:

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### Persistencia de datos

La información ingresada por el usuario se guarda automáticamente cuando:
- Haga clic en "Siguiente" para avanzar a la siguiente tarjeta
- Haga clic en "Anterior" para volver

Cuando los usuarios regresan a una tarjeta anterior, sus datos ingresados se restauran.

### Acceso a los datos de la tarjeta

Cuando el usuario hace clic en "Finalizar" en la última tarjeta, todos los datos recopilados se muestran en la salida estándar (stdout) en formato JSON.

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### Llamadas de retorno sobre pagos anticipados

Utilice la opción `--onadvance` para ejecutar un comando de shell al avanzar entre las tarjetas del flujo de trabajo.

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

El script recibe:
- Índice de tarjetas (basado en cero).
- Identificación de la tarjeta (si se especifica).
- La información de la tarjeta se recibe actualmente en formato JSON a través de la entrada estándar

El script debe finalizar con:
- **Código de salida 0:** Permitir el avance
- **Código de salida no nulo:** Impide el avance y muestra un mensaje de error

Ejemplo de script de devolución de llamada:
```bash
#!/bin/bash
# script.sh - Validate email format before advancing

input=$(cat)
email=$(echo "$input" | jq -r '.["Email Address"]')

if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
    echo "Invalid email address format"
    exit 1
fi

exit 0
```

## Mejores prácticas

### 1. Mantenga los flujos de trabajo enfocados
Cada tarjeta debe tener un único propósito claro. Evite sobrecargar a los usuarios con demasiados campos en una misma tarjeta.

### 2. Utilice títulos descriptivos
Los títulos de las tarjetas deben indicar claramente en qué etapa del proceso se encuentra el usuario:
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. Proporcionar contexto
Utilice el campo de mensaje para explicar al usuario qué debe hacer:
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. Utilice la validación de campos obligatorios
Marque los campos obligatorios para garantizar la integridad de los datos.
```json
{ "title": "Email", "required": true }
```

### 5. Proporcionar tarjetas de resumen
Incluya una tarjeta de resumen final que muestre toda la información recopilada.
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. Tenga en cuenta el flujo de navegación
- No haga que la primera pantalla requiera una gran cantidad de información; facilite la experiencia al usuario
- Coloque la recopilación de los datos más importantes al principio
- Guardar la confirmación/revisión para la tarjeta final

### 7. Utilice un estilo consistente
Defina los valores predeterminados globales para garantizar una apariencia consistente.
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## Limitaciones y notas

1. **Actualizaciones del archivo de comandos:** Al utilizar el modo de flujo de trabajo con un archivo de comandos, es posible que algunas actualizaciones dinámicas no funcionen como se espera. El modo de flujo de trabajo está diseñado para la recopilación de datos de entrada, y no para actualizaciones dinámicas del estado.

2. **Personalización de botones:** El comportamiento de los botones 1 y 2 está controlado por el modo de flujo de trabajo y no se puede personalizar completamente mientras se está en modo de flujo de trabajo.

3. **Códigos de salida:** En el modo de flujo de trabajo, el diálogo solo se cierra cuando:
   - El usuario hace clic en el botón "Finalizar" en la última tarjeta (código de salida 0).
   - El usuario canceló la operación (el código de salida varía).
   - La validación falla y el usuario decide cancelar la operación

4. **Ámbito de las variables:** Las variables de tarjetas de flujo de trabajo anteriores solo están disponibles en tarjetas posteriores, no en las tarjetas de flujo de trabajo anteriores. La sustitución de variables es unidireccional.

5. **Nombres de campos:** Para una correcta sustitución de variables, utilice caracteres alfanuméricos y espacios en los títulos de los campos. Los caracteres especiales pueden causar problemas.

## Solución de problemas

### Las tarjetas no aparecen
- Verifique la sintaxis de JSON con `jsonlint` o una herramienta similar
- Asegúrese de que el `workflow` arreglo se encuentre en el nivel raíz
- Verifique que al menos una tarjeta esté definida

### Variables que no se están sustituyendo
- Asegúrese de que los nombres de los campos coincidan exactamente (sensibles a mayúsculas y minúsculas).
- Verifique que las referencias a variables utilicen llaves: `{fieldname}`
- Verifique que el campo al que se hace referencia estuviera presente en una tarjeta anterior, y no en la tarjeta actual o en una futura

### La validación no funciona
- Verificar que el campo `"required": true` esté configurado correctamente
- Verifique que el campo tenga una propiedad que indique `title` o `name`
- Revisar los registros de depuración con la opción `--debug`

### El botón "Anterior" no se muestra
- Verifique que no se encuentre en la primera tarjeta del flujo de trabajo (el elemento anterior está oculto en la primera tarjeta).
- Verifique que el modo de flujo de trabajo esté realmente habilitado (que exista el arreglo de flujo de trabajo).

### La sucursal emite la tarjeta incorrecta
- Confirme que el valor `branch.field` coincida con el valor del campo `name` (o con su `title`/`label` si no se ha establecido un nombre).
- Para los menús desplegables, las claves se comparan con el valor seleccionado por el usuario de forma exacta, teniendo en cuenta mayúsculas y minúsculas, así como los espacios en blanco
- Para las casillas de verificación, es preferible utilizar las claves de mapeo `ifTrue`/`ifFalse` en lugar de `"true"`/`"false"`
- Verifique el registro de swiftDialog; los objetivos inválidos `nextpage`/`branch` se reportan durante el proceso de carga

## Ejemplo completo: Asistente de incorporación de empleados

```json
{
  "title": "Employee Onboarding",
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns",
  "width": 750,
  "height": 500,
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome to the Company!",
      "message": "## Welcome Aboard!\\n\\nThis wizard will guide you through the onboarding process.\\n\\nClick Continue to get started.",
      "icon": "SF=hands.clap.fill",
      "iconsize": 120
    },
    {
      "title": "Personal Information",
      "message": "Please provide your personal details (all fields required):",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true },
        { "title": "Employee ID", "required": true },
        { "title": "Work Email", "required": true, "prompt": "name@company.com" }
      ]
    },
    {
      "title": "Department Assignment",
      "message": "Select your department and role:",
      "selectitems": [
        {
          "title": "Department",
          "values": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
          "default": "Engineering"
        },
        {
          "title": "Role",
          "values": ["Manager", "Senior", "Mid-level", "Junior"],
          "default": "Mid-level"
        }
      ]
    },
    {
      "title": "System Preferences",
      "message": "Configure your system preferences:",
      "checkbox": [
        { "label": "Enable email notifications", "checked": true },
        { "label": "Join company Slack", "checked": true },
        { "label": "Subscribe to company newsletter", "checked": true },
        { "label": "Opt-in to mentorship program", "checked": false }
      ]
    },
    {
      "title": "Review & Confirm",
      "message": "Please review your information before completing the onboarding process:",
      "icon": "SF=checkmark.circle",
      "infobox": "**Name:** {First Name} {Last Name}\\n**Employee ID:** {Employee ID}\\n**Email:** {Work Email}\\n\\n**Department:** {Department}\\n**Role:** {Role}\\n\\n**Email Notifications:** {Enable email notifications}\\n**Slack:** {Join company Slack}\\n**Newsletter:** {Subscribe to company newsletter}\\n**Mentorship:** {Opt-in to mentorship program}",
      "button1text": "Complete Onboarding"
    }
  ]
}
```

Guarde esto como `onboarding.json` y ejecútelo:
```bash
dialog --jsonfile onboarding.json
```

## Ejemplo de integración: Script de shell

Aquí hay un ejemplo completo de un script de shell que utiliza el modo de flujo de trabajo y procesa la salida:

```bash
#!/bin/bash

# onboarding.sh - Employee onboarding with swiftDialog workflow

DIALOG="/usr/local/bin/dialog"
CONFIG="/tmp/onboarding_config.json"

# Create the JSON configuration
cat > "$CONFIG" << 'EOF'
{
  "title": "Employee Onboarding",
  "icon": "SF=person.crop.circle.badge.checkmark",
  "width": 700,
  "height": 450,
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to Company XYZ! This wizard will set up your account."
    },
    {
      "title": "Enter Details",
      "message": "Please provide your information:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Onboarding complete for {Full Name}!",
      "infobox": "We'll send a confirmation to {Email}"
    }
  ]
}
EOF

# Run dialog and capture output
if output=$("$DIALOG" --jsonfile "$CONFIG" 2>&1); then
    echo "Onboarding completed successfully!"
    echo "Collected data:"
    echo "$output" | jq .
    
    # Extract specific fields
    full_name=$(echo "$output" | jq -r '.["Full Name"]')
    email=$(echo "$output" | jq -r '.Email')
    
    echo "Processing onboarding for $full_name ($email)..."
    
    # Add your custom logic here
    # - Create user account
    # - Send welcome email
    # - Configure systems
    
else
    echo "Onboarding was cancelled or failed"
    exit 1
fi

# Cleanup
rm -f "$CONFIG"
```

## Resumen

La función de flujo de trabajo en swiftDialog ofrece una forma potente de crear interfaces con múltiples pasos, similares a asistentes, utilizando una configuración sencilla en formato JSON. Entre sus principales ventajas se incluyen:

- **Simplificación de flujos de trabajo complejos:** Descomposición de procesos complicados en pasos manejables
- **Navegación integrada:** Botones automáticos de "Siguiente", "Anterior" y "Finalizar"
- **Recopilación de datos:** Permite recopilar y validar fácilmente la información proporcionada por los usuarios en diversas pantallas
- **Configuración flexible:** Utilice valores predeterminados globales y opciones de personalización específicas para cada flujo de trabajo
- **Sustitución de variables:** Permite referenciar los valores de tarjetas de flujo de trabajo anteriores en tarjetas de flujo de trabajo posteriores
- **No se requiere programación** - Defina todo en formato JSON

Para obtener más información sobre las opciones y parámetros individuales de swiftDialog, consulte la documentación principal de swiftDialog o utilice `dialog --help`.
