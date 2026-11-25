---
title: 自定义消息区域
description: 学习如何在 swiftDialog 中设置和自定义消息文本、字体属性以及位置
translationSynced: 2026-11-25T05:01:19+00:00
---

使用 `-m` 或 `--message` 命令行的选项，可以指定您希望在对话框的消息区域中显示的内容。

示例：

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

消息区域的宽度可以选择占据对话窗口的2/3，或者在不显示图标区域的情况下占据整个窗口的宽度。

如果消息内容超出显示区域的宽度，会自动换行。如果消息内容超出可用的总显示区域，则会滚动显示。


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### 内容来源

除了传入一段文本字符串之外，您还可以传入一个 Markdown 文件的路径或 URL。 任何以 `.md` 结尾的文件都将被视为 Markdown 源代码文件。

示例：

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## 消息位置

`--messagealignment` 和 `--messageposition` 允许您指定消息在对话框中的位置。这对于创建消息在垂直和水平方向上居中的对话框非常有用。

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## 修改消息的字体、颜色、大小和对齐方式

`--alignment [left | centre | center | right]`

设置消息的对齐方式。 默认值为“左对齐”。

`--messagefont <text>`

允许您修改消息的字体、文本大小和颜色。

`color,colour=<text><hex>`

> `<text>` 可以是苹果公司标准的任何一种颜色，包括：`black`、`blue`、`gray`、`green`、`orange`、`pink`、`purple`、`red`、`white`、`yellow`。 如果选项无效，则默认使用系统的主色调（通常在浅色模式下为 `black`，在深色模式下为 `white`）。

> `<hex>` 以十六进制格式指定，例如：#00A4C7。

`size=<float>` 接受任何浮点数值（例如：15.7、20、32.0）。

`name=<fontname>` - 接受任何已安装的字体名称。


示例：`--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### 在消息中使用更多颜色

使用`colour=<value>`可以设置消息的基本颜色，但您可以使用`:colour[text]`格式来设置单个单词或字母的颜色。

示例：

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

