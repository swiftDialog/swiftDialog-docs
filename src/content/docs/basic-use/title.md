---
title: Customising the Title
description: Learn how to set and customize the title text and font properties in swiftDialog
---

## Setting Title Text

use the `-t` or `--title` command line option to specify what you would like in the Dialog title area.

Example:

`--title "An Important Message"`

`-t "An Important Message"`

The title area is a fixed width bold area at the top of the Dialog window. Text longer than the size of the window can display will be truncated

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## Customising Title Font Properties

Use the `--titlefont` command line option to set title font properties.

Font properties are expressed in the form of `property=value` and multiple properties are separated by a comma

Properties available for modification are:
 * `colour=<hex_value>` (alternatly `color=<hex_value>`)
   * specified in hex format, e.g. #00A4C7
 * `size=<float>`
   * accepts any float value, e.g. 30, 65, 72.3
 * `weight=<text>`
   * accepts any of thin, light, regular, medium, heavy or bold (default)
 * `name=<fontname>`
   * accepts a font name or family. list of available names can be determined with `--listfonts` or by consulting the macOS Font Book application.

 > **CAUTION :** Be careful when mixing font names and weights. When specifying a font or font family by name, certain weights may not be available. If this occurs, the font weight specified will be ignored.

You can utilise one or more and the order in which they are specified is not important. For instance if you only wished to modify the size, you could use the following:

`--titlefont "size=60"`

#### Hiding the title area

Use the keyword `none` to hide the title area. This will remove the title bar and the horizontal separator line

e.g. `--title none`



### Usage

Example 1: `--titlefont "colour=#00A4C7,weight=light,size=60"`

This example sets the colour to the value `#00A4C7`, weight to `light` and the font size to `60` and will appear like so:

<img width="400" alt="image" src="/images/titlefont1.png" />

Example 2: `--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

This example sets the colour to the value `#D054A0 `, size to `40` and use the font name "Chalkboard-Bold":

<img width="400" alt="image" src="/images/titlefont2.png" />