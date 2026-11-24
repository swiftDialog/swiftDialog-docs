---
title: Configuración en formato JSON
description: Utilizar JSON para especificar las opciones de diálogo en configuraciones complejas
translationSynced: 2026-11-24T22:26:28+00:00
---

En lugar de utilizar numerosas opciones de línea de comandos para construir diálogos complejos, puede usar las opciones `--jsonfile` o `--jsonstring` para definir parámetros.

El formato JSON utiliza las mismas opciones que se especifican en la línea de comandos, con algunas excepciones y consideraciones.

**Nota:**
 - Las opciones de línea de comandos se pueden utilizar junto con JSON, pero cualquier opción definida en el archivo JSON tendrá prioridad
 - Para admitir caracteres literales `\n` en el texto del mensaje, `--jsonstring` requiere que la entrada en formato JSON se encuentre en una sola línea continua

Aquí hay un ejemplo:

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## Diferencias con las opciones de línea de comandos

Las opciones que se pueden utilizar varias veces se pueden ingresar como un arreglo.

Por ejemplo, para especificar múltiples imágenes y sus leyendas, utilice un `image` arreglo con `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

Las casillas de verificación pueden especificarse como "marcada" y/o "deshabilitada". El valor predeterminado es `"disabled" : false` y no es necesario especificarlo

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

Para múltiples `textfield` opciones, especifique un único campo de texto donde los nombres de los campos se indiquen como un array

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### Cadenas de texto y valores booleanos

La mayoría de las opciones se pasarán como valores de tipo cadena, por lo que se requerirán comillas para especificar los valores. Algunos valores pueden especificarse como valores booleanos (`true` o `false`, sin comillas). Las opciones que aceptan un valor booleano son:

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### Opciones no disponibles desde el archivo JSON

Existen varias opciones que no están disponibles para su uso a través de JSON, ya que no tienen sentido en un entorno de producción. Estas son:

* `--jh` - Se utiliza como un reemplazo directo para aceptar las opciones de línea de comandos de JamfHelper.
* `--listfonts` - Se utiliza durante la fase de prototipado para mostrar una lista de fuentes disponibles
* `--help` - Muestra mensajes de ayuda y finaliza el programa. Se utiliza durante la fase de prototipado
* `--demo` - Muestra un cuadro de diálogo utilizando únicamente la configuración predeterminada. Se utiliza durante la fase de prototipado
* `--version` - Muestra la información de la versión del diálogo y luego finaliza el programa.
* `--showlicense` - Imprime la información de la licencia y finaliza el programa
* `--coffee` - Imprime información sobre el café y finaliza el programa

## Aquí hay un ejemplo de cómo generar JSON en Python y pasarlo como un archivo o una cadena de texto

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```