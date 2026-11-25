---
title: 文本字段
description: 创建具有各种属性和验证功能的文本输入框
translationSynced: 2026-11-25T05:22:28+00:00
---

这个选项允许您指定一个区域，用户可以在该区域输入文本，然后再关闭对话框。`--textfield`

它接受一个文本参数，并将该参数用作文本框的标签，不仅在对话框的用户界面中，也在报告输出中都使用该标签。

程序结束后，结果会以以下格式输出到标准输出（stdout）：

`<textfield text> : <user input>`

或者，如果使用 `--json` 选项来启用 JSON 输出：

```json
{
"<textfield text>" : "<user input>"
}
```

## 例子

如果使用以下对话：

`dialog --textfield "Textfield 1"`

将显示以下对话框：

![图片](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

用户输入了回复：

![图片](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

这将产生以下输出结果：

`Textfield 1 : This is what the user entered`

或者在使用 `--json` 时。

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## 其他文本输入框

在调用对话框时，可以通过添加额外的`--textfield`选项来指定多个文本输入框。

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![图片](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

您可以指定任意数量的文本字段。每个文本字段将在输出结果中作为一个独立的字段呈现。

如果您在对话窗口中添加了多个文本框，可能需要调整对话窗口的`--height`大小，以确保它们能够完整显示。

示例：

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

这会产生以下输出结果：

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## 文本框修饰符

修饰符以逗号分隔的形式附加到文本框的标签上。

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| 修饰语。 | 描述。 |
|---|---|
| `name=<text>` | 将此值用作输出的键，而不是标签。 |
| `required` | 在 swiftDialog 对话框关闭之前，必须填写所有字段。 |
| `secure` | 隐藏输入内容，仅显示密码字段中的字符。 |
| `passwordfill` | 在某个字段中启用 macOS 密码自动填充功能。`secure` |
| `prompt="<text>"` | 字段内部显示的占位符文本（不在输出结果中返回）。 |
| `value="<text>"` | 为该字段预设一个默认值（可编辑）。 |
| `regex=<pattern>` | 要求字段内容必须匹配指定的正则表达式。 |
| `regexerror=<text>` | 当正则表达式不符合条件时，会显示自定义的错误提示信息。 |
| `editor` | 多行文本编辑器，而不是单行输入框。 |
| `isdate` | 将文本输入框替换为日期选择器。输出结果以简短的日期字符串格式显示。 |
| `fileselect` | 添加一个“选择”按钮，点击后会打开文件选择器。 |
| `filetype=<types>` | 限制文件选择器仅允许选择指定类型的文件（类型之间用空格分隔）。可以使用文件扩展名（例如：`png jpg`），或者使用类型关键词 `folder`、`image`、`movie`、`video`、`audio`。 |
| `path=<path>` | 设置文件选择器的初始目录。 |
| `confirm` | 添加一个确认字段，其内容必须与主字段完全一致。 |

### 姓名

`name=<text>` 将标签替换为输出中的键。 当您希望在输出中使用友好的标签，但又希望键名更简洁时，这很有用。

### 安全

`secure` 它会隐藏用户输入的字符，并显示一个锁的图标。但是，内容仍然会以纯文本形式输出到标准输出。

```sh
--textfield "Password,secure"
```

![图片](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### 密码自动填充功能

`passwordfill` 启用 macOS 的密码自动填充功能。必须与 `secure` 配合使用。

```sh
--textfield "Password,secure,passwordfill"
```

### 必需的

`required` 防止 swiftDialog 在字段获得值之前退出。 必填字段会用一个 `*` 标记，并且当用户尝试在未填写的情况下关闭对话框时，这些字段会高亮显示。

```sh
--textfield "Full Name,required"
```

![图片](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### 提示

`prompt="<text>"` 显示输入框内的占位符文本。当用户开始输入时，该文本会消失，并且不会包含在输出结果中。不支持在 `secure` 类型的输入框中使用。

```sh
--textfield "Name,prompt="Enter your full name""
```

![图片](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### 价值

`value="<text>"` 该字段会预先填充一个默认值，用户可以对其进行编辑。

```sh
--textfield "Default Value Test",value="Some default value"
```

![图片](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### 正则表达式和正则表达式错误

`regex=<pattern>` 要求字段内容必须与正则表达式匹配，才能使 swiftDialog 对话框关闭。 `regexerror=<text>` 设置当模式不匹配时显示的提示信息。

除非模式明确允许，否则一个 `regex` 字段不能为空。

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![图片](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

使用 `--textfieldlivevalidation` 在输入框中显示绿色或红色覆盖层，根据用户输入的内容，实时反馈正则表达式是否匹配。

### 编辑

`editor` 提供一个更大的、多行文本输入区域，而不是一个单行输入框。

```sh
--textfield "Notes,editor"
```

![图片](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### 日期选择器

使用 `date` 或 `time` 修饰符，可以将文本字段替换为 macOS 的日期/时间选择器。所选的值将以格式化字符串的形式返回。

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

**注意：** `isdate` 这个修饰符已被弃用，建议使用 `date` 和 `time`。

#### 日期范围

使用 `mindate=` 和 `maxdate=` 来限制可选择的日期范围。

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**格式：** 日期必须采用`YYYYMMDD`格式（适用于所有地区）。允许使用分隔符，但会被移除（例如，`2026-09-30` → `20260930`）。无效的日期将被忽略，并且不会应用限制。

#### 日期格式

使用 `format=` 来指定返回格式，采用 strftime 语法。

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

常见的格式字符串：
- `+%Y-%m-%d` - 符合 ISO 8601 标准的格式（例如：`2026-09-29`）。
- `+%s` - Unix时间戳（自纪元以来的秒数）。
- `+%x` - 本地化的日期显示方式。
- `+%D` - 美国格式（例如：`09/29/26`）。

#### 初始化日期选择器

使用 `value=` 来设置初始日期。 日期选择器支持多种格式：

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

支持的格式包括：ISO 8601 格式、特定地区格式、12/24 小时制、自 Unix 纪元以来的时间戳，以及自然语言。

### 文件选择

`fileselect` 添加了一个“**选择**”按钮，点击该按钮会打开一个标准的“文件选择”对话框。用户选择的路径会被填入相应字段，并在输出结果中返回。

```sh
--textfield "Config File,fileselect"
```

使用 `filetype` 来限制可以被选择的内容。 值之间用空格分隔，可以是文件扩展名或类型关键词：

| 价值。 | 选择。 |
|---|---|
| `folder` | 仅限目录。 |
| `image` | 任何类型的图像。 |
| `movie` / `video` | 任何类型的视频。 |
| `audio` | 任何类型的音频。 |
| `<extension>` | 与该扩展名匹配的文件（例如：`png`，`pdf`）。 |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

使用 `path=<path>` 来设置文件选择器打开的目录。

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![图片](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### 确认

`confirm` 在主字段下方增加一个额外的字段。 在 `swiftDialog` 接受输入之前，这两个字段必须包含相同的值。 这对于密码确认非常有用。

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### 组合修饰语

修饰符可以自由组合（前提是它们之间兼容）。

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### JSON 格式

文本字段可以通过以下两种方式以 JSON 格式进行定义：

#### 完整的JSON配置文件

在使用 JSON 配置文件或 `--jsonstring`/`--jsonfile` 时，请将文本字段指定为数组。

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### 每个论点的 JSON 配置

从版本 3.1.1 开始，文本字段也可以通过 `--textfield` 以 JSON 对象的形式进行指定（而不是使用逗号分隔的修饰符）。 这样可以提供更直接的控制，尤其适用于复杂的配置。

**语法：**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**特性：**
- `title` - 字段标签文本。
- `name` - 替代的输出键名。
- `required` - 该字段必须填写（真/假）。
- `secure` - 隐藏输入内容（密码框）。
- `passwordfill` - 启用 macOS 密码自动填充功能（需要 `secure`）。
- `prompt` - 字段内部显示的占位符文本。
- `value` - 预先填充该字段，使用默认值。
- `regex` - 要求字段内容与正则表达式匹配。
- `regexerror` - 当正则表达式不符合要求时，会显示自定义的错误提示信息。
- `editor` - 使用多行文本编辑器，而不是单行输入框。
- `date` - 将该字段替换为日期选择器 (是)。
- `time` - 将该字段替换为时间选择器 (true)。
- `mindate` - 可选的最小日期（YYYYMMDD格式）。
- `maxdate` - 可选的最大日期（格式为YYYYMMDD）。
- `format` - 使用 `strftime` 语法返回格式化后的字符串 (例如：`+%Y-%m-%d`, `+%s`)。
- `fileselect` - 添加一个“选择”按钮，点击该按钮会打开文件选择器。
- `filetype` - 将文件选择器限制为特定类型的文件（可以使用空格分隔的文件扩展名或关键词）。
- `path` - 文件选择器的初始目录。
- `confirm` - 添加一个确认字段，其内容必须与主字段相同。

**示例：**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**日期选择字段：**
- 使用`"date": true`或`"time": true`（或两者）来创建一个选择器。
- `"mindate"` 和 `"maxdate"` 接受 `YYYYMMDD` 格式的日期（分隔符会被移除）。
- `"format"` 使用 `strftime` 语法设置返回格式。
- `"value"` 提供初始日期/时间，并以多种格式（ISO、本地化格式、时间戳、自然语言）进行输出。

**所有修饰符均受支持：** CSV格式中可用的所有修饰符，也都可以在JSON键中找到。

**多个文本字段：**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**注意：** 当使用针对每个参数的 JSON 格式时，每个 `--textfield` 都是独立的。 仍然支持整体配置的 JSON 格式，用于批量初始化。

## 键盘行为

按下任何单行文本框中的“回车”键将触发“按钮 1”的操作，这相当于点击默认按钮。但这不适用于`editor`字段。