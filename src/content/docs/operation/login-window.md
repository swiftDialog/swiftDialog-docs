---
title: Login Window
description: Running swiftDialog dialogs in the macOS login window context
---

## Login Window Support (from v2.5.0)

`--loginwindow`

In swiftDialog 2.5 you can run dialogs in the login window.

Standard dialogs are supported, with or without `--blurscreen`

## Requirements

To run in the login window context you will need to set up the following:

 - A script that launches swiftDialog in the configuration you want
   - Include the argument `--loginwindow`
 - A LaunchAgent

### LaunchAgent Setup

#### Manual Configuration

The following is an example of a basic LaunchAgent:

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

Name this appropriately, e.g. `com.swiftDialog.example-login-window.plist` and install it to `/Library/LaunchAgents/`

#### Using Outset

The Macadmins Open Source tool [Outset](https://github.com/macadmins/outset/) has functionality for running items at the login window.

In addition to making the process easier, you also get access to controls to prevent a user from disabling login items. See the [Outset wiki](https://github.com/macadmins/outset/wiki/Deployment#login-items-management) for more details.

Place your script in the `/usr/local/outset/login-window/` directory with permissions set to `root:root` `0755` (`-rwxr-xr-x`) and outset will manage launching the script when the login window appears.

### Considerations

You will need to consider what happens after the script has run. If you do not want this to run every time the login window is presented then you will need to have conditions in your script to either perform no action or uninstall itself when it is no longer needed.

### Example Use Case

#### Organisation Acceptable Use Policy

The following is an example Acceptable Use Policy dialog that requires the checkbox to be ticked and includes content from a markdown file (example [AcceptableUsePolicy.md](https://github.com/user-attachments/files/15521093/AcceptableUsePolicy.md)) and displayed using `--eula` mode. It would be displayed every time the login window is presented.

```bash
dialog --message "/path/to/AcceptableUsePolicy.md" --height 50% --width 35% --style centred --icon sf=rectangle.and.pencil.and.ellipsis,colour=accent --title "{COMPANY-NAME} Acceptable Use" --button1disabled --checkbox "I Agree",enableButton1 --quitkey A --eula --blurscreen --loginwindow
```
<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/4139ae63-f420-439f-8aaa-152f8fcc91b9" width=500px>