---
title: swiftDialog ワークフロー。
description: swiftDialogにおける、複数ステップで構成される対話フロー。
translationSynced: 2026-11-23T23:13:40+00:00
---

> **注意:** 「ワークフロー」機能は、swiftDialog 3.1で導入されました。

# swiftDialogのワークフロー機能に関するドキュメント。

## 概要

**Workflow（ワークフロー）**機能を使用すると、swiftDialogで複数のステップを含む対話型ワークフローを作成できます。これにより、ユーザーが複数の入力画面や情報画面を順に表示する、ウィザードのようなユーザーインターフェースを構築できます。各カードは独立した画面を表し、それぞれ独自の構成を持っています。ユーザーは、ワークフロー内で画面を前後に移動することができます。

ワークフローは、JSON形式の設定ファイルを使用して定義されます。これにより、コードを書かずに、複雑で複数のステップを含む対話フローを簡単に作成できます。

## 主な特長：

- **多段階のワークフロー**: 複雑な対話の流れを、扱いやすい段階に分割します。
- **ナビゲーションコントロール**: 自動で「次へ」「前へ」「終了」ボタンを表示します。
- **条件分岐**: ドロップダウンメニューの選択やチェックボックスの状態に基づいて、異なるワークフローカードに分岐させることができます。スクリプトの記述は不要です。
- **データ保持機能**: ワークフローカード間の移動時に、ユーザーが入力したデータが保持されます。
- **グローバル設定:** 共通の設定を一度定義し、必要に応じてカードごとに上書きすることができます。
- **変数の置換**: 以前のワークフローカードから参照値を取得する際に、`{fieldname}`という構文を使用します。
- **入力チェック**: 次のステップに進む前に、必須項目が入力されているかを確認します。
- **動的な構成**: 各カードは、それぞれ異なるUI要素と設定を持つことができます。
- **コールバック機能**: ワークフローのカード間を移動する際に、シェルスクリプトを実行します。

## 基本概念

### ワークフローの構造

ワークフローに基づいた対話フローは、以下の構造を持つJSON設定ファイルで定義されます。

```json
{
  "workflow": [
    { "title": "Step 1", "message": "First screen..." },
    { "title": "Step 2", "message": "Second screen..." },
    { "title": "Step 3", "message": "Final screen..." }
  ]
}
```

### グローバル設定

ルートレベルで定義されたプロパティ（`workflow`配列の外側にあるもの）は、すべてのワークフローカードのデフォルト値として機能します。個々のワークフローカードは、これらのデフォルト値を上書きすることができます。

```json
{
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertNoteIcon.icns",
  "button1text": "Continue",
  "workflow": [
    { "title": "Step 1", "message": "Uses default icon" },
    { "title": "Step 2", "icon": "SF=checkmark.circle", "message": "Custom icon" }
  ]
}
```

### カード識別

カードは、配列内の位置に基づいて自動的に並べ替えられます。必要に応じて、独自の並べ替え順を指定することも可能です。`id`

```json
{
  "workflow": [
    { "id": 0, "title": "First" },
    { "id": 10, "title": "Second" },
    { "id": 5, "title": "Third (will be displayed second)" }
  ]
}
```

## ナビゲーション。

### ボタンの動作。

ワークフローモードでは、ボタンの動作が自動的に変更されます。

- **ボタン1** (右側):
  - ワークフローカードの1番からn-1番まで、「次へ」という表示がされている。
  - 最終カードに「完了」という文字を表示します (または、`button1text`で指定したカスタムテキストを表示します)。
  - 必須項目がすべて入力されていることを確認してから、次のステップに進みます。
  
- **ボタン2** (左側):
  - 最初のカードに隠されています。
  - ワークフローカードの2番目以降に、「前へ」という表示を表示します。
  - 逆方向に移動する際には、検証は行われません。

### ボタンのテキストのカスタマイズ。

デフォルトでは、ナビゲーションボタンは「次へ」、「前へ」、および「終了」と表示されます。これらの表示をカスタマイズするには、以下の方法を使用してください。

- `--nextbuttontext "<text>"` — 「次へ」ボタンの表示テキスト（デフォルト：`Next`）
- `--previousbuttontext "<text>"` — 「前のページ」ボタンの表示テキスト（デフォルト：`Previous`）
- `button1text` (最上位レベルまたはカード単位) - 最終的な「**完了**」ボタンに表示されるテキスト。

