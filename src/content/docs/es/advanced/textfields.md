---
title: Campos de texto
description: Crear campos de entrada de texto con diversas propiedades y validaciones
translationSynced: 2026-11-24T22:31:35+00:00
---

La opción `--textfield` permite especificar un área donde el usuario puede ingresar texto antes de cerrar la ventana de diálogo

Toma un parámetro como texto y utiliza ese parámetro como la etiqueta del campo de texto, tanto en la interfaz de diálogo como en la salida de los informes

Los resultados se envían a la salida estándar (stdout) cuando el programa dialog finaliza, y tienen el siguiente formato:

`<textfield text> : <user input>`

o, si se utiliza la opción `--json` para habilitar la salida en formato JSON:

```json
{
"<textfield text>" : "<user input>"
}
```

## Ejemplos

Si utiliza el siguiente diálogo:

`dialog --textfield "Textfield 1"`

Mostrará el siguiente diálogo:

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

El usuario introduce una respuesta:

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

que producirá el siguiente resultado:

`Textfield 1 : This is what the user entered`

o al utilizar `--json`

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## Campos de texto adicionales

Se pueden especificar múltiples campos de texto añadiendo opciones adicionales al llamar a la función `dialog`. `--textfield`

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

Puede especificar tantos campos de texto como necesite. Cada campo de texto se mostrará como un campo separado en el resultado.

Es posible que deba ajustar el tamaño `--height` de su ventana de diálogo si está agregando varios campos de texto para que quepan

Aquí hay un ejemplo:

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

Esto produce el siguiente resultado:

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## Modificadores de campos de texto

Los modificadores se añaden a la etiqueta del campo de texto como valores separados por comas:

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| Modificador | Descripción |
|---|---|
| `name=<text>` | Utilice este valor como la clave de salida en lugar de la etiqueta |
| `required` | El campo debe estar completado antes de que la ventana de diálogo se cierre |
| `secure` | Ocultar lo que se escribe (campo de contraseña). |
| `passwordfill` | Activar la función de autocompletar contraseñas de macOS en un campo `secure` |
| `prompt="<text>"` | Texto de ejemplo que se muestra dentro del campo (no se incluye en el resultado). |
| `value="<text>"` | Pre-llenar el campo con un valor predeterminado (que se puede editar). |
| `regex=<pattern>` | Exigir que el contenido del campo coincida con la expresión regular |
| `regexerror=<text>` | Se muestra un mensaje de error personalizado cuando la expresión regular no se cumple |
| `editor` | Editor de texto de múltiples líneas en lugar de un campo de una sola línea |
| `isdate` | Reemplace el campo de texto con un selector de fecha. La salida se formatea como una cadena de fecha abreviada. |
| `fileselect` | Agregue un botón de "Seleccionar" que abra un explorador de archivos |
| `filetype=<types>` | Restrinja el selector de archivos a los tipos especificados (separados por espacios). Utilice las extensiones de archivo (por ejemplo, `png jpg`) o las palabras clave de tipo `folder`, `image`, `movie`, `video`, `audio`. |
| `path=<path>` | Establezca el directorio inicial para el selector de archivos |
| `confirm` | Agregue un campo de confirmación cuyo contenido debe coincidir con el campo principal |

### Nombre

`name=<text>` Reemplaza la etiqueta como clave en la salida. Es útil cuando se desea una etiqueta amigable, pero un nombre de clave más claro en el resultado.

### Seguro

`secure` Oculta la información que se introduce mientras se escribe y muestra un icono de candado. El contenido sigue devolviéndose como texto plano en la salida estándar.

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### Autocompletar contraseñas

`passwordfill` Permite la función de autocompletar contraseñas en macOS. Debe utilizarse junto con `secure`.

```sh
--textfield "Password,secure,passwordfill"
```

### Requerido

`required` Evita que la ventana de diálogo "swiftDialog" se cierre hasta que el campo tenga un valor. Los campos obligatorios están marcados con un `*` y se resaltan cuando el usuario intenta cerrarla sin completarlos.

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### Prompt

`prompt="<text>"` Muestra un texto de ejemplo dentro del campo. Este texto desaparece tan pronto como el usuario comienza a escribir y no se incluye en el resultado. No es compatible con campos de tipo `secure`.

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### Valor

`value="<text>"` El campo se rellena automáticamente con un valor predeterminado que el usuario puede modificar.

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### Expresiones regulares y errores de expresiones regulares

`regex=<pattern>` Requiere que el contenido del campo coincida con la expresión regular antes de que la ventana swiftDialog se cierre. `regexerror=<text>` Establece el mensaje que se muestra cuando el patrón no se encuentra.

A menos que el formato lo permita explícitamente, un campo `regex` no puede estar vacío.

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

Utilice `--textfieldlivevalidation` para mostrar una superposición de color verde/rojo en el campo a medida que el usuario escribe, proporcionando una retroalimentación inmediata sobre si la expresión regular se cumple.

### Editor

`editor` presenta un área de texto más grande y de varias líneas, en lugar de un campo de una sola línea.

