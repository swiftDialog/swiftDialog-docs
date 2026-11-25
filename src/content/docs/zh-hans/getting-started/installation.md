---
title: 安装
description: 如何在macOS上安装swiftDialog
translationSynced: 2026-11-25T04:56:15+00:00
---

## 安装方法

### 安装包（推荐）

安装 swiftDialog 最简单的方法是使用来自[releases](https://github.com/swiftDialog/swiftDialog/releases)页面的 **.pkg** 安装程序。

安装程序会将 swiftDialog 放置在 `/usr/local/bin/dialog` 目录，该目录应该是 macOS 系统的默认目录 $PATH。

### 手动安装

如果您更喜欢手动安装：

1. 您可以从[releases页面](https://github.com/swiftDialog/swiftDialog/releases)下载最新版本。
2. 提取二进制文件
3. 将其复制到 `/usr/local/bin/dialog` 或您 $PATH 中的其他位置。
4. 确保该二进制文件具有执行权限：`chmod +x /usr/local/bin/dialog`

### Homebrew 安装

即将推出 - 自制配方正在开发中

## 验证

安装完成后，请确认 swiftDialog 是否正常工作：

```bash
dialog --version
```

或者，您可以尝试使用一个简单的对话来进行测试：

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## 更新 swiftDialog

要更新 swiftDialog，只需下载并安装最新版本。安装程序将替换现有版本。

您可以使用以下编程方式来检查更新：

```bash
dialog --checkupdates
```

## 卸载

要移除 swiftDialog：

```bash
sudo rm /usr/local/bin/dialog
```

## 通过移动设备管理 (MDM) 进行部署

swiftDialog 可以通过移动设备管理 (MDM) 解决方案，例如 Jamf Pro、Mosyle 或 Iru 进行部署。只需将 .pkg 安装程序部署到您的管理设备上即可。

### 示例 Jamf 策略

1. 将 swiftDialog 的 .pkg 文件上传到 Jamf Pro。
2. 制定一个策略，用于部署该软件包。
3. 针对您想要的设备进行配置。
4. 设置触发器（例如：签到、定期、自助服务等）。
