---
title: Command File
description: Updating Dialog with new content dynamically using command files
---

Some dialog content can be updated on the fly after it has been launched. This is facilitated by sending commands to a command file which Dialog reads and interprets.

---

Dialog must be launched in the background to allow commands to be sent to it from the same script:

```sh
/usr/local/bin/dialog & sleep 0.1
```

The `sleep 0.1` gives Dialog 100ms to initialise before the first command is sent.

The default command file path is `/var/tmp/dialog.log`. A custom path can be set with the `--commandfile` argument:

```sh
dialog --commandfile /var/tmp/my.log
```

Send commands using:

```sh
echo "<command>: <value>" >> /var/tmp/dialog.log
```

---

## Content

| Command | Description |
|---|---|
| `title: <text>` | Update the dialog title |
| `title: none` | Hide the title area |
| `titlefont: <params>` | Update title font properties. Accepts space-separated `key=value` pairs: `size=<float>`, `weight=<value>`, `colour=<color\|hex>`, `name=<fontname>`, `shadow=<bool>` |
| `message: <text>` | Replace the message content. Supports Markdown. |
| `message: + <text>` | Append to the existing message (adds a newline before the new content) |
| `message: /path/to/file.md` | Load message content from a local Markdown file |
| `alignment: [left\|center\|right]` | Set the message text alignment |

---

## Icon

| Command | Description |
|---|---|
| `icon: <path\|url\|SF Symbol>` | Change the displayed icon |
| `icon: none` | Hide the icon |
| `icon: centre` / `icon: center` | Move the icon to the centre position |
| `icon: left` / `icon: default` | Move the icon back to the default left position |
| `icon: size: <num>` | Change the icon size |
| `iconalpha: <float>` | Set icon opacity (0.0 transparent → 1.0 opaque) |
| `overlayicon: <path\|url\|SF Symbol>` | Set the overlay icon |
| `overlayicon: none` | Hide the overlay icon |

---

## Banner & Background

| Command | Description |
|---|---|
| `bannerimage: <path\|url>` | Set the banner image |
| `bannerimage: none` | Remove the banner image |
| `bannertext: enable` | Show the title as banner text (sets font colour to white) |
| `bannertext: disable` | Restore default title appearance |
| `bannertext: shadow` | Enable drop shadow on banner title text |
| `bannertext: <text>` | Set the banner title text and enable banner text mode |

---

## Images & Media

| Command | Description |
|---|---|
| `image: <path\|url>` | Display an image (appends to carousel if one is already shown) |
| `image: show` | Show the current image |
| `image: hide` | Hide the current image |
| `image: clear` | Remove all images |
| `imagecaption: <text>` | Set the caption below the displayed image |
| `video: <path\|url>` | Display a video. Supports `youtube=<id>` and `vimeo=<id>` shortcuts. |
| `video: none` | Remove the video |
| `webcontent: <url>` | Load a URL in the web content area |
| `webcontent: none` | Remove the web content |

---

## Buttons

| Command | Description |
|---|---|
| `button1: enable` / `button1: show` | Enable Button 1 |
| `button1: disable` / `button1: hide` | Disable Button 1 |
| `button1text: <text>` | Update Button 1 label |
| `button2: enable` / `button2: show` | Enable Button 2 |
| `button2: disable` / `button2: hide` | Disable Button 2 |
| `button2text: <text>` | Update Button 2 label |
| `buttonsize: [mini\|small\|regular\|large]` | Set button size |
| `infobutton: <text>` | Update the info button label |
| `infotext: <text>` | Update the info text area |
| `infotext: disable` / `infotext: hide` | Hide the info text |
| `infotext: reset` / `infotext: clear` | Clear the info text value |

---

## Info Box

| Command | Description |
|---|---|
| `infobox: <text>` | Replace the info box content. Supports Markdown. |
| `infobox: + <text>` | Append to the existing info box content |
| `infobox: /path/to/file.md` | Load info box content from a local Markdown file |

---

## Progress Bar

