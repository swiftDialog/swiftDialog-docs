---
title: チェックボックス。
description: swiftDialogで、インタラクティブなチェックボックスとスイッチを作成する方法。
translationSynced: 2026-11-23T22:52:11+00:00
---

チェックボックスは、ユーザーが選択したり、選択しないように設定したりできる複数のオプションを提供するために使用できます。そして、選択された内容に基づいて、その後の処理を行うことができます。

## 基本的な使い方。

指定された1つ以上の`--checkbox <text>`パラメータに基づいて、ダイアログには、ラベルが`<text>`となっているチェックボックスが表示されます。

### スタイル。

チェックボックスは、チェックボックスとして表示される代わりに、スイッチのような表示にすることも可能です。

デフォルトでは、ラベルの横にチェックボックスが表示されます。

![image](https://user-images.githubusercontent.com/3598965/235893894-1d4c26ba-1afc-4e9f-a58d-16a36c27787f.png)

以下の操作で、スイッチのデザインを変更できます：`--checkboxstyle switch`

![image](https://user-images.githubusercontent.com/3598965/235894156-c8cf82e7-d627-43a4-b11e-3acfc296a3e2.png)

もし、より大きなスイッチのデザインをご希望の場合は、スイッチのデザイン設定において、その旨を明示することができます。

選択肢は、`mini`、`small`、`regular`、または`large`です。

`--checkboxstyle switch,large`

![image](https://user-images.githubusercontent.com/3598965/235894351-71200445-5871-4e27-b792-2a983a34514c.png)
## 高度な利用方法。

[JSON設定](/ja/advanced/json-configuration)を使用してダイアログのオプションを設定する場合、オプションのチェックボックスに関するパラメータが利用可能になります。

JSONデータは、以下の形式で構成されます。

```json
{
  "checkbox" : [
	  {"label" : "<label>", "checked" : false, "disabled" : false, "icon" : "<file|url>" }
	],
 "checkboxstyle" : {
    "style" : "switch",
    "size"  : "regular"
	}
}
```

`"checked" : [true|false]` - この設定が`true`の場合、チェックボックスは初期状態でチェックされた状態になります。デフォルトではチェックされていません。

`"disabled" : [true|false]` - チェックボックスの設定が`true`の場合、チェック状態に関わらず、チェックボックスを無効にします。

`"icon" : "<file|url>"` - これは、`checkboxstyle` が `switch` に設定されている場合にのみ、JSONパラメータとして利用可能です。それ以外の場合は、無視されます。

<img src="https://user-images.githubusercontent.com/3598965/234565903-dad6db14-16aa041aeeca8ffc.png" width=400>

### 引数ごとのJSON設定。

バージョン3.1.1から、チェックボックスもJSONオブジェクトとして指定できるようになりました。具体的には、設定全体をJSONで記述する代わりに、`--checkbox`を使用して指定します。これにより、より詳細な制御が可能になり、特に複雑な設定を行う場合に役立ちます。

**構文:**
```bash
dialog --checkbox '{"label":"Enable telemetry","checked":true,"enableButton1":true}'
```

**特徴：**
- `label` - チェックボックスのラベル表示テキスト
- `checked` - 初期状態 (真/偽、デフォルト: 偽)
- `disabled` - チェックボックスが無効になっているかどうか (true/false、デフォルト: false)。
- `enableButton1` - このチェックボックスが選択されている場合（真の場合）、ボタン1を有効にします（真/偽）。
- `icon` - アイコンのパス、またはJSON形式のアイコンオブジェクト（`switch`スタイルでのみ使用）。

**例：**

```bash
# Basic checkbox
dialog --checkbox '{"label":"I agree to terms"}'

# Checked by default
dialog --checkbox '{"label":"Enable notifications","checked":true}'

# Checkbox that enables Button 1
dialog --checkbox '{"label":"I understand","enableButton1":true}' --button1disabled

# Checkbox with icon (switch style)
dialog --checkbox '{"label":"Enable feature","checked":true,"icon":"/System/Library/CoreServices/Software Update.app"}' --checkboxstyle switch

# Checkbox with JSON icon object
dialog --checkbox '{"label":"Enable","icon":{"sf":"checkmark.circle","colour":"green"}}' --checkboxstyle switch
```

**注意:** `enableButton1`を使用する際には、`--button1disabled`も設定して、チェックボックスが選択される前にボタンがクリックされないようにしてください。

### 設定全体を記述したJSONファイル。

設定ファイル全体をJSON形式で記述する方法は、引き続きサポートされています。

```json
{
  "checkbox" : [
    {"label" : "Option 1", "checked" : true, "disabled" : true },
    {"label" : "Option 2", "checked" : true, "disabled" : false },
    {"label" : "Option 3", "checked" : false }
  ],
  "checkboxstyle" : {
    "style" : "switch",
    "size" : "large"
  }
}
```

### 例

以下に示すJSONデータと、それに対応するダイアログのスクリーンショットは、これらの設定がどのように機能するかを示しています。

```json
{
  "checkbox" : [
	  {"label" : "Option 1", "checked" : true, "disabled" : true },
	  {"label" : "Option 2", "checked" : true, "disabled" : false },
	  {"label" : "Option 3", "checked" : false },
	  {"label" : "Option 4", "checked" : true, "disabled" : true },
	  {"label" : "Option 5" },
	  {"label" : "Option 6", "disabled" : true }
	]
}
```

![image](https://user-images.githubusercontent.com/3598965/150663608-6ee03207-0558-4769-a016-44fe5822fccb.png)

## チェックボックスを使用して、ボタン1の状態を制御します。

チェックボックスを使用して、デフォルトボタンの状態を制御することができます。これは、ユーザーが次のステップに進む前に、必須のオプションが選択されていることを確認したい場合に役立ちます。

例：

`dialog --checkbox "I Agree",enableButton1 --button1disabled`

<img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/5a4d2ce4-ea37-447d-86d1-a12ca9d4807e"> <img width="450" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/ec12eb71-b6f9-466e-ad32-cb8812bc759c">

これは、JSONファイルを使用して設定することも可能です。

```json
{
  "checkbox" : [
    {"label" : "I Agree", "enableButton1" : true }
  ],
  "button1disabled" : true
}
```

 > ボタン1を最初に無効に設定することが重要です。そうしないと、チェックボックスが選択される前に、ユーザーがボタンをクリックしてしまう可能性があります。これはデフォルトでは設定されていません。また、チェックボックスの`disabled`プロパティと`enablebutton1`プロパティの両方を設定することは推奨されません。なぜなら、それによってチェックボックスが操作できなくなるからです。

## 出力。

結果は標準出力に出力され、デフォルトでは以下のようになります。
```
Option 1 : true
Option 2 : true
Option 3 : false
Option 4 : true
Option 5 : false
Option 6 : false
```

オプションとして、`--json` パラメータを指定することで、結果をJSON形式で取得することができます。

```json
{
  "Option 2" : true,
  "Option 4" : true,
  "Option 5" : false,
  "Option 6" : true,
  "Option 1" : true,
  "Option 3" : false
}
```