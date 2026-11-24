---
title: ログイン画面
description: macOSのログインウィンドウ内で、swiftDialogダイアログを表示させる。
translationSynced: 2026-11-23T23:29:31+00:00
---

## ログイン画面のサポート機能（バージョン2.5.0以降）。

`--loginwindow`

swiftDialog 2.5 では、ログイン画面上でダイアログを表示させることができます。

標準的な対話形式がサポートされており、`--blurscreen`の有無に関わらず利用可能です。

## 要件。

ログイン画面で動作させるためには、以下の設定が必要です。

 - 指定された設定で swiftDialog を起動するスクリプトです。
   - 引数を含めてください。`--loginwindow`
 - ランチャージェント。

### LaunchAgentの設定手順。

#### 手動設定。

以下は、基本的な LaunchAgent の例です。

```xml
<plist version="1.0">
<dict>
	<key>OnDemand</key>
	<false/>
	<key>LaunchOnlyOnce</key>
	<true/>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/script.sh</string>
	</array>
	<key>LimitLoadToSessionType</key>
	<string>LoginWindow</string>
	<key>Label</key>
	<string>com.swiftDialog.example-login-window</string>
</dict>
</plist>
```

適切な名前を付けてください (例: `com.swiftDialog.example-login-window.plist`)。そして、それを `/Library/LaunchAgents/` にインストールしてください。

#### Outsetの使用方法。

Macadminsが提供するオープンソースツールである[Outset](https://github.com/macadmins/outset/)には、ログイン画面で特定の機能を実行する機能が備わっています。

この機能は、操作を簡素化するだけでなく、ユーザーがログイン時に自動的に実行される設定を無効にすることを防ぐための制御機能も提供します。詳細については、[OutsetのWiki](https://github.com/macadmins/outset/wiki/Deployment#login-items-management)]をご覧ください。

スクリプトファイルを、アクセス権が`root:root` `0755` (`-rwxr-xr-x`) に設定された`/usr/local/outset/login-window/`ディレクトリに配置してください。outsetは、ログイン画面が表示された際に、スクリプトの起動を自動的に管理します。

### 考慮事項。

スクリプトが実行された後に何が起こるかを考慮する必要があります。もし、ログイン画面が表示されるたびにこのスクリプトが実行されるのを避けたい場合は、スクリプトに条件を設定し、不要になった場合に何も実行しないか、または自身をアンインストールするようにする必要があります。

### 使用例

#### 組織の利用規約。

以下は、利用規約のダイアログの例です。このダイアログでは、チェックボックスにチェックを入れることを必須とし、マークダウンファイル（例：[AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)]）の内容を表示し、`--eula`モードで表示します。このダイアログは、ログイン画面が表示されるたびに表示されます。

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>