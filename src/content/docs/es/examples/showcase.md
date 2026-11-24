---
title: Showcase
description: Proyectos comunitarios, guiones y ejemplos que utilizan swiftDialog
translationSynced: 2026-11-24T23:04:44+00:00
---

## A continuación, se presenta una muestra de las diferentes formas en que se puede utilizar swiftDialog.

[Ejemplos de código para la demostración de swiftDialog](https://github.com/swiftdialog/demo)

## Talleres y videos

Estos son videos grabados en diversas conferencias.

Bart Reardon

 - [JNUC 2022](https://www.youtube.com/watch?v=HXwUeBWh20I)

 - Taller de swiftDialog [MacDevOpsYVR 2024](https://www.youtube.com/watch?v=dZgmmQbTTdg)

Jon Crain

 - PSU MacAdmins 2023: [Diálogos personalizables para macOS: Utilizando SwiftDialog para una mejor experiencia de usuario. ](https://www.youtube.com/watch?v=QtWNBn76LQM)

Trevor Sysock

 - PSU MacAdmins 2024 [¡Has instalado tu "Installomator" en mi "swiftDialog"!](https://www.youtube.com/watch?v=WU6o3iJNQM4)

## Blogs

[Cómo mostrar notificaciones personalizadas con swiftDialog y SimpleMDM](https://simplemdm.com/blog/how-to-display-custom-notifications-with-swiftdialog-and-simplemdm/)

[Conozca a Bart: Jamf](https://www.jamf.com/blog/bart-reardon-swiftdialog/)


## Proyectos que se integran con swiftDialog

Estos proyectos no requieren que swiftDialog funcione, pero se ofrecen integraciones opcionales

### [Scripting en macOS](https://scriptingosx.com) - Installomator

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Installomator/Installomator/main)

Un único script de instalación para hacerlo todo. https://github.com/Installomator/Installomator

 - [Mostrar el progreso de Installomator con SwiftDialog en Jamf.](https://github.com/Installomator/Installomator/tree/main/MDM/Jamf)

### [Mac Nerd](https://github.com/Mac-Nerd/) - Patchomator]

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Mac-Nerd/patchomator/1.1)

Un script de gestión para Installomator. https://github.com/Mac-Nerd/patchomator

 - [Mostrar el progreso y otros mensajes a través de swiftDialog, si está instalado. ](https://github.com/Mac-Nerd/patchomator#swift-dialog)

### [Actualización automática de la aplicación](https://github.com/App-Auto-Patch/App-Auto-Patch)

![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/App-Auto-Patch/App-Auto-Patch)

App Auto-Patch combina el descubrimiento de aplicaciones instaladas localmente, la integración con Installomator y ventanas de diálogo intuitivas de swiftDialog para automatizar la gestión de actualizaciones de aplicaciones en computadoras Mac.

App Auto-Patch fue desarrollado basándose en un concepto similar al proyecto Patchomator, y una parte importante de su código fue tomado de este último.

## Proyectos adicionales que se basan en swiftDialog o que lo utilizan de alguna otra manera

### [Scott Kendall](https://github.com/ScottEKendall/)

 - [Scripts de Jamf Pro]](https://github.com/ScottEKendall/JAMF-Pro-Scripts)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/ScottEKendall/JAMF-Pro-Scripts/main)

### [Richard Purves](https://github.com/franton/)

 - [Implementación rápida ](https://github.com/franton/SwiftDeploy) Método de implementación sin intervención manual para Jamf Pro y SwiftDialog

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/franton/SwiftDeploy/main)

### [Graham Pugh](https://github.com/grahampugh/)

 - [Borrar e instalar](https://github.com/grahampugh/erase-install) - Reinstalar macOS directamente desde la partición del sistema utilizando `startosinstall`

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/grahampugh/erase-install/main)

### [Dan Snelson](https://github.com/dan-snelson/dialog-scripts)

 - [Mostrar mensaje](https://github.com/dan-snelson/dialog-scripts/tree/main/Display%20Message): Utilice los parámetros de los scripts de políticas de SwiftDialog y Jamf Pro para mostrar fácilmente mensajes atractivos para los usuarios finales.

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/dan-snelson/dialog-scripts/main)

 - [Configuración de su Mac](https://github.com/setup-your-mac/Setup-Your-Mac): Simplifique la configuración inicial del dispositivo utilizando swiftDialog y los eventos de personalización de políticas de Jamf Pro

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/setup-your-mac/Setup-Your-Mac/main)


### [Adam Codega](https://github.com/acodega/dialog-scripts)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/acodega/dialog-scripts/main)

 - [MDM Apps Deploy](https://github.com/acodega/dialog-scripts/blob/main/MDMAppsDeploy.sh) - Display a Dialog with a list of applications and indicate when they've been installed

 - [Nombre de la computadora, según la entrada](https://github.com/acodega/dialog-scripts/blob/main/computerNameFromInput.sh)

 - [Verificación e instalación de swiftDialog](https://github.com/acodega/dialog-scripts/blob/main/dialogCheckFunction.sh): Comprueba la versión actual de swiftDialog que está instalada e instala los componentes necesarios.]

### [Jon Crain](https://github.com/joncrain/)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/joncrain/swiftDialog-scripts/main)

 - [swiftDialog scripts](https://github.com/joncrain/swiftDialog-scripts): Scripts que utilizan [swiftDialog](https://github.com/bartreardon/swiftDialog) para diversas tareas.

 - [Flujo de trabajo DEP/ADE](https://github.com/joncrain/swiftDialog-scripts/tree/main/depnotify-swiftdialog): Flujo de trabajo de tipo DEPnotify con selección opcional de software.

 - [Aviso de FileVault](https://github.com/joncrain/swiftDialog-scripts/tree/main/fv_alert-swiftdialog): Mensaje de alerta que se muestra cuando Crypt detecta un problema con el almacenamiento de claves.]

 - [Aviso del Asistente de Migración](https://github.com/joncrain/swiftDialog-scripts/tree/main/ma_alert-swiftdialog): mostrar una notificación al usuario final cuando se inicia el Asistente de Migración]

 - [Software Update](https://github.com/joncrain/swiftDialog-scripts/tree/main/nudge-swiftdialog) - Nudge para swiftDialog. Basado de forma aproximada en [Nudge](https://github.com/macadmins/nudge)

 - [Alerta de inscripción a MDM ](https://github.com/joncrain/swiftDialog-scripts/tree/main/umad-swiftdialog) - Conceptualizada a partir de [umad](https://github.com/macadmins/umad) de Erik Gomez.

### [James Smith](https://github.com/smithjw/)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/smithjw/speedy-prestage-pkg/main)

 - [swiftDialog speedy-prestage](https://github.com/smithjw/speedy-prestage-pkg/tree/feature/swiftDialog) - Script de inscripción de Jamf]

### [Thijs Xhaflaire](https://github.com/txhaflaire/)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/txhaflaire/DiskEncrypter/main)

 - [Cifrar dispositivos de almacenamiento extraíbles sin cifrar ](https://github.com/txhaflaire/DiskEncrypter) - Cifrar dispositivos de almacenamiento extraíbles sin cifrar

### [Second Son Consulting](https://www.secondsonconsulting.com/)

 - [Solución básica](https://github.com/SecondSonConsulting/Baseline): Una solución de configuración automática e independiente de cualquier plataforma de gestión de dispositivos móviles (MDM) para macOS.]

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/SecondSonConsulting/Baseline/main)

 - [Renew](https://github.com/SecondSonConsulting/Renew): Un script para macOS que anima a los usuarios a reiniciar sus estaciones de trabajo

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/SecondSonConsulting/Renew/main)

 - [Ejemplos de swiftDialog](https://github.com/SecondSonConsulting/swiftDialogExamples)

   ![Última modificación en GitHub (rama)](https://img.shields.io/github/last-commit/SecondSonConsulting/swiftDialogExamples/main) - ejemplos de scripts para demostrar las diferentes funcionalidades de [SwiftDialog](https://github.com/bartreardon/swiftDialog)

### [Martin Piron](https://github.com/ooftee)

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/ooftee/dialog-starterkit/main)

 - [Kit de inicio de diálogo ](https://github.com/ooftee/dialog-starterkit): una forma sencilla e intuitiva de seleccionar e instalar un conjunto de aplicaciones

### [PezzaD84](https://github.com/PezzaD84)

 - [Ensamblar](https://github.com/PezzaD84/Assemble): Script para configurar dispositivos utilizando swiftDialog.]

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/PezzaD84/Assemble/main)

 - [JAMF-LAPS-UI](https://github.com/PezzaD84/JAMF-LAPS-UI): Una interfaz de usuario para la función integrada de JAMF LAPS

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-UI/main)

 - [JAMF-LAPS-Configurator](https://github.com/PezzaD84/JAMF-LAPS-Configurator): Un script de Bash para ayudar a configurar JAMF LAPS

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/PezzaD84/JAMF-LAPS-Configurator/main)

 - [Información del dispositivo](https://github.com/PezzaD84/Device-Information): Un script de bash para mostrar información del dispositivo en una interfaz de usuario sencilla

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/PezzaD84/Device-Information/main)

### [Andrew Barnett](https://github.com/AndrewMBarnett)

 - [Reinscripción](https://github.com/AndrewMBarnett/ReEnroll): Automatice el proceso de reinscripción de dispositivos en Jamf Pro

   ![Último commit de GitHub (rama)](https://img.shields.io/github/last-commit/AndrewMBarnett/ReEnroll/main)

### [Microsoft](https://github.com/microsoft)

 - [Implementación de una pantalla de bienvenida con Swift Dialog e Intune.](https://github.com/microsoft/shell-intune-samples/tree/03b181ca16c8a8f677a19a3a45f5943fb36e69b9/macOS/Config/Swift%20Dialog)

   ![Última actualización en GitHub (rama)](https://img.shields.io/github/last-commit/microsoft/shell-intune-samples/master) - Pantalla de inicio para Intune