---
title: Imágenes para banners
description: Mostrar imágenes en la parte superior de los cuadros de diálogo, con la opción de superponer un texto de título
translationSynced: 2026-11-24T22:36:00+00:00
---

Utilice la opción de línea de comandos `-n` o `--bannerimage` para especificar una imagen que se mostrará en la parte superior del cuadro de diálogo.

Uso:

`--bannerimage <file | url | colour= >`

El uso de una imagen de encabezado deshabilitará la visualización del área de la imagen del icono. Esto es equivalente a utilizar la opción `--hideicon`

## Uso básico

Dialog acepta imágenes en formato png y jpg, y muestra la imagen especificada en el área del banner. La imagen del banner tiene una altura máxima de 150 puntos y se extiende a lo ancho de la ventana del diálogo. En combinación con la opción `-s` o `--small`, la altura de la imagen del banner se limita a 100 puntos

Se puede utilizar una imagen de cualquier tamaño. El área de visualización de la imagen se adaptará al tamaño de la imagen de encabezado que desee utilizar, con una altura máxima de 150 puntos.

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

Se puede especificar una altura determinada utilizando la opción `--bannerheight`. Esto anulará la altura predeterminada.

Además, se puede especificar un color sólido utilizando el prefijo `colour=`. El color puede especificarse como un valor hexadecimal o como un nombre de color.

Aquí hay un ejemplo:

`--bannerimage colour=red` o `--bannerimage colour=#ff0000`

Por defecto, se aplica una sutil transición de color, que va del blanco a un color y luego al negro, a los colores sólidos. Para desactivarla, añada `,nogradient`.

`--bannerimage colour=red,nogradient`

### Banners con degradado

Se puede especificar un degradado lineal utilizando el prefijo `gradient=`. Proporcione dos o más colores separados por comas, y opcionalmente defina la dirección con `:angle=<degrees>`:

```sh
--bannerimage "gradient=red,blue"
--bannerimage "gradient=red,orange,yellow:angle=135"
```

Convenciones de ángulo: `0` = de abajo hacia arriba, `90` = de izquierda a derecha (por defecto), `180` = de arriba hacia abajo, `270` = de derecha a izquierda.

Si se proporciona solo un color a `gradient=`, el resultado es idéntico a `colour=` (una superposición que va del blanco al color y luego al negro).

## Texto del título dentro del área del banner

`--bannertitle`

Utilizando este comando, puede optar por mostrar el texto del título dentro del banner utilizando la opción `.`. Al hacerlo, se establece el color del texto a blanco de forma predeterminada, aunque esto se puede modificar con los modificadores de personalización de la fuente del título](/basic-use/customizing-title#customising-title-font-properties).

Puede usarlo como una opción alternativa a `--title`, o bien, puede pasar una cadena de texto para que se muestre como título. Si tanto `--title` como `--bannertitle` tienen argumentos de tipo cadena, `--bannertitle` tendrá prioridad.

Todos los modificadores `--titlefont` se aplican al texto del título del banner, incluyendo `shadow`, `colour`, `size`, `weight`, `alignment` y `offset`.

`--titlefont shadow=1` Aplica una sombra sutil debajo del texto.

Si `--subtitle` también está activado, el subtítulo se muestra debajo del título, dentro del área del banner, utilizando la misma fuente pero con un tamaño más pequeño.

![image](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)