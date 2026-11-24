---
title: コマンドファイル
description: コマンドファイルを使用して、ダイアログに新しいコンテンツを動的に追加・更新します。
translationSynced: 2026-11-23T22:53:09+00:00
---

一部のダイアログの内容は、一度起動された後でも、リアルタイムで更新することができます。これは、Dialogが読み込み、解釈するコマンドファイルにコマンドを送信することで実現されます。

---

Dialogプログラムは、バックグラウンドで起動されている必要があります。これにより、同じスクリプトからDialogプログラムにコマンドを送信できるようになります。

```sh
/usr/local/bin/dialog & sleep 0.1
```

システムは、最初のコマンドを送信する前に、Dialogが初期化を完了するまで100ミリ秒の猶予を与えます。`sleep 0.1`

デフォルトのコマンドファイルへのパスは`/var/tmp/dialog.log`です。カスタムパスを設定するには、`--commandfile`という引数を使用します。

```sh
dialog --commandfile /var/tmp/my.log
```

コマンドの送信方法：

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## 内容。

| コマンド | 説明 |
|---|---|
| `title: <text>` | ダイアログのタイトルを更新します。 |
| `title: none` | タイトル領域を非表示にする。 |
| `titlefont: <params>` | タイトルのフォントプロパティを更新します。スペースで区切られた以下のパラメータを受け付けます: `key=value`、`size=<float>`、`weight=<value>`、`colour=<color\|hex>`、`name=<fontname>`、`shadow=<bool>`。 |
| `message: <text>` | メッセージの内容を置き換えます。Markdown形式に対応しています。 |
| `message: + <text>` | 既存のメッセージに追記します（新しい内容の前に改行を挿入します）。 |
| `message: /path/to/file.md` | ローカルのMarkdownファイルからメッセージの内容を読み込みます。 |
| `alignment: [left\|center\|right]` | メッセージのテキストの配置を設定します。 |

---

## アイコン

| コマンド | 説明 |
|---|---|
| `icon: <path\|url\|SF Symbol>` | 表示されているアイコンを変更します。 |
| `icon: none` | アイコンを非表示にする。 |
| `icon: centre` / `icon: center` | アイコンを中央の位置に移動してください。 |
| `icon: left` / `icon: default` | アイコンをデフォルトの左側に移動してください。 |
| `icon: size: <num>` | アイコンのサイズを変更します。 |
| `iconalpha: <float>` | アイコンの透明度を設定します (0.0: 透明、1.0: 不透明)。 |
| `overlayicon: <path\|url\|SF Symbol>` | オーバーレイアイコンを設定します。 |
| `overlayicon: none` | オーバーレイアイコンを非表示にする。 |

---

## バナーと背景。

| コマンド | 説明 |
|---|---|
| `bannerimage: <path\|url>` | バナー画像の指定を行います。 |
| `bannerimage: none` | バナー画像を削除します。 |
| `bannertext: enable` | タイトルをバナーテキストとして表示します（フォントの色を白に設定します）。 |
| `bannertext: disable` | タイトル表示をデフォルト設定に戻す。 |
| `bannertext: shadow` | バナーのタイトルテキストに影を追加する機能を有効にします。 |
| `bannertext: <text>` | バナーのタイトルテキストを設定し、バナーテキスト表示モードを有効にします。 |

---

## 画像とメディア。

| コマンド | 説明 |
|---|---|
| `image: <path\|url>` | 画像を表示します（すでに画像が表示されている場合は、カルーセルに追加されます）。 |
| `image: show` | 現在の画像を表示します。 |
| `image: hide` | 現在の画像を非表示にする。 |
| `image: clear` | すべての画像を削除します。 |
| `imagecaption: <text>` | 表示されている画像の下に、キャプションを設定します。 |
| `video: <path\|url>` | 動画を表示します。`youtube=<id>` および `vimeo=<id>` のショートカットに対応しています。 |
| `video: none` | 動画を削除する。 |
| `webcontent: <url>` | ウェブコンテンツ表示領域にURLを入力します。 |
| `webcontent: none` | ウェブコンテンツを削除します。 |

---

## ボタン

| コマンド | 説明 |
|---|---|
| `button1: enable` / `button1: show` | ボタン1を有効にする。 |
| `button1: disable` / `button1: hide` | ボタン1を無効にする。 |
| `button1text: <text>` | ボタン1のラベル（更新用） |
| `button2: enable` / `button2: show` | ボタン2を有効にする。 |
| `button2: disable` / `button2: hide` | ボタン2を無効にする。 |
| `button2text: <text>` | 更新ボタン2のラベル。 |
| `buttonsize: [mini\|small\|regular\|large]` | ボタンのサイズを設定します。 |
| `infobutton: <text>` | 「情報」ボタンのラベルを更新する。 |
| `infotext: <text>` | 情報テキストの表示領域を更新します。 |
| `infotext: disable` / `infotext: hide` | 情報を表示するテキストを非表示にする。 |
| `infotext: reset` / `infotext: clear` | 情報テキストの値をクリアします。 |

---

## 情報ボックス

