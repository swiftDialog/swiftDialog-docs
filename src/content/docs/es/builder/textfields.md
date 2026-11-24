---
title: "Modo Constructor: Campos de texto"
description: Modifique las propiedades y la apariencia de una ventana de diálogo y genere los resultados en formato JSON
translationSynced: 2026-11-24T23:18:48+00:00
---

Configure `--textfield` entradas

<img width="500" alt="image" src="/builder/builder_textfields.png" />

Haga clic en el botón `[+]` para añadir una nueva entrada

Haga clic en el icono de la papelera para eliminar una entrada

Arrastra el control (☰) que se encuentra a la izquierda de una fila para cambiar el orden de las entradas


<img width="500" alt="image" src="/builder/builder_textfields_popualated.png" />


## Propiedades

Las siguientes propiedades se pueden configurar

#### Formatear la salida en formato JSON

Establece el formato de salida. Esta propiedad se comparte con [casillas de verificación](/es/builder/checkboxes/)

#### Requerido

Establece la marca `required`.

#### Confirmar

Establece la `confirm` bandera. Al activar esta opción, se mostrará un campo de texto duplicado para la entrada configurada

#### Seleccionar archivo

Activa el botón `fileselect`

##### Tipo de archivo

Se utiliza con `fileselect`. Introduzca el tipo de archivo deseado (o los tipos como un archivo CSV), por ejemplo: `"png,jpg"`

##### Ruta inicial

Se utiliza con `fileselect`. Establece la ruta inicial que se utilizará al mostrar el cuadro de diálogo de selección de archivos

#### Título

Establece el título/etiqueta del campo de texto

#### Nombre

Establece el nombre del campo de texto. Si se utiliza, este valor representará esta entrada en la salida en lugar de la etiqueta

#### Valor predeterminado

Establezca el valor predeterminado que se mostrará en el campo de texto. Este contenido aparecerá en la salida

#### Indicación

Establece un texto de sugerencia que se mostrará en el campo de texto. Este contenido no aparecerá en la salida

#### Expresiones regulares

Establezca una expresión regular que el contenido del campo de texto debe cumplir

#### Error de expresión regular

Establezca el mensaje de error que se mostrará cuando el contenido del campo de texto no coincida con la expresión regular proporcionada

[Volver](/es/builder/builder/)