---
title: Vordefinierte Variablen
description: Die Verwendung von dynamischen Variablen für Systeminformationen in Dialogen
translationSynced: 2026-11-20T09:59:42+00:00
---

## Vordefinierte Variablen

swiftDialog enthält jetzt integrierte Variablen, die mit hostspezifischen Informationen gefüllt werden. Integrieren Sie diese in Ihre Textzeichenketten als `{variablename}`

Die enthaltenen Variablen sind:

    {computername}  - hostname of the computer
    {computermodel} - computer model, e.g. "Mac mini (2023)"
    {serialnumber}  - serial number
    {username}      - current username, e.g. `johndoe`
    {userfullname}  - full name, e.g. `John Doe`
    {osversion}     - macOS version, e.g. `14.4.1`
    {osname}        - macOS name, e.g. `Sonoma`

Alle Umgebungsvariablen können ebenfalls auf diese Weise abgerufen werden

    dialog --icon computer --title "{computermodel}" --message "Running {osname} {osversion}" --style centred

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">