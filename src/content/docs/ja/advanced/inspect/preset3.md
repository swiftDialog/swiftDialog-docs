---
title: プリセット3 - コンパクトサイズ。
description: インスペクトモードのプリセット3を使用するための設定。
translationSynced: 2026-11-23T23:15:25+00:00
---

これは、ロゴやトップバナー画像を表示する、リスト形式の簡潔なデザインです。項目は自動的にスクロールし、現在インストールされているものが強調表示されます。

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

