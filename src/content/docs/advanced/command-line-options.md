---
title: Command Line Options
description: Complete reference for all swiftDialog command line options and arguments
---

Dialog is configurable through command line options. All options can also be specified using [JSON configuration](/advanced/json-configuration).

```sh
dialog --title "Hello" --message "World"
```

Use `--help <option>` for detailed information about a specific argument.

---

## Content

| Argument | Short | Description |
|---|---|---|
| `--title <text>` | `-t` | Set the dialog title. Use `none` to hide. |
| `--subtitle <text>` | | Secondary line of text displayed below the title. Also used as subtitle text for [notifications](/advanced/notifications). |
| `--message <text>` | `-m` | Set the dialog message. Supports [Markdown](/basic-use/markdown). |
| `--messagealignment [left\|centre\|right]` | | Horizontal alignment of the message |
| `--messageposition [top\|centre\|bottom]` | | Vertical position of the message content block |
| `--titlefont <params>` | | Modify title font. Accepts comma-separated `key=value` pairs: `colour`, `size`, `weight`, `name`, `alignment`, `offset`, `shadow` |
| `--messagefont <params>` | | Modify message font (color, size) |

See [Title](/basic-use/title) and [Message](/basic-use/message) for details.

---

## Icon

| Argument | Short | Description |
|---|---|---|
| `--icon <file\|url>` | `-i` | Set the dialog icon. Accepts file path, URL, SF Symbol (`SF=name`), or `info\|caution\|warning` |
| `--iconsize <num>` | | Icon size in points (default: 150) |
| `--iconalpha <num>` | | Icon opacity from 0.0 (transparent) to 1.0 (opaque) |
| `--iconalttext <text>` | | Accessibility label for the icon |
| `--overlayicon <file\|url>` | `-y` | Overlay image displayed at bottom-right of icon |
| `--hideicon` | `-h` | Hide the icon to increase message area |
| `--centreicon` / `--centericon` | | Reposition icon to centre between title and message |

See [Icon](/basic-use/icon) for details.

---

## Banner & Background

| Argument | Short | Description |
|---|---|---|
| `--bannerimage <file\|url>` | `-n` | Display a banner image at the top of the dialog |
| `--bannertitle <text>` | | Display title text overlaid on the banner |
| `--bannertext <text>` | | Equivalent to setting `--bannertitle` and `--title` |
| `--bannerheight <num>` | | Set the banner height |
| `--background <file>` | `-bg` | Set a background/watermark image |
| `--bgalpha <num>` | `-ba` | Background image opacity (default: 0.5) |
| `--bgposition <position>` | `-bp` | Background image position (e.g. `center`, `topleft`) |
| `--bgfill [fill\|fit]` | `-bf` | Background image fill mode |
| `--bgscale [fill\|fit]` | `-bs` | Background image scale mode |

See [Banner Images](/advanced/banner-images) and [Background Images](/advanced/background-images) for details.

---

## Buttons

| Argument | Short | Description |
|---|---|---|
| `--button1text <text>` | | Label for Button 1 (bound to Return ↵, default: `OK`) |
| `--button1action <url>` | | URL to open when Button 1 is clicked |
| `--button1shellaction <cmd>` | | Shell command to run when Button 1 is clicked |
| `--button1symbol <sf symbol>` | | SF Symbol to display on Button 1 |
| `--button1disabled` | | Launch with Button 1 disabled |
| `--button2` | `-2` | Show Button 2 |
| `--button2text <text>` | | Label for Button 2 (bound to Esc ⎋, default: `Cancel`) |
| `--button2symbol <sf symbol>` | | SF Symbol to display on Button 2 |
| `--button2disabled` | | Launch with Button 2 disabled |
| `--infobutton` | `-3` | Show the info button |
| `--infobuttontext <text>` | | Label for the info button |
| `--infobuttonaction <url>` | | URL to open when the info button is clicked |
| `--infobuttonsymbol <sf symbol>` | | SF Symbol to display on the info button |
| `--buttonstyle [center\|stack]` | | Button layout style |
| `--buttonsize [mini\|small\|regular\|large]` | | Button size |
| `--buttontextsize <num>` | | Button label font size |
| `--quitoninfo` | | Quit dialog when info button is selected |

See [Buttons](/basic-use/buttons) for details.

