---
title: 预设 5 - 统一模式
description: 配置说明：使用“检查模式”预设 5
translationSynced: 2026-11-25T05:35:58+00:00
---

自助服务门户预设：带有品牌标识的网页视图，可选身份验证功能。

支持：
- 可选的、基于 SwiftUI 的开场和结束界面，用于品牌化的设置流程。
- 简单的、未经身份验证的网址（例如，SOFA、文档）。
- 经过身份验证的门户网站，支持令牌注入。
- 通过移动设备管理（MDM）应用配置，实现多品牌主题定制。

流程：启动界面（可选）→ 门户网页视图 → 结束界面（可选）。

<img width="500" alt="image" src="/inspect/preset_5a.png" /> <img width="500" alt="image" src="/inspect/preset_5b.png" />


```json
{
  "highlightColor" : "#007AFF",
  "introSteps" : [
    {
      "content" : [
        {
          "content" : "This is a two-step starter. Edit config.json to add more steps, change layouts, or customise the content.",
          "type" : "text"
        },
        {
          "items" : [
            "Step types: intro, deployment, carousel, guide, showcase, bento, processing, portal, outro",
            "55+ content block types available",
            "Add branding, forms, compliance checks"
          ],
          "type" : "bullets"
        }
      ],
      "continueButtonText" : "Next",
      "heroImage" : "SF=macbook.gen2",
      "heroImageSize" : 180,
      "id" : "welcome",
      "showBackButton" : false,
      "stepType" : "intro",
      "subtitle" : "Your starter Preset 5 workflow (example)",
      "title" : "Welcome"
    },
    {
      "continueButtonText" : "Finish",
      "heroImage" : "SF=arrow.down.app.fill",
      "id" : "apps",
      "items" : [
        {
          "displayName" : "Safari",
          "guiIndex" : 0,
          "icon" : "/Applications/Safari.app",
          "id" : "safari",
          "paths" : [
            "/Applications/Safari.app"
          ]
        },
        {
          "displayName" : "Calculator",
          "guiIndex" : 1,
          "icon" : "/System/Applications/Calculator.app",
          "id" : "calculator",
          "paths" : [
            "/System/Applications/Calculator.app"
          ]
        },
        {
          "displayName" : "TextEdit",
          "guiIndex" : 2,
          "icon" : "/System/Applications/TextEdit.app",
          "id" : "textedit",
          "paths" : [
            "/System/Applications/TextEdit.app"
          ]
        }
      ],
      "showBackButton" : true,
      "stepType" : "deployment",
      "subtitle" : "Simulated deployment step",
      "title" : "App Installation"
    }
  ],
  "preset" : "5"
}
```