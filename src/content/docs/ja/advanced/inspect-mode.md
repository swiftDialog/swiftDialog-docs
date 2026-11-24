---
title: 検査モード。
description: swiftDialogのインスペクトモードに関する入門ガイド：インストール状況とシステムコンプライアンスの監視について。
translationSynced: 2026-11-23T23:17:37+00:00
---


# swiftDialog インスペクトモード

SwiftDialogのインスペクトモードは、macOSのファイルシステム内でリアルタイムの監視を可能にする、新たに組み込まれた機能です。この機能は、AppleのFSEvents APIを活用してファイルシステムの状況を監視するとともに、アプリケーションのインストール状況や、キャッシュフォルダ、ファイル、plistの内容などを検査し、コンプライアンスチェックの結果を可視化します。この機能は、デバイスの登録時、ソフトウェアの展開時、およびコンプライアンス監査の際に特に有効であり、エンドユーザーが自身のコンプライアンス状況を明確に把握できるように設計されています。

## 概要

「検査モード」は、指定されたファイルパスやキャッシュディレクトリを継続的に監視し、アプリケーションやシステムコンポーネントの状態を追跡します。 あらかじめ用意された様々な表示形式を通じて、視覚的に情報を分かりやすく提示し、それぞれの用途に最適化された情報を提供します。


### 主な特長：
- リアルタイムでのファイルシステム監視。
- キャッシュ監視によるダウンロード進捗状況の検出。
- 様々な状況に対応できる、複数の表示設定が用意されています。
- plistファイルを使用した、簡易的な検証機能（真偽値、文字列、および存在確認）。
- カスタマイズ可能なテーマとブランド設定（一部機能）。
- 操作が完了すると、自動的にボタンが有効になるように設定します。

## はじめに

### 基本的な使い方。

1. JSON形式の設定ファイルを作成します。
```json
{
  "title": "Application Installation",
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}

```
:::tip[order of items]
重要：`guiIndex` は一意でなければならず、GUI 上の要素の表示順序を決定します。 数値が小さいほど、先に表示されます。
:::

2. "inspect"フラグを指定してswiftDialogを起動します。
```bash
/usr/local/bin/dialog --inspect-mode --inspect-config /path/to/config.json
```

3. オプションとして、設定ファイルのパスを指定する環境変数を設定できます。
```bash
export DIALOG_INSPECT_CONFIG="/path/to/config.json"
/usr/local/bin/dialog --inspect-mode
```

## JSON 設定リファレンス

### 一般的な会話オプション。

検査モードでは、JSONの設定ファイルに新しいオブジェクトが追加され、これにより、一般的なダイアログの動作を制御できます。これにより、コマンドライン引数を使用せずに、検査設定ファイル内でウィンドウのプロパティを直接設定することができます。`options`

```json
{
  "options": {
    "moveable": true,
    "ontop": true,
    "resizable": true,
    "windowbuttons": "min,max,close"
  }
}
```

**利用可能なオプション：**
- `moveable` (boolean) - ウィンドウのドラッグ機能を許可します。
- `ontop` (ブール値) - このウィンドウを他のウィンドウよりも常に前面に表示します。
- `resizable` (ブール値) - ウィンドウのリサイズを許可します。（`moveable`を意味します）
- `windowbuttons` (文字列) - ウィンドウボタンの表示を有効にする：`close`、`min`、`max` (カンマ区切り)。

**優先順位:** コマンドラインオプションは、JSON形式の設定よりも優先されます。

**サポートされていないオプション:** 許可リストにないオプションは、ログメッセージと共に無視されます。

**例：**
```json
{
  "title": "Application Installation",
  "options": {
    "moveable": true,
    "ontop": true
  },
  "items": [
    {
      "id": "app1",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"]
    }
  ]
}
```

### ルートレベルのキー。

