---
title: 系统要求
description: swiftDialog 的 macOS 版本要求和兼容性
translationSynced: 2026-11-25T04:59:05+00:00
---

## macOS 系统要求

swiftDialog 是一个使用 SwiftUI 编写的通用二进制应用程序。

### 3.0+
- **最低macOS版本：** macOS 15 (Sonoma)
- **架构：** 通用二进制格式（支持 Intel 和 Apple Silicon 芯片）
- **框架：** SwiftUI

### 2.3+
- **最低macOS版本：** macOS 12 (Monterey)

### 旧版本
- 支持 **macOS 11 (Big Sur)** 的最新版本是 [v2.2.1](https://github.com/swiftDialog/swiftDialog/releases/tag/v2.2.1)


## 依赖关系

swiftDialog 是一个独立的应用程序，不依赖于任何外部组件。它包含了应用程序包中所有必要的框架。

## 权限

swiftDialog 在使用时可能需要某些权限，具体取决于使用方式。

### 基本操作
- 无需任何特殊权限即可显示基本的对话框。

### 高级功能
- **通知：** 用户必须授予系统通知权限，才能接收系统通知。
- **完全磁盘访问权限：** 如果需要读取或写入受保护的区域，可能需要授予此权限。

## 网络需求

- **离线操作：** swiftDialog 可以在完全离线状态下运行。
- **在线运营：**
  - 检查更新。
  - 显示网页内容。
  - 下载远程图片。
