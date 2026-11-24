---
title: ボタンとボタンの動作について。
description: swiftDialogで、ボタンのテキスト、動作、および動作設定方法を学びましょう。
translationSynced: 2026-11-23T22:42:32+00:00
---

ダイアログには、最大で3つのボタンを表示できます。

ボタンは、ダイアログウィンドウの下部に表示されます。

![対話ボタン領域 ](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## ボタン1 - デフォルトボタン。
デフォルトでは、「**OK**」というラベルが付いたボタンが一つ表示されます。このデフォルトのボタンは常に表示され、**_Enter_**キーに割り当てられており、Dialogアプリケーションを終了コード`0`で終了します。

デフォルトボタンのラベルは、`--button1text` オプションを使用することで、任意のテキストで変更することができます。

e.g. `--button1text "Enter to Continue"`

ボタン1のテキスト](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

この操作は、`--button1action`というオプションを使って変更することも可能です。そのため、Dialogアプリを単に終了するだけでなく、他の操作を実行することもできます。

現在の段階では、実行できる操作は、ユーザーのデフォルトブラウザで指定されたURLを開くことのみです。

e.g. `--button1action "https://github.com/"`

## ボタン2 - キャンセルボタン。
2つ目のボタンは、デフォルトでは非表示になっています。このボタンを表示するには、`-2`または`--button2`のオプションを使用します。このオプションを使用すると、ボタンにデフォルトで「キャンセル」というラベルが表示されます。2つ目のボタンは「Esc」キーに割り当てられており、このキーを押すと、ダイアログアプリが終了コード`2`を伴って終了します。

2つ目のボタンのラベルは、`--button2text`オプションを使用することで、任意の量のテキストで変更できます。このオプションを使用する場合、`--button2`オプションを別途指定する必要はありません。テキストラベルを変更すると、ボタンが表示されます。

例：

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![ボタン2：気にしません](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

ボタン2には、他の機能は実装されていません。

## 詳細情報のボタン。
「詳細情報」ボタンは、デフォルトでは非表示になっています。このボタンを表示するには、`-3`または`--infobutton`のオプションを使用します。これにより、「詳細情報」というラベルが付いたボタンが表示されます。このボタンをクリックすると、swiftDialogが終了し、終了コードとして`3`が返されます。

もし`--infobuttonaction`引数が指定されている場合、詳細情報のボタンをクリックすると、`--infobuttonaction`アクションのみが実行され、swiftDialogは自動的に終了しません。一方、`--quitoninfo`引数を追加すると、元の終了動作が復元されます。

情報ボタンのラベルは、`--infobuttontext`というオプションを使用して、任意のテキストで変更することができます。このオプションを使用する場合、`--infobutton`というオプションを別途指定する必要はありません。テキストラベルを変更する場合、ボタンの表示は自動的に行われます。

例：

`--infobuttontext "Click here for more details"`

![詳細については、このアイコンをクリックしてください。](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

この操作は、`--infobuttonaction`というオプションを使って変更することも可能です。そのため、Dialogアプリを単に終了するだけでなく、他の操作を実行することもできます。

現在の段階では、実行できる操作は、ユーザーのデフォルトブラウザで指定されたURLを開くことのみです。

e.g. `--infobuttonaction "https://github.com/"`

## ボタンのアイコン。

ボタンのラベルに加えて、使用するSF Symbolsを設定します。

### CSV 形式について。

```bash
--button1symbol <sf symbol name>[,position,rendering mode,size,color]
--button2symbol <sf symbol name>[,position,rendering mode,size,color]
--infobuttonsymbol <sf symbol name>[,position,rendering mode,size,color]
```

SFシンボルの名前を引数として受け取ります。

オプションのプロパティは、カンマで区切られた値のリストとして指定します（値の順序は問いません）。
 - 位置：先頭、末尾、上部、下部のいずれか - デフォルトは先頭。
 - レンダリングモード：階層構造、モノクロ、マルチカラー、パレットのいずれか。デフォルトはモノクロ。
 - パレット：以下の形式で、2つまたは3つの色を追加します。palette=色1-色2-色3
   - 例：パレット = 赤-緑-青
 - サイズ：形式は size=<num> のように指定してください。
 - 色: 以下の形式で指定してください: color=<text|hex>
   - マルチカラー表示モードが設定されている場合、色の指定は無視されます。

例：

`--button1symbol heart.fill,color=red`

<img width="400" alt="image" src="/images/button_symbol.png" />

### JSONオブジェクトの構文

バージョン3.1.1以降、ボタンのアイコンもJSONオブジェクトとして指定できるようになり、より詳細な制御が可能になりました。

```bash
--button1symbol '{"name":"checkmark.circle","colour":"green","position":"trailing"}'
--button2symbol '{"name":"xmark.circle","colour":"red","position":"leading"}'
--infobuttonsymbol '{"name":"info.circle","colour":"blue"}'
```

**特徴：**
- `name` - SFシンボルの名前（必須）
- `position` - シンボルの位置: `leading`, `trailing`, `top`, `bottom` (デフォルト: `leading`)
- `colour` / `color` - シンボルの色 (16進数表記または色名)
- `size` - シンボルのサイズ（ポイント単位）。
- `rendering` - レンダリングモード：`hierarchical`、`monochrome`、`multicolour`、`palette`
- `palette` - 複数の色を使用するシンボルの場合、2～3色の配列を指定します (CSVファイルではカンマ区切りで、JSONファイルでは配列形式で記述)。

**例：**

```bash
# Basic symbol with colour
dialog --button1symbol '{"name":"checkmark.circle","colour":"green"}'

# Symbol with position and size
dialog --button2symbol '{"name":"xmark.circle","colour":"red","position":"leading","size":20}'

# Multicolor symbol with palette
dialog --button1symbol '{"name":"person.3.sequence.fill","rendering":"palette","palette":["red","green","blue"]}'

# Symbol with all options
dialog --button1symbol '{"name":"heart.fill","colour":"pink","position":"trailing","size":24,"rendering":"hierarchical"}'
```

**注意:** `rendering: palette` パレットを使用する場合、JSON形式では、パレットは配列で記述する必要があります。`["red","green","blue"]` CSV形式では、ハイフンで区切って記述してください。`palette=red-green-blue`

## ボタンの位置。

デフォルトでは、ボタン1とボタン2は右側に、情報ボタンは左側に配置されています。

`--buttonstyle center` を使用すると、ボタン1（およびボタン2が存在する場合）が、ダイアログウィンドウの最下部中央に配置されます。

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` と `--infotext` は、`--buttonstyle center` オプションを使用する場合、互換性がない。

## ボタンの配置スタイルとして「スタック」形式。

`--buttonstyle stack`

ボタン1とボタン2を、画面の幅いっぱいに並べて表示します。

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` と `--infotext` は、`--buttonstyle stack` オプションを使用する場合、互換性がない。

## `[return]`キーと`[enter]`キーの動作について。

入力フィールドが存在しない場合、ダイアログ上でアクティブな入力コントロールは`button1`となり、`[enter]`と`[return]`もボタンをアクティブにします。これは、ウィンドウ上の唯一のインタラクティブな要素であるため、キーボードのデフォルトのフォーカスが設定されているからです。その結果、ボタンが有効で無効になっていない場合、この操作によってダイアログが閉じられます。

`[return]`キーは、エディタの入力フィールドがアクティブでない限り、常にボタン1を起動します。一方、`[enter]`キーは、アクティブな要素に対してのみ機能します（そのため、入力要素のないウィンドウでダイアログを閉じる際に有効です）。

1行のテキストフィールドでは、`[return]`は改行を追加できないため、デフォルトの動作が優先されダイアログが閉じられます（デフォルトのレスポンダーが起動します）。一方、`[enter]`は改行を追加できない上にデフォルトのレスポンダーの動作を制御しないため、何もしません。

複数行のテキストフィールド（例：`--textfield`で、`editor`が有効な場合）、`[return]`キーは改行を挿入することができ、この操作はデフォルトの設定（例：ボタン1を押すとウィンドウが閉じる）よりも優先されます。また、`[return]`キーも通常通り動作し、新しい行を挿入します。

### `[return]`、`[enter]`、または`[esc]`のデフォルト動作を変更する。

もし、`[return]`、`[enter]`、または`[esc]`のデフォルトの動作（ダイアログを閉じる）を変更したい場合は、`--hidedefaultkeyboardaction`というオプションを使用できます。このオプションを使用すると、デフォルトの`[return]`または`[escape]`キーが、動作を有効にするために、さらに`cmd`+`shift`の同時押しを必要とするようになります。これにより、意図しないダイアログの閉じを防ぐことができます。

## 戻り値コード

以下の戻り値コードは、各操作の実行後に送信されます。これらのコードは無視することも、呼び出しスクリプト内でさらなる処理を行うために使用することもできます。

| ボタン名 | オプション | ホットキー | 戻り値コード |
| ----------- | -------- | ------ | ----------- |
| `button1`   | いいえ       | `Enter`  | 0           |
| `button2`   | はい      | `Esc`    | 2           |
| `infobutton` | はい      |        | 3           |

## ボタンの無効化。

Button1とButton2は、以下のいずれかのコマンドを使用して、起動時に無効化することができます。

`--button1disabled`

`--button2disabled`

ボタン1は、ボタンのテキストを`none`に設定することで、完全に非表示にすることができます。

注意点として、これは[return]キーを使ってダイアログを閉じる機能を無効にするため、ダイアログを閉じるための別の方法を必ず用意してください。