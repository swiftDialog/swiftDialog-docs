---
title: 背景图片
description: 为对话窗口添加背景图片和水印
translationSynced: 2026-11-25T05:29:39+00:00
---

## 背景图片

图像可以作为背景显示在主对话窗口中，这可以用来在常规对话内容的背后添加水印或其他图像。

![图片](https://user-images.githubusercontent.com/3598965/171406081-8e9e5363-56fc-46f9-baa8-ff881a4a4af3.png)

背景可以通过以下控件进行调整：

### `--background`

```
-bg, --background <file | url | colour= >
```

将选定的文件显示为背景图片。如果图片尺寸大于默认对话框大小（820x380），并且没有指定窗口大小选项（特别是窗口高度），对话框窗口的高度将自动调整，以使图片填充整个窗口宽度，默认宽度为820，或者根据`--width`中指定的数值。

另一种方法是，可以使用 `colour=` 前缀来指定一种纯色。 颜色可以指定为十六进制值或颜色名称。

例如：`--background colour=red` 或 `--background colour=#ff0000`。

默认情况下，会为纯色添加一种微妙的渐变效果。要禁用此效果，请在设置中添加 `,nogradient`。

`--background colour=red,nogradient`

可以使用 ``gradient=`` 前缀来指定线性渐变。 需提供两个或更多个用逗号分隔的颜色值，并且可以选择使用 ``:angle=<degrees>`` 来设置方向。

```sh
--background "gradient=red,blue"
--background "gradient=red,orange,yellow:angle=135"
```

角度约定：`0` = 从下到上；`90` = 从左到右（默认）；`180` = 从上到下；`270` = 从右到左。

如果只提供一种颜色给`gradient=`，结果将与`colour=`完全相同。


### `--bgalpha`

```
-ba, --bgalpha <number>
```

设置背景图层的透明度。可以是介于 `0` (完全透明) 和 `1` (完全不透明) 之间的任意数值。默认值为 `0.5`。


### --背景位置

```
-bp, --bgposition [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]
```

将背景图片放置在窗口中。如果图片尺寸小于主对话窗口，效果最佳，例如公司logo。默认位置是 `centre`。


### --bgfill

```
-bf, --bgfill [fill | fit]
```

该设置控制对话框如何将图像显示在窗口框架内。

`fill` 会将图像调整为填充整个窗口。如果需要，图像将被截断。`fit` 会将图像调整为适合窗口，但不会截断，这可能会导致非透明区域出现信箱效应（如果使用 PNG 图像源）

默认设置是`none`，这将以图像的实际分辨率显示图像。

## 屏幕背景 - `--screenbackground`

```
--screenbackground <file | url>
```

显示指定的图像，以**全屏模式，位于对话框窗口的后面**——这与`--background`不同，后者位于_对话框窗口的内部_。所有其他对话框功能仍然可用，但用户无法与任何其他应用程序进行交互，直到 swiftDialog 退出（类似于`--blurscreen`，但显示图像而不是模糊效果）。

```sh
dialog --screenbackground /path/to/wallpaper.jpg
dialog --screenbackground https://example.com/background.png
```