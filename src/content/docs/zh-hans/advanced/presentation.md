---
title: 演示文稿
description: 为正在进行的流程和任务创建演示模式对话框
translationSynced: 2026-11-25T05:30:56+00:00
---

## 演示模式

`--presentation` 或者 `--style presentation`

“演示模式”是 swiftDialog 的一种输出模式（不接受用户输入），用于显示正在进行的流程或任务。

更新显示需要使用一个[命令文件](/zh-hans/advanced/command-file))以及相应的命令。

该界面被划分为两个主要内容区域和一个底部区域，底部区域包含一个进度条和一些按钮。

## 信息区域

窗口的左侧1/3区域是一个信息显示区域，可以显示以下内容中的_一项_：

### 默认设置

一个背景颜色，用于表示用户的突出显示颜色偏好。

您可以选择性地添加以下修改器：
 - `--infobox <text>` 用于显示文本（支持 Markdown 格式）。
   - 文本垂直居中对齐。
 - `--background color=<color|hex>` 用于设置背景颜色。
   - 如果没有指定颜色，系统将使用默认的强调色。
 - `--icon <image>` 用于在左上角显示一个图标。
 - `--iconsize <int>` 用于设置图标的大小。

### 图片

指定一个或多个`--image <image>`，以使用图像填充该区域。

多张图片会以轮播图的形式展示。 包含 `--autoplay <sec>` 可以使图片自动轮换。

**提示**
* 为了获得最佳效果，请使用纵向的图片。
* 图像会按照比例进行缩放以填充整个区域，如果使用多个不同尺寸比例的图像，可能会进行裁剪。

运行演示模式后，系统会在调试日志输出中包含一个推荐的图像尺寸，该尺寸适用于当前窗口。在您关闭对话框后，即可查看这些信息。`--debug`

e.g.

    调试信息：对于这些窗口尺寸，侧边栏图片的理想尺寸应为：宽度 492.0 像素，高度 636.0 像素。

### 网页内容

指定`--webcontent <url>`以显示HTML源文件的内容。

**提示**
* 如果使用本地文件，请使用 `file:///path/to/file.html` 来引用该文件。

## 内容区域

窗口的右侧2/3区域用于显示以下形式的内容：

### 默认设置

任何格式，只要是支持的格式都可以。`--message <text>`

### 清单

一个或多个 --listitem 选项，可以采用支持的任何形式。<item>

## 页脚

由于演示模式的主要功能是显示进度和其他可更新的内容，因此窗口的底部始终可见，并专门用于显示一个全宽的进度条以及一些按钮。

## 例子

请提供需要翻译的英文文本。

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

**信息区域显示网页视图，内容区域显示列表项。**

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">