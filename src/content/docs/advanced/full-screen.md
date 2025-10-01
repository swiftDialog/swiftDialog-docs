---
title: Full Screen
description: Creating full screen dialogs for presentations and kiosk modes
---

Taking over the entire screen is supported with the `--fullscreen` or `-f` command line options.

In this view, only banner, title, icon and message are visible. Other options can still be specified but will not be displayed, however dialog will still respond to keyboard input (escape and enter) and will exit with the appropriate exit code.

The display area will re-size to different resolutions from 1024x640 up to 5k. (Will accept donations of XDR displays for testing 6k resolutions)

Options will behave slightly differently than in non fullscreen mode:

### `--bannerimage` `-n`

Banner images are displayed centered at the top of the screen and will take up to a maximum width of 95% of the display area and a maximum height 10% of the display area. This allows for a long narrow banner image if required.

Displaying a banner also displays a horizontal line underneath, also 95% of the width of the display area.

### `--title` `-t`

The title centred at the top of the display or directly beneath a banner and will take up the full width of the display.

### `--icon` `-i`

Icon images are displayed centred underneath the title.
Standard image sources are accepted however this display does not support the icon overlay option.

### `--message` `-m`

The message area will occupy whatever screen real estate is remaining beneath the title, banner and icon. and is centred both vertically and horizontally and will take up the full width of the display.

If banner, title and icon are all used, the message area will occupy the bottom 40-50% of the display (more display area is available on larger screens). If icon and banner are omitted the bottom 60-75% of the display is used.

Each line of text in the message area is double spaced up to a maximum of 12 lines.

## Examples

These examples show how fullscreen looks on a standard 13" display with the content areas highlighted.

### Simple view with title and message only

<img width="1000" alt="Screenshot1" src="https://user-images.githubusercontent.com/3598965/114690586-306d0280-9d5a-11eb-9504-1e2d25f93711.png">


### Using up all options with added banner image and icon image

<img width="1000" alt="Screenshot2" src="https://user-images.githubusercontent.com/3598965/114690604-3531b680-9d5a-11eb-94c5-242693f6d335.png">