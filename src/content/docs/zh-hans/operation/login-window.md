---
title: 登录窗口
description: 在 macOS 登录窗口中使用 swiftDialog 对话框
translationSynced: 2026-11-25T05:49:27+00:00
---

## 登录窗口支持（从版本2.5.0开始）

`--loginwindow`

在 swiftDialog 2.5 版本中，您可以在登录窗口中运行对话框。

支持标准对话模式，可以选择是否包含`--blurscreen`。

## 要求

为了在登录窗口的环境下运行，您需要进行以下设置：

 - 一个脚本，用于以您想要的配置方式启动 swiftDialog。
   - 包含该论点 `--loginwindow`。
 - 一个启动代理。

### LaunchAgent 配置设置

#### 手动配置

以下是一个基本 LaunchAgent 的示例：

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

根据实际情况，为该文件起一个合适的名称，例如`com.swiftDialog.example-login-window.plist`，然后将其安装到`/Library/LaunchAgents/`。

#### 使用 Outset

Macadmins 开源工具 [Outset](https://github.com/macadmins/outset/)) 具有在登录窗口运行程序的实用功能。

除了简化流程之外，您还可以获得一些控制选项，以防止用户禁用登录项。 更多详情请参见 [Outset 维基百科](https://github.com/macadmins/outset/wiki/Deployment#login-items-management))。

将您的脚本放置在 `/usr/local/outset/login-window/` 目录中，并设置权限为 `root:root` `0755` (`-rwxr-xr-x`)。outset 会自动在登录窗口出现时启动该脚本。

### 注意事项

您需要考虑脚本运行完毕后的情况。 如果您不希望脚本在每次出现登录窗口时都运行，那么您的脚本需要包含一些条件，使其在不需要时要么不执行任何操作，要么自动卸载自身。

### 示例用例

#### 组织的使用政策

以下是一个可接受的使用政策对话框的示例，该对话框要求用户勾选复选框，并包含来自Markdown文件（例如 [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md))）的内容，并以 `--eula` 模式显示。它会在每次显示登录窗口时都显示。

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>