```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### Selector de fecha

Utilice el modificador `date` o `time` para reemplazar el campo de texto con un selector de fecha y hora de macOS. El valor seleccionado se devuelve como una cadena formateada.

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

**Nota:** El modificador `isdate` ha quedado obsoleto, y se recomienda utilizar `date` y `time` en su lugar.

#### Límites de fecha

Utilice `mindate=` y `maxdate=` para limitar el rango de fechas seleccionables:

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**Formato:** Las fechas deben estar en el formato `YYYYMMDD` (independiente de la región). Se aceptan separadores, que serán eliminados (por ejemplo, `2026-09-30` → `20260930`). Las fechas inválidas se ignorarán y no se aplicará el límite establecido.

#### Formato de fecha

Utilice `format=` para especificar el formato de la salida utilizando la sintaxis de `strftime`:

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

Cadenas de formato comunes:
- `+%Y-%m-%d` - Formato ISO 8601 (por ejemplo, `2026-09-29`).
- `+%s` - Marca de tiempo Unix (segundos desde la época).
- `+%x` - Representación de la fecha según la configuración regional
- `+%D` - Formato estadounidense (por ejemplo, `09/29/26`).

#### Inicialización del selector de fechas

Use `value=` para establecer la fecha inicial. El selector acepta múltiples formatos:

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

Formatos admitidos: ISO 8601, formatos específicos de la configuración regional, formatos de 12/24 horas, marcas de tiempo de la época y lenguaje natural.

### Seleccionar archivo

`fileselect` Agrega un botón de "**Seleccionar**" que abre un explorador de archivos estándar. La ruta seleccionada se inserta en el campo y se devuelve en la salida.

```sh
--textfield "Config File,fileselect"
```

Use `filetype` para limitar las opciones de selección. Los valores deben estar separados por espacios y pueden ser extensiones de archivo o palabras clave que indiquen el tipo:

| Valor | Selecciona |
|---|---|
| `folder` | Solo directorios |
| `image` | Cualquier tipo de imagen |
| `movie` / `video` | Cualquier tipo de video |
| `audio` | Cualquier tipo de audio |
| `<extension>` | Archivos que coinciden con esa extensión (por ejemplo, `png`, `pdf`). |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

Utilice `path=<path>` para establecer el directorio que se abrirá al usar el selector de archivos:

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### Confirmar

`confirm` añade un segundo campo debajo del campo principal. Ambos campos deben contener el mismo valor antes de que swiftDialog acepte la entrada. Esto es útil para la confirmación de contraseñas.

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### Combinación de modificadores

Los modificadores pueden combinarse libremente (siempre que sean compatibles).

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### Formato JSON

Los campos de texto se pueden especificar en formato JSON de dos maneras:

#### JSON de configuración completa

Al utilizar un archivo de configuración JSON o `--jsonstring`/`--jsonfile`, especifique los campos de texto como una matriz:

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### Configuración JSON para argumentos individuales

A partir de la versión 3.1.1, los campos de texto también pueden especificarse como objetos JSON a través de `--textfield` (en lugar de utilizar modificadores separados por comas). Esto proporciona un control más directo y es especialmente útil para configuraciones complejas.

**Sintaxis:**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**Características:**
- `title` - El texto de la etiqueta del campo
- `name` - Nombre alternativo para la clave de salida
- `required` - El campo debe estar completado (verdadero/falso).
- `secure` - Ocultar lo que se escribe a medida que se introduce (campo de contraseña).
- `passwordfill` - Activar la función de autocompletar contraseñas de macOS (requiere `secure`).
- `prompt` - Texto de ejemplo que se muestra dentro del campo
- `value` - Completar automáticamente el campo con un valor predeterminado
- `regex` - Exigir que el contenido del campo coincida con la expresión regular
- `regexerror` - Se muestra un mensaje de error personalizado cuando la expresión regular no se cumple
- `editor` - Editor de texto de varias líneas en lugar de un campo de una sola línea
- `date` - Reemplazar el campo con un selector de fecha (verdadero).
- `time` - Reemplazar el campo con un selector de fecha y hora (verdadero).
- `mindate` - Fecha mínima seleccionable (formato AAAAmmDD).
- `maxdate` - Fecha máxima seleccionable (formato AAAAmmDD).
- `format` - Formato de retorno utilizando la sintaxis de `strftime` (por ejemplo, `+%Y-%m-%d`, `+%s`).
- `fileselect` - Añadir un botón de "Seleccionar" que abra un explorador de archivos
- `filetype` - Limitar el selector de archivos a tipos específicos (extensiones o palabras clave separadas por espacios).
- `path` - Directorio inicial para el selector de archivos
- `confirm` - Añadir un campo de confirmación que debe coincidir con el campo principal

**Ejemplos:**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**Campos para la selección de fechas:**
- Utilice `"date": true` o `"time": true` (o ambos) para crear un selector
- `"mindate"` y `"maxdate"` aceptan fechas en formato `YYYYMMDD` (se eliminan los separadores).
- `"format"` Establece el formato de la salida utilizando la sintaxis de `strftime`
- `"value"` Permite establecer la fecha y hora inicial en múltiples formatos (ISO, configuración regional, época, lenguaje natural).

**Todos los modificadores son compatibles:** Cada modificador disponible en formato CSV también está disponible como una clave JSON.

**Campos de texto múltiples:**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**Nota:** Cuando se utiliza JSON con parámetros individuales, cada `--textfield` es independiente. El formato JSON de configuración completa sigue siendo compatible para la inicialización por lotes.

## Comportamiento del teclado

Presionar la tecla **Enter** en cualquier campo de texto de una sola línea activa la función del Botón 1, lo cual es equivalente a hacer clic en el botón predeterminado. Esto no se aplica a los campos `editor`.