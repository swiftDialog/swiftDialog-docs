---
title: 命令行选项
description: swiftDialog 命令行的所有选项和参数的完整参考指南
translationSynced: 2026-11-25T05:17:42+00:00
---

对话功能可以通过命令行选项进行配置。所有选项也可以通过[JSON配置文件](/zh-hans/advanced/json-configuration)来指定。

```sh
dialog --title "Hello" --message "World"
```

使用 `--help <option>` 获取关于特定论点的详细信息。

---

## 内容

| 选项 | 简写 | 描述 |
|---|---|---|
| `--title <text>` | `-t` | 设置对话框的标题。使用`none`来隐藏。 |
| `--subtitle <text>` | | 在标题下方显示第二行文本。也用作[通知](/zh-hans/advanced/notifications))的副标题文本。 |
| `--message <text>` | `-m` | 设置对话消息。支持 Markdown 语法。](/zh-hans/basic-use/markdown) |
| `--messagealignment [left\|centre\|right]` | | 消息的水平对齐方式。 |
| `--messageposition [top\|centre\|bottom]` | | 消息内容块的垂直位置。 |
| `--titlefont <params\|json>` | | 修改标题字体。 接受逗号分隔的参数对，或者 JSON 对象：`key=value`, `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow`。 |
| `--messagefont <params\|json>` | | 修改消息字体。接受逗号分隔的`key=value`参数对，或JSON对象。 |

详情请参见“[标题](/zh-hans/basic-use/title)”和“[消息](/zh-hans/basic-use/message)”。

---

## 图标

| 选项 | 简写 | 描述 |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | 设置对话框图标。支持文件路径、URL、SF Symbols（`SF=name`）、内置图标或 JSON 对象。 |
| `--iconsize <num>` | | 图标大小，单位为点（默认值为150）。 |
| `--iconalpha <num>` | | 图标的透明度范围从 0.0（完全透明）到 1.0（完全不透明）。 |
| `--iconalttext <text>` | | 图标的可访问性标签。 |
| `--overlayicon <file\|url\|json>` | `-y` | 图标的右下角会显示一个覆盖层图像。它支持与`--icon`相同的图像格式。 |
| `--hideicon` | `-h` | 隐藏图标以增大消息显示区域。 |
| `--centreicon` / `--centericon` | | 将图标重新定位，使其位于标题和消息的中心位置。 |

请查看[图标](/zh-hans/basic-use/icon))以获取详细信息。

---

## 横幅和背景

| 选项 | 简写 | 描述 |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | 在对话框的顶部显示一个横幅图片。 |
| `--bannertitle <text>` | | 在横幅上显示标题文本。 |
| `--bannertext <text>` | | 相当于设置`--bannertitle`和`--title`。 |
| `--bannerheight <num>` | | 设置横幅的高度。 |
| `--background <file>` | `-bg` | 设置背景图片/水印。 |
| `--bgalpha <num>` | `-ba` | 背景图像的透明度（默认值：0.5）。 |
| `--bgposition <position>` | `-bp` | 背景图片的位置（例如：`center`, `topleft`）。 |
| `--bgfill [fill\|fit]` | `-bf` | 背景图片填充模式。 |
| `--bgscale [fill\|fit]` | `-bs` | 背景图像的缩放模式。 |
| `--screenbackground <file\|url>` | | 在对话窗口的后面，全屏显示一张图片。 |

详情请参见[横幅图片](/zh-hans/advanced/banner-images))和[背景图片](/zh-hans/advanced/background-images))。

---

## 按钮

| 选项 | 简写 | 描述 |
|---|---|---|
| `--button1text <text>` | | 按钮 1 的标签（与“返回”键绑定，默认值：`OK`）。 |
| `--button1action <url>` | | 当按钮 1 被点击时，将打开以下网址。 |
| `--button1shellaction <cmd>` | | 当按钮 1 被点击时，要执行的 shell 命令。 |
| `--button1symbol <sf symbol\|json>` | | 按钮 1 的 SF 符号或 JSON 对象。 |
| `--button1disabled` | | 启动时，禁用按钮 1。 |
| `--button2` | `-2` | 显示按钮 2。 |
| `--button2text <text>` | | 按钮 2 的标签（默认绑定到 Esc ⎋ 键：`Cancel`）。 |
| `--button2symbol <sf symbol\|json>` | | 按钮 2 的 SF 符号或 JSON 对象。 |
| `--button2disabled` | | 启动时禁用按钮 2。 |
| `--infobutton` | `-3` | 显示信息按钮。 |
| `--infobuttontext <text>` | | 信息按钮的标签。 |
| `--infobuttonaction <url>` | | 点击信息按钮时打开的网址。 |
| `--infobuttonsymbol <sf symbol\|json>` | | 用于信息按钮的 SF 符号或 JSON 对象。 |
| `--buttonstyle [center\|stack]` | | 按钮布局样式。 |
| `--buttonsize [mini\|small\|regular\|large]` | | 按钮尺寸。 |
| `--buttontextsize <num>` | | 按钮标签字体大小。 |
| `--quitoninfo` | | 当点击“信息”按钮时，显示退出对话框。 |