```bash
dialog --jsonfile config.json --nextbuttontext "Continue" --previousbuttontext "Back"
```

### ナビゲーションの流れ。

<img width="650" alt="image" src="/images/navigation-flow.png" />


## 分岐型ナビゲーション

デフォルトでは、ワークフローカードは配列の順序で表示されます。ただし、カードごとに設定できる3つのオプションプロパティを使用することで、この表示順序を変更することができます。

| 不動産。 | 種類。 | 目的。 |
|---|---|---|
| `branch` | 物体 | 現在のカードにある特定の値に基づいて、次のカードを選びます。 |
| `nextpage` | 整数 | 静的オーバーライド — 次に、このカードに進んでください `id`。 |
| `finalpage` | ブーリアン型 | このカードはワークフローを終了し、「次」のステータスを「完了」に変更します。 |

ユーザーが「次へ」をクリックすると、swiftDialogは以下の順序で、次にアクセスする場所を決定します。

1. `branch` (設定されており、かつ一致するルールが見つかった場合)
2. `nextpage` (設定されている場合)
3. 配列内の次のカード。
4. ワークフローの終了（次のカードが存在しない場合、または`finalpage`が真の場合）。

「前のボタン」は、ユーザーが実際にどの画面から来たかという履歴を保持しており、「現在のインデックス - 1」という単純な計算ではなく、実際に遷移してきた画面に戻ります。この機能は、異なるセクション間での遷移においても正しく動作します。

> swiftDialogは、ループや到達不能なカードをチェックしません。もしワークフローが自己参照的なループを含む場合、ユーザーは単純にそのカードを再度確認することになります。意図しない動作であれば、ワークフローのロジックをデバッグしてください。

### ドロップダウンメニューから派生する機能。

`branch.field`の値は、フィールドの`name`（推奨）またはその`title`/`label`と一致します。ドロップダウンリストの場合、選択された値は、`branch.map`に定義されたキーと比較されます。

```json
{
  "workflow": [
    {
      "id": 1,
      "title": "Choose your path",
      "message": "Pick an option to control which card appears next.",
      "selectitems": [
        {
          "name": "userType",
          "title": "Account type",
          "values": ["Admin", "Standard", "Guest"],
          "default": "Standard"
        }
      ],
      "branch": {
        "field": "userType",
        "map": {
          "Admin":    10,
          "Standard": 20,
          "Guest":    30
        },
        "default": 99
      }
    },
    { "id": 10, "title": "Admin setup", "nextpage": 99 },
    { "id": 20, "title": "Standard setup", "nextpage": 99 },
    { "id": 30, "title": "Guest setup", "nextpage": 99 },
    { "id": 99, "title": "Summary", "finalpage": true }
  ]
}
```

`branch.default` はオプションです。設定した場合、選択された値が`map`に存在しない場合、ワークフローは代替となるカードに進みます。

### チェックボックスからの分岐。

単一の真偽値フィールドの場合、`map` の代わりに、より簡潔な表記である `ifTrue` / `ifFalse` を使用してください。

```json
{
  "id": 5,
  "checkbox": [
    { "name": "wantsExtras", "label": "Show advanced options" }
  ],
  "branch": {
    "field": "wantsExtras",
    "ifTrue":  6,
    "ifFalse": 99
  }
}
```

`map`は、必要に応じて、キーの`"true"`と`"false"`と組み合わせて使用することもできますが、`ifTrue`/`ifFalse`の方がより分かりやすい表現になります。

### 静的オーバーライド `nextpage`

動的なルーティングが必要ないが、処理を優先的に行いたい場合は、以下の設定を行ってください：`nextpage`

```json
{ "id": 3, "title": "Optional details", "nextpage": 10 }
```

### ワークフローを早期に終了する。

カードを「最終」としてマークすると、その時点でのワークフローは終了します。

```json
{ "id": 99, "title": "Summary", "finalpage": true }
```

最終のカードでは、ボタン1に「終了」と表示され、このボタンをクリックすると、配列内にさらにワークフローカードがいくつ存在しようと、ダイアログが閉じられます。

## 使用例：

### 例1：シンプルな3ステップ形式のウィザード。