| コマンド | 説明 |
|---|---|
| `infobox: <text>` | 情報ボックスの内容を置き換えます。Markdown形式に対応しています。 |
| `infobox: + <text>` | 既存の情報ボックスの内容に追記します。 |
| `infobox: /path/to/file.md` | ローカルのMarkdownファイルから情報ボックスの内容を読み込む。 |

---

## 進捗状況バー

| コマンド | 説明 |
|---|---|
| `progress: <int>` | プログレスバーの進捗状況を、特定のステップの値に設定します。 |
| `progress: increment` | プログレスバーを1ステップ分進める。 |
| `progress: increment <n>` | プログレスバーを`n`ステップずつ進めます。 |
| `progress: complete` | プログレスバーを最大値に設定してください。 |
| `progress: reset` / `progress: indeterminate` | プログレスバーを、進行状況が不明な状態に戻します。 |
| `progress: show` / `progress: enable` / `progress: create` | 進捗状況を示すバーを表示します。 |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | 進捗バーを非表示にする。 |
| `progresstext: <text>` | プログレスバーの下にあるラベルを更新してください。 |

---

## リスト

| コマンド | 説明 |
|---|---|
| `list: <csv>` | リストの内容を、新しいカンマ区切りの項目で置き換えてください。 |
| `list: clear` | リスト内のすべての項目を削除し、リストを非表示にします。 |
| `list: show` | リストを表示します。 |
| `list: hide` | リストの内容を消去せずに、リストを非表示にします。 |

### リスト項目の更新。

既存のアイテムを、タイトルに基づいて更新します（簡易フォーム）。

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

カンマ区切りのプロパティを使用して、アイテムを完全に制御しながら更新します。

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

リストの末尾に新しい項目を追加します。

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

項目を削除する：

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**利用可能な物件：`listitem`**

| 不動産。 | 説明 |
|---|---|
| `title: <text>` | タイトルで検索します。 |
| `index: <int>` | インデックス（0から始まる）に基づいて項目を照合します。 |
| `subtitle: <text>` | アイテムのサブタイトルを設定します。 |
| `icon: <path\|url\|SF Symbol>` | アイテムのアイコンを設定します。 |
| `iconalpha: <float>` | 設定アイテムのアイコンの透明度。 |
| `status: <status>` | ステータスアイコンを設定します。以下のいずれかを選択してください：`wait`、`success`、`fail`、`error`、`pending`、`progress`、またはSFシンボルの名前（オプションで色の指定を付加することも可能です。例：`lock.shield.fill-green`）。 |
| `statustext: <text>` | ステータスラベルのテキストを設定します。 |
| `progress: <float>` | インラインで進行状況を表示する値を設定します（進行状況を示すステータスを表示します）。 |
| `action: <url>` | アイテムがクリックされたときに開くURL。 |
| `add:` | リストに新しい項目を追加します。 |
| `delete:` | 一致した項目を削除します。 |

---

## ヘルプメッセージ

| コマンド | 説明 |
|---|---|
| `helpmessage: <text>` | ヘルプメッセージの内容を更新します。Markdown形式に対応しています。 |

---

## 窓

| コマンド | 説明 |
|---|---|
| `width: <num>` | ウィンドウの幅を変更します。 |
| `height: <num>` | ウィンドウの高さを変更します。 |
| `position: <position>` | ウィンドウを移動します。以下のいずれか、またはそれらの組み合わせ (例: `topright`) を選択してください: `top`、`bottom`、`left`、`right`、`centre`。 |

---

## ウィンドウの表示可否。

| コマンド | 説明 |
|---|---|
| `activate:` | ダイアログウィンドウを最前面に表示します。 |
| `show:` | ダイアログウィンドウを再表示します。 |
| `hide:` | ダイアログウィンドウを非表示にする。 |
| `minimize:` / `minimise:` | ダイアログウィンドウを最小化して、ドックに表示します。 |
| `maximize:` / `maximise:` | 最小化されたダイアログウィンドウを元の状態に戻します。 |
| `blurscreen: enable` | 画面をぼかす効果を有効にする。 |
| `blurscreen: disable` | 画面のぼかし効果を無効にする。 |

---

## ドックのアイコン。

| コマンド | 説明 |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | ドックに「ダイアログ」アイコンを表示します。 |
| `showdockicon: <any other value>` | ドックからダイアログアイコンを非表示にする。 |
| `dockicon: <file\|url>` | ドックのアイコンを、ユーザーが指定した画像に設定します。 |
| `dockicon: none` / `dockicon: default` | ダイアログドックのアイコンをデフォルト設定に戻します。 |
| `dockiconbadge: <text>` | ドックのアイコンにバッジを表示します。 |
| `dockiconbadge: none` / `dockiconbadge: remove` | ドックアイコンのバッジを削除します。 |
| `bounce:` | 「Dock」アイコンをクリックして、その情報を確認してください。（情報表示用） |
| `bounce: critical` | Dockアイコンをクリックし続けて、ウィンドウが前面に表示されるまで繰り返します。 |

---

## 退職する。

| コマンド | 説明 |
|---|---|
| `quit:` | プログラムを終了する際に、終了コード5を返します。 |
