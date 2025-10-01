---
title: Shell Commands
description: Experimental feature for running shell commands from button actions
---

v1.1.2 introduces an experimental feature via the `button1shellaction` command


```
--button1shellaction <command>
                << EXPERIMENTAL >>
                Runs the specified shell command using zsh
                Command input and output is not sanitised or checked.
                If your command fails, Dialog still exits 0
```

It takes a single string parameter and passes that to a shell for execution, e.g.

` --button1shellaction "say thank you for running dialog"`

There is currently no input sanitisation or output sanitisation. If the specified command exits with an error, Dialog will still exit `0` as the exit code for button 1. A command status will be printed to the screen including the command exit code, e.g.

```
.../Dialog.app/Contents/MacOS/Dialog --button1shellaction "bad command here"
zsh:1: command not found: bad
```

Command output will be piped directly to sdtout so you can see or parse the results as required.

## Shell actions for other buttons

Button 2 and button 3 (cancel and info) will exit dialog with code 2 and 3 respectively. These exit codes can be detected and parsed so to an admin wanting to perform some action in the shell after processing either of these actions I'd recommend capturing Dialogs exit status and processing accordingly.

## Considerations

The command is not run in the background so Dialog will be visible but un-responsive while the command is executed, after which Dialog will exit. Keep this in mind if you are wanting to execute a command that may take some time to complete.

The shell command also inherits permissions of the process that called it. If Dialog is executed from root then the shell command will also have root privileges.