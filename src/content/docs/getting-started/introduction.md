---
title: Getting Started with swiftDialog
description: Introduction to swiftDialog, a modern macOS dialog utility for administrators
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialog Welcome Example](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

swiftDialog's purpose is intended as a helper utility for macadmins to use via script to display a dialog to present information to a user and report the action the user took which can be later used for more script processing or simply used to display some piece of information.

swiftDialog accepts input from the command line with one or more [command line options](/advanced/command-line-options) to tell swiftDialog what to display and how to display it.

There are a number of options available that can be used to customise what you want to show that can range from the very simplistic informational display to more complex processing with text entry, dropdown list, image display and more.

## Running swiftDialog

The **.pkg** installer from the [releases](https://github.com/swiftDialog/swiftDialog/releases) page will install swiftDialog to `/usr/local/bin/dialog` which should also be in the default `$PATH` on macOS

To call dialog from your script, you can use the full path or rely on `$PATH`

```bash
$ dialog --title ...
```

or

```bash
$ /usr/local/bin/dialog --title ...
```

At the most basic level, dialog can simply use the `--title` and `--message` command line options to present a dialog with the desired message.

swiftDialog can perform much more than that though and you should read the [Command Line Options](/advanced/command-line-options) page for a full list of options available or call dialog with the `--help` option.

## Quick Links

### Basic Features
- [Customising swiftDialog's Title](/basic-use/title)
- [Customising swiftDialog's Message Display](/basic-use/message)
- [Customising the image displayed in swiftDialog's Icon area](/basic-use/icon)
- [Adding a Banner Image](/advanced/banner-images)
- [Customising the Buttons and Button Behaviour](/basic-use/buttons)

### Advanced Features
- [Info Box](/advanced/info-box)
- [Banner Images](/advanced/banner-images)
- [Help Message](/operation/help-message)
- [Dropdowns and Radio buttons](/advanced/select-lists)
- [Text Entry](/advanced/textfields)
- [Checkboxes](/advanced/checkboxes)
- [Timer with Progress Bar](/advanced/timer-progress)
- [Window Size and Behaviour](/advanced/window-size)
- [Full Screen Mode](/advanced/full-screen)
- [Presentation Mode](/advanced/presentation)
- [Lists of items](/advanced/item-lists)
- [System Notifications](/advanced/notifications)
- [Modifying CMD+Q](/operation/command-q)
- [Built-in Variables](/operation/builtin-variables)

## Support

swiftDialog was started in part as a learning exercise in how to write applications using SwiftUI and partly to satisfy a need for a way to communicate information to mac users in a style that I liked.

Support can be offered by [creating an issue](https://github.com/swiftDialog/swiftDialog/issues). Feature requests are also welcome.

## Contact

You can reach the author over at the [Macadmins slack](https://www.macadmins.org/slack) in the #swiftdialog channel (username @bartreardon - usually hanging out in #anzmac) however please limit any support queries or general questions to github, at the very least so your problem can be tracked and addressed. Thank you 😃