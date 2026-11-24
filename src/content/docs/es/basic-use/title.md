---
title: Personalización del título
description: Aprenda cómo configurar y personalizar el texto del título y las propiedades de la fuente en swiftDialog
translationSynced: 2026-11-24T22:12:40+00:00
---

## Título de la configuración

Utilice la opción de línea de comandos `-t` o `--title` para especificar el texto que desea que aparezca en el área del título del cuadro de diálogo.

Aquí hay un ejemplo:

`--title "An Important Message"`

`-t "An Important Message"`

El área del título es una sección rectangular de ancho fijo y texto en negrita que se encuentra en la parte superior de la ventana de diálogo. Si el texto es más largo que el tamaño de la ventana, se truncará

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## Personalización de las propiedades de la fuente del título

Utilice la opción de línea de comandos `--titlefont` para establecer las propiedades de la fuente del título.

### Sintaxis de CSV

Las propiedades de la fuente se expresan en forma de `property=value`, y las múltiples propiedades se separan mediante una coma.

Las propiedades que se pueden modificar son:
 * `colour=<hex_value>` (alternativamente `color=<hex_value>`)
   * especificado en formato hexadecimal, por ejemplo, #00A4C7
 * `size=<float>`
   * Acepta cualquier valor numérico decimal, por ejemplo, 30, 65, 72.3
 * `weight=<text>`
   * Acepta cualquiera de las siguientes opciones: delgada, ligera, normal, media, gruesa o negrita (por defecto).
 * `name=<fontname>`
   * Acepta un nombre de fuente o una familia de fuentes. Se puede obtener una lista de los nombres disponibles utilizando `--listfonts` o consultando la aplicación "Libro de fuentes" de macOS.
 * `alignment=[left|right]`
   * Alinea el texto del título a la izquierda o a la derecha
 * `offset=<float>`
   * Desplaza el texto del título horizontalmente según el número de puntos especificado. Los valores positivos desplazan el texto hacia la derecha, mientras que los valores negativos lo desplazan hacia la izquierda. Cuando se utiliza `alignment=right`, la dirección del desplazamiento se invierte automáticamente, de modo que un valor positivo sigue desplazando el texto hacia el borde derecho.
 * `shadow`
   * Agrega una sombra difusa al texto (booleano, no se requiere valor).

 > **PRECAUCIÓN:** Tenga cuidado al combinar nombres de fuentes y grosores. Al especificar una fuente o una familia de fuentes por nombre, es posible que ciertos grosores no estén disponibles. Si esto ocurre, el grosor de la fuente especificado se ignorará.

Puede utilizar uno o varios de estos parámetros, y el orden en que se especifiquen no es relevante. Por ejemplo, si solo desea modificar el tamaño, podría utilizar lo siguiente:

`--titlefont "size=60"`

Ejemplo 1: `--titlefont "colour=#00A4C7,weight=light,size=60"`

Este ejemplo establece el color al valor `#00A4C7`, el peso a `light` y el tamaño de la fuente a `60`, y se mostrará de la siguiente manera:

<img width="400" alt="image" src="/images/titlefont1.png" />

Ejemplo 2: `--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

Este ejemplo establece el color al valor `#D054A0 `, el tamaño a `40` y utiliza el nombre de la fuente "Chalkboard-Bold".

<img width="400" alt="image" src="/images/titlefont2.png" />

Ejemplo: Alineación a la izquierda/a la derecha:

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### Sintaxis de objetos JSON

A partir de la versión 3.1.1, `--titlefont` y `--messagefont` también pueden especificarse como objetos JSON para un control más preciso:

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**Características:**
- `name` - Nombre o familia de la fuente
- `size` - Tamaño de fuente en puntos
- `colour` / `color` - Color del texto (código hexadecimal o nombre).
- `weight` - Grosor de la fuente: `thin`, `light`, `regular`, `medium`, `heavy`, `bold`
- `alignment` - Alineación del texto: `left`, `right` (solo título).
- `offset` - Desplazamiento horizontal en puntos (solo para el título).
- `shadow` - Añadir sombra difusa (booleano).

**Ejemplos:**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**Nota:** La clave `shadow` ahora está soportada en formato JSON (anteriormente, solo estaba disponible en formato CSV).

### Utilizar el color en el título

Usar `colour=<value>` establecerá el color base del texto; sin embargo, puede definir el color de palabras o letras individuales utilizando el formato `:colour[text]`

Aquí hay un ejemplo:

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## Subtítulo

Utilice `--subtitle <text>` para mostrar una línea de texto secundaria debajo del título, utilizando la misma fuente pero con un tamaño más pequeño.

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

El subtítulo hereda el mismo nombre de fuente, peso y color que el título, pero se muestra en `titlefont size − 10pt`.

#### Ocultar el área del título

Utilice la palabra clave `none` para ocultar el área del título. Esto eliminará la barra de título y la línea de separación horizontal

e.g. `--title none`




