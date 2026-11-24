---
title: Variables predefinidas
description: Utilizar variables dinámicas para mostrar información del sistema en cuadros de diálogo
translationSynced: 2026-11-24T22:59:17+00:00
---

## Variables predefinidas

swiftDialog ahora contiene variables integradas que se completarán con información específica del servidor. Inclúyalas en sus cadenas de texto como `{variablename}`

Las variables incluidas son:

    {computername}  - nombre del host del equipo {computermodel} - modelo del equipo, por ejemplo, "Mac mini (2023)" {serialnumber}  - número de serie {username}      - nombre de usuario actual, por ejemplo, `johndoe` {userfullname}  - nombre completo, por ejemplo, `John Doe` {osversion}     - versión de macOS, por ejemplo, `14.4.1` {osname}        - nombre de macOS, por ejemplo, `Sonoma`

Las variables de entorno también se pueden acceder de esta manera

    dialogo --icono computadora --título "{computermodel}" --mensaje "Ejecutando {osname} {osversion}" --estilo centrado

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">