---
title: Exit Codes
description: Understanding swiftDialog exit codes and return values
---

When swiftDialog closes it will return an exit code which can be used to determine what, if any, action was taken

|Exit Code|Cause|
|---------|-----|
|0|User clicked the default button (button 1)|
|2|User clicked Button 2|
|3|User clicked the Info button|
|5|exited via the command file `quit:` command|
|10|exited because the user used `cmd+q` (or cmd+quitkey)|
|20|quit because `--timer` reached 0|
|201|an image resource was not found|
|202|a file resource was not found|
|203|an invalid colour value was used|

More details on this page: [Capturing Dialog output for further processing](/operation/capturing-output)