请参阅[按钮](/zh-hans/basic-use/buttons))以获取详细信息。

---

## 工作流程

| 选项 | 简写 | 描述 |
|---|---|---|
| `--nextbuttontext <text>` | | 工作流“下一步”按钮的标签（默认值：`Next`）。 |
| `--previousbuttontext <text>` | | 工作流程中的“上一步”按钮的标签（默认值：`Previous`）。 |
| `--onadvance <command>` | | 用于在工作流程页面之间切换时执行的 Shell 命令 <br> (输入通过标准输入；非零退出码会阻止页面切换)。 |

请参阅 [工作流程](/zh-hans/advanced/workflows)) 以获取详细信息。

---

## 帮助信息

| 选项 | 简写 | 描述 |
|---|---|---|
| `--helpmessage <text>` | | 显示一个带有弹出窗口内容的帮助按钮。支持 Markdown 格式。 |
| `--helpimage <file\|url>` | | 为帮助提示框添加一张图片。 |
| `--helpsheetbuttontext <text>` | | 帮助文档页面的“关闭”按钮的标签（默认值：`OK`）。 |
| `--helpalignment [left\|centre\|right]` | | 帮助信息内容的对齐。 |

请参阅[帮助信息](/zh-hans/operation/help-message))以获取详细信息。

---

## 图片、视频和网页内容

| 选项 | 简写 | 描述 |
|---|---|---|
| `--image <file\|url>` | `-g` | 显示一张图片。 多个实例可以创建轮播效果。 |
| `--imagecaption <text>` | | 图像下方显示的说明文字。 |
| `--video <file\|url>` | | 显示视频。支持`youtube=<id>`和`vimeo=<id>`快捷键。 |
| `--videocaption <text>` | | 视频下方显示的文字说明。 |
| `--autoplay` | | 启动时自动播放视频。 |
| `--webcontent <url>` | | 在消息区域显示网页。 |

详情请参见图片、视频和网页内容。](/zh-hans/basic-use/images) ](/zh-hans/basic-use/video) ](/zh-hans/basic-use/web-content)

---

## 信息区域

| 选项 | 简写 | 描述 |
|---|---|---|
| `--infotext <text>` | | 将信息按钮替换为静态文本。 |
| `--infobox <text>` | | 在图标下方显示文本（支持 Markdown 格式）。 |
| `--infoboxwidth <num>` | | 独立设置信息框的宽度，使其与图标的大小无关。 |

请参阅[信息框](/zh-hans/advanced/info-box))以获取详细信息。

---

## 用户输入

| 选项 | 简写 | 描述 |
|---|---|---|
| `--textfield <text\|json>[,options]` | | 添加一个文本输入框。支持 `required`、`secure`、`prompt`、`regex`、`fileselect`、`date`、`time`、`mindate`、`maxdate` 等多种格式，也可以指定为 JSON 对象。 |
| `--textfieldlivevalidation` | | 在文本输入框中实时显示正则表达式验证的反馈结果。 |
| `--checkbox <text\|json>` | | 添加一个带有指定标签的复选框。 也可以以 JSON 对象的形式指定。 |
| `--checkboxstyle [checkbox\|switch][,size]` | | 更改复选框的显示样式。 |
| `--selecttitle <text>[,options]` | | 添加一个名为指定名称的下拉选择列表。 |
| `--selectvalues <csv>` | | 用于下拉列表的以逗号分隔的值。 |
| `--selectdefault <text>` | | 下拉列表的默认选中值。 |
| `--selectstyle` | | 用于下拉列表的样式。 |
| `--selectitem <json>` | | 使用 JSON 对象语法定义一个选中的列表项。 |

详情请参见“文本字段”、“复选框”和“下拉列表”。](/zh-hans/advanced/textfields) ](/zh-hans/advanced/checkboxes) ](/zh-hans/advanced/select-lists)

