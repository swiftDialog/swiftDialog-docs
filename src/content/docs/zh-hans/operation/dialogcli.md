---
title: Dialog 命令行启动器
description: 对话命令行界面的二进制文件的工作原理以及常用选项
translationSynced: 2026-11-25T05:46:45+00:00
---

位于 `/usr/local/bin/dialog` 的 `dialog` 命令实际上不是 Dialog 应用程序本身，而是一个轻量级的命令行启动器（`dialogcli`），它封装了 Dialog.app 程序。了解它的作用对于使用 swiftDialog 进行部署或编写脚本很有帮助。

---

## 启动器的作用

当您运行 `dialog` 时，启动器会：

1. 该功能会定位到 `Dialog.app` 可执行文件，其位置是相对于应用程序包内的自身路径而言。
2. 如果命令文件不存在，则在`/var/tmp/dialog.log`（或使用`--commandfile`指定的路径）创建该文件。 如果指定的路径是符号链接，则启动程序会中止，以防止安全风险。
3. **确定当前图形用户界面 (GUI) 用户**，使用 `SCDynamicStoreCopyConsoleUser`。 如果没有活动的图形用户界面用户，并且未指定 `--loginwindow`，则启动器将以代码 `1` 退出。
4. **在正确的用户上下文中运行对话框。** 当以root用户身份调用时（例如，从Jamf策略或LaunchDaemon），启动器使用`launchctl asuser`以登录的图形界面用户的身份运行对话框，从而使窗口显示在正确的显示会话中。
5. **自动通过验证** — 启动器会将自身的进程ID注入其中 `--pid`，以便对话框可以监控调用进程，并在其终止时自动退出 `--pid <pid>`。
6. **样式化的通知**—— 当同时使用 `--notification` 和 `--style alert` 或 `--style banner` 时，启动器会将呼叫转发到相应的嵌入式通知辅助应用程序，而不是主 Dialog 程序。

---

## 创建符号链接

启动器包含一个 `--link` 标志，用于创建指向自身的 `/usr/local/bin/dialog` 符号链接。必须以 root 权限运行：

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

这通常由 swiftDialog 的安装包自动处理。

---

## 实用功能选项

这些选项由 Dialog 程序的二进制文件本身处理，主要用于系统管理或部署脚本。

### `--setappicon <file>`

将 swiftDialog 应用程序的图标设置为指定图像文件，然后立即退出。 这还会更新任何嵌入式通知辅助程序的图标。

```sh
dialog --setappicon /path/to/custom-icon.png
```

这是一个一次性操作，Dialog 不会显示任何窗口。 它的目的是在安装完成后进行自定义设置，以便 Dock 图标和通知与贵组织的品牌形象相符。

### `--callingpid <int>`

监控指定的进程ID。如果该进程终止，Dialog会自动退出，退出码为`40`。

```sh
dialog --title "Installing..." --callingpid 12345
```

这部分信息由`dialogcli`启动器自动注入（使用其自身的进程ID），因此如果调用脚本或进程被终止，Dialog也会退出。 您可以显式地提供一个不同的进程ID，但这会将Dialog与不同的进程关联，但这种用法目前不受支持。

当被监控的进程终止时，Dialog 程序退出，会返回错误代码 40。
