---
title: Códigos de salida
description: Comprender los códigos de salida y los valores de retorno de swiftDialog
translationSynced: 2026-11-24T22:57:48+00:00
---

Cuando swiftDialog se cierra, devuelve un código de salida que puede utilizarse para determinar qué acción, si alguna, se ha realizado

|Código de salida|Causa|
|---------|-----|
|0|El usuario hizo clic en el botón predeterminado (botón 1).|
|2|El usuario hizo clic en el botón 2|
|3|El usuario hizo clic en el botón de información|
|5|Salió del programa a través del comando especificado en el archivo de comandos `quit:`|
|10|Salió del programa porque el usuario usó `cmd+q` (o la combinación de teclas Ctrl+Q).|
|20|dejó porque `--timer` alcanzó el valor 0|
|201|No se encontró el recurso de imagen|
|202|No se encontró el archivo solicitado|
|203|Se utilizó un valor de color inválido|

Más detalles en esta página: [Captura de la salida del diálogo para su procesamiento posterior](/es/operation/capturing-output)