---

## Help Message

| Argument | Short | Description |
|---|---|---|
| `--helpmessage <text>` | | Show a help button with popover content. Supports Markdown. |
| `--helpimage <file\|url>` | | Add an image to the help popover |
| `--helpsheetbuttontext <text>` | | Label for the help sheet dismiss button (default: `OK`) |
| `--helpalignment [left\|centre\|right]` | | Alignment of help message content |

See [Help Message](/operation/help-message) for details.

---

## Images, Video & Web Content

| Argument | Short | Description |
|---|---|---|
| `--image <file\|url>` | `-g` | Display an image. Multiple instances create a carousel. |
| `--imagecaption <text>` | | Caption displayed below the image |
| `--video <file\|url>` | | Display a video. Supports `youtube=<id>` and `vimeo=<id>` shortcuts. |
| `--videocaption <text>` | | Caption displayed below the video |
| `--autoplay` | | Autoplay video on launch |
| `--webcontent <url>` | | Display a web page in the message area |

See [Images](/basic-use/images), [Video](/basic-use/video), and [Web Content](/basic-use/web-content) for details.

---

## Info Area

| Argument | Short | Description |
|---|---|---|
| `--infotext <text>` | | Replace the info button with static text |
| `--infobox <text>` | | Display text (Markdown supported) below the icon |

See [Info Box](/advanced/info-box) for details.

---

## User Input

| Argument | Short | Description |
|---|---|---|
| `--textfield <text>[,options]` | | Add a text input field. Supports `required`, `secure`, `prompt`, `regex`, `fileselect` and more. |
| `--textfieldlivevalidation` | | Show live regex validation feedback on text fields |
| `--checkbox <text>` | | Add a checkbox with the given label |
| `--checkboxstyle [checkbox\|switch][,size]` | | Change checkbox appearance |
| `--selecttitle <text>[,options]` | | Add a dropdown select list with the given name |
| `--selectvalues <csv>` | | Comma-separated values for the select list |
| `--selectdefault <text>` | | Default selected value for the select list |
| `--selectstyle` | | Style for the select list |

See [Text Fields](/advanced/textfields), [Checkboxes](/advanced/checkboxes), and [Select Lists](/advanced/select-lists) for details.

---

## Item Lists

| Argument | Short | Description |
|---|---|---|
| `--listitem <text>` | | Add a list item. Supports status icons and click actions. |
| `--liststyle [expanded\|compact]` | | Vertical spacing between list rows |
| `--enablelistselect` | | Allow list items to be selected; selection is returned on exit |

See [Item Lists](/advanced/item-lists) for details.

---

## Timer & Progress

| Argument | Short | Description |
|---|---|---|
| `--timer [<seconds>]` | | Show a countdown timer (default: 10s). Exits with code 4 on timeout. |
| `--hidetimerbar` | | Hide the timer bar while still counting down |
| `--hidetimer` | | Hide the timer completely |
| `--progress [<int>]` | | Show a progress bar with the specified number of steps |
| `--progresstext <text>` | | Initial text shown below the progress bar |

See [Timer & Progress](/advanced/timer-progress) for details.

---

## Window Size & Position

| Argument | Short | Description |
|---|---|---|
| `--width <num>` | | Dialog window width in points |
| `--height <num>` | | Dialog window height in points |
| `--small` | `-s` | Decrease default window size by 25% |
| `--big` | `-b` | Increase default window size by 25% |
| `--position <position>` | | Window position (e.g. `center`, `topright`, or `x,y`) |
| `--positionoffset <int>` | | Edge offset when using `--position` (default: 16) |
| `--moveable` | `-o` | Allow the window to be dragged |
| `--resizable` | | Allow the window to be resized (implies `--moveable`) |
| `--ontop` | `-p` | Keep the window above all other windows |
| `--windowbuttons [close,min,max]` | | Enable window close/minimise/maximise buttons |
| `--showonallscreens` | | Show the window on all connected screens |
| `--appearance [dark\|light]` | | Override the window appearance |

See [Window Size](/advanced/window-size) and [Layout](/advanced/layout) for details.

---

## Window Style Presets

