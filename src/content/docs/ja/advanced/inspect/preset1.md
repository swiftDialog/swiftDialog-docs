---
title: プリセット1 - 展開設定
description: 検査モードのプリセット1を使用するための設定。
translationSynced: 2026-11-23T23:15:26+00:00
---

伝統的なサイドバーレイアウトで、アイコン、進捗バー、および項目リストが表示されます。標準的なアプリケーションのインストールに最適です。

<img width="500" alt="image" src="/inspect/preset_1.png" />

```json
{
  "highlightColor" : "#007AFF",
  "icon" : "SF=arrow.down.app.fill",
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
  "preset" : "1",
  "title" : "App Deployment"
}
```
