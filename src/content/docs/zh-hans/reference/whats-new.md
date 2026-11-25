---
title: 最新动态
description: swiftDialog 的最新功能和更新
translationSynced: 2026-11-25T05:50:32+00:00
---

## swiftDialog 2.5.6

## 修复内容：

 - 修复了一个问题，该问题在使用 JSON 文件指定图标时，即使只有一个图标，也要求图标必须位于数组中。修复了 #493。
 - 版本 2.5.5 中，点击通知会关闭对话框。 (#499)
 - 当没有用户登录时，更新对话框脚本的版本信息。由 @HowardGMac 在 https://github.com/swiftDialog/swiftDialog/pull/510 中提出。
 - 使用完整的路径来运行 `scutil` 命令（重新提交），由 @MikeRich88 提出。https://github.com/swiftDialog/swiftDialog/pull/515
 - 为“帮助图片”添加了尾部填充。
 - 为发送通知添加了必要的授权验证，如果需要的话。 (#485)
 - 修复帮助文档中关于`--textfield`的缺失选项。 #485

## 贡献：

### 更多关于处理通知的选项

 - 新增功能，允许为通知设置一个标识符，这样可以轻松地用更新的通知替换旧的通知。此外，还支持通过标识符删除特定通知，或者删除所有通知。

_示例：_

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

感谢 @chrisgrande。

### 添加了“buttonsize”作为命令行参数和控制文件变量

 - 支持迷你、小和大型按钮尺寸，使用macOS内置的尺寸。如果未指定或尺寸无效，按钮尺寸将默认为常规尺寸。
 - 支持在构建模式下调整按钮大小，以便进行测试和生成JSON文件。

按钮样式应用于`button1`、`button2`以及信息按钮。它也应用于普通布局和堆叠布局中的按钮。

 它不会调整帮助按钮的大小，该按钮的尺寸是固定的。

示例：

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

感谢 @k2graham。

### 从命令行文件中隐藏或显示对话窗口的选项

 - 将`hide:`和`show:`命令添加到命令文件中的命令列表中，用于隐藏和显示窗口。这不会阻止窗口在被隐藏时进行更新。

感谢 @fabienconus。