| Command | Description |
|---|---|
| `progress: <int>` | Set the progress bar to a specific step value |
| `progress: increment` | Increment the progress bar by one step |
| `progress: increment <n>` | Increment the progress bar by `n` steps |
| `progress: complete` | Set the progress bar to maximum |
| `progress: reset` / `progress: indeterminate` | Reset the progress bar to indeterminate mode |
| `progress: show` / `progress: enable` / `progress: create` | Show the progress bar |
| `progress: hide` / `progress: disable` / `progress: delete` / `progress: remove` | Hide the progress bar |
| `progresstext: <text>` | Update the label below the progress bar |

---

## Lists

| Command | Description |
|---|---|
| `list: <csv>` | Replace the list with new comma-separated items |
| `list: clear` | Clear all list items and hide the list |
| `list: show` | Show the list |
| `list: hide` | Hide the list without clearing its contents |

### Updating List Items

Update an existing item by title (simple form):

```sh
echo "listitem: My Item: success" >> /var/tmp/dialog.log
echo "listitem: My Item: Processing..." >> /var/tmp/dialog.log
```

Update an item with full control using comma-separated properties:

```sh
echo "listitem: title: My Item, status: success, statustext: Done" >> /var/tmp/dialog.log
echo "listitem: index: 0, status: fail, statustext: Error occurred" >> /var/tmp/dialog.log
```

Add a new item to the end of the list:

```sh
echo "listitem: add:, title: New Item, status: wait, statustext: Pending" >> /var/tmp/dialog.log
```

Delete an item:

```sh
echo "listitem: title: My Item, delete:" >> /var/tmp/dialog.log
echo "listitem: index: 0, delete:" >> /var/tmp/dialog.log
```

**Available `listitem` properties:**

| Property | Description |
|---|---|
| `title: <text>` | Match item by title |
| `index: <int>` | Match item by index (0-based) |
| `subtitle: <text>` | Set the item subtitle |
| `icon: <path\|url\|SF Symbol>` | Set the item icon |
| `iconalpha: <float>` | Set item icon opacity |
| `status: <status>` | Set the status icon. One of `wait`, `success`, `fail`, `error`, `pending`, `progress`, or an SF Symbol name (optionally with a colour suffix, e.g. `lock.shield.fill-green`) |
| `statustext: <text>` | Set the status label text |
| `progress: <float>` | Set an inline progress value (displays a progress-style status) |
| `action: <url>` | URL to open when the item is clicked |
| `add:` | Add a new item to the list |
| `delete:` | Delete the matched item |

---

## Help Message

| Command | Description |
|---|---|
| `helpmessage: <text>` | Update the help message content. Supports Markdown. |

---

## Window

| Command | Description |
|---|---|
| `width: <num>` | Change the window width |
| `height: <num>` | Change the window height |
| `position: <position>` | Move the window. One of `top`, `bottom`, `left`, `right`, `centre`, or a combination (e.g. `topright`) |

---

## Window Visibility

| Command | Description |
|---|---|
| `activate:` | Bring the dialog window to the foreground |
| `show:` | Unhide the dialog window |
| `hide:` | Hide the dialog window |
| `minimize:` / `minimise:` | Minimise the dialog window to the Dock |
| `maximize:` / `maximise:` | Restore a minimised dialog window |
| `blurscreen: enable` | Enable the blur screen effect |
| `blurscreen: disable` | Disable the blur screen effect |

---

## Dock Icon

| Command | Description |
|---|---|
| `showdockicon: enable` / `showdockicon: true` / `showdockicon: 1` | Show the Dialog icon in the Dock |
| `showdockicon: <any other value>` | Hide the Dialog icon from the Dock |
| `dockicon: <file\|url>` | Set a custom image as the Dock icon |
| `dockicon: none` / `dockicon: default` | Restore the default Dialog Dock icon |
| `dockiconbadge: <text>` | Display a badge on the Dock icon |
| `dockiconbadge: none` / `dockiconbadge: remove` | Remove the Dock icon badge |
| `bounce:` | Bounce the Dock icon once (informational) |
| `bounce: critical` | Bounce the Dock icon continuously until the window is brought to the foreground |

---

## Quit

| Command | Description |
|---|---|
| `quit:` | Quit Dialog with exit code 5 |
