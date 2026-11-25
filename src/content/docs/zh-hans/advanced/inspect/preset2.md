---
title: 预设模式 2 - 卡片模式
description: 配置：使用“检查模式”预设 2
translationSynced: 2026-11-25T05:35:44+00:00
---

该功能支持添加Logo或顶部横幅图片，并采用简洁的卡片式展示方式。非常适合用于品牌推广。

<img width="500" alt="image" src="/inspect/preset_2.png" />

```json
{
  "highlightColor" : "#34C759",
  "icon" : "SF=rectangle.split.3x1.fill",
  "items" : [
    {
      "displayName" : "Safari",
      "icon" : "/Applications/Safari.app",
      "id" : "safari",
      "paths" : [
        "/Applications/Safari.app"
      ],
      "showBundleInfo" : "all"
    },
    {
      "displayName" : "Calculator",
      "icon" : "/System/Applications/Calculator.app",
      "id" : "calculator",
      "paths" : [
        "/System/Applications/Calculator.app"
      ],
      "showBundleInfo" : "all"
    },
    {
      "displayName" : "TextEdit",
      "icon" : "/System/Applications/TextEdit.app",
      "id" : "textedit",
      "paths" : [
        "/System/Applications/TextEdit.app"
      ],
      "showBundleInfo" : "all"
    }
  ],
  "message" : "Installing applications...(example)",
  "preset" : "2",
  "title" : "App Catalog"
}
```