| キー | 種類 | 必須 | デフォルト | 説明 |
|-----|------|----------|---------|-------------|
| `preset` | 文字列。 | いいえ。 | 「プリセット1」 | 表示レイアウトのプリセット（プリセット1～7）。 |
| `title` | 文字列。 | いいえ。 | 「システム点検」 | ウィンドウのタイトル。 |
| `message` | 文字列。 | いいえ。 | - | 主要なメッセージ本文。 |
| `icon` | 文字列。 | いいえ。 | - | アイコンのパス、またはSFシンボル（例: "sf=shield.fill"）。 |
| `size` | 文字列。 | いいえ。 | 「標準」 | ウィンドウサイズ： 「コンパクト」「標準」「大型」 |
| `width` | 整数。 | いいえ。 | - | カスタムウィンドウ幅（サイズ設定を上書きします）。 |
| `height` | 整数。 | いいえ。 | - | ウィンドウの高さのカスタム設定（サイズ設定を上書きします）。 |
| `cachePaths` | 配列。 | いいえ。 | - | ダウンロードを監視するディレクトリを指定します。 |
| `scanInterval` | 整数。 | いいえ。 | 2 | ファイルシステムのスキャン間隔（秒）。 |
| `button1text` | 文字列。 | いいえ。 | "OK" | 主要ボタンのテキスト。 |
| `button1disabled` | ブーリアン | いいえ。 | 偽 | 最初は主要ボタンを無効にします。 |
| `button2text` | 文字列。 | いいえ。 | キャンセル。 | 補助ボタンのテキスト。 |
| `button2visible` | ブーリアン | いいえ。 | 真実 | セカンダリボタンを表示する。 |
| `autoEnableButton` | ブーリアン | いいえ。 | 真実 | 完了したら、自動的にボタンが有効になります。 |
| `autoEnableButtonText` | 文字列。 | いいえ。 | "OK" | 自動で有効になった場合のボタンの表示テキスト。 |
| `items` | 配列。 | はい。 | - | 検査対象となる項目の一覧。 |

### 視覚的なカスタマイズ設定項目。

| キー。 | 種類。 | デフォルト | 説明 |
|-----|------|---------|-------------|
| `banner` | 文字列。 | - | バナー画像のパス（アイコンを上書きします）。 |
| `bannerHeight` | 整数。 | 100 | バナーの高さ（ピクセル単位）。 |
| `bannerTitle` | 文字列。 | - | バナーに表示されるタイトル。 |
| `highlightColor` | 文字列。 | "#808080" | アクセントカラー（16進数表記） |
| `backgroundColor` | 文字列。 | - | 背景色（16進数表記） |
| `backgroundImage` | 文字列。 | - | 背景画像のパス。 |
| `backgroundOpacity` | 二重。 | 1.0 | 背景の透明度（0～1）。 |
| `textOverlayColor` | 文字列。 | - | 背景に対するテキストのオーバーレイの色。 |
| `gradientColors` | 配列。 | - | グラデーションに使用する16進数カラー値の配列。 |
| `iconBasePath` | 文字列。 | - | 相対アイコンパスの基準となるパス。 |
| `appearance` | 文字列。 | 「自動」 | 検査ウィンドウの表示を強制します：`"dark"`、`"light"`、または`"auto"` (OSに準拠)。OSの設定を上書きし、両方の方向で適用されます。 |

### アイテム設定

配列内の各要素には、以下のものが必要です：`items`

| キー。 | 種類。 | 必須。 | 説明 |
|-----|------|----------|-------------|
| `id` | 文字列。 | はい。 | 一意な識別子 |
| `displayName` | 文字列。 | はい。 | UIに表示される名前。 |
| `guiIndex` | 整数。 | はい。 | 並べ替え順序（0から始まる）。 |
| `paths` | 配列。 | はい。 | 確認すべきファイルパス。 |
| `icon` | 文字列。 | いいえ。 | 商品固有のアイコン。 |
| `plistKey` | 文字列。 | いいえ。 | Plistキーの検証。 |
| `expectedValue` | 文字列。 | いいえ。 | 期待されるplistの値。 |
| `evaluation` | 文字列。 | いいえ。 | 評価タイプ： "equals"（等しい）、"boolean"（真偽）、"exists"（存在）、"contains"（包含）、"range"（範囲）。 |
| `description` | 文字列。 | いいえ。 | 商品名の下に、オプションで表示される説明文（プリセット1、2、3、5および6によって表示される）。 |
<!-- | `subtitle` | String | No | Subtitle text (preset6) | --> <!-- | `category` | 文字列 | いいえ | カテゴリのグループ化（プリセット5） |
| `categoryIcon` | 文字列。 | いいえ。 | カテゴリアイコン（プリセット5） | -->


