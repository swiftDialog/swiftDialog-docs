---
title: 通知
description: swiftDialogを使用して、ダイアログウィンドウを表示する代わりに、システム通知を送信します。
translationSynced: 2026-11-23T23:03:31+00:00
---

## 通知

swiftDialogでは、`--notification`という引数を使用することで、通知を送信できます。これは、swiftDialogがダイアログウィンドウを表示する代わりに、通知を送信するように指示するものです。

通知は、テキストやメディアを表示するために、同じ`--title`、`--message`および`--icon`の引数を使用します。このページに記載されていないその他の引数は無視されます。

通知にサブタイトルを追加するオプションが用意されています。`--subtitle`

### 通知の表示形式 (バージョン3.1以降)

v3.1から、swiftDialogは`Dialog.app`に組み込まれた専用のヘルパーアプリケーションを通じて通知をルーティングします。`--style`引数を使用して通知タイプを選択してください：

| `--style` 値 | 行動 | 使用されたヘルパー。 |
|---|---|---|
| `banner` | 一時的に表示され、その後自動的に消えるシステム通知。 | `Dialog Banner` |
| `alert` | ユーザーがそれを閉じるまで表示され続けるシステム通知。 | `Dialog Alert` |
| `pseudo` | 擬似的な通知バナー（`pseudo-banner`と同じ）。 | メインアプリ。 |
| `pseudo-banner` | 自動的に一定時間経過後に消える、擬似的な通知。 | メインアプリ。 |
| `pseudo-alert` | ユーザーの操作が行われるまで表示される、擬似的な通知。 | メインアプリ。 |

省略された場合のデフォルト値は、アプリケーションに設定されているシステム通知の設定によって異なります。`--style`

> #### 従来のパス（バージョン3.1で非推奨となりました）
>
> --notificationを`--style`なしで呼び出しても、下位互換性のためまだ動作しますが、メインの`Dialog.app`バンドルを経由します。このパスは非推奨であり、stderrに警告を出力します：
> 今後のリリースでは、`--style`なしで通知を送信すると、`--style banner`がデフォルトになります。

システム通知のスタイルが正しく設定されるように、関連するヘルパーアプリ（`au.csiro.dialog.notifier.banner` および `au.csiro.dialog.notifier.alert`）に対して、希望する通知スタイルで事前に承認された設定ファイル（mobileconfig）を導入してください。

### 使用する。

基本的なバナー通知の送信：

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

