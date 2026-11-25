---
title: 横幅图片
description: 在对话框的顶部显示图像，可以选择性地添加标题文字覆盖在图像上
translationSynced: 2026-11-25T05:27:49+00:00
---

使用 `-n` 或 `--bannerimage` 命令行选项，可以指定一个图像，该图像将显示在对话框的顶部。

用途：

`--bannerimage <file | url | colour= >`

使用横幅图片会禁用图标图像区域的显示。这等同于使用 `--hideicon` 选项。

## 基本使用方法

Dialog 窗口支持 PNG 和 JPG 格式的图片，并将指定的图片显示在横幅区域。横幅图片的最高高度为 150pt，并且横跨整个对话窗口的宽度。 配合 `-s` 或 `--small` 选项时，横幅图片的高度限制为 100pt。

可以使用任何尺寸的图片。 图片显示区域会根据您选择的横幅图片的大小进行调整，但最大高度为150个像素。

<img width="727" alt="Banner Image Small" src="https://user-images.githubusercontent.com/3598965/112744135-fcb77c00-8fe8-11eb-8fac-437c86872eae.png">

可以使用 `--bannerheight` 选项来指定特定的高度。这将覆盖默认的高度设置。

此外，可以使用 `colour=` 前缀来指定纯色。颜色可以指定为十六进制值或颜色名称。

示例：

`--bannerimage colour=red` 或者 `--bannerimage colour=#ff0000`

默认情况下，纯色背景会应用一种微妙的白色到颜色到黑色的渐变效果。可以通过添加 `,nogradient` 来禁用此效果。

`--bannerimage colour=red,nogradient`

### 渐变横幅

可以使用 ``gradient=`` 前缀来指定线性渐变。 需提供两个或更多个用逗号分隔的颜色值，并且可以选择使用 ``:angle=<degrees>`` 来设置方向。

```sh
--bannerimage "gradient=red,blue"
--bannerimage "gradient=red,orange,yellow:angle=135"
```

角度约定：`0` = 从下到上；`90` = 从左到右（默认）；`180` = 从上到下；`270` = 从右到左。

如果只提供一种颜色给`gradient=`，结果与`colour=`（从白色到指定颜色再到黑色渐变）完全相同。

## 横幅区域内的标题文字

`--bannertitle`

使用此命令，您可以选择在横幅中显示标题文本，使用 `--bannertitle` 选项。这样会默认将文本颜色设置为白色，但可以通过 [标题字体自定义](/zh-hans/basic-use/title/) 选项进行修改。

您可以将其作为 `--title` 的选项使用，也可以传入一个字符串作为标题显示。如果 `--title` 和 `--bannertitle` 都有字符串参数，`--bannertitle` 将优先。

所有修改器都适用于横幅标题文本，包括`--titlefont`、`shadow`、`colour`、`size`、`weight`、`alignment`和`offset`。

`--titlefont shadow=1` 在文字下方添加一个阴影效果。

如果同时设置了`--subtitle`，字幕将显示在标题下方，位于横幅区域内，并继承相同的字体，但字体大小会缩小。

![图片](https://user-images.githubusercontent.com/3598965/216027666-5e4433d5-9e1e-4590-b34d-8d7943cbe5a5.png)