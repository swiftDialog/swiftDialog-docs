---
title: 预设模式 6 - 引导模式
description: 配置：使用“检查模式”预设 6
translationSynced: 2026-11-25T05:36:04+00:00
---

现代化的侧边栏导航，设计简洁。

特性：
- 垂直侧边栏导航。
- 简洁、现代的IntroStepContainer设计。
- 内容引导：用于展示丰富内容的模块。
- 外部命令文件监控。
- 支持处理状态机。
- 状态持久性。

<img width="500" alt="image" src="/inspect/preset_6a.png" />

<img width="500" alt="image" src="/inspect/preset_6b.png" />

<img width="500" alt="image" src="/inspect/preset_6c.png" />

```json
{
  "highlightColor" : "#007AFF",
  "items" : [
    {
      "displayName" : "Overview",
      "guidanceContent" : [
        {
          "content" : "Welcome to the sidebar navigation layout. Users can navigate between sections.",
          "type" : "text"
        },
        {
          "content" : "Edit config.json to add more sections, change icons, or customise the content blocks.",
          "type" : "info"
        }
      ],
      "guidanceTitle" : "Welcome",
      "icon" : "SF=house.fill",
      "id" : "overview"
    },
    {
      "displayName" : "Applications",
      "guidanceContent" : [
        {
          "content" : "This section could list available applications or provide self-service options.",
          "type" : "text"
        },
        {
          "items" : [
            "Safari — Web browser",
            "Calculator — Quick math",
            "TextEdit — Text editor"
          ],
          "type" : "bullets"
        }
      ],
      "guidanceTitle" : "Applications",
      "icon" : "SF=app.badge.fill",
      "id" : "apps"
    },
    {
      "displayName" : "Help & Support",
      "guidanceContent" : [
        {
          "content" : "Add links, contact info, or troubleshooting guides here.",
          "type" : "text"
        },
        {
          "action" : "url",
          "content" : "Open Apple Support",
          "icon" : "safari.fill",
          "type" : "button",
          "url" : "https://support.apple.com"
        }
      ],
      "guidanceTitle" : "Help & Support",
      "icon" : "SF=questionmark.circle.fill",
      "id" : "help"
    }
  ],
  "preset" : "6",
  "title" : "Service Portal"
}
```