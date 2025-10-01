---
title: Installation
description: How to install swiftDialog on macOS
---

## Installation Methods

### Package Installer (Recommended)

The easiest way to install swiftDialog is using the **.pkg** installer from the [releases](https://github.com/swiftDialog/swiftDialog/releases) page.

The installer will place swiftDialog at `/usr/local/bin/dialog` which should be in the default `$PATH` on macOS.

### Manual Installation

If you prefer manual installation:

1. Download the latest release from the [releases page](https://github.com/swiftDialog/swiftDialog/releases)
2. Extract the binary
3. Copy it to `/usr/local/bin/dialog` or another location in your `$PATH`
4. Ensure the binary has execute permissions: `chmod +x /usr/local/bin/dialog`

### Homebrew Installation

Coming soon - Homebrew formula is under development.

## Verification

After installation, verify swiftDialog is working:

```bash
dialog --version
```

Or test with a simple dialog:

```bash
dialog --title "Test" --message "swiftDialog is installed!"
```

## Updating swiftDialog

To update swiftDialog, simply download and install the latest version. The installer will replace the existing version.

You can check for updates programmatically using:

```bash
dialog --checkupdates
```

## Uninstallation

To remove swiftDialog:

```bash
sudo rm /usr/local/bin/dialog
```

## Deployment via MDM

swiftDialog can be deployed through Mobile Device Management (MDM) solutions like Jamf Pro, Mosyle, or Kandji. Simply deploy the .pkg installer to your managed devices.

### Example Jamf Policy

1. Upload the swiftDialog .pkg to Jamf Pro
2. Create a policy to deploy the package
3. Scope to your desired devices
4. Set trigger (check-in, recurring, self-service, etc.)