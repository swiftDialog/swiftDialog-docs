---
title: デモスクリプト
description: アプリケーションの選択とインストールに関する完全なデモンストレーションスクリプト。
translationSynced: 2026-11-23T23:35:47+00:00
---

詳細なデモ版は、以下のサイトでご確認いただけます。https://github.com/swiftDialog/demo

## swiftDialog 総合デモスイート。

[swiftDialog⟧の主要な機能を、インタラクティブな形式で、ユーザー自身が操作しながら学べるようにするための、zshスクリプトの集です。](https://github.com/swiftDialog/swiftDialog)

## 要件。

- macOS 15 以降のバージョン。
- [**swiftDialog 3 以降のバージョン**](https://github.com/swiftDialog/swiftDialog/releases)

## クイックスタート

```zsh
# clone this repo
git clone https://github.com/swiftDialog/demo.git swiftDialog-demo

# or download the zip
curl -sL "https://github.com/swiftDialog/demo/archive/refs/heads/main.zip" -o swiftDialog-demo.zip && unzip swiftDialog-demo.zip -d swiftDialog-demo

cd swiftDialog-demo
./run_demos.zsh
```

メインコントローラーでは、swiftDialog自体が使用されています。チェックボックスを使用したデモを選び、一つずつ試してみてください。

## swiftDialog 作成のためのAIスキル。

**swiftDialogを初めてお使いの方へ:** まずは、公式の[swiftDialog Builderページ](https://swiftdialog.app/builder/builder/)]から始めて、操作方法の理解と視覚的なプロトタイピングを行ってください。その後、リポジトリに含まれるスキルパックのいずれかを利用して、その理解をリポジトリ形式のシェルスクリプトに変換することができます。Builderは便利ですが、全てを網羅しているわけではなく、最終的なサイズ調整、調整作業、ワークフローの決定といった重要な要素を代替するものではありません。

### 利用可能なスキル。

**[`codex-swiftdialog-builder`](skills/codex-swiftdialog-builder/)** - GitHub Copilot / OpenAI Codex 用

- [`SKILL.md`](skills/codex-swiftdialog-builder/SKILL.md) — Codexのワークフローとランク選択について]
- [`references/`](skills/codex-swiftdialog-builder/references/) — デモの構成と作成に関するガイダンス]
- [`assets/templates/`](skills/codex-swiftdialog-builder/assets/templates/) — 初心者向けのシェルスクリプトのサンプル]
- Jamf/root権限での実行に加え、所有権の引き継ぎパターンをサポートしており、コマンドファイルを使用したワークフローを効率的に実行できます。`/var/tmp` `root`

**[`claude-swiftdialog-builder`](skills/claude-swiftdialog-builder/)** - クロード・ソネット様へ

- [`CLAUDE.md`](skills/claude-swiftdialog-builder/CLAUDE.md) — Claudeのワークフローとプランの選択]
- [`references/`](skills/claude-swiftdialog-builder/references/) — デモの構成と作成に関するガイダンス]
- [`templates/`](skills/claude-swiftdialog-builder/templates/) — 初心者向けのシェルスクリプトのサンプル]
- Jamf/root権限での実行に加え、所有権の引き継ぎパターンをサポートしており、コマンドファイルを使用したワークフローを効率的に実行できます。`/var/tmp` `root`

両方の機能は同じリポジトリの規約に従い、同じスクリプト出力を生成します。ご自身のAIプラットフォームに合った方を選択してください。詳細な使用方法については、[`skills/README.md`](skills/README.md) を参照してください。

これらは、AIアシスタント向けの機能セットであり、このソフトウェアスイートに含まれる実行可能なデモではありません。

## AIを活用した開発環境。

デモ環境を試用し、swiftDialogの機能を理解した後は、[`playground/`](playground/)] ディレクトリを使用して、AIのサポートを受けながら独自のスクリプトを作成できます。 この環境には、以下の手順を詳しく解説した包括的なガイドが含まれています。

- 同梱されている機能を使用して、AIアシスタント（Claude、Copilotなど）と連携して作業を行います。
- ワークフローに最適なレベルを選択してください。（基本的なダイアログ → フォーム → 進行状況の更新 → インスペクションモード）
- 具体的な実例に基づいたシナリオを通じて、詳細な指示と、そこで期待されるAIとのやり取りを体験できます。
- Macの管理者向けタスク（初期設定、コンプライアンス、展開、監視、破壊的な操作の確認など）を実行するための、本番環境で使用できるスクリプトを作成します。

**ここから始めましょう:** [`playground/README.md`](playground/README.md)] - AIを活用したswiftDialogスクリプト開発のための作業スペースです。

## デモインデックス。

