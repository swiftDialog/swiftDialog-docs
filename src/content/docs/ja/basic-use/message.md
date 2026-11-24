---
title: メッセージ表示領域のカスタマイズ。
description: swiftDialog で、メッセージテキスト、フォント設定、および表示位置を調整する方法を学びましょう。
translationSynced: 2026-11-23T22:35:11+00:00
---

ダイアログメッセージ領域に表示したい内容を指定するには、`-m` または `--message` のコマンドラインオプションを使用してください。

例：

`--message "This is the detail of an Important Message that you should read"`

`-m "This is the detail of an Important Message that you should read"`

メッセージ表示領域は、ダイアログウィンドウの幅の2/3を占めるか、アイコン表示領域が表示されない場合は、ダイアログウィンドウ全体の幅を占めることができます。

メッセージが画面の幅を超えて表示される場合、自動的に折り返されます。また、メッセージが画面全体で使用可能な表示領域を超えてしまう場合は、スクロールして表示されます。


<img width="400" alt="image" src="/images/lorem_ipsum_1.png" />

<img width="400" alt="image" src="/images/lorem_ipsum_2.png" />

### コンテンツの調達

テキスト文字列を渡す代わりに、MarkdownファイルのパスまたはURLを指定することも可能です。拡張子が`.md`で終わるファイルは、Markdownソースファイルとして扱われます。

例：

`--message "/path/to/content.md"`

`--message "https://www.example.com/example.md"`

## メッセージの配置。

`--messagealignment` と `--messageposition` を使用すると、メッセージがダイアログのどの位置に表示されるかを調整できます。メッセージを垂直方向および水平方向に中央に配置したダイアログを作成する際に役立ちます。

<img width="200" alt="image" src="/images/lorem_ipsum_3.png" />

## メッセージのフォント、色、サイズ、および配置を変更します。

`--alignment [left | centre | center | right]`

メッセージの配置を設定します。デフォルトは「left」です。

`--messagefont <text>`

メッセージのフォント、文字サイズ、および色を変更することができます。

`color,colour=<text><hex>`

> `<text>` は、標準的なAppleのカラーバリエーション（例：`black`、`blue`、`gray`、`green`、`orange`、`pink`、`purple`、`red`、`white`、`yellow`）のいずれかを選択できます。無効なオプションが指定された場合、デフォルトではシステムのプライマリカラーが適用されます（ライトモードの場合は通常`black`、ダークモードの場合は通常`white`）。

> `<hex>` は16進数形式で指定されます。例：#00A4C7

`size=<float>` は、あらゆる浮動小数点数 (例えば、15.7、20、32.0) を受け付けます。

`name=<fontname>` - インストールされているフォントの名前を入力できます。


`--message "Welcome to swiftDialog" --messagefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`


<img width="400" alt="image" src="/images/message_font.png" />

### メッセージに別の色を使用する。

`colour=<value>`を使用すると、メッセージの基本色を設定できます。ただし、`:colour[text]`の形式を使用することで、個々の単語や文字の色をそれぞれ設定することも可能です。

例：

`--message ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/message_colour.png" />

