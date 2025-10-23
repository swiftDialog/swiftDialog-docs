---
title: What's New
description: Recent features and updates in swiftDialog
---

## swiftDialog 2.5.6

## Fixes:

 - Fixed an issue where specifying an icon from json required the icon to be in an array even if there was a single icon. fixes #493
 - Notification click closes dialogs in v2.5.5 #499 
 - Update dialog script version message when no user logged in by @HowardGMac in https://github.com/swiftDialog/swiftDialog/pull/510
 - Use whole path for scutil (resubmit) by @MikeRich88 in https://github.com/swiftDialog/swiftDialog/pull/515
 - Added trailing padding to helpimage
 - Adds key authorisation to sending notifications if one is required #485 
 - fix missing options for `--textfield` in help #485 

## Contributions:

### Additional options for working with notifications

 - Adds ability to set an identifier for a notification, allowing you to easily replace a notification with an updated one. Also the ability to remove a specific notification by identifier or all notifications.

_Example:_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

Thanks to @chrisgrande

### Added buttonsize as a command line and control file variable

 - Support for mini, small and large button button sizes, using the built in macOS sizes. The button size will default to the current value of regular if not specified or not valid.
 - Support for button size to the builder mode for testing and JSON generation.

Button style is applied to `button1`, `button2` and the info button. It is also applied in the normal and stacked button layout.

 It does not scale the help button, which is a fixed size.

Examples:

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

Thanks to @k2graham

### Options to hide and show the dialog window from the command file

 - Added `hide:` and `show:` commands to the list of command file commands to hide and show windows. This does not prevent window updates from occurring while a window is hidden.

Thanks to @fabienconus

