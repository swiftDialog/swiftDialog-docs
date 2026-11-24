---
title: プリセット4 - トースト調理モード
description: インスペクトモードのプリセット4を使用するための設定。
translationSynced: 2026-11-23T23:20:06+00:00
---


最小表示サイズは550×180ピクセルで、一度に1つの項目を表示します。 導入画面 → 項目一覧 → まとめ画面という流れを、すべてコンパクトなウィンドウ内でサポートします。

進捗状況表示モード：
 - 「共有」 - 進行状況を示す単一のプログレスバー。デフォルトでは、「X / Y 完了」と表示されます。
 - "perItem" - 各項目ごとの進捗状況を表示し、完了すると自動的に次の項目に進みます。

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
