---
title: Customising the Message Area
description: Learn how to set and customize the message text, font properties, and positioning in swiftDialog
---

Use the `-m` or `--message` command line option to specify what you would like in the Dialog title area.

Example:

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

The message area can take up either 2/3 of the width of the Dialog window or the full width if the icon area is not being shown

Messages will line wrap if they go beyond the width of the display area and will scroll if they go beyond the total available display area.


![image](https://user-images.githubusercontent.com/3598965/171407698-775b75a8-07ad-462a-a191-55a5ec674e22.png)

![image](https://user-images.githubusercontent.com/3598965/171408153-2e7175d1-fc28-4996-9913-49af6205bd99.png)

## Message positioning

`--messagealignment` and `--messageposition` let you position where in the dialog the message appears. Useful for creating dialogs with the message centred vertically and horizontally.

![image](https://user-images.githubusercontent.com/3598965/192680013-da9e86cb-c3a0-4257-9a0c-f9f137eb487e.png)

## Modifying message font, colour, size and alignment

`--alignment [left | centre | center | right]`

Set the message alignment. Default is 'left'

`--messagefont <text>`

Lets you modify the message text of the dialog. Can accept up to three parameters, in a comma seperated list, to modify font properties.

`color,colour=<text><hex>`

> `<text>` can be any of the standard Apple colours black, blue, gray, green, orange, pink, purple, red, white, yellow. The default if option is invalid is system primary colour (usually black if in light mode or white if in dark mode)

> `<hex>` is specified in hex format, e.g. #00A4C7

`size=<float>` accepts any float value (e.g. 15.7, 20, 32.0)

`name=<fontname>` accepts a font name or family. list of available names can be determined from the macOS Font Book app or alternately, run dialog with the `--listfonts` parameter and it will print out a lost of font families and font names

**CAUTION** : Results may be unexpected when mixing font names and weights with markdown. For best results, only specify a font family, that way when using **bold** or _italics_, the markdown renderer will be able to use the correct font style. If you are specific about a font name, e.g. `name=Arial-BoldMT` then markdown will not render any additional modifications if they are not present in the font definition.

`weight=<weight> accepts one of thin, light, regular, medium, heavy or bold. The default is regular

Example1: `"colour=#00A4C7,weight=medium,size=40"`

![image](https://user-images.githubusercontent.com/3598965/184132608-43220184-d315-4a69-85c6-4a41adac2cb7.png)

Example2: `"name=Chalkboard,colour=#FF3012,size=25"`

![image](https://user-images.githubusercontent.com/3598965/184132857-81bf56db-4ca4-492a-a45e-ada971cd8b68.png)