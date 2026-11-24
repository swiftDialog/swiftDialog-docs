---
title: "Modo de construcción: Botones"
description: Modifique las propiedades y la apariencia de una ventana de diálogo y genere los resultados en formato JSON
translationSynced: 2026-11-24T23:14:56+00:00
---

Permite configurar las propiedades del área del botón

<img width="500" alt="image" src="/builder/builder buttons.png" />

#### Tamaño del botón

Establezca uno de los cuatro tamaños de botón disponibles (afecta a todos los botones).

 - miniatura
 - pequeño/a
 - estándar (predeterminado)
 - grande

#### Botón 1

Establece el texto que se mostrará en el Botón 1, también conocido como el botón predeterminado

Predeterminado `"OK"`

La opción "Deshabilitado" establecerá el estado del botón 1 como deshabilitado (y podrá ser reactivado a través de un comando en el archivo de configuración `button1: enable`).

#### Botón 2

Establezca el texto que se mostrará en el Botón 2

Predeterminado `"Cancel"`

#### Botón de información

Configure el texto que se mostrará en el botón de información

Habilite la opción "Cerrar al mostrar información" para que el cuadro de diálogo se cierre cuando se haga clic en el botón de información

Configure la opción "Acción del botón de información" para que se abra una URL específica cuando se hace clic en el botón.

#### Símbolo

El botón 1, el botón 2 y el botón de información pueden mostrar cada uno un símbolo de SF junto a su etiqueta. El editor de símbolos expone las propiedades del símbolo a través de controles individuales:

 - Nombre del símbolo de SF
 - **Posición** — líder, seguidor, superior o inferior
 - Modo de renderizado: jerárquico, monocromático, multicolor o basado en paleta
 - **Color:** Un solo color, o 2-3 colores de la paleta, cuando se selecciona el modo de renderizado de paleta
 - **Tamaño personalizado**

Se muestra una vista previa en tiempo real del símbolo que se está creando, y el botón se actualiza en la ventana de vista previa a medida que se realizan los cambios.

[Volver](/es/builder/builder/)