- `01_basic_styles.zsh` - `--style` (注意、警告、中心)、スタイル設定の優先順位。
- `02_title_message.zsh` - `--title`、`--titlefont`、`--message`、`--messagefont`、`--messagealignment`、`--messageposition`、`--bannertitle`、タイトル: 「なし」
- `03_icons.zsh` - `--icon` (SF Symbols、アプリケーション、標準機能、QRコード、パレット、自動カラー調整、ウェイト)、`--iconsize`、`--iconalpha`、`--centreicon`、`--overlayicon`、`--hideicon`
- `04_buttons.zsh` - `--button1text`、`--button1symbol`、`--button1disabled`、`--button2text`、`--button2symbol`、`--infobuttontext`、`--infobuttonsymbol`、`--infobuttonaction`、`--buttonstyle` (中央、スタック)、`--buttonsize`、`--buttontextsize`、`--hidedefaultkeyboardaction`
- `05_images_banners.zsh` — `--image`, `--imagecaption`, `--bannerimage`, `--bannertitle`, `--bannertext`, `--background`, `--bgalpha`, `--bgposition`, `--bgfill`
- `06_progress_timer.zsh` - `--progress` (絶対値、増分、リセット、完了)、`--progresstext`、`--progresstextalignment`、`--timer`、`--hidetimerbar`、コマンドファイル処理状況の更新。
- `07_text_fields.zsh` - `--textfield` (必須、安全、迅速、価値、正規表現、正規表現エラー、確認、ファイル選択、ファイルタイプ、パス、名前), `--textfieldlivevalidation`
- `08_dropdowns.zsh`：—、`--selecttitle`、`--selectvalues`、`--selectdefault`、修飾子（必須項目、ラジオボタン、検索可能、複数選択可、名前）、区切り文字。
- `09_checkboxes.zsh` — `--checkbox` (名前の修飾子), `--checkboxstyle` (チェックボックス、スイッチ、サイズ)
- `10_list_items.zsh` - `--listitem` (ステータス、ステータステキスト、カスタムSFシンボル)、`--liststyle`、`--enablelistselect`、コマンドファイル（リスト:、リストアイテム:、追加、削除、インデックス）
- `11_window_options.zsh` — `--width`, `--height`, `--big`, `--small`, `--position`, `--positionoffset`, `--moveable`, `--ontop`, `--resizable`, `--windowbuttons`, `--appearance`, `--showdockicon`, `--dockiconbadge`
- `12_command_file.zsh` — コマンドファイル全体の構成： タイトル（title:）、タイトルフォント（titlefont:）、メッセージ（message:、追記可能）、配置（alignment:）、アイコン（icon:）、オーバーレイアイコン（overlayicon:）、アイコンの透明度（iconalpha:）、ボタン1のテキスト（button1text:）、ボタン1（button1:）、情報テキスト（infotext:）、情報ボックス（infobox:）、アイコンの配置（icon: center/left）。
- `13_notifications.zsh` — `--notification`, `--subtitle`, `--identifier`, `--remove`
- `14_mini_presentation.zsh` — `--mini` (進捗状況付き), `--presentation` (リスト項目、インフォボックス、進捗状況付き)
- `15_web_video.zsh` - `--webcontent`、`--video` (youtubeのショート動画)、`--videocaption`、`--autoplay`
- `16_json_input.zsh` チェックボックス、選択肢、テキストフィールド、画像などを表現するための、JSON形式の配列データ。`--jsonstring` および `--jsonfile` は、それぞれのデータ構造に関する詳細情報を示します。
- `17_fullscreen_blur.zsh` — `--fullscreen`, `--blurscreen`, `--hideotherapps`
- `18_misc_features.zsh` - `--helpmessage`、`--infotext`、`--infobox`、`--vieworder`、`--quitkey`、`--sound`、`--showsoundcontrols`、`--displaylog`、`--loghistory`、`--debug`、`--eula`、`--alwaysreturninput`、認証キー/チェックサムの説明
- `19_inspect_mode.zsh` - `--inspect-mode`、`--inspect-config`、`--published-sessions-dir`、`stepType: "cadence"`、`cadenceStyle: "carousel"`、cadence IPC (`cadence:satisfy`、`cadence:advance`、`cadence:goto`)、プリセット3のデザイン変更、フッターのロゴ、強制的な`appearance`、`cacheExtensions` (※`aria2`)。
- `20_branched_workflows.zsh` トップレベルの `workflow` 配列、`branch.map`、`branch.default`、`branch.ifTrue`、`branch.ifFalse`、`nextpage`、`finalpage`、履歴を考慮した。 以前の。

## 個別のデモの実行方法。

各デモスクリプトは、それぞれ独立した内容で構成されています。

```zsh
./demos/06_progress_timer.zsh
./demos/12_command_file.zsh
```

## 注釈

- `--blurscreen`または`--fullscreen`を使用するデモでは、一時的に画面表示が変更されます。
- 通知機能を利用するデモでは、swiftDialogを使用するために、通知の許可設定が必要です。
- 一部の画像デモでは、macOSのバージョンによって異なるシステムデスクトップの画像が使用されている場合があります。
- 今回のデモ19では、v3.1.0b4の機能改善に焦点を当てており、具体的には、カデンステーブルの表示改善、プリセット3のコンパクトなデザイン変更、セッションの公開機能、および、関連する設定情報サンプルJSONファイルについて紹介します。
- デモ版19および20では、タイミング調整機能や分岐型ワークフローのサポートに必要なため、**swiftDialog バージョン3.1.0b4以降**のバージョンをご利用ください。
- 詳細は、[swiftDialog v3.1.0b4]のリリースノート](https://github.com/swiftDialog/swiftDialog/releases/tag/v3.1.0b4)をご確認ください。