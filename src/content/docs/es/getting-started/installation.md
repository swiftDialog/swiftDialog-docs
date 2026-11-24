---
title: Instalación
description: Cómo instalar swiftDialog en macOS
translationSynced: 2026-11-24T22:11:01+00:00
---

## Métodos de instalación

### Instalador de paquetes (recomendado).

La forma más sencilla de instalar swiftDialog es utilizando el instalador **.pkg** disponible en la página de [lanzamientos](https://github.com/swiftDialog/swiftDialog/releases)].

El instalador colocará swiftDialog en `/usr/local/bin/dialog`, que debería estar en la ubicación predeterminada `$PATH` en macOS.

### Instalación manual

Si prefiere la instalación manual:

1. Descargue la última versión desde la [página de lanzamientos](https://github.com/swiftDialog/swiftDialog/releases)
2. Extraiga el archivo binario
3. Cópielo a `/usr/local/bin/dialog` o a otra ubicación en su `$PATH`
4. Asegúrese de que el archivo binario tenga permisos de ejecución: `chmod +x /usr/local/bin/dialog`

### Instalación mediante Homebrew

Próximamente: La fórmula para la elaboración casera está en desarrollo.

## Verificación

Después de la instalación, verifique que swiftDialog esté funcionando correctamente:

```bash
dialog --version
```

O pruebe con un diálogo sencillo:

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## Actualización de swiftDialog

Para actualizar swiftDialog, simplemente descargue e instale la última versión. El instalador reemplazará la versión existente.

Puede verificar si hay actualizaciones de forma programática utilizando:

```bash
dialog --checkupdates
```

## Desinstalación

Para eliminar swiftDialog:

```bash
sudo rm /usr/local/bin/dialog
```

## Implementación a través de MDM

swiftDialog se puede implementar a través de soluciones de gestión de dispositivos móviles (MDM) como Jamf Pro, Mosyle o Iru. Simplemente, instale el archivo .pkg en los dispositivos gestionados.

### Ejemplo de política de Jamf

1. Suba el archivo .pkg de swiftDialog a Jamf Pro
2. Crear una política para implementar el paquete
3. Adapte la configuración a sus dispositivos deseados
4. Establecer disparador (registro, recurrencia, autoservicio, etc.).