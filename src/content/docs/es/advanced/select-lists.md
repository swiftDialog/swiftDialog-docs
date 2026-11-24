---
title: Seleccionar listas y botones de opción
description: Creación de listas desplegables y grupos de botones de opción para la selección por parte del usuario
translationSynced: 2026-11-24T22:33:57+00:00
---

Dialog tiene la capacidad de tomar una lista de valores y mostrarlos en un menú desplegable, con la opción de seleccionar un valor por defecto.

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## Cómo utilizar


### Título de la lista seleccionada

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

La etiqueta se puede asignar a la lista mediante la opción de línea de comandos `--selecttitle`. Por ejemplo: `--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


Este nombre aparecerá en la salida de swiftDialog en la consola estándar (STDOUT) junto con el valor del elemento seleccionado. Para una lista de selección única, el formato de la salida estándar será:
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

Se pueden especificar múltiples argumentos `--selecttitle`. Se pueden especificar argumentos relacionados `--selectvalues` y `--selectdefault`, y estos se asocian a una lista seleccionable en el orden en que se presentan

Si se utilizan listas de selección múltiple, los atributos "SelectedOption" y "SelectedIndex" no se representan.

La visualización de elementos seleccionados solo se muestra si el código de salida de swiftDialog es 0

### Seleccionar valores de la lista

`--selectvalues <text><csv>`

Los valores se especifican en formato CSV y se pasan mediante la opción de línea de comandos `--selectvalues`, por ejemplo: `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### Lista predefinida

`--selectdefault <text>`

La opción predeterminada se puede establecer mediante la opción de línea de comandos `--selectdefault`, por ejemplo: `--selectdefault "Option 4"`

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

Si no se especifica un valor predeterminado, y el usuario no selecciona ninguna opción de la lista, no se mostrará ningún resultado.


ejemplo de resultado:
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

La información sobre la producción de ciertos elementos solo se muestra si el código de salida del programa Dialog es 0

### Configuración JSON para argumentos individuales

Las listas seleccionables también se pueden definir utilizando objetos JSON a través de `--selectitem` (o `--selecttitle` con un valor JSON). Esto proporciona un control más directo sobre las propiedades de cada elemento.

**Sintaxis:**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**Características:**
- `title` - La etiqueta para la lista desplegable
- `values` - Conjunto de valores de opción
- `default` - El valor seleccionado por defecto
- `required` - Indica si el campo es obligatorio (se ignora para los botones de opción).
- `style` - Estilo de visualización: `list`, `radio`, `searchable` o `multiselect`
- `name` - Nombre alternativo para la clave de salida

**Ejemplos:**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

Los elementos JSON son independientes de los argumentos posicionales `--selectvalues/--selecttitle/--selectdefault`. Al utilizar JSON, los valores se filtran de la lista de etiquetas posicionales para evitar duplicaciones.

## Esquema JSON

Las listas seleccionables se pueden especificar mediante JSON para tener un control más preciso.

### Archivo de configuración JSON completo.

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### Formato JSON para argumentos

Los elementos individuales también pueden definirse utilizando `--selectitem` o `--selecttitle`, junto con un objeto JSON:

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

**Nota:** `--selecttitle` trata los objetos JSON de la misma manera que `--selectitem`.

### Ejemplos:

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## Modificadores

### Nombre

Hace que la salida se registre con el texto especificado `name` en lugar de utilizar el título

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### Buscable

El modificador `searchable` agrega un campo de búsqueda a la lista. Escribir en el cuadro de texto filtrará la lista.

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### Radio

El modificador `radio` cambiará la lista de selección para mostrar un grupo con botones de opción. Cuando se utiliza `radio` sin especificar un elemento predeterminado, el primer elemento de la lista se convertirá en el elemento seleccionado por defecto. Por lo tanto, el uso de botones de opción *siempre* obliga a que se seleccione uno de los valores, y los modificadores como `required` se ignoran.

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### Requerido

El modificador `required` hará que esa lista específica sea un campo obligatorio que debe tener un valor antes de que la ventana de diálogo (swiftDialog) se cierre

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### Selección múltiple

El modificador `multiselect` permite seleccionar más de una opción de la lista. Los elementos seleccionados aparecen como etiquetas que se pueden eliminar, y el resultado es una lista de los valores elegidos, separados por comas.

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

Al utilizar `multiselect`, los valores seleccionados se devuelven como una única cadena de texto separada por comas:

```
"Choose options" : "Option One, Option Three"
```

O, en formato JSON:
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## Estilo global

`--selectstyle [list | radio | searchable | multiselect]`

Establece el estilo de visualización para **todos** los elementos de la lista de selección en el diálogo. Este es el equivalente global de establecer el modificador de estilo en cada `--selecttitle` individualmente. Los modificadores de estilo por lista en `--selecttitle` tienen prioridad sobre esta configuración global.

| Valor | Descripción |
|---|---|
| `list` | Menú desplegable estándar (por defecto). |
| `radio` | Grupo de botones de opción |
| `searchable` | Lista desplegable con un campo de texto para filtrar |
| `multiselect` | Campo de búsqueda que permite seleccionar múltiples opciones |

## Añadir secciones a la lista

Agregue tres o más guiones `---` a su lista donde necesite un separador

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**NOTA: cada `---` se contará en el índice, aunque el separador en sí mismo no sea seleccionable. En el ejemplo anterior, habrá 7 elementos en el array de la lista, aunque solo se muestren 5 en el menú. Tenga esto en cuenta al crear sus listas de opciones.**

## Salida

Dialog mostrará el valor seleccionado por el usuario (o el valor predeterminado, si se ha definido, en caso de que el usuario no seleccione ninguna opción) en `stdout` al finalizar. Esta salida puede ser procesada por un script y, en consecuencia, se pueden realizar acciones sobre ella.

Hay dos líneas en la salida.
* La primera línea es el texto del elemento de la lista y se mostrará como `SelectedOption: <text of item>`
* La segunda línea indica el índice del elemento seleccionado y tendrá el formato `SelectedIndex: <index of item>`

El índice comienza en `0`, por lo que si se selecciona el tercer elemento de la lista, el resultado de `SelectedIndex` será `SelectedIndex: 2`

## Ejemplo de resultado de lectura

Dado el siguiente resultado:
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

Para obtener el valor que desea procesar, haga que la información pase por los comandos grep y awk

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

o

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## Añadir listas de selección múltiple

Para agregar múltiples listas de selección, simplemente especifique múltiples instancias de `--selectvalues`, `--selecttitle` y `--selectdefault`. El título y el valor predeterminado se asignarán en el orden en que se proporcionan.


### Salida con selección múltiple

Cuando se utilizan múltiples listas de selección, la salida se modifica para permitir el análisis de las diferentes listas con nombres. Por ejemplo, si se utiliza el formato JSON anterior y se seleccionan las opciones "dos" y "rojo", el resultado será el siguiente:

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

Si se envía la salida en formato JSON, el resultado sería el siguiente:

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```