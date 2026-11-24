---
title: swiftDialog の使い始め
description: swiftDialogのご紹介：これは、macOSの管理者向けの、最新のダイアログ表示ユーティリティです。
translationSynced: 2026-11-23T22:02:01+00:00
---

`dialog -s --title "Welcome to swiftDialog" --message "Hi There.  <br>It's really nice to see you 🙂"`

![swiftDialogのウェルカム画面の例](https://github.com/user-attachments/assets/1a06df20-860f-4c0c-bd14-cdb572604048)

swiftDialogは、macOS管理者の方々がスクリプトを通じて利用できるユーティリティで、ユーザーに対して情報を表示したり、ユーザーが行った操作を記録したりするために使用されます。記録された情報は、後でスクリプト処理に利用したり、単に情報を表示したりする目的で使用できます。

swiftDialogは、コマンドラインから入力を受け付けます。動作時には、表示する内容や表示方法を指示するための、1つ以上のコマンドラインオプションが必要です。[コマンドラインオプション](/ja/advanced/command-line-options)

表示する内容をカスタマイズするための様々なオプションがあり、非常にシンプルな情報表示から、テキスト入力、ドロップダウンリスト、画像表示などを組み合わせたより複雑な処理まで、幅広い選択肢があります。

## swiftDialog を実行する

[releases](https://github.com/swiftDialog/swiftDialog/releases) ページにある **.pkg** インストーラーを使用すると、swiftDialogがインストールされます。インストール先は `/usr/local/bin/dialog` で、macOSのデフォルト設定に含まれているはずの場所です。このパスは通常 `$PATH` に含まれています。

スクリプトからダイアログを呼び出すには、完全なパスを指定するか、`$PATH` を利用することができます。

```bash
$ dialog --title ...
```

または

```bash
$ /usr/local/bin/dialog --title ...
```

最も基本的なレベルで、dialogコマンドは、指定されたメッセージを表示するダイアログを生成するために、`--title` および `--message` のコマンドラインオプションを単純に使用することができます。

swiftDialogは、それ以上の機能も備えていますが、利用可能なオプションの一覧については、[コマンドラインオプション](/ja/advanced/command-line-options)のページを参照するか、dialogコマンドを`--help`オプション付きで実行してください。

## クイックリンク

### 基本的な機能
- [swiftDialogのタイトルをカスタマイズする](/ja/basic-use/title)
- [swiftDialog のメッセージ表示をカスタマイズする](/ja/basic-use/message)
- [swiftDialog のアイコン領域に表示される画像をカスタマイズする](/ja/basic-use/icon)
- [バナー画像を追加する](/ja/advanced/banner-images)
- [ボタンをカスタマイズしボタンの動作を設定する](/ja/basic-use/buttons)

### 高度な機能
- [情報ボックス](/ja/advanced/info-box)
- [バナー画像](/ja/advanced/banner-images)
- [ヘルプメッセージ](/ja/operation/help-message)
- [ドロップダウンメニューとラジオボタン](/ja/advanced/select-lists)
- [Text Entry](/ja/advanced/textfields)
- [チェックボックス](/ja/advanced/checkboxes)
- [タイマーと進捗バー](/ja/advanced/timer-progress)
- [ウィンドウのサイズと動作](/ja/advanced/window-size)
- [フルスクリーン表示モード](/ja/advanced/full-screen)
- [Presentation Mode](/ja/advanced/presentation)
- [項目のリスト](/ja/advanced/item-lists)
- [システム通知](/ja/advanced/notifications)
- [CMD+Qキーの機能を変更する](/ja/operation/command-q)
- [組み込み変数](/ja/operation/builtin-variables)

## サポート

swiftDialogは、SwiftUIを使ったアプリケーション開発の学習の一環として、また、私が好むスタイルでmacユーザーに情報を提供する手段が必要だったことから、部分的に開発が開始されました。

サポートが必要な場合は、[問題として報告してください](https://github.com/swiftDialog/swiftDialog/issues)。機能に関するご要望も歓迎いたします。

## お問い合わせ

著者は、[Macadmins slack](https://www.macadmins.org/slack) の #swiftdialog チャンネル（ユーザー名：@bartreardon - 通常は #anzmac で活動しています）で連絡を取ることができます。ただし、サポートに関するお問い合わせや一般的な質問は、GitHub 上で行ってください。そうすることで、問題が追跡され、対応しやすくなります。ありがとうございます 😃
