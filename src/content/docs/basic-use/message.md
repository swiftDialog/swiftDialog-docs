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


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

## Message positioning

`--messagealignment` and `--messageposition` let you position where in the dialog the message appears. Useful for creating dialogs with the message centred vertically and horizontally.

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## Modifying message font, colour, size and alignment

`--alignment [left | centre | center | right]`

Set the message alignment. Default is 'left'

`--messagefont <text>`

Lets you modify the message text size and colour.

`color,colour=<text><hex>`

> `<text>` can be any of the standard Apple colours black, blue, gray, green, orange, pink, purple, red, white, yellow. The default if option is invalid is system primary colour (usually black if in light mode or white if in dark mode)

> `<hex>` is specified in hex format, e.g. #00A4C7

`size=<float>` accepts any float value (e.g. 15.7, 20, 32.0)


Example: `"colour=#00A4C7,size=40"`

<img width="400" alt="image" src="/images/messagefont.png" />
