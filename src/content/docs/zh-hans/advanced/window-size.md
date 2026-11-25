---
title: 窗口大小和行为
description: 控制对话窗口的位置、大小和外观
translationSynced: 2026-11-25T05:49:03+00:00
---

默认情况下，对话框窗口会显示在屏幕中央，并且无法移动。其他窗口可以显示在对话框窗口的上方。 您可以通过以下命令行选项来修改这种默认行为。

这两种方案可以独立使用，互不影响。

## 窗口可见性

`-p` 或者 `--ontop`

使用此选项可以强制对话窗口始终显示在最顶层。

## 窗口位置

`-o` 或者 `--moveable`

使用此选项允许窗口在屏幕上被拖动。

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

将对话窗口放置在屏幕上定义的指定位置。

`--positionoffset <num>`

设置窗口的边距，即窗口与屏幕边缘之间的距离。

`--position <x>,<y>`

将对话窗口放置在指定的 x, y 坐标位置，例如：`--position 100,200`。

**注意事项：**
 - 坐标 (0,0) 位于可见屏幕区域的左上角。
 - 可见屏幕区域不包括停靠栏或菜单栏所占用的区域。例如，如果停靠栏位于屏幕的左侧，那么原点会向内偏移。


## 窗口大小

您可以根据消息内容多少或不同显示设备的尺寸，调整字体大小，使其大于或小于默认值。 图片会相应地进行缩放。 文本的字体大小保持不变。

`-b` 或者 `--big`

这会使窗口看起来比正常情况下大约25%更大，从而增加图标显示区域的视觉效果。

![图片](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` 或者 `--small`

这会导致窗口看起来比正常情况下缩小约25%。

![图片](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## 窗口外观

您可以强制使用深色或浅色模式，并且系统会始终采用您设置的模式，而不管用户的默认偏好设置如何。

`--appearance dark` 或者 `--appearance light`

## 迷你模式

迷你模式可以通过设置一个参数来启用。`--mini`

迷你模式会强制显示一个小型窗口，该窗口采用修改后的布局，并且提供有限的显示选项。 `--title` 会变得更小，并位于窗口的顶部中央，或者可以通过 `--title none` 禁用。 `--message` 可以显示最多四行文本（超出此长度的文本会被截断）。 当 `--icon` 可见时，它会占据窗口的左侧，而所有其他内容则位于右侧。 `--hideicon` 和 `--icon none` 会被遵循。 `--button1text` 和 `--button2text` 可用，但“信息”按钮不可用。

![图片](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

如果使用了 `--progress` 参数，则按钮区域会被移除，并替换为进度条和一段进度文本。为了关闭对话框，必须将命令 `quit:` 传递给命令文件。

![图片](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - 配置预设的窗口样式

修改默认值，从而改变对话框的显示方式。

除了`--mini`之外的其他样式没有特殊的属性，可以通过使用各种参数来设置窗口属性，从而实现不同的视觉效果。

`centered`、`alert` 和 `caution` 将使用来自 `--title` 的值，将其作为标题添加到消息区域，然后禁用标题显示。这会将标题放置在显示图标的下方。

    "mini" is functionally equavelent to --mini "centered" will set all the options for centered content "alert" sets a pre-configured dialog window 300x300 and centered content "caution" and "warning" are the same as "alert" with the icon configured

示例：`dialog --style alert`

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

这相当于输入：

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## 定制窗户尺寸

Dialog can be any size you want instead of the default, `--small` or `--big` options.

`--width` 和 `--height` 可以用来定义对话框的大小。内容会根据选择的大小进行调整。

swiftDialog 支持使用 `%` 作为当前屏幕尺寸的函数，例如，`--width 50%` 会将对话框的宽度设置为当前屏幕分辨率的 50%。

![图片](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` 将会在所有显示界面上覆盖一个模糊的背景，并将对话窗口置于所有其他窗口之上。 这样可以实现更具针对性的信息展示，或者在某些工作流程中，防止用户与其他的应用程序或桌面环境进行交互（例如，在用户首次使用时）。


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### `--ontop` 在 `--blurscreen` 以及现有对话窗口下的行为表现

如果存在一个已存在的对话框，并且该对话框处于激活状态（`--blurscreen`），那么使用`--ontop`会导致后续的对话框出现在模糊层之上。 这样就可以运行一个后台对话框，并启动其他对话框，同时让它们保持可见。 需要注意的是，如果您计划通过编程方式与这些对话框进行交互，请确保为每个对话框使用唯一的命令文件。

## `--showonallscreens`

当使用该功能时，对话窗口将出现在所有虚拟桌面上。

如果使用了多个显示器，对话框将出现在与所使用的显示器相关的所有虚拟桌面中。