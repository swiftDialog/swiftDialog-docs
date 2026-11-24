---
title: 新機能・変更点
description: swiftDialogの最近の機能とアップデートについて。
translationSynced: 2026-11-23T23:41:37+00:00
---

## swiftDialog バージョン 2.5.6

## 修正点：

 - JSONファイルからアイコンを指定する際に、アイコンが一つでも配列で指定される問題を修正しました。 (issue #493 を修正)
 - バージョン2.5.5において、通知をクリックすると、表示されているダイアログが閉じられます。（#499）
 - @HowardGMac 氏による、ログインしていないユーザーがいる場合に、アップデートダイアログのスクリプトバージョンに関するメッセージを更新する。https://github.com/swiftDialog/swiftDialog/pull/510
 - @MikeRich88 氏による、`scutil` コマンド実行時のパス全体を指定する修正（再投稿）。https://github.com/swiftDialog/swiftDialog/pull/515
 - "helpimage" 画像に、末尾にパディングを追加しました。
 - 通知の送信に必要な認証機能を新たに追加しました。（#485）
 - ヘルプメッセージの`--textfield`に関する、不足しているオプションを修正しました。 #485

## 貢献：

### 通知の取り扱いに関する追加オプション。

 - 通知に識別子を設定する機能を追加しました。これにより、古い通知を新しい通知に簡単に置き換えることができます。また、特定の識別子に基づいて特定の通知を削除したり、すべての通知をまとめて削除したりする機能も追加しました。

例：

```
dialog --notification --identifier "update.message" --title "Updates" --message "Please update by tonight."
dialog --notification --identifier "update.message" --title "Updates" --message "Please update within the next hour."
dialog --notification --identifier "update.message" --remove
```

@chrisgrande さん、ありがとうございます。

### ボタンのサイズを、コマンドライン引数および設定ファイルで指定できるようにしました。

 - ミニ、スモール、およびラージのボタンサイズに対応しており、macOSに組み込まれているサイズを使用します。 ボタンサイズが指定されていない場合、または無効な場合、デフォルトでは通常のサイズが適用されます。
 - ボタンのサイズに関する設定を、テスト用モードやJSONファイル生成機能に追加しました。

ボタンのデザインは、`button1`、`button2`、および情報ボタンに適用されます。また、通常配置のボタンや、縦に並んだボタンのレイアウトにも適用されます。

 ヘルプボタンのサイズは固定されており、拡大・縮小されません。

例：

```
dialog --buttonsize large --commandfile /var/tmp/dialog.txt
echo "buttonsize: mini" >> /var/tmp/dialog.txt   
```

@k2grahamさん、ありがとうございます。

### コマンドファイルから、ダイアログウィンドウの表示/非表示を切り替えるオプションがあります。

 - ウィンドウを非表示および表示するためのコマンド「`hide:`」と「`show:`」を、コマンドファイルで使用可能なコマンド一覧に追加しました。ただし、これはウィンドウが非表示になっている間でも、ウィンドウの内容が更新されることを防ぐものではありません。

@fabienconus 様、ありがとうございます。

