---
title: 容易犯的错误
description: swiftDialog 常见问题及故障排除技巧
translationSynced: 2026-11-25T05:47:21+00:00
---

# 命令文件问题

## 权限不足

如果您启动 swiftDialog，并且无法写入命令文件，您将收到一个错误提示。

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

应该删除该命令文件，或者修改其权限设置为 `-rw-rw-rw` (666)。

---

# swiftDialog 3.1.1 版本行为变更说明

## `--alwaysreturninput` 所有退出路径的回报

**变化内容：** 从版本 3.1.1 开始，`--alwaysreturninput` 会在所有退出途径下（而不仅仅是点击按钮时）返回选择、列表或 JSON 格式的结果。

**受影响的退出路径：**
- 命令文件，退出。
- 定时器超时。
- 退出键按下。
- 已终止进程。

**迁移：** 依赖于旧行为（仅在按钮按下时返回结果）的脚本可能会产生新的输出。 如果您使用了 `--alwaysreturninput`，请检查您的解析逻辑。

## `--ontop` 尊重泊位位置

**变更内容：** `--ontop` 选项现在会考虑停靠栏的位置，并将对话框放置在屏幕区域内（而不是停靠栏的上方）。

**影响：** 当使用该功能时，对话框将不再遮挡底座。这撤销了早期版本中一项有意识的决策。`--ontop`

## 日期选择器修饰符

**变更内容：** `isdate` 修饰符已被**废弃**，取而代之的是 `date` 和 `time`。

**迁移：** 更新您的脚本。

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# 常见问题

## 可重复使用的选项作为最后一个参数

**问题：** 作为最终参数使用的可重复选项（`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`）可能导致程序崩溃。

**状态：** 已在 3.1.1 版本中修复。

## 日期选择器未返回任何值

**问题：** 使用 `--textfield ...,isdate` 没有返回任何值，因为它是用于构建框架的代码，该代码本身不返回任何值。

**状态：** 已在 3.1.1 版本中修复。请使用 `date` 或 `time` 修饰符。

## 图像描述功能无法正常工作

**问题：** 命令行文件 `imagecaption:` 没有起作用，因为它只写入了 `appvars.imageCaptionArray`（启动时一次性读取），而不是写入 `observedData.imageArray`（用于响应式数据源）。

**状态：** 已在 3.1.1 版本中修复。

## 预设的5个分组标题显示不正确

**问题：** 部署组的标题（例如“已完成”、“待安装”）显示在错误的位置，或者出现重复。

**状态：** 已在 3.1.1 版本中修复。

## 按钮栏键盘功能无法正常使用

**问题：** `--hidedefaultkeyboardaction` 无法正常工作，原因是按钮栏视图重写过程中出现了一个问题。

**状态：** 已在 3.1.1 版本中修复。