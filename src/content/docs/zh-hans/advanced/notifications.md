---
title: 通知
description: 使用 swiftDialog 发送系统通知，而不是显示对话框
translationSynced: 2026-11-25T05:32:38+00:00
---

## 通知

swiftDialog 允许您通过使用 `--notification` 参数来发送通知。这意味着 swiftDialog 应该发送通知，而不是显示对话窗口。

通知使用相同的`--title`、`--message`和`--icon`参数来显示文本和媒体。 页面上未列出的其他参数将被忽略。

还有一个额外的参数 `--subtitle`，它可以为通知添加一个字幕。

### 通知样式 (版本 3.1 及以上)

从版本 3.1 开始，swiftDialog 通过嵌入在 `Dialog.app` 中的专用辅助应用程序来处理通知。 使用 `--style` 参数来选择通知类型：

| `--style` 价值。 | 行为。 | 已使用的辅助工具。 |
|---|---|---|
| `banner` | 系统通知，短暂显示后会自动消失。 | `Dialog Banner` |
| `alert` | 系统通知，会持续显示直到用户手动关闭。 | `Dialog Alert` |
| `pseudo` | 伪通知横幅（与`pseudo-banner`相同）。 | 主要应用程序。 |
| `pseudo-banner` | 一种虚拟通知，在超时后会自动消失。 | 主要应用程序。 |
| `pseudo-alert` | 一种伪通知，它会一直显示，直到用户进行交互。 | 主要应用程序。 |

当 `--style` 未被指定时，默认值取决于为该应用程序配置的系统通知设置。

> #### 遗留路径（在3.1版本中已弃用）
>
> 拨打电话`--notification`，即使在没有`--style`的情况下，仍然有效，但会通过主模块`Dialog.app`进行路由。这种方式已被弃用，并且会向标准错误输出（stderr）发出警告。
> In a future release, sending a notification without `--style` will default to `--style banner`.

为了确保系统通知的样式设置正确，请部署一个配置文件（mobileconfig），该配置文件可以预先批准相关辅助应用程序（`au.csiro.dialog.notifier.banner` 和 `au.csiro.dialog.notifier.alert`）的通知，并设置所需的通知样式。

### 使用

发送一个简单的横幅通知：

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message"
```

发送持续的提醒通知：

```bash
dialog --notification --style alert --title "Test Notification" --message "A test notification message"
```

![图片](https://user-images.githubusercontent.com/3598965/201508706-be8fd3c5-5f06-434c-b97b-b773f6b96bdb.png)

如果消息内容超过通知栏显示的长度，消息会被截断，并显示省略号 `...`，以表明内容已被截断。当用户将鼠标悬停在通知上时，通知栏的右上角会显示一个箭头，允许用户展开显示完整内容。

![截图 2022-11-13 晚上 5:26:10 ](https://user-images.githubusercontent.com/3598965/201508943-f382a961-9a8e-4bc6-98a3-67925d367005.png)

![截图 2022-11-13 晚上 5:26:15](https://user-images.githubusercontent.com/3598965/201509015-cc6591cc-5e66-4f9f-94bb-d9c0688460e9.png)

添加字幕：

```bash
dialog --notification --style banner --title "Test Notification" --message "A test notification message" --subtitle "Test Subtitle"
```

![图片](https://user-images.githubusercontent.com/3598965/201508719-5f13f9fd-9507-4d6d-81c5-854d6ad4a79b.png)

包括标题和副标题，一个通知最多可以包含5行文本。消息体内的`\n`字符会创建换行符，从而在通知中产生新的行。

可以添加图片，使用`--icon`功能，支持所有现有的图片格式和来源。

![图片](https://user-images.githubusercontent.com/3598965/201508767-b091140f-d040-4c86-b16b-d25bcfac8606.png)

当显示图像时，用户可以展开通知的内容。

![图片](https://user-images.githubusercontent.com/3598965/201508803-29a1a02a-450f-4952-8991-9348dd754b38.png)

注意：您__不能__替换默认显示的通知图标。使用`--icon`添加的图像将显示在通知中。

## 设置一个动作

您可以设置一个操作，当用户点击通知时，该操作将被执行。这个操作可以是网址链接，也可以是 shell 命令。

注意：通知是由用户发起的，因此通知执行的任何操作都发生在用户所处的上下文中。

这个功能的常见用途是：

```bash
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "open -a Safari.app"
dialog --notification --style banner --title "<text>" --message "<text>" --button1action "https://swiftdialog.app/"
```

您可以指定一个额外的操作，并定义按钮的标签。

```bash
dialog --notification --style banner --title "<text>" --message "<text>" \
    --button1text "Do Something" --button1action "/do/something" \
    --button2text "Do Something Else" --button2action "/do/something/else/"
