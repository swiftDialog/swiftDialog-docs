---
title: 自定义标题
description: 学习如何在 swiftDialog 中设置和自定义标题文本以及字体属性
translationSynced: 2026-11-25T05:01:01+00:00
---

## 设置标题文本

使用 `-t` 或 `--title` 命令选项来指定您希望在对话框标题区域中显示的内容。

示例：

`--title "An Important Message"`

`-t "An Important Message"`

标题区域是对话窗口顶部的固定宽度加粗区域。如果文本长度超过窗口的显示范围，则会被截断。

![图片](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## 自定义标题字体属性

使用 `--titlefont` 命令行选项来设置标题字体属性。

### CSV 语法

字体属性以 `property=value` 的形式表示，多个属性之间用逗号分隔。

可修改的属性包括：
 * `colour=<hex_value>` (或者 `color=<hex_value>`)
   * 以十六进制格式指定的颜色值，例如：#00A4C7。
 * `size=<float>`
   * 它可以接受任何浮点数值，例如 30、65、72.3。
 * `weight=<text>`
   * 接受以下任何一种字体：纤细、轻盈、常规、中等、粗体或加粗（默认）。
 * `name=<fontname>`
   * 它可以接受一个字体名称或字体系列。可用名称的列表可以通过 `--listfonts` 命令确定，或者通过查阅 macOS 上的“字体册”应用程序。
 * `alignment=[left|right]`
   * 将标题文本左对齐或右对齐。
 * `offset=<float>`
   * 将标题文本水平移动指定的像素数量。正值向右移动，负值向左移动。当使用`alignment=right`时，偏移方向会自动反转，因此正值仍然会将文本向右边缘移动。
 * `shadow`
   * 为文本添加阴影效果（布尔值，无需指定具体值）。

 > **警告：** 在混合使用字体名称和字重时，请务必小心。当通过名称指定字体或字体系列时，某些字重可能无法使用。如果发生这种情况，将忽略您指定的字重。

您可以选择使用一个或多个参数，并且它们的排列顺序并不重要。例如，如果您只想修改大小，可以使用以下参数：

`--titlefont "size=60"`

示例 1：`--titlefont "colour=#00A4C7,weight=light,size=60"`

这个例子将颜色设置为 `#00A4C7`，粗细设置为 `light`，字体大小设置为 `60`，最终显示效果如下：

<img width="400" alt="image" src="/images/titlefont1.png" />

示例 2：`--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

这个示例将颜色设置为值 `#D054A0 `，大小设置为 `40`，并使用字体名称 "Chalkboard-Bold"。

<img width="400" alt="image" src="/images/titlefont2.png" />

示例 - 左右对齐：

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### JSON 对象语法

从版本 3.1.1 开始，`--titlefont` 和 `--messagefont` 也可以指定为 JSON 对象，以便进行更直接的控制。

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**特性：**
- `name` - 字体名称或字体系列。
- `size` - 字体大小，单位为点。
- `colour` / `color` - 文本颜色（十六进制或颜色名称）。
- `weight` - 字体粗细：`thin`, `light`, `regular`, `medium`, `heavy`, `bold`
- `alignment` - 文本对齐方式：`left`，`right` (仅适用于标题)。
- `offset` - 标题的水平偏移量，单位为点。
- `shadow` - 添加阴影效果（布尔值）。

**示例：**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**注意：** `shadow` 键现在支持 JSON 格式（此前仅支持 CSV 格式）。

### 在标题中使用颜色

使用`colour=<value>`可以设置文本的基础颜色，但您可以使用`:colour[text]`格式来设置单个单词或字母的颜色。

示例：

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## 字幕

使用 `--subtitle <text>` 可以显示标题下方的一行辅助文本，该文本使用相同的字体，但字号较小。

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

字幕标题继承了与主标题相同的字体名称、字重和颜色，但以不同的方式呈现。`titlefont size − 10pt`

#### 隐藏标题区域

使用关键词 `none` 可以隐藏标题区域。这将移除标题栏和水平分隔线。

e.g. `--title none`




