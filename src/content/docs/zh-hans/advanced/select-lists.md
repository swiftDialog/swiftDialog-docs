---
title: 选择列表和单选按钮
description: 创建下拉列表和单选按钮组，供用户选择
translationSynced: 2026-11-25T05:23:46+00:00
---

Dialog 组件可以接收一个值列表，并将这些值以下拉菜单的形式显示，并且可以选择默认选项。

![图片](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## 如何使用


### 选择列表的标题

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

可以通过命令行选项来设置标签，该标签将应用于列表。例如：`--selecttitle` `--selecttitle "Select an Option"`

![图片](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


这个名称将出现在 `swiftDialog` 的标准输出（STDOUT）中，并显示所选项目的数值。对于单选列表，标准的输出格式将如下所示：
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

可以指定多个`--selecttitle`参数。 相关的`--selectvalues`和`--selectdefault`参数也可以指定，并且会按照它们出现的顺序与一个选定列表关联。

如果使用了多选列表，则不会显示“已选项”（SelectedOption）和“所选索引”（SelectedIndex）。

只有当 swiftDialog 的退出码为 0 时，才会显示选定项目的输出结果。

### 选择列表中的值

`--selectvalues <text><csv>`

值以 CSV 格式指定，并通过 `--selectvalues` 命令行选项传入，例如 `--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![图片](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### 选择列表 默认设置

`--selectdefault <text>`

默认选项可以通过命令行选项进行设置，例如：`--selectdefault "Option 4"`。 `--selectdefault`

![图片](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

如果未指定默认值，并且用户未从列表中选择任何选项，则不会产生任何输出。


示例输出：
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

只有当Dialog程序的退出码为0时，才会显示选定项目的输出结果。

### 每个论点的 JSON 配置

也可以使用 JSON 对象通过 `--selectitem` (或 `--selecttitle`，配合 JSON 值) 来定义选择列表。 这样可以更直接地控制每个条目的属性。

**语法：**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**特性：**
- `title` - 用于下拉列表的标签。
- `values` - 选项值的数组。
- `default` - 默认选择的值。
- `required` - 是否为必填项（对于单选按钮，此项将被忽略）。
- `style` - 显示样式：`list`、`radio`、`searchable` 或 `multiselect`。
- `name` - 替代的输出键名。

**示例：**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

JSON 数据项与位置参数是相互独立的。在使用 JSON 时，值会从位置标签列表中进行筛选，以避免重复。`--selectvalues/--selecttitle/--selectdefault`

## JSON 模式

可以通过使用 JSON 格式来指定选定列表，从而实现更直接的控制。

### 完整的 JSON 配置文件

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### 每个论点的 JSON 格式

也可以使用 `--selectitem` 或 `--selecttitle` 以及一个 JSON 对象来定义单个选定项：

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

**注意：** `--selecttitle` 对 JSON 对象与 `--selectitem` 的处理方式完全相同。

### 示例：

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![图片](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![图片](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## 修饰语

### 姓名

将输出记录保存为指定的文件名 `name`，而不是使用默认的标题。

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### 可搜索的

这个`searchable`修饰符会在列表中添加一个搜索字段。在文本框中输入内容可以筛选列表。

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### 无线电

`radio` 属性会改变选择列表的显示方式，使其显示一个包含单选按钮的组。当使用 `radio` 且未指定默认项时，列表中的第一个条目将成为默认选择项。因此，使用单选按钮总是会强制选择其中一个值，并且像 `required` 这样的属性会被忽略。

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![图片](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### 必需的

该 `required` 修饰符会将特定的列表项设置为必填项，只有在设置了该项的值后，swiftDialog 才会退出。

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![图片](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![图片](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### 多选

这个`multiselect`修饰符允许从列表中选择多个选项。选中的项目会显示为可移除的标签，输出结果是一个以逗号分隔的所选值的列表。

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

在使用 `multiselect` 时，选择的值将以单个逗号分隔的字符串形式返回：

```
"Choose options" : "Option One, Option Three"
```

或者，以JSON格式呈现：
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## 全球风格

`--selectstyle [list | radio | searchable | multiselect]`

设置对话框中**所有**选择列表项目的显示样式。这等同于在每个 `--selecttitle` 上单独设置样式修饰符。列表级样式修饰符在 `--selecttitle` 上优先于此全局设置。

| 价值。 | 描述。 |
|---|---|
| `list` | 标准下拉菜单（默认）。 |
| `radio` | 单选按钮组。 |
| `searchable` | 带有筛选文本框的下拉菜单。 |
| `multiselect` | 可搜索的字段，允许进行多项选择。 |

## 向列表中添加部分内容

在您的列表中，根据需要，在各个项目之间添加三个或更多个连字符 `---`，用以分隔列表中的内容。

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![图片](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**注意：** `---` 每个标记都会在索引中计数，即使分隔符本身不可选择。 在上面的示例中，即使菜单中只显示 5 个项目，列表数组中也会有 7 个项目。 在构建您的选择列表时，请务必考虑到这一点。

## 输出

程序在退出时，会将用户选择的值（或者如果指定了默认值且用户未选择任何值，则输出默认值）输出到`stdout`。 脚本可以解析此输出，并根据需要采取相应的操作。

输出结果包含两行内容。
* 第一行是列表项的文本内容，并将以 `SelectedOption: <text of item>` 的形式输出。
* 第二行表示所选项目的索引，格式为`SelectedIndex: <index of item>`。

索引从 `0` 开始，因此，如果列表中的第三个项目被选中，那么 `SelectedIndex` 的输出结果将是 `SelectedIndex: 2`。

## 示例阅读输出结果

考虑到以下输出结果：
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

通过 `grep` 和 `awk` 命令，可以提取出您需要处理的特定值。

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

或者。

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## 添加多选列表

要添加多个选择列表，只需指定多个 `--selectvalues`、`--selecttitle` 和 `--selectdefault` 的实例即可。标题和默认值将按照它们出现的顺序进行设置。


### 多项选择输出

当使用多个选择列表时，输出结果会被修改，以便解析不同的命名列表。例如，如果使用上述 JSON 数据，并选择 "two" 和 "red"，则会得到以下输出：

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

如果以 JSON 格式输出，结果将如下所示：

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```