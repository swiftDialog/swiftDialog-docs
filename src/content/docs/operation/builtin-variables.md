---
title: Built-in Variables
description: Using dynamic variables for system information in dialogs
---

## Built in variables

swiftDialog now contains built in variables that will populate with host specific info. Include into your text strings as `{variablename}`

The included variables are:

    {computername}  - hostname of the computer
    {computermodel} - computer model, e.g. "Mac mini (2023)"
    {serialnumber}  - serial number
    {username}      - current username, e.g. `johndoe`
    {userfullname}  - full name, e.g. `John Doe`
    {osversion}     - macOS version, e.g. `14.4.1`
    {osname}        - macOS name, e.g. `Sonoma`

Any environment variables are also accessable in this way

    dialog --icon computer --title "{computermodel}" --message "Running {osname} {osversion}" --style centred

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">