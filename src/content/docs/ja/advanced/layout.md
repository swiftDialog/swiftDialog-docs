---
title: レイアウト
description: ダイアログ要素の順序や配置をカスタマイズする。
translationSynced: 2026-11-23T23:00:40+00:00
---

## カスタム表示での注文順序。

`--vieworder <csv>`

画像やメッセージの内容を除き、ウィンドウの要素の配置順序は変更可能です。

デフォルトの順序は以下の通りです：
 > テキストファイル。
 > ウェブコンテンツ。
 > リスト項目。
 > チェックボックス
 > テキスト入力欄
 > ラジオボタン
 > ドロップダウンメニュー

 これらの要素は、表示要件に合わせて再配置できます。希望する順序をCSV形式のリストで指定することで、例えば`--vieworder "dropdown, textfield, checkbox"`のように設定できます。

 <img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/1b69abc7-4367-4eac-9e2d-a208ea47a60f" width="750px">