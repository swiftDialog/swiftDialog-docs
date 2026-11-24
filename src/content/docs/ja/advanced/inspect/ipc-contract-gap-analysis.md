---
title: ICP契約のギャップ分析。
description: swiftDialogとignitecliのIPC（プロセス間通信）契約に関するギャップ分析を行い、現状の課題、潜在的なリスクを特定するとともに、両コンポーネント間の堅牢な通信を確保するための契約条項を提案しました。
translationSynced: 2026-11-23T23:24:18+00:00
---

**Status:** Draft for review **Date:** 2026-06-17 **Scope:** Runtime IPC between `swiftDialog` (Inspect Mode, presets 1–6) and `ignitecli` that launches and drives it. **Repos:**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

この文書では、現在のIPC契約の内容を詳細に記述し、両者が偶然の一致によって合意している点、または保証が規定されているものの執行されていない点を列挙します。すべての主張は、再検証を可能にするために、特定の箇所に紐付けられています。`file:line`

---

## 1. 交通に関する概要

現在、3つのデータ転送システムが稼働中です。この契約は、これら3つのシステムを統合したものであり、堅牢な実装を行うためには、どのシステムも完全に信頼できるとは想定できません。

| 輸送 | 方向 | チャンネル / パス | Payload | 信頼性 |
|---|---|---|---|---|
| 分散型通知（コマンド） | ignitecli → ダイアログ | `com.swiftdialog.command` **そして** `com.ignitecli.command` | `userInfo` dict, stringified | 最善を尽くしますが、順序は保証できません。また、観察者が登録する前に投稿された内容は失われる可能性があります。 |
| 分散型通知（イベント） | dialog → ignitecli | `com.swiftdialog.event` | `userInfo` 辞書（以下、⟨用語⟩を含む）。`event`、`pid` | 最善の努力。 |
| 分散型通知（確認応答）。 | dialog → ignitecli | `com.swiftdialog.ack` | `userInfo` 辞書（以下、`command`、`stepId`、`status`、`pid`を含む）。 | 最善を尽くしますが、**ほとんど使用されることはありません**。 |
| トリガーファイル / コマンドファイル | ignitecli → ダイアログ | `--status-log-file` プロセスID（PID）ごと。`.command` | 改行区切り、コロン区切り。 | 耐久性があり、バイトオフセットで追跡が可能です。 |
| 準備ファイル | dialog → ignitecli | `<trigger>.ready` または 設定 `readinessFile` | JSON | 耐久性があり、存在感のあるデザイン。 |
| イベントファイル | dialog → ignitecli | 設定情報 `eventFile` または、それに基づいて生成された情報 `.events` | JSONL形式。 | 耐久性があり、尾が切除された。 |
| 結果ファイル。 | dialog → ignitecli | 設定 `resultFile` / プロセスIDごとの設定 `.result.json` | JSON | 耐久性がある。 |
| 公開されているセッションのディレクトリ。 | dialog → *(誰もいない)* | `--published-sessions-dir` (デフォルト設定) `/private/tmp/swiftdialog/sessions/<pid>.json` | JSON | 耐久性があり、**消費されません**。詳細は「ギャップ1」を参照してください。 |
| ignitecli の IPC (プロセス間通信) の状態。 | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON | 耐久性がある。 |

**固定アンカー**
- チャンネル：`dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36`。
  ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- 両チャンネルへの投稿： ignitecli `Sources/Commands/IpcCommand.swift:414`.
