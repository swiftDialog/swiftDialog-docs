---
title: Shell 命令
description: 一个实验性功能，允许通过按钮操作来执行 shell 命令
translationSynced: 2026-11-25T05:44:12+00:00
---

v1.1.2版本引入了一个实验性功能，可以通过`button1shellaction`命令来使用。


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

它接受一个字符串参数，并将该参数传递给 shell 环境进行执行，例如：

` --button1shellaction "say thank you for running dialog"`

目前没有输入过滤或输出过滤功能。如果指定的命令以错误状态退出，Dialog 仍然会以退出码 1 结束 `0`。命令的状态信息会显示在屏幕上，包括命令的退出码，例如：

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

命令的输出结果将直接通过标准输出流显示，您可以根据需要查看或解析这些结果。

## 其他按钮的快捷操作

按钮2（取消）和按钮3（信息）分别会以代码2和3结束对话框。这些退出代码可以被检测和解析。如果管理员希望在处理上述操作后在 shell 中执行某些操作，建议捕获对话框的退出状态，并根据状态进行相应的处理。

## 注意事项

该命令不会在后台运行，因此在命令执行期间，对话框会显示出来，但用户无法进行操作。命令执行完成后，对话框将自动关闭。 如果您想要执行一个可能需要较长时间才能完成的命令，请注意这一点。

该 shell 命令也会继承调用它的进程的权限。如果从 root 用户身份执行 Dialog，那么该 shell 命令也将拥有 root 权限。