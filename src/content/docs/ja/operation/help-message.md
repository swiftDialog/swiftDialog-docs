---
title: ヘルプメッセージ。
description: ダイアログにコンテキストヘルプメッセージを追加する。
translationSynced: 2026-11-23T23:31:54+00:00
---

## ヘルプメッセージ。

ヘルプメッセージは、必要に応じて詳細な情報を追加で提供する手段となり、同時に画面上の表示領域を圧迫することを防ぐことができます。

`--helpmessage <text>`

`<text>` は、メッセージの書式設定にマークダウン形式をサポートします。

デフォルトのボタンの横に、もし「ヘルプ」ボタンが表示される設定になっている場合は、追加の「ヘルプ」ボタンが表示されます。


![image](https://user-images.githubusercontent.com/3598965/216032093-2aede3aa-4cda-402c-9cd7-fa4edb506cfc.png)

それをクリックすると、ヘルプメッセージがポップアップウィンドウで表示されます。

![image](https://user-images.githubusercontent.com/3598965/216032203-35960f72-24f5-491e-8d75-b6b43e4a123c.png)

表示されるシートの高さは、メッセージのサイズに合わせて自動的に調整されます。

### `--helpimage`

画像を追加します。`--helpimage /path/to/image.png`

<img width="550" alt="image" src="https://github.com/user-attachments/assets/d4c4504f-2e6f-4e83-882f-be0e799c9ffc" />

標準のアイコン引数に対応しており、QRコードもサポートしています。

<img width="550" alt="image" src="https://github.com/user-attachments/assets/1c4c99bc-8548-4547-b16b-0dd02cc2c02d" />

### `--helpalignment`

`--helpalignment [left | centre | center | right]`

ヘルプシートのメッセージ内容のテキスト配置を設定します。デフォルトでは、現在のメッセージ配置設定と同じ配置が適用されます。

### `--helpsheetbuttontext`

`--helpsheetbuttontext <text>`

ヘルプ表示を閉じるボタンに表示するラベルを設定します。デフォルト値は`OK`です。