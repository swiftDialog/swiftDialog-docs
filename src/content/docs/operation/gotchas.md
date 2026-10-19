---
title: Gotchas
description: Common issues and troubleshooting tips for swiftDialog
---

# Command file issues

## Insufficient permissions

If you launch swiftDialog and the command file cannot be written to, you will receive an error:

```bash
ERROR: Existing file at /var/tmp/dialog.log but couldn't clean.
ERROR: Error info: Error Domain=NSCocoaErrorDomain Code=513 "You don't have permission to save the file "dialog.log" in the folder "tmp"." UserInfo={NSFilePath=/var/tmp/dialog.log, NSUnderlyingError=0x60000320f660 {Error Domain=NSPOSIXErrorDomain Code=13 "Permission denied"}}
```

The command file should be removed or otherwise set permissions to `-rw-rw-rw` (666).

---

# swiftDialog 3.1.1 Behaviour Changes

## `--alwaysreturninput` Returns on All Quit Paths

**What changed:** From 3.1.1, `--alwaysreturninput` returns select/list/JSON results on **all** quit paths, not just button press.

**Affected quit paths:**
- Command-file quit
- Timer timeout  
- Quit key press
- Killed process

**Migration:** Scripts relying on the old behaviour (only returning on button press) may see new output. Review your parsing logic if you use `--alwaysreturninput`.

## `--ontop` Respects Dock Position

**What changed:** The `--ontop` option now respects the dock position and positions the dialog within the screen frame (not on top of the dock).

**Impact:** Dialogs will no longer cover the dock when `--ontop` is used. This reverts a deliberate decision from an earlier version.

## Date Picker Modifiers

**What changed:** The `isdate` modifier has been **deprecated** in favour of `date` and `time`.

**Migration:** Update your scripts:

```bash
# Old (deprecated)
dialog --textfield "Start Date,isdate"

# New
dialog --textfield "Start Date,date"
```

---

# Common Gotchas

## Repeatable Options as Final Argument

**Issue:** Repeatable options (`--selectvalues`, `--selecttitle`, `--textfield`, `--checkbox`, `--image`, `--listitem`, `--icon`, `--imagecaption`) used as the final argument could cause a crash.

**Status:** Fixed in 3.1.1

## Date Picker Returns No Value

**Issue:** Using `--textfield ...,isdate` returned no value because it was scaffolding that never returned values.

**Status:** Fixed in 3.1.1. Use `date` or `time` modifiers instead.

## Image Caption Command Not Working

**Issue:** Command-file `imagecaption:` had no effect because it only wrote to `appvars.imageCaptionArray` (consumed once at launch) instead of `observedData.imageArray` (reactive source).

**Status:** Fixed in 3.1.1

## Preset5 Group Headers Rendering Incorrectly

**Issue:** Deployment group headers ("Completed", "Pending Installation") rendered in wrong position or duplicated.

**Status:** Fixed in 3.1.1

## Button Bar Keyboard Action Not Working

**Issue:** `--hidedefaultkeyboardaction` was not working due to a regression in the button bar view rewrite.

**Status:** Fixed in 3.1.1