- コマンドファイルのルーティング：`dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`。
- 公開されているセッションのディレクトリ：`dialog/Command Line/CommandLineArguments.swift:167`。
  `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli の状態: `Sources/Dialog/IpcState.swift:11`.

---

## 2. イベント関連用語（ワイヤー契約）

swiftDialogは、以下のイベントタイプと、関連する生のデータ（locked rawValues）を発生させます。`DistributedNotifications.swift:36`

| イベントの種類 | 生データ | 発生するタイミングは、 | 主要な項目。 |
|---|---|---|---|
| `ready` | `ready` | コマンドに対応したユーザーインターフェース。 | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | 終了しようとしています。 | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | ユーザーによる保留。 | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | ボタンクリック。 | `stepId`, `button`, `action` |
| `step` | `step` | 段階的移行 | `stepId`, `action` (e.g. `completed`, `all_complete`) |
| `selection` | `selection` | ピッカー/グリッド コミット | `key`, `values` |

プリセット6が、`step`、`button`、`selection`（`Preset6.swift:1251`、`:1116`、`:1638`）を放出することが確認されました。

受け入れられるコマンド（ignitecli → ダイアログ）：以下のコマンドが利用可能です。`CommandRouter.swift:76–163`: `success`、`failure`、`warning`、`complete`、`navigate`/`goto`、`next`/`prev`/`back`、`reset`、`progress`、`update_guidance`、`update_message`、`batch_update`、`display_data`、`recheck`、`set`、`item`、`listitem`、`select`。 短縮形の`userInfo`キーは、これらに展開されます（`DistributedNotifications.swift:177`）。

---

## 3. 欠落箇所

重要度順に並べてあります。各項目では、**実際に確認された状況**、**リスク**、そして**提案されている契約条項**（将来的な共通仕様で使用される文言）を示しています。

### 問題点1：公開セッションのディレクトリは書き込み専用であり、ignitecliはそれを読み込むことができません。**重要**

**Observed.** swiftDialog writes a per-PID discovery file to `/private/tmp/swiftdialog/sessions/<pid>.json` (`PresetCommonHelpers.swift:1134`, CLI `CommandLineArguments.swift:167`). A grep of all of ignitecli `Sources/` finds **no reader** for that directory. ignitecli discovers sessions solely via its own `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), which it wrote at launch.

2つの並行するレジストリは、同じ事実（どのトリガーファイルに対してどのダイアログがアクティブであるか）を記述していますが、互いに整合性を保つことはありません。

| レジストリ | swiftDialogが記述します。 | ignitecli コマンドは、以下の内容を読み込みます。 |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | ✅ | ❌ |
| `…/.ignitecli-ipc-<pid>.json` | ❌ | ✅ |

**リスク:** ignitecli は、自身が起動したダイアログにのみ接続できます。 ignitecli が自身の状態ファイルを失った場合（クラッシュ、再起動、別のプロセスからの起動など）、swiftDialog がそのダイアログをアクティブにしている状態でも、その実行中のダイアログは回復できません。 最近リリースされたディスカバリー機能は、現状では社内でのみ利用されており、その価値を十分に発揮できていません。

**提案されている条項。**
> swiftDialogは、各ライブセッションごとに発見記録を公開します。 ignitecliについても、同様の機能を提供します。
> 公開されているセッションディレクトリを、最も信頼できる情報源として扱い、必ず以下の点に留意してください。
> be able to adopt a session found there (read `triggerFile`, `resultFile`,
> `readinessFile`、`ackChannel`、`pid`) を、まだ起動していない状態で。 ignitecli の...
> プライベートな設定ファイルは、起動時のキャッシュとして残る可能性がありますが、それだけが唯一の設定ファイルであってはなりません。
> 真実の源。

**オープンな設定 (所有者: ignitecli)。** セッションディレクトリは、ignitecliの復旧用なのか、それとも外部ツール（監視/MDMなど）用なのか。この選択によって、ignitecliが「発見と導入」の機能を持つようになるか、あるいは意図的に外部との連携を持たない状態になるかが決まります。

### ギャップ2：イベントファイルパスが、2つの異なるルールに基づいて算出されている。**中程度**

**確認済み。** swiftDialogは、イベントパスを`config.eventFile ?? readinessFile(.ready → .events)`として解決します（`Preset5.swift:4834`、`Preset1.swift:460`、`Preset2.swift:533`、およびプリセット6において同じ）。 ignitecliのテンプレートでは、**常に`eventFile`を明示的に設定します**（`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`）。 それらが一致するのは、設定ファイルが常にそのキーを設定しているためです。

