---
title: 商品リスト
description: ステータス表示やアイコン付きで、動的に並び替え可能なリストを作成します。
translationSynced: 2026-11-23T22:58:30+00:00
---

アイテムリストを使用すると、指定された数のアイテムを順番に並べて表示できます。リストの内容が画面に収まりきらない場合、スクロール機能が有効になります。

リストは、既存のカスタマイズオプションのいずれかと組み合わせて、ダイアログに表示できます。ただし、メッセージ全体を表示する画像を使用するオプションとの組み合わせはできません。

<hr />
アイテムリストを作成する方法は3つあります。

### 1) コマンドライン。

コマンドライン引数として、1つ以上の`--listitem <text>` エントリを指定します。リストは、指定された順序で構築されます。

リスト項目のアイコンは、コマンドライン引数を使用して設定できますが、より高度なオプションが必要な場合は、JSON形式を使用する必要があります。`--listitem "<text>,icon=<image>"`

### 2) JSON形式。

JSONを構成ファイルとして使用する場合、設定項目を一次配列として記述してください。

#### 基本。

基本的な方法は、ステータスが設定されていない項目をリストに追加する簡単な方法です。

```json
{
  "listitem" : ["Item 1", "Item 2", "Item 3"]
}
```

#### 高度な。

「詳細設定」では、リストを初期化し、必要に応じてアイコン、ステータス、およびステータス表示テキストを設定することができます。

```json
{
  "listitem" : [
    {"title" : "Item One", "icon" : "/path/to/image", "status" : "pending", "statustext" : "Pending"},
    {"title" : "Item Two", "icon" : "/path/to/SomeApp.app", "status" : "wait", "statustext" : "Waiting"},
    {"title" : "Item Three", "icon" : "https://some.url/image", "status" : "success", "statustext" : "Winning"}
  ]
}
```

##### ステータスに関するオプション。

リスト項目のステータスは、`wait`、`success`、`fail`、`error`、`pending`、または`progress`のいずれかであり、ステータス領域に適切なアイコンが表示されます。

`progress`をステータスとして使用する場合、ステータスアイコンとして円形の進捗カウンターが表示されます。数値を追加することで、例えば`progress: 20`のようにすると、インジケーターが適切な位置にアニメーションで移動し、表示される割合を表します。進捗インジケーターは、`0`から`100`までの任意の値をサポートします。

<img width="599" alt="image" src="https://user-images.githubusercontent.com/3598965/182604151-3eabe9b5-3f77-4949-9b88-c522676e3314.png">

#### 引数ごとのJSON設定。

バージョン3.1.1以降、リスト項目は、全体の構成ファイル（JSON形式）を使用する代わりに、JSONオブジェクトとして指定することも可能です。これにより、より詳細な制御が可能になり、特に、ネストされたアイコンオブジェクトを含む複雑な構成において有効です。`--listitem`

**構文:**
```bash
dialog --listitem '{"title":"Download","status":"wait","statustext":"Working…"}'
```

**特徴：**
- `title` - リスト項目ラベルのテキスト。
- `status` - 状態表示：`wait`、`success`、`fail`、`error`、`pending`、`progress`、または`progress:<value>` (0～100)
- `statustext` - ステータスインジケーターの横に表示される状態を示すテキスト。
- `icon` - アイコンのパス、URL、または**ネストされたJSON形式のアイコンオブジェクト**。

**ネストされたアイコンオブジェクト:**

この`icon`フィールドでは、高度なアイコン設定を行うためのJSON形式のアイコンオブジェクトを受け付けます。

```bash
# Basic list item with SF Symbol
dialog --listitem '{"title":"Processing","status":"wait","icon":{"sf":"gear","colour":"blue"}}'

# List item with animated icon
dialog --listitem '{"title":"Downloading","status":"progress:50","icon":{"sf":"arrow.triangle.turn","colour":"green","animation":"variable"}}'

# List item with gradient icon
dialog --listitem '{"title":"Installing","status":"wait","icon":{"sf":"arrow.down.circle","colour":"pink","colour2":"purple"}}'

# List item with application icon
dialog --listitem '{"title":"App Installation","status":"success","icon":{"path":"/Applications/MyApp.app"}}'
```