### 每个论点的 JSON 配置

许多可以接受逗号分隔值的参数，也可以指定为 JSON 对象。 这种方式提供更直接的控制，尤其适用于复杂的配置。

**检测：** 如果某个值可以解析为 JSON 对象，则使用 JSON 解析器；否则，应用 CSV 解析。

**支持的论点：**
- `--textfield` - 完整的字段配置，包含所有修饰符。
- `--checkbox` - 带图标的复选框，以及按钮的启用/禁用功能。
- `--listitem` - 带有嵌套图标的列表项。
- `--selecttitle` - 采用与 `--selectitem` 相同的处理方式。
- `--selectitem` - 使用 JSON 定义的下拉列表项。
- `--titlefont` / `--messagefont` - 字体配置，包括颜色、大小、粗细和阴影。
- `--icon` / `--overlayicon` - 包含符号、颜色、调色板和动画的图标对象。
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - 按钮符号及其位置。

请参考各个文档页面，其中提供了详细的 JSON 模式和示例。

---

## 项目列表

| 选项 | 简写 | 描述 |
|---|---|---|
| `--listitem <text\|json>` | | 添加一个列表项。支持状态图标和点击操作。也可以指定为包含嵌套图标的 JSON 对象。 |
| `--liststyle [expanded\|compact]` | | 列表行之间的垂直间距。 |
| `--enablelistselect` | | 允许选择列表中的项目；选择结果将在退出时返回。 |

请参考[物品列表](/zh-hans/advanced/item-lists))获取详细信息。

---

## 定时器与进度

| 选项 | 简写 | 描述 |
|---|---|---|
| `--timer [<seconds>]` | | 显示倒计时器（默认值为10秒）。如果超时，程序将以代码4退出。 |
| `--hidetimerbar` | | 在计时器仍在倒计时时，隐藏计时条。 |
| `--hidetimer` | | 完全隐藏计时器。 |
| `--progress [<int>]` | | 显示一个进度条，该进度条包含指定数量的步骤。 |
| `--progresstext <text>` | | 在进度条下方显示初始文本。 |

详情请参见[计时器和进度条]](/zh-hans/advanced/timer-progress)。

---

## 窗口大小和位置

| 选项 | 简写 | 描述 |
|---|---|---|
| `--width <num>` | | 对话框的宽度，单位为点。 |
| `--height <num>` | | 对话框的高度，单位为像素。 |
| `--small` | `-s` | 将默认窗口大小减少25%。 |
| `--big` | `-b` | 将默认窗口大小增加25%。 |
| `--position <position>` | | 窗口位置（例如：`center`、`topright`或`x,y`）。 |
| `--positionoffset <int>` | | 使用`--position`时，边缘偏移量（默认值为：16）。 |
| `--moveable` | `-o` | 允许拖动窗口。 |
| `--resizable` | | 允许调整窗口大小（隐含 `--moveable`） |
| `--ontop` | `-p` | 始终将该窗口置于其他窗口之上。 |
| `--windowbuttons [close,min,max]` | | 启用窗口的关闭、最小化和最大化按钮。 |
| `--showonallscreens` | | 在所有已连接的屏幕上显示窗口。 |
| `--appearance [dark\|light]` | | 覆盖窗口外观。 |

有关详细信息，请参阅 [窗口大小](/zh-hans/advanced/window-size) 和 [布局](/zh-hans/advanced/layout)。

---

## 窗户样式预设

| 选项 | 简写 | 描述 |
|---|---|---|
| `--style <preset>` | | 应用预设样式：`presentation`、`mini`、`centered`、`alert`、`caution`、`warning`。 |
| `--mini` | | 一个紧凑的窗口，显示标题、图标以及两行文字信息。 |
| `--fullscreen` | `-f` | 全屏模式（没有按钮显示；键盘操作仍然有效）。 |
| `--presentation` | | 带有进度条和结构化布局的演示模式。 |
| `--eula` | | 以用户协议（EULA）接受模式显示。 |
| `--blurscreen` | | 模糊显示对话窗口背后的所有屏幕内容。 |
| `--hideotherapps` | | 启动时隐藏所有其他应用程序。 |

有关详细信息，请参阅 [全屏显示](/zh-hans/advanced/full-screen) 和 [演示](/zh-hans/advanced/presentation)。

---

## 通知

