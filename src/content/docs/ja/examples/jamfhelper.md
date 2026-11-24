---
title: jamfHelper サポートサービス。
description: swiftDialogをjamfHelperの代替として、容易に導入・利用することができます。
translationSynced: 2026-11-23T23:39:23+00:00
---

Dialogには、新しい`--jh`フラグによって、jamfHelper形式の基本的なコマンドラインオプションを受け入れる機能が追加されました。

これにより、既存のワークフローやスクリプトに組み込むことが容易になります。なぜなら、`/Library/Application\ Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper`への呼び出しを`/usr/local/bin/dialog --jh`に置き換えるだけで済むからです。

このフラグを使用すると、ダイアログが `jamfHelper` のオプションを、同等のダイアログのオプションに変換されます。すべてのオプションがサポートされているわけではありません。 `jamfHelper` に同等の機能がない標準的なダイアログのオプションは引き続き利用可能です。例えば、`--width`、`--height`、および `--image` などです。

<br/>

## 機能と動作について。

***
### 実装済み。

#### `-windowType [hud | utility | fs]`

`hud` と `utility` は無視されます。`fs` はダイアログ `--fullscreen` に変換され、ダイアログ画面全体に表示されます。

#### `-windowPosition [ul | ll | ur | lr]`

ウィンドウの位置は、ユーザーの画面の右上、左上、右下、または左下のいずれかに設定できます。これは、現在の標準設定には含まれていない機能ですが、jamfHelperとの互換性のために実装されています。

#### `-title "string"`
変換されました。`--title`

ウィンドウのタイトルを、指定された文字列に設定します。

#### `-heading "string"` と `-description "string"`
変換されました。`--message`

`-heading`と`-description`は、どちらもダイアログの`--message`オプションにマージされます。`-heading`はマークダウンの見出し4`####`に変換され、その後に空行と`-description`が続きます。

#### `-icon path`
変換されました。`--icon`

もし指定されていない場合、ダイアログの表示オプションを、`jamfHelpers` の動作に合わせて、ID が指定されていない場合に ID を表示しないようにします。`--hideicon`

#### `-button1 "string"`
変換されました。`--button1text`

**_変更点:_** ダイアログボックスでは、常にデフォルトボタンが表示されます。これは、jamfHelperの動作とは異なります。デフォルトボタンのテキストは`OK`です。

#### `-button2 "string"`
変換されました。`--button2text`

#### `-alignDescription [right | left | center | justified | natural]`
変換されました。`--alignment`

実装されている選択肢は、`right`、`centre`、および`left`のみです。

#### `-timeout int` と `-countdown`
変換されました。`--timer`

`-countdown` は常に暗黙的に設定されており、ダイアログには常にタイマーバーが表示されます。もしタイマーバーを表示しないようにしたい場合、ダイアログ内にタイマーバーの実装がされていないため、実現できません。

<br/>

***
### 未実装。

#### `-defaultButton [1 | 2]`
デフォルトのボタンは常にボタン1です。

#### `-cancelButton [1 | 2]`
キャンセルボタンは常にボタン2です（表示されている場合）。

#### `-showDelayOptions "int, int, int,..."`

#### `-alignHeading [right | left | center | justified | natural]`

#### `-alignCountdown [right | left | center | justified | natural]`

#### `-iconSize pixels`

#### `-lockHUD`

#### `-fullScreenIcon`