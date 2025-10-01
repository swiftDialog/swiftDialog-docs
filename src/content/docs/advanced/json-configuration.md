---
title: JSON Configuration
description: Using JSON to specify Dialog options for complex configurations
---

Instead of using numerous command line options for construction complex dialogs, you can use the `--jsonfile` or `--jsonstring` options to define parameters.

The JSON format uses the same options as specified on the command line with a few exceptions and considerations.

**Note:**
 - **Command line options can be used in conjunction with JSON but any options defined in JSON will take precedence.**
 - **To support literal `\n` characters in the message text, `--jsonstring` will expect JSON input to be on one continuous line**

Example:

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## Differences from command line options

Options that can be used multiple times can be entered in as an array.

For example to specify multiple images and image captions, use a `image` array with `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

Checkboxes can be specified as check and/or disabled. The default is `"disabled" : false` and doesn't need to be specified

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

For multiple `textfield` options, specify a single textfield with the names of the fields as an array

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### Strings and boolean values

Most options will be passed through as string values requiring quotes for the specified values. Some values can be specified as a boolean value though (`true` or `false`, without quotes). Options that take a boolean value are:

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### Options not available from json

There are a number of options that are not available to be used from JSON as they do not make sense in a deployed context. They are:

* `--jh` - used as a drop in replacement to accept JamfHelper command line options.
* `--listfonts` - used during prototyping to display a list of fonts available
* `--help` - displays help text and exits. Used during prototyping
* `--demo` - displays a dialog using nothing but the default settings. Used during prototyping
* `--version` - outputs dialog version info and exits.
* `--showlicense` - prints license info and exits
* `--coffee` - prints coffee info and exits

## Example: generating json in python and passing in as a file or a string

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```