---
title: Banner Images
description: Displaying images at the top of dialogs with optional title text overlay
---

Use the `-n` or `--bannerimage` command line option to specify an image to use at the top of the dialog.

Use:

`--bannerimage <file | url | colour= >`

**Using a banner image will disable the display of the icon image area. This is the equivalent of using the `--hideicon` option**

## Basic Use

Dialog accepts images in png and jpg formats and displays the specified image in the banner area. The banner image is at most 150pt high and spans the width of the dialog window. In conjunction with the `-s` or `--small` option the banner image is limited to 100pt high

Any size image can be used. The image display area will adjust to the size of the banner image you wish to use, up to a maximum height of 150 points.

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

A specific height can be specified using the `--bannerheight` option. This will override the default height.

Additionally, a solid colour can be specified using the `colour=` prefix. The colour can be specified as a hex value or a named colour.

Example:

`--bannerimage colour=red` or `--bannerimage colour=#ff0000`

## Title text within the banner area

`--bannertitle`

Using this command you can opt to display title text within the banner using the . Doing so forces the text colour to white by default, however this can be changed with [title font customization](/basic-use/customizing-title#customising-title-font-properties) modifiers.

You can use it as an option to `--title` or you can pass in a string to display as the title. If both `--title` and `--bannertitle` have string arguments, `--bannertitle` will take precedence.

An additional `--titlefont` modifier is available with text over a banner image.

`--titlefont shadow=1` will place a drop shadow underneath the text and can be used in combination with other title font arguments either as a command line argument or as json.

![image](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)