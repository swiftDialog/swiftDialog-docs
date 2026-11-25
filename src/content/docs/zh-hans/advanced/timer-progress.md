---
title: 计时器和进度条
description: 创建带有倒计时器和交互式进度条的对话框
translationSynced: 2026-11-25T05:27:06+00:00
---

对话可以由一个定时器启动，当计时器达到设定的秒数时，对话将自动关闭。

`--timer (<seconds>)`


将默认按钮替换为倒计时器，倒计时结束后，对话框将以退出码 `4` 关闭。默认倒计时值为 `10` 秒。可以选择指定 `<seconds>` 值来设置所需的倒计时时间。如果 `<seconds>` 大于 60，则倒计时将以 `HH:MM:SS` 格式显示，例如，280 秒将显示为 `4:40` (用于初始倒计时)。

如果与`--button1text`一起使用，默认按钮将显示，但在计时器开始后的前3秒内，该按钮将被禁用。之后，该按钮将变为可用状态，可以用于通过标准按钮1以退出码0的方式关闭对话框。

<img width="727" alt="image" src="https://user-images.githubusercontent.com/3598965/129475759-9ba50127-8366-46a3-8288-780298142f09.png">


`--hidetimerbar` 将隐藏进度条和倒计时显示。

这样做可以确保默认按钮始终可见，以防止出现无法关闭的对话框，并且在对话框中提供计时器到期的明确提示。

---

## 进度条

Dialog 可以显示一个交互式进度条，该进度条可以通过 [命令文件](/zh-hans/advanced/command-file)) 动态更新。

`--progress [<int>]`

显示一个进度条，其中包含指定数量的步骤。 如果未指定任何值，则默认值为 10 个步骤。

为了推进进度条，请向对话框的命令文件发送一个命令：

```sh
echo "progress: <int>" >> /var/tmp/dialog.log
```

`--progresstext <text>`

设置进度条下方最初显示的文本。 文本可以随时更新。

```sh
echo "progresstext: Installing software..." >> /var/tmp/dialog.log
```

### 文本进度对齐

`--progresstextalignment [left | right]`

设置进度条下方显示文本的水平对齐方式。默认值为居中。