```json
{
  "title": "Setup Wizard",
  "icon": "SF=gearshape.2",
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to the setup wizard. Click Continue to begin."
    },
    {
      "title": "Enter Information",
      "message": "Please provide your details:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email Address", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Setup is complete! Click Finish to close this wizard.",
      "button1text": "Finish"
    }
  ]
}
```

実行する。
```bash
dialog --jsonfile /path/to/config.json
```

### 例2：変数の置換の使用方法

変数置換機能を使用すると、以前のワークフローカードに記載された値を、`{fieldname}`という構文を使って参照することができます。

```json
{
  "title": "User Registration",
  "workflow": [
    {
      "title": "Personal Information",
      "message": "Step 1: Enter your details",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true }
      ]
    },
    {
      "title": "Confirmation",
      "message": "Hello {First Name} {Last Name}! Please confirm your information is correct.",
      "infobox": "**Name:** {First Name} {Last Name}"
    }
  ]
}
```

カード2にある`{First Name}`と`{Last Name}`というプレースホルダーは、カード1に入力された値で置き換えられます。

### 例3：グローバル設定と上書き設定について。

```json
{
  "icon": "SF=info.circle",
  "width": 600,
  "height": 400,
  "workflow": [
    {
      "title": "Introduction",
      "message": "This card uses the default icon and size."
    },
    {
      "title": "Custom Layout",
      "icon": "SF=wrench.and.screwdriver",
      "width": 800,
      "height": 500,
      "message": "This card has a custom icon and larger size."
    },
    {
      "title": "Back to Normal",
      "message": "This card reverts to default icon and size."
    }
  ]
}
```

### 例4：複数の段階にわたるデータ収集。

```json
{
  "title": "System Configuration",
  "icon": "/System/Library/PreferencePanes/Appearance.prefPane/Contents/Resources/AppIcon.icns",
  "workflow": [
    {
      "title": "Network Settings",
      "message": "Configure network preferences:",
      "selectitems": [
        {
          "title": "Network Type",
          "values": ["WiFi", "Ethernet", "VPN"],
          "default": "WiFi"
        }
      ]
    },
    {
      "title": "User Preferences",
      "message": "Set user preferences:",
      "checkbox": [
        { "label": "Enable notifications", "checked": true },
        { "label": "Auto-update", "checked": true },
        { "label": "Send analytics", "checked": false }
      ]
    },
    {
      "title": "Summary",
      "message": "Review your settings:",
      "infobox": "**Network:** {Network Type}\\n\\n**Notifications:** {Enable notifications}\\n**Auto-update:** {Auto-update}\\n**Analytics:** {Send analytics}"
    }
  ]
}
```

### 例5：カードを使用した進捗状況表示。

```json
{
  "title": "Installation Wizard",
  "workflow": [
    {
      "title": "Preparing (1 of 3)",
      "message": "Preparing installation...",
      "progress": 100,
      "progresstext": "Checking system requirements"
    },
    {
      "title": "Installing (2 of 3)",
      "message": "Installing software...",
      "progress": 100,
      "progresstext": "Copying files"
    },
    {
      "title": "Complete (3 of 3)",
      "message": "Installation complete!",
      "icon": "SF=checkmark.circle.fill",
      "progress": 100,
      "progresstext": "Finished"
    }
  ]
}
```

### 例6：必須項目の入力チェック機能。

```json
{
  "title": "Registration Form",
  "workflow": [
    {
      "title": "Account Details",
      "message": "All fields marked with * are required",
      "textfield": [
        { "title": "Username", "required": true, "prompt": "Enter username" },
        { "title": "Password", "required": true, "secure": true },
        { "title": "Confirm Password", "required": true, "secure": true }
      ]
    },
    {
      "title": "Contact Information",
      "message": "Please provide at least one contact method",
      "textfield": [
        { "title": "Email", "required": true },
        { "title": "Phone", "required": false }
      ]
    }
  ]
}
```

ユーザーが必須項目を入力せずに「次へ」ボタンをクリックしようとすると、エラーメッセージが表示されます。

## 高度な機能。

### ワークフロー固有のプロパティ。

任意の標準的な swiftDialog プロパティを、ワークフローで使用することができます。一般的なプロパティとしては、以下のようなものがあります。

