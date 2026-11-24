---
title: プリセット5 - 統合モード
description: インスペクトモードのプリセット5を使用するための設定。
translationSynced: 2026-11-23T23:20:11+00:00
---

セルフサービスポータル向けプリセット：カスタマイズ可能なWebビュー。オプションで認証機能を追加可能。

対応機種：
- ブランドイメージに合わせた、オプションのネイティブSwiftUIによる、セットアップ画面の導入・終了画面をご用意できます。
- 認証を必要としない単純なURL（例：SOFA、ドキュメント）。
- 認証済みポータルへのトークン注入。
- MDM（モバイルデバイス管理）のAppConfig機能を利用した、複数のブランドに対応したテーマ設定。

フロー：(オプション) イントロ画面 → ポータルWebView → (オプション) アウトロ画面。

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