---
title: Command File
description: Updating Dialog with new content dynamically using command files
---

Some dialog content can be updated on the fly after it has been launched. This is facilitated by sending commands to a command file which Dialog will read and interpret.

<hr />

Dialog will need to be launched in the background in order for you to be able to send commands to it (assuming you're calling and commanding dialog from the same script. To do this and allow time for dialog to initiate before sending commands, use the following:

`/usr/local/bin/dialog & sleep 0.1`

This will launch dialog, background it and sleep for 100 milliseconds which should be enough time to avoid any race conditions.

The default command file is `/var/tmp/dialog.log` but a custom command file can be set using the `--commandfile` argument followed by a path where the command file will be written to and read from.

e.g. `dialog --commandfile /var/tmp/custom_command_file.log`

Commands can be sent in the following manner:

`/bin/echo "<command>: <value>" >> /var/tmp/dialog.log`

## Available Commands

Commands take the same format as they would if used on the command line or via json input

|Command &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Effect|
|---|-|
|`title: <text>`             |Updates the dialog title with the specified `<text>`|
|`title: none`.            |Hides the title area|
|`message: (+)<text>`            |Updates the dialog title with the specified `<text>`  <br>For inserting newlines into the message you can use a `<br>` tag.  <br>You can also append to an existing message by prepending message content with a `+`, e.g. `message: + Additional Content` and the contents will be added to the end of an existing message.|
|`alignment: [left \| center \| right]`|Sets the message alignment|
|`image: <path/url>`          |Displays the selected image|
|`imagecaption: <text>`       |Displays the specified text underneath any displayed image|
|`progress: <int>/<text>`     |When Dialog is initiated with the `--progress` command line option, this will update the progress value<br />If an integer value is sent, this will move the progress bar to that value of steps<br />Other options are: <br /> * `increment` - increments the progress by one<br /> * `reset` - resets the progress bar to 0<br /> * `complete` - maxes out the progress bar|
|`progress: hide/show`    |Hides or shows the progress bar |
|`progresstext: <text>`       |Will update the label associated with the progress bar|
|`helpmessage: <text>`|Update help message content|
|`list: <text/csv>`           |Create a list from the provided comma separated items|
|`list: clear`           |Clears the list and removes it from display|
|`listitem: <item>: [<text>/wait]` |Update the named item with the additional status text `<text>` or display a spinning wait cursor|
|`listitem: add, title: <text>[, status: <status>, statustext: <text>]` |Add a new item to the end of the current list with the specified title and optionally status and status text|
|`listitem: delete, title: <text>` |Delete an item by name|
|`listitem: delete, index: <index>` |Delete an item by index number (starting at 0)|
|`button1: [disable/enable]`  |Will enable or disable the default button|
|`button2: [disable/enable]`  |Will enable or disable button 2|
|`button1text: <text>`        |Changes the button 1 label to the value in `<text>`|
|`button2text: <text>`        |Changes the button 2 label to the value in `<text>`|
|`buttonsize: [mini \| small \| regular \| large]`|Set the button size|
|`infobuttontext: <text>`     |Changes the info button label to the value in `<text>`|
|`infotext: <text>`|Set the info text (not visible if infobutton is also in use)|
|`infobox: <text>`            |Update the content in the info box  <br>For inserting newlines into the content you can use a `<br>` tag.  <br>You can also append to existing content by prepending the text with a `+`, e.g. `infobox: + Additional Content` and the text will be added to the end of any existing infobox content.|
|`icon: <path/url/SF Symbol>`           |Changes the displayed icon|
|`icon: <centre/center/left/default>`           |Moves the icon being shown to the centre or to the default location|
|`icon: none`           |Hide the icon|
|`icon: size: <num>`           |Changes the size of the displayed icon to the requested size.|
|`iconalpha: <float> (0.0 -> 1.0)`|Set the transparancy/alpha value. Accepts float valuse between 0.0 and 1.0|
|`overlayicon: <path/url/SF Symbol>`|Set the overlay icon|
|`bannerimage: <path/url>`|Set the banner image|
|`bannertext: [enable \| disable \| shadow \| <text>]`|Enable banner text mode, text shadow or set the title value. If a text value is not set, `title:` value is used|
|`width: <num>`           |Changes the width of the window maintaining the current position.|
|`height: <num>`           |Changes the height of the window maintaining the current position.|
|`position: <position>`           |Changes the window position. One of `top`, `bottom`, `left`, `right`, `centre` or a combination (e.g. `topright`)|
|`webcontent: <url>`           |Display content from the specified URL. send `webcontent: none` to reset|
|`video: <path/url>`           |Display a video from the specified path or URL. send `video: none` to reset|
|`blurscreen: [disable/enable]`                 |Activates the blur window layer|
|`activate:`                |Activates the dialog window and brings it to the forground.|
|`hide:`|Hides the dialog window|
|`show:`|Unhides a hidden dialog window|
|`quit:`                      |Quits dialog with exit code 5|

## Additional Command line options

The following command line options are also available for use

|Command &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Action|
|-|-|
|`--commandfile <path>`|Lets you provide an alternate path to read status commands from. The default is `/var/tmp/dialog.log`|
|`--progress <int>`|Shows a progress bar with `<int>` number of increments.<br /><br />The progress bar is updated by sending `progress: ...` commands to the status log file.<br />e.g. if you launch dialog with `--progress 100` then sending a `progress: 20` command will set the progress bar 20 increments<br /><br />Specifying no value for `<int>` will start the progress bar in indeterminate mode with a default step count of 100 |
|`--blurscreen`|Will blur out the screen contents behind the dialog window making them unavailable|
|`--button1disabled`|Will disable button1 on launch|