- **レイアウト**: `width`、`height`、`position`
- **内容**: `title`、`message`、`icon`、`iconsize`
- **入力**: `textfield`、`selectitems`、`checkbox`、`radio`
- **表示**: `image`、`video`、`webcontent`、`listitem`
- **進捗状況**: `progress`、`progresstext`
- **情報**: `infobox`、`helpmessage`
- **スタイル**: `messagefont`、`alignment`、`bannerimage`
- **ナビゲーション**: `branch`、`nextpage`、`finalpage` (「分岐型ナビゲーション」を参照) ](#分岐型ナビゲーション).

### 入力フィールドの命名規則。

変数の置換が正しく機能するためには、入力フィールドの名前が一貫している必要があります。

```json
{
  "textfield": [
    { "title": "First Name" }  // Referenced as {First Name}
  ],
  "selectitems": [
    { "title": "Department", "values": ["IT", "HR", "Sales"] }  // Referenced as {Department}
  ]
}
```

フィールドに明示的な`title`が定義されていない場合、以下の`name`プロパティを使用できます。

```json
{
  "textfield": [
    { "title": "Your Name", "name": "username" }  // Referenced as {username}
  ]
}
```

### データ永続性

ユーザーからの入力は、以下の条件の場合に自動的に保存されます。
- 「次へ」をクリックすると、次のカードに進みます。
- 「前のページ」をクリックすると、前の画面に戻ります。

ユーザーが以前に表示されていた画面に戻ると、入力された内容は復元されます。

### カードデータのアクセス方法について。

ユーザーが最後のカードで「完了」ボタンをクリックすると、入力されたすべてのデータがJSON形式で標準出力に出力されます。

```json
{
  "First Name": "John",
  "Last Name": "Doe",
  "Email Address": "john.doe@example.com",
  "Department": "IT",
  "Enable notifications": true
}
```

### 「アドバンス」機能のコールバック設定。

ワークフローのカード間を移動する際に、特定のオプションを使用することで、シェルコマンドを実行できます。`--onadvance`

```bash
dialog --jsonfile config.json --onadvance "/path/to/script.sh"
```

このスクリプトは、以下の情報を入力として受け取ります：
- カードインデックス (0を基準とする)。
- カードID（指定されている場合）
- 現在、カード情報をJSON形式で標準入力から読み込んでいます。

スクリプトは、以下の状態で終了する必要があります。
- **終了コード 0:** 処理を続行します。
- **終了コードがゼロでない場合：** プロセスの進行を停止し、エラーメッセージを表示します。

コールバックスクリプトの例：
```bash
#!/bin/bash
# script.sh - Validate email format before advancing

input=$(cat)
email=$(echo "$input" | jq -r '.["Email Address"]')

if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$ ]]; then
    echo "Invalid email address format"
    exit 1
fi

exit 0
```

## ベストプラクティス

### 1. ワークフローを集中させる。
各カードには、明確で単一の目的を持たせるようにしてください。 ユーザーが混乱しないように、一つのカードに多くの項目を詰め込みすぎないように注意してください。

### 2. わかりやすいタイトルを使用する。
カードのタイトルは、ユーザーが現在どの段階にいるのかを明確に示すようにしてください。
```json
{ "title": "Step 1: Personal Information" }
{ "title": "Step 2: Contact Details" }
{ "title": "Step 3: Review & Confirm" }
```

### 3. 文脈を提供する。
メッセージ欄を使用して、ユーザーがどのような操作を行う必要があるかを説明してください。
```json
{
  "title": "Account Setup",
  "message": "Create your account by choosing a username and password. Your username must be at least 6 characters."
}
```

### 4. 必須項目チェック機能を使用する。
必須項目には、データが完全であることを確認するために、適切な指示を記載してください。
```json
{ "title": "Email", "required": true }
```

### 5. 要約カードの提供。
収集したすべての情報をまとめた最終確認カードを含めてください。
```json
{
  "title": "Review Your Information",
  "message": "Please verify everything is correct before proceeding.",
  "infobox": "**Name:** {Full Name}\\n**Email:** {Email}\\n**Department:** {Department}"
}
```

### 6. 画面の操作の流れを検討する。
- 最初の画面で、ユーザーに過剰な入力作業を求めないようにしましょう。徐々に操作に慣れてもらうように配慮してください。
- 最も重要なデータ収集は、できるだけ早い段階で行うようにしてください。
- 最終的なカードデザインを確認・確定するには、保存してください。

### 7. 一貫性のあるデザインを採用する。
一貫した表示を実現するために、グローバルなデフォルト設定を定義します。
```json
{
  "icon": "SF=person.crop.circle",
  "width": 700,
  "height": 450,
  "messagefont": "size=13",
  "workflow": [ /* ... */ ]
}
```

## 制限事項と注意事項

1. **コマンドファイル更新について**: コマンドファイルを使用したワークフローモードでは、一部の動的な更新機能が期待通りに動作しない場合があります。ワークフローモードは、主にデータの収集を目的としており、動的なステータス更新には適していません。

2. **ボタンのカスタマイズ**: ボタン1とボタン2の動作は、ワークフローモードによって制御され、ワークフローモード中は完全にカスタマイズすることができません。

3. **終了コード**: ワークフローモードでは、ダイアログは以下の条件の場合にのみ終了します。
   - ユーザーが最後のカードで「終了」ボタンをクリックしました。（終了コード：0）
   - ユーザーが操作を中断しました (終了コードは状況によって異なります)。
   - 検証に失敗し、ユーザーがキャンセルを選択しました。

4. **変数のスコープ**: 前のワークフローカードで定義された変数は、その後のカードでのみ利用可能です。前のカードで定義された変数を、より前のカードで使用することはできません。変数の適用は一方通行です。

5. **フィールド名:** 変数の置換を正しく行うためには、フィールド名に英数字とスペースを使用してください。特殊文字を使用すると、問題が発生する可能性があります。

## トラブルシューティング (問題解決)

### カードが表示されない。
- JSONの構文を、`jsonlint`や類似のツールを使って確認してください。
- 配列が最上位レベルにあることを確認してください。`workflow`
- 少なくとも1つのカードが定義されていることを確認してください。

### 変数置換がうまくいかない場合。
- フィールド名が完全に一致することを確認してください（大文字と小文字を区別します）。
- 変数の参照において、波括弧が正しく使用されているか確認してください。`{fieldname}`
- 参照されているフィールドが、現在のカードではなく、以前のカードに存在していたことを確認してください。

### 検証が機能していません。
- 以下の項目が正しく設定されていることを確認してください。`"required": true`
- そのフィールドが、`title`または`name`のプロパティを持っているか確認してください。
- デバッグログを`--debug`フラグを使って確認する。

### 前のボタンが表示されていません。
- 最初のワークフローカードにいるかどうかを確認してください。（最初のカードでは、前の項目は表示されません。）
- ワークフローモードが実際に有効になっているか（ワークフロー配列が存在するか）を確認してください。

### ブランチが誤ったカードを選択してしまった。
- 確認してください。入力値が、フィールドの該当する項目（または、項目名が設定されていない場合は、その代替項目）と一致しているか。`branch.field` `name` `title` `label`
- ドロップダウンリストの場合、マップのキーと、ユーザーが選択した値が完全に一致するかどうかを比較します。大文字・小文字、および空白文字も区別されます。
- チェックボックスの場合、マップキーとしては、`ifTrue`/`ifFalse`を優先し、`"true"`/`"false"`を避けてください。
- swiftDialogのログを確認してください。無効なターゲットがロード時に報告されます。`nextpage` `branch`

## 完全な例：従業員向けオンボーディング支援ツール。

```json
{
  "title": "Employee Onboarding",
  "icon": "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns",
  "width": 750,
  "height": 500,
  "button1text": "Continue",
  "workflow": [
    {
      "title": "Welcome to the Company!",
      "message": "## Welcome Aboard!\\n\\nThis wizard will guide you through the onboarding process.\\n\\nClick Continue to get started.",
      "icon": "SF=hands.clap.fill",
      "iconsize": 120
    },
    {
      "title": "Personal Information",
      "message": "Please provide your personal details (all fields required):",
      "textfield": [
        { "title": "First Name", "required": true },
        { "title": "Last Name", "required": true },
        { "title": "Employee ID", "required": true },
        { "title": "Work Email", "required": true, "prompt": "name@company.com" }
      ]
    },
    {
      "title": "Department Assignment",
      "message": "Select your department and role:",
      "selectitems": [
        {
          "title": "Department",
          "values": ["Engineering", "Marketing", "Sales", "HR", "Finance"],
          "default": "Engineering"
        },
        {
          "title": "Role",
          "values": ["Manager", "Senior", "Mid-level", "Junior"],
          "default": "Mid-level"
        }
      ]
    },
    {
      "title": "System Preferences",
      "message": "Configure your system preferences:",
      "checkbox": [
        { "label": "Enable email notifications", "checked": true },
        { "label": "Join company Slack", "checked": true },
        { "label": "Subscribe to company newsletter", "checked": true },
        { "label": "Opt-in to mentorship program", "checked": false }
      ]
    },
    {
      "title": "Review & Confirm",
      "message": "Please review your information before completing the onboarding process:",
      "icon": "SF=checkmark.circle",
      "infobox": "**Name:** {First Name} {Last Name}\\n**Employee ID:** {Employee ID}\\n**Email:** {Work Email}\\n\\n**Department:** {Department}\\n**Role:** {Role}\\n\\n**Email Notifications:** {Enable email notifications}\\n**Slack:** {Join company Slack}\\n**Newsletter:** {Subscribe to company newsletter}\\n**Mentorship:** {Opt-in to mentorship program}",
      "button1text": "Complete Onboarding"
    }
  ]
}
```

このファイルを `onboarding.json` として保存し、実行してください。
```bash
dialog --jsonfile onboarding.json
```

## 統合の例：シェルスクリプト。

以下に、ワークフローモードを使用し、その出力を処理する、完全なシェルスクリプトの例を示します。

```bash
#!/bin/bash

# onboarding.sh - Employee onboarding with swiftDialog workflow

DIALOG="/usr/local/bin/dialog"
CONFIG="/tmp/onboarding_config.json"

# Create the JSON configuration
cat > "$CONFIG" << 'EOF'
{
  "title": "Employee Onboarding",
  "icon": "SF=person.crop.circle.badge.checkmark",
  "width": 700,
  "height": 450,
  "workflow": [
    {
      "title": "Welcome",
      "message": "Welcome to Company XYZ! This wizard will set up your account."
    },
    {
      "title": "Enter Details",
      "message": "Please provide your information:",
      "textfield": [
        { "title": "Full Name", "required": true },
        { "title": "Email", "required": true }
      ]
    },
    {
      "title": "Complete",
      "message": "Onboarding complete for {Full Name}!",
      "infobox": "We'll send a confirmation to {Email}"
    }
  ]
}
EOF

# Run dialog and capture output
if output=$("$DIALOG" --jsonfile "$CONFIG" 2>&1); then
    echo "Onboarding completed successfully!"
    echo "Collected data:"
    echo "$output" | jq .
    
    # Extract specific fields
    full_name=$(echo "$output" | jq -r '.["Full Name"]')
    email=$(echo "$output" | jq -r '.Email')
    
    echo "Processing onboarding for $full_name ($email)..."
    
    # Add your custom logic here
    # - Create user account
    # - Send welcome email
    # - Configure systems
    
else
    echo "Onboarding was cancelled or failed"
    exit 1
fi

# Cleanup
rm -f "$CONFIG"
```

## 概要

swiftDialogのワークフロー機能は、シンプルなJSON設定によって、段階的な操作を伴う、ウィザードのようなインターフェースを構築するための強力な手段を提供します。主な利点としては、以下が挙げられます。

- **複雑なワークフローの簡素化** - 複雑なプロセスを、扱いやすいステップに分割します。
- **内蔵ナビゲーション機能** - 自動で「次へ」「前へ」「終了」ボタンが表示されます。
- **データ収集** - 複数の画面にわたって、ユーザーからの入力情報を簡単に収集し、検証できます。
- **柔軟な設定** - グローバルなデフォルト設定を使用し、必要に応じてワークフローごとに個別の設定を上書きすることができます。
- **変数の置換** - ワークフロー内の後続のカードで、以前のカードに設定された値を参照することができます。
- **コーディングは不要** - すべての設定をJSON形式で記述します。

個々の swiftDialog の機能や設定の詳細については、swiftDialog の公式ドキュメントを参照するか、`dialog --help` をご利用ください。