**複数の商品：**

```bash
dialog --listitem '{"title":"Step 1","status":"success","statustext":"Complete"}' \
       --listitem '{"title":"Step 2","status":"wait","icon":{"sf":"gear","colour":"blue","animation":"variable"}}' \
       --listitem '{"title":"Step 3","status":"pending"}'
```

**注意:** 引数ごとにJSON形式を使用する場合、各`--listitem`は独立しています。 バッチ初期化には、引き続き全体の設定をJSON形式で記述する方法もサポートされています。


### 3) コマンドファイルに送信されるコマンドとして。

アイテムをカンマ区切りで送信してください。

`echo "list: Item 1, Item 2, Item 3" >> /var/tmp/dialog.log`


## 既存のリストの更新。

既に表示されているリスト内の項目は、コマンドファイルにコマンドを送信することで、ステータスを更新することができます。


#### 基本。

必要な基本的な構文は以下の通りです。

`echo listitem: <list item title>: <status text> >> /var/tmp/dialog.log`

 - `<list item title>`は、リスト項目名/タイトルと完全に一致している必要があります。大文字と小文字も区別されます。
 - `<status text>` は、任意のUnicodeテキスト文字列です。
   - もしサポートされているステータスキーワードのいずれか送信した場合、テキストの代わりに、対応するインジケーターが表示されます。

#### 高度な。

高度な構文を使用することで、ステータス表示テキストやステータスインジケーターを更新するだけでなく、リスト項目をインデックスで参照することも可能です。キーワードは、カンマで区切られたリストで指定されます（ただし、このため、`title`と`statustext`の項目には、カンマを含むテキストは使用できません）。

`listitem: [title: <title>|index: <index>], status: <status>, statustext: <text>`

`<index>` は 0 から始まります。

e.g.

`listitem: index: 0, status: complete, statustext: Item 1 on the list has completed`

新しい項目は、既存のリストの末尾に、`add:`コマンドを使って追加できます。また、項目は、`delete:`コマンドを使って削除できます。行を追加する際、「ステータス」と「ステータステキスト」はオプションです。

例：

`echo "listitem: add, title: <title>, statustext: <text>, status: <status>" >> /var/tmp/dialog.log`

インデックスによる削除：`echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log`

タイトルを参照して削除する。`echo "listitem: title: Some Row Title, delete:" >> /var/tmp/dialog.log`

現在表示されているリストがなくても、リスト内の項目を追加したり削除したりすることができます。

## リストの表示/非表示。

リストは、その内容を変更することなく、非表示にしたり表示したりすることができます。

表示する `echo "list: show`

非表示にする`echo "list: hide`

## リストの削除。

既存のリストは、コマンドファイルにコマンド `list: clear` を送信することで削除できます。

リストをクリアすると、そのリストに関連付けられているすべての項目と状態が削除されます。

## 例：


`echo "list: Test item 1, Test item 2, Test item 3" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151488006-ba027af7-0736-47b2-abdd-ba847491f086.png)

その後、以下のコマンドを実行することで、リストの状態が更新されます。

`echo "listitem: Test item 1: Complete ✅" >> /var/tmp/dialog.log`

`echo "listitem: Test item 2: There was an error processing this item ❌" >> /var/tmp/dialog.log`

`echo "listitem: Test item 3: wait" >> /var/tmp/dialog.log`

![image](https://user-images.githubusercontent.com/3598965/151486051-967e760e-f164-467f-8bd6-dcccba3c7504.png)

#### 高度なJSON形式。

![image](https://user-images.githubusercontent.com/3598965/163742836-22fd32e8-8010-467f-a518-b4d348619698.png)