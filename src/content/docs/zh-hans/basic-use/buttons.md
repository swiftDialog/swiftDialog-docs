---
title: 按钮及其行为
description: 学习如何在 swiftDialog 中配置按钮的文本、操作和行为
translationSynced: 2026-11-25T05:05:55+00:00
---

对话框最多可以显示三个按钮。

按钮显示在对话框窗口的下方区域。

![对话按钮区域 ](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## 按钮 1 - 默认按钮
默认情况下，会显示一个按钮，其标签为“**确定**”。 默认按钮始终存在，并且映射到“**Enter**”键，按下该按钮将退出对话框应用程序，并返回退出码 `0`。

可以使用`--button1text`选项，通过添加任意文本来修改默认按钮的标签。

e.g. `--button1text "Enter to Continue"`

按钮 1 的文字：](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

该操作还可以通过`--button1action`选项进行修改，因此，除了简单地退出对话应用程序之外，您还可以执行其他操作。

目前，可执行的操作仅限于在用户的默认浏览器中打开一个网址。

e.g. `--button1action "https://github.com/"`

## 按钮 2 - 取消按钮
第二个按钮默认情况下是隐藏的。可以通过使用“`-2`”或“`--button2`”选项来显示该按钮，此时按钮上会显示默认的“取消”字样。第二个按钮与“_Esc_”键关联，按下后会退出对话框应用程序，并返回退出码 `2`。

第二个按钮的标签可以使用“`--button2text`”选项进行修改，可以输入任意数量的文本。使用此选项时，无需调用“`--button2`”选项。 如果您正在修改文本标签，则按钮会自动显示。

示例：

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![按钮 2 我不关心 ](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

按钮2目前没有其他功能实现。

## “更多信息”按钮
“更多信息”按钮默认情况下是隐藏的。可以通过使用“`-3`”或“`--infobutton`”选项来显示该按钮，该按钮默认显示“**更多信息**”字样。点击该按钮将关闭 swiftDialog，并返回退出码 `3`。

如果存在`--infobuttonaction`参数，点击“更多信息”按钮只会执行`--infobuttonaction`操作，并且swiftDialog不会自动退出。如果添加了`--quitoninfo`参数，则会恢复默认的退出行为。

可以使用“信息”按钮的标签，并通过“`--infobuttontext`”选项修改其文本内容。使用此选项时，无需调用“`--infobutton`”选项。 如果您正在修改文本标签，则会自动显示该按钮。

示例：

`--infobuttontext "Click here for more details"`

![信息按钮，点击以获取更多详情](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

该操作还可以通过`--infobuttonaction`选项进行修改，因此，除了简单地退出对话应用程序之外，您还可以执行其他操作。

目前，可执行的操作仅限于在用户的默认浏览器中打开一个网址。

e.g. `--infobuttonaction "https://github.com/"`

## 按钮符号

设置按钮上显示的符号，除了按钮的文本标签之外，还可以使用指定的SF符号。

### CSV 语法

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

该函数接受一个 SF Symbol 的名称作为参数。

可选属性以逗号分隔的格式提供，顺序可以任意排列。
 - 位置：可以是“前置”、“后置”、“顶部”或“底部” - 默认值为“前置”。
 - 渲染模式：可以选择分层、单色、多色或调色板模式，默认使用单色模式。
 - 调色板：添加两个或三个颜色，格式为：palette=颜色1-颜色2-颜色3。
   - 例如：调色板 = 红色-绿色-蓝色。
 - 尺寸：格式为 size=<num>。
 - 颜色：格式为 color=<text|hex>。
   - 如果设置了多色渲染模式，则颜色信息会被忽略。

示例：

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### JSON 对象语法

从版本 3.1.1 开始，按钮符号也可以指定为 JSON 对象，以便进行更直接的控制。

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**特性：**
- `name` - SF 图标名称（必填）。
- `position` - 符号位置：`leading`, `trailing`, `top`, `bottom` (默认值：`leading`)
- `colour` / `color` - 符号颜色（十六进制或颜色名称）。
- `size` - 符号大小，单位：点。
- `rendering` - 渲染模式：`hierarchical`、`monochrome`、`multicolour`、`palette`。
- `palette` - 包含2到3种颜色的数组，用于多色符号 (在CSV文件中以逗号分隔的值表示，在JSON文件中以数组表示)。

**示例：**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**注意：** 当使用 `rendering: palette` 时，调色板应以 JSON 数组的形式存在：`["red","green","blue"]`。当使用 CSV 格式时，颜色值之间应使用连字符分隔：`palette=red-green-blue`。

## 按钮位置

默认情况下，“按钮1”和“按钮2”位于右侧，“信息按钮”位于左侧

使用 `--buttonstyle center` 会将按钮 1（如果存在则还包括按钮 2）放置在对话框窗口底部居中位置

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` 和 `--infotext` 在使用 `--buttonstyle center` 选项时，不兼容。

## “堆叠” 样式，适用于按钮

`--buttonstyle stack`

将按钮 1 和按钮 2 以全宽排列，并堆叠在一起。

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` 和 `--infotext` 在使用 `--buttonstyle stack` 选项时，不兼容。

## `[return]` 和 `[enter]` 键的行为

如果没有输入框，对话框中当前聚焦的输入控件是 `button1`，而 `[enter]` 和 `[return]` 都会激活按钮，因为它是窗口上唯一的交互元素，因此默认情况下会获得键盘的焦点。 这样一来，就会关闭对话框（假设按钮是可用的，而不是被禁用的）。

`[return]` 键始终激活 button1，除非编辑器字段具有焦点。`[enter]` 键仅在聚焦元素上激活（这就是为什么它可以在没有输入元素的窗口上关闭对话框的原因）。

在一个单行文本输入框中，`[return]`无法添加换行符，因此默认操作会生效，关闭对话框（激活默认的响应器）。相比之下，`[enter]`没有任何作用，因为它也无法添加换行符，但由于它无法控制默认响应器的行为，因此没有任何事情发生。

在多行文本输入框中（即，启用`editor`功能的`--textfield`），按下“回车”键（即“Enter”键，此处用“回车”代替）_可以_插入一个换行符，并且这个操作会优先于其默认的设置（例如，按下按钮1关闭窗口）。“Tab”键也像预期那样工作，插入一个新行。`[return]` `[return]`

### 修改 `[return]`、`[enter]` 或 `[esc]` 的默认行为

如果您不希望默认情况下，`[return]`、`[enter]`或`[esc]`关闭对话框，可以使用`--hidedefaultkeyboardaction`选项来更改其行为。该选项会将默认的`[return]`或`[escape]`键的触发方式也改为需要同时按下`cmd`和`shift`才能激活。这有助于防止意外关闭对话框。

## 返回码

以下是每次操作完成后返回的错误代码。您可以忽略这些代码，也可以在调用脚本中使用它们，以执行进一步的操作。

| 按钮名称。 | 可选的。 | 快捷键。 | 返回码。 |
| ----------- | -------- | ------ | ----------- |
| `button1`   | 不。       | 进入。  | 0           |
| `button2`   | 是的。      | 退出。    | 2           |
| `infobutton` | 是的。      |        | 3           |

## 禁用按钮

按钮1和按钮2可以在启动时被禁用，可以使用以下命令中的一种来实现：

`--button1disabled`

`--button2disabled`

可以通过将按钮文本设置为`none`，完全隐藏“Button1”按钮。

请注意，这也会禁用使用“[返回]”按钮关闭对话框的功能，因此请确保对话框有其他退出方式。