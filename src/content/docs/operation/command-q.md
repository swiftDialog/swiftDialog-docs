---
title: Modifying Command+Q Behaviour
description: Customizing keyboard shortcuts for quitting dialogs
---

In swiftDialog 1.10.2 and newer, the command `--quitkey <char>` which will re-map `command+q` to `command +<char>`

e.g. `--quitkey x` will disable command+q from quitting the dialog, but allow `command+x`.

In addition, if a dialog is quit using a command+<char> action, the exit code will be `10` allowing for any action to be taken if detected.

The shortcuts `command+w`, `command+m` and 'command+n` are also disabled by default and cannot be re-assigned.