---
title: jamfHelper 技术支持
description: 将 swiftDialog 作为 jamfHelper 的替代方案，直接替换使用
translationSynced: 2026-11-25T05:43:58+00:00
---

Dialog 现在可以通过新的 `--jh` 标志，支持接收一些基本的 jamfHelper 格式的命令行选项。

这使得将其集成到现有的工作流程和脚本中变得更容易，只需将对 `/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper` 的调用替换为对 `/usr/local/bin/dialog --jh` 的调用即可。

使用该标志会指示对话框将 `jamfHelper` 的选项转换为等效的对话框选项。并非所有选项都受到支持。 那些在 `jamfHelper` 中没有等效项的标准对话框选项仍然可用，例如 `--width`、`--height` 和 `--image`。

<br/>

## 功能和行为

***
### 已实施

#### `-windowType [hud | utility | fs]`

`hud` 和 `utility` 会被忽略。 `fs` 会被转换为对话框 `--fullscreen`，并在对话框的全屏视图中显示。

#### `-windowPosition [ul | ll | ur | lr]`

将窗口定位在用户屏幕的右上角、左上角、右下角或左下角。 这是目前“对话框”标准选项中没有的功能，但为了与 jamfHelper 兼容而实现的。

#### `-title "string"`
已转换为 `--title`。

将窗口的标题设置为指定的字符串。

#### `-heading "string"` 和 `-description "string"`
已转换为 `--message`。

Both `-heading` and `-description` are merged into dialogs `--message` option. `-heading` is converted into a markdown heading 4 `####` then a blank newline followed by `-description`

#### `-icon path`
已转换为 `--icon`。

如果未提供相关参数，则强制对话框选项与 `jamfHelpers` 的行为一致，即在未指定 `idon` 值时，不显示 `idon`。`--hideicon`

#### `-button1 "string"`
已转换为 `--button1text`。

**_行为变更：_** 对话框始终显示默认按钮，这与 jamfHelper 的工作方式不同。默认按钮的文本是 `OK`。

#### `-button2 "string"`
已转换为 `--button2text`。

#### `-alignDescription [right | left | center | justified | natural]`
已转换为 `--alignment`。

目前已实现的选项仅有 `right`、`centre` 和 `left`。

#### `-timeout int` 和 `-countdown`
已转换为 `--timer`。

`-countdown` 总是默认存在，因为对话框总是显示计时器条的超时状态，而如果未实现计时器条，则无法显示超时状态。

<br/>

***
### 未实现

#### `-defaultButton [1 | 2]`
默认按钮始终是按钮 1。

#### `-cancelButton [1 | 2]`
“取消”按钮始终是第二个按钮（如果显示的话）。

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`