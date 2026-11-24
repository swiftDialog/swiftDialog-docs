---
title: コマンドラインオプション。
description: swiftDialogのコマンドラインオプションと引数に関する完全な参照ガイド。
translationSynced: 2026-11-24T00:10:12+00:00
---

Dialogの設定は、コマンドラインオプションを通じて行えます。すべてのオプションは、JSON形式の設定ファイルでも指定可能です。[JSON設定](/ja/advanced/json-configuration)

```sh
dialog --title "Hello" --message "World"
```

特定のオプションに関する詳細情報については、`--help <option>` を参照してください。

---

## 内容。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--title <text>` | `-t` | ダイアログのタイトルを設定します。非表示にする場合は、`none` を使用してください。 |
| `--subtitle <text>` | | タイトル下部に表示される、補足的なテキスト。また、[通知](/ja/advanced/notifications)のサブタイトルとしても使用されます。 |
| `--message <text>` | `-m` | ダイアログメッセージを設定します。マークダウン記法に対応しています。](/ja/basic-use/markdown) |
| `--messagealignment [left\|centre\|right]` | | メッセージの水平方向の配置。 |
| `--messageposition [top\|centre\|bottom]` | | メッセージ内容ブロックの垂直方向の位置。 |
| `--titlefont <params\|json>` | | タイトルフォントを変更します。カンマ区切りの`key=value`ペア、またはJSONオブジェクトを受け付けます：`colour`、`size`、`weight`、`name`、`alignment`、`offset`、`shadow` |
| `--messagefont <params\|json>` | | メッセージのフォントを変更します。カンマ区切りの`key=value`のペア、またはJSONオブジェクトを受け付けます。 |

詳細は、[タイトル](/ja/basic-use/title)と[メッセージ](/ja/basic-use/message)をご覧ください。

---

## アイコン

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--icon <file\|url\|json>` | `-i` | ダイアログアイコンを設定します。ファイルパス、URL、SFシンボル（`SF=name`）、プリセット、またはJSONオブジェクトを指定できます。 |
| `--iconsize <num>` | | アイコンのサイズ（ポイント単位）。デフォルト値は150です。 |
| `--iconalpha <num>` | | アイコンの透明度を0.0（透明）から1.0（不透明）までの範囲で調整できます。 |
| `--iconalttext <text>` | | アイコンのアクセシビリティラベル。 |
| `--overlayicon <file\|url\|json>` | `-y` | アイコンの右下に表示されるオーバーレイ画像です。サポートするファイル形式は、`--icon`と同じです。 |
| `--hideicon` | `-h` | アイコンを非表示にすると、メッセージ表示領域が広くなります。 |
| `--centreicon` / `--centericon` | | アイコンを、タイトルとメッセージの中央に配置し直してください。 |

詳細は[アイコン](/ja/basic-use/icon)]をご覧ください。

---

## バナーと背景。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | ダイアログの上部にバナー画像を表示します。 |
| `--bannertitle <text>` | | バナーの上に、タイトルテキストを表示します。 |
| `--bannertext <text>` | | `--bannertitle`と`--title`を設定することに相当します。 |
| `--bannerheight <num>` | | バナーの高さを設定してください。 |
| `--background <file>` | `-bg` | 背景画像または透かし画像を設定します。 |
| `--bgalpha <num>` | `-ba` | 背景画像の透明度（デフォルト：0.5）。 |
| `--bgposition <position>` | `-bp` | 背景画像の配置場所（例：`center`、`topleft`）。 |
| `--bgfill [fill\|fit]` | `-bf` | 背景画像の塗りつぶしモード。 |
| `--bgscale [fill\|fit]` | `-bs` | 背景画像の拡大縮小モード。 |
| `--screenbackground <file\|url>` | | ダイアログウィンドウの背面に、画像をフルスクリーンで表示します。 |

詳細は、[バナー画像](/ja/advanced/banner-images)と[背景画像](/ja/advanced/background-images)をご覧ください。

---

## ボタン

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--button1text <text>` | | ボタン1のラベル (Returnキーに割り当て、デフォルト: `OK`)。 |
| `--button1action <url>` | | ボタン1がクリックされた際に開くURL。 |
| `--button1shellaction <cmd>` | | ボタン1がクリックされたときに実行されるシェルコマンド。 |
| `--button1symbol <sf symbol\|json>` | | ボタン1に使用するSF SymbolまたはJSONオブジェクト。 |
| `--button1disabled` | | ボタン1が無効な状態で起動します。 |
| `--button2` | `-2` | ボタン2を表示。 |
| `--button2text <text>` | | ボタン2のラベル（Escキーに割り当て、デフォルト：`Cancel`）。 |
| `--button2symbol <sf symbol\|json>` | | ボタン2に使用するSFシンボルまたはJSONオブジェクト。 |
| `--button2disabled` | | ボタン2が無効の状態での起動。 |
| `--infobutton` | `-3` | 情報ボタンを表示します。 |
| `--infobuttontext <text>` | | 情報ボタンのラベル。 |
| `--infobuttonaction <url>` | | 情報ボタンがクリックされたときに開くURL。 |
| `--infobuttonsymbol <sf symbol\|json>` | | 情報ボタンに使用する、SF Symbol または JSON オブジェクト。 |
| `--buttonstyle [center\|stack]` | | ボタンの配置スタイル。 |
| `--buttonsize [mini\|small\|regular\|large]` | | ボタンのサイズ。 |
| `--buttontextsize <num>` | | ボタンのラベルのフォントサイズ。 |
| `--quitoninfo` | | 情報ボタンが選択されたときに、終了確認ダイアログを表示します。 |

