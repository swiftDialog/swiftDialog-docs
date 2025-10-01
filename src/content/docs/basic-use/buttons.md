---
title: Buttons and Button Behaviour
description: Learn how to configure button text, actions, and behaviour in swiftDialog
---

Dialog can display up to three buttons.

The buttons are displayed in the lower portion of the Dialog window

![Dialog Button Area](https://user-images.githubusercontent.com/3598965/111854511-b4a6b280-8973-11eb-943d-e9843a6dc0fa.png)

## Button 1 - The Default Button
By default there is a single button displayed with the label "**OK**". The default button is always present, is mapped to the **_Enter_** key and exits the Dialog app with exit code `0`

The label of the default button can be modified with an arbitrary amount of text using the `--button1text` option

e.g. `--button1text "Enter to Continue"`

![Button 1 text](https://user-images.githubusercontent.com/3598965/111854635-4f9f8c80-8974-11eb-9f3c-ddbc62880209.png)

The action can also be modified using the `--button1action` option, so in addition to simply exiting the Dialog app you can perform an action

At this stage actions are limited to opening a URL in the users default browser:

e.g. `--button1action "https://github.com/"`

## Button 2 - The Cancel Button
The second button is hidden by default. It can be invoked using the `-2` or `--button2` option which will display the button with the default label of **Cancel**"
The second button is mapped to the **_Esc_** key and exits the Dialog app with exit code `2`

The label of the second button can be modified with an arbitrary amount of text using the `--button2text` option. When using this option you do not need to invoke the `--button2` option. Display of the button is implied if you are modifying the text label.

Example:

`--button2text "I Don't Care"`

`-2 "I Don't Care"`

![Button 2 I dont care](https://user-images.githubusercontent.com/3598965/111854834-7a3e1500-8975-11eb-8b00-e77756c9a917.png)

Button 2 has no other actions implemented

## The More Information Button
The more info button is hidden by default. It can be invoked using the `-3` or `--infobutton` option which will display the button with the default label of **More Information**". Clicking the button will exit swiftDialog with an exit code of `3`

If the `--infobuttonaction` argument is present ,clicking the More Information button will only process the `--infobuttonaction` action and swiftDialog will not automatically exit. If the `--quitoninfo` argument is added, the exit behaviour will be restored.

The label of the info button can be modified with an arbitrary amount of text using the `--infobuttontext` option. When using this option you do not need to invoke the `--infobutton` option. Display of the button is implied if you are modifying the text label.

Example:

`--infobuttontext "Click here for more details"`

![Info Button text click for more details](https://user-images.githubusercontent.com/3598965/111854992-5cbd7b00-8976-11eb-9f3b-4e93c76db6f3.png)

The action can also be modified using the `--infobuttonaction` option, so in addition to simply exiting the Dialog app you can perform an action

At this stage actions are limited to opening a URL in the users default browser:

e.g. `--infobuttonaction "https://github.com/"`

## Button Position

By default Button1 and Button2 are on the right and Infobutton is on the left.

Using `--buttonstyle center` will place buttons 1 (and 2 if present) at the bottom center of the dialog window

<img width="412" alt="buttoncenter" src="https://github.com/bartreardon/swiftDialog/assets/3598965/4081016a-7c70-41a9-95e8-4f1afb08a635">

`--infobuttontext` and `--infotext` are not compatible when using the option `--buttonstyle center`

## "Stack" style for buttons

`--buttonstyle stack`

Displays button 1 and button 2 in a full width stack.

<img width="250" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/f6003ee0-a2ac-4305-8073-c8b1504ed295">

`--infobuttontext` and `--infotext` are not compatible when using the option `--buttonstyle stack`

## Behaviour of `[return]` and `[enter]` keys

With no input fields the focused input control on the dialog is `button1` and both `[enter]` and `[return]` will activate the button as it's the only interactive element on the window and thus has the default focus of the keyboard. The effect is that this closes the dialog (presuming the button is active and not disabled).

The `[return]` key always activates button1 unless an editor field has focus. The `[enter]` key only activates on the focused element (which is why it works to close the dialog on windows with no input elements)

In a single line text field, `[return]` cannot add a newline and so the default action takes over and closes the dialog (activates the default responder). In contrast, `[enter]` has no effect since it also cannot add a new line but since it has no control over the default responder action, nothing happens.

In a multi line text field (i.e. `--textfield` with `editor` enabled), the `[return]` key _can_ insert a newline and this action takes precedence over whatever default assignment it has (i.e. actioning button1 to close the window). The `[return]` key also acts as it should and inserts a new line.

### Altering the default behaviour of `[return]`, `[enter]` or `[esc]`

If you don't want the default behaviour of `[return]`, `[enter]` or `[esc]` to close the dialog, you can use the `--hidedefaultkeyboardaction` option to change the behaviour. This option will change the default `[return]` or `[escape]` keys to also require `cmd`+`shift` to activate. This helps mitigate against non-intentional dismissal of dialogs.

## Return Codes

The following return codes are sent after each action. These can be ignored or used in a calling script for further action

| Button Name | Optional | Hotkey | Return Code |
| ----------- | -------- | ------ | ----------- |
| button1     | No       | Enter  | 0           |
| button2     | Yes      | Esc    | 2           |
| infobutton  | Yes      |        | 3           |

## Disabling buttons

Button1 and Button2 can be disabled on launch using one of the following commands:

`--button1disabled`

`--button2disabled`

Button1 can be hidden completly by setting the buttontext to `none`

_Note that this also disables the use of [return] to close a dialog so be sure to have a way for the dialog to exit._