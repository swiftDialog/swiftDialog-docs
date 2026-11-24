---
title: Captura de la salida de Dialog
description: Métodos para capturar la información ingresada por el usuario y procesar los resultados de la interacción
translationSynced: 2026-11-24T22:58:16+00:00
---

Existen varias formas de obtener información de Dialog o de saber qué acción realizó un usuario, o de acceder a cualquier dato que haya sido ingresado.

## Códigos de retorno

El diálogo más básico siempre tendrá al menos un botón que, al ser pulsado, cerrará la ventana con un código de retorno de `0`.

Los botones opcionales, que se activan mediante `--button2`, `--infobutton` (o sus derivados), al ser pulsados, devolverán el código `2` o `3`, dependiendo del botón que se haya presionado.

Los siguientes códigos de retorno se envían después de cada acción. Estos pueden ser ignorados o utilizados en un script de llamada para realizar acciones adicionales

| Acción      | Opcional | Tecla de acceso directo | Código de retorno |
| ----------- | -------- | ------ | ----------- |
| `button1`   | No       | Entrar  | 0           |
| `button2`   | Sí      | Esc    | 2           |
| `infobutton` | Sí      |        | 3           |
| \<timer\>   | Sí      |        | 4           |
| archivo de comandos `quit:` | Sí |    | 5           |
| `--quitkey` | Sí      | Ctrl+Q  | 10          |
| Error de autenticación | Sí  |        | 30          |
| Recurso de imagen no encontrado | |    | 201         |
| Archivo no encontrado |       |        | 202         |


Para procesar el código de retorno en su script, simplemente capture el resultado de `$?` en bash o a través del lenguaje de scripting que haya elegido.

Ejemplo: procesamiento de códigos de retorno en `zsh`:

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## salida estándar

Además de los códigos de retorno, la salida se enviará a `sdtout` si se presentan uno o más `--textfield` o `--selectvalues`. La salida predeterminada no está formateada, excepto por la separación de la etiqueta y la salida mediante un carácter `:`.

Dado el siguiente diálogo y la entrada del usuario:

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

El resultado sería el siguiente:

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` es el texto de la opción del menú desplegable que fue seleccionada. `SelectedIndex` es el índice de la opción seleccionada (los índices comienzan en 0, por lo que el índice 2 indica que se seleccionó la tercera opción de la lista).

Los campos de texto se presentan utilizando la etiqueta que se pasa al diálogo, que se utiliza como etiqueta en la salida. Por lo tanto, en el ejemplo anterior:

`text 1` muestra el texto que el usuario ingresó en el campo de texto etiquetado como "texto 1", y lo mismo ocurre con `text 2`

Para dividir estos datos, podría utilizar `awk` para procesar cada línea de salida que le interese, por ejemplo.
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

Para un procesamiento más avanzado, puede incluir el parámetro `--json`, que formateará la salida como JSON para su procesamiento mediante un analizador JSON (por ejemplo, en Python).

La salida JSON para el ejemplo anterior tendría el siguiente formato:
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## Ejemplos adicionales

Capturar la salida y el código de retorno utilizando Python:
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```