詳細は[ボタン](/ja/basic-use/buttons)]をご覧ください。

---

## ワークフロー

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--nextbuttontext <text>` | | ワークフローの「次へ」ボタンのラベル（デフォルト：`Next`）。 |
| `--previousbuttontext <text>` | | ワークフローの「前の」ボタンのラベル（デフォルト：`Previous`）。 |
| `--onadvance <command>` | | ワークフローのページ間を移動する際に実行されるシェルコマンド。<br> (標準入力からデータを受け取り、正常終了しない場合はページ遷移がブロックされます)。 |

詳細は、[ワークフロー](/ja/advanced/workflows)] をご参照ください。

---

## ヘルプメッセージ

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--helpmessage <text>` | | ヘルプボタンを表示し、ポップオーバー形式で詳細な内容を表示します。Markdown形式に対応しています。 |
| `--helpimage <file\|url>` | | ヘルプのポップオーバーに画像を追加します。 |
| `--helpsheetbuttontext <text>` | | ヘルプシートの「閉じる」ボタンのラベル (デフォルト: `OK`)。 |
| `--helpalignment [left\|centre\|right]` | | ヘルプメッセージの内容の調整。 |

詳細は、[ヘルプメッセージ](/ja/operation/help-message)] をご確認ください。

---

## 画像、動画、およびウェブコンテンツ。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--image <file\|url>` | `-g` | 画像を表示します。複数の画像をまとめて表示すると、カルーセル形式になります。 |
| `--imagecaption <text>` | | 画像の下に表示されるキャプション。 |
| `--video <file\|url>` | | 動画を表示します。`youtube=<id>` および `vimeo=<id>` のショートカットに対応しています。 |
| `--videocaption <text>` | | 動画の下に表示される字幕。 |
| `--autoplay` | | 起動時に自動で動画を再生する。 |
| `--webcontent <url>` | | メッセージ表示領域にウェブページを表示します。 |

詳細は、[画像](/ja/basic-use/images)]、[動画](/ja/basic-use/video)]、および[ウェブコンテンツ](/ja/basic-use/web-content)]をご覧ください。

---

## 情報エリア

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--infotext <text>` | | 「情報」ボタンを、固定テキストに置き換えます。 |
| `--infobox <text>` | | アイコンの下に、テキスト（Markdown形式に対応）を表示します。 |
| `--infoboxwidth <num>` | | アイコンのサイズとは独立して、情報ボックスの幅を設定できるようにする。 |

詳細は、[情報ボックス](/ja/advanced/info-box)] をご確認ください。

---

## ユーザー入力。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--textfield <text\|json>[,options]` | | テキスト入力フィールドを追加します。 `required`、`secure`、`prompt`、`regex`、`fileselect`、`date`、`time`、`mindate`、`maxdate`など、さまざまな形式に対応しています。また、JSONオブジェクトとして指定することも可能です。 |
| `--textfieldlivevalidation` | | テキストフィールドに入力した内容に対して、リアルタイムで正規表現による検証結果を表示します。 |
| `--checkbox <text\|json>` | | 指定されたラベルを持つチェックボックスを追加します。JSONオブジェクトとして指定することも可能です。 |
| `--checkboxstyle [checkbox\|switch][,size]` | | チェックボックスの表示を変更する。 |
| `--selecttitle <text>[,options]` | | 指定された名前のドロップダウン選択リストを追加します。 |
| `--selectvalues <csv>` | | 選択リストの項目を、カンマで区切って記述します。 |
| `--selectdefault <text>` | | 選択リストのデフォルトで選択される値。 |
| `--selectstyle` | | 選択肢リストのスタイル設定。 |
| `--selectitem <json>` | | 選択肢として機能するリスト項目を、JSONオブジェクトの構文を用いて定義します。 |

詳細は、[テキスト入力欄](/ja/advanced/textfields)]、[チェックボックス](/ja/advanced/checkboxes)]、および[選択リスト](/ja/advanced/select-lists)]をご参照ください。

