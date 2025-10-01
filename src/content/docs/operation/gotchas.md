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