| Argument | Short | Description |
|---|---|---|
| `--style <preset>` | | Apply a preset style: `presentation`, `mini`, `centered`, `alert`, `caution`, `warning` |
| `--mini` | | Compact window showing title, icon and a two-line message |
| `--fullscreen` | `-f` | Full-screen mode (no buttons; keyboard events still work) |
| `--presentation` | | Presentation mode with progress bar and structured layout |
| `--eula` | | Display in EULA acceptance mode |
| `--blurscreen` | | Blur all screen content behind the dialog window |
| `--hideotherapps` | | Hide all other apps on launch |

See [Full Screen](/advanced/full-screen) and [Presentation](/advanced/presentation) for details.

---

## Notifications

| Argument | Short | Description |
|---|---|---|
| `--notification` | | Send a macOS system notification |
| `--identifier <text>` | `-id` | Unique identifier for the notification |
| `--remove` | | Remove the notification with the matching `--identifier` |
| `--enablenotificationsounds` | | Enable notification sounds |

See [Notifications](/advanced/notifications) for details.

---

## Sound

| Argument | Short | Description |
|---|---|---|
| `--sound <file\|url>` | | Play an audio file on launch |
| `--showsoundcontrols` | | Show playback controls (play/pause, mute, timeline) |

---

## Dock Icon

| Argument | Short | Description |
|---|---|---|
| `--showdockicon` | | Show the Dialog icon in the macOS Dock |
| `--dockicon <file\|url>` | | Show a custom image as the Dock icon (implies `--showdockicon`) |
| `--dockiconbadge <text>` | | Display a badge on the visible Dock icon |

---

## Command File

| Argument | Short | Description |
|---|---|---|
| `--commandfile [<file>]` | | Path to the command file for live dialog updates (default: `/var/tmp/dialog.log`) |
| `--displaylog <file>` | | Display the contents of a file as it is written |
| `--loghistory [<int>]` | | Pre-populate `--displaylog` with the last N lines (default: 100) |

See [Command File](/advanced/command-file) for details.

---

## JSON Input & Output

| Argument | Short | Description |
|---|---|---|
| `--jsonfile <file>` | | Load dialog configuration from a JSON file |
| `--jsonstring <text>` | | Load dialog configuration from a JSON string |
| `--json` | `-j` | Output results in JSON format |

See [JSON Configuration](/advanced/json-configuration) for details.

---

## Keyboard & Interaction

| Argument | Short | Description |
|---|---|---|
| `--quitkey <char>` | | Custom quit key (used as `⌘ + <key>`, default: `q`) |
| `--hidedefaultkeyboardaction` | | Require `⌘ + ⇧` to trigger Return/Esc keyboard actions |
| `--alwaysreturninput` | | Always return user input on exit regardless of exit code |
| `--ignorednd` | `-d` | Display dialog even when Do Not Disturb is active |
| `--vieworder <csv>` | | Override the display order of input element types |

---

## Authorization

| Argument | Short | Description |
|---|---|---|
| `--key <string>` | `-k` | Authentication key required to launch dialog |
| `--checksum <string>` | | Generate a SHA256 hash (for use with `--key`) |

See [Authorization](/operation/authorization) for details.

---

## Login Window

| Argument | Short | Description |
|---|---|---|
| `--loginwindow` | | Show the dialog at login window (requires appropriate LaunchAgent) |

See [Login Window](/operation/login-window) for details.

---

## Inspect Mode

| Argument | Short | Description |
|---|---|---|
| `--inspect-mode` | | Launch in inspect mode |
| `--inspect-config <file>` | | Specify configuration for inspect mode |
| `--inspect-schema <file>` | | Specify schema for inspect mode |
| `--schema-validate <file>` | | Validate a configuration against a schema |

See [Inspect Mode](/advanced/inspect-mode) for details.

---

## Utility & Debug

| Argument | Short | Description |
|---|---|---|
| `--version` | `-v` | Print the version string |
| `--help [<argument>]` | | Print help, or detailed help for a specific argument |
| `--licence` | `-l` | Print the license |
| `--debug [<colour>]` | | Enable debug mode with optional content boundary highlights |
| `--verbose` | `-vvv` | Enable verbose log output |
| `--listfonts` | | Print available font names |
| `--demo` | | Launch in demo mode |
| `--builder` | | Launch the construction kit UI |
| `--jh` | `-jh` | Enable jamfHelper compatibility mode |

See [Builder](/reference/builder) for details.
