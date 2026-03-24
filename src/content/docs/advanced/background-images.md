---
title: Background Images
description: Adding background images and watermarks to dialog windows
---

## Background Images

Images can be displayed in the background as part of the main dialog window which can be used to imprint a watermark or other image behind the regular dialog content.

![image](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

Backgrounds can be controlled with the following controls:

### `--background`

```
-bg, --background <file | url | colour= >
```

Displays the selected file as a background image. If the image is larger than the default dialog size (820x380) and no window size options are given (specifically window height), the dialog window height will be adjusted so the image fills the entire window width, 820 by default or if specified using `--width`

Alternatively a solid colour can be specified using the `colour=` prefix. The colour can be specified as a hex value or a named colour.

e.g. `--background colour=red` or `--background colour=#ff0000`

By default a subtle gradient overlay is applied to solid colours. Append `,nogradient` to disable it:

`--background colour=red,nogradient`

A linear gradient can be specified using the `gradient=` prefix. Supply two or more comma-separated colours, and optionally set the direction with `:angle=<degrees>`:

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

Angle conventions: `0` = bottom-to-top, `90` = left-to-right (default), `180` = top-to-bottom, `270` = right-to-left.

If only one colour is supplied to `gradient=`, the result is identical to `colour=`.

```


### `--bgalpha`

```
-ba, --bgalpha <number>
```

Sets the alpha or transparency of the background layer. Can be any number between `0` (fully transparent) and `1` (fully opaque). Default value is `0.5`



### --bgposition

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

Positions the background image in the window. Works best if the image dimensions are smaller than the main dialog window such as a company logo. Default position is `centre`


### --bgfill

```
-bf, --bgfill [fill | fit]
```

Tells dialog how to display the image within the window frame

`fill` resizes the image to fill the entire window. Image will be truncated if necessary
`fit` resizes the image to fit the window but will not truncate which may result in letterboxing of non transparent areas (if using a PNG image source)

Default is `none` which will display the image at the actual image resolution