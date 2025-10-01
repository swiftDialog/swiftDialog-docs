---
title: Customising the Icon
description: Learn how to set and customize icons, images, and overlays in swiftDialog
---

##### Table of Contents
 - [Basic Use](#basic-use)
 - [Slightly More Advanced Use](#slightly-more-advanced-use)
 - [Built in Icons](#built-in-icons)
 - [Using SF Symbols](#using-sf-symbols)
 - [Icon Overlays](#icon-overlays)
 - [Icon Size](#icon-size-new-in-v180)
 - [Hiding the Icon](#hiding-the-icon)
 - [Setting Light or Dark mode icons](#setting-dark-or-light-icons-depending-if-the-ui-is-in-dark-mode-or-light-mode)

***


Use the `-i` or `--icon` command line option to specify what icon or image you would like in the Icon title area.

### Use:

`--icon <file | url | text= >`


## Basic Use

swiftDialog accepts images in `png` and `jpg` formats and displays the specified image in the icon display area.

Images will be resized to fit the image display area which is 170pt wide by 260pt high.

`png` is preferred however if `jpg` is specified the images will be presented with slightly rounded corners for a less harsh look.

<img src="https://user-images.githubusercontent.com/3598965/111853793-912e3880-8970-11eb-852f-3d5f7e5d2119.png" width=450>

## Slightly more advanced use
swiftDialog will accept an Application path and will use the applications icon as the image.

e.g. `--icon /Applications/Safari.app`

<img src="https://user-images.githubusercontent.com/3598965/111853901-e36f5980-8970-11eb-80e2-c3fca298627d.png" width=450>

swiftDialog will also accept a URL to an image resource.

e.g. `--icon "https://user-images.githubusercontent.com/3598965/111854068-84f6ab00-8971-11eb-935b-487f1a15b91f.png"`

<img src="https://user-images.githubusercontent.com/3598965/111854089-a5bf0080-8971-11eb-95fe-a720206bb10a.png" width=450>

## Setting icon transparancy

Use `--iconalpha` to set a transparancy value.

The range is from `0.0` (fully transparant) to `1.0` (fully opaque)

## Alternate icon (dark mode)

Use `:dark=` and specify an alternate icon or path to be used if the user's appearance is in dark mode

e.g. `--icon /path/to/light.png:dark=/path/to/dark.png`

## Built in icons

swiftDialog has several built in icons that can be used with the `--icon` option

`--icon info`

![Info Icon](https://user-images.githubusercontent.com/3598965/111854259-5e853f80-8972-11eb-9476-e2c5ceed3da9.png)

`--icon caution`

![Caution Icon](https://user-images.githubusercontent.com/3598965/111854239-46adbb80-8972-11eb-9708-e864a71e3e0a.png)

`--icon warning`

![Warning Icon](https://user-images.githubusercontent.com/3598965/111854248-52997d80-8972-11eb-9f11-52a0b8a8d650.png)

`--icon computer`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/2ee4c788-bc9a-4328-ac1b-1537bf30dcb7">

## Using `text=`

You can also use the `text=` prefix to display text in the icon area. This is useful for displaying a single character or emoji.

e.g. `--icon text=👍`

<img width="570" alt="image" src="https://github.com/swiftDialog/swiftDialog/assets/3598965/931fa9f5-0f96-4b32-bf6e-cffa28c26e31">


## Using SF Symbols

swiftDialog can also display any SF Symbol iconography https://developer.apple.com/sf-symbols/

When Specifying SF Symbols for icon or overlay icon, additional parameters for colour and weight are available:

  `"SF=sf.symbol.name,colour=<text><hex>,weight=<text>"`

  `color,colour=<text><hex>`  specified in hex format, e.g. #00A4C7
     Also accepts any of the standard Apple colours
     `black`, `blue`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `white`, `yellow`
     default if option is invalid is system `primary` colour

Special colour `"auto"`.

When used with a multicolor SF Symbol, the symbols default colour scheme will be used. If used with a monochrome SF Symbol it will default to black and will not respect dark mode.

e.g. `dialog -s -i SF=airplane.circle.fill,colour=auto`

![image](https://user-images.githubusercontent.com/3598965/126090330-8dc612a9-419c-40f9-99e2-caf41d07903e.png)

Colour gradients can be set by adding the additional `colour2` or `color2` argument e.g. `SF=applelogo,colour=pink,colour2=purple`

![image](https://user-images.githubusercontent.com/3598965/170815055-e943c2a4-e846-44d5-b323-bb8be1333438.png)

Multicolor SF Symbols can colourised using the `palette` argument, e.g. `SF=person.3.sequence.fill,palette=red,green,blue`

![image](https://user-images.githubusercontent.com/3598965/171398294-0a74dcad-b5b2-4dd0-b320-c65d5d5e8d22.png)

SF Symbol Weight can be set with the `weight` argument

  `weight=<text>` accepts any of the following values:
   * thin (default)
   * light
   * regular
   * medium
   * heavy
   * bold

### Animated SF Symbols

Support for animated SF symbols is availabe on macOS 14 or newer.

Example usage:

`--icon sf=rainbow,colour=auto,animation=variable`

Limited support at this time using the following animation types:
 - "variable":
 - "variable.reversing"
 - "variable.iterative"
 - "variable.iterative.reversing"
 - "variable.cumulative"
 - "pulse"
 - "pulse.bylayer"



## Icon Overlays

Use the `-y` or `--overlayicon ` command line option to specify what icon or image you would like as an overlay to the main icon.

Overlays are displayed at half the normal resolution and shifted to the bottom right of the main icon display area. Using this option you can combine images to display

Overlay icons take all the same image types and locations as the `--icon` parameter including built-ins and SF Symbols


Example:

`--icon caution --overlayicon /Applications/Safari.app`

`-i caution -y /Applications/Safari.app`

![caution icon with safari Overlay Icon](https://user-images.githubusercontent.com/3598965/111854381-16b2e800-8973-11eb-9cf9-c2b1d8d8b6b7.png)

Example 2:

`--icon /Applications/Google\ Chrome.app --overlayicon warning`

`-i /Applications/Google\ Chrome.app -y warning`

![Chrome Icon with warning overlay](https://user-images.githubusercontent.com/3598965/111888622-2e9d7100-8a32-11eb-9693-e53bb2f42692.png)

### Overlay Background when using SF Symbols

When using SF Symbols, a semi-transparant squircle is added to make the symbol stand out over the main icon as many symbols contain elements that don't work well as an overlay.

![image](https://user-images.githubusercontent.com/3598965/173157681-0dd05429-35db-4872-89a1-8a8e42bf44a4.png)

The background appearance can be adjusted with a `bgcolor=` modifier and uses the same syntax wherever `color` can be set. You can also specify the special colour `bgcolor=none` if the overlay background is not desired.

![image](https://user-images.githubusercontent.com/3598965/173157715-46fda24b-2cfb-417b-835a-ed452888546d.png)

## Icon Size

`--iconsize <float>` Will re-size the icon to the specified width. The default width is `170`

Example 1:

`--icon caution --overlayicon /Applications/Safari.app --iconsize 300`

![image](https://user-images.githubusercontent.com/3598965/137573508-a2eb2dfc-cf46-4009-8783-66d8e2040724.png)


Example 2:

`--icon /Applications/Firefox.app --iconsize 100 -s`

![image](https://user-images.githubusercontent.com/3598965/137573587-0e11823b-dc12-4756-ab4c-8442c4d5f050.png)

## Icon Position

`--centreicon` or `--centericon`

Changes the icon position to be centred

![image](https://user-images.githubusercontent.com/3598965/159693524-551b863d-33db-4af0-b971-a9a08161d525.png)

Can also be changed using the command file while swiftDialog is running

`echo "icon: centre" >> /var/tmp/dialog.log`

## Hiding the icon

The icon can be removed entirely with either one of the following commands:

`--hideicon`

or

`--icon none`

## Setting dark or light icons depending if the UI is in dark mode or light mode

Except for some SF Symbols, swiftDialog doesn't have any built in functionality for switching between dark and light mode icons.

Setting icon based on UI settings though can be achieved in the calling script:

**zsh / bash** (thanks to [mm2270](https://github.com/mm2270))

```bash
#!/bin/zsh

icon_path_dark="/path/to/icondark.png"
icon_path_lite="/path/to/iconlite.png"

logged_in_user=$(/usr/sbin/scutil <<< "show State:/Users/ConsoleUser" | /usr/bin/awk '/Name :/ && ! /loginwindow/ {print $3}')

os_color_mode=$(/usr/bin/defaults read /Users/$logged_in_user/Library/Preferences/.GlobalPreferences.plist AppleInterfaceStyle)

if [ "$os_color_mode" = "Dark" ]; then
	icon_path=$icon_path_dark
else
	icon_path=$icon_path_lite
fi
```

or in python (thanks to [joncrain](https://github.com/joncrain))

```python
from Foundation import NSBundle

def is_dark_mode():
    appearanceBundle = NSBundle.bundleWithPath_(
        "/System/Library/PreferencePanes/Appearance.prefPane"
    )
    appearanceShared = appearanceBundle.classNamed_("AppearanceShared")
    app = appearanceShared.sharedAppearanceAccess()
    if app.theme() == 1:
        return False
    else:
        return True

if is_dark_mode():
    content["icon"] = "dark_icon.png"
else:
    content["icon"] = "light_icon.png"
```