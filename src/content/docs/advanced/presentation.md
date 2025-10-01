---
title: Presentation
description: Creating presentation mode dialogs for ongoing processes and tasks
---

## Presentation Mode

`--presentation` or `--style presentation`

Presentation mode is an output only (no user input) mode of swiftDialog intended for displaying
an ongoing process or task.

Updating the display will require the use of a [command file](/advanced/command-file) and appropriate commands.

The view is split into two main content areas and a footer containing a progress bar and buttons.

## Info Area

The left 1/3 of the window contains an information area and can show _one_ of the following:

### Default

A background colour representing the users highlight colour preference.

You can optionally make the following modifiers:
 - `--infobox <text>` to display text (markdown format supported)
   - Text is centred vertically
 - `--background color=<color|hex>` to set the background colour
   - If no colour is specified, the system accent colour is used
 - `--icon <image>` to display an icon in the top left
 - `--iconsize <int>` to set the icon size.

### Image

Specify one or more `--image <image>` to fill this area with an image

Multiple images will stack as an image carousel. Include `--autoplay <sec>` to have the images rotate.

**Tips**
* Use images with portrait orientation for best results
* Images will be scaled to fill the area and cropping may occur if using multiple images with varying size ratios.

Run presentation mode with `--debug` and a recommended image size for the current window will be included in debug log output after you dismiss the dialog.

e.g.

    DEBUG: Ideal presentation sidebar image size for these window dimensions would be width:492.0, height:636.0

### Web content

Specify `--webcontent <url>` to display the contents of a html source.

**Tip**
* If using a local file, reference the file using `file:///path/to/file.html`

## Content Area

The right 2/3 of the window is dedicated to content in one of the following forms:

### Default

Any `--message <text>` in any of the supported forms.

### List

One or more --listitem <item> in any of the supported forms.

## Footer

As displaying progress and other updateable content is the primary function of presentation mode, the footer of the window is always visible and dedicated to a full width progress bar and buttons.

## Examples

**Text only content**

`dialog --presentation --infobox "<markdown>" --icon "<image>" --message "<markdown>"`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/7e5ebb1b-6fe1-4005-ab6f-47ef7396801c" width="500px">

**Web view in the info area and listitems in the content area**

`dialog --presentation --infobox "<url>" --listitem ...<items>...`

<img src="https://github.com/swiftDialog/swiftDialog/assets/3598965/db20a3b0-f683-4e7f-baf6-89ca56d9684e" width="500px">