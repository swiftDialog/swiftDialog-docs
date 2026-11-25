---
title: 信息框
description: 在次要内容区域中显示更多信息
translationSynced: 2026-11-25T05:27:13+00:00
---

## 信息框 - `--infobox`

信息框是图标下方显示的那一区域。

它使用一种次要的颜色来显示较小的字体，这对于显示诸如系统信息等辅助信息非常有用。

`--infobox` 接受任何使用 Markdown 格式的文本。

#### 示例：

`--infobox "### Additional Info\n\n#### Item 1  \n - Point one  \n - Point two  \n#### Item 2  \n - Point three  \n - Point four"`

![截图 2024-09-10 晚上 4:13:59 ](https://github.com/user-attachments/assets/d78c2abc-976b-4bb7-b6e8-ff0c487cfe01)

## 信息框宽度 - `--infoboxwidth`

默认情况下，信息框的宽度与图标列的宽度相同。`--infoboxwidth <number>` 可以独立于图标的大小设置信息框文本区域的宽度（以点为单位），这样您就可以扩大信息框的宽度，而无需放大图标。

`--infoboxwidth 300`