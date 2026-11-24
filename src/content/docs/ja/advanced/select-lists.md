---
title: 選択リストとラジオボタンを選択します。
description: ユーザーが選択できるように、ドロップダウンリストやラジオボタンのグループを作成します。
translationSynced: 2026-11-23T23:02:36+00:00
---

Dialogは、値のリストを受け取り、それらをプルダウンメニューとして表示する機能を持っています。オプションで、デフォルトで選択された項目を設定することも可能です。

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)

## 使用方法


### 選択リストのタイトル。

`--selecttitle <text>(,radio|required|searchable|multiselect|name="<text>")`

`--selecttitle`コマンドラインオプションでリストにラベルを設定できます。例：`--selecttitle "Select an Option"`

![image](https://user-images.githubusercontent.com/3598965/122635336-9ee98a80-d126-11eb-8839-f859eb19688e.png)


この名前は、`swiftDialog`の出力において、標準出力（STDOUT）に表示され、選択された項目の値と紐付けられます。単一選択リストの場合、標準出力の形式は以下のようになります。
```
    "SelectedOption" : "<value>"
    "SelectedIndex" : <index>
    "<name>" : "<value>"
    "<name>" index : "<index>"
```

複数の`--selecttitle`引数を指定することができます。関連する`--selectvalues`および`--selectdefault`引数を指定することも可能で、これらは指定された順序で選択リストに関連付けられます。

複数の選択肢を持つリストが使用されている場合、"SelectedOption" と "SelectedIndex" は機能しません。

特定のアイテムの表示は、swiftDialogが終了コード0を返す場合にのみ行われます。

### 選択肢の値を指定します。

`--selectvalues <text><csv>`

値はCSV形式で指定し、`--selectvalues`コマンドラインオプションで渡します。例：`--selectvalues "Option 1,Option 2,Option 3,Option 4, Option 5"`

![image](https://user-images.githubusercontent.com/3598965/122635303-6053d000-d126-11eb-94f1-6950f0e3d43e.png)

### 選択リスト (デフォルト)

`--selectdefault <text>`

デフォルトの設定は、`--selectdefault`というコマンドラインオプションを使用して変更できます。例えば、`--selectdefault "Option 4"`のように指定します。

![image](https://user-images.githubusercontent.com/3598965/122635358-c2143a00-d126-11eb-80b2-475a62b6ed9a.png)

デフォルト値が指定されていない場合、また、ユーザーがリストから項目を選択しない場合、出力は行われません。


例：出力結果：
```
    SelectedOption: Option 1
    SelectedIndex: 0
```

選択された項目が表示されるのは、Dialogの終了コードが0の場合のみです。

### 引数ごとのJSON設定。

選択リストは、JSONオブジェクトを使用して定義することも可能です（`--selectitem`、またはJSON形式の値を使用する`--selecttitle`）。これにより、各項目のプロパティをより直接的に制御できます。

**構文:**
```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU","required":true}'
```

**特徴：**
- `title` - 選択肢リストのラベル。
- `values` - オプションの値の配列。
- `default` - デフォルトで選択されている値。
- `required` - 入力必須かどうか (ラジオボタンの場合は無視されます)。
- - 表示スタイル：`style`、`list`、`radio`、または`searchable`、`multiselect`から選択してください。
- `name` - 代替となる出力キー名

**例：**

```bash
# Basic JSON item
dialog --selectitem '{"title":"Size","values":["S","M","L"],"default":"M"}'

# Searchable with required field
dialog --selectitem '{"title":"Region","values":["AU","US","UK"],"required":true,"style":"searchable"}'

# Radio button group
dialog --selectitem '{"title":"Priority","values":["Low","Medium","High"],"style":"radio"}'

# Mix JSON with positional arguments
dialog --selectitem '{"title":"Color","values":["red","green","blue"]}' --selectdefault "red"
```

JSONの要素は、位置情報に基づく引数とは独立しています。JSONを使用する際、値は位置情報に基づくラベルのリストから抽出され、重複を避けるように処理されます。`--selectvalues/--selecttitle/--selectdefault`

## JSONスキーマ

より詳細な制御を行うために、JSON形式で選択リストを指定することができます。

### 完全設定ファイル（JSON形式）

```json
{
  "selectitems" : [
    {
      "title" : "Select Item",
      "name" : "altname",
      "values" : ["red","green","blue"],
      "default" : "red",
      "required" : false,
      "style" : "default | radio | searchable | multiselect"
    }
  ]
}
```

### 引数ごとのJSON形式データ。

個別の選択項目も、JSONオブジェクトと組み合わせて、`--selectitem`または`--selecttitle`を使用して定義することができます。

```bash
dialog --selectitem '{"title":"Region","values":["AU","US"],"default":"AU"}'
dialog --selecttitle '{"title":"Size","values":["S","M","L"],"required":true}'
```

**注:** `--selecttitle` は、`--selectitem` と同様に、JSONオブジェクトを扱います。

### 例：

```json
"selectitems" : [
  {"title" : "Select 1", "values" : ["one","two","three"]},
  {"title" : "Select 2", "values" : ["red","green","blue"], "default" : "red"}
]
```

![image](https://user-images.githubusercontent.com/3598965/235899756-95fc6f85-1357-40c8-bf05-aa550c0d4d7d.png)


```json
"selectitems" : [
  {"title" : "Pick One", "values" : ["One","Two","Three"], "style" : "radio"}
]
```

![image](https://github.com/bartreardon/swiftDialog/assets/3598965/1d2659c6-9048-440b-9246-2756ec097a24)


## 修飾語句

### 名前

指定された`name`を使ってタイトルではなく、その内容を出力として記録します。

```bash
% dialog --selecttitle "Alternate Name",name=alt --selectvalues "Option One, Option Two, Option Three"

"SelectedOption" : "Option One"
"SelectedIndex" : 0
"alt" : "Option One"
"alt" index : "0"
```

### 検索可能。

この`searchable`オプションは、リストに検索フィールドを追加します。 テキストボックスに入力すると、リストが絞り込まれます。

<img width="550" alt="image" src="/images/select_1.png" />

<img width="550" alt="image" src="/images/select_2.png" />

### ラジオ。

`radio` モディファイアを使用すると、選択リストがラジオボタンを表示するグループに変わります。 `radio` を使用する際に、デフォルトの項目が指定されていない場合、リストの最初の項目がデフォルトで選択された項目になります。 そのため、ラジオボタンを使用すると、常に値のいずれかが選択され、`required` のようなモディファイアは無視されます。

`--selecttitle "Radio buttons",radio --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235897669-c08fdd79-aa14-4fec-8c6d-a930861a122f.png)

### 必須

`required` モディファイアを使用すると、特定のリスト項目が必須項目となり、swiftDialogが終了する前に必ず値を入力する必要があります。

`--selecttitle "Required item",required --selectvalues "Option One, Option Two, Option Three"`

![image](https://user-images.githubusercontent.com/3598965/235898090-5f7e9fac-2913-413f-ae85-c850ae86ee6b.png)

![image](https://user-images.githubusercontent.com/3598965/235898473-6fb9749f-3406-4f8d-b112-b214e95dccd4.png)

### 複数選択。

`multiselect` モディファイアを使用すると、リストから複数のオプションを選択できます。選択された項目は、削除可能なタグとして表示され、出力は選択された値のカンマ区切りリストになります。

`--selecttitle "Choose options",multiselect --selectvalues "Option One, Option Two, Option Three, Option Four"`

`multiselect`を使用する際、選択された値は、単一のカンマ区切りの文字列として返されます。

```
"Choose options" : "Option One, Option Three"
```

または、JSON形式で以下のように記述することもできます。
```json
{
  "Choose options" : "Option One, Option Three"
}
```

## グローバルスタイル

`--selectstyle [list | radio | searchable | multiselect]`

ダイアログ内の**すべて**の選択リスト項目の表示スタイルを設定します。これは、すべての`--selecttitle`にスタイル修飾子を設定することと同等です。リスト単位のスタイル修飾子は、このグローバル設定よりも優先されます。

| 価値 | 説明 |
|---|---|
| `list` | 標準的なドロップダウンメニュー（デフォルト設定）。 |
| `radio` | ラジオボタングループ。 |
| `searchable` | フィルター入力欄を備えたドロップダウンリスト。 |
| `multiselect` | 複数選択が可能な検索フィールド。 |

## リストに項目を追加します。

リストの中で、区切りが必要な箇所には、3つ以上のハイフンを続けて使用してください。`---`

`--selectvalues "Option One, Option Two, ---, Option Three, Option Four, ---, Option Five"`

![image](https://user-images.githubusercontent.com/3598965/235900591-96ace495-5205-459c-9b2e-4bcd3ede00ee.png)

**注意：各`---`はインデックスに含まれますが、区切り線自体は選択できません。上記の例では、メニューに5つの項目が表示されていても、リスト配列には7つの項目が含まれます。セレクトリストを作成する際には、この点にご留意ください。**

## 出力。

Dialogは、ユーザーが選択した値（または、デフォルト値が指定されており、ユーザーが何も選択しない場合はそのデフォルト値）を、終了時に`stdout`に出力します。この出力はスクリプトによって解析され、それに応じて処理することができます。

出力には2つの行が含まれています。
* 最初の行は、リスト項目に含まれるテキストであり、これが `SelectedOption: <text of item>` として出力されます。
* 二行目は、選択された項目のインデックスを示し、その形式は`SelectedIndex: <index of item>`となります。

インデックスは`0`から始まるため、リスト内の3番目の項目が選択された場合、`SelectedIndex`の出力は`SelectedIndex: 2`になります。

## サンプル読み出し結果。

以下の出力結果が与えられた場合：
```
 SelectedOption: Option 4
 SelectedIndex: 3
```

取得したい値を処理するために、`grep` コマンドと `awk` コマンドを組み合わせて使用します。

` | grep "SelectedOption" | awk -F ": " '{print $NF}'`

または

` | grep "SelectedIndex" | awk -F ": " '{print $NF}'`

## 複数の選択肢リストを追加する。

複数の選択リストを追加するには、`--selectvalues`、`--selecttitle`、および`--selectdefault`をそれぞれ複数回指定するだけです。 タイトルとデフォルト値は、指定された順序で割り当てられます。


### 複数選択の出力結果。

複数の選択リストを使用する場合、出力形式が変更され、様々な名前付きリストを解析できるようになります。例えば、上記のJSONデータを使用し、「two」と「red」を選択した場合、以下の出力が得られます。

```
Select 1 : two
Select 1 index : 1
Select 2 : red
Select 2 index : 0
```

JSON形式で出力する場合、以下のような結果になります。

```json
{
  "Select 1" : {
    "selectedIndex" : 1,
    "selectedValue" : "two"
  },
  "Select 2" : {
    "selectedIndex" : 0,
    "selectedValue" : "red"
  }
}
```