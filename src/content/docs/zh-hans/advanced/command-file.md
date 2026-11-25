---
title: 命令文件
description: 使用命令文件，动态地更新对话框的内容
translationSynced: 2026-11-25T06:07:25+00:00
---

某些对话内容可以在程序运行后进行实时更新。这可以通过向一个命令文件发送指令来实现，Dialog程序会读取并解析这些指令。

---

为了允许脚本向 Dialog 发送命令，必须在后台启动 Dialog 进程。

```sh
/usr/local/bin/dialog & sleep 0.1
```

系统`sleep 0.1`会在发送第一个命令之前，给予Dialog 100毫秒的时间进行初始化。

默认的命令文件路径是 `/var/tmp/dialog.log`。 可以使用 `--commandfile` 参数来设置自定义路径：

```sh
dialog --commandfile /var/tmp/my.log
```

使用以下方式发送指令：

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## 内容

| 命令。 | 描述。 |
|---|---|
| `title: <text>` | 更新对话框的标题。 |
| `title: none` | 隐藏标题区域。 |
| `titlefont: <params>` | 更新标题字体属性。 接受空格分隔的参数对：`key=value`, `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>`。 |
| `message: <text>` | 替换消息内容。支持 Markdown 格式。 |
| `message: + <text>` | 附加到现有消息（在新增内容之前添加一个换行符）。 |
| `message: /path/to/file.md` | 从本地的 Markdown 文件中加载消息内容。 |
| `alignment: [left\|center\|right]` | 设置消息文本的对齐方式。 |

---

## 图标

| 命令。 | 描述。 |
|---|---|
| `icon: <path\|url\|SF Symbol>` | 更改显示的图标。 |
| `icon: none` | 隐藏图标。 |
| `icon: centre` / `icon: center` | 将图标移动到中心位置。 |
| `icon: left` / `icon: default` | 将图标恢复到默认的左侧位置。 |
| `icon: size: <num>` | 更改图标大小。 |
| `iconalpha: <float>` | 设置图标的透明度（0.0 表示完全透明，1.0 表示完全不透明）。 |
| `overlayicon: <path\|url\|SF Symbol>` | 设置覆盖图标。 |
| `overlayicon: none` | 隐藏覆盖层图标。 |

---

## 横幅和背景

| 命令。 | 描述。 |
|---|---|
| `bannerimage: <path\|url>` | 设置横幅图片。 |
| `bannerimage: none` | 移除横幅图片。 |
| `bannertext: enable` | 将标题显示为横幅文字（并将字体颜色设置为白色）。 |
| `bannertext: disable` | 恢复默认标题显示样式。 |
| `bannertext: shadow` | 为横幅标题文字启用阴影效果。 |
| `bannertext: <text>` | 设置横幅标题的文本，并启用横幅文本模式。 |

---

## 图片与媒体

| 命令。 | 描述。 |
|---|---|
| `image: <path\|url>` | 显示一张图片（如果已经显示了图片，则将其添加到轮播图中）。 |
| `image: show` | 显示当前图像。 |
| `image: hide` | 隐藏当前图像。 |
| `image: clear` | 移除所有图片。 |
| `imagecaption: <text>` | 将标题文字设置在显示的图像下方。 |
| `video: <path\|url>` | 显示视频。支持`youtube=<id>`和`vimeo=<id>`快捷键。 |
| `video: none` | 删除视频。 |
| `webcontent: <url>` | 在网页内容区域中加载一个网址。 |
| `webcontent: none` | 移除网页内容。 |

---

## 按钮

| 命令。 | 描述。 |
|---|---|
| `button1: enable` / `button1: show` | 启用按钮 1。 |
| `button1: disable` / `button1: hide` | 禁用按钮 1。 |
| `button1text: <text>` | 更新按钮 1 的标签。 |
| `button2: enable` / `button2: show` | 启用按钮2。 |
| `button2: disable` / `button2: hide` | 禁用按钮2。 |
| `button2text: <text>` | “更新”按钮的标签2。 |
| `buttonsize: [mini\|small\|regular\|large]` | 设置按钮大小。 |
| `infobutton: <text>` | 更新“信息”按钮的标签。 |
| `infotext: <text>` | 更新信息文本区域。 |
| `infotext: disable` / `infotext: hide` | 隐藏信息文本。 |
| `infotext: reset` / `infotext: clear` | 清除信息文本中的值。 |

---

## 信息框

