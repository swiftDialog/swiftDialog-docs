---
title: MDM環境における段階的な導入プロセス。
description: 「ゲート付きカデンステップ」という方式を用いて、システムの状態に基づいて動的に変化する属性駆動型の展開画面を作成します。この機能は、Fleet、Jamf、Intuneなどのツールを使用したMDM（モバイルデバイス管理）環境での展開に最適です。
translationSynced: 2026-11-23T23:22:01+00:00
---

「ゲート付きカデンステップ」は、展開画面を「属性駆動型」のシーケンスに変換します。各メッセージは、特定の「現実の条件」が満たされるまで表示され、その後、次のメッセージに進みます。これらの条件は、システムの実際の状態から読み取られるため、画面は実際に完了する前に「完了」と表示することはありません。

これは、特定のMDM（モバイルデバイス管理）ソリューションに依存しません。このツールが読み取る情報—インストールされたアプリケーション、パッケージの受領確認、および**`/Library/Managed Preferences/`**下で管理されるモバイル設定—は、**Fleet、Jamf、Intune、Mosyle、Kandji、Munki、Installomator**などの製品によっても同様に生成されます。以下に示す例では、**Fleet**を具体的な例として使用していますが、これはFleetに特有のものではありません。

## これは、どのような展開戦略に適合するのか。

MDM（モバイルデバイス管理システム）がソフトウェアのインストールやプロファイルの適用などの作業を実行します。swiftDialogは、その作業を監視します。

| 展開タスク。 | テンポ属性 | それがどのように書かれているか。 |
|---|---|---|
| アプリケーションがインストールされました。 | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| パッケージがインストールされました。 | `file` | 領収書を`/var/db/receipts/<pkgid>.bom`にて。 |
| **「Profile」および「mobileconfig」の機能が実装されました。** | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (機器) または `…/<user>/<domain>.plist` |
| スクリプトによる設定。 | `file` | スクリプトが参照するマーカーファイル。 |
| 非観察可能な確認項目。 | `source:"ipc"` | MDMスクリプトは、以下のものを呼び出します：`cadence:satisfy:<id>` (osquery、Installomatorのログ、MDM API)。 |

**Hybrid drive:** most entries poll natively (no orchestrator, works offline / at the login window); a few `source:"ipc"` entries are advanced by an MDM script for things that can't be observed directly. The IPC verb is `cadence:satisfy:<id>` (also `advance` / `goto`).

`timeout` システムは、タスクが完了しない場合に、自動的に次の処理に進むため、ポリシーが失敗した場合でも、ユーザーインターフェースが停止することはありません。

## 二つの段階。

ログイン画面/セットアップアシスタントの段階では、**ユーザーセッションが存在しません**（ユーザーアプリケーションはなく、デバイスレベルでの設定のみ）。そのため、ランチャーによってセッションごとに選択される2つの設定ファイルを使用します。

### フェーズA：ログイン画面 / セットアップウィザード（デバイスレベルのみ）
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### フェーズB：ログイン後のデスクトップ環境（すべての信号が有効）
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
The `compliance` entry is `source:"ipc"`: an MDM script runs the check (osquery / vendor API) and then `… ipc send "cadence:satisfy:compliance"`.

## （Fleet社の例：どのMDMでも同じ形状です。）
1. **パッケージ内容:** swiftDialog、ランチャー、および両方のCadence JSONファイル。
2. **プロファイル (mobileconfig):** ランチャーの設定。各セッション、ログイン画面に関する設定項目。
   (ランチャーも同様に、自身が管理する設定情報を同じ方法で読み込みます — `/Library/Managed Preferences/` の下で。)
3. **LaunchAgents** (デバイス + ログインウィンドウ) を使用して、swiftDialog を適切なセッションで起動します。
4. **GitOps / ポリシー**: Cadence が管理するプロファイルとソフトウェア、および関連する小さなスクリプト。
   あらゆる項目に対して、エラーメッセージを生成します。`cadence:satisfy` `source:"ipc"`

`contour`/`fleet-gitops`のツールを使用して、モバイル設定ファイル（mobileconfig）とGitOps関連の成果物を作成します。このツールは、作成された設定ファイルがAppleのスキーマに準拠しているか検証します。

## テナントごとにカスタマイズされたブランド表示と、管理された設定に基づく情報提供。

マルチテナント環境での展開において、表示されるメッセージやブランドカラーなどの情報は、あらかじめ設定されたプロファイルから読み込むことができ、ハードコーディングされることはありません。これにより、各テナントのMDMプロファイルが独自の値を設定し、出荷時の設定を変更することなくカスタマイズが可能です。これらは両方とも、`ManagedValueRef`を使用します。

| キー。 | 種類。 | 説明 |
|---|---|---|
| `domain` | 文字列。 | 優先度管理領域、例：`nl.root3.support` |
| `key` | 文字列。 | その領域（色の明るさの値）における重要な要素。 |
| `darkKey` | 文字列。 | オプションで、ダークモード表示用のキー（色のみ）を設定できます。 |

- `cadenceRef` — reads the cadence claims array (the `CadenceEntry` dicts) from a managed preference, instead of an inline `cadence` array.
- `brandColorRef` — 管理された設定から、ブランド名やカラー（明るい色、オプションで濃い色も指定可能）を取得します。

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

値が`/Library/Managed Preferences/<domain>.plist`から算出されるため、上記の`managedpref`属性と同様に、「プロファイルが読み込まれた瞬間に値が更新される」という動作に従います。

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## 注釈
- `managedpref` はファイルを直接読み込むため、プロファイルが適用されるとすぐに処理が開始されます (遅延はありませ
  CFPreferences キャッシュの遅延に関する情報。`evaluation:"exists"` は「プロファイルが存在する」ことを示し、`equals`/`boolean` は「特定の値を強制的に適用している」ことを示します。
- ログイン画面の段階では、デバイスの範囲でのみ設定が有効であり、ユーザーごとの設定や確認は行われません。`app`
  これはフェーズBに該当します。
- リズムの終わりまで再生し（または、最初に戻って）、**高速リプレイ**を行い、その後停止します。`cadenceMinDwell`
  再利用したり、吊るしたりしないでください。
