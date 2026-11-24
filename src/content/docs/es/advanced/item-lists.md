---
title: Listados de elementos
description: Crear listas ordenadas dinámicas con indicadores de estado e iconos
translationSynced: 2026-11-24T22:33:39+00:00
---

Las listas de elementos le permiten mostrar un número razonable de elementos en una lista ordenada. Si la lista se extiende más allá del área visible, la lista se vuelve desplazable.

Las listas pueden aparecer en un diálogo con cualquiera de las opciones de personalización existentes, excepto en el caso de las imágenes, que ocupan toda la pantalla de visualización del mensaje.

<hr />
Existen tres métodos para crear una lista de elementos:

### 1) Línea de comandos

Especifique una o más entradas `--listitem <text>` como un argumento en la línea de comandos. La lista se construirá en el orden especificado.

Los iconos de los elementos de la lista se pueden configurar mediante argumentos de línea de comandos `--listitem "<text>,icon=<image>"`; sin embargo, si necesita opciones más avanzadas, debe utilizar JSON.

### 2) JSON

Al utilizar JSON como fuente de configuración, especifique los elementos como un arreglo unidimensional.

#### Básico

El método básico es una forma sencilla de iniciar una lista de elementos que no tienen un estado definido.

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### Avanzado

"Avanzado" le permite inicializar una lista y, opcionalmente, establecer un icono, un estado y un texto de estado

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### Opciones de estado

El estado de los elementos de la lista puede ser uno de los siguientes: `wait`, `success`, `fail`, `error`, `pending` o `progress`, y se mostrará un icono correspondiente en el área de estado.

Cuando se utiliza `progress` como estado, se mostrará un indicador de progreso circular como icono de estado. Agregar un número, por ejemplo, `progress: 20`, animará el indicador a la posición adecuada que represente el porcentaje a completar. El indicador de progreso acepta cualquier valor entre `0` y `100`

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### Configuración JSON para argumentos individuales

A partir de la versión 3.1.1, los elementos de la lista también pueden especificarse como objetos JSON a través de `--listitem` (en lugar de utilizar el objeto JSON de configuración completo). Esto proporciona un control más directo y es especialmente útil para configuraciones complejas con objetos de iconos anidados.

**Sintaxis:**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**Características:**
- `title` - El texto de la etiqueta del elemento de la lista
- `status` - Indicador de estado: `wait`, `success`, `fail`, `error`, `pending`, `progress` o `progress:<value>` (0-100).
- `statustext` - Texto de estado que se muestra junto al indicador de estado
- `icon` - Ruta al icono, URL, o **objeto JSON de icono anidado**

**Objetos de iconos anidados:**

El campo `icon` acepta objetos JSON para la configuración avanzada de los iconos.

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**Varios artículos:**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**Nota:** Cuando se utiliza JSON con parámetros individuales, cada `--listitem` es independiente. El formato JSON de configuración completa sigue siendo compatible para la inicialización por lotes.


### 3) Como un comando enviado al archivo de comandos

Envía los elementos como valores separados por comas

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## Actualizar una lista existente

Las entradas de una lista ya mostrada pueden actualizarse con un estado mediante el envío de comandos al archivo de comandos.


#### Básico

La sintaxis básica requerida es la siguiente:

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>` debe coincidir con el nombre/título del elemento de la lista y distingue entre mayúsculas y minúsculas
 - `<status text>` puede ser cualquier cadena de texto Unicode
   - Si se envía una de las palabras clave de estado admitidas, se mostrará un indicador correspondiente en lugar de texto

#### Avanzado

La sintaxis avanzada permite actualizar el texto de estado y el indicador de estado, así como referenciar el elemento de la lista mediante su índice. Las palabras clave están separadas por comas (esto significa que las entradas `title` y `statustext` no pueden contener texto que incluya comas).

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` comienza en 0

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

Se pueden añadir nuevos elementos al final de una lista existente con el comando `add:`, y se pueden eliminar elementos con el comando `delete:`. Al añadir una fila, los campos "estado" y "texto de estado" son opcionales.

Ejemplos:

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

Eliminar por índice: `echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

Eliminar por referencia al título `echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

Es posible agregar o eliminar elementos de una lista, incluso si la lista no está visible en ese momento.

## Mostrar u ocultar una lista

La lista puede ser ocultada o mostrada sin afectar su contenido.

mostrar `echo "list: show`

ocultar `echo "list: hide`

## Eliminar una lista

Una lista existente puede ser eliminada enviando el comando `list: clear` al archivo de comandos.

Eliminar una lista elimina todas las entradas y los estados asociados a ella.

## Ejemplos


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

Luego, al enviar los siguientes comandos, se actualizará el estado de la lista

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### Formato JSON avanzado

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)