---
title: プリセット2 - カード設定
description: インスペクトモードのプリセット2を使用するための設定。
translationSynced: 2026-11-23T23:15:27+00:00
---

ロゴやトップバナー画像を表示し、カードアイテムを洗練されたデザインで表示します。ブランドイメージを重視した展開に最適です。

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
