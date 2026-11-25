---
title: 内置变量
description: 在对话框中使用动态变量来显示系统信息
translationSynced: 2026-11-25T05:45:53+00:00
---

## 内置变量

swiftDialog现在包含了一些内置变量，这些变量将自动填充主机特定的信息。请将这些变量包含在您的文本字符串中，例如：`{variablename}`。

包含的变量有：

    {computername}  - hostname of the computer {computermodel} - computer model, e.g. "Mac mini (2023)" {serialnumber}  - serial number {username}      - current username, e.g. `johndoe` {userfullname}  - full name, e.g. `John Doe` {osversion}     - macOS version, e.g. `14.4.1` {osname}        - macOS name, e.g. `Sonoma`

同样，可以通过这种方式访问任何环境变量。

    对话框 --图标：电脑 --标题：“{computermodel}” --信息：“正在运行 {osname} {osversion}” --样式：居中。

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">