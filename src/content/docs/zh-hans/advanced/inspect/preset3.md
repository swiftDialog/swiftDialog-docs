---
title: 预设3 - 紧凑型
description: 配置：使用检查模式预设 3
translationSynced: 2026-11-25T05:35:47+00:00
---

这是一种精简的列表布局，顶部可以放置Logo或横幅图片。它能够自动滚动显示项目，并突出显示当前已安装的项目。

<img width="500" alt="image" src="/inspect/preset_3.png" />

```json
{
  "highlightColor" : "#5856D6",
  "icon" : "SF=list.bullet.rectangle.fill",
  "items" : [
    {
      "displayName" : "Safari",
      "icon" : "/Applications/Safari.app",
      "id" : "safari",
      "paths" : [
        "/Applications/Safari.app"
      ]
    },
    {
      "displayName" : "Calculator",
      "icon" : "/System/Applications/Calculator.app",
      "id" : "calculator",
      "paths" : [
        "/System/Applications/Calculator.app"
      ]
    },
    {
      "displayName" : "TextEdit",
      "icon" : "/System/Applications/TextEdit.app",
      "id" : "textedit",
      "paths" : [
        "/System/Applications/TextEdit.app"
      ]
    }
  ],
  "message" : "Installing essentials...(example)",
  "preset" : "3",
  "secondaryColor" : "#AF52DE",
  "title" : "Quick Install"
}
```

