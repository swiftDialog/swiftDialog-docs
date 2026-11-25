---
title: 布局
description: 自定义对话元素的排列和顺序
translationSynced: 2026-11-25T05:30:30+00:00
---

## 自定义视图排序

`--vieworder <csv>`

除了图片和消息内容外，窗口中的其他元素可以重新排列。

默认排序方式为：
 > 文本文件。
 > 网页内容。
 > 列表项。
 > 复选框
 > 文本输入框
 > 单选按钮。
 > 下拉菜单

 这些元素可以重新排列，以满足显示需求。可以通过指定所需的顺序，例如使用 CSV 格式的列表来定义这些元素，例如：`--vieworder "dropdown, textfield, checkbox"`。

 <img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/1b69abc7-4367-4eac-9e2d-a208ea47a60f" width="750px">