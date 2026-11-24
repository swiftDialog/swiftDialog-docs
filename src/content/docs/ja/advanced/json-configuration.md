---
title: JSON設定
description: 複雑な設定を行う際に、JSONを使用してダイアログのオプションを指定する方法。
translationSynced: 2026-11-23T22:58:05+00:00
---

複雑なダイアログを作成するために、多数のコマンドラインオプションを使用する代わりに、`--jsonfile`または`--jsonstring`のオプションを使用してパラメータを定義することができます。

JSON形式は、コマンドラインで指定されたオプションと基本的に同じものを使用しますが、いくつかの例外と考慮事項があります。

**注意:**
 - コマンドラインオプションはJSONファイルと組み合わせて使用できますが、JSONファイルで定義されたオプションが優先されます。
 - メッセージ本文に特殊文字を正確に含めるためには、`\n`がJSON形式の入力データを1行で記述することを前提としています。`--jsonstring`

例：

```json
{
  "title" : "An Important Message",
  "titlefont" : "colour=red",
  "icon" : "/Applications/Remote Desktop.app",
  "hideicon" : true,
  "infobutton" : true,
  "quitoninfo" : true,
  "image" : "/Users/Shared/Pictures/Image 1.jpg",
  "imagecaption" : "Test image 1"
}
```

## コマンドラインオプションとの違い。

繰り返し使用できる選択肢は、配列として入力することができます。

例えば、複数の画像と画像キャプションを指定する場合、`image` 配列を使用し、その中に`imagename, caption` を含めます。

```json
{
  "image" : [
    {"imagename" : "/Users/Shared/Pictures/Image 1.jpg", "caption" : "Test image 1"},
    {"imagename" : "/Users/Shared/Pictures/Image 2.jpg", "caption" : "Test image 2"},
    {"imagename" : "/Users/Shared/Pictures/Image 3.jpg", "caption" : "Test image 3"}
  ]
}
```

チェックボックスは、チェック状態であるか、または無効になっているかを指定できます。デフォルトは`"disabled" : false`であり、特に指定する必要はありません。

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5", "checked" : false },
	  {"label" : "Option 6", "checked" : true }
	]
}
```

複数の選択肢がある場合、フィールド名が配列として含まれる、単一のテキストフィールドを指定してください。`textfield`

```json
{
  "textfield" : ["Text Entry 1", "Text Entry 2", "Text Entry 3"]
}
```

### 文字列と真偽値。

多くのオプションは、指定された値を文字列として扱い、引用符で囲む必要があります。ただし、一部の値は、ブール値（真：`true`、偽：`false`）として指定することも可能です（この場合、引用符は不要です）。ブール値を受け取るオプションは以下の通りです。

```json
{
  "button2" : false
  "infobutton" : false
  "hideicon" : false
  "moveable" : false
  "ontop" : false
  "small" : false
  "big" : false
  "fullscreen" : false
  "json" : false
  "ignorednd" : false
  "hidetimerbar" : false
  "quitoninfo" : false
}
```

### JSONファイルから取得できないオプションがあります。

JSONで利用可能なオプションの中には、運用環境においては適切でないものがいくつか存在します。それらは以下の通りです。

* `--jh` - JamfHelperコマンドラインオプションを受け入れるために、既存のシステムに組み込んで使用できます。
* `--listfonts` - プロトタイプの開発段階で使用され、利用可能なフォントの一覧を表示します。
* `--help` - ヘルプテキストを表示し、プログラムを終了します。プロトタイプ作成時に使用されます。
* `--demo` - デフォルト設定のみを使用してダイアログを表示します。プロトタイプ作成時に使用されます。
* `--version` - ダイアログのバージョン情報を表示し、プログラムを終了します。
* `--showlicense` - ライセンス情報を表示し、終了します。
* `--coffee` - コーヒーに関する情報を表示し、プログラムを終了します。

## 例：PythonでJSONデータを生成し、それをファイルとしてまたは文字列として渡す。

```python
#!/usr/bin/python3

import json
import os

# set to false to generate an intermediate json file
# set to true to pass generated json in as a string
stringinput = True

dialog_app = "/Library/Application Support/Dialog/Dialog.app/Contents/MacOS/Dialog"

contentDict = {"title" : "An Important Message",
            "titlefont" : "name=Chalkboard,colour=#3FD0a2,size=40",
            "message" : "This is a **very important** messsage and you _should_ read it carefully\n\nThis is on a new line",
            "icon" : "/Applications/Safari.app",
            "hideicon" : false,
            "infobutton" : true,
            "quitoninfo" : true
            }

jsonString = json.dumps(contentDict)

if stringinput:
    print("Using string Input")
    os.system("'{}' --jsonstring '{}'".format(dialog_app, jsonString))
else:
    print("Using file Input")

    # create a temporary file
    jsonTMPFile = "/tmp/dialog.json"
    f = open(jsonTMPFile, "w")
    f.write(jsonString)
    f.close()

    os.system("'{}' --jsonfile {}".format(dialog_app, jsonTMPFile))

    # clean up
    os.remove(jsonTMPFile)
```