継続的なアラート通知の送信：

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![image](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

メッセージが通知で表示できる文字数を超える場合、メッセージは省略され、省略記号（…）が表示されます`...`。また、ユーザーが通知の上にマウスカーソルを合わせると、通知の右上に展開ボタン（▼）が表示され、ユーザーはそれをクリックして内容を詳しく表示することができます。

![スクリーンショット 2022年11月13日 午後5時26分](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![スクリーンショット 2022年11月13日 午後5時26分15秒](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

字幕を追加する：

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![image](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

通知には、タイトルとサブタイトルを含めて、最大5行のテキストを表示できます。メッセージ本文に含まれる`\n`という文字は、通知内に改行を挿入します。

画像は、`--icon` を使用して追加でき、既存のすべての画像形式とソースに対応しています。

![image](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

画像を表示する際、ユーザーは通知の内容を詳細表示させることができます。

![image](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

_注意: 通知に表示されるデフォルトのアイコンは、変更できません。`--icon`を使って追加する画像は、通知内に表示されます。_

## アクションの設定

ユーザーが通知をクリックした際に実行されるアクションを設定できます。これは、URLであったり、シェルコマンドであったりする場合があります。

注意：通知はユーザー主導で行われ、したがって、通知によって実行される操作は、ユーザーの状況下で行われます。

この機能の基本的な使い方は以下の通りです。

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

追加のアクションを指定したり、ボタンのラベルを定義したりすることができます。

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` は、通知本文またはボタン1がクリックされた場合に実行されるデフォルトのアクションです。 `--button2action` は、ボタン2がクリックされた場合にのみ実行されます。

## 通知の識別子と削除方法について。

通知に、`--identifier` を使用して永続的な識別子を割り当てることができます。これにより、後で特定の通知を削除することが可能になります。

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

呼び出しコマンドにオプションパラメータを省略すると、そのヘルパーに関連するすべての未通知の状態がクリアされます。`--remove` `--identifier`

識別子は、擬似通知（詳細は後述）にも対応しています。

## 通知音の設定を有効にする。

通知が送信される際に、デフォルトの通知音を再生するには、`--enablenotificationsounds`を使用します。

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## 疑似通知

「疑似通知」とは、macOSのシステム通知ではなく、swiftDialog自体が生成する、通知のようなウィンドウのことです。画面の右端からスライドして表示され、半透明の背景素材を使用することで、ネイティブの通知と似た外観をしています。

### 擬似通知を使用する理由は何ですか？

- **カスタムアイコンのサポート** - 通知に表示されるアイコンは、`--icon`を使用することで、完全にカスタマイズ可能です。SF Symbols、URL、ファイルパス、アプリケーションバンドルなどが利用できます。システム通知とは異なり、Dialog.appのバンドルアイコンを設定したり、NotificationCenterを再起動したりする必要はありません。
- **MDMプロファイルは不要です** - この疑似通知はmacOSの通知センターを経由しないため、モバイル設定ファイル（mobileconfig）や通知権限の設定は必要ありません。
- **インライン画像** - `--image` を使用して、通知本文内に画像を挿入します。
- **インラインマークダウン** — `--message` このコンテンツは、インラインマークダウン形式をサポートしています。

### 「疑似通知」とは、具体的にどのようなものではないのでしょうか？

疑似通知は、システム通知とは異なります。一度閉じると消え去り、macOSの標準的なシステム通知のルールに従いません。また、積み重なることもありません。複数の疑似通知を送信できますが、それらは重ねて表示されます。もしこれが重要である場合は、通常のシステム通知を使用してください。



### 疑似通知スタイル。

| `--style` 値 | 行動 |
|---|---|
| `pseudo` | 同じく`pseudo-banner` |
| `pseudo-banner` | 6秒後（または`--timer`の値）で自動的に非表示になります。 |
| `pseudo-alert` | 画面上に表示されたままになり、ユーザーがクリックするか、ウィンドウを閉じるまで表示され続けます。 |

### 基本的な使い方。

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### カスタムアイコンと画像。

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### アクションボタン。

`--button2text`または`--button2action`が指定された場合、通知の下部にアクションバーが表示され、そのアクションバーには2つのボタンがあります。

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- 通知本文または**ボタン1**をクリックすると、`--button1action`が実行されます。
- 「ボタン2」をクリックすると、`--button2action`が実行されます。
- もし、`--button2text` も `--button2action` も指定されていない場合、アクションバーは非表示になり、通知領域のどこをクリックしても、`--button1action` が実行されます。

### 自動消去タイマー。

`pseudo-banner` スタイルの場合、通知はデフォルトで6秒後に自動的に消えます。カスタムの表示時間を秒単位で設定するには、`--timer` を使用してください。

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### 閉じるボタン

<img width="400" alt="image" src="/images/restart-hover-button.png" />

ユーザーが擬似的な通知にマウスカーソルを合わせた場合、左上隅に閉じるボタン（×）が表示されます。このボタンをクリックすると、通知が非表示になり、タイムアウトした場合と同じ動作（画面から消え、終了コード0で終了、ボタン操作は実行されません）となります。

### ライブタイムスタンプ。

疑似通知には、タイトル横に「現在」というタイムスタンプが表示されます。60秒後には「1分前」と表示に変わり、通知が表示されている間、60秒ごとに更新されます。

### 識別子と削除について。

疑似通知機能は、特定の対象者に対する通知の配信停止をサポートします。`--identifier`

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

既存の通知と同じ識別子を持つ新しい擬似通知を送信する場合、新しい通知が表示される前に、古い通知が自動的に削除されます。

### 通知音

偽の通知が表示された際に、システムのアラート音を再生するには、`--enablenotificationsounds`を使用します。

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## MDM（モバイルデバイス管理）を通じて、通知の種類を承認し、設定する方法。

初めて通知機能を使用する際、フィードバックが全く得られない場合や、通知の許可を求めるメッセージが表示されない場合があります。

通知を手動で許可するには、システム設定 -> 通知 にアクセスし、該当するアプリケーションの通知を有効にしてください。また、通知の表示方法を「なし」、「バナー表示」、「アラート表示」のいずれかから選択できます。

swiftDialogをMDM経由で展開する際には、通知の事前承認を設定し、通知の種類を指定するモバイル設定ファイル（.mobileconfig）をあらかじめ配布することが推奨されます。

### バンドル識別子

| バージョン。 | バンドル識別子 | 注釈 |
|---|---|---|
| バージョン2.2.1以前のバージョン。 | `au.bartreardon.dialog` | 遺産 |
| v2.3 – v3.0 | `au.csiro.dialog` | メインアプリバンドル。 |
| v3.1以降 (バナー形式) | `au.csiro.dialog.notifier.banner` | `Dialog Banner` 手伝い役、補助者 |
| バージョン3.1以降（アラート表示形式） | `au.csiro.dialog.notifier.alert` | `Dialog Alert` 手伝い役、補助者 |

> インストールされたビルドの正確なバンドルIDを確認するには、以下のコマンドを実行してください。
> ```
> `defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist" CFBundleIdentifier` コマンドを実行します。このコマンドは、指定されたファイル（Info.plist）から、CFBundleIdentifier というキーに対応する値を読み取ります。
> `defaults read "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" CFBundleIdentifier` コマンドを実行すると、指定されたファイル（`/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist`）から `CFBundleIdentifier` というキーに対応する値が読み込まれます。この値は、アプリケーションの識別子を表しています。
> ```

もし複合的な構成になっている場合、同じプロファイルに複数のバンドルエントリーを含めることができます。例えば、バナー形式の通知に関する設定は、以下のような内容になる可能性があります。

```xml
<key>PayloadContent</key>
<array>
    <dict>
        <key>PayloadDisplayName</key>
        <string>Notifications Payload</string>
        <key>PayloadIdentifier</key>
        <string>449B1259-E631-4051-ADCE-9532B813ADDC</string>
        <key>PayloadOrganization</key>
        <string>Org Name</string>
        <key>PayloadType</key>
        <string>com.apple.notificationsettings</string>
        <key>PayloadUUID</key>
        <string>12EA8FDA-B204-4AD0-802C-C980615F0BA5</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>NotificationSettings</key>
        <array>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.bartreardon.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>1</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.banner</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
            <dict>
                <key>AlertType</key>
                <integer>2</integer>
                <key>BadgesEnabled</key>
                <true/>
                <key>BundleIdentifier</key>
                <string>au.csiro.dialog.notifier.alert</string>
                <key>CriticalAlertEnabled</key>
                <false/>
                <key>NotificationsEnabled</key>
                <true/>
                <key>ShowInLockScreen</key>
                <true/>
                <key>ShowInNotificationCenter</key>
                <true/>
                <key>SoundsEnabled</key>
                <true/>
            </dict>
        </array>
    </dict>
</array>
```

注意点として、`AlertType` キーは、`--style` とは独立して、通知の表示形式を制御します。
- `1` = バナー (自動的に非表示になります)
- `2` = 警告 (解除されるまで表示され続けます)

`--style alert`を使用して展開する場合、設定ファイル内の`au.csiro.dialog.notifier.alert`という項目で、広告の場合は`AlertType`を`2`に設定し、その逆も同様です。

 > #### 通知に関するエラーについて
 >
 > もし、以下のものを受け取った場合：
 >
 > ```
 > 通知が表示できません：補助アプリケーションとの通信に失敗しました。
 > ```
 >
 > システム設定で、関連するDialogアプリケーションに通知機能が有効になっていることを確認してください。確認方法は、上記のモバイル設定ファイル（.mobileconfig）をMDM（モバイルデバイス管理）を通じて適用するか、またはシステム設定を手動で確認する方法があります。

## デフォルトの通知アイコンを更新する。

通知には、標準の swiftDialog アイコンが使用されます。もし、企業ロゴなど、別のアイコンを使用したい場合は、以下の手順でアプリのアイコンを、より適切なものに変更することができます。

> #### macOS 26.4 以降のバージョンをサポートします。
>
> macOS 26.4 以降のバージョンでは、アプリケーションバンドルのアイコン、およびそれに伴う通知アイコンが正常に更新されなくなりました。ブランドイメージが重要な場合は、新しい疑似通知機能をご利用ください。この機能は、システム通知と似たようなUIを提供しますが、macOSのシステム通知機能を使用していないため、すべての状況に適しているとは限りません。

### 前提条件

 - 最新の swiftDialog パッケージ。
 - 適切な代替画像をご用意ください。解像度は少なくとも512x512ピクセル（推奨は1024x1024ピクセル）。

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### 画像の生成

   `sips`コマンドを使用すると、MDMベンダーが提供するセルフサービスアプリケーションから画像を生成できます。例えば：

    ##### カンジ

    ```bash
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sips -s format png /Applications/Kandji\ Self\ Service.app/Contents/Resources/AppIcon.icns --out /Library/Application\ Support/Dialog/Dialog.png
    ```

    ##### Jamf

    ```bash
    temp_file=$(/usr/bin/mktemp)
    /usr/bin/xxd -p -s 260 "$(defaults read /Library/Preferences/com.jamfsoftware.jamf self_service_app_path)"/Icon$'\r'/..namedfork/rsrc | /usr/bin/xxd -r -p > "$temp_file"
    sudo /bin/mkdir -p /Library/Application\ Support/Dialog
    sudo /usr/bin/sips -s format png "$temp_file" --out /Library/Application\ Support/Dialog/Dialog.png
    ```

### 手順

  1. 置き換えたいアイコン画像のファイルを、以下の場所にコピーしてください。`/Library/Application Support/Dialog/Dialog.png` (大文字と小文字を区別します)
  2. swiftDialogを、提供されているインストーラーからインストールしてください。`.pkg`

インストールが完了すると、インストーラーはシステムに組み込まれているアイコンを、指定された画像に置き換えます。その後、通知機能は、このカスタム画像を通知アイコンとして使用します。`Dialog.png`

 申し訳ありませんが、画像が表示されていません。画像の内容を説明していただければ、翻訳することができます。](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
