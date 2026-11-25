---
title: 预设模式 4 - 吐司
description: 配置，用于使用“检查模式”预设 4
translationSynced: 2026-11-25T05:35:52+00:00
---


最小化窗口尺寸约为550x180像素，每次只显示一个项目。支持“介绍→项目→总结”的流程，所有内容都显示在同一个紧凑的窗口中。

进度模式：
 - “共享”—— 显示单个进度条，显示“已完成 X 个，总共 Y 个”（默认）。
 - "perItem" - 每个项目的进度显示不确定，完成后会自动进入下一步。

<img width="500" alt="image" src="/inspect/preset_4a.png" /> <img width="500" alt="image" src="/inspect/preset_4b.png" />


```json
{
  "highlightColor" : "#FF9500",
  "icon" : "SF=bell.badge.fill",
  "introScreen" : {
    "buttonText" : "Begin",
    "subtitle" : "Checking 3 applications...",
    "title" : "Software Check"
  },
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
  "preset" : "4",
  "summaryScreen" : {
    "buttonText" : "Close",
    "subtitle" : "All applications installed successfully.",
    "title" : "All Done"
  },
  "title" : "Background Install"
}
```
