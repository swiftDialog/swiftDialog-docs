---
title: Gotchas
description: swiftDialog に関する一般的な問題と、そのトラブルシューティングのヒント。
translationSynced: 2026-11-23T23:34:58+00:00
---

# コマンドファイルに関する問題。

## 権限が不足しています。

swiftDialogを起動した際に、コマンドファイルが書き込めない場合、エラーメッセージが表示されます。

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

コマンドファイルは削除するか、またはアクセス権を`-rw-rw-rw`（666）に設定してください。

---

# swiftDialog 3.1.1 の動作変更点。

## `--alwaysreturninput` 全ての離脱経路におけるリターン値。

**変更点:** 3.1.1 以降、`--alwaysreturninput` は、ボタン操作だけでなく、**すべての**終了方法において、選択肢、リスト、または JSON 形式の結果を返します。

**影響を受ける終了パス：**
- コマンドファイルによる終了。
- タイマーのタイムアウト。
- 終了キーの押下。
- プロセスを終了しました。

**移行について:** 以前の動作（ボタンが押されたときのみ反応する）に依存しているスクリプトは、新しい動作により出力が異なる場合があります。 `--alwaysreturninput`をご利用の場合は、解析ロジックを見直してください。

## `--ontop` ドックの位置を尊重します。

**変更点：** `--ontop` オプションは、現在、ドックの位置を考慮し、ダイアログを画面の範囲内に表示します（ドックの上に表示されません）。

**影響:** `--ontop` が使用される場合、ダイアログがドックを隠すことはなくなります。これは、以前のバージョンで行われた意図的な変更を元に戻したものです。

## 日付ピッカーのカスタマイズオプション。

変更点：`isdate` モディファイアは、`date` と `time` の採用により、**非推奨**となりました。

**移行:** スクリプトを更新してください。

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# 一般的な注意点。

## 繰り返して使用できるオプションを、最終引数として指定します。

**問題点:** 最終引数として使用される、繰り返し可能なオプション (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`) が、プログラムのクラッシュを引き起こす可能性がある。

**状態:** 3.1.1 で修正済み。

## 日付選択コントロールが値を返さない。

**問題点:** `--textfield ...,isdate` を使用しても何も返ってこなかった。これは、値を返さないように設計された一時的なコード（ダミーコード）だったためです。

**状況:** 3.1.1で修正済み。代わりに`date`または`time`の修飾子を使用してください。

## 画像キャプション機能が正常に動作していません。

**問題点:** コマンドファイル`imagecaption:`が効果を発揮しなかったのは、それが起動時に一度だけ読み込まれる`appvars.imageCaptionArray`にのみ書き込まれており、反応を促すための情報源である`observedData.imageArray`には書き込まれていなかったためです。

**状態:** 3.1.1 で修正済み。

## 「Preset5」グループのヘッダー表示が正しく行われていません。

**問題点:** デプロイメントグループのヘッダー（「完了」「インストール中」など）が、表示位置が誤っているか、または重複して表示される。

**状態:** 3.1.1 で修正済み。

## ボタンバーのキーボード操作が機能していない。

**問題点：** `--hidedefaultkeyboardaction`が、ボタンバーの表示に関する修正作業中に発生した問題により、正常に動作していませんでした。

**状態:** 3.1.1 で修正済み。