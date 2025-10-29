---
title: Window Size and Behaviour
description: Controlling dialog window positioning, size, and visual appearance
---

The default behaviour of the Dialog window is to be positioned in the centre of the screen and cannot be moved. Other windows can be placed on top. You can change this behaviour with the following command line options.

Either option can be used independently of the other.

## Window Visibility

`-p` or `--ontop`

Use this option to force the dialog window to be always on top.

## Window position

`-o` or `--moveable`

Use this option to allow the window to be dragged around the screen.

`--position [topleft | left | bottomleft | top | center/centre | bottom | topright | right | bottomright]`

Positions the dialog window at the the defined location on the screen

`--positionoffset <num>`

Sets the edge offset for the window (distance from the edges of the screen to the window)

`--position <x>,<y>`

Positions the dialog window at the provided x,y co-ordinates, example `--position 100,200`

**Notes:**
 - 0,0 position is top left of the visible screen area
 - visible screen area excludes area taken up by the Dock or menu bar. For example, if the dock is positioned on the left side of the screen the origin point will be inset.


## Window Size

You can change the size to be larger or smaller than the default depending if you have more or less to say in your message or want to display different sizes on different sized displays.
Images are scaled accordingly.
Text font size remains the same.

`-b` or `--big`

This makes the window appear ~25% bigger than normal increasing the appearance of the icon display area or

![image](https://user-images.githubusercontent.com/3598965/184131775-9ec40570-8e70-47ba-aecd-5561f6b6f54d.png)

`-s` or `--small`

This makes the window appear ~25% smaller than normal

![image](https://user-images.githubusercontent.com/3598965/184131853-94255fc7-b040-4b64-812b-bbe7e9bf412b.png)

## Window Appearance

You can force either dark or light mode and it will use that appearance regardless of the users current preference

`--appearance dark` or `--appearance light`

## Mini mode

Mini mode is set passing the `--mini` argument.

Mini mode forces a small window with a modified layout and limited options for displaying content. `--title` is smaller and centered at the top of the window, or can be disabled with `--title none`. `--message` can have up to four lines of text (anything longer will be truncated). `--icon` when visible takes up the left portion of the window and all other content to the right. `--hideicon` and `--icon none` are respected. `--button1text` and `--button2text` are available but the info button is not.

![image](https://user-images.githubusercontent.com/3598965/184130942-8e0461e3-744d-4e69-89bc-6754cbd92abf.png)

If the `--progress` argument is used, the button area is removed and replaced with a progress bar and a single line of progress text. In order to dismiss the dialog, the command `quit:` must be passed to the command file.

![image](https://user-images.githubusercontent.com/3598965/184131293-efe2e2a3-2a33-42cf-b397-941d053b2693.png)

## `--style` - Configure a pre-set window style

Changes the default values to alter how a dialog is displayed.

Styles other than `--mini` have no special attributes and the visual appearance can be acheived by using the various arguments to set window properties.

`centered`, `alert` and `caution` will use the value from `--title` and add it as a heading to the message area and then disable the title. This places the title underneath the centre displayed icon.

    "mini" is functionally equavelent to --mini
    "centered" will set all the options for centered content
    "alert" sets a pre-configured dialog window 300x300 and centered content
    "caution" and "warning" are the same as "alert" with the icon configured

Example of `dialog --style alert`:

<img width="412" alt="image" src="https://github.com/bartreardon/swiftDialog/assets/3598965/53add8af-3407-4152-b374-486db664b8e9">

This is the equavelent of typing:

```bash
dialog --title none --iconsize 80 --message "### An Important Message  \n\nThis contains important message content\n\nPlease read" --messagealignment centre --buttonstyle centre --centreicon --width 300 --height 300
```

## Custom Window Sizes

Dialog can be any size you want instead of the default, `--small` or `--big` options.

`--width` and `--height` can be used to define the dialog size of choice. Content will resize to fit.

swiftDialog supports the use of `%` as a function of the current screen size, e.g. `--width 50%` will set the dialog width to 50% of the current screen resolution.

![image](https://user-images.githubusercontent.com/3598965/129476080-a708fe71-c566-4caf-8323-899e5dbdcc2b.png)

## `--blurscreen`

`--blurscreen` will overlay all displays with a blurred background and place the dialog window above all other windows. This allows for either more focused messaging or for workflows where you don't want a user interacting with other applications or the desktop (e.g. during onboarding)


<img src="https://user-images.githubusercontent.com/8291873/229149297-ab060e52-120a-42bc-8a4c-1150b7d80ca2.png" width="500">


### Behaviour of `--ontop` with `--blurscreen` and existing dialog windows

If an existing dialog is present with `--blurscreen` active, using `--ontop` will cause subsequent dialogs to appear above the blur layer. This allows for running a background dialog and launch additional dialogs and have them visible. It should be noted that if you plan to interact with these dialogs programatically, ensure you use unique command files for each.

## `--showonallscreens`

When used, the dialog window will appear on all virtual desktops

If multiple screens are in use, the dialog will appear on all virtual desktops associated with the screen it was launched on.