```

`--button1action` 是默认的操作，当点击通知内容或按钮1时会触发。 `--button2action` 仅在点击按钮2时才会触发。

## 通知标识符和移除方法

你可以使用`--identifier`为通知分配一个永久标识符。这让你可以在以后删除特定的通知：

```bash
# Send a notification with an identifier
dialog --notification --style banner --title "Update Available" --message "Version 2.0 is ready" --identifier "update-available"

# Remove it later
dialog --notification --style banner --remove --identifier "update-available"
```

调用 `--remove` 函数而不传递 `--identifier` 参数，会清除该辅助程序的所有待处理通知。

标识符也适用于伪通知（请参见下文）。

## 启用通知声音

使用 `--enablenotificationsounds` 可以在接收到通知时播放默认的通知声音。

```bash
dialog --notification --style alert --title "Alert" --message "Action required" --enablenotificationsounds
```

## 虚假通知

“伪通知”是 swiftDialog 本身渲染的、具有通知窗口风格的界面元素，而不是 macOS 系统通知。它们从屏幕右边缘滑入，并模仿原生通知的外观，采用半透明的背景材质。

### 为什么使用伪通知？

- **自定义图标支持** — 可以在通知中显示的图标是完全可定制的，可以使用`--icon`进行设置，包括SF Symbols、URL、文件路径和应用程序包。与系统通知不同，这不需要设置 Dialog.app 的图标，也不需要重启 NotificationCenter。
- **无需 MDM 配置文件** — 伪通知不会经过 macOS 的通知中心，因此不需要任何 mobileconfig 文件或通知权限。
- **内联图片** — 使用 `--image` 来在通知正文中显示图片。
- **行内 Markdown** — `--message` 内容支持行内 Markdown 格式。

### 什么是“伪通知”？（或者说，哪些东西不是“伪通知”）

“伪通知”不是系统通知。一旦被关闭，它们不会保留，并且不遵循macOS系统通知的标准规则。它们也不会堆叠显示。虽然可以发送多个“伪通知”，但它们会重叠显示，直到被关闭。如果您认为这一点很重要，请使用标准的系统通知。



### 伪造的通知样式

| `--style` 价值。 | 行为。 |
|---|---|
| `pseudo` | 与 `pseudo-banner` 相同。 |
| `pseudo-banner` | 自动消失，持续时间为6秒（或为`--timer`所设定的值）。 |
| `pseudo-alert` | 该界面会一直显示在屏幕上，直到用户点击关闭或手动关闭它。 |

### 基本用法

<img width="400" alt="image" src="/images/update-available.png" />

```bash
# Banner-style pseudo notification (auto-dismisses)
dialog --notification --style pseudo --title "Update Available" --message "Version 2.0 is ready to install"

# Alert-style pseudo notification (persistent)
dialog --notification --style pseudo-alert --title "Restart Required" --message "Please save your work and restart"
```

### 自定义图标和图像

<img width="400" alt="image" src="/images/deployment-install-complete.png" />

```bash
dialog --notification --style pseudo --title "Deployment" --message "Software install complete" \
    --icon /System/Applications/App\ Store.app  \
    --image "/Applications/Keynote.app"
```

### 操作按钮

当`--button2text`或`--button2action`被指定时，一个操作栏会出现在通知的底部，其中包含两个按钮。

<img width="400" alt="image" src="/images/update-available-buttons.png" />

```bash
dialog --notification --style pseudo-alert --title "Update Available" \
    --message "macOS 26.4 is ready to install" \
    --button1text "Later" \
    --button2text "Install Now" --button2action "open 'x-apple.systempreferences:com.apple.Software-Update-Settings.extension'"
```

- 点击通知内容区域或“按钮 1”将执行 `--button1action`。
- 点击“按钮 2”会执行`--button2action`。
- 如果既未指定`--button2text`，也未指定`--button2action`，则操作栏会被隐藏，并且在通知区域的任何位置点击都会触发`--button1action`。

### 自动关闭定时器

对于`pseudo-banner`风格的通知，默认情况下会在6秒后自动消失。可以使用`--timer`来设置自定义的持续时间（以秒为单位）：

```bash
# Auto-dismiss after 15 seconds
dialog --notification --style pseudo-banner --title "Reminder" --message "Meeting in 5 minutes" --timer 15
```

### 关闭按钮

<img width="400" alt="image" src="/images/restart-hover-button.png" />

当用户将鼠标悬停在模拟通知上时，一个关闭按钮（×）会出现在左上角。点击该按钮会关闭通知，其行为方式与超时的情况相同（滑动消失，以代码0退出，不执行任何按钮操作）。

### 实时时间戳

伪通知会在标题旁边显示一个“现在”的时间戳。 60秒后，该时间戳会更新为“1分钟前”，并且每隔60秒会继续更新，直到通知消失。

### 标识符和移除操作

伪通知支持针对性地进行移除操作 `--identifier`。

```bash
# Send a pseudo notification with an identifier
dialog --notification --style pseudo-alert --title "Updating" --message "Please wait..." --identifier "update-progress"

