---
title: Modo constructor
description: Edite las propiedades y la apariencia de una ventana de diálogo y guarde los resultados en un archivo de configuración JSON
translationSynced: 2026-11-24T23:14:49+00:00
---


## Kit de construcción swiftDialog

Para activar, ejecute `dialog --builder`. Al llamarla, se muestra una ventana adicional que le permite actualizar el contenido y las propiedades del diálogo, y ver los resultados en tiempo real.

Luego, puede exportar el resultado en formato **JSON** o como una **línea de comandos** lista para usar, que le permitirá recrear el diálogo tal como lo diseñó. `dialog`

** NOTA: Esta función no cubre el 100% de todas las características de swiftDialog, y algunos ajustes no están disponibles o no aparecerán en el resultado generado. El desarrollo está en curso. **

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### Básico
 - [Título](/es/builder/title/)
 - [Mensaje](/es/builder/message/)
 - [Icono](/es/builder/icon/)
 - [Barra lateral](/es/builder/sidebar/)
 - [Ventana](/es/builder/window/)
 - [Botones](/es/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### Avanzado
 - [Casillas de verificación](/es/builder/checkboxes/)
 - [Imágenes](/es/builder/images/)
 - [Elementos de la lista](/es/builder/listitems/)
 - [Medios](/es/builder/media/)
 - [Campos de texto](/es/builder/textfields/)

</div>

</div>

### Salida

La vista de **Salida** muestra el diseño actual, ya sea en formato **JSON** o como una llamada a la **línea de comandos**, y permite alternar entre ambas opciones mediante la pestaña correspondiente. Desde allí, puede **copiar al portapapeles** o **guardar el archivo**. El botón **Comando de exportación**, ubicado en el pie de página, copia la línea de comandos desde cualquier parte del editor.