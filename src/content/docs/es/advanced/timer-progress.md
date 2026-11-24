---
title: Temporizador y barra de progreso
description: Crear diálogos con temporizadores de cuenta regresiva y barras de progreso interactivas
translationSynced: 2026-11-24T22:32:40+00:00
---

Se puede iniciar un diálogo con un temporizador que se cerrará una vez que hayan transcurrido los segundos especificados

`--timer (<seconds>)`


Reemplaza el botón predeterminado con un temporizador de cuenta regresiva, después del cual el diálogo se cerrará con un código de salida `4`. El valor predeterminado del temporizador es de `10` segundos. Se puede especificar un valor opcional `<seconds>` para establecer la duración deseada. Si `<seconds>` es mayor que 60, la cuenta regresiva se mostrará en formato `HH:MM:SS`, por ejemplo, 280 segundos se mostrarán como `4:40` durante la cuenta regresiva inicial.

Si se utiliza en conjunto con `--button1text`, se mostrará el botón predeterminado, pero estará desactivado durante los primeros 3 segundos del temporizador. Después de ese tiempo, el botón se activa y se puede utilizar para cerrar la ventana de diálogo con el código de salida estándar 1, que es 0

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` ocultará la barra de progreso y el indicador de cuenta regresiva.

De esta manera, se asegura que el botón predeterminado sea visible para evitar que aparezcan cuadros de diálogo que no se pueden cerrar y que no indican cuándo expira el temporizador.

---

## Barra de progreso

Dialog puede mostrar una barra de progreso interactiva que puede actualizarse dinámicamente a través del [archivo de comandos](/es/advanced/command-file).

`--progress [<int>]`

Muestra una barra de progreso con el número de pasos especificado. Si no se proporciona ningún valor, el valor predeterminado es de 10 pasos.

Para avanzar la barra de progreso, envíe un comando al archivo de comandos del diálogo:

```sh
echo "progress: <int>" >> /var/tmp/dialog.log
```

`--progresstext <text>`

Establece el texto inicial que se muestra debajo de la barra de progreso. Este texto se puede actualizar en cualquier momento:

```sh
echo "progresstext: Installing software..." >> /var/tmp/dialog.log
```

### Alineación del texto de progreso

`--progresstextalignment [left | right]`

Establece la alineación horizontal del texto de progreso que se muestra debajo de la barra de progreso. El valor predeterminado es centrado.