# Remove it when done
dialog --notification --style pseudo --remove --identifier "update-progress"

# Remove ALL visible pseudo notifications
dialog --notification --style pseudo --remove
```

当发送一个新的伪通知，且其标识符与已存在的通知相同，系统会自动取消旧通知，然后再显示新的通知。

### 通知声音

使用 `--enablenotificationsounds` 可以在出现伪通知时播放系统警报声音。

```bash
dialog --notification --style pseudo --title "Alert" --message "Something happened" --enablenotificationsounds
```

## 通过移动设备管理 (MDM) 系统，可以批准和设置通知类型

首次使用通知功能时，您可能不会收到任何反馈，也可能不会被提示允许接收通知。

要手动允许通知，您需要进入“系统设置”->“通知”，并为相应的应用程序启用通知。 您还可以选择“无”、“横幅”或“提醒”等通知方式。

在通过移动设备管理系统（MDM）部署 swiftDialog 时，建议部署一个配置文件（mobileconfig），该配置文件可以预先批准通知，并设置通知类型。

### 应用包标识符

| 版本。 | 应用包标识符。 | 注释。 |
|---|---|---|
| 版本 2.2.1 及更早版本。 | `au.bartreardon.dialog` | 遗产；传承。 |
| v2.3 – v3.0 | `au.csiro.dialog` | 主要应用包。 |
| 版本 3.1 及以上版本（横幅样式）。 | `au.csiro.dialog.notifier.banner` | `Dialog Banner` 助手；帮手 |
| 版本 3.1 及更高版本（警示样式）。 | `au.csiro.dialog.notifier.alert` | `Dialog Alert` 助手；帮手 |

> 要确认已安装版本的确切包标识符，请执行以下操作：
> ```bash
> 读取位于 "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Banner.app/Contents/Info.plist" 文件的 CFBundleIdentifier 属性。
> 读取位于 "/Library/Application Support/Dialog/Dialog.app/Contents/Helpers/Dialog Alert.app/Contents/Info.plist" 文件的 "CFBundleIdentifier" 属性值。
> ```

如果您使用的是混合安装方式，可以在同一个配置文件中包含多个捆绑包条目。一个用于横幅式通知的示例数据包可能如下所示：

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

请注意，`AlertType` 键可以独立于 `--style` 控制通知的显示方式。
- `1` = 横幅广告（自动关闭）。
- `2` = 警告（持续显示，直到用户手动关闭）。

在使用 `--style alert` 时，请在 `au.csiro.dialog.notifier.alert` 字段中将 `AlertType` 设置为 `2`，反之亦然，这适用于横幅广告。

 > #### 关于通知错误的说明
 >
 > 如果您收到了以下内容：
 >
 > ```
 > 无法显示通知：无法与辅助应用程序进行通信。
 > ```
 >
 > 请确认相关的 Dialog 应用程序在系统设置中已启用通知功能。这可以通过以下两种方式实现：一是通过移动设备管理 (MDM) 系统应用上述的 .mobileconfig 文件；二是手动在系统设置中启用通知。

## 更新默认通知图标

通知将使用默认的 swiftDialog 图标。 如果您希望更改图标，例如使用公司标识，您可以按照以下步骤更新应用程序包的图标，以便使用更适合您需求的图标。

> #### 支持 macOS 26.4 及更高版本。
>
> 在macOS 26.4版本中，更新应用程序包的图标，以及由此带来的通知图标，已不再能正常工作。如果品牌形象非常重要，可以使用新的“伪通知”功能，它提供类似于系统通知的用户界面，但未使用macOS的系统通知机制，因此可能不适用于所有情况。

### 先决条件

 - 最新版的 swiftDialog 包。
 - 请提供一个合适的替换图片，其尺寸至少为 512x512 像素（建议使用 1024x1024 像素）。

 <img src="https://user-images.githubusercontent.com/3598965/201548460-042b057f-3174-407e-ae42-0916c0a57cee.png" width="500" />

 - #### 生成图像

   您可以使用 `sips` 命令，从您的移动设备管理 (MDM) 供应商的自助服务应用程序中生成图像。例如：

    ##### 坎吉 (Kandji)

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

### 步骤

  1. 将您替换的图标图像复制到 `/Library/Application Support/Dialog/Dialog.png` 目录中（注意大小写）。
  2. 从安装程序中安装 swiftDialog。`.pkg`

安装完成后，程序会将内置的图标替换为指定的图像。 之后，通知将使用该自定义图像作为通知图标。 `Dialog.png`

 ![截图 2022-11-14 上午 9:55 ](https://user-images.githubusercontent.com/3598965/201548926-669bc9e0-8257-4bb1-ac1f-0e23ff82f378.png)
