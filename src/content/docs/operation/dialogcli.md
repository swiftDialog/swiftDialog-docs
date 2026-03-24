---
title: Dialog CLI Launcher
description: How the dialog CLI binary works and utility-level options
---

The `dialog` command available at `/usr/local/bin/dialog` is not the Dialog application itself — it is a lightweight CLI launcher (`dialogcli`) that wraps the Dialog.app binary. Understanding what it does helps when deploying or scripting with swiftDialog.

---

## What the launcher does

When you run `dialog`, the launcher:

1. **Locates the Dialog.app binary** relative to its own path inside the app bundle.
2. **Creates the command file** at `/var/tmp/dialog.log` (or the path given with `--commandfile`) if it does not already exist. If the path is a symbolic link, the launcher aborts to prevent security risks.
3. **Identifies the current GUI user** using `SCDynamicStoreCopyConsoleUser`. If no GUI user is active and `--loginwindow` is not specified, the launcher exits with code `1`.
4. **Runs Dialog in the correct user context.** When called as root (e.g. from a Jamf policy or LaunchDaemon), the launcher uses `launchctl asuser` to run Dialog as the logged-in GUI user so the window appears on the correct display session.
5. **Passes `--pid` automatically** — the launcher's own PID is injected as `--pid <pid>` so Dialog can monitor the calling process and exit if it terminates.
6. **Routes styled notifications** — when both `--notification` and `--style alert` or `--style banner` are used, the launcher forwards the call to the appropriate embedded notification helper app rather than the main Dialog binary.

---

## Creating the symlink

The launcher includes a `--link` flag that creates the `/usr/local/bin/dialog` symlink pointing to itself. This must be run as root:

```sh
sudo Dialog.app/Contents/MacOS/dialog --link
```

This is normally handled automatically by the swiftDialog installer package.

---

## Utility options

These options are handled by the Dialog binary itself and are primarily useful for administration or deployment scripts.

### `--setappicon <file>`

Sets the swiftDialog application icon to the specified image file and then exits immediately. This also updates the icons of any embedded notification helper apps.

```sh
dialog --setappicon /path/to/custom-icon.png
```

This is a one-shot operation — Dialog will not display a window. It is intended for post-install customisation so the Dock icon and notifications match your organisation's branding.

### `--callingpid <int>`

Monitors the specified process ID. If that process terminates, Dialog automatically exits with code `40`.

```sh
dialog --title "Installing..." --callingpid 12345
```

This is injected automatically by the `dialogcli` launcher (using its own PID), so Dialog will exit if the calling script or process is killed. You could supply a different PID explicitly which would tie Dialog to a different process, however this use case is not supported.

**Exit code 40** is returned when Dialog exits due to the monitored process terminating.
