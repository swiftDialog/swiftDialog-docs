---
title: タイトルのカスタマイズについて。
description: swiftDialogで、タイトルテキストとフォントのプロパティを設定およびカスタマイズする方法を学びましょう。
translationSynced: 2026-11-24T10:56:44+00:00
---

## タイトルテキストの設定。

ダイアログのタイトル部分に表示したい内容を指定するには、`-t` または `--title` のコマンドラインオプションを使用してください。

例：

`--title "An Important Message"`

`-t "An Important Message"`

タイトル領域は、ダイアログウィンドウの上部に配置された、固定幅の太字表示エリアです。ウィンドウの幅を超える長いテキストは、表示されないように省略されます。

![image](https://user-images.githubusercontent.com/3598965/125153474-47739300-e197-11eb-8b46-85b3cb13194a.png)

## タイトルのフォントプロパティのカスタマイズ方法。

タイトルのフォント設定には、`--titlefont` コマンドラインオプションを使用してください。

### CSV 形式について。

フォントの属性は、`property=value`という形式で表現され、複数の属性はコンマで区切られます。

変更可能なプロパティは以下の通りです。
 * `colour=<hex_value>` (または `color=<hex_value>`)
   * 16進数形式で指定されます。例：#00A4C7。
 * `size=<float>`
   * このフィールドは、30、65、72.3などの任意の浮動小数点数を受け付けます。
 * `weight=<text>`
   * 以下のいずれかのフォントの太さを選択できます。細字、ライト、標準、中太、太字、またはデフォルトの太字。
 * `name=<fontname>`
   * フォント名またはフォントファミリーを指定できます。利用可能な名前の一覧は、`--listfonts` コマンドを使用するか、macOSのフォントブックアプリケーションを参照することで確認できます。
 * `alignment=[left|right]`
   * タイトルテキストを左寄せまたは右寄せに配置します。
 * `offset=<float>`
   * 指定されたポイント数だけ、タイトルテキストを水平方向に移動させます。正の値は右方向に、負の値は左方向に移動します。`alignment=right`を使用する場合、オフセットの方向が自動的に反転されるため、正の値でもテキストは右端の方向に移動します。
 * `shadow`
   * テキストに影を追加します（真偽値。値は不要です）。

 > **注意：** フォント名と太さ（ウェイト）を組み合わせる際には、ご注意ください。フォント名またはフォントファミリーを指定する際、特定の太さ（ウェイト）が利用できない場合があります。その場合、指定された太さ（ウェイト）は無視されます。

以下のオプションを1つまたは複数組み合わせて使用できます。また、指定する順番は問いません。例えば、サイズのみを変更したい場合は、以下のように記述できます。

`--titlefont "size=60"`

例1：`--titlefont "colour=#00A4C7,weight=light,size=60"`

この例では、色を値`#00A4C7`に、太さを`light`に、フォントサイズを`60`に設定し、以下のように表示されます。

<img width="400" alt="image" src="/images/titlefont1.png" />

例2：`--titlefont "name=Chalkboard-Bold,colour=#D054A0,size=40"`

この例では、色を値「`#D054A0 `」に、サイズを「`40`」に設定し、フォント名を「Chalkboard-Bold」として使用します。

<img width="400" alt="image" src="/images/titlefont2.png" />

例：左寄せ/右寄せ。

`--titlefont alignment=left` - `--titlefont alignment=right`

<img width="400" alt="image" src="/images/titlefont_left.png" /> <img width="400" alt="image" src="/images/titlefont_right.png" />

### JSONオブジェクトの構文

3.1.1 以降、`--titlefont` と `--messagefont` は、より詳細な制御を行うために、JSON オブジェクトとして指定することも可能です。

```bash
--titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'
--messagefont '{"size":24,"colour":"red","weight":"medium"}'
```

**特徴：**
- `name` - フォント名またはフォントファミリー
- `size` - フォントサイズ（ポイント単位）。
- `colour` / `color` - テキストの色 (16進数または色名)
- `weight` - フォントの太さ: `thin`、`light`、`regular`、`medium`、`heavy`、`bold`
- `alignment` - テキストの配置：`left`、`right`（タイトルのみ）
- `offset` - タイトルのみに適用される、水平方向のオフセット量をポイント単位で指定します。
- `shadow` - ドロップシャドウを追加 (真偽値)

**例：**

```bash
# Title font with all properties
dialog --titlefont '{"name":"Chalkboard","colour":"#FFD012","size":40,"weight":"bold","shadow":true}'

# Message font with size and colour
dialog --messagefont '{"size":24,"colour":"#FF0000","weight":"medium"}'

# Title font with alignment and offset
dialog --titlefont '{"size":36,"colour":"blue","alignment":"right","offset":20}'
```

**注意:** `shadow` キーは、現在JSON形式でサポートされています（以前はCSV形式でのみ利用可能でした）。

### タイトルに色を使用する。

`colour=<value>`を使用すると、テキストの基本色を設定できます。ただし、`:colour[text]`の形式を使用することで、個々の単語や文字の色をそれぞれ設定することも可能です。

例：

`--title ":orange[Welcome] :green[to] :teal[swiftDialog]"`

<img width="400" alt="image" src="/images/title_colour.png" />

## 字幕

`--subtitle <text>` を使用すると、タイトルの下に、同じフォントで、ただし小さいサイズで書かれたサブテキストを表示できます。

```sh
dialog --title "System Update" --subtitle "Please save your work before continuing"
```

サブタイトルは、タイトルと同じフォント名、太さ、色を使用しますが、表示サイズが異なります。`titlefont size − 10pt`

#### タイトル領域を非表示にする。

キーワード `none` を使用すると、タイトル領域を非表示にできます。これにより、タイトルバーと水平方向の区切り線が消えます。

e.g. `--title none`