| 选项 | 简写 | 描述 |
|---|---|---|
| `--notification` | | 发送一个macOS系统通知。 |
| `--identifier <text>` | `-id` | 用于唯一标识通知的ID。 |
| `--remove` | | 移除与指定内容相匹配的通知。`--identifier` |
| `--enablenotificationsounds` | | 启用通知声音。 |

详情请参见[通知](/zh-hans/advanced/notifications))。

---

## 声音

| 选项 | 简写 | 描述 |
|---|---|---|
| `--sound <file\|url>` | | 启动时播放音频文件。 |
| `--showsoundcontrols` | | 显示播放控制按钮（播放/暂停、静音、时间轴）。 |

---

## 停靠图标

| 选项 | 简写 | 描述 |
|---|---|---|
| `--showdockicon` | | 在 macOS 的 Dock 中显示“对话”图标。 |
| `--dockicon <file\|url>` | | 显示自定义图片作为 Dock 图标（隐含功能 `--showdockicon`）。 |
| `--dockiconbadge <text>` | | 在 Dock 栏中可见的图标上显示一个徽标。 |

---

## 命令文件

| 选项 | 简写 | 描述 |
|---|---|---|
| `--commandfile [<file>]` | | 实时对话更新的命令文件路径（默认值：`/var/tmp/dialog.log`）。 |
| `--displaylog <file>` | | 显示文件的内容，按照其原始书写顺序。 |
| `--loghistory [<int>]` | | 预先填充`--displaylog`，显示最近的N行（默认值为100行）。 |

请参阅[命令文件](/zh-hans/advanced/command-file))以获取详细信息。

---

## JSON 输入和输出

| 选项 | 简写 | 描述 |
|---|---|---|
| `--jsonfile <file>` | | 从JSON文件中加载对话配置。 |
| `--jsonstring <text>` | | 从 JSON 字符串中加载对话配置。 |
| `--json` | `-j` | 输出结果采用JSON格式。 |

请参阅 [JSON 配置文件](/zh-hans/advanced/json-configuration)) 以获取详细信息。

---

## 键盘与交互

| 选项 | 简写 | 描述 |
|---|---|---|
| `--quitkey <char>` | | 自定义退出键（用作 `⌘ + <key>`，默认值：`q`） |
| `--hidedefaultkeyboardaction` | | 要求`⌘ + ⇧`触发“返回”/“退出”键盘操作。 |
| `--alwaysreturninput` | | 无论退出代码是什么，程序都应始终将用户的输入返回。 |
| `--ignorednd` | `-d` | 即使在“请勿打扰”模式下，也显示对话框。 |
| `--vieworder <csv>` | | 覆盖输入元素类型的显示顺序。 |

---

## 授权

| 选项 | 简写 | 描述 |
|---|---|---|
| `--key <string>` | `-k` | 启动对话框需要提供身份验证密钥。 |
| `--checksum <string>` | | 生成一个 SHA256 哈希值（用于与 `--key` 配合使用）。 |

请参阅[授权说明](/zh-hans/operation/authorization))以获取详细信息。

---

## 登录窗口

| 选项 | 简写 | 描述 |
|---|---|---|
| `--loginwindow` | | 在登录窗口显示对话框（需要相应的启动代理）。 |

请参阅[登录窗口](/zh-hans/operation/login-window))获取详细信息。

---

## 检查模式

| 选项 | 简写 | 描述 |
|---|---|---|
| `--inspect-mode` | | 以检查模式启动。 |
| `--inspect-config <file>` | | 指定检查模式的配置。 |
| `--inspect-schema <file>` | | 指定用于检查模式的模式。 |
| `--schema-validate <file>` | | 验证配置是否符合预定义的模式。 |

详情请参见“检查模式”](/zh-hans/advanced/inspect-mode)。

---

## 实用工具与调试

| 选项 | 简写 | 描述 |
|---|---|---|
| `--version` | `-v` | 打印版本字符串。 |
| `--help [<argument>]` | | 打印帮助信息，或打印关于特定参数的详细帮助信息。 |
| `--licence` | `-l` | 打印许可证。 |
| `--debug [<colour>]` | | 启用调试模式，并可选择性地显示内容边界高亮。 |
| `--verbose` | `-vvv` | 启用详细的日志输出。 |
| `--listfonts` | | 打印可用的字体名称。 |
| `--demo` | | 以演示模式启动。 |
| `--builder` | | 启动构建工具的用户界面。 |
| `--jh` | `-jh` | 启用 jamfHelper 的兼容模式。 |

详情请参见[Builder](/zh-hans/reference/builder))。