### 引数ごとのJSON設定。

カンマ区切りの値を受け付ける多くの引数オプションは、JSONオブジェクトとしても指定できます。これにより、より直接的な制御が可能になり、特に複雑な設定を行う場合に役立ちます。

**検出:** 値がJSONオブジェクトとして解析できる場合、JSONパーサーが使用されます。それ以外の場合は、CSVパーサーが適用されます。

**サポートされている主張：**
- `--textfield` - 全ての調整オプションが設定された、フルフィールド構成。
- `--checkbox` - アイコン付きのチェックボックスと、ボタンの有効/無効設定。
- `--listitem` - アイコンオブジェクトがネストされたリスト項目。
- `--selecttitle` - `--selectitem` と全く同じ扱いがされます。
- `--selectitem` - JSON形式で定義された選択肢リスト項目。
- `--titlefont` / `--messagefont` - フォントの設定：色、サイズ、太さ、影の調整。
- `--icon` / `--overlayicon` - シンボル、色、カラースキーム、アニメーションなどを備えたアイコンオブジェクト。
- `--button1symbol` / `--button2symbol` / `--infobuttonsymbol` - ボタンの記号と配置に関する情報。

詳細なJSONスキーマとサンプルについては、各ドキュメントページを参照してください。

---

## 商品リスト

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--listitem <text\|json>` | | リスト項目を追加します。ステータスアイコンとクリック時のアクションをサポートしています。また、JSONオブジェクトとして指定することも可能で、この際、ネストされたアイコンもサポートされます。 |
| `--liststyle [expanded\|compact]` | | リストの行間の垂直方向の間隔。 |
| `--enablelistselect` | | 許可リストにある項目を選択できるようにし、選択された項目を終了時に返します。 |

詳細は、[アイテムリスト](/ja/advanced/item-lists)] をご確認ください。

---

## タイマーと進捗状況。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--timer [<seconds>]` | | 指定された時間（デフォルト：10秒）をカウントダウン表示します。タイムアウトした場合、エラーコード4で終了します。 |
| `--hidetimerbar` | | タイマー表示バーを非表示にしながら、カウントダウンを継続します。 |
| `--hidetimer` | | タイマーを完全に非表示にします。 |
| `--progress [<int>]` | | 指定されたステップ数で、進捗状況を示すプログレスバーを表示します。 |
| `--progresstext <text>` | | 進捗状況のバーの下に、初期表示されるテキスト。 |

詳細は、[タイマーと進捗状況⟧ をご参照ください。](/ja/advanced/timer-progress)

---

## ウィンドウのサイズと位置。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--width <num>` | | ダイアログウィンドウの幅（ポイント単位）。 |
| `--height <num>` | | ダイアログウィンドウの高さ（ポイント単位）。 |
| `--small` | `-s` | デフォルトのウィンドウサイズを25%縮小します。 |
| `--big` | `-b` | デフォルトのウィンドウサイズを25%拡大します。 |
| `--position <position>` | | ウィンドウの位置（例：`center`、`topright`、または`x,y`）。 |
| `--positionoffset <int>` | | エッジのオフセット値（デフォルト：16）。`--position`を使用する場合に適用されます。 |
| `--moveable` | `-o` | ウィンドウをドラッグできるようにする。 |
| `--resizable` | | ウィンドウのサイズを変更できるようにする (意図する意味合い：`--moveable`)。 |
| `--ontop` | `-p` | 他のウィンドウよりも常にこのウィンドウを最前面に表示してください。 |
| `--windowbuttons [close,min,max]` | | ウィンドウの閉じる、最小化、最大化ボタンを有効にします。 |
| `--showonallscreens` | | 接続されているすべての画面にウィンドウを表示します。 |
| `--appearance [dark\|light]` | | ウィンドウの外観をオーバーライドします |

詳細は、[ウィンドウサイズ](/ja/advanced/window-size)と[レイアウト](/ja/advanced/layout)をご覧ください。

---

## ウィンドウのスタイル設定プリセット。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--style <preset>` | | プリセットスタイルを適用する：`presentation`、`mini`、`centered`、`alert`、`caution`、`warning` |
| `--mini` | | タイトル、アイコン、および2行で構成されるメッセージを表示する、コンパクトなウィンドウ。 |
| `--fullscreen` | `-f` | フルスクリーンモード（ボタンは表示されず、キーボード操作は引き続き有効です）。 |
| `--presentation` | | 進捗状況を示すプログレスバーと、整理されたレイアウトを備えたプレゼンテーションモード。 |
| `--eula` | | EULA（エンドユーザーライセンス契約）の同意画面を表示します。 |
| `--blurscreen` | | ダイアログウィンドウの背後にある画面上のすべてのコンテンツをぼかします。 |
| `--hideotherapps` | | 起動時に他のすべてのアプリを非表示にします。 |

