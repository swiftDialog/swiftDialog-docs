---
title: jamfHelper Support
description: Using swiftDialog as a drop-in replacement for jamfHelper
---

Dialog now has the ability to accept a basic subset jamfHelper format command line options with the new `--jh` flag.

This makes it easier to implement into existing workflows and scripts by substituting the call to `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` with `/usr/local/bin/dialog --jh`

Using the flag will instruct dialog to convert jamfHelper options into equivalent dialog options. Not all options are supported. Standard dialog options that have no equivalent in jamfHelper are still available, e.g. `--width`, `--height` and `--image`.

<br/>

## Features and behaviour

***
### Implemented

#### `-windowType [hud | utility | fs]`

`hud` and `utility` are ignored. `fs` is converted into dialog `--fullscreen` and will display in dialogs full screen view

#### `-windowPosition [ul | ll | ur | lr]`

Positions window in the upper right, upper left, lower right or lower left of the user's screen
This is the only feature that is not currently part of dialogs standard options but is implemented for jamfHelper compatibility.

#### `-title "string"`
Converted to `--title`

Sets the window's title to the specified string

#### `-heading "string"` and `-description "string"`
Converted to `--message`

Both `-heading` and `-description` are merged into dialogs `--message` option. `-heading` is converted into a markdown heading 4 `####` then a blank newline followed by `-description`

#### `-icon path`
Converted to `--icon`

If not present, forces dialogs `--hideicon` option to match jamfHelpers behaviour of displaying with no idon if one is not specified

#### `-button1 "string"`
Converted to `--button1text`

**_Changed behaviour:_** Dialog always shows the default button which is different to how jamfHelper works. The default button text is `OK`

#### `-button2 "string"`
Converted to `--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
Converted to `--alignment`

The only options implemented are `right` `centre` and `left`

#### `-timeout int` and `-countdown`
Converted to `--timer`.

`-countdown` is always implied as dialog always shows the timer bar
timeout with no timer bar is not implemented in dialog.

<br/>

***
### Not implemented

#### `-defaultButton [1 | 2]`
Default button is always button 1

#### `-cancelButton [1 | 2]`
Cancel button is always button 2 (if displayed)

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`