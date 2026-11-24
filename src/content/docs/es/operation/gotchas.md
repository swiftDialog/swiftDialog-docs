---
title: Gotchas
description: Problemas comunes y consejos para solucionar problemas de swiftDialog
translationSynced: 2026-11-24T23:00:58+00:00
---

# Problemas con los archivos de comandos

## Permisos insuficientes

Si se ejecuta swiftDialog y no se puede escribir en el archivo de comandos, se mostrará un error:

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

El archivo de comandos debe ser eliminado o, alternativamente, se deben establecer los permisos a `-rw-rw-rw` (666).

---

# Cambios en el comportamiento de swiftDialog 3.1.1

## `--alwaysreturninput` Rentabilidad de todas las opciones de cese

**¿Qué ha cambiado:** A partir de la versión 3.1.1, `--alwaysreturninput` devuelve resultados en formato de selección/lista/JSON en **todos** los métodos de salida, no solo al presionar un botón.

**Rutas de salida afectadas:**
- Archivo de comandos para salir
- Límite de tiempo del temporizador
- Tecla de salida
- Proceso finalizado

**Migración:** Los scripts que dependen del comportamiento anterior (que solo devolvía un resultado al presionar un botón) podrían mostrar resultados diferentes. Revise su lógica de análisis si utiliza `--alwaysreturninput`.

## `--ontop` Respeta la posición del muelle

**¿Qué ha cambiado?:** La opción `--ontop` ahora respeta la posición de la barra de tareas y ubica la ventana de diálogo dentro del marco de la pantalla (no encima de la barra de tareas).

**Impacto:** Los cuadros de diálogo ya no cubrirán el dock cuando se utilice la opción `--ontop`. Esto revierte una decisión tomada deliberadamente en una versión anterior.

## Modificadores del selector de fechas

**¿Qué ha cambiado:** El modificador `isdate` ha sido **obsoleto** y reemplazado por `date` y `time`.

**Migración:** Actualice sus scripts:

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# Errores comunes que se suelen cometer

## Opciones repetibles como argumento final

**Problema:** Las opciones repetibles (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`) utilizadas como el argumento final podrían provocar un fallo.

**Estado:** Solucionado en la versión 3.1.1

## El selector de fecha no devuelve ningún valor

**Problema:** El uso de `--textfield ...,isdate` no devolvía ningún valor porque era una estructura de soporte que nunca devolvía valores.

**Estado:** Corregido en la versión 3.1.1. Utilice los modificadores `date` o `time` en su lugar.

## El comando para añadir una descripción a la imagen no funciona

**Problema:** El archivo de comandos `imagecaption:` no tuvo ningún efecto porque solo escribía en `appvars.imageCaptionArray` (se consumía una vez al inicio) en lugar de en `observedData.imageArray` (fuente reactiva).

**Estado:** Solucionado en la versión 3.1.1

## Los encabezados del grupo "Predeterminado 5" se están mostrando incorrectamente

**Problema:** Los encabezados de los grupos de implementación ("Completado", "En proceso de instalación") se muestran en una posición incorrecta o se duplican.

**Estado:** Solucionado en la versión 3.1.1

## La barra de botones del teclado no funciona

**Problema:** `--hidedefaultkeyboardaction` no funcionaba debido a un error introducido durante la reescritura de la barra de herramientas.

**Estado:** Solucionado en la versión 3.1.1