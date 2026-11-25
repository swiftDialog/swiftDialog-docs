---
title: 修改“命令+Q”的功能
description: 自定义退出对话框的键盘快捷键
translationSynced: 2026-11-25T05:46:21+00:00
---

在 swiftDialog 1.10.2 及更高版本中，可以使用以下命令来重新映射：`--quitkey <char>`，该命令会将 `command+q` 映射到 `command +<char>`。

例如，`--quitkey x` 会禁用“命令+Q”快捷键关闭对话框的功能，但允许使用 `command+x`。

此外，如果通过命令+<char>操作关闭对话框，退出码将为`10`，这样可以检测到退出事件并采取相应的操作。

默认情况下，快捷键 `command+w`、`command+m` 以及 "command+n" 均被禁用，并且无法重新设置。