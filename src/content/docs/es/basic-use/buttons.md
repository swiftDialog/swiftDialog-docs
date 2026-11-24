---
title: Botones y comportamiento de los botones
description: Aprenda cómo configurar el texto, las acciones y el comportamiento de los botones en swiftDialog
translationSynced: 2026-11-24T22:20:27+00:00
---

El cuadro de diálogo puede mostrar hasta tres botones.

Los botones se muestran en la parte inferior de la ventana de diálogo

![Área de botones de diálogo](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## Botón 1: El botón predeterminado
Por defecto, se muestra un único botón con la etiqueta "**Aceptar**". El botón predeterminado siempre está presente, está asociado a la tecla **_Enter_** y cierra la aplicación de diálogo con el código de salida `0`

La etiqueta del botón predeterminado se puede modificar con una cantidad arbitraria de texto utilizando la opción `--button1text`

e.g. `--button1text "Enter to Continue"`

![Texto del botón 1 ](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

La acción también se puede modificar utilizando la opción `--button1action`, por lo que, además de simplemente cerrar la aplicación Dialog, se puede realizar una acción

En esta etapa, las acciones se limitan a abrir una URL en el navegador predeterminado del usuario.

e.g. `--button1action "https://github.com/"`

## Botón 2: El botón de cancelar
El segundo botón está oculto de forma predeterminada. Se puede mostrar utilizando la opción `-2` o `--button2`, que mostrará el botón con la etiqueta predeterminada de "**Cancelar**". El segundo botón está asignado a la tecla **_Esc_** y cierra la aplicación de diálogo con el código de salida `2`

La etiqueta del segundo botón se puede modificar con una cantidad arbitraria de texto utilizando la opción `--button2text`. Cuando se utiliza esta opción, no es necesario invocar la opción `--button2`. La visualización del botón se muestra automáticamente si se está modificando la etiqueta de texto.

Aquí hay un ejemplo:

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![Botón 2 No me importa ](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

El botón 2 no tiene ninguna otra función implementada

## El botón "Más información"
El botón "Más información" está oculto por defecto. Se puede mostrar utilizando la opción `-3` o `--infobutton`, lo que hará que el botón aparezca con la etiqueta predeterminada de "**Más información**". Al hacer clic en el botón, se cerrará la ventana swiftDialog con un código de salida de `3`

Si el argumento `--infobuttonaction` está presente, al hacer clic en el botón "Más información", solo se ejecutará la acción `--infobuttonaction` y swiftDialog no se cerrará automáticamente. Si se añade el argumento `--quitoninfo`, se restaurará el comportamiento de cierre.

La etiqueta del botón de información puede modificarse con una cantidad arbitraria de texto utilizando la opción `--infobuttontext`. Al utilizar esta opción, no es necesario activar la opción `--infobutton`. La visualización del botón se realiza automáticamente si se modifica la etiqueta de texto.

Aquí hay un ejemplo:

`--infobuttontext "Click here for more details"`

![Texto del botón "Información": haga clic para obtener más detalles.](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

La acción también se puede modificar utilizando la opción `--infobuttonaction`, por lo que, además de simplemente cerrar la aplicación Dialog, se puede realizar una acción

En esta etapa, las acciones se limitan a abrir una URL en el navegador predeterminado del usuario.

e.g. `--infobuttonaction "https://github.com/"`

## Símbolos de los botones

Establece el símbolo de SF que se utilizará, además de la etiqueta del botón

### Sintaxis de CSV

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

Recibe el nombre de un símbolo de San Francisco como argumento

Propiedades opcionales proporcionadas como valores separados por comas (en cualquier orden):
 - posición: una de las siguientes: inicial, final, superior, inferior; valor predeterminado: inicial
 - modo de renderizado: una de las opciones disponibles son: jerárquico, monocromo, multicolor, paleta. El valor predeterminado es monocromo
 - paleta: Añada dos o tres colores en el formato "paleta=color1-color2-color3"
   - Por ejemplo: paleta = rojo-verde-azul
 - tamaño: en el formato tamaño=<num>
 - color: en el formato color=<text|hex>
   - Si se ha seleccionado el modo de renderizado multicolor, el color se ignora

Aquí hay un ejemplo:

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### Sintaxis de objetos JSON

A partir de la versión 3.1.1, los símbolos de los botones también pueden especificarse como objetos JSON para un control más preciso.

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**Características:**
- `name` - Nombre del símbolo de SF (obligatorio).
- `position` - Posición del símbolo: `leading`, `trailing`, `top`, `bottom` (por defecto: `leading`).
- `colour` / `color` - Color del símbolo (en código hexadecimal o por nombre).
- `size` - Tamaño del símbolo en puntos
- `rendering` - Modo de renderizado: `hierarchical`, `monochrome`, `multicolour`, `palette`
- `palette` - Arreglo de 2 a 3 colores para símbolos multicolores (separados por comas en formato CSV, en formato de arreglo en JSON).

**Ejemplos:**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**Nota:** Cuando se utiliza `rendering: palette`, la paleta debe ser un arreglo en formato JSON: `["red","green","blue"]`. En formato CSV, utilice guiones para unir los elementos: `palette=red-green-blue`.

## Posición del botón

Por defecto, el botón 1 y el botón 2 se encuentran en el lado derecho, mientras que el botón de información se encuentra en el lado izquierdo.

Usar `--buttonstyle center` colocará los botones 1 (y el 2, si está presente) en la parte inferior central de la ventana de diálogo

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` y `--infotext` no son compatibles al utilizar la opción `--buttonstyle center`

## Estilo "apilado" para los botones

`--buttonstyle stack`

Muestra el botón 1 y el botón 2 en una disposición vertical que ocupa todo el ancho disponible.

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` y `--infotext` no son compatibles al utilizar la opción `--buttonstyle stack`

## Comportamiento de las teclas `[return]` y `[enter]`

Si no hay campos de entrada, el elemento de control de entrada con foco en el diálogo es `button1`, y tanto `[enter]` como `[return]` activarán el botón, ya que es el único elemento interactivo en la ventana y, por lo tanto, tiene el foco predeterminado del teclado. El efecto es que esto cierra el diálogo (asumiendo que el botón está activo y no está deshabilitado).

La tecla `[return]` siempre activa el botón 1, a menos que un campo de edición tenga el foco. La tecla `[enter]` solo se activa en el elemento que tiene el foco (por eso funciona para cerrar el diálogo en ventanas que no tienen elementos de entrada).

En un campo de texto de una sola línea, `[return]` no permite insertar saltos de línea, por lo que la acción predeterminada se activa y se cierra el cuadro de diálogo (se ejecuta el elemento de respuesta predeterminado). En cambio, `[enter]` no tiene ningún efecto, ya que tampoco permite insertar una nueva línea, pero como no tiene control sobre la acción del elemento de respuesta predeterminado, no ocurre nada.

En un campo de texto de varias líneas (es decir, `--textfield` con `editor` habilitado), la tecla `[return]` *puede* insertar una nueva línea, y esta acción tiene prioridad sobre cualquier asignación predeterminada (es decir, la acción de presionar el botón 1 para cerrar la ventana). La tecla `[return]` también funciona como se espera e inserta una nueva línea.

### Modificar el comportamiento predeterminado de `[return]`, `[enter]` o `[esc]`

Si no desea que el comportamiento predeterminado de `[return]`, `[enter]` o `[esc]` sea cerrar el cuadro de diálogo, puede utilizar la opción `--hidedefaultkeyboardaction` para modificar este comportamiento. Esta opción cambiará las teclas predeterminadas `[return]` o `[escape]`, de modo que también requieran la combinación `cmd`+`shift` para activarse. Esto ayuda a prevenir el cierre accidental de los cuadros de diálogo.

## Códigos de retorno

Los siguientes códigos de retorno se envían después de cada acción. Estos pueden ser ignorados o utilizados en un script de llamada para realizar acciones adicionales

| Nombre del botón | Opcional | Tecla de acceso directo | Código de retorno |
| ----------- | -------- | ------ | ----------- |
| `button1`   | No       | Entrar  | 0           |
| `button2`   | Sí      | Esc    | 2           |
| `infobutton` | Sí      |        | 3           |

## Deshabilitar botones

Los botones 1 y 2 se pueden desactivar al inicio utilizando uno de los siguientes comandos:

`--button1disabled`

`--button2disabled`

El botón 1 se puede ocultar por completo estableciendo el texto del botón en `none`

_Tenga en cuenta que esto también desactiva el uso de la tecla [Intro] para cerrar un cuadro de diálogo, así que asegúrese de tener una forma de que el cuadro de diálogo se pueda cerrar._