| 命令。 | 描述。 |
|---|---|
| `infobox: <text>` | 替换信息框的内容。支持 Markdown 格式。 |
| `infobox: + <text>` | 将内容添加到现有的信息框中。 |
| `infobox: /path/to/file.md` | 从本地的 Markdown 文件中加载信息框的内容。 |

---

## 进度条

| 命令。 | 描述。 |
|---|---|
| `progress: <int>` | 将进度条设置为特定的步骤值。 |
| `progress: increment` | 将进度条增加一个单位。 |
| `progress: increment <n>` | 增加进度条的数值，每次增加`n`个单位。 |
| `progress: complete` | 将进度条设置为最大值。 |
| `progress: reset` / `progress: indeterminate` | 将进度条重置为不确定状态。 |
| `progress: show` / `progress: enable` / `progress: create` | 显示进度条。 |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | 隐藏进度条。 |
| `progresstext: <text>` | 更新进度条下方的标签。 |

---

## 列表

| 命令。 | 描述。 |
|---|---|
| `list: <csv>` | 用新的、以逗号分隔的项目替换掉列表中的内容。 |
| `list: clear` | 清除列表中的所有项目，并隐藏列表。 |
| `list: show` | 显示列表。 |
| `list: hide` | 隐藏列表，但不清除其内容。 |

### 更新列表项

通过标题更新现有条目（简单表单）：

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

使用逗号分隔的属性来完全控制地更新一个条目：

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

将一个新的项目添加到列表的末尾：

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

删除项目：

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**可用的属性：** `listitem`

| 房产；财产。 | 描述。 |
|---|---|
| `title: <text>` | 按标题匹配项目。 |
| `index: <int>` | 根据索引（从0开始）匹配项目。 |
| `subtitle: <text>` | 设置项目副标题。 |
| `icon: <path\|url\|SF Symbol>` | 设置项目图标。 |
| `iconalpha: <float>` | 设置项目图标的透明度。 |
| `status: <status>` | 设置状态图标。可以选择以下选项之一：`wait`、`success`、`fail`、`error`、`pending`、`progress`，或者一个SF Symbols图标的名称（可以选择性地添加颜色后缀，例如：`lock.shield.fill-green`）。 |
| `statustext: <text>` | 设置状态标签的文本。 |
| `progress: <float>` | 设置内联进度值（显示进度条式的状态）。 |
| `action: <url>` | 当点击该项目时，将打开以下网址。 |
| `add:` | 将新项目添加到列表中。 |
| `delete:` | 删除匹配项。 |

---

## 帮助信息

| 命令。 | 描述。 |
|---|---|
| `helpmessage: <text>` | 更新帮助信息内容。支持 Markdown 格式。 |

---

## 窗户

| 命令。 | 描述。 |
|---|---|
| `width: <num>` | 更改窗口宽度。 |
| `height: <num>` | 修改窗口高度。 |
| `position: <position>` | 移动窗口。可以选择以下选项之一：`top`、`bottom`、`left`、`right`、`centre`，或者它们的组合（例如：`topright`）。 |

---

## 窗口可见性

| 命令。 | 描述。 |
|---|---|
| `activate:` | 将对话窗口置于最前层。 |
| `show:` | 显示对话窗口。 |
| `hide:` | 隐藏对话窗口。 |
| `minimize:` / `minimise:` | 将对话窗口最小化到停靠栏。 |
| `maximize:` / `maximise:` | 恢复最小化对话窗口。 |
| `blurscreen: enable` | 启用模糊屏幕效果。 |
| `blurscreen: disable` | 禁用模糊屏幕效果。 |

---

## 停靠图标

| 命令。 | 描述。 |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | 在Dock栏中显示“对话”图标。 |
| `showdockicon: <any other value>` | 隐藏停靠栏中的对话框图标。 |
| `dockicon: <file\|url>` | 将自定义图片设置为 Dock 图标。 |
| `dockicon: none` / `dockicon: default` | 恢复对话框停靠窗口的默认图标。 |
| `dockiconbadge: <text>` | 在 Dock 图标上显示一个徽章。 |
| `dockiconbadge: none` / `dockiconbadge: remove` | 移除 Dock 图标上的小红点。 |
| `bounce:` | 点击“Dock”图标一次（仅作提示）。 |
| `bounce: critical` | 持续点击“Dock”图标，直到窗口显示在最前面。 |

---

## 退出

| 命令。 | 描述。 |
|---|---|
| `quit:` | 以退出码 5 结束对话框。 |
