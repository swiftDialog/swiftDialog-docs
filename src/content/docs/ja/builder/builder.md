---
title: ビルダーモード。
description: ダイアログウィンドウのプロパティや外観を編集し、その結果をJSON形式の設定ファイルとして出力します。
translationSynced: 2026-11-23T23:51:51+00:00
---


## swiftDialog 構築キット

実行するには、"run" コマンドを使用します。呼び出すと、追加のウィンドウが表示され、コンテンツやダイアログのプロパティを更新し、その結果をリアルタイムで確認できます。`dialog --builder`

その後、結果を**JSON**形式でエクスポートするか、または、設計したダイアログを再作成するための、すぐに実行可能な`dialog`**コマンドライン**として出力することができます。

**注意：この機能は、swiftDialogのすべての機能に対して100%の対応を保証するものではありません。また、一部の設定は利用できないか、生成される出力には表示されない場合があります。開発は現在も進行中です。**

<img width="500" alt="image" src="/builder/builder_main.png" />

<div className="not-content" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin: 2rem 0; align-items: flex-start;">

<div style="align-self: flex-start;">

### 基本。
 - [タイトル](/ja/builder/title/)
 - [メッセージ](/ja/builder/message/)
 - [アイコン](/ja/builder/icon/)
 - [サイドバー](/ja/builder/sidebar/)
 - [ウィンドウ](/ja/builder/window/)
 - [ボタン](/ja/builder/buttons/)

</div>

<div style="align-self: flex-start;">

### 高度な。
 - [チェックボックス](/ja/builder/checkboxes/)
 - [画像](/ja/builder/images/)
 - [箇条書き項目](/ja/builder/listitems/)
 - [メディア](/ja/builder/media/)
 - [テキストフィールド](/ja/builder/textfields/)

</div>

</div>

### 出力。

「出力」ビューでは、現在のデザインを「JSON」形式または「コマンドライン」形式で表示します。タブを使って、表示形式を切り替えることができます。そこから、「クリップボードにコピー」または「ファイルに保存」を選択できます。フッターにある「エクスポートコマンド」ボタンをクリックすると、ビルダー内のどこからでもコマンドラインをコピーできます。