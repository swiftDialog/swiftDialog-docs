---
title: インストール
description: macOS で swiftDialog をインストールする方法。
translationSynced: 2026-11-23T22:31:47+00:00
---

## 設置方法

### パッケージインストーラー（推奨）

swiftDialogをインストールする最も簡単な方法は、[リリースページ](https://github.com/swiftDialog/swiftDialog/releases)から提供されている**.pkg**インストーラーを使用することです。

インストーラーは swiftDialog を `/usr/local/bin/dialog` に配置します。このパスは通常、macOS のデフォルトの `$PATH` に含まれています。

### 手動でのインストール。

もし手動でのインストールをご希望の場合は：

1. 最新版を[リリースページ](https://github.com/swiftDialog/swiftDialog/releases)からダウンロードしてください。
2. バイナリデータを抽出する。
3. それを`/usr/local/bin/dialog`、または`$PATH`内の別の場所にコピーしてください。
4. 実行権限が設定されていることを確認してください。`chmod +x /usr/local/bin/dialog`

### ホームブリューでのインストール方法。

近日公開予定 - 自作ソフトウェアのレシピ（フォーミュラ）を開発中です。

## 動作確認

インストール後、swiftDialog が正常に動作しているか確認してください。

```bash
dialog --version
```

簡単なダイアログを使って試してみることもできます。

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## swiftDialogのアップデート。

swiftDialogをアップデートするには、最新版をダウンロードしてインストールするだけです。インストーラーが、既存のバージョンを置き換えます。

プログラム的にアップデートを確認するには、以下の方法を使用できます。

```bash
dialog --checkupdates
```

## アンインストール (プログラムの削除)

swiftDialogを削除するには：

```bash
sudo rm /usr/local/bin/dialog
```

## MDM（モバイルデバイス管理）による展開。

swiftDialogは、Jamf Pro、Mosyle、またはIruといったモバイルデバイス管理（MDM）ソリューションを通じて展開できます。 簡単に言うと、.pkgインストーラーを管理対象のデバイスにインストールするだけです。

### Jamf ポリシーの例。

1. swiftDialogの.pkgファイルをJamf Proにアップロードしてください。
2. パッケージの展開に関するポリシーを作成してください。
3. ご希望のデバイスに合わせて調整できます。
4. トリガー設定 (チェックイン、定期実行、セルフサービスなど)。