## 高度な機能。

### キャッシュ監視

インストール作業の進行状況を監視するために、ダウンロードディレクトリを監視します。

```json
{
  "cachePaths": [
    "/Library/Managed Installs/Cache",
    "/Library/Application Support/Installomator/Downloads",
    "/Library/Application Support/JAMF/Downloads", 
    "/Library/Application Support/AirWatch/Data/Munki/Managed Installs/Cache"
  ],
  "scanInterval": 5,
  "cacheExtensions": ["download", "pkg", "dmg", "aria2"]
}
```

デフォルトでは、`cachePaths`内にあり、ファイル名が`.pkg`、`.dmg`、または`.download`で終わるファイルは、対応する項目が「ダウンロード中」とマークされます。 `cacheExtensions`を設定することで、このリストを変更できます。 例えば、aria2cの`<name>.aria2`で生成される部分ファイルも検出するために、`aria2`を追加することができます（問題 #617）。 ファイル名の先頭に付くドットは省略可能です。

### Plist準拠の検証。

システム設定を、plistファイルの内容を確認することで検証します。

```json
{
  "preset": "preset5",
  "items": [{
    "id": "findmymac",
    "displayName": "Find My Mac Status",
    "guiIndex": 0,
    "paths": ["/Library/Preferences/com.apple.FindMyMac.plist"],
    "plistKey": "FMMEnabled",
    "expectedValue": "true",
    "evaluation": "boolean"
  }]
}
```

### カスタムカラー閾値設定。

カスタムのコンプライアンスレベルと色を設定します。

```json
{
  "colorThresholds": {
    "excellent": 0.95,
    "good": 0.80,
    "warning": 0.60,
    "excellentColor": "#00C853",
    "goodColor": "#2196F3",
    "warningColor": "#FF9800",
    "criticalColor": "#F44336"
  }
}
```


### コンプライアンス管理ダッシュボード

plistファイルに基づいてコンプライアンス報告を行う場合、最上位に配列を設けます。swiftDialogは、参照されたplistファイルを、合格数/総数と総合スコアで分類し、それらをコンテンツブロック（および必要に応じてbentoセル）を通じて表示します。表示は一定間隔で更新されます。`plistSources` `compliance-summary` `findings-list`

```json
{
  "plistSources": [
    {
      "path": "/Library/Preferences/com.company.compliance.plist",
      "type": "compliance",
      "healthyLabel": "Compliant",
      "attentionLabel": "Action Required"
    }
  ],
  "guidance": [
    { "type": "compliance-summary" },
    { "type": "findings-list" }
  ]
}
```

**`plistSources[]` 特徴：**

| キー。 | 種類。 | デフォルト | 説明 |
|-----|------|---------|-------------|
| `path` | 文字列。 | - | plist ファイルへのパス。 |
| `type` | 文字列。 | - | 情報源の種類：`compliance`、`health`、`licenses`、`preferences`、または`custom`。 |
| `healthyLabel` | 文字列。 | 「健康」 | 合格済みを示すラベル<br> (概要カード、結果行、およびベントー形式のサブタイトルに表示されます)。 |
| `attentionLabel` | 文字列。 | "Needs Attention" | 検査に失敗した場合のラベル。 |
| `successValues` | 配列。 | - | 成功を示す価値観。 |
| `expectedValue` | 文字列。 | - | 法令遵守に関する期待される効果。 |
| `findingKey` | 文字列。 | 「発見」 | 詳細な検索結果を読むためのサブキーです。 |
| `timestampKey` | 文字列。 | 自動。 | 最終チェック時刻を保持するキー（自動試行：`lastComplianceCheck`、`LastUpdateCheck`、`lastCheck`、`timestamp`）。 |
| `includePattern` | 文字列。 | - | 自動検出に含めるキーを特定するための正規表現。 |
| `excludeKeys` | 配列。 | - | 自動検出から除外するキー。 |
| `keyMappings` | 配列。 | - | 特定のplistキーの解釈方法。 |
| `maxCheckDetails` | 整数。 | 15 | カテゴリごとに表示されるチェック項目の最大数を設定します。 |
| `icon` | 文字列。 | - | カテゴリを表すSFシンボル。 |

