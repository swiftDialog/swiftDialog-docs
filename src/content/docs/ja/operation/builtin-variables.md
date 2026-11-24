---
title: 組み込み変数
description: ダイアログでシステム情報を表示する際に、動的な変数を使用する方法。
translationSynced: 2026-11-23T23:31:52+00:00
---

## 組み込み変数。

swiftDialogには、ホストに関する固有の情報が自動的に入力される組み込み変数があります。これらの変数を、テキスト文字列の中に`{variablename}`として含めてください。

含まれる変数は以下の通りです。

    {computername} - コンピュータのホスト名
{computermodel} - コンピュータモデル（例："Mac mini (2023)"）
{serialnumber} - シリアル番号
{username} - 現在のユーザー名（例：`johndoe`）
{userfullname} - フルネーム（例：`John Doe`）
{osversion} - macOSバージョン（例：`14.4.1`）
{osname} - macOS名（例：`Sonoma`）

同様に、環境変数もこの方法でアクセス可能です。

    ダイアログボックスを表示します。アイコンはコンピュータ、タイトルは「{computermodel}」、メッセージは「{osname} {osversion}を実行中」、表示スタイルは中央寄せです。

<img width="350" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/84c41296-8571-4a7b-b9a0-54359465561f">