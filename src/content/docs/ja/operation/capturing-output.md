---
title: Dialogの出力の取得方法について。
description: ユーザーからの入力データの取得方法と、対話結果の処理方法。
translationSynced: 2026-11-23T23:29:54+00:00
---

Dialogから結果を取得したり、ユーザーが行った操作や入力されたデータを確認したりする方法はいくつかあります。

## 戻り値コード

最も基本的なダイアログには、少なくとも一つのボタンがあり、そのボタンをクリックすると、ステータスコード `0` を返して終了します。

オプションのボタンは、`--button2`、`--infobutton` (またはその派生機能) を通じて利用でき、クリックすると、クリックされたボタンに応じて、コード `2` または `3` が返されます。

以下の戻り値コードは、各操作の実行後に送信されます。これらは無視することも、呼び出し元のスクリプトでさらなる処理を行うために利用することも可能です。

| 行動 | オプション | ホットキー | 戻り値コード |
| ----------- | -------- | ------ | ----------- |
| `button1`   | いいえ。       | 入力してください。  | 0           |
| `button2`   | はい。      | （このテキストは不完全です。翻訳はできません。）    | 2           |
| `infobutton` | はい。      |        | 3           |
| \<timer\>   | はい。      |        | 4           |
| コマンドファイル `quit:` | はい。 |    | 5           |
| `--quitkey` | はい。      | Command + Q (または、macOS環境では「⌘ + Q」)  | 10          |
| 認証エラーが発生しました。 | はい。  |        | 30          |
| 画像が見つかりませんでした。 | |    | 201         |
| ファイルが見つかりません。 |       |        | 202         |


スクリプト内でリターンコードを処理するには、bashを使用するか、選択したスクリプト言語で、`$?`から結果を取得してください。

例：`zsh`における戻り値の処理について。

```zsh
#!/bin/zsh
dialog ...<options_here>
case $? in
  0)
  echo "Pressed OK"
  # Button 1 processing here
  ;;
  2)
  echo "Pressed Cancel Button (button 2)"
  # Button 2 processing here
  ;;
  3)
  echo "Pressed Info Button (button 3)"
  # Button 3 processing here
  ;;
  4)
  echo "Timer Expired"
  # Timer ran out code here
  ;;
  5)
  echo "quit: command used"
  # post quit: command code here
  ;;
  10)
  echo "User quit with cmd+q"
  # User quit code here
  ;;
  30)
  echo "Key Authorisation Failed"
  # Key auth failure code here
  ;;
  201)
  echo "Image resource not found"
  ;;
  202)
  echo "Image for icon not found"
  ;;
  *)
  echo "Something else happened"
  ;;
esac
```


## 標準出力 (標準出力ストリーム)

リターンコードに加えて、1つ以上の`--textfield`または`--selectvalues`が指定された場合、出力は`sdtout`に送信されます。デフォルトの出力形式は、ラベルと出力を区切るために`:`という文字を使用する以外は、整形されていない状態です。

以下に、ダイアログの例とユーザーからの入力内容を示します。

`dialog --textfield "text 1" --textfield "text 2" --selecttitle "make selection" --selectvalues "one,two,three,four"`

<img width="932" alt="image" src="https://user-images.githubusercontent.com/3598965/127793083-b07b4b46-8da6-46ee-a4ce-fcca84949a31.png">

出力結果は以下のようになります。

```
 SelectedOption : three
 SelectedIndex : 2
text 1 : one
text 2 : two
```

`SelectedOption` は選択されたドロップダウンメニューのオプションのテキストです。`SelectedIndex` は選択されたオプションのインデックスです（インデックスは0から始まるため、インデックス2はリストに表示されている3番目のオプションが選択されたことを意味します）。

テキストフィールドは、ダイアログに渡されたラベルを、出力時のラベルとして使用して表示されます。したがって、上記の例では、そのように表示されます。

`text 1` は、「テキスト1」とラベル付けされたテキストフィールドに入力されたテキストを表示します。`text 2` も同様です。

これらの情報を分割するには、例えば、出力の各行を処理するために、`awk`を使用することができます。
```bash
/usr/local/bin/dialog <...> | grep "SelectedOption" | awk -F " : " '{print $NF}'
```

より高度な処理を行う場合、`--json` パラメータを指定することで、出力結果をJSON形式に変換し、JSONパーサー（例えばPythonなど）を使用して処理することができます。

上記の例に対するJSON形式の出力は、以下のようになります。
```json
{
"SelectedOption" : "three",
"SelectedIndex" : 2,
"text 1" : "one",
"text 2" : "two"
}
```

## 追加の例：

Pythonを使って、プログラムの出力と終了コードを取得する方法：
```python
import subprocess

result = subprocess.Popen("/usr/local/bin/dialog <...>")
text = result.communicate()[0]   # contents of stdout
return_code = result.returncode  # return code
```