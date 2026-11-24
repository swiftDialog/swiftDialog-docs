---
title: Imágenes de fondo
description: Agregar imágenes de fondo y marcas de agua a las ventanas de diálogo
translationSynced: 2026-11-24T22:35:59+00:00
---

## Imágenes de fondo

Las imágenes pueden mostrarse en el fondo, como parte de la ventana principal de diálogo, y pueden utilizarse para insertar una marca de agua u otra imagen detrás del contenido habitual de la ventana.

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

Los fondos se pueden controlar mediante los siguientes elementos:

### `--background`

```
-bg, --background <file | url | colour= >
```

Muestra el archivo seleccionado como imagen de fondo. Si la imagen es más grande que el tamaño predeterminado del cuadro de diálogo (820x380) y no se proporcionan opciones para el tamaño de la ventana (específicamente, la altura de la ventana), la altura del cuadro de diálogo se ajustará para que la imagen ocupe toda el ancho de la ventana, que por defecto es 820, o el valor especificado mediante `--width`

Alternativamente, se puede especificar un color sólido utilizando el prefijo `colour=`. El color puede especificarse como un valor hexadecimal o como un color con nombre.

Por ejemplo: `--background colour=red` o `--background colour=#ff0000`

Por defecto, se aplica una sutil superposición de degradado a los colores sólidos. Para desactivarla, añada `,nogradient`.

`--background colour=red,nogradient`

Se puede especificar un degradado lineal utilizando el prefijo `gradient=`. Proporcione dos o más colores separados por comas, y opcionalmente defina la dirección con `:angle=<degrees>`:

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

Convenciones de ángulos: `0` = de abajo hacia arriba, `90` = de izquierda a derecha (por defecto), `180` = de arriba hacia abajo, `270` = de derecha a izquierda.

Si se proporciona solo un color a `gradient=`, el resultado es idéntico al de `colour=`.


### `--bgalpha`

```
-ba, --bgalpha <number>
```

Establece el valor alfa o la transparencia de la capa de fondo. Puede ser cualquier número entre `0` (totalmente transparente) y `1` (totalmente opaco). El valor predeterminado es `0.5`


### --bgposition

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

Ubica la imagen de fondo dentro de la ventana. Funciona mejor si las dimensiones de la imagen son menores que las de la ventana principal del diálogo, como, por ejemplo, el logotipo de una empresa. La posición predeterminada es `centre`


### --bgfill

```
-bf, --bgfill [fill | fit]
```

Especifica cómo el diálogo debe mostrar la imagen dentro del marco de la ventana

`fill` Redimensiona la imagen para que ocupe toda la ventana. La imagen se recortará si es necesario. `fit` Redimensiona la imagen para que se ajuste a la ventana, pero no se recortará, lo que podría resultar en barras negras en las áreas no transparentes (si se utiliza una imagen PNG).

La opción por defecto es `none`, que mostrará la imagen con la resolución original

## Fondo de pantalla - `--screenbackground`

```
--screenbackground <file | url>
```

Muestra la imagen especificada **en pantalla completa, detrás de la ventana de diálogo** — a diferencia de `--background`, que se muestra _dentro_ de la ventana de diálogo. Todas las demás funciones de la ventana de diálogo siguen estando disponibles, pero se impide que el usuario interactúe con cualquier otra aplicación hasta que swiftDialog se cierre (similar a `--blurscreen`, pero mostrando una imagen en lugar de un efecto de desenfoque).

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```