**リスク:** カスタムの`readinessFile`を設定し、`eventFile`を省略した設定の場合、swiftDialogが生成するパスが、ignitecliが監視していない`wait-step`と一致しないことがあります。この場合、`wait-step` (`IpcCommand.swift` WaitStep, 2秒間隔でポーリング) が実行された後、タイムアウトが発生し、パスの不一致を示す診断情報が表示されません。

**提案されている条項。**
> イベントファイルのパスは、両者で共通の、厳密に一つのルールに基づいて決定される必要があります。
> もし両端が派生する（明示的な指示を必要とせずに）場合、`eventFile`。
> 導出アルゴリズムは、ここに正確に記述され、テストによって検証されることになります。
> 各側で、タイムアウトが発生した場合、解決されたイベントファイルへのパス情報が必ず含まれること。`wait-step`
> そのエラー。

### Gap 3 - 重要なウェイターは、プロセスの稼働状況を常に確認する必要はない。・**中程度**

**Observed.** `wait-exit` checks `kill(pid, 0)` (`IpcState.swift:58`) and notices a dead dialog. `wait-ready` and `wait-step` wait on a notification or file mutation; `wait-step` only catches a dead PID if its early check happens to fire, otherwise it burns the full timeout (`IpcCommand.swift` WaitStep, `:376`).

**リスク:** プログラムの実行中にエラーが発生し、その時点で処理が中断されると、原因不明の一般的なタイムアウトが発生し、その持続時間は2秒から600秒の間で変動します。

**提案されている条項。**
> すべてのウェイター（`wait-ready`、`wait-step`、`wait-exit`）は、以下の項目についてアンケートに回答する必要があります。`kill(pid,0)`
> ファイルや通知の確認を行う際の処理サイクルと合わせて実行され、問題が発生した場合には、迅速にエラーを検出し、処理を停止します。
> `dialog PID <n> exited before <condition>` 一般的なタイムアウトではなく、より具体的な状況に応じたタイムアウトを設定します。

### ギャップ4：両端にACKチャンネルが存在するものの、バリアとして機能していない。**中程度**

**Observed.** swiftDialog posts to `com.swiftdialog.ack` after every routed command (`CommandRouter.swift:351`). ignitecli has `waitAck()` (`Sources/Dialog/DialogOrchestrator.swift:151`) but most workflows never call it; the default delivery mode is fire-and-forget over a best-effort transport.

**リスク:** `navigate` 通知が途中で途切れると、後続で準備されていたデータの一貫性が失われ、システム全体に影響が及ぶ可能性があります。UIの表示機能は、データの一時的な消失に対してある程度の耐性がありますが、処理順序が重要なコマンドは、そのような問題の影響を受けやすいです。

**提案されている条項。**
> 後続のコマンドに影響を与えるコマンド（`navigate`、`goto`、`reset`、...）。
> `batch_update` navigate コマンドの前に送信されるデータは、確認応答を待機する設定で送信されるものとします。
> `ignitecli` は、特定のコマンドに対して応答（ACK）が一定時間内に受信されない場合、そのコマンドを再度実行するか、エラーメッセージを表示します。
> ACK（確認応答）のタイムアウト時間内に処理を行う必要があります。ただし、멱等性（同じ操作を繰り返しても結果が変わらない性質）を持つ操作については、確認応答なしで実行することも可能です。
> (`progress`, `update_message`, `display_data`).

### Gap 5 - トリガーファイルのリプレイに関する問題が2回修正されました。所有者は特定されていません。**重要度：低～中**

**Observed.** ignitecli deletes IPC files pre-launch (`DialogLauncher.swift:199`) to stop swiftDialog replaying stale `success:` lines (the preset-5 flash-through). swiftDialog independently records the initial byte offset to skip pre-existing content (`CommandRouter.swift:79`). Two independent fixes guard one hazard.

**リスク:** もし、いずれかの処理に問題が発生した場合（例えば、swiftDialog がオフセット 0 から再度読み込みを開始したり、ignitecli が新しいパスでのクリーンアップを省略したりした場合）、このバグが静かに再発する可能性があります。