**集計されたデータを表示するコンテンツブロック。**

- `compliance-summary` — 全体的な状況を示すバナーに加え、カテゴリごとの詳細な情報を示すカードを表示します。
- `findings-list` 一覧は、カテゴリー別に分類され、個々のチェック項目が詳細に記載されています。

Bentoセルは、同じデータに自動的にリンクします。セルのサブタイトルやアイコンの色は、リアルタイムで更新され、追加のスキーマ項目は必要ありません。<br>

## 完全な例

### 基本的なアプリケーション インストーラー。

```json
{
  "title": "Installing Office Suite",
  "message": "Please wait while we install your applications",
  "preset": "preset1",
  "icon": "sf=apps.iphone.badge.plus",
  "iconBasePath":"/Users/Shared/icons/",
  "cachePaths": ["/Users/Shared/Downloads"],
  "button1text": "Please Wait...",
  "button1disabled": true,
  "autoEnableButton": true,
  "autoEnableButtonText": "Continue",
  "items": [
    {
      "id": "microsoft_word",
      "displayName": "Microsoft Word",
      "guiIndex": 0,
      "paths": ["/Applications/Microsoft Word.app"],
      "icon": "Microsoft Word.png"
    },
    {
      "id": "microsoft_excel",
      "displayName": "Microsoft Excel",
      "guiIndex": 1,
      "paths": ["/Applications/Microsoft Excel.app"],
      "icon": "Microsoft Excel.png"
    },
    {
      "id": "microsoft_powerpoint",
      "displayName": "Microsoft PowerPoint",
      "guiIndex": 2,
      "paths": ["/Applications/Microsoft PowerPoint.app"],
      "icon": "Microsoft PowerPoint.png"
    }
  ]
}
```
:::tip[iconBasePath]
アイテムアイコンのベースパスを定義することで、設定を簡素化できます。画像ファイル名は、利用可能な場合は`iconBasePath`から読み込まれます。それ以外の場合、アイテムごとに完全なパスを指定してください。
:::


## トラブルシューティング (問題解決)

### 設定が読み込まれていません。
- JSONの構文が正しいか、`jq`またはオンラインの検証ツールを使用して確認してください。
- ファイルへのアクセス権を確認してください（読み取り可能である必要があります）。
- 環境変数が正しく設定されていることを確認してください。

### 検出されない項目。
- 正確なファイルパス（大文字と小文字を区別）を確認してください。
- パスに管理者権限が必要かどうかを確認してください。
- ダウンロードの検出に使用します。`cachePaths`
- システムが処理速度の低い場合、この値を大きくしてください。`scanInterval`

### デバッグモード
デバッグ出力を有効にする：
```bash
/usr/local/bin/dialog --inspect-mode --debug
```

```bash
export DIALOG_DEBUG=1
/usr/local/bin/dialog --inspect-mode
```

### 一般的な環境変数。
- `DIALOG_INSPECT_CONFIG`: 設定ファイルのJSON形式データへのパス。
- `DIALOG_DEBUG`: デバッグログの記録を有効にする。
- `DIALOG_COMMAND_FILE`: カスタムコマンドファイルへのパス。

## ベストプラクティス

1. **シンプルに始めましょう**: プリセット1を使用し、設定を最小限に保ってから始めましょう。
2. **テスト対象パス**: すべてのファイルパスが存在するか、または将来的に存在することを確認します。
3. **キャッシュ監視機能の利用**: ダウンロードの検出機能を追加します。`cachePaths`
4. **アイコン管理**: アイコンを集中管理された場所に保存します。`iconBasePath`
5. **ボタンの状態**: より優れたユーザーエクスペリエンスのために、`autoEnableButton` を活用してください。
6. **適切なプリセットの選択:** 使用目的に合わせて、最適なプリセットを選択してください。
   - インストール状況の追跡：プリセット1、2、または3を選択してください。
   - コンプライアンス表示：プリセット4。


