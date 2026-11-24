---
title: Personalización del icono
description: Aprenda cómo configurar y personalizar iconos, imágenes y superposiciones en swiftDialog
translationSynced: 2026-11-24T22:17:11+00:00
---

##### Índice
 - [Uso básico](#uso-básico)
 - [Uso un poco más avanzado ](#uso-ligeramente-más-avanzado)
 - [Iconos integrados](#iconos-integrados)
 - [Utilizando los símbolos SF](#cómo-usar-los-símbolos-de-sf)
 - [Superposiciones de iconos](#superposiciones-de-iconos)
 - [Tamaño del icono](#tamaño-del-icono)
 - [Ocultar el icono](#ocultar-el-icono)
 - [Establecer iconos oscuros o claros](#establecer-iconos-oscuros-o-claros-según-si-la-interfaz-de-usuario-está-en-modo-oscuro-o-en-modo-claro)

***


Utilice la opción de línea de comandos `-i` o `--icon` para especificar qué icono o imagen desea mostrar en el área del título del icono.

### Uso:

`--icon <file | url | text= >`


## Uso básico

swiftDialog acepta imágenes en formatos `png` y `jpg` y muestra la imagen especificada en el área de visualización de iconos.

Las imágenes se redimensionarán para ajustarse al área de visualización, que tiene un ancho de 170 puntos y una altura de 260 puntos.

`png` es la opción preferida; sin embargo, si `jpg` está especificado, las imágenes se mostrarán con esquinas ligeramente redondeadas para un aspecto menos agresivo.

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## Uso ligeramente más avanzado
swiftDialog aceptará la ruta de una aplicación y utilizará el icono de esa aplicación como imagen.

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialog también acepta una URL que apunta a un recurso de imagen.

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## Configuración de la transparencia del icono

Utilice `--iconalpha` para establecer un valor de transparencia.

El rango va de `0.0` (totalmente transparente) a `1.0` (totalmente opaco).

## Icono alternativo (modo oscuro).

Utilice `:dark=` y especifique un icono alternativo o una ruta a utilizar si la apariencia del usuario está configurada en modo oscuro

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## Iconos integrados

swiftDialog tiene varios iconos integrados que se pueden utilizar con la opción `--icon`

`--icon info`

![Icono de información](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Icono de precaución](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![Icono de advertencia](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## Utilizando `text=`

También puede usar el prefijo `text=` para mostrar texto en el área del icono. Esto es útil para mostrar un solo carácter o un emoji.

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## Cómo usar los símbolos de SF

swiftDialog también puede mostrar cualquier icono del sistema SF Symbol. https://developer.apple.com/sf-symbols/

### Sintaxis de los símbolos SF (formato CSV).

Al especificar símbolos de sistema (SF Symbols) para un icono o un icono de superposición, se ofrecen parámetros adicionales para el color y el grosor.

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>` Especificado en formato hexadecimal, por ejemplo, #00A4C7. También acepta cualquiera de los colores estándar de Apple: `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`. Si la opción no es válida, el color predeterminado es el color del sistema `primary`

Color especial `"auto"`.

Cuando se utiliza con un símbolo SF multicolor, se aplicará el esquema de colores predeterminado del símbolo. Si se utiliza con un símbolo SF monocromático, se mostrará en negro y no se adaptará al modo oscuro.

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-40f9-99e2-caf41d07903e.png)

Los degradados de color se pueden configurar añadiendo el argumento adicional `colour2` o `color2`, por ejemplo: `SF=applelogo,colour=pink,colour2=purple`

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

Los símbolos SF multicolores se pueden colorear utilizando el argumento `palette`, por ejemplo: `SF=person.3.sequence.fill,palette=red,green,blue`

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b5b2-4dd0-b320-c65d5d5e8d22.png)

El grosor del símbolo SF se puede establecer con el argumento `weight`

   `weight=<text>` puede aceptar cualquiera de los siguientes valores:
    * delgado (predeterminado)
    * luz
    * regular
    * medio
    * pesado
    * negrita

### Símbolos de San Francisco animados

El soporte para símbolos de SF animados está disponible en macOS 14 o versiones más recientes.

Ejemplo de uso:

`--icon sf=rainbow,colour=auto,animation=variable`

Actualmente, el soporte es limitado y se aplica a los siguientes tipos de animación:
 - "variable":
 - "variable.invertir"
 - "variable.iterativo"
 - "variable.iterativo.inverso"
 - "variable.acumulativa"
 - "pulso"
 - "pulse.bylayer"

### Objetos de icono en formato JSON

Los iconos también pueden especificarse como objetos JSON para tener un control más preciso. Esto es especialmente útil para configuraciones de iconos complejas que incluyen múltiples propiedades.

**Sintaxis:**
```bash
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'
```

**Teclas admitidas:**
- `sf` / `name` / `symbol` - Nombre del símbolo SF
- `path` / `icon` / `value` - Ruta del archivo de la imagen o de la aplicación
- `weight` - Grosor de la fuente (delgado, ligero, normal, medio, grueso, negrita).
- `colour` / `color` - Color primario (en código hexadecimal o por nombre).
- `colour2` / `color2` - Color secundario para degradados
- `palette` - Conjunto de colores para símbolos multicolores
- `animation` - Tipo de animación para símbolos animados (macOS 14 o posterior).
- `bgcolour` / `bgcolor` - Color de fondo para los iconos superpuestos
- `auto` - Valor especial para el esquema de color automático
- `light` / `dark` - Variantes de modo claro/oscuro (objeto de icono anidado).

**Ejemplos:**

```bash
# Basic symbol with colour and weight
dialog --icon '{"sf":"gear","colour":"blue","weight":"bold"}'

# Gradient
dialog --icon '{"sf":"applelogo","colour":"pink","colour2":"purple"}'

# Multicolor palette
dialog --icon '{"sf":"person.3.sequence.fill","palette":["red","green","blue"]}'

# Application icon
dialog --icon '{"path":"/Applications/Chess.app"}'

# Light/dark variants
dialog --icon '{"light":{"sf":"sun.max"},"dark":{"sf":"moon"}}'

# Animated symbol (macOS 14+)
dialog --icon '{"sf":"rainbow","colour":"auto","animation":"variable"}'

# Overlay icon with background
dialog --overlayicon '{"sf":"exclamationmark","colour":"yellow","bgcolour":"none"}'
```

Funciona en: `--icon`, `--overlayicon`, `--listitem` (campo de icono), `--checkbox` (campo de icono)

**Nota:** Cuando se utiliza en `--listitem` o `--checkbox`, el campo de icono acepta objetos JSON anidados:

```bash
dialog --listitem '{"title":"Download","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}'
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}'
```



## Superposiciones de iconos

Utilice la opción de línea de comandos `-y` o `--overlayicon ` para especificar qué icono o imagen desea utilizar como superposición del icono principal.

Las superposiciones se muestran con la mitad de la resolución normal y se desplazan a la esquina inferior derecha del área de visualización de los iconos principales. Con esta opción, puede combinar imágenes para su visualización

Los iconos superpuestos utilizan los mismos tipos de imagen y las mismas ubicaciones que el parámetro `--icon`, incluyendo los recursos integrados y los símbolos de SF


Aquí hay un ejemplo:

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![icono de precaución con superposición del icono de Safari](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

Ejemplo 2:

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Icono de Chrome con una superposición de advertencia](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### Superponer un fondo al utilizar los símbolos de SF

Al utilizar los símbolos SF, se añade un círculo ligeramente translúcido para que el símbolo destaque sobre el icono principal, ya que muchos símbolos contienen elementos que no funcionan bien como una superposición.

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

La apariencia del fondo se puede ajustar con un modificador `bgcolor=` y utiliza la misma sintaxis en todas las situaciones en las que `color` puede ser configurado. También se puede especificar un color especial `bgcolor=none` si no se desea utilizar el fondo predeterminado.

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## Tamaño del icono

`--iconsize <float>` Redimensionará el icono a la anchura especificada. La anchura predeterminada es `170`

Ejemplo 1:

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


Ejemplo 2:

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## Posición del icono

`--centreicon` o `--centericon`

Cambia la posición del icono para que quede centrado

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

También se puede modificar utilizando un archivo de comandos mientras swiftDialog está en ejecución

`echo "icon: centre" >> /var/tmp/dialog.log`

## Ocultar el icono

El icono se puede eliminar por completo utilizando cualquiera de los siguientes comandos:

`--hideicon`

o

`--icon none`

## Establecer iconos oscuros o claros, según si la interfaz de usuario está en modo oscuro o en modo claro

Excepto para algunos símbolos de San Francisco (SF Symbols), swiftDialog no incluye ninguna funcionalidad integrada para cambiar entre los iconos del modo oscuro y el modo claro.

El icono de configuración se puede establecer en función de la configuración de la interfaz de usuario, aunque esto se puede lograr en el script que realiza la llamada.

**zsh / bash** (gracias a [mm2270](https://github.com/mm2270)).

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

o en Python (gracias a [joncrain](https://github.com/joncrain)).

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```