**提案されている条項。**
> swiftDialogは、投稿する際に、トリガーファイルに存在する以前の内容を無視します。`ready`
> この保証は、swiftDialog側で所有およびテストされます。 ignitecliの...
> 発売前の最終チェックは、あくまで多層的な防御の一環であり、主要な保証ではありません。

### Gap 6 - どの通信経路においても認証が行われていない (許可されているが、明記されていない)。**低リスク**

**確認された内容:** 分散型通知において、送信元の検証が行われていません（APIは関連する機能を提供していません）。コマンドファイルまたはトリガーファイルは、すべてのユーザーが書き込み可能な状態です。セッションディレクトリは、すべてのユーザーが読み取り可能で、ファイル一覧を取得できる状態です。ローカルプロセスであれば、ダイアログを操作したり、偽装したりすることができ、実行中のプロセスID（PID）やトリガーファイルのパスを一覧表示することも可能です。新しいセッションディレクトリの導入は、この脆弱性をさらに拡大する可能性があります。

**リスク:** 同じユーザーによるローカル信頼モデル下では許容範囲ですが、その前提が崩れた場合（共有ホスト環境、または権限の低い共同利用環境など）には危険です。

**提案されている条項。**
> IPC（プロセス間通信）の信頼境界は、「同一ユーザー、同一ホスト、ローカル」です。すべての通信方式は、この信頼境界を前提としています。
> 地元の送付業者との連携。これは意図的な、記録された前提であり、例外はありません。
> データ転送における認証または完全性保護機能を提供します。それ以外の環境での利用はできません。
> この機能は対象範囲外であり、サポートされていません。

---

## 4. 重症度に関する要約と順序付け。

| # | ギャップ | 重症度 | Fix locus |
|---|---|---|---|
| 1 | セッションディレクトリは、書き込み専用です。 | 高。 | ignitecli (読み取り専用) |
| 2 | イベントパスに関する2つのルール。 | 中サイズ。 | 両者共通のルール。 |
| 3 | ウェイターがサービス提供の質を軽視している。 | 中サイズ。 | ignitecli コマンド |
| 4 | 「ACK」は、ここではバリアとして機能しません。 | 中サイズ。 | ignitecli (ポリシー) |
| 5 | リプレイ機能が2回修正されました。 | 低～中程度 | swiftDialog (当社保証) |
| 6 | 認証なし、詳細不明。 | 低い。 | ドキュメントファイルのみ。 |

**推奨される手順:** まず、この契約内容を確定します (5～6の箇所はドキュメントのみで、すぐに完了します)。次に、**1と2の箇所をまとめて**実施します。具体的には、`ignitecli`が公開されているセッションディレクトリを信頼できる情報源として利用し、イベントパスの推論を1つのルールに統合します。これにより、最近の`swiftDialog`のIPC関連の変更を、`ignitecli`が実際に利用できる形にすることができます。3～4の箇所は、`ignitecli`の安定性に関する独立した修正であり、後で実施できます。

---

## 5. 認証ログ

この文書に含まれる記述は、2026年6月17日に参照資料と照合して確認されました。

- "sessions" ディレクトリが ignitecli によって読み込まれていません。 "`Sources/`" の grep コマンドを実行しました。
  `swiftdialog/sessions` / `publishedSessions`: 消費者なし。
- プリセット6は、ステップ、ボタン、または選択肢を出力します。`Preset6.swift:1116,1152,1251,1638`
- イベントパスの二重導出法 — `Preset1.swift:460`、`Preset2.swift:533`。
  `Preset5.swift:4834`; ignitecli コマンドにおける明示的な指定について。`eventFile` の中で、`Sources/Resources/templates/*/config.json` を使用する際の注意点。
- 確認済みとみなされるが、必須ではない。`CommandRouter.swift:351`
  ignitecli `DialogOrchestrator.swift:151`.
- 生気があるのは、`wait-exit` の部分だけ。`IpcState.swift:58`
- ローンチ前のデータクリーンアップと、バイトオフセットによるスキップ処理 — `DialogLauncher.swift:199`。
  `CommandRouter.swift:79`.
