---
title: JSON 配置文件
description: 使用 JSON 格式来指定复杂配置中的对话选项
translationSynced: 2026-11-25T06:09:58+00:00
---

与其使用大量的命令行选项来构建复杂的对话框，您可以使用 `--jsonfile` 或 `--jsonstring` 选项来定义参数。

JSON 格式使用的选项与命令行中指定的选项基本相同，但存在一些例外情况和需要注意的地方。

**注意：**
 - 命令行选项可以与JSON文件一起使用，但JSON文件中定义的选项将优先生效。
 - 为了支持消息文本中的原始字符`\n`，`--jsonstring`会期望JSON输入以单行连续的方式呈现。

示例：

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## 与命令行选项的不同之处

可以重复使用的选项可以以数组的形式输入。

例如，要指定多个图像及其标题，可以使用一个数组，其中包含 `image` 数组，每个 `imagename, caption`

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

复选框可以被设置为选中状态和/或禁用状态。 默认状态是`"disabled" : false`，无需特别指定。

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

对于多个选项，请指定一个文本框，其中包含字段名称的数组。`textfield`

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### 字符串和布尔值

大多数选项会以字符串形式传递，因此需要使用引号来指定其值。某些值可以指定为布尔值（`true` 或 `false`，无需引号）。可以接受布尔值的选项有：

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### 无法从 JSON 文件中获取这些选项

以下是一些选项，它们无法在 JSON 文件中使用，因为在实际应用中它们没有意义：

* `--jh` - 作为一个直接替换，用于接收 JamfHelper 命令行选项。
* `--listfonts` - 在原型设计阶段使用，用于显示可用的字体列表。
* `--help` - 显示帮助信息并退出。主要用于原型设计阶段。
* `--demo` - 使用默认设置显示一个对话框。在原型设计阶段使用。
* `--version` - 显示对话版本信息并退出。
* `--showlicense` - 打印许可信息并退出。
* `--coffee` - 打印咖啡信息并退出。

## 示例：在Python中生成JSON数据，并将其作为文件或字符串传递

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```