詳細は、[フルスクリーン](/ja/advanced/full-screen)と[プレゼンテーションモード](/ja/advanced/presentation)をご覧ください。

---

## 通知

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--notification` | | macOSのシステム通知を送信します。 |
| `--identifier <text>` | `-id` | 通知の一意な識別子。 |
| `--remove` | | 一致する`--identifier`に対応する通知を削除してください。 |
| `--enablenotificationsounds` | | 通知音を有効にする。 |

詳細は、[通知](/ja/advanced/notifications)] をご確認ください。

---

## 音

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--sound <file\|url>` | | 起動時に音声ファイルを再生します。 |
| `--showsoundcontrols` | | 再生コントロール（再生/一時停止、ミュート、タイムライン）を表示します。 |

---

## ドックのアイコン。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--showdockicon` | | macOSのドックに、Dialogアイコンを表示します。 |
| `--dockicon <file\|url>` | | Dockアイコンとしてカスタム画像を表示します（`--showdockicon`を意味します） |
| `--dockiconbadge <text>` | | ドックのアイコンに、目に見えるバッジを表示します。 |

---

## コマンドファイル

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--commandfile [<file>]` | | ライブダイアログの更新に使用するコマンドファイルへのパス（デフォルト：`/var/tmp/dialog.log`）。 |
| `--displaylog <file>` | | ファイルの内容を、そのまま表示します。 |
| `--loghistory [<int>]` | | `--displaylog` を、直近の N 行（デフォルト：100 行）で初期表示します。 |

詳細は、[コマンドファイル](/ja/advanced/command-file)] をご参照ください。

---

## JSON 入出力

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--jsonfile <file>` | | JSONファイルからダイアログの設定を読み込みます。 |
| `--jsonstring <text>` | | JSON形式の文字列からダイアログの設定情報を読み込みます。 |
| `--json` | `-j` | 結果をJSON形式で出力します。 |

詳細は、[JSON設定](/ja/advanced/json-configuration)をご覧ください。

---

## キーボードと操作方法

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--quitkey <char>` | | カスタム終了キー（使用するキーとして指定、デフォルト：`q`）。`⌘ + <key>` |
| `--hidedefaultkeyboardaction` | | キーボードのReturn/Escキーの機能を、特定の条件が満たされた場合にのみ有効にする。`⌘ + ⇧` |
| `--alwaysreturninput` | | プログラムが終了する際に、常にユーザーからの入力を返却するようにします。終了コードに関わらず、この動作を維持します。 |
| `--ignorednd` | `-d` | 「邪魔しないで」モードが有効になっている場合でも、ダイアログを表示します。 |
| `--vieworder <csv>` | | 入力要素の表示順序を上書きします。 |

---

## 承認

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--key <string>` | `-k` | ダイアログを開始するには、認証キーが必要です。 |
| `--checksum <string>` | | SHA256ハッシュ値を生成します（`--key`で使用するために）。 |

詳細は、[権限に関する記述](/ja/operation/authorization)] をご参照ください。

---

## ログイン画面

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--loginwindow` | | ログイン画面にダイアログを表示します。（適切なLaunchAgentが必要です。） |

詳細は、[ログイン画面⟧をご覧ください。](/ja/operation/login-window)

---

## 検査モード。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--inspect-mode` | | 検査モードで起動する。 |
| `--inspect-config <file>` | | 検査モードの設定を指定します。 |
| `--inspect-schema <file>` | | インスペクトモードで使用するスキーマを指定します。 |
| `--schema-validate <file>` | | 設定情報を、定義されたスキーマに基づいて検証する。 |

詳細は、[検査モード](/ja/advanced/inspect-mode)] をご参照ください。

---

## ユーティリティ機能とデバッグ機能。

| 引数 | 短縮形 | 説明 |
|---|---|---|
| `--version` | `-v` | バージョン情報を表示します。 |
| `--help [<argument>]` | | ヘルプを表示します。または、特定の引数に関する詳細なヘルプを表示します。 |
| `--licence` | `-l` | ライセンスを印刷してください。 |
| `--debug [<colour>]` | | オプションでコンテンツの境界線を強調表示しながら、デバッグモードを有効にします。 |
| `--verbose` | `-vvv` | 詳細なログ出力を有効にする。 |
| `--listfonts` | | 利用可能なフォントの名前を出力します。 |
| `--demo` | | デモモードで起動します。 |
| `--builder` | | 構築キットのユーザーインターフェースを起動します。 |
| `--jh` | `-jh` | jamfHelperとの互換性モードを有効にする。 |

詳細は[Builder](/ja/reference/builder)]をご参照ください。
