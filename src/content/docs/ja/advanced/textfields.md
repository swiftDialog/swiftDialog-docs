---
title: テキストフィールド
description: 様々なプロパティと検証機能を備えたテキスト入力フィールドを作成します。
translationSynced: 2026-11-23T23:12:40+00:00
---

このオプションを使用すると、ユーザーがダイアログを閉じる前に、テキストを入力できる領域を指定できます。`--textfield`

この機能は、テキスト形式でパラメータを受け取り、そのパラメータをテキストフィールドのラベルとして、ダイアログのユーザーインターフェースとレポートの出力の両方で使用します。

プログラムが終了すると、結果は以下の形式で標準出力（stdout）に送られます。

`<textfield text> : <user input>`

または、JSON形式の出力を使用する場合（該当するオプションを有効にする場合）：`--json`

```json
{
"<textfield text>" : "<user input>"
}
```

## 例：

もし以下の対話を使用する場合：

`dialog --textfield "Textfield 1"`

以下のダイアログが表示されます。

![image](https://user-images.githubusercontent.com/3598965/235908715-5f24a167-5ad1-4f81-aa7e-30faf5590b1c.png)

ユーザーが応答を入力します。

![image](https://user-images.githubusercontent.com/3598965/235908865-40b37eac-874b-4ceb-a4e7-e8701ebdf790.png)

これにより、以下の出力結果が得られます。

`Textfield 1 : This is what the user entered`

または、`--json`を使用する場合に。

```json
{
"Textfield 1" : "This is what the user entered"
}
```

## 追加のテキスト入力欄。

ダイアログ呼び出し時に、追加のオプションを指定することで、複数のテキスト入力欄を設定することができます。`--textfield`

e.g. `dialog --textfield "Textfield 1" --textfield "Textfield 2"`

![image](https://user-images.githubusercontent.com/3598965/235909015-2c4f187b-a86d-4281-84ff-09afa6b87857.png)

必要な数だけテキストフィールドを指定できます。各テキストフィールドは、出力において個別の項目として表示されます。

テキストフィールドを複数追加する場合、それらがうまく収まるように、ダイアログウィンドウのサイズを調整する必要があるかもしれません。`--height`

例：

`dialog --textfield "First Name" --textfield "Surname" --textfield "Age" --textfield "Favourite Colour"`

その結果、以下の出力が得られます。

```
First Name : Joe
Surname : Bloggs
Age : 32
Favourite Colour : Red
```

`--json`
```json
{
"First Name" : "Joe",
"Surname" : "Bloggs",
"Age" : "32",
"Favourite Colour" : "Red"
}
```

## テキストフィールドの修飾子。

テキストフィールドのラベルには、カンマで区切られた値が追加として付与されます。

```sh
--textfield "<label>,<modifier>,<modifier>=<value>"
```

| 修飾語 | 説明 |
|---|---|
| `name=<text>` | この値を、ラベルの代わりに、出力キーとして使用してください。 |
| `required` | 「フィールド」に入力がない場合、swiftDialogは終了しません。 |
| `secure` | 入力中に表示される文字を隠す（パスワード入力欄の場合）。 |
| `passwordfill` | macOSのパスワード自動入力機能を、特定の`secure`フィールドで有効にします。 |
| `prompt="<text>"` | フィールド内に表示されるプレースホルダーテキスト（出力には含まれません）。 |
| `value="<text>"` | このフィールドに、編集可能なデフォルト値をあらかじめ設定します。 |
| `regex=<pattern>` | 入力フィールドの内容が、指定された正規表現に一致することを確認します。 |
| `regexerror=<text>` | 正規表現に合致しない場合に表示されるカスタムエラーメッセージ。 |
| `editor` | 単一行の入力欄ではなく、複数行のテキストを編集できるエディタを使用します。 |
| `isdate` | テキスト入力欄を日付ピッカーに置き換えます。出力は、短い日付形式の文字列で表示されます。 |
| `fileselect` | 「選択」ボタンを追加し、それをクリックするとファイル選択ダイアログが開くようにします。 |
| `filetype=<types>` | ファイル選択ダイアログで許可するファイルの種類を、指定されたものに制限します（スペースで区切って指定）。ファイル拡張子（例：`png jpg`）を使用するか、またはタイプキーワードである`folder`、`image`、`movie`、`video`、`audio`を使用してください。 |
| `path=<path>` | ファイル選択ダイアログの初期表示ディレクトリを設定します。 |
| `confirm` | 確認用の入力欄を追加し、その内容が最初に指定された入力欄の内容と一致する必要があります。 |

### 名前

`name=<text>` は、出力におけるキーとしてラベルを置き換えます。ユーザーにとって分かりやすいラベルを使用したい場合に、出力側のキー名をより簡潔にしたい場合に役立ちます。

### 安全を確保する。

`secure` 入力内容は入力中に非表示になり、鍵のアイコンが表示されます。ただし、出力される内容は依然として標準出力にプレーンテキストとして表示されます。

```sh
--textfield "Password,secure"
```

![image](https://user-images.githubusercontent.com/3598965/159697347-e1c5d102-2064-4f8d-a767-a17ef0ed6c7e.png)

### パスワード自動入力機能。

`passwordfill` は、macOSのパスワード自動入力機能を有効にします。 `secure` と組み合わせて使用する必要があります。

```sh
--textfield "Password,secure,passwordfill"
```

### 必須。

`required` swiftDialogが、入力フィールドに値が入力されるまで、画面を閉じられないようにします。必須項目には`*`マークが表示され、ユーザーが項目を入力せずに画面を閉じようとすると、その項目がハイライト表示されます。

```sh
--textfield "Full Name,required"
```

![image](https://user-images.githubusercontent.com/3598965/159698383-db0647f3-ddbd-43cf-ac85-78814cf0c070.png)

### プロンプト。

`prompt="<text>"` は、フィールド内にプレースホルダーテキストを表示します。ユーザーが入力を開始すると、このテキストは消え、出力には含まれません。`secure` フィールドではサポートされていません。

```sh
--textfield "Name,prompt="Enter your full name""
```

![image](https://user-images.githubusercontent.com/3598965/159698757-80fb613e-05e9-461a-a257-c18c6630520e.png)

### 価値

`value="<text>"` このフィールドには、ユーザーが編集可能なデフォルト値が自動的に入力されます。

```sh
--textfield "Default Value Test",value="Some default value"
```

![image](https://user-images.githubusercontent.com/3598965/216030817-c90259b5-e8c1-4042-9a8f-721260e420dd.png)

### 正規表現と、正規表現におけるエラー。

`regex=<pattern>` swiftDialogが終了する前に、入力フィールドの内容が指定された正規表現に一致する必要があります。`regexerror=<text>` パターンが一致しない場合に表示されるメッセージを設定します。

パターンが明示的に許可していない場合、`regex`フィールドは空にすることはできません。

```sh
--textfield "Product Code",prompt="Enter 5 digit code",regex="\d{5}",regexerror="Must be a five digit number"
```

![image](https://user-images.githubusercontent.com/3598965/171410790-c05c44d5-daf6-402d-9efc-0f331cb8945b.png)

入力中に、フィールド上に緑色または赤色のオーバーレイを表示し、ユーザーが入力した内容が正規表現に合致しているかどうかをリアルタイムでフィードバックします。`--textfieldlivevalidation`

### 編集者

`editor` は、単一行の入力欄ではなく、より広くて複数行のテキスト入力領域を表示します。

```sh
--textfield "Notes,editor"
```

![image](https://user-images.githubusercontent.com/3598965/235909625-af60af64-200e-4b66-8274-90f7ab1d9251.png)

### 日付選択機能

`date` または `time` モディファイアを使用すると、テキスト入力欄をmacOSの日付/時刻ピッカーに置き換えることができます。選択された値は、フォーマットされた文字列として返されます。

```sh
--textfield "Start Date,date"
--textfield "Start Time,time"
--textfield "Start Date and Time,date,time"
```

**注意:** `isdate` モディファイアは、`date` および `time` に置き換えられる形で廃止されました。

#### 日付範囲。

`mindate=`と`maxdate=`を使用して、選択可能な日付範囲を制限します。

```sh
--textfield "Pick a day,date,mindate=20260901,maxdate=20260930"
--textfield "No earlier than today,date,mindate=20260928"
--textfield "Before end of year,date,maxdate=20261231"
```

**形式:** 日付は`YYYYMMDD`の形式（地域に依存しない形式）で入力する必要があります。区切り文字は許可されますが、削除されます（例：`2026-09-30` → `20260930`）。無効な日付は無視され、制限は適用されません。

#### 日付の形式。

strftime構文を使用して、返されるデータの形式を指定するには、`format=`を使用します。

```sh
--textfield "Select date,date,format=+%Y-%m-%d"
--textfield "Get epoch,date,value=20260901,format=+%s"
```

一般的な書式文字列：
- `+%Y-%m-%d` - ISO 8601 形式 (例：`2026-09-29`)
- `+%s` - Unixタイムスタンプ（エポックからの秒数）
- `+%x` - ローケールの日付表示形式。
- `+%D` - 米国形式（例：`09/29/26`）

#### 日付ピッカーの初期設定。

初期の日付を設定するには、`value=`を使用します。 このカレンダーは、複数の形式に対応しています。

```sh
--textfield "Start date,date,value=2026-09-30"
--textfield "Start date,date,value=September 30, 2026"
--textfield "Start date,date,value=1759132800"
```

対応形式：ISO 8601形式、地域設定に合わせた形式、12時間/24時間形式、エポックタイムスタンプ、および自然言語。

### ファイル選択

`fileselect` は、標準のファイル選択ダイアログを開く「選択」ボタンを追加します。 選択されたパスは入力欄に表示され、出力として返されます。

```sh
--textfield "Config File,fileselect"
```

`filetype` を使用して、選択できるものを制限します。値はスペースで区切られており、ファイル拡張子またはファイルの種類を示すキーワードを指定できます。

| 価値 | 選択肢。 |
|---|---|
| `folder` | ディレクトリのみ。 |
| `image` | あらゆる種類の画像。 |
| `movie` / `video` | あらゆる種類の動画。 |
| `audio` | あらゆる種類の音声ファイル。 |
| `<extension>` | その拡張子（例：`png`、`pdf`）を持つファイル。 |

```sh
--textfield "Select an image,fileselect,filetype=png jpg"
--textfield "Select a folder,fileselect,filetype=folder"
```

`path=<path>` を使用して、ファイル選択ダイアログが開くディレクトリを指定します。

```sh
--textfield "Log File,fileselect,path=/var/log"
```

![image](https://user-images.githubusercontent.com/3598965/235909743-17cbbc69-65f4-48ea-a143-0594201e44e0.png)

### 確認する。

`confirm` は、主要な入力フィールドの下に、もう一つのフィールドを追加します。 swiftDialog が入力を受け入れるためには、両方のフィールドに同じ値が入力されている必要があります。 パスワードの確認などに役立ちます。

```sh
--textfield "Password,secure,required,confirm"
```

<img width="500" alt="Screenshot 2024-05-19 at 5 03 46 PM" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db3873ed-24a3-4722-a2c2-cacb98ddbcf9">

### 修飾語の組み合わせについて。

修正子は、互換性がある場合に、自由に組み合わせて使用できます。

```sh
--textfield "<label>,secure,required,prompt="<prompt_text>""
--textfield "<label>,required,regex="\d{5}",regexerror="Five digits required",prompt="00000""
--textfield "<label>,fileselect,filetype="jpeg jpg png",path=/Users/Shared"
```

### JSON形式

テキストフィールドは、JSON形式で以下の2つの方法で指定できます。

#### 全体設定用のJSONファイル。

JSON形式の設定ファイルや、`--jsonstring`/`--jsonfile`を使用する場合、テキストフィールドを配列として指定してください。

```json
{
  "textfield" : [
    {"title" : "<label>", "required" : true, "secure" : true, "prompt" : "<prompt_text>"},
    {"title" : "<label>", "editor" : true},
    {"title" : "<label>", "fileselect" : true, "filetype" : "png jpg"},
    {"title" : "<label>", "date" : true, "mindate" : "20260901", "maxdate" : "20260930", "format" : "+%Y-%m-%d"},
    {"title" : "<label>", "time" : true, "value" : "14:30"},
    {"title" : "<label>", "regex" : "\\d{5}", "regexerror" : "Five digits required"},
    {"title" : "<label>", "secure" : true, "confirm" : true}
  ]
}
```

#### 引数ごとのJSON設定。

3.1.1以降、テキストフィールドは、カンマで区切られた修飾子を使用する代わりに、JSONオブジェクトとして指定することも可能です。これにより、より直接的な制御が可能になり、特に複雑な設定において役立ちます。`--textfield`

**構文:**
```bash
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'
```

**特徴：**
- `title` - フィールドラベルのテキスト。
- `name` - 代替の出力キー名。
- `required` - 入力必須項目 (真/偽)
- `secure` - 入力内容をリアルタイムで表示しないようにする（パスワード入力欄など）。
- `passwordfill` - macOSのパスワード自動入力機能を有効にする（`secure`が必要です）。
- `prompt` - フィールド内に表示されるプレースホルダーテキスト。
- `value` - フィールドにデフォルト値を自動的に設定します。
- `regex` - 入力フィールドの内容が、指定された正規表現に一致することを必須とします。
- `regexerror` - 正規表現が条件を満たさない場合に表示される、カスタムエラーメッセージ。
- `editor` - 単一行の入力欄ではなく、複数行のテキストエディタを使用します。
- `date` - フィールドを日付選択機能に置き換える (true)
- `time` - フィールドを日付・時刻選択コントロールに置き換える (true)
- `mindate` - 選択可能な最小日付 (YYYYMMDD形式)
- `maxdate` - 選択可能な最新の日付（YYYYMMDD形式）。
- `format` - `strftime` 構文を使用して日付を文字列として返します (例: `+%Y-%m-%d`, `+%s`)。
- `fileselect` - ファイル選択ダイアログを開く「選択」ボタンを追加します。
- `filetype` - ファイル選択ダイアログを特定のファイル形式（スペースで区切られた拡張子またはキーワード）に制限します。
- `path` - ファイル選択ダイアログの初期表示ディレクトリ。
- `confirm` - 確認用の入力欄を追加し、これは必須項目とし、入力値が最初の入力欄の値と一致する必要があるように設定します。

**例：**

```bash
# Basic required field with prompt
dialog --textfield '{"title":"Name","required":true,"prompt":"Enter your full name"}'

# Secure field with password fill
dialog --textfield '{"title":"Password","secure":true,"passwordfill":true,"prompt":"Enter password"}'

# Date picker with bounds
dialog --textfield '{"title":"Select Date","date":true,"mindate":"20260901","maxdate":"20260930","format":"+%Y-%m-%d"}'

# Time picker with default value
dialog --textfield '{"title":"Select Time","time":true,"value":"14:30"}'

# File picker with restrictions
dialog --textfield '{"title":"Select Config","fileselect":true,"filetype":"json plist","path":"/Library/Preferences"}'

# Multi-line editor
dialog --textfield '{"title":"Notes","editor":true}'

# Regex validation
dialog --textfield '{"title":"Product Code","prompt":"Enter 5 digit code","regex":"\\d{5}","regexerror":"Must be a five digit number"}'

# Confirmation field
dialog --textfield '{"title":"Password","secure":true,"required":true,"confirm":true}'
```

**日付選択フィールド:**
- `"date": true`または`"time": true`（または両方）を使用して、選択コントロールを作成します。
- `"mindate"` と `"maxdate"` は、`YYYYMMDD` 形式の日付を受け付けます（区切り文字は削除されます）。
- `"format"` は、strftime 構文を使用して、返されるデータの形式を設定します。
- `"value"` 初期の日付/時刻を、様々な形式（ISO、地域設定、エポック、自然言語）で記録します。

**サポートされるすべての修飾子:** CSV形式で利用可能なすべての修飾子は、JSONのキーとしても利用可能です。

**複数のテキスト入力欄:**

```bash
dialog --textfield '{"title":"First Name","required":true}' \
       --textfield '{"title":"Last Name","required":true}' \
       --textfield '{"title":"Email","regex":".+@.+\\..+","prompt":"user@example.com"}'
```

**注意:** 引数ごとにJSON形式を使用する場合、各`--textfield`は独立しています。 バッチ初期化には、引き続き全体の設定をJSON形式で記述する方法もサポートされています。

## キーボードの動作について。

任意の1行テキスト入力フィールドで **Return** キーを押すと、ボタン1のアクションが実行されます。これは、デフォルトのボタンをクリックした場合と同じ動作です。ただし、これは`editor`フィールドには適用されません。