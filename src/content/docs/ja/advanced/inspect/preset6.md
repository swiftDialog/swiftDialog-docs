---
title: プリセット6 - ガイド機能
description: インスペクトモードのプリセット6を使用するための設定。
translationSynced: 2026-11-23T23:20:12+00:00
---

洗練されたデザインの、最新のサイドバーナビゲーション。

特徴：
- 垂直方向のサイドバーナビゲーション。
- シンプルでモダンなデザインのIntroStepContainer。
- コンテンツ表示のためのガイド：リッチコンテンツ表示のためのブロック機能。
- 外部コマンドファイル監視機能。
- 処理状態機械のサポート。
- 状態の保持。

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