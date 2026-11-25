---
title: 开始使用 swiftDialog
description: swiftDialog 是一款现代化的 macOS 对话框工具，专为管理员设计
translationSynced: 2026-11-25T04:50:42+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialog 欢迎示例](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

swiftDialog 的设计目的是作为一个辅助工具，供 macOS 管理员通过脚本使用。它能够弹出一个对话框，向用户展示信息，并报告用户所采取的操作。这些信息随后可以用于进一步的脚本处理，或者仅仅用于显示某些信息。

swiftDialog 可以通过命令行接收输入，并接受一个或多个命令行选项](/zh-hans/advanced/command-line-options/)，用于告诉 swiftDialog 要显示什么内容以及如何显示。

有很多可供选择的选项，可以用来定制您想要显示的内容。这些选项范围从非常简单的信息展示，到更复杂的处理功能，包括文本输入、下拉列表、图像显示等等。

## 运行 swiftDialog

从 [releases](https://github.com/swiftDialog/swiftDialog/releases) 页面获取的 **.pkg** 安装程序会将 swiftDialog 安装到 `/usr/local/bin/dialog`，该路径通常也在 macOS 的默认 `$PATH` 中。

要从你的脚本中调用对话，你可以使用完整的路径，或者依赖于 $PATH。

```bash
$ dialog --title ...
```

或者

```bash
$ /usr/local/bin/dialog --title ...
```

在最基本的情况下，`dialog` 可以直接使用 `--title` 和 `--message` 命令行选项，以显示包含所需信息的对话框。

swiftDialog 可以实现更多功能，建议您阅读“[命令行选项](/zh-hans/advanced/command-line-options/)”页面，以获取所有可用选项的完整列表，或者使用 `dialog` 命令并带上 `--help` 选项。

## 快速链接

### 基本功能

- [自定义 swiftDialog 的标题](/zh-hans/basic-use/title/)
- [自定义 swiftDialog 的消息显示方式](/zh-hans/basic-use/message/)
- [自定义 swiftDialog 中图标区域显示的图像](/zh-hans/basic-use/icon/)
- [添加横幅图片](/zh-hans/advanced/banner-images/)
- [自定义按钮及其行为方式](/zh-hans/basic-use/buttons/)

### 高级功能

- [信息框](/zh-hans/advanced/info-box/)
- [横幅图片](/zh-hans/advanced/banner-images/)
- [帮助信息](/zh-hans/operation/help-message/)
- [下拉菜单和单选按钮](/zh-hans/advanced/select-lists/)
- [文本输入](/zh-hans/advanced/textfields/)
- [复选框](/zh-hans/advanced/checkboxes/)
- [带有进度条的计时器](/zh-hans/advanced/timer-progress/)
- [窗口大小和行为](/zh-hans/advanced/window-size/)
- [全屏模式](/zh-hans/advanced/full-screen/)
- [演示模式](/zh-hans/advanced/presentation/)
- [项目列表](/zh-hans/advanced/item-lists/)
- [系统通知](/zh-hans/advanced/notifications/)
- [Command-Q 行为](/zh-hans/operation/command-q/)
- [内置变量](/zh-hans/operation/builtin-variables/)

## 支持

swiftDialog 的开发初衷部分是为了学习如何使用 SwiftUI 编写应用程序，另一部分是为了满足一种需求，即找到一种向 macOS 用户传递信息的方式，并且这种方式符合我的个人喜好。

可以提供支持，方法是[提交问题报告](https://github.com/swiftDialog/swiftDialog/issues)。我们也欢迎用户提出功能建议。

## 联系方式

您可以联系作者，在 [Macadmins slack](https://www.macadmins.org/slack) 的 #swiftdialog 频道中（用户名 @bartreardon，通常在 #anzmac 频道）。但是，请将任何技术支持问题或一般性问题限制在 GitHub 上，至少这样可以追踪